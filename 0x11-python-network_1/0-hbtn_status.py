
#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/
                                status/') as resp:
        read = resp.read()
        print('Body response:')
        print('\t- type: {}'.format(type(read)))
        print('\t- content: {}'.format(read))
        print('\t- utf8 content: {}'.format(read.decode("utf-8", "replace")))

