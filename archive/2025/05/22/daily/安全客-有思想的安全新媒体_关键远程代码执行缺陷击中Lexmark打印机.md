---
title: 关键远程代码执行缺陷击中Lexmark打印机
url: https://www.anquanke.com/post/id/307605
source: 安全客-有思想的安全新媒体
date: 2025-05-22
fetch_date: 2025-10-06T22:26:50.577551
---

# 关键远程代码执行缺陷击中Lexmark打印机

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

# 关键远程代码执行缺陷击中Lexmark打印机

阅读量**32410**

发布时间 : 2025-05-21 15:26:35

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/critical-remote-code-execution-flaw-hits-lexmark-printers/>

译文仅供参考，具体内容表达以及含义原文为准。

![CVE-2025-1126 Lexmark,远程代码执行]()

Lexmark发布了针对关键漏洞的安全公告——CVE-2025-1127——影响其各种打印机型号。该漏洞是Lexmark设备嵌入式Web服务器中Path Traversal和Concurrent Execution漏洞的组合,可能允许攻击者远程执行任意代码。

DEVCORE研究团队的研究人员与Trend Micro的零日计划(ZDI)合作发现,这个漏洞对Lexmark打印机广泛部署的企业环境构成了严重风险。

*“在各种Lexmark设备中的嵌入式Web服务器中存在相结合的Path Traversal和Concurrent Execution漏洞*[,”该咨询解释说。](https://support.lexmark.com/content/dam/support/collateral/security-alerts/CVE-2025-1127.pdf)

根据该咨询,该漏洞可以通过网络利用,CVSSv3基本得分为9.1。

如果成功利用,攻击者可以在设备上远程执行任意代码。

这为劫持打印机,访问内部网络,窃取文档或使用设备作为更大入侵活动的枢轴点打开了大门。

大量 Lexmark 打印机型号和固件版本受到影响。如果您的设备运行固件版本。240.205或更早,则可能易受攻击。受影响的系列包括:CX950,MX953,CX961,CS963,MS531,CX532,CX930,MX931,MS622,MX421,XM1246,CS720,CS921等等。

要检查固件版本:“从操作程序面板中选择’设置’→’报告’→’菜单设置页面’。

Lexmark 建议用户根据型号立即更新固件到版本 .240.206 或更高版本。

*如果固件更新不能立即应用:“在设备上设置管理密码……*将阻止不受信任的用户执行此漏洞。

固件更新可以通过 [Lexmark](https://www.lexmark.com/en_us/technical-support.html) 技术支持获得。

Lexmark 不知道该漏洞对 Lexmark 产品有任何恶意使用。然而,鉴于危急性质和广泛的攻击面,建议组织毫不拖延地采取行动。

本文翻译自securityonline [原文链接](https://securityonline.info/critical-remote-code-execution-flaw-hits-lexmark-printers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/307605](/post/id/307605)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/critical-remote-code-execution-flaw-hits-lexmark-printers/)

如若转载,请注明出处： <https://securityonline.info/critical-remote-code-execution-flaw-hits-lexmark-printers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

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

* ##### [ISC.AI 2025创新独角兽沙盒大赛开启，政产学研共举创新势力](/post/id/308810)

  2025-06-23 17:47:17
* ##### [与“AI”同行，和ISC.AI共启新篇](/post/id/308800)

  2025-06-23 17:37:20
* ##### [手慢无！ISC.AI 2025 早鸟票100张限时6折，赠泡泡玛特乐园门票](/post/id/308736)

  2025-06-20 18:22:35
* ##### [航空公司向国土安全局出售乘客数据](/post/id/308408)

  2025-06-12 15:39:51
* ##### [美国政府疫苗网站被人工智能生成的内容污损](/post/id/308404)

  2025-06-12 15:36:04
* ##### [美国CISA警告 SinoTrack GPS 跟踪器存在远程控制漏洞](/post/id/308398)

  2025-06-12 15:15:38
* ##### [安全行动： 国际刑警组织在打击网络犯罪的重大行动中摧毁了 20,000 多个恶意 IP](/post/id/308395)

  2025-06-12 14:43:06

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