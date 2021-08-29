import requests
import argparse
from json import loads,dumps


parser = argparse.ArgumentParser(description="Instagram Video Downloader")
parser.add_argument("-u","--url",type=str,required=True,help="Instagram video link")
parser.add_argument("-o",'--output',type=str,required=True,help="Video filename")

args =parser.parse_args()

def download(url):
    filename = args.output
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return filename

def main():
    url = args.url
    
    
    if not url.startswith('http'):
        url="http://"+url
    
    if not url.endswith("/"):
        url+="/?__a=1"
    else:
        url+="?__a=1"
    


    req = requests.get(url,headers={"User-Agent":"InstaDownloader v0.1"})
    if req.text == "{}":
        print("Invalid Url!")
        exit()

    print("Video Found !")

    json = req.json()
    baseUrl = json['graphql']['shortcode_media']['video_url']
    print("Base Url Found !")

    filename = download(baseUrl)
    print(f"Saved {filename} !")
    exit(0)




main()
