---
title: 注意！网络犯罪分子利用 NFC 与移动支付平台实施复杂诈骗
url: https://www.anquanke.com/post/id/306348
source: 安全客-有思想的安全新媒体
date: 2025-04-11
fetch_date: 2025-10-06T22:03:02.945402
---

# 注意！网络犯罪分子利用 NFC 与移动支付平台实施复杂诈骗

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

# 注意！网络犯罪分子利用 NFC 与移动支付平台实施复杂诈骗

阅读量**67088**

发布时间 : 2025-04-10 11:07:41

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/hackers-hiding-nfc-carders/>

译文仅供参考，具体内容表达以及含义原文为准。

网络犯罪分子已经设计出了复杂的方法，通过流行的移动支付平台来利用 NFC 技术。

这些攻击者现在在通过网络钓鱼手段获取受害者的银行卡凭证后，利用 Apple Pay 和 Google Wallet 进行未经授权的交易。

该诈骗方案包括将被盗的支付卡信息关联到欺诈性的移动钱包账户上，使得犯罪分子无需接触实体银行卡，就能使用受害者的资金进行非接触式支付。

这种攻击通常始于受害者访问那些模仿送货服务、在线零售商或公用事业缴费门户的欺骗性网站。

毫无防备的用户会被诱导关联他们的支付卡或进行小额验证支付，这就需要输入完整的银行卡详细信息，并通过一次性密码（OTP）来确认卡的归属权。

这些详细信息并不会用于处理合法交易，而是会立即被传送给等待接收的网络犯罪分子。

Kaspersky 的研究人员发现，这些诈骗操作几乎达到了工业化的规模，诈骗者获取了大量智能手机，创建了多个 Apple 或 Google 账户，并安装非接触式支付应用程序来实施他们的诈骗计划。

根据他们的调查，攻击者使用专门的软件生成受害者银行卡的完美数字副本，然后将其直接拍照录入移动钱包应用程序，以便即时关联。

这些攻击特别有效的原因在于，在盗取凭证和提取资金之间存在显著的时间延迟。

网络犯罪分子通常会在盗取银行卡信息数周甚至数月后才使用这些被盗用的银行卡，到那时受害者可能已经忘记了与可疑网站的交互行为。

当最终发生交易时，通常是在实体店购买奢侈品或通过支持 NFC 功能的智能手机从自动取款机（ATM）取款，而这两种交易都不需要额外的个人识别码（PIN）或一次性密码（OTP）验证。

对 NFC 技术的利用代表了支付欺诈手段的重大演变，它结合了数字和实体元素，设计出了通过传统安全措施难以察觉和追踪的诈骗方案。

**Ghost Tap技术**

这种欺诈生态系统的核心是一种被称为 Ghost Tap 的 NFC 中继技术，安全专家认为这种技术特别危险，因为它能够绕过传统的反欺诈措施。

这种方法包括在两部不同的智能手机上安装诸如 NFCGate 这样的合法应用程序 —— 一部手机的钱包中存有被盗取的银行卡信息，另一部手机则用于进行实际支付。

中继应用程序通过加密的互联网连接，将第一部设备上钱包的 NFC 数据实时传输到第二部设备的 NFC 天线，然后由被称为 “mules” 的犯罪分子在支付终端使用第二部设备进行支付操作。

**NFC 中继操作的简化表示**

def nfc\_relay(source\_device, target\_device):
while connection\_active:
nfc\_data = source\_device.read\_nfc\_signal()
encrypted\_data = encrypt(nfc\_data)
send\_over\_internet(encrypted\_data, target\_device)

**在目标设备上**

def receive\_and\_transmit ():
received\_data = receive\_from\_internet ()
decrypted\_data = decrypt (received\_data)
target\_device.broadcast\_to\_nfc\_antenna (decrypted\_data)

这种方法的技术复杂性在于它能够在远距离传输信号的同时保持信号的完整性。

支付终端和自动取款机无法区分中继的 NFC 信号和合法的 NFC 信号，这使得检测变得异常困难。

负责支付的 “mule” 的设备上只装有合法软件，没有直接证据表明存在被盗取的银行卡凭证，而这些凭证则安全地存储在幕后主使的远程设备上，这些设备通常位于完全不同的地理区域。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/hackers-hiding-nfc-carders/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306348](/post/id/306348)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/hackers-hiding-nfc-carders/)

如若转载,请注明出处： <https://cybersecuritynews.com/hackers-hiding-nfc-carders/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

### 热门推荐

文章目录

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