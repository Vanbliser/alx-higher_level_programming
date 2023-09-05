#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

URL=$1
curl -so /dev/null -w '%{size_download}\n' "$URL"
