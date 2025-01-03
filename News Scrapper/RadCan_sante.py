from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd


driver = webdriver.Chrome()


url = "https://ici.radio-canada.ca/sante/en-continu"
driver.get(url)

num_pages = 700


link_array = []


for page_num in range(num_pages):
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, "html.parser")

    link_elements = soup.select("a.content-col-text")

    # Extract and store the links
    for link_element in link_elements:
        link = link_element.get("href")
        print("Scraped link:", link)
        link_array.append({'link': link})

    # Go to the next page if there is one
    if page_num < num_pages - 1:
        next_page_button = driver.find_element(By.CSS_SELECTOR, "span.cbcrc-icon-plus")
        driver.execute_script("arguments[0].click();", next_page_button)
        time.sleep(3)  # Allow time for content to load

# Close the browser
driver.quit()

# Create a DataFrame from the link_array
df = pd.DataFrame(link_array)

# Save the DataFrame to a CSV file
csv_file_path = "links.csv"
df.to_csv(csv_file_path, index=False)

print("CSV file created:", csv_file_path)
