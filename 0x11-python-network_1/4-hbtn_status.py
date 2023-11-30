#!/usr/bin/python3
"""Fetch URL using requests package"""

if __name__ == "__main__":
    from requests import get

    try:
        req = get('https://intranet.hbtn.io/status')
        print('Body response:')
        print('\t- type: {}'.format(type(req.text)))
        print('\t- content: {}'.format(req.text))
    except Exception as err:
        print(err)
