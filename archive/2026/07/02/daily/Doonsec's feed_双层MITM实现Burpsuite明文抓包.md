---
title: 双层MITM实现Burpsuite明文抓包
url: https://mp.weixin.qq.com/s/Hk-JQoHFoPzVTWODPV5JDA
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:44:46.613283
---

# 双层MITM实现Burpsuite明文抓包

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVmianNPuNQOcKshPA5vibXriabCrriadouiaREnNW0hTzsADtTMmtRKIOVnRgZltmfZlSUl1mWGzo1Jf8z1XOxXKiaVtwtcaTLBbyibRI/0?wx_fmt=jpeg)

# 双层MITM实现Burpsuite明文抓包

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 746，阅读大约需 4 分钟

## 前言

前几天，写了一篇文章

* • 请求响应包都加密时，如何用大模型分析明文数据包来挖洞 [https://mp.weixin.qq.com/s/eDadHY0Far\_cVL-md6zK3w](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247490221&idx=1&sn=27e02c7ec0d7d659f572c2276570edf9&scene=21#wechat_redirect)

里面介绍了一种方法，通过 MITM + Burpsuite + MITM 实现 Burpsuite 明文抓包的方案。

简单来说，就是风林火山……茶道……然后是风林火山。

最近做项目时，又遇到了类似的情况。该 web 应用采用的是：

* • 请求包和响应包都采用了 SM2 加密
* • 前端加密： SM2 + 公钥 加密数据
* • 前端解密： SM2 + 私钥 解密数据
* • 其中，公钥和私钥属于不同的密钥对，无法使用前端的私钥解密前端的公钥。

## 原理

中间人流程：

```
请求：
browser web 应用 ——> mitmproxy 解密 ——> Burpsuite 查看明文 ——> mitmproxy 加密 ——> 服务端

响应：
服务端 ——> mitmproxy 解密 ——> Burpsuite 查看明文 ——> mitmproxy 加密 ——> browser web 应用
```

## 演示

### 分析加解密

用 MCP chrome-devtools 让大模型分析 JS 加解密

或者将 js 下载到本地，让大模型分析

![d4052b710fe6292dbd98b2a9a8c2be72.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVko606IVBnQ5P60JxnjSeuczlgVFWL57tibnOibrJ0LlBaY3Uicknia4Q9LNj36HOib0djseQnvTliahvISIJpAnZjRic3oYogSV6TupY/640?from=appmsg "null")

d4052b710fe6292dbd98b2a9a8c2be72.png

将 Burpsuite 中抓取的数据包请求和响应保存到 markdown

```
读取 请求响应包.md ，分析 jsfiles 当中的js，分析请求响应包中的加解密方式

注意：
Windows 下，python 是 python 不是 python3
```

![8008618fe6b1000e9a47ab286a5af231.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnviaFe91ibIZuKKh6UiavhprFjia3fhVo66AMOJRVex15Jkm9ajNK8D9Eib0ic3s0f7MC1HYnaXTicCy1ssmBsKILw29wCCDKgPMIDwk/640?from=appmsg "null")

8008618fe6b1000e9a47ab286a5af231.png

同时给出了公钥和私钥保存的地址

### MITM

安装依赖

```
pip install mitmproxy
```

skills 链接见文末

```
/analyze-encrypted-web-traffic 读取 jsfiles 下的JS文件，分析加解密。
请求响应包参考：请求响应包.md

输出 mitmproxy 的脚本，要求满足如下要求

中间人流程：
请求：
browser web 应用 ——> mitmproxy 解密 ——> Burpsuite 查看明文 ——> mitmproxy 加密 ——> 服务端

响应：
服务端 ——> mitmproxy 解密 ——> Burpsuite 查看明文 ——> mitmproxy 加密 ——> browser web 应用

其中，需要生成web应用可解析使用的密钥对，通过中间人的形式，在js当中替换。
web 应用采用新生成的公钥进行加密，用新生成的私钥进行解密。
```

### 运行

browser ——》MITM ——》Burpsuite

```
set MITM_MODE=client
mitmdump -s mitmproxy_addon.py --mode upstream:http://127.0.0.1:8080 -p 8888
```

Burpsuite 配置上游代理
![02ee7592a53ccffb3008b74b69c22c19.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlMH9IYpzfJCJpDJwTAUrsY2rXk4h7nN6JRWKARW3Bw9JA42LCrfgFkxSX1lHoopyB9B5TfwMqBVJGeqt7Q8PKRqTY65sIriaao/640?from=appmsg "null")

02ee7592a53ccffb3008b74b69c22c19.png

Burpsuite ——》server

```
set MITM_MODE=server
mitmdump -s mitmproxy_addon.py -p 8889
```

### 注意

可以一股脑交给大模型，让他直接处理，给它设置一个目标。

如果大模型略差，可以分步骤进行。在生成 mitmproxy 脚本时候，可能出现不必要的错误。

执行过程中出错了，把错误复制粘贴给 AI 让它解决。

**常见的问题**

```
生成的 python 脚本中， 没有替换JS当中公钥和私钥
```

## skills

把操作的步骤写成了一个 skill，放在 github 上了。

https://github.com/boqiqibo/Sec-Skills/tree/main/analyze-encrypted-web-traffic

skills 里也差不多是上面做的思路，也可以自己看这个 skill，然后手把手指导大模型的思路，具体实现让大模型自己做。

![de7ec121c95afa30af9aeca5df0a1c5c.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlib6IapD2q4xpnhBUteOyoVTIHaKVQmDYibM2NfBEWficLsEUjXZeVT0QON2M9WCsl1ZKr36CIwJWO7MGlYL0XZKibQ9Yj4wNfa8Q/640?from=appmsg "null")

de7ec121c95afa30af9aeca5df0a1c5c.png

## 总结

实现 Burpsuite 明文抓包用，用 burp 的 mcp 会更方便，更容易分析业务逻辑漏洞

预览时标签不可点

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过