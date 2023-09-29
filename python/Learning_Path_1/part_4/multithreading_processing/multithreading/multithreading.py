import queue
import time
import threading
import requests



# code to download images / files in a multithreaded fashion -> spin this up into a randomized xkcd downloader

def download_file(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)

# URL list for demonstration purposes
urls = ["https://imgs.xkcd.com/comics/choices_part_3.jpg", "https://imgs.xkcd.com/comics/herpetology.png", "https://imgs.xkcd.com/comics/upcoming_hurricanes.png"]

threads = []
for i, url in enumerate(urls):
    thread = threading.Thread(target=download_file, args=(url, f"file{i+1}.jpg"))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Download completed.")



# join example code:
def my_function(x):
    print(f"Thread {x} starting...")
    time.sleep(2)
    print(f"Thread {x} finished.")

# Create threads
threads = [threading.Thread(target=my_function, args=(i,)) for i in range(3)]

# Start threads
for thread in threads:
    # loops through and starts each thread
    thread.start()

# Without join
print("Without join, this will print while the threads are still running.")

# Join threads
for thread in threads:
    thread.join()

print("This will only print after all threads have finished.")












def producer(q):
    for i in range(5):
        print("Producing", i)
        q.put(i)
        time.sleep(1)

def consumer(q):
    while True:
        item = q.get()
        print("Consuming", item)
        q.task_done()

my_queue = queue.Queue()

producer_thread = threading.Thread(target=producer, args=(my_queue,))
consumer_thread = threading.Thread(target=consumer, args=(my_queue,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

















"""Old code examples"""
# import threading

# def print_numbers():
#     for i in range(15):
#         print(i)

# def print_letters():
#     for letter in 'abcdefghijklmnop':
#         print(letter)

# # Create two threads
# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_letters)

# # Start the threads
# t1.start()
# t2.start()

# # Wait for both threads to complete
# t1.join()
# t2.join()

# # print('Done!')

# ## sample script 2
# counter = 0
# lock = threading.Lock()

# def increment_counter():
#     global counter
#     lock.acquire()
#     temp = counter + 1
#     counter = temp
#     lock.release()

# threads = []
# for i in range(100):
#     thread = threading.Thread(target=increment_counter)
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print("Final counter value:", counter)


