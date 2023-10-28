#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import socket

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
        # 创建socket对象
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置超时时间为2秒
        sock.settimeout(2)
        # 尝试连接IP和端口
        result = sock.connect_ex((ip, port))
        # 检查连接结果
        if result == 0:
            return True
        else:
            return False
        # 关闭socket连接
        sock.close()
    except socket.error as e:
        print(f"发生错误：{e}")
        return False

if __name__ == '__main__':
    start()

