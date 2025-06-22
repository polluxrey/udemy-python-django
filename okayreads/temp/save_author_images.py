import os
import json
import requests

from pathlib import Path
from bs4 import BeautifulSoup

with open('author_img_urls.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    url = item['url']

    # Fetch HTML
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the image
    div = soup.find('div', class_=["leftContainer", "authorLeftContainer"])

    if div:
        img = div.find('img')
        if img and img.has_attr('src'):
            img_url = img['src']
            print("Image src:", img_url)

            # Download the image
            img_response = requests.get(img_url)

            if img_response.status_code == 200:
                # Define save path in Downloads/book_covers
                downloads_folder = Path.home() / "Downloads" / "author_images"
                # Create folder if it doesn't exist
                downloads_folder.mkdir(parents=True, exist_ok=True)

                orig_file_name = os.path.basename(img_url)
                root, ext = os.path.splitext(orig_file_name)

                file_name = f"{item['slug']}{ext}"

                # Generate filename
                save_path = downloads_folder / file_name

                # Save the image
                with open(save_path, 'wb') as f:
                    f.write(img_response.content)

                print(f"Image saved to: {save_path}")
        else:
            print("Failed to download the image.")
    else:
        print("No img tag or src attribute found inside the div.")
else:
    print("No div with class 'authorLeftContainer' found.")
