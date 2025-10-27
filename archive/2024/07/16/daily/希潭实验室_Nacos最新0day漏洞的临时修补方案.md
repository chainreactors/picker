---
title: Nacos最新0day漏洞的临时修补方案
url: https://mp.weixin.qq.com/s?__biz=MzkzMjI1NjI3Ng==&mid=2247486807&idx=1&sn=535d1e07bd4d997e2690a98a39fbdf31&chksm=c25fc22cf5284b3ab2ccb50b745ffd189dc0f75f336eb1b247068abf350c63a1dc35445d62af&scene=58&subscene=0#rd
source: 希潭实验室
date: 2024-07-16
fetch_date: 2025-10-06T17:45:06.337642
---

# Nacos最新0day漏洞的临时修补方案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450AQs2qljPrMOnY6iaURUpGJTUKcfCSuWjGhxorNhdiaJX9E4UAQ5ic4ibMfiaovTq4pn3s5scrz88IA9sw/0?wx_fmt=jpeg)

# 速报：Nacos最新0day漏洞的临时修补方案

原创

abc123info

希潭实验室

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9Lbc0INLwTJTZT1GaNutZrfDn6csvjBoS2ox0efLUEexXqPEcVbYfbLo8w/640?wx_fmt=png)

## **Part1 前言**

**大家好，我是ABC\_123**。今天下午github上有网友公布了最新的nacos远程代码执行漏洞及exp，目前官方补丁还没出来，这里ABC\_123给大家提供一个临时的漏洞修补方案。

## **Part2 技术研究过程**

首先这个nacos的0day漏洞是真实存在的，危害是很严重的，再者这是一个登录后台才能利用的漏洞，而且不出网也能利用。有网友会说，有的nacos不需要登录后台也能打，那是因为所打的nacos存在之前的匿名访问漏洞、或者鉴权漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450AQs2qljPrMOnY6iaURUpGJT8xFkj24IJuCnlkJGMianvBiawjQDz93OaJ3vCSzPZW4qTLKSGOlYBt5w/640?wx_fmt=png&from=appmsg)

**这里给出一个临时的修补漏洞的方法：**

**1   升级nacos到最新版本**（原因：杜绝nacos前期出现的几个未授权访问漏洞）。

**2   禁止nacos的匿名访问，开启鉴权**。

**3   nacos的口令设置得足够复杂**（原因：杜绝弱口令，这个nacos的0day漏洞是需要登录后台才能利用）。

**以上三条措施做好了，就可以解决修复该漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**公众号专注于网络安全技术，包括安全咨询、APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**(replace # with @)**

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

希潭实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

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