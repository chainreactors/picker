---
title: CTFHub：第八十一章——JSON Web Token——基础知识
url: https://mp.weixin.qq.com/s/ePMpjxwSiTzy3ZK5mWIv-g
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:57:27.957808
---

# CTFHub：第八十一章——JSON Web Token——基础知识

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TkbqemjbpIrkNpHscyIeicoIH27f06RqM1zJaerCRmoowYoJsOJV0MqTnecrrkOfCsDTc6OibhAKwwOsWia0snllydwkAXLqwOPiaaJ7U0erpCY/0?wx_fmt=jpeg)

# CTFHub：第八十一章——JSON Web Token——基础知识

原创

君陌社区
君陌社区

君陌社区渗透安全笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

CTFHub网址:【https://www.ctfhub.com/#/index】

登录账号
点击技能树

选择“web进阶- JSON Web Token-基础知识”开启题目

题目描述: 学习什么是 JWT

由于题目附件无法打开所以本章我们就来学习一下JWT的知识

![](https://mmbiz.qpic.cn/mmbiz_png/TkbqemjbpIrDOogLQ4ibFT0vFzicEUZWcfZiaUzyqs0J2Tz1bjIiciaEliagEoOE3KE3J7ZfPC4o3xjJjDQgia5mhEMF0k5rrORQEZvM3f35dutogE/640?wx_fmt=png&from=appmsg)

# 一、JSON Web Token原理

JSON Web Token，简称 JWT，是一种开放标准。它定义了一种紧凑且自包含的方式，用于在各方之间安全地将信息作为 JSON 对象传输。JWT 主要用于两个场景：

1.认证：当用户登录成功后，服务器会生成一个JWT并返回给客户端。之后，客户端在每次请求时都带上这个JWT，服务器通过验证JWT来确认用户的身份。这就是所谓的“基于令牌的认证”

2.安全的信息交换：JWT可以本签名，就可以确保发送方的身份。由于签名是基于头部和有效负载计算的，还可以验证内容是否在传输过程中被篡改

# 二、JWT的结构（三部分，用.分隔）

```
Header.Payload.Signature
```

1.Header：算法和类型，如 {"alg":"HS256","typ":"JWT"}

2.Payload：实际数据（用户ID、角色等），仅Base64编码，未加密

3.Signature：对前两部分用密钥签名，防止篡改

关键知识：Payload是明文可见的，绝不可存放密码等敏感信息。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/csuE9m26HkI8taS28gIOWsc8KaibxmZ9HDovmlvGsicEnJuSw0Ricdq3KibbTUnRicEO0NohDyczWdgJBOe3RWF1tQw/0?wx_fmt=png)

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