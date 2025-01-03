import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://montrealgazette.com/sports/tennis/roddick-leaves-roma-in-a-snit"
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
response = requests.get(url, headers=headers)
# Send an HTTP GET request to the URL


# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    # Find and print the article title
    article_title = soup.find('h1').text.strip()
    print("Article Title:", article_title)

    # Find and print the article author and date
    author_date = soup.find('p', class_='container-article__author').text.strip()
    print("Author and Date:", author_date)

    # Find and print the article content
    article_content = soup.find('div', class_='article-content').text.strip()
    print("Article Content:", article_content)

else:
    print("Failed to retrieve the webpage")

