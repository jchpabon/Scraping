"""
Collection of working proxies while avoiding duplicates for efficient and reliable 
web scraping with proxies
"""

from bs4 import BeautifulSoup
import random
import concurrent.futures
import requests
import os

def getProxies():
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies = []
    for row in table:
        if row.find_all('td')[4].text == 'elite proxy':
            proxy = ':'.join([row.find_all('td')[0].text,row.find_all('td')[1].text])
            proxies.append(proxy)
        else:
            pass
    return proxies

def proxy_from_file(filename):
    with open(filename, 'r') as f:
        txt_proxies = [line.strip() for line in f]
    return txt_proxies

def proxy_already_exists(filename, proxy):
    with open(filename, 'r') as f:
        existing_proxies = set(line.strip() for line in f)
    return proxy in existing_proxies

def write_proxy_to_file(filename, proxy):
    if not proxy_already_exists(filename, proxy):
        with open(filename, 'a') as f:
            f.write(f"{proxy}\n")

def extract(proxy):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    try:
        r = requests.get('https://shopify.com', headers = headers, proxies={'http': proxy, 'https': proxy}, timeout = 10)
        if r.status_code == 200:
            working_proxy = {
                'proxy': proxy,
                'statuscode': r.status_code,
                'data': r.text[:200]
            }
            print(working_proxy)
            save_proxy(working_proxy)
    except requests.ConnectionError:
        pass
    return proxy

def save_proxy(working_proxy):
    write_proxy_to_file('working_proxies.txt', working_proxy['proxy'])


def main():
    txt_prox = proxy_from_file('working_proxies.txt')
    proxylist = getProxies()

    for p in txt_prox:
        proxylist.append(p)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, proxylist)
    return
         
if __name__=='__main__':
    print(main())


