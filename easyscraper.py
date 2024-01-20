import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def getArgs():
    parser = argparse.ArgumentParser(
        prog="Easy-Scraper",
        description="This will analyze the specified web page and output a list of all URLs found on it.",
    )
    parser.add_argument(
        "--url", help="URL to be parsed and analyzed. http://domain.com", required=True
    )
    return parser.parse_args()


def isValidUrl(url) -> bool:
    partes_url = urlparse(url)
    return bool(partes_url.scheme) and bool(partes_url.netloc)


def getLinks(url):
    try:
        base_domain = urlparse(url).netloc
        response = requests.get(url, allow_redirects=True)
        soup = BeautifulSoup(response.text, "html.parser")
        links = set()
        for link in soup.find_all("a", href=True):
            links.add(urljoin(url, link["href"]))
        return links
    except Exception as e:
        print(f"[-] {url}")
        print(f"[-] Error: {e}")


if __name__ == "__main__":
    args = getArgs()
    url = args.url
    if isValidUrl(url) is not True:
        print("[-] Please enter valid url. http[s]://domain.com")
        exit()
    links = getLinks(url)
    print("")
    print("")
    print(f"[+] {url}")
    for link in links:
        print(f"[+][+] {link}")
