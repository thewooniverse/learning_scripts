import requests
import random
import os
import time
import threading
import logging
import datetime
import pandas as pd
from threading import Thread, Lock


# check / create a xkcd dump directory
xkcd_dump_dir = f'{os.getcwd()}{os.path.sep}xkcd_dump'
if not os.path.exists(xkcd_dump_dir):
    os.mkdir(xkcd_dump_dir)

# start logging the time and create the log:
start_time = time.time()
logging.basicConfig(filename='xkcd_time.log', level=logging.INFO)

# create the initial dataframe and the directory to which we will write the log file to;
xkcd_download_logs = f'{os.getcwd()}{os.path.sep}xkcd_download_logs'
if not os.path.exists(xkcd_download_logs):
    os.mkdir(xkcd_download_logs)

df = pd.DataFrame(columns=['date_downloaded', 'date_published', 'comic_name', 'comic_num', 'file_size'])
df_lock = Lock()




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
    # set the global variable df
    global df

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
        
        
        
        
        date_published = '-'.join([data.get('day'), data.get('month'), data.get('year')])
        title = data.get('title')
        comic_num = comic_number
        file_size = os.path.getsize(f"{xkcd_dump_dir}{os.path.sep}{title}.png")
        date_downloaded = datetime.datetime.now()
        new_row_data = [date_downloaded, date_published, title, comic_num, file_size]
        with df_lock:
            df.loc[len(df)] = new_row_data


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




print(df)


# end logging the time
end_time = time.time()
elapsed_time = end_time - start_time
total_downloaded_size = df['file_size'].sum()
logging.info(f'Type: {type} to download {length} comics. Time elapsed: {elapsed_time}, total download size: {total_downloaded_size}')



# log the results:
## get the logging path based on the date today
date_today = datetime.date.today()
log_path = f'{xkcd_download_logs}{os.path.sep}{date_today}.csv'

# if the path (file for the day) doesn't exist
if os.path.exists(log_path):
    existing_df = pd.read_csv(log_path)
    new_df = pd.concat([existing_df, df], ignore_index=True)
    new_df.to_csv(log_path, index=False)

else:
    df.to_csv(log_path, index=False)

