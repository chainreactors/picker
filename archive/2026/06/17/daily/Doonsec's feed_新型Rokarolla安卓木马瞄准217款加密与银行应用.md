---
title: 新型Rokarolla安卓木马瞄准217款加密与银行应用
url: https://mp.weixin.qq.com/s/_urnb9p94Uz2UvIEVezJ4Q
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:48:02.622563
---

# 新型Rokarolla安卓木马瞄准217款加密与银行应用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0gNYMNklA9gX6TNObgUnyBXJ3LXYxiaicgZyicib5dAIwDHLSmEibBRepA5t83xHD1E3hI0KymiakrN0FYLSSdfnVMFdNEzXH7nJYzc/0?wx_fmt=jpeg)

# 新型Rokarolla安卓木马瞄准217款加密与银行应用

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX0fIoxqPZ72uuTt3HFgwzOOibCrVibNAJC4ssib293Q5pwVgawibz3YLiaO8AKbqib9rJ9TOhyIiazHss3AZQr11WMuIWXGjSbqwSWiccg/640?wx_fmt=gif)

![image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1NAS4rKdtyKdGCQfhjcvwo1L9depaUOlBVsKKrzzGPJ9X5FpJqZ7G14wN2H0n9IyyEM8DJnxJicjNBJwU1LQl6Q8YtC496YE5M/640?wx_fmt=jpeg&from=appmsg)

Zimperium旗下zLabs安全团队发现名为**Rokarolla**的新型安卓银行木马，该木马针对217款银行和加密货币应用，内置137条远程控制指令。攻击者通过这套指令可近乎完全控制受感染手机：窃取锁屏PIN码、读取发送短信、篡改剪贴板以劫持加密货币转账，并关闭Google Play Protect防护功能。

Part01

## 传播途径与初始入侵

Rokarolla（名称源自其C2服务器）通过伪装成TikTok、Chrome等知名应用的恶意网站传播。受害者首先安装的是一款伪装成Google Play Protect的释放器程序，该程序利用此伪装安装有效载荷并获取无障碍辅助功能权限。恶意软件运行后，会立即通过指令关闭Play Protect防护。

Part02

## 覆盖攻击与凭证窃取

该木马采用覆盖攻击技术：从服务器获取目标应用列表后，为每个标记为活跃的应用下载伪造的HTML登录页面并存储于本地数据库。当受害者打开真实的银行或钱包应用时，恶意软件立即在顶层覆盖虚假页面，窃取所有输入信息（包括银行卡详情）。研究报告中展示了模仿银行应用"imagin"的伪造页面实例。

另一覆盖层会仿冒安卓锁屏界面窃取PIN码、图形密码或文字密码，使得攻击者能在设备锁屏状态下持续控制手机。该木马还会读取设备所有短信并自主发送消息，借此截获银行用于验证登录和交易的短信验证码。通过将自己设为默认短信/通话应用，它还能拦截来电（包括银行的风险预警电话）。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3phMvRnFHumIkcyzzHdaP8FxL4Gibqic321BB3KM7Fkgjm3rjkJYxLBRRJpTRqK9mj9XLAnCg4hrjQ1JwH5DJrvWYW3Ec5wHMVw/640?wx_fmt=jpeg&from=appmsg)

Part03

## 高级监控与数据窃取

键盘记录器和屏幕记录器会捕获用户输入及屏幕内容，同时木马还会窃取通讯录和通知信息。其剪贴板劫持功能会静默替换加密货币钱包地址，导致转账资金流入攻击者账户。

在监控方面，Rokarolla摒弃了会触发可见录制提示的MediaProjection投屏技术，转而通过无障碍功能截屏，将图像压缩为PNG格式后逐帧外传。这种截图方案比Klopatra等家族采用的隐蔽VNC直播更为简单安静。

Part04

## 持久化与防御建议

该木马配备多个备用C2域名且支持动态更新，使得单点服务器关闭收效甚微。其137条指令数量远超Zimperium在HOOK木马中记录的107条，攻击手法与2026年爆发的安卓银行木马浪潮如出一辙：虚假应用释放器、无障碍功能滥用及HTML覆盖攻击。

由于属于恶意软件而非系统漏洞，目前没有补丁可修复。防御措施遵循安卓银行木马标准应对方案：仅从Google Play安装应用、保持Play Protect开启，并将任何意外的无障碍权限请求视为危险信号——该权限正是整个攻击链的核心驱动。Zimperium表示其产品已能检测该家族，相关入侵指标已发布至GitHub仓库。

研究人员尚未将Rokarolla与已知攻击组织关联。其代码结构显示出明确意图：专门针对用户依赖的核心防护措施（从Play Protect到锁屏）进行突破。

参考来源：

New Rokarolla Android Malware Steals PINs, SMS Codes, and Crypto Wallet Funds

https://www.freebuf.com/news/486357.html

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2cVdntRnNdReFrEC9uicNrkrzxp72OgpNDz7srDyd0sPwPYZejHF5E9TqvpJWJ5qHkqqDtlREdb65n2YIfXD2jnNBFTqRI2LhM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1uQ9xLm3d4ZLoKboK1GHqPxkP2twtDHay11g4CqZnzXFyjmtib8WT7iaP1Libibnib4wCE0UreN6hUMgkYJ6NP9gD2ib8g2RNFTUAj8/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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