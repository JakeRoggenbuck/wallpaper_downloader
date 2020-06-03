import urllib
import requests

access_page = input("Access page name: ")
main_url = 'https://wallpaperaccess.com/'
url = f'{main_url}{access_page}'
response = urllib.request.urlopen(url)
page = response.read().decode("UTF-8")
lines = page.split("\n")

def image_download(local_filename):
    image_url = f'{main_url}{local_filename}'
    with requests.get(image_url, stream=True) as r:
        r.raise_for_status()
        save_name = local_filename.split("/")[2] 
        with open(save_name, 'wb+') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded {save_name}")

for x, line in enumerate(lines):
    if 'href="/download' in line and 'data-id' in line:
        file_name = line.split('"')[1]
        image_download(file_name)
