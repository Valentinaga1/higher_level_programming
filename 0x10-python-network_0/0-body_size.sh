# Bash script that takes a URL, send a request and displays the size of the body
#!/bin/bash
curl -I -s $1 | grep Content-Length | cut -d" " -f2
