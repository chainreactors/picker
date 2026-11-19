---
title: 【安全圈】苹果崩了！！！
url: https://mp.weixin.qq.com/s/aLagQuhSATtO2DfcsPoz_g
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:40:06.426989
---

# 【安全圈】苹果崩了！！！

# 【安全圈】苹果崩了！！！

安全圈
安全圈

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

苹果

**核心事实**：北京时间 11 月 18 日 00:15 起，苹果多项在线服务接连失联，iCloud 账户登录、App Store、AppleCare、企业批量采购与教育管理平台全部在列。最后一组服务在 06:00 恢复。苹果给彭博社的说法是一句没有细节的「**内部系统更新**」，并明确否认遭到网络攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFDacuwrwSjiaSFetYPZuWA7a0bYsuJibBJr1yEdxqUibh5gzQ7GTD9iasiba0T6YHpVPqltH9ksaeQUx6YFKiaQIiam66wQzseBoUOn4/640?wx_fmt=other&from=appmsg)

用户端最先撞上的是登录。据 MacRumors 记录，社交平台上陆续有人报告 Apple 账户与 iCloud 无法登录，App Store 打不开，Apple Music 与 Apple Pay 也不对劲；直营店排到柜台，店员那台设备结不了账。苹果官网的系统状态页随后挂出条目，措辞分成三档——Outage（中断）、Issue（异常）、Performance（性能下降），这三档在当晚被同时用上了。

## ⏱ 六小时时间线（北京时间）

* **00:15**

  ：AppleCare on Device 中断。状态页标注受影响范围是「所有用户」，具体表现是设备保障购买暂时不可用。
* **00:45**

  ：iCloud 账户与登录出问题，App Store 直接中断。同一时刻挂出的还有 Volume Purchase Program 与 iCloud Mail、iCloud.com 网页端。
* **02:40**

  ：Apple Business、Apple School Manager、Schoolwork 一并转入「慢或不可用」，这一组一直到 **06:00** 才收尾。
* **04:00 / 05:15 / 06:00**

  ：App Store 与 VPP 在 04:00 恢复，iCloud 三项在 05:15 恢复，企业教育组在 06:00 恢复。全程近 6 小时。

这份时间线来自苹果自己的状态页数据源，不是二手转述。同一批事件里还夹着一条 11 月 16 日的 VPP 例行维护记录，标注「无用户影响」——它和 17 日的故障不是一回事，写在一起容易被误读。

## 🔍 苹果说了什么，没说什么

对外的完整表述有三层：故障由一次未具名的内部更新引起；不是网络攻击；其余系统正在尽快恢复上线。到此为止。苹果没有说明是哪套内部系统、更新了什么、为什么能穿透到面向用户的服务层，也没有给出时间点的因果解释。一句话概括这份声明的结构：确认、定性、不给根因。

开发者侧另有一条线：App Store Connect、Apple Music API、Apple Music Connect、Apple Podcasts Connect 的账户服务同期中断。这条对独立开发者和小团队影响更直接——提审卡住、构建上传失败、订阅对账延迟，都要等到服务恢复才能补。

## ⚠️ 报障数字要打个折

Downdetector 记录到，美国东部时间 11 月 17 日 12:20 前后，Apple Pay 报障一度到约 **2300 条**；iCloud 的报障峰值约 **1800 条**。这两个数字只代表「有人主动去点了报障按钮」，不是受影响用户数。

还有一处需要校正：苹果当晚的状态页**没有单列 Apple Pay 事件**，它列的是 App Store、AppleCare、iCloud 账户与登录、iCloud Mail、iCloud.com、Apple Business、Apple School Manager、Schoolwork、VPP。Apple Pay 的报障更可能是账户登录失败往支付链路上传导——钱包本身没坏，验证身份那一步走不通。把两者当成同一个故障来写，会高估支付系统的受损程度。

## 🏬 真正被卡住的是线下

苹果零售门店的系统当晚离线，顾客无法完成购买，设备维修受理流程同样中断。门店收银、售后受理、库存查询共用同一套后台，账户体系一停，这三件事会一起停——不是「收银机坏了」，而是整套身份与授权链断了。

企业侧同理。Apple Business 与 Apple School Manager 管的是设备注册、批量采购、应用分发，学校那一层还挂着 Schoolwork 的作业分发。这一段从 02:40 挂到 06:00，正好覆盖欧美工作日的收尾时段。

## 💻 一周之内，第三次

往前数：11 月 12 日微软 365 全球性中断，Outlook 邮件、Teams、Copilot 受影响，持续近 24 小时才基本恢复，微软给的解释是「早前一次网络容量升级引入的问题，经由近期一次网络变更暴露」；同期美国联邦航空管理局通信网络故障，一度导致全美航班停飞；再往前，摩根大通的软件问题影响过部分银行服务与跨行交易。路透社的说法是，相关企业与美国官员均表示没有证据指向网络攻击。

三次事件的共同点在于变更管理，不在对抗。微软那条写得最清楚：容量升级埋的问题，在下一次网络变更时才浮出来。苹果这次只有一句「内部更新」，细节暂时没有。

## 🎯 一条被低估的连带损失

同一周里有个更扎眼的案例。德国主题乐园 Phantasialand 旗下酒店，泳池的自动加氯设备 11 月 13 日故障，持续加氯；本应报警的监测系统靠 Outlook 邮件推送。当天微软 365 全球中断，邮件没发出去，员工没收到告警。等到住客在泳池里感到不适才发现，15 人受影响，4 人送医，1 人因中度伤情留院。

这不是段子。告警通道挂在单一第三方邮件服务上，等于把安全联锁的最后一环交给了别人家的可用性。哪怕再补一条 Telegram 或 Discord 的 WebHook，结论都会不一样。

## ✅ 处置现状

截至本文写作时，苹果状态页上这批事件全部标记为 resolved，没有残留条目，也没有发布事件复盘文档。苹果方面仅表示剩余系统正在恢复，未回应是否会公开根因。受影响用户无需任何操作，服务已自行恢复；有未完成的购买、维修预约或应用提审，重新走一遍流程即可。

***END***

阅读推荐

[【安全圈】178个站点被投毒：官方CDN送出了盗卡脚本](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079911&idx=1&sn=30b6dbda996787a2462c7afcd183f474&scene=21#wechat_redirect)

[【安全圈】运维工具长出蠕虫：SCKit跳到技术员电脑](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079911&idx=2&sn=a83acfe4ccc4a76cfdbf3a930ca47aca&scene=21#wechat_redirect)

[【安全圈】一次补掉17个洞：遗留API开关被彻底删除](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079911&idx=3&sn=cbb961e616211be500f55d885d1a8cac&scene=21#wechat_redirect)

[【安全圈】无印良品明文存卡号：109万张信用卡多留了五年](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079900&idx=1&sn=07e67415a5bb07511d553704768da1d6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过