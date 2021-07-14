#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import time
import re
import json
import os

global openid, ua, xm, sjhm, dw, tzb, zzbh

ua = "Mozilla/5.0 (Linux; Android 9; QNDXX 666 Pro Build/PKQ1.180917.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045111 Mobile Safari/537.36 MMWEBID/3667 MicroMessenger/7.0.14.1660(0x27000E37) Process/tools NetType/4G Language/zh_CN ABI/arm64 WeChat/arm64"  # 模拟微信UA
root_url = "http://qndxx.youth54.cn"  # 根地址
nvi_url = "/SmartLA/dxxjfgl.w?method=getNewestVersionInfo"  # 获取最新大学习信息


s = requests.Session()  # 建立会话


def versions():
    r = s.post(root_url + nvi_url, data="", headers={"User-Agent": ua})
    version = r.json()['version']
    url = r.json()['url']
    return version, url


##获取截图地址，需要自行测试是否为截图，适用于大多数情况。url为sign()签到后的返回值。
def endjpg(url, v='end'):
    try:
        for i in range(len(url) - 1, -1, -1):  # 寻找最后一次出现字符'/'时的位置
            if url[i] == '/':
                break
        end_url = url[0:i] + "/images/end.jpg"  # 构建一个简单截图链接
        try:
            r = s.get(end_url, data="", headers={"User-Agent": ua})
            if r.status_code == 200:
                open('./' + v + '.jpg', 'wb').write(r.content)
                print(v + '.jpg\t' + end_url)
            else:
                print("截图链接无效，请手动获取截图！")
        except:
            print("保存失败！")
        return end_url
    except:
        return "未知错误！"


if __name__ == "__main__":
    print(time.strftime("[%Y/%m/%d %H:%M:%S]\t"), end='')
    version, url = versions()
    if version == '10-4-1':
        print("截图" + version + "需要手动获取!")
        exit(0)
    if os.path.exists('./' + version + '.jpg'):
        print("截图" + version + ".jpg已存在!")
        exit(0)
    endjpg(url, version)  # 获取最新一期截图地址