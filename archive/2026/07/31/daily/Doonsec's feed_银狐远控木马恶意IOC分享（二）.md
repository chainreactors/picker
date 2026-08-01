---
title: 银狐远控木马恶意IOC分享（二）
url: https://mp.weixin.qq.com/s/k6Ji4yXTeUEnA4tX3JyZEQ
source: Doonsec's feed
date: 2026-07-31
fetch_date: 2026-08-01T05:11:20.636043
---

# 银狐远控木马恶意IOC分享（二）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FEWcqzYgxoibZwt5l7jpAjDiawFqUZrSpIMgOMVa0UYs510xInicxpwrI8IvVhf220J3UBvNUicLNKwUMGbk2kopFywRFSxoMWr3N5h8yEkiaiaN8/0?wx_fmt=jpeg)

# 银狐远控木马恶意IOC分享（二）

剁椒Muyou鱼头
剁椒Muyou鱼头

剁椒Muyou鱼头

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/92Yia6FpSFA2QiaAzq0Dumm39PGIsC7mk4lX6c4yYnERUGvnHo7SQreGiboYBj0ib7TlaUx1DKtEGlU8mqS9ZtLZRw/640?wx_fmt=gif)

**阅读须知**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/92Yia6FpSFA2QiaAzq0Dumm39PGIsC7mk4lX6c4yYnERUGvnHo7SQreGiboYBj0ib7TlaUx1DKtEGlU8mqS9ZtLZRw/640?wx_fmt=gif)

**本公众号文章皆为网上公开的漏洞，仅供日常学习使用，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把**剁椒Muyou鱼头**“设为星标”，否则可能就看不到了啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/92Yia6FpSFA2hvEA8gEIeGOEiba9uWicXD01hM2Bw8oTpcNCZl68Bj8T0aLpOHAMFCv9Qd6KeeQgTscOURdQUDbLw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/92Yia6FpSFA2QiaAzq0Dumm39PGIsC7mk4Z7hc6oGV6C6IwibzfQUM1oq1yUciadAKQ3Ap29o8GGnBU52wXgSSicBxQ/640?wx_fmt=gif)

**2026/07/31 星期五**

//01 前言

上次发的银狐IOC不少朋友反馈已经安排上了。最近在应急现场又攒了一批，来源杂，IDS流量日志里命中的、微步上关联出来的、沙箱跑出来的都有。可以结合微步以及其他威胁情报厂商交叉验证，综合分析是否可以封禁。

可以直接导入防火墙黑名单或者规则里用。格式稍微改改就能适配不同设备。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FEWcqzYgxoibwrCF7pkgqzyt1qNgibHN7cQpGfSyHLqyDMIUoicbJzIXJzklq7IcbL2hrHw3FllT1Dxc6Xre5PZfWU53OwoWRRrW7Jlzu227cw/640?wx_fmt=png&from=appmsg)

//02 IOC列表

和上篇一样，Base64兜个底，懂的都懂，解一下就能看到了。

ZGRvc2Rucy5jYwpkdmhndGRzbi5jbgpmeXV1ay5iaW5nLmhrLmNuCmdid3NkdWt6LmNuCmxvdGV2a2suY24KbHBvbW5oY2YuY24Kcm9tbmtsai5jbgp0Ymhqa2xvc3cuY24KdXVray53ZWM1MTIuY29tCnltaW5zZ2RiLmNuCnRvbW5odWRzLmNuCjg4OC54YXNmMDMuY29tCnVvbm1nYi5jbgpmYWRram5rbWlwLmNuCnBkeHgucDlsMTIuY29tCnpoeXlkcy5zdGFyMWluZS5jb20KeXlkcy55ZHNzaXNzLmljdQo1NTU4ODguY3lvdQpxYXFiYmEuY29tCmxhb21zamR1bi5jbgp4aXV5aXUubmV0CmRnai5leDRheDJveDMuY29tCmljZWlpc2tlbmcuY29tCmpqYmJhYTEyLmNjCmpxbi5qaHd0d3VlLmNvbQp3d3cudHVpZ3VhbmcxNjgudG9wCnh3YS5haXNpc3MuaWN1CnlrLmdnZHkuY29tCnpob25nLjJqM2oueHl6CjExNi5iZWk5Lnh5eg==

http://www.lpsz.cn/

![](https://mmbiz.qpic.cn/mmbiz_png/FEWcqzYgxoicua5Xm6Xl2icq3mkwcH0OJwia7lLnSO9nwuRaLA43E9pkzURJX6z6oSfTGJWRxBM4wvPOsxibghnpaZnQp3udcicwO8YSUnk0jO4E/640?wx_fmt=png&from=appmsg)

//03 结尾

这批货不算多，但都是在实际应急里真刀真枪命中过的，或者威胁情报平台公布的。防火墙、IDS该配的都配上，配置不复杂，效果立竿见影。后续再有新的继续攒，攒够了发第三篇。

END

---

 作者 | 剁椒Muyou鱼头

I like you,but just like you.

我喜欢你，仅仅如此，喜欢而已~

**点赞在看不迷路哦！**

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/92Yia6FpSFA3QZ2ZMP7Q5urLdMRypjGymwnDtUS5Xjq1N9yn2aZG2ew66sCg9G7fK8auy2l85VrjGx7Yy1snyXA/0?wx_fmt=png)

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