### Python `requests` Library: Basics, Real-World Examples, and Status Code Handling

The `requests` library is a popular Python library for making HTTP requests. It abstracts the complexities of making requests behind a simple API, allowing you to send HTTP/1.1 requests, without the need for manual labor. With it, you can add content like headers, form data, multipart files, and query parameters via simple Python libraries to HTTP requests.

#### Core Concepts and Objects

1. **HTTP Methods**: `GET`, `POST`, `PUT`, `DELETE`, etc. are different types of request methods in HTTP.

2. **Status Codes**: These indicate the result of the HTTP request. E.g., `200 OK`, `404 Not Found`.

3. **Response Object**: After making a request, a `Response` object is returned which contains the server's response to your request.

4. **Headers**: Additional information in the HTTP request and response. Often required for authentication and setting content types.

---

#### Example 1: Simple GET Request

```python
import requests

def fetch_todo(todo_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")

    if response.status_code == 200:
        print("Success:", response.json())
    elif response.status_code == 404:
        print("Not Found.")
    else:
        print("An error has occurred.")

if __name__ == "__main__":
    fetch_todo(1)
```

Here we are fetching a TODO item from a REST API. The `get` method sends a GET request to the specified URL, and then we check the status code to see if it was successful.

---

#### Example 2: POST Request With Data and Headers

Let's say we want to create a new TODO item.

```python
import json
import requests

def create_todo(title):
    headers = {'Content-type': 'application/json'}
    payload = json.dumps({"title": title, "userId": 1, "completed": False})

    response = requests.post("https://jsonplaceholder.typicode.com/todos", headers=headers, data=payload)

    if response.status_code == 201:
        print("Successfully created:", response.json())
    else:
        print("Failed to create todo.")

if __name__ == "__main__":
    create_todo("New Task")
```

In this example, we use the `post` method for making POST requests. We also pass headers and JSON data to the method.

---

#### Status Code Handling

The HTTP status codes indicate whether a specific HTTP request has been successfully completed or not. While `requests` does raise exceptions for entirely malformed requests, it does not raise exceptions for failed status codes. Therefore, you should always check `response.status_code` to see how the request went.

Common status codes:
- `200 OK`: The request was successful.
- `201 Created`: The request was successful and something was created.
- `400 Bad Request`: The server could not understand the request.
- `401 Unauthorized`: You are not authenticated.
- `403 Forbidden`: You are authenticated but not allowed to access.
- `404 Not Found`: The requested resource could not be found.

---

#### Best Practices:

1. Use timeouts to ensure that the request doesn't hang indefinitely.
2. Reuse the `Session` object when making multiple requests to the same server, for connection pooling.
3. Properly handle exceptions and status codes.

By adhering to best practices and understanding the core concepts, you can use the `requests` library effectively for various networking tasks.