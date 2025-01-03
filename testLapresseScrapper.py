from newsplease import NewsPlease
article = NewsPlease.from_url('https://www.lapresse.ca/actualites/chroniques/2023-09-14/10-000-un-chiffre-rond-et-laid.php')




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
            # "URL": url
        }

print(data)