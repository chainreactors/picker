---
title: 苹果Find My私有协议被逆向，Linux设备无需iPhone即可读取共享位置
url: https://mp.weixin.qq.com/s/_MqNflG3Df4oZIJ_TEE3bQ
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:01:30.120461
---

# 苹果Find My私有协议被逆向，Linux设备无需iPhone即可读取共享位置

# 苹果Find My私有协议被逆向，Linux设备无需iPhone即可读取共享位置

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX2d8GlhfRCnuAq5geICEhPgW79ZOiaFBkYFVJy2MOOmWjhdOkiaHws5hGlFwh4eVoKia29Z3PeibMThNQaN8GkpDo97WMetT1AmUgU/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0rFNlGJTnRVvc4xU0XHX3YYSODELypagJqZKeoYQYERPn0Z87EicRyhcIOFs2dy8ibNiafKOjYM4jaHxtrvTcMLOHEh3So6PI1sg/640?wx_fmt=jpeg&from=appmsg)

一名安全研究人员成功逆向工程了苹果私有的Find My People协议，证明一台Linux机器可以在完全不接触Mac或iPhone的情况下，注册到苹果内部服务、接收现有的位置共享密钥，并解密好友的实时位置。

这个项目起初并无恶意：研究人员想利用好友通过苹果Find My应用已共享的位置数据，构建Discord地理围栏提醒。原以为只是一次简单的经过身份验证的API调用，结果却耗费了约一周时间对苹果私有设备身份与消息基础设施进行逆向工程，因为此前没有开源项目完整复现过这一流程。

研究人员结合苹果fmfd、findmylocated和searchpartyd守护进程的反编译结果，以及FindMy.py、pypush等开源工具，逐字段重建了整个数据管道。

Part01

从零伪造苹果设备

第一个障碍是身份验证。标准iCloud登录令牌在调用旧的Find My Friends API时返回401错误，因为每个苹果服务都会通过代理交换机制签发各自限定作用域的凭证。

通过苹果账户登录协议GrandSlam完成身份验证后，研究人员获得了IDS的委托令牌。IDS是苹果私有的身份与加密消息层，同时支撑着iMessage和Find My。

要将该令牌转化为可用的设备身份，需要提交一个证书签名请求，其中包含非常具体且尚未公开的约束条件：2048位RSA密钥、SHA-1签名，以及由账户profile ID的SHA-1哈希派生而出的通用名称，并封装在gzip压缩的XML属性列表中。

注册为Find My设备同样要求严格，需要加入苹果"alloy"多路复用服务下的六个特定子服务，而非直接注册Find My Friends。

Part02

获取密钥并解密实时位置

概念上最棘手的部分，是让苹果把已接受共享的加密密钥发送给这台新的Linux“设备”。

据Zerotistic研究人员介绍，发送一个intent为distributeKeys的SubscribeAndFetch请求，即可触发共享设备通过苹果推送通知服务（APNs）重新分发其当前密钥，密钥封装在名为pair-ec的带签名且经过ECDH（椭圆曲线迪菲-赫尔曼）验证的信封中。

关键在于，这无需重新共享或更改账户，因为苹果的架构设计会自动将现有密钥交给新添加的设备。

传递过来的密钥使用了基于P-224曲线的椭圆曲线密码学，与消息信封本身所用的P-256密钥不同。

拿到每项共享对应的密钥后，研究人员查询了苹果的SearchParty服务（该服务存储加密的位置报告），并利用ECDH密钥交换和AES-GCM（伽罗瓦/计数器模式高级加密标准）在本地解密密文。最终，研究人员仅依靠Linux工具就获得了已同意共享的好友设备的实时且经过验证的坐标、精度半径与时间戳。

这项研究并未发现苹果需要修复的安全漏洞，因为它仅访问了该好友已经自愿共享给研究人员账户的位置信息。

其价值反而在于首次详细记录了苹果私有IDS与SearchParty协议如何分发和轮换位置共享密钥，这对构建可互操作或自托管Find My客户端的研究人员很有帮助。

参考来源：

Apple’s Private Find My People Reversed to Decrypt Live Shared Locations on Linux

https://cybersecuritynews.com/apple-find-my-people-reversed/

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0grlwwcpsEQ5CIH725a7xAnwDLGFctXFohPibiaOVyzdqwaibKgD4x4enG6jhdgJQHziaqTMy1WR0Hibx4MceSVKd6C7HGGlA9zLibg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651344398&idx=1&sn=56c4e0d580e04a250d0e8c6cffd592b8&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3eRDUpH3UJicSe4tdw7nZYu9aa5PQ9KgkaP84oZz0bVYdBiaDt97VfDBLulDp3sWLgvzI4m0mc89MZ7feP2yfFAmcRWOlicWubZ4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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