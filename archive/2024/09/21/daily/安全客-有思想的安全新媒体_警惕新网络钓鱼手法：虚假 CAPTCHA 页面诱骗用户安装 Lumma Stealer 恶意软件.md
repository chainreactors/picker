---
title: 警惕新网络钓鱼手法：虚假 CAPTCHA 页面诱骗用户安装 Lumma Stealer 恶意软件
url: https://www.anquanke.com/post/id/300236
source: 安全客-有思想的安全新媒体
date: 2024-09-21
fetch_date: 2025-10-06T18:24:53.828677
---

# 警惕新网络钓鱼手法：虚假 CAPTCHA 页面诱骗用户安装 Lumma Stealer 恶意软件

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

# 警惕新网络钓鱼手法：虚假 CAPTCHA 页面诱骗用户安装 Lumma Stealer 恶意软件

阅读量**132794**

发布时间 : 2024-09-20 14:34:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 瓦卡斯，文章来源：hackread

原文地址：<https://hackread.com/fake-captcha-verification-pages-lumma-stealer-malware/#google_vignette>

译文仅供参考，具体内容表达以及含义原文为准。

一个新的网络钓鱼活动使用虚假的 CAPTCHA 验证页面来诱骗 Windows 用户运行恶意 PowerShell 命令、安装 Lumma Stealer 恶意软件并窃取敏感信息。随时了解和保护。

CloudSec 的网络安全研究人员发现了一种新的网络钓鱼活动，该活动诱骗用户通过虚假的人工验证页面运行恶意命令。该活动主要针对 Windows 用户，旨在安装 **Lumma Stealer 恶意软件**，导致敏感信息被盗。

#### 攻击的工作原理

威胁行为者正在创建托管在各种平台上的网络钓鱼网站，包括 Amazon S3 存储桶和内容分发网络 （CDN）。这些网站模仿合法的验证页面，例如虚假的 **Google CAPTCHA** 页面。当用户单击 “Verify” 按钮时，他们会看到不寻常的指示：

1. **打开“运行”对话框 （Win+R）**
2. **按 Ctrl+V**
3. **按 Enter 键**

在用户不知道的情况下，这些操作会执行一个隐藏的 JavaScript 函数，该函数将 base64 编码的 PowerShell 命令复制到剪贴板。当用户粘贴并运行命令时，它会从远程服务器下载 Lumma Stealer 恶意软件。

CloudSec 在周四发布之前与 Hackread.com 分享的**报告**显示，下载的恶意软件通常会下载额外的恶意组件，这使得检测和删除变得更加困难。虽然目前用于传播 Lumma Stealer，但这种技术可以轻松适应提供其他类型的恶意软件。

![传播 Lumma Stealer 恶意软件的虚假 CAPTCHA 验证页面]()

当用户点击虚假的 Google CAPTCHA 提示时触发攻击流和虚假验证过程（截图：CloudSec）

供您参考，Lumma Stealer 旨在从受感染的设备中窃取敏感数据。虽然目标的具体数据可能有所不同，但通常包括登录凭据、财务信息和个人文件。就在这次最新的活动是在恶意软件被发现伪装成 **OnlyFans 黑客工具**感染其他黑客的设备几天后进行的。

**2024 年 1 月**，发现 Lumma 通过受感染的 YouTube 频道分发的破解软件进行传播。早些时候，**在 2023 年 11 月**，研究人员发现了 LummaC2 的新版本，称为 LummaC2 v4.0，它使用三角技术来窃取用户数据来检测人类用户。

> 我在此确认。https://t.co/1q4cARQLDM pic.twitter.com/GEBzqJeaSs
>
> — 瓦卡斯 （@WAK4S） 2023 年 12 月 31 日

### **现在怎么办？**

既然已经报道了新的 Lumma 窃取者感染狂潮，企业和毫无戒心的用户需要保持警惕，避免陷入最新的虚假验证骗局。以下是一些常识性规则和简单而必要的提示，用于防范 Lumma 和其他类似的窃取者：

* **教育自己和他人：**与朋友、家人和同事分享这些信息，以提高对这种新威胁的认识。
* **警惕不寻常的验证请求：**合法网站很少要求用户通过 “Run” 对话框执行命令。对任何提出此类请求的网站保持警惕。
* **不要复制和粘贴未知命令：**避免从不受信任的来源复制和粘贴任何内容，尤其是要在终端或命令提示符下运行的命令。
* **保持软件更新：**确保您的操作系统和防病毒软件是最新的，以修补已知漏洞。
* **重要：**关注 Hackread.com 了解最新的网络安全新闻。

本文翻译自hackread [原文链接](https://hackread.com/fake-captcha-verification-pages-lumma-stealer-malware/#google_vignette)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/300236](/post/id/300236)

安全KER - 有思想的安全新媒体

本文转载自: [hackread](https://hackread.com/fake-captcha-verification-pages-lumma-stealer-malware/#google_vignette)

如若转载,请注明出处： <https://hackread.com/fake-captcha-verification-pages-lumma-stealer-malware/#google_vignette>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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