import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import requests

def save_images_from_google(query, num_images=1000, save_folder='images'):
    # Create save folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Initialize Chrome options and set preferences to emulate user behavior
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without opening GUI)
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid /dev/shm usage

    # Initialize the WebDriver with Chrome options
    driver = webdriver.Chrome(options=chrome_options)  # Make sure chromedriver is in your PATH or specify its path

    # Format the Google search URL
    url = f'https://www.google.com/search/pins/?q={query}'

    # Open the URL in the WebDriver
    driver.get(url)

    # Scroll down the page to load more images
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Adjust the sleep time if needed
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Parse the HTML content
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all image elements
    img_tags = soup.find_all('img', {'src': True})

    # Counter for downloaded images
    count = 0

    # Iterate over the image tags and download the images
    for img_tag in img_tags:
        if count == num_images:
            break

        img_url = img_tag['src']

        try:
            # Send a GET request to the image URL
            img_response = requests.get(img_url)

            # Save the image
            with open(f'{save_folder}/{count+1}x.jpg', 'wb') as f:
                f.write(img_response.content)
                print(f'Saved image {count+1}')
                count += 1
        except Exception as e:
            print(f'Error downloading image {count+1}: {e}')

    # Close the WebDriver
    driver.quit()

# Example usage
save_images_from_google('Aipan Art (Uttarakhand)', num_images=5000, save_folder='Aipan Art (Uttarakhand)')