# Bash script that takes in a URL and displays all HTTP methods the server will accept.
#!/bin/bash
curl -i - -X OPTIONS $1 | grep Allow | cut -d" " -f2