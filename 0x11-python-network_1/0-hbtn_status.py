
#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/
                                status/') as resp:
        ready = resp.read()
        print('Body response:')
        print('\t- type: {}'.format(type(ready)))
        print('\t- content: {}'.format(ready))
        print('\t- utf8 content: {}'.format(ready.decode("utf-8", "replace")))

