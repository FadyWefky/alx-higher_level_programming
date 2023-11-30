#!/usr/bin/python3
"""GitHub id using github API Authentication"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        req = get('https://api.github.com/user', auth=(argv[1], argv[2]))
        j = req.json()
        print(j.get('id'))
    except ValueError as err:
        print(err)
