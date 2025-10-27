---
title: SCDN 放弃 DDNS 回源 — IP 地址回源更新工具 V1.0【开源】
url: https://h4ck.org.cn/2024/12/18710
source: obaby@mars
date: 2024-12-05
fetch_date: 2025-10-06T19:36:30.212547
---

# SCDN 放弃 DDNS 回源 — IP 地址回源更新工具 V1.0【开源】

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# SCDN 放弃 DDNS 回源 — IP 地址回源更新工具 V1.0【开源】

2024年12月4日
[46 条评论](https://h4ck.org.cn/2024/12/18710#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/WechatIMG1216.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/WechatIMG1216.jpg)

前端时间家里的路由器坏了，导致一些服务挂掉了，包括自己的博客，闺蜜圈 wiki 等。然后就是每天收到各种离线消息。

终于网络恢复之后，感觉一切正常然而，通过 cdn 反问就是回源错误。于是跟技术沟通了一下下下，发现盾云的域名回源竟然存在延迟，并且这个延迟好几个小时，这就比较蛋疼了。所以，每次换了 ip 首先要去设置 ip 地址才能正常回源。

[![](https://h4ck.org.cn/wp-content/uploads/2024/12/WechatIMG780-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/12/WechatIMG780.jpg)

既然，这个东西存在延迟，那么 dnspod 的 vip 的动态 ddns 解析也就没有任何的用了，延迟已经不是动态域名的问题了，是 cdn 域名刷新的问题。

今天早上忽然想到，既然域名有延迟，那就直接 ip 地址回源吧，不过域名太多了也不能每次都改啊。直接尝试代码解决吧，下面就是全部的代码了：

```
# 盾云SCDN 接口工具
# by:obaby
# https://h4ck.org.cn
# https://oba.by
from datetime import datetime

import requests

username = '邮箱地址'
password = '密码，先设置用户邮箱地址和密码'

def login():
    url = "https://scdn.ddunyun.com/prod-api/login"

    payload = "{\"email\":\""+username+"\",\"password\":\""+password+"\"}"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://scdn.ddunyun.com',
        'priority': 'u=1, i',
        'referer': 'https://scdn.ddunyun.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.json())
    js = response.json()
    if js['code'] == 0:
        return js['data']['access_token']
    else:
        print('[E] 发生错误：', js['message'])
    return None
    # return None

def get_site_list(token):
    url = "https://scdn.ddunyun.com/prod-api/site?domain_name=&sub_domain_name=&cname=&status=&current_page=1&total=0&page_size=20"

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer ' + token,
        # 'cookie': 'LeCDN-Client=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjbGllbnQiLCJleHAiOjE3MzMyOTM5NDcsIm5iZiI6MTczMzI3MTM0NywianRpIjoiNDEifQ.lpSIjvtVGE7wcxZgNF2upZiZ8QsPh2CYajevHqgsjzg; sidebarStatus=0',
        'priority': 'u=1, i',
        'referer': 'https://scdn.ddunyun.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    js = response.json()
    if js['code'] == 0:
        return js['data']['data']
    else:
        print('[E] 发生错误：', js['message'])
    return None

def get_site_source(access_token, site_id):
    url = "https://scdn.ddunyun.com/prod-api/site_source?site_id=" + str(site_id)

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer ' + access_token,
        # 'cookie': 'LeCDN-Client=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjbGllbnQiLCJleHAiOjE3MzMyOTM5NDcsIm5iZiI6MTczMzI3MTM0NywianRpIjoiNDEifQ.lpSIjvtVGE7wcxZgNF2upZiZ8QsPh2CYajevHqgsjzg; sidebarStatus=0',
        'priority': 'u=1, i',
        'referer': 'https://scdn.ddunyun.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    js = response.json()
    if js['code'] == 0:
        return js['data']['data']
    else:
        print('[E] 发生错误：', js['message'])
    return None

def delete_source(access_token, site_id, source_id):
    # url = "https://scdn.ddunyun.com/prod-api/site_source/593?site_id=382"
    url = "https://scdn.ddunyun.com/prod-api/site_source/" + str(source_id) + "?site_id=" + str(site_id)

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer ' + access_token,
        # 'cookie': 'LeCDN-Client=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjbGllbnQiLCJleHAiOjE3MzMyOTM5NDcsIm5iZiI6MTczMzI3MTM0NywianRpIjoiNDEifQ.lpSIjvtVGE7wcxZgNF2upZiZ8QsPh2CYajevHqgsjzg; sidebarStatus=0',
        'origin': 'https://scdn.ddunyun.com',
        'priority': 'u=1, i',
        'referer': 'https://scdn.ddunyun.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    js = response.json()
    if js['code'] == 0:
        return js['data']
    else:
        print('[E] 发生错误：', js['message'])
    return None

def edit_source(access_token, site_id, source_id, ip_address):
    url = "https://scdn.ddunyun.com/prod-api/site_source/" + str(source_id)

    payload = "{\"id\":" + str(source_id) + ",\"site_id\":" + str(
        site_id) + ",\"type\":\"ipaddr\",\"content\":\"" + ip_address + "\",\"priority\":\"20\",\"weight\":15,\"created_at\":\"2024-11-25 13:21:23\",\"updated_at\":\"2024-12-01 13:39:13\",\"isEdit\":true}"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer ' + access_token,
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'LeCDN-Client=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjbGllbnQiLCJleHAiOjE3MzMyOTM5NDcsIm5iZiI6MTczMzI3MTM0NywianRpIjoiNDEifQ.lpSIjvtVGE7wcxZgNF2upZiZ8QsPh2CYajevHqgsjzg; sidebarStatus=0',
        'origin': 'https://scdn.ddunyun.com',
        'priority': 'u=1, i',
        'referer': 'https://scdn.ddunyun.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'se...