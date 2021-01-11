# 0x11. Python - Network #1

# Learning Objectives

* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

### [0-hbtn_status.py](./0-hbtn_status.py)
Python script that fetches https://intranet.hbtn.io/status using package urllib.

### [1-hbtn_header.py](./1-hbtn_header.py)
Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response using package urllib.

### [2-post_email.py](./2-post_email.py)
Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) using packages urllib and sys.

### [3-error_code.py](./3-error_code.py)
Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8). You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code using packages urllib and sys.

### [4-hbtn_status.py](./4-hbtn_status.py)
Python script that fetches https://intranet.hbtn.io/status using package requests.

### [5-hbtn_header.py](./5-hbtn_header.py)
Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header using packages requests and sys.

### [6-post_email.py](./6-post_email.py)
Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response. The email must be sent in the variable email using packages requests and sys.

### [7-error_code.py](./7-error_code.py)
Python script that takes in a URL, sends a request to the URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code using packages requests and sys.

### [8-json_api.py](./8-json_api.py)
Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter using packages requests and sys.

### [10-my_github.py](./10-my_github.py)
Python script that takes your Github credentials (username and password) and uses the Github API to display your id  using packages requests and sys.