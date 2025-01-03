import feedparser
import os
import json
import time

FEEDS_DIR = "feeds"

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
    try:
        feed_files = [f for f in os.listdir(FEEDS_DIR) if f.endswith(".json")]
        for feed_file in feed_files:
            feed_config = load_feed_config(os.path.join(FEEDS_DIR, feed_file))
            if feed_config is None:
                continue

            feed_url = feed_config["url"]
            last_article_published = feed_config["last_article_published"]

            feed = feedparser.parse(feed_url)

            if feed['entries']:  # Check if there are entries in the feed
                print('je rentre')
                latest_article = feed['entries'][0]
                #print(feed['entries'])
                if latest_article.published != last_article_published:
                    print(f"New article on {feed_config['name']}: {latest_article.title}")
                    feed_config["last_article_published"] = latest_article.published
                    feed_config["last_article_url"] = latest_article.link  # Add the URL of the latest article
                    save_feed_config(os.path.join(FEEDS_DIR, feed_file), feed_config)
            else:
                print(f"No articles in the feed for {feed_config['name']}")
    except Exception as e:
        print(f"An error occurred while checking feeds: {e}")

def main():
    try:
        while True:
            check_feeds()
            time.sleep(600)  # Wait for 10 minutes before checking again
    except KeyboardInterrupt:
        print("Feed checker stopped.")

if __name__ == "__main__":
    main()
