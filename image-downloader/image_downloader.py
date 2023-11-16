import os 
import requests 
from bs4 import BeautifulSoup

#Function to download and save an image
def download_image(url, directory):
  response = requests.get(url, stream=True)
  if response.status_code == 200:
    with open(directory, 'wb') as file: 
      for chunk in response:
        file.write(chunk)

#Function to scrape the URLs of the images on the website
def scrape_images(url, directory):
  response = requests.get(url)
  soup = BeautifulSoup(response.txt, 'html.parser')
  images = soup.find_all('img')

  if not os.path.exists(directory):
    os.makedirs(directory)

  for image in images:
    image_url = image.get('src')
    file_name = os.path.join.(directory, image_url.split('/')[-1])
    download_image(image_url, file_name)
    scrape_images(input('Enter the complete address of the website you want to scrape images from', 'images')
