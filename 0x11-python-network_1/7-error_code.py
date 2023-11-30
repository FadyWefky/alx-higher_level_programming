#!/usr/bin/python3
"""print content or status code on error"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        req = get(argv[1])
        if req.status_code >= 400:
            print('Error code: {}'.format(req.status_code))
        else:
            print(req.text)
    except Exception as err:
        print(err)
