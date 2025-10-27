---
title: 勒索软件团伙利用伪装成 IP 扫描仪的新型 RAT 攻击 IT 工作者
url: https://www.anquanke.com/post/id/298902
source: 安全客-有思想的安全新媒体
date: 2024-08-08
fetch_date: 2025-10-06T17:59:26.770819
---

# 勒索软件团伙利用伪装成 IP 扫描仪的新型 RAT 攻击 IT 工作者

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

# 勒索软件团伙利用伪装成 IP 扫描仪的新型 RAT 攻击 IT 工作者

阅读量**78605**

发布时间 : 2024-08-07 15:40:59

**x**

##### 译文声明

本文是翻译文章，文章原作者 Zeljka Zorz，文章来源：HELPNETSECURITY

原文地址：<https://www.helpnetsecurity.com/2024/08/06/ransomware-targets-it-workers/>

译文仅供参考，具体内容表达以及含义原文为准。

勒索软件即服务机构 Hunters International 正在使用一种新的远程访问木马 （RAT）。Quorum Cyber 研究人员发现：“由于使用 C# 编程语言，该恶意软件被命名为 SharpRhino，它通过冒充合法工具 Angry IP Scanner 的域名进行传播。

Angry IP Scanner 是一个 IP 地址和端口扫描器，因此更有可能被 IT 工作者下载和使用。这种特定的针对性可能是试图破坏具有更高权限并可以访问企业网络大多数角落和缝隙的系统和帐户，以便威胁参与者可能会四处乱窜造成很大的损害。

这些目标是如何最终出现在域名被抢注的域名上的，目前尚不清楚，但恶意广告似乎是最有可能的理论。

今年早些时候，一个恶意广告活动同样通过 Google 系统实用程序广告针对 IT 专业人员，并传播了 Nitrogen 恶意软件。

### The SharpRhino RAT

包含 RAT 的恶意文件的名称 – *ipscan-3.9.1-setup.exe* – 使其看起来像是它试图冒充的软件的合法安装程序（俗称 ipscan）。

![Ransomware targets IT workers]( "The contents of the malicious installer (Source: Quorum Cyber)")

恶意安装程序的内容（来源：Quorum Cyber）

该文件是一个 NSIS 安装程序，它修改 Windows 注册表以实现持久性，并创建 *Microsoft.AnyKey.exe* 的快捷方式，然后执行*LogUpdate.bat*文件。

该文件包含一个 PowerShell 脚本，该脚本编译 C# 代码并将编译后的二进制文件加载到内存中，其中的函数已准备好被调用。

该恶意软件还使用相同的文件建立两个目录，即使找到并删除了其中一个目录，攻击者也可以向 RAT 发送命令。

### 关于Hunters International

“到目前为止，猎人国际已声称对 2024 年前七个月的 134 起袭击事件负责。作为典型的勒索软件运营商，Hunters International 在加密文件、将文件扩展名更改为 *.locked* 并留下 README 消息之前从受害组织泄露数据，引导收件人到 TOR 网络上的聊天门户以获取付款说明，“研究人员指出。

其目标主要是位于美洲、欧洲和澳大利亚的组织。该组织避免在受俄罗斯影响的独立国家联合体（CIS）内的组织，这表明该组织与俄罗斯有附属关系。

本文翻译自HELPNETSECURITY [原文链接](https://www.helpnetsecurity.com/2024/08/06/ransomware-targets-it-workers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298902](/post/id/298902)

安全KER - 有思想的安全新媒体

本文转载自: [HELPNETSECURITY](https://www.helpnetsecurity.com/2024/08/06/ransomware-targets-it-workers/)

如若转载,请注明出处： <https://www.helpnetsecurity.com/2024/08/06/ransomware-targets-it-workers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索软件](/tag/%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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