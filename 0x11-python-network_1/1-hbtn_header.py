#!/usr/bin/python3
"""Python script that takes in a URL"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as req:
            print(req.getheader('X-Request-Id'))
    except (urllib.error.URLError, IndexError) as err:
        print(err)
