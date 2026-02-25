---
title: 【0day】东胜物流软件 CrmProxyMailListHtmlGridSource.aspx SQL注入漏洞
url: https://mp.weixin.qq.com/s/aqxO7fa8Nk-Dl8LCN7EfkQ
source: Doonsec's feed
date: 2026-02-24
fetch_date: 2026-02-25T04:12:39.061723
---

# 【0day】东胜物流软件 CrmProxyMailListHtmlGridSource.aspx SQL注入漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZrTsB3aQgWDHFCicAGtZJou9vic3VIg7Eyb8Zp2I80PBwlcNMNNsphrcT1d7W2BkQB8zzLBnCb5Yl4XxYjia0ISnPWiacW5DhiaD62Wse6h1nC8o/0?wx_fmt=jpeg)

# 【0day】东胜物流软件 CrmProxyMailListHtmlGridSource.aspx SQL注入漏洞

0day收割机

![]()

在小说阅读器中沉浸阅读

# 漏洞简介

东胜物流软件是青岛东胜伟业软件有限公司一款集订单管理、仓库管理、运输管理等多种功能于一体的物流管理软件。东胜物流信息管理系统 CrmProxyMailListHtmlGridSource.aspx 接口存在SQL注入漏洞，未经身份验证的远程攻击者除了可以利用SQL 注入漏洞获取数据库中的信息（例如，管理员后台密码、站点的用户个人信息）之外，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。

# 影响版本

# fofa语法

> body="FeeCodes/CompanysAdapter.aspx" || body="dhtmlxcombo\_whp.js" || body="dongshengsoft" || body="theme/dhtmlxcombo.css"

# 漏洞复现

```
GET/PriceCarrier/CrmProxyMailListHtmlGridSource.aspx?handle=list&cur_page=1&show_page=10&TITLE=SQLI_POC HTTP/1.1
Host:
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWBoGiabomeuQFGGLHohicz7lYlP4VAmicxNItqGSlM2qnXTZjUFbtllkCzy5C50EDN9iblmSs2F04ct3HwvQRa2WxzficmDVh8icu9qw/640?wx_fmt=png&from=appmsg)

成功通过报错注入在响应中回显数据库版本信息。

仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。

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