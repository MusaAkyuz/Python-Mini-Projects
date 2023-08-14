
import os
import sys
import time
import socket
import asyncio
import aiofiles
import requests
import win32event
import win32service
import servicemanager
import win32serviceutil
from bs4 import BeautifulSoup
import win32api, win32con, win32gui
from wallpaper import set_wallpaper, get_wallpaper

URL = "https://apod.nasa.gov/apod/"
FOLDER = "C:\\NASA\\"
SAVE_FOLDER = FOLDER + "last_image.jpg"

def get_image_src(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.find("img").get("src")

def get_image(URL, img_src):
    response = requests.get(URL + img_src)
    return response.content

async def save_image(img, img_src):
    async with aiofiles.open(img_src, 'wb') as file:
        await file.write(img)
        
async def setWallpaper(path):
    try:
        if os.name == 'nt':
            # for some reason windows doesn't like the wallpaper module, It might just be my computer though, feel free to remove this if you're on linux or mac
            import ctypes 
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3) 
        else:
            wallpaper.change(path)
    except Exception as e:
        async with aiofiles.open("C:\\NASA\\error.txt", "w") as file:
            await file.write('Failed to upload to ftp: '+ str(e))
            
async def main():
    image_src = get_image_src(URL)
    image = get_image(URL, image_src)
    await save_image(image, SAVE_FOLDER)
    await setWallpaper(SAVE_FOLDER)             


if __name__ == '__main__':
    asyncio.run(main())