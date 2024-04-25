from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

search = input("Search For:")
param = {"p": search}
headers = {
    "User-Agent": "It's Loki."
}
r = requests.get("http://in.images.search.yahoo.com/search/images", params=param, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

links = soup.findAll('a', {"class": "img"})

# Create directory if it doesn't exist
os.makedirs("scrapped_images", exist_ok=True)

for link in links:

    image_url = link['href']
    print("Downloading image:", image_url)

    # Download the image
    img_obj = requests.get(image_url)

    # Generate a filename for the image
    title = image_url.split("/")[-1]

    # Open the image using PIL
    img = Image.open(BytesIO(img_obj.content))

    # Save the image to disk
    img.save(os.path.join("scrapped_images", title), img.format)
