#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def start():
    """
    获取快代理上的代理
    :return: 代理列表
    """
    proxies = []
    url = 'https://www.kuaidaili.com/free/inha/1/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'table table-bordered table-striped'})
    tbody = table.find('tbody')
    trs = tbody.find_all('tr')
    for tr in trs:
        #print(".")
        tds = tr.find_all('td')
        if tds[2].text == '高匿名' and tds[3].text == 'HTTP':
            print(tds[0].text,tds[1].text,tds[2].text,tds[3].text)
            proxies.append('http://{}:{}'.format(tds[0].text, tds[1].text))
    print(proxies)

if __name__ == "__main__":
    start()
