import requests
import random
import os
import time
import threading
import logging


# check / create a xkcd dump directory
xkcd_dump_dir = f'{os.getcwd()}{os.path.sep}xkcd_dump'
if not os.path.exists(xkcd_dump_dir):
    os.mkdir(xkcd_dump_dir)

# start logging the time and create the log:
start_time = time.time()

logging.basicConfig(filename='xkcd_time.log', level=logging.INFO)






# Function to get latest XKCD comic number
def get_latest_comic_number():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("num")
    else:
        print("Failed to get latest comic number")
        return None

# Function to download a comic by its number
def download_comic(comic_number):
    url = f"https://xkcd.com/{comic_number}/info.0.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        img_url = data.get("img")
        title = data.get("title")
        
        # Download the image
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            img_data = img_response.content
            with open(f"{xkcd_dump_dir}{os.path.sep}{title}.png", "wb") as f:
                f.write(img_data)
            print(f"Successfully downloaded comic: {title}")
        else:
            print(f"Failed to download comic image for comic number {comic_number}")

# Main function
def download_random_comic():
    latest_comic = get_latest_comic_number()
    if latest_comic:
        random_comic = random.randint(1, latest_comic)
        print(f"Downloading comic number {random_comic}...")
        download_comic(random_comic)


type = ""
length = 10

# Multi-Threaded path
threads = []

# PATH 1 - threaded download of 25 different comics using threads
for i in range(length):
    thread = threading.Thread(target=download_random_comic)
    threads.append(thread)
    thread.start()


# print("Print here for pre-thread join")
for thread in threads:
    thread.join()
type = "Multi Threaded"

# print("Print here for POST-thread join")

"""
OUTPUT:
Print here for pre-thread join
Downloading comic number 890...
Downloading comic number 1158...
Downloading comic number 1963...
Downloading comic number 2082...
Downloading comic number 1240...
Successfully downloaded comic: Rubber Sheet
Successfully downloaded comic: Mercator Projection
Successfully downloaded comic: Quantum Mechanics
Successfully downloaded comic: Etymology
Successfully downloaded comic: Namespace Land Rush
Print here for POST-thread join
"""


# PATH 2;
# for i in range(length):
#     download_random_comic()
# type = "Single Threaded"






# end logging the time
end_time = time.time()
elapsed_time = end_time - start_time
logging.info(f'Type: {type} to download {length} comics. Time elapsed: {elapsed_time}.')



