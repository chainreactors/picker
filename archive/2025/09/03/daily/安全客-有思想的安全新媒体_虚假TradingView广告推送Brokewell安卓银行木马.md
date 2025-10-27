---
title: 虚假TradingView广告推送Brokewell安卓银行木马
url: https://www.anquanke.com/post/id/311790
source: 安全客-有思想的安全新媒体
date: 2025-09-03
fetch_date: 2025-10-02T19:32:37.097524
---

# 虚假TradingView广告推送Brokewell安卓银行木马

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 虚假TradingView广告推送Brokewell安卓银行木马

阅读量**41861**

发布时间 : 2025-09-02 15:44:45

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ionut Ilascu，文章来源：bleepingcomputer

原文地址：<https://www.bleepingcomputer.com/news/security/brokewell-android-malware-delivered-through-fake-tradingview-ads/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络犯罪分子正在滥用 Meta 的广告平台，以“免费获取 TradingView Premium 应用”为诱饵，向 Android 用户投放恶意广告，传播 **Brokewell 恶意软件**。

这一攻击行动自 **7 月 22 日起活跃**，涉及约 75 个本地化广告，主要瞄准加密货币资产用户。

**Brokewell 恶意软件最早在 2024 年初被发现**，具备广泛的功能，包括窃取敏感信息、远程监控以及完全控制受感染设备。

## 假冒 TradingView 推广

Bitdefender 的研究人员对这波广告进行了调查。攻击者利用 TradingView 的品牌和视觉元素，向用户承诺“免费 Premium 应用”。
研究显示，该攻击专门针对移动端用户设计——如果在非 Android 系统上点击广告，则只会显示无害内容；但在 Android 上访问时，会被重定向至一个仿冒的 TradingView 网站，诱导下载恶意的 **tw- update.apk**，该文件托管在 **tradiwiw[.]online/** 域名下。

研究人员指出，安装后的恶意应用会立即索取辅助功能权限，并在获得权限后用一个假的“更新提示”遮盖屏幕，同时在后台悄悄授予自己所有所需权限。

更具隐蔽性的是，该应用还会通过模拟 Android 系统更新请求，引诱受害者输入锁屏密码，以窃取设备 PIN 码。

![]()

## 高级版本的 Brokewell 恶意软件

据 Bitdefender 报告，这款假冒 TradingView 应用实际上是 **Brokewell 恶意软件的高级版本**，内置了庞大的攻击工具集，能够全面监控、控制并窃取用户的敏感信息：

**重点能力包括：**

1.扫描并窃取 **BTC、ETH、USDT** 等加密资产及银行账户信息（IBAN）；

2.窃取并导出 **Google Authenticator 动态验证码**，绕过双重认证；

3.通过伪造登录界面窃取各类账户凭证；

4.记录屏幕和按键输入、窃取浏览器 Cookie、启用摄像头和麦克风、追踪地理位置；

5.劫持默认 **短信应用**，拦截银行验证码及 2FA 验证短信；

6.通过 **Tor 或 WebSocket** 接收远程指令，可执行发送短信、拨打电话、卸载应用甚至自毁等操作。

研究人员指出，该恶意程序的完整命令集超过 **130 条**，展现出极高的攻击复杂度。

Bitdefender 还强调，这并非孤立行动。早期阶段，攻击者曾利用 **Facebook 广告冒充数十个知名品牌**，针对 **Windows 用户** 发动攻击。而此次 Android 平台的投毒，则是这一更大规模行动的延伸。

本文翻译自bleepingcomputer [原文链接](https://www.bleepingcomputer.com/news/security/brokewell-android-malware-delivered-through-fake-tradingview-ads/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311790](/post/id/311790)

安全KER - 有思想的安全新媒体

本文转载自: [bleepingcomputer](https://www.bleepingcomputer.com/news/security/brokewell-android-malware-delivered-through-fake-tradingview-ads/)

如若转载,请注明出处： <https://www.bleepingcomputer.com/news/security/brokewell-android-malware-delivered-through-fake-tradingview-ads/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

### 热门推荐

文章目录

* [假冒 TradingView 推广](#h2-0)
* [高级版本的 Brokewell 恶意软件](#h2-1)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)