from newsplease import NewsPlease
import pandas as pd
import json


def getArticle(json_array):
    

#csv_file_path = "/home/jeremi/Desktop/project/News Feed media Analytics /News Scrapper/Radio-Canada/links.csv"
   
# CATEGORY = "sante"

    #url = "https://montrealgazette.com/news/local-news/westmount-resident-discovers-invasive-worms-coated-in-toxic-mucus-in-garden" 
    

    data_list = []

    for json_obj in json_array:
        # Vérifier si l'élément JSON a une clé "link"
        if "link" in json_obj:
            link = json_obj["link"]
            article = NewsPlease.from_url(link)
            print(article)
        # print(index)
            print("link ",link)
        
        if article is not None:
            data = {
                "Title": article.title,
                "Description": article.description,
                "Image URL": article.image_url,
                "Main Text": article.maintext,
                "Filename": article.filename,
                "Source Domain": article.source_domain,
                "Language": article.language,
                "Authors": article.authors,
                "Date Publish": article.date_publish,
                "Date Download": article.date_download,
                "Date Modify": article.date_modify,
                "URL": link
            }

            print(data)
            data_list.append(data)
        else:
            print("Article could not be extracted for URL:", link)
    return data_list





def read_file(json_file_path):


    # Open the JSON file for reading
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)  # This parses the JSON data

    # Now 'data' contains the contents of the JSON file
    #print(data)
    return data



#def save_file()
# temp=scrape_article()

# print(temp)