import feedparser
import os
import json
import time
import datetime
from dateutil import parser as date_parser


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

# ... (other functions and code above)

def check_feeds():
        
        fresh_news = []
    #try:
        feed_files = [f for f in os.listdir(FEEDS_DIR) if f.endswith(".json")]
        for feed_file in feed_files:
            feed_config = load_feed_config(os.path.join(FEEDS_DIR, feed_file))
            if feed_config is None:
                continue
                           #Thu, 31 Aug 2023 21:44:54 +0000
            date_format = "%a, %d %b %Y %H:%M:%S %z"
            
            #Feed the feed parser to get the RSS json array file
            feed_url = feed_config["url"]
            feed = feedparser.parse(feed_url)
          
            
            #Logic de condition qui save dans le folder feeds the last article date 
            last_article_published = feed_config["last_article_published"]
            print(feed['entries'][0])
            print("feed['entries']")

            if feed['entries']:
                latest_article = feed['entries'][0]
                
                #print('datetime.datetime.strftime(latest_article.published')
                #print(datetime.datetime.strptime(latest_article.published, date_format))
                
                
                #datetime.datetime.strptime(latest_article.published, date_format )
                #Thu, 31 Aug 2023 18:18:19 +0000   Thu, 31 Aug 2023 21:44:54 +0000
                
                print("je rentre")
                #if in the the first position of the json array feed != the last save date last_article_published
                if latest_article.published != last_article_published:

                    print(f"New article on {feed_config['name']}: {latest_article.title}")
                    feed_config["last_article_published"] = latest_article.published
                    print("feed_config[last_article_published]",feed_config["last_article_published"])
                    feed_config["last_article_url"] = latest_article.link
                    save_feed_config(os.path.join(FEEDS_DIR, feed_file), feed_config)
                    for  entry in feed['entries']:
                        print("entry.published :",entry.published)
                        print(datetime.datetime.strptime(entry.published, date_format))
                        #print(datetime.datetime.strptime(last_article_published, date_format))
                        print(type(datetime.datetime.strptime(entry.published, date_format)))
                        #print(type(datetime.datetime.strptime(last_article_published, date_format)))
                        if datetime.datetime.strptime(entry.published, date_format) > datetime.datetime.strptime(last_article_published, date_format):
                                   feed_entries = {
                                                "date": entry.published,
                                                "title": entry.title,
                                                "link": entry.link
                                                }
                                            
                                   print(feed_entries)
                                   fresh_news.append(feed_entries)
                                   

                    #for entry in feed['entries']:
                        #print(type(datetime.datetime.strptime(entry.published, date_format)))
                        #print(datetime.datetime.strptime(last_article_published, date_format))
                    # Filter and save feed entries
                 
                       # for entry in feed['entries']
                       # if datetime.datetime.strptime(entry.published, date_format) > datetime.datetime.strptime(last_article_published, date_format)
                   # ]
                    
                    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
                    feed_entries_file_path = os.path.join('/home/jeremi/Desktop/project/News Feed media Analytics /LeDevoir/data', f"{feed_config['name']}_{timestamp}_entries.json")
                    with open(feed_entries_file_path, "w", encoding="utf-8") as entries_file:
                         json.dump(fresh_news, entries_file, ensure_ascii=False, indent=4)
                    


            else:
                print(f"No articles in the feed for {feed_config['name']}")
    #except Exception as e:
        #print(f"An error occurred while checking feeds: {e}")


def main():
    try:
        while True:
            check_feeds()
            time.sleep(400)  # Wait for 10 minutes before checking again
    except KeyboardInterrupt:
        print("Feed checker stopped.")

if __name__ == "__main__":
    main()