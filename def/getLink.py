from bs4 import BeautifulSoup
import requests

#this funtion will get the link for the each title from the txt file with webscrapping in youtube
def getLink(file):
    # Get the title of the video by the txt file
    with open (file, 'r') as file:
        title = file.read()
    # Get the link of the video by the title
    url = 'https://www.youtube.com/results?search_query=' + title
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Get the link of the video
    link = soup.find_all('a', class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ')
    # Get the first link
    link = link[0].get('href')
    # Add the link to the url
    url = 'https://www.youtube.com' + link
    return url
print(getLink('a.txt'))