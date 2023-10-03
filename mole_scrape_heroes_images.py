import requests
import os

url = "https://mapi.mobilelegends.com/hero/list?language=en"

# Make an HTTP request to the website
response = requests.get(url)
datas = response.json()["data"]

# Create a directory to store the images
if not os.path.exists("images"):
    os.makedirs("images")

# Get the total number of data
total_data = len(datas)

# Loop through the data in reverse order and save the images
for index, data in enumerate(reversed(datas)):
    img_url = data["key"]
    response = requests.get("https:" + img_url)
    filename = f"images/{index + 1}.jpg"
    with open(filename, "wb") as f:
        f.write(response.content)
