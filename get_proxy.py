#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import telnetlib

def start():
    url = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"
    # 发送GET请求
    proxy_list = []
    response = requests.get(url)
    # 检查响应状态码
    if response.status_code == 200:
        # 获取响应内容
        data = response.text
        arr = data.split("\n")
        for s in arr:
            if len(s)>20:
                json_data = json.loads(s)
                ty = json_data['type']
                host = json_data['host']
                port = json_data['port']
                strs = ty + "://" + str(host) + ":" + str(port)
                proxy_list.append(strs)
                if verify(host,port):
                    proxy_list.append(strs)
        print(proxy_list)
    else:
        print("请求失败，状态码：" + str(response.status_code))

def verify(ip,port):
    try:
        telnet = telnetlib.Telnet(ip,port=port,timeout=3)
    except:
        return False
    else:
        return True

if __name__ == '__main__':
    start()

