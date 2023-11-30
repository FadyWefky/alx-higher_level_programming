#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST"""

import urllib.parse
import urllib.request
import urllib.error
import sys

try:
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode()
    with urllib.request.urlopen(sys.argv[1], data=data) as req:
        print(req.read().decode('utf8'))
except (urllib.error.URLError, IndexError) as e:
    print(e)
