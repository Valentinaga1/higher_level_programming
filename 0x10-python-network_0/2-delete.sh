#!/bin/bash
#Bash script that takes in a URL, sends a DELETE request to the URL, displaying the body size
curl -s -L $1 -X DELETE
