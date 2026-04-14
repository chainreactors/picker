---
title: 我在 OSCP 考场上演18小时极限翻盘
url: https://mp.weixin.qq.com/s/ibperJHIEaEJheWY80mZxw
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:40:13.201635
---

# 我在 OSCP 考场上演18小时极限翻盘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wIGVBqrREoZnq8agibleGL4VqIz6icz0XlVVu2rvBuWLCGnvibV0h44spBiclLLJjKC1PMGUaicrgOMibfGvm3oXPhShic8okNia2ib4v0DzZRvFhMKI/0?wx_fmt=jpeg)

# 我在 OSCP 考场上演18小时极限翻盘

原创

SKillLab
SKillLab

SkillLab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/giaH4bTW3BOn7HPhfCMVxA0xejnkZnrB7IzGmjhJgJiaZOqicg7CFjrT9RpRjGhAgRjQmzq3mxicx4Omb2qFBFLP4Q/640)

![](https://mmbiz.qpic.cn/mmbiz_png/yE70PlBSEozVzTlePtQiashoYBKamZxNpJ51KxAQrTo1uNYOmLQxWs5GWialAxToZvVxIm7ic31Bw4WEM8icL4dDog/640)

本文内容仅用于 **OSCP 备考交流**

互联网不是法外之地，请严格遵守《网络安全法》

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0R0gH979OQm5DPYX5ibxXe5qQhhHPuj3jWWRNSfSJ4IRal5yNkjTjcDVezJ3y6xzHYqlVUhwTW1HvqX5CFzmlOg/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qDqAuCnIXITRGeD5aouLKbXRJia0uSyY5EPCes7mMPeKNc22Tv4trYWibW7ta9xujbnmSBa04z1kIyFd65Fa6GqA/640)

![](https://mmbiz.qpic.cn/mmbiz_jpg/wIGVBqrREobZUPt1uufGG0Duib10kJU2UEn6g9qSluzYmSvt9yzswpWcE7cHeVT9BFiclCsrbq9B7iaqQBw4fV2bg9K45vyicPKsG1IKOD0dRAU/640?wx_fmt=other&from=appmsg)

01

出师不利——消失的 40 分钟

4 月 6 日上午 7:00，我开始了 OSCP 考试。

然而，现实在我开始的那一秒就给了我一记闷棍。

因为我的outlook邮箱开启了自动翻译功能，原本用于 VPN 认证的凭据被翻译成了汉字并未第一时间察觉。

结果就是：VPN 认证反复失败。在还没看到靶机影子的时候，我就在认证环节整整耗掉了 40 分钟。除去吃饭、睡觉和这个意外，我真正的战斗时间被压缩到了约 18 小时。

02

至暗时刻——前 12 小时的“颗粒无收”

按照自己的考前规划，我采取“先 AD 域环境，后独立靶机”的策略。

利用官方提供的凭据进入第一台域靶机后，我本以为会顺风顺水，现实却是死一般的寂静。我像疯了一样翻找：

* 第三方程序？ 有但无权限。

* 系统运行日志？ 干净。

* 定时任务（Cron jobs）？ 毫无线索。

时间一分一秒过去，整整 12 个小时，我在域环境和独立靶机之间反复横跳，心思完全无法集中。那种“明明就在眼前却找不到入口”的挫败感，让我几度想要直接“放弃”。到晚上19点，我手里只有可怜的 10 分，距离及格线遥不可及。

03

战术重启——一顿晚饭定下心神

晚上19点，我告诉自己：必须停下来。

我强制自己离开屏幕去吃了一顿饭。这时候拼的已经不是技术，而是心态。饭后，我放弃了死磕域环境，转而攻坚独立靶机。

果然，心态平稳后，思路也清晰了。22:00 左右，我顺利拿下一台独立靶机的完整权限，总分来到 30 分。这 30 分像是一剂强心针，让我重新找回了掌控感。我再次回到第一台域靶机，在细致的“地毯式”搜索下，终于抓住了那个隐藏极深的关键线索！

凌晨 1:00，第二台域靶机权限到手。

04

凌晨 5 点的豪赌——最后 35 分钟的绝杀

此时距离考试结束仅剩 6 小时，体力和精力都到了临界点。

最后一台域控需要进行密码爆破。我从互联网找到一个对应工具，但它需要繁琐的调试才能适配当前环境。在耗费 1 小时调试后，此时已经来到了凌晨2点，我开启了爆破任务。

所以我做了一个大胆的决定：睡觉，此时我已经困到了极致，完全凭意志力在坚持 。 我深知如果大脑不休息，我也无法处理任何新的问题。

清晨 5:00，我被闹钟惊醒。距离考试结束仅剩 2 小时，但爆破结果依然没有出现！这时候我做出了全场最关键的一个决策： 果断放弃当前爆破工具，更换另一种爆破逻辑和工具。

06:25 分，在考试结束前 35 分钟， 拿下域管权限，全域通关！

05

那些看似“无用”的坚持

第二天收到通过邮件时，我的心情反而很平静。

回想从 2025 年 9 月开始的备考之路，那是一段漫长且孤独的旅程。每天雷打不动的 2 小时靶机训练，即便中间穿插着高强度的护网行动、重保任务和开不完的会，我也从未松懈。

从刚开始面对复杂网络环境的不知所措，到现在可以在 24 小时高压环境下独立完成渗透测试全流程，这不仅仅是一张证书，更是我努力路上最好的勋章。

OSCP 教给我的不仅仅是 Nmap 或 Metasploit ，而是一种“Try Harder”的意志：即便前 12 小时颗粒无收，只要不放弃，最后 35 分钟依然可以翻盘。

06

备考小贴士

1. 注意细节： 考试时关闭所有自动翻译插件，避免出现判断错误。
2. 心态管理： 当你感到崩溃时，强迫自己离开屏幕 15 分钟，这比死磕更有用。
3. 工具储备： 永远准备好方案 B，当一个工具失效时，果断切换。

如果你也走在OSCP这条路上，希望我的经历能给你带去一点力量。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icm4ChVndamFMq6SvSQ198icGFvO95e1w2hyPynxE0A6tWibxnWHasd6pcLddg54FWasFcmV1vc44eAXSkCvIK3mw/0?wx_fmt=png)

SkillLab

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icm4ChVndamFMq6SvSQ198icGFvO95e1w2hyPynxE0A6tWibxnWHasd6pcLddg54FWasFcmV1vc44eAXSkCvIK3mw/0?wx_fmt=png)

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