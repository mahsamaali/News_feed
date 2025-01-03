#https://medium.com/@stefentaime_10958/building-a-scalable-rss-feed-pipeline-with-apache-airflow-kafka-and-mongodb-flask-api-da379cc2e3fb


# bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic feed_topic1
# bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic feed_topic2
# Repeat for other feeds/topics

from confluent_kafka import Producer
import feedparser
import os
import json
import time

FEEDS_DIR = "feeds"

KAFKA_BROKER = "localhost:9092"  # Update with your Kafka broker address
KAFKA_TOPIC_PREFIX = "feed_topic"  # Update with your Kafka topic prefix

producer = Producer({'bootstrap.servers': KAFKA_BROKER})
def publish_to_kafka(data, feed_name):
    topic = f"{KAFKA_TOPIC_PREFIX}{feed_name}"
    producer.produce(topic, key=data['date'], value=json.dumps(data))
    producer.flush()

def load_feed_config(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error while loading feed config from {file_path}: {e}")
        return None

def save_feed_config(file_path, config):
    try:
        with open(file_path, "w") as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"Error while saving feed config to {file_path}: {e}")

def check_feeds():
    #try:
        feed_files = [f for f in os.listdir(FEEDS_DIR) if f.endswith(".json")]
        for feed_file in feed_files:
            feed_config = load_feed_config(os.path.join(FEEDS_DIR, feed_file))
            if feed_config is None:
                continue

            feed_url = feed_config["url"]
            last_article_published = feed_config["last_article_published"]

            feed = feedparser.parse(feed_url)

            if feed['entries']:
                latest_article = feed['entries'][0]
                if latest_article.published != last_article_published:
                    for entry in feed['entries']:
                        print(entry.published)
                    
                   
                
                        print(f"New article on {feed_config['name']}: {entry.title}")
                        feed_config["last_article_published"] = entry.published
                        feed_config["last_article_url"] = entry.link
                        save_feed_config(os.path.join(FEEDS_DIR, feed_file), feed_config)

                        # Save feed entries as JSON with timestamp in file name
                        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
                        feed_entries_file_path = os.path.join('/home/jeremi/Desktop/project/News Feed media Analytics /TheGazette/data', f"{feed_config['name']}_{timestamp}_entries.json")
                        with open(feed_entries_file_path, "w", encoding="utf-8") as entries_file:  # Specify UTF-8 encoding
                            entry_data = [{"date": e.published, "title": e.title, "link": e.link} for e in feed['entries'] if e.published > last_article_published]
                            json.dump(entry_data, entries_file, ensure_ascii=False, indent=4)  # Use ensure_ascii=False to keep non-ASCII characters as is
            else:
                print(f"No articles in the feed for {feed_config['name']}")
    #except Exception as e:
        #print(f"An error occurred while checking feeds: {e}")


def main():
    try:
        while True:
            check_feeds()
            time.sleep(600)  # Wait for 10 minutes before checking again
    except KeyboardInterrupt:
        print("Feed checker stopped.")

if __name__ == "__main__":
    main()