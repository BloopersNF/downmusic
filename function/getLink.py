from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

def getLink(search):
    # Create a new instance of the Chrome driver
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    links = []  # Define links here

    with open(search, 'r') as file:
        titles = file.read().splitlines()

    try:
        for title in titles:
            try:
                # Go to the YouTube search results page
                driver.get('https://www.youtube.com/results?search_query=' + title)

                # Wait for the page to load
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "video-title"))
                )

                # Parse the page source with BeautifulSoup
                soup = BeautifulSoup(driver.page_source, 'html.parser')

                # Get the link of the video
                link = soup.find_all('a', id='video-title')

                # Get the first link
                video_link = 'https://www.youtube.com' + link[0]['href']

                links.append(video_link)  # Append the link to the list
            except Exception as e:
                print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()
    print(f'links found: {len(links)} [{links}]')
    return links  # Return the list of links
pass