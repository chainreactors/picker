---
title: 黑客利用交换文件对Magento网站进行电子浏览攻击
url: https://www.anquanke.com/post/id/298252
source: 安全客-有思想的安全新媒体
date: 2024-07-25
fetch_date: 2025-10-06T17:41:26.955947
---

# 黑客利用交换文件对Magento网站进行电子浏览攻击

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

# 黑客利用交换文件对Magento网站进行电子浏览攻击

阅读量**58745**

发布时间 : 2024-07-24 14:38:26

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/166073/malware/threat-actors-abused-swap-files-e-skimming.html>

译文仅供参考，具体内容表达以及含义原文为准。

## ![]()

## 威胁行为者滥用了被攻陷的Magento网站中的交换文件（swap files）来隐藏信用卡嗅探器并窃取支付信息。

Sucuri的安全研究人员观察到，威胁行为者在被攻陷的Magento网站中利用交换文件来隐藏一个持久性的软件嗅探器，以窃取支付信息。

攻击者使用这种策略来维持持久性，并让恶意软件在多次清理尝试后仍能存活。

研究人员在被攻陷网站的结账页面上发现了一个可疑脚本，该脚本具有所有典型的恶意软件特征。脚本中包含了base64编码的变量和十六进制编码的字符串。专家们解码了脚本，并确定它被用来捕获信用卡详情。

![]()

当点击结账按钮时，一个脚本通过querySelectorAll函数捕获信用卡数据。此脚本还收集敏感信息，如姓名、地址和卡号。被盗的信息被发送到域名amazon-analytic[.]com，该域名注册于2024年2月，已被用于其他信用卡盗窃案件中。攻击者经常在域名中使用知名品牌的名称，试图逃避检测。

在分析恶意脚本时，专家注意到一个有趣的“swapme”文件引用。虽然最初是不可见的，但使用命令揭示了一个包含与感染脚本相同恶意软件的交换文件。攻击者利用这个交换文件来在服务器上保留恶意软件并逃避检测。在移除交换文件并清空缓存后，结账页面变得干净。

“swapme”作为文件名的一部分提示我们可能有些交换文件残留在周围。当文件直接通过SSH编辑时，服务器会创建一个临时的‘swap’版本，以防编辑器崩溃，这可以防止全部内容丢失。”Sucuri发布的报告中写道。

“虽然我们无法通过ls命令看到任何~swapme文件，但通过在bootstrap.php-swapme上运行vi命令直接编辑交换文件，我们发现该文件确实存在，且包含与受感染的bootstrap.php版本完全相同的内容。很明显，攻击者正利用交换文件来保持恶意软件在服务器上的存在，并逃避常规的检测方法。”

攻击者滥用交换文件系统突显了除了基本扫描之外采取更深层次安全措施的必要性。交换文件的存在表明攻击者最初可能是通过SSH或终端会话访问被攻陷的网站。为了防止此类持久性恶意软件感染，应限制sFTP、SSH、FTP和CPanel仅对可信IP开放，配置FTP和SSH限制在托管服务器上，并使用网站防火墙提供额外保护。专家也建议定期更新您的CMS和插件，以避免被自动化攻击工具利用的漏洞。

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/166073/malware/threat-actors-abused-swap-files-e-skimming.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298252](/post/id/298252)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/166073/malware/threat-actors-abused-swap-files-e-skimming.html)

如若转载,请注明出处： <https://securityaffairs.com/166073/malware/threat-actors-abused-swap-files-e-skimming.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

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

* [威胁行为者滥用了被攻陷的Magento网站中的交换文件（swap files）来隐藏信用卡嗅探器并窃取支付信息。](#h2-1)

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