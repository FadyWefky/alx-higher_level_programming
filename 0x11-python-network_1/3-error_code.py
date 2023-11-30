#!/usr/bin/python3
"""Script that sends URL request and prints status code on error"""


if __name__ == "__main__":
    import urllib.error
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as req:
            print(req.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
