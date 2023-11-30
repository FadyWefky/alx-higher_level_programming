#!/usr/bin/python3
"""Get value of X-Request-Id header from requested URL"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        req = get(argv[1])
        print(req.headers.get('X-Request-Id'))
    except Exception as err:
        print(err)
