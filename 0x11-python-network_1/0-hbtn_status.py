#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as re:
        message = re.read()
        print("message response:")
        print("\t- type: {}".format(type(message)))
        print("\t- content: {}".format(message))
        print("\t- utf8 content: {}".format(message.decode('utf8')))
