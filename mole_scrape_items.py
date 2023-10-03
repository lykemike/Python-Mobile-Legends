import requests
from bs4 import BeautifulSoup
import os

url = "https://liquipedia.net/mobilelegends/Portal:Battle_Spells"

folder_name = "mole_hero_spells"

# Create a directory to store the images
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Make an HTTP request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all the img tags in the HTML
li_tags = soup.find_all("li", class_="gallerybox")

for li_tag in li_tags:
    img_tag = li_tag.find("img")
    img_url = img_tag["src"]
    img_response = requests.get("https://liquipedia.net/" + img_url)
    filename = os.path.join(folder_name, img_url.split("/")[-1])
    with open(filename, "wb") as f:
        f.write(img_response.content)
