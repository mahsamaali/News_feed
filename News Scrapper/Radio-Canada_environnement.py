from bs4 import BeautifulSoup
import requests
import pandas as pd 

radCanPrefix = 'https://ici.radio-canada.ca/'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

link_array = []

# Loop through URLs
for number in range(1, 501):  # Change the range as needed
    url = f"https://ici.radio-canada.ca/environnement/en-continu/{number}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the <a> tag with class bdYqnn
        target_a_tag = soup.find_all('a', class_='bdYqnn')
        
        # Extract the link from the 'href' attribute
        for l in target_a_tag:
            link = l['href']
            print("Scraped link:", link)
            link_array.append({'link': radCanPrefix + link})

# Create a DataFrame from the link_array
df = pd.DataFrame(link_array)

# Save the DataFrame to a CSV file
csv_file_path = "links.csv"
df.to_csv(csv_file_path, index=False)

print("CSV file created:", csv_file_path)
