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


proxies=getProxies()
print(proxies)