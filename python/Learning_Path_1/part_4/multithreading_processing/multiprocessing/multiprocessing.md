
================================================================================================================================
## BASICS
================================================================================================================================

The Python `multiprocessing` module allows for the creation of parallel processes. This is particularly useful for CPU-bound tasks, where threading might be less effective due to Python's Global Interpreter Lock (GIL).

### Basic Object Classes and Functions

- `Process`: Represents a process object.
- `Queue`: Provides a simple way to send and receive messages between processes.
- `Pipe`: Another way to establish a communication channel between processes.
- `Value`: To store a ctypes object in shared memory.
- `Array`: To store an array of ctypes objects in shared memory.
- `Pool`: A process pool object, which controls a pool of worker processes for parallel execution.
- `Manager`: A manager object to manage Python objects across multiple processes.

### Basic Methods and Attributes

- `start()`: Starts the process.
- `join()`: Blocks until the process terminates.
- `is_alive()`: Checks if the process is alive.
- `terminate()`: Terminates the process.
  
### Common Use Cases with Real-World Examples

#### 1. Parallel Data Processing:

Suppose you have a large list of numbers and you want to square them.

```python
from multiprocessing import Process

def square_numbers(numbers):
    for n in numbers:
        print(n * n)

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    processes = []

    for _ in range(4):
        p = Process(target=square_numbers, args=(arr,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("Done!")
```

#### 2. Web Scraping:

In this example, you can fetch multiple web pages in parallel.

```python
from multiprocessing import Process
import requests

def fetch_page(url):
    response = requests.get(url)
    print(f"Fetched content from {url}, length: {len(response.text)}")

if __name__ == "__main__":
    urls = ['http://example.com', 'http://example.org', 'http://example.net']
    processes = []

    for url in urls:
        p = Process(target=fetch_page, args=(url,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("Done fetching pages.")
```

#### 3. Image Processing:

You have multiple images and you want to apply some filter to all of them.

```python
from multiprocessing import Process
from PIL import Image, ImageFilter

def process_image(image_name):
    img = Image.open(image_name)
    img = img.filter(ImageFilter.CONTOUR)
    img.save(f"processed_{image_name}")

if __name__ == "__main__":
    image_names = ['img1.jpg', 'img2.jpg', 'img3.jpg']
    processes = []

    for image_name in image_names:
        p = Process(target=process_image, args=(image_name,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("Done processing images.")
```

#### 4. File Operations:

Suppose you have multiple large files that you need to read, process, and write back.

```python
from multiprocessing import Process

def read_and_process_file(filename):
    with open(filename, 'r') as f:
        data = f.read()  # Read and process the file
    with open(f"processed_{filename}", 'w') as f:
        f.write(data)

if __name__ == "__main__":
    filenames = ['file1.txt', 'file2.txt', 'file3.txt']
    processes = []

    for filename in filenames:
        p = Process(target=read_and_process_file, args=(filename,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("Done processing files.")
```

In these examples, each process runs independently of the others, and since each has its own memory space, they don't interfere with each other. This is in contrast to threading, where all threads share the same memory space.










================================================================================================================================
## Multiprocessing drawbacks
================================================================================================================================
Using multiprocessing in Python is a powerful way to parallelize CPU-bound and I/O-bound operations, but there are some considerations to keep in mind:

### Memory Usage

Each new process uses its own memory space. For large data sets, this can lead to substantially increased memory usage, which can be problematic for systems with limited memory.

### Communication Overhead

Inter-process communication (IPC) is generally slower than inter-thread communication because processes do not share memory space. Data needs to be serialized and sent through IPC mechanisms, which can incur a performance penalty.

### Complexity

Writing multiprocessing code can be more complex and prone to certain kinds of bugs, such as deadlocks. Debugging multiprocessing code can also be more challenging compared to single-threaded code.

### Startup Overhead

Processes are heavier than threads and take longer to start. If you're creating many processes, the time it takes to create each one can add up.

### Platform Limitations

Multiprocessing might behave differently on different platforms (Unix vs. Windows). For example, due to the use of `fork` on Unix-based systems, the child process might inherit resources from the parent process, which might not be desired.

### GIL (Global Interpreter Lock) Still Relevant for C Extensions

While Python's GIL is bypassed when using multiprocessing, some C extensions may have their own GIL or equivalent lock mechanisms, which can still lead to performance bottlenecks.

### Not Always the Best Tool for I/O-bound Operations

For I/O-bound tasks that spend more time waiting for data from the network or disk to be available, threading or asynchronous I/O can often be more efficient. Multiprocessing is generally more useful for CPU-bound tasks that require significant computation.

### Difficulty in Sharing State

Sharing state between processes is not as straightforward as in threading and usually involves more complex data structures like pipes or queues, which can be challenging to implement and maintain.

### Limited Scalability

The number of processes is often limited by the number of cores available on the machine. On systems with a small number of cores, you might not see a significant improvement in performance.

Understanding these trade-offs can help you make an informed decision about whether or not to use multiprocessing for a given task.