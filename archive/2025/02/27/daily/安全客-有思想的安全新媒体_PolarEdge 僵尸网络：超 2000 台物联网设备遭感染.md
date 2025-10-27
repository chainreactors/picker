---
title: PolarEdge 僵尸网络：超 2000 台物联网设备遭感染
url: https://www.anquanke.com/post/id/304759
source: 安全客-有思想的安全新媒体
date: 2025-02-27
fetch_date: 2025-10-06T20:35:22.128246
---

# PolarEdge 僵尸网络：超 2000 台物联网设备遭感染

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

# PolarEdge 僵尸网络：超 2000 台物联网设备遭感染

阅读量**95553**

发布时间 : 2025-02-26 10:15:01

**x**

##### 译文声明

本文是翻译文章，文章原作者 do son，文章来源：securityonline

原文地址：<https://securityonline.info/polaredge-botnet-2000-iot-devices-infected/>

译文仅供参考，具体内容表达以及含义原文为准。

![PolarEdge IoT botnet]()

Sekoia 公司的威胁检测与研究（TDR）团队发现了 PolarEdge僵尸网络，这是一场复杂的基于物联网的恶意软件攻击活动，目标是存在漏洞的思科小型企业路由器和其他边缘设备。该僵尸网络已在全球范围内感染了超过 2000 台设备，并且至少从 2023 年末就开始活跃了。

此次攻击活动利用了 CVE-2023-20118 漏洞，这是一个影响多种思科小型企业路由器型号的远程代码执行（RCE）漏洞。

报告指出：“2025 年 1 月 22 日，我们通过蜜罐观察到了可疑的网络痕迹。分析表明，有人试图利用 CVE-2023-20118 漏洞。通过这一漏洞利用，攻击者执行了一条远程命令（RCE），在目标路由器上部署了一个网页后门。”

该漏洞源于 /cgi-bin/config\_mirror.exp 中不当的输入验证，这使得未经身份验证的攻击者能够通过构造恶意的 HTTP 请求来远程执行命令。

在 2025 年 1 月 22 日至 31 日期间，攻击者向存在漏洞的路由器部署了一个经过 Base64 编码且采用 gzip 压缩的网页后门。报告解释称：“为了实现持久控制，攻击者用他们的网页后门替换了路由器的身份验证 CGI 脚本（/usr/local/EasyAccess/www/cgi-bin/userLogin.cgi）。” 这种方法确保攻击者能够持续控制受感染的路由器，同时躲避检测。

到 2025 年 2 月 10 日，PolarEdge 的操控者改进了他们的攻击策略，用一个基于传输层安全（TLS）的后门植入程序替换了网页后门，这标志着其向大规模僵尸网络基础设施的转变。“对这些有效载荷的研究使得我们发现了一个由全球超过 2000 台受感染设备以及攻击者的基础设施组成的僵尸网络。”

PolarEdge 采用了多种躲避检测和实现持久控制的技术，包括：

1.隐藏自身存在：删除日志以及自身的执行痕迹。

2.清除竞争的恶意软件：终止可疑进程。

3.利用加密的命令通道：使用 Mbed TLS（前身为 PolarSSL）来保护命令与控制（C2）通信的安全。

4.动态更新攻击基础设施：从硬编码的命令与控制（C2）服务器转变为使用域名生成算法（DGA）。

威胁检测与研究（TDR）团队发现多个地区都有设备遭到入侵，其中美国的受感染设备数量最多（有 540 个 IP 地址），其次是中国台湾地区和南美洲。该僵尸网络能够针对多种架构（思科、华硕、威联通和群晖）的设备，这表明其攻击活动仍在不断扩大。

报告总结道：“‘PolarEdge 僵尸网络至少从 2023 年末就开始活跃，目标是广泛的设备，并且与一个庞大的基础设施相关联。”

本文翻译自securityonline [原文链接](https://securityonline.info/polaredge-botnet-2000-iot-devices-infected/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/304759](/post/id/304759)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/polaredge-botnet-2000-iot-devices-infected/)

如若转载,请注明出处： <https://securityonline.info/polaredge-botnet-2000-iot-devices-infected/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

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