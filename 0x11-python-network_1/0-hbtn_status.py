#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode(encoding='utf-8')))
