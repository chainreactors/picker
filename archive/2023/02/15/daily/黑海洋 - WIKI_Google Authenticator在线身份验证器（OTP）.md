---
title: Google Authenticator在线身份验证器（OTP）
url: https://blog.upx8.com/3223
source: 黑海洋 - WIKI
date: 2023-02-15
fetch_date: 2025-10-04T06:37:48.800685
---

# Google Authenticator在线身份验证器（OTP）

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Google Authenticator在线身份验证器（OTP）

发布时间:
2023-02-14

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
130990

## 简介

基于开源的代码（@Author：gbraad.nl），搭建了一个在线版的身份验证器，方便使用。 TOTP、Google Authenticator 在线版

## 原理

### HOTP的工作原理

$$ HTOP(K,C) = Truncate(HMAC-SHA-1(K,C))$$
客户端和服务器事先协商好一个密钥K，用于一次性密码的生成过程。此外，客户端和服务器各有一个计数器C，并且事先将计数值同步。而Truncate是为了获得一个符合HTOP要求的值。

### TOTP的工作原理

Time-based One-time Password (TOTP)：即基于时间的一次性密码算法，也称时间同步的动态密码。
$$TOTP = Truncate(HMAC-SHA-1(K,T))$$
TOTP是HOTP的一个变种，将HOTP中的计数器C替换为依托时间的参数T，T是由当前时间(CurrentUnixTime、初始时间(T0)、步长(X)决定的。即：$$ T = (Current Unix time – T0) / X $$

* CurrentUnixTime：当前的Unix时间。
* T0： 开始计步初始化时间，默认为0
* X : 步长，默认情况下为30s

### TOTP的一些要求

* 客户端和服务器必须能够彼此知道或者推算出对方的Unix Time
* 客户端和服务器端必须共享一个密钥
* 算法必须使用HOTP作为其关键实现环节
* 客户端和服务器端必须使用相同的步长X
* 每一个客户端必须拥有不同的密钥
* 密钥的生成必须足够随机
* 密钥必须储存在防篡改的设备上，而且不能在不安全的情况下被访问或使用。
* 对该算法中T的实现必须大于int32，因为它在2038年将超出上限。
* T0和X的协商必须在之前的步骤中就已经做好了。

## 代码

[https://github.com/gbraad/gauth](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dicmFhZC9nYXV0aA)

## 在线版

* gauth.cpp.la
* gauth.apps.gbraad.nl（备用）
* [https://gg.7761.cf/](https://blog.upx8.com/go/aHR0cHM6Ly9nZy43NzYxLmNmLw)（会生成链接）

1. ![李四季](//q2.qlogo.cn/headimg_dl?dst_uin=2125900833&spec=100)

   **李四季**

   2024-05-23 23:31:38

   [回复](https://blog.upx8.com/3223/comment-page-1?replyTo=29623#respond-post-3223)

   不拒绝看看嘛没看看
2. ![Gerard Braad](https://gravatar.loli.net/avatar/avatar/e466994eea3c2a1672564e45aca844d0?s=32&r=&d=)

   **Gerard Braad**

   2023-07-07 22:40:10

   [回复](https://blog.upx8.com/3223/comment-page-1?replyTo=27341#respond-post-3223)

   谢谢
3. ![.](//q2.qlogo.cn/headimg_dl?dst_uin=3615143581&spec=100)

   **.**

   2023-02-18 22:43:14

   [回复](https://blog.upx8.com/3223/comment-page-1?replyTo=26915#respond-post-3223)

   嘎嘎好用
4. ![小二不羊](//q2.qlogo.cn/headimg_dl?dst_uin=1762748917&spec=100)

   **小二不羊**

   2023-02-14 23:53:13

   [回复](https://blog.upx8.com/3223/comment-page-1?replyTo=26906#respond-post-3223)

   666

[取消回复](https://blog.upx8.com/3223#respond-post-3223)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")