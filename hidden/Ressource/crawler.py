import requests
import argparse
from bs4 import BeautifulSoup

def crawl(url, rdm):
    r = requests.get(url)
    if (r.status_code != 200):
        return rdm
    print(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all('a', href=True):
        if (link['href'] != '../' and link['href'] != 'README'):
            rdm = crawl(url + link['href'], rdm)
        elif link['href'] == 'README':
            r2 = requests.get(url + 'README')
            if r2.status_code == 200:
                if r2.text not in rdm:
                    rdm.append(r2.text)
    return rdm

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("url_VM", help="the url given by the VM")
    args = parser.parse_args()
    url = args.url_VM + '.hidden/'
    rdm = list()
    rdm = crawl(url, rdm)
    print("Le flag se trouve dans une de ces strings:")
    for elem in rdm:
        print("\t-", elem, end="")
