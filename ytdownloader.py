import os
import subprocess
import sys
from time import sleep

# Check if the required packages are installed
def check_dependencies():
    required_packages = ['pip', 'colorama', 'yt-dlp']
    missing_packages = []

    for package in required_packages:
        try:
            if package == 'pip':
                subprocess.check_call([sys.executable, '-m', 'pip', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                __import__(package)
        except ImportError:
            missing_packages.append(package)
        except subprocess.CalledProcessError:
            if package == 'pip':
                missing_packages.append(package)

    if missing_packages:
        print(f"The following packages are missing: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        for package in missing_packages:
            if package == 'pip':
                print("pip is not installed. Please install pip manually.")
                sys.exit(1)
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print("All required packages are now installed. Please re-run the script.")
        sys.exit(0)

# Check dependencies before proceeding
check_dependencies()

import yt_dlp as dlp
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

FFMPEG_LOCATION = "C:/ffmpeg/bin"  # Replace with your actual path

def download_video(url):
    options = {
        'format': 'best',
        'outtmpl': 'ytdownloads/%(title)s.%(ext)s',
        'download_archive': 'ytdownloads/downloaded.archive',
        'ffmpeg_location': FFMPEG_LOCATION
    }
    
    with dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

def download_audio(url, format, quality):
    options = {
        'format': 'bestaudio/best',
        'outtmpl': 'ytdownloads/%(title)s.%(ext)s',
        'download_archive': 'ytdownloads/downloaded.archive',
        'ffmpeg_location': FFMPEG_LOCATION,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format,
            'preferredquality': quality
        }]
    }
    
    with dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    
    print(Fore.RED + """
            $$\           $$\                                   $$\                           $$\                     
            $$ |          $$ |                                  $$ |                          $$ |                    
$$\   $$\ $$$$$$\    $$$$$$$ | $$$$$$\  $$\  $$\  $$\ $$$$$$$\  $$ | $$$$$$\   $$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\  
$$ |  $$ |\_$$  _|  $$  __$$ |$$  __$$\ $$ | $$ | $$ |$$  __$$\ $$ |$$  __$$\  \____$$\ $$  __$$ |$$  __$$\ $$  __$$\ 
$$ |  $$ |  $$ |    $$ /  $$ |$$ /  $$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$ /  $$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$$ |  \$$$$  |\$$$$$$$ |\$$$$$$  |\$$$$$\$$$$  |$$ |  $$ |$$ |\$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      
 \____$$ |   \____/  \_______| \______/  \_____\____/ \__|  \__|\__| \______/  \_______| \_______| \_______|\__|      
$$\   $$ |                                                                                                            
\$$$$$$  |                                                                                                            
 \______/                                                                                                             
 """)
    print(Fore.LIGHTYELLOW_EX + "\n                 Made by dLL44/LolTroll898/trurubn\n")
    sleep(.5)
    url = input(Fore.LIGHTGREEN_EX + "url: ")
    mode = input(Fore.LIGHTGREEN_EX + "audio or video (a/v): ")
    
    if mode == "v":
        download_video(url)
    elif mode == "a":
        format = input(Fore.LIGHTGREEN_EX + "format (e.g., ogg, mp3): ")
        quality = input(Fore.LIGHTGREEN_EX + "quality (e.g., 128, 192 (recommended), 256, 320 (highest, but massive)): ")
        download_audio(url, format, quality)
