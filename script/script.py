import requests
import os

def download_clip(clip_url, filename):
    response = requests.get(clip_url, stream=True)
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

clip_url = input("Enter the URL of the Twitch clip: ")
filename = input("Enter the filename for the clip (with the .mp4 extension): ")
download_clip(clip_url, filename)
print("The Twitch clip has been successfully downloaded!")
