---
title: HZ RAT后门软件 macOS 版本瞄准中国消息应用用户
url: https://www.anquanke.com/post/id/299581
source: 安全客-有思想的安全新媒体
date: 2024-08-29
fetch_date: 2025-10-06T17:59:23.591204
---

# HZ RAT后门软件 macOS 版本瞄准中国消息应用用户

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

# HZ RAT后门软件 macOS 版本瞄准中国消息应用用户

阅读量**96978**

发布时间 : 2024-08-28 12:51:23

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/macos-version-of-hz-rat-backdoor.html>

译文仅供参考，具体内容表达以及含义原文为准。

钉钉和微信等中国即时通讯应用程序的用户是 Apple macOS 版本名为 **HZ RAT** 的后门的目标。

卡巴斯基研究员谢尔盖·普赞（Sergey Puzan）说，这些工件“几乎完全复制了Windows版本的后门程序的功能，仅在有效载荷上有所不同，有效载荷以shell脚本的形式从攻击者的服务器接收。

HZ RAT 于 2022 年 11 月由德国网络安全公司 DCSO 首次记录，恶意软件通过自解压 zip 档案或恶意 RTF 文档分发，这些文档可能是使用 Royal Road RTF 武器化器构建的。

涉及 RTF 文档的攻击链旨在通过利用方程式编辑器中存在多年的 Microsoft Office 漏洞 （CVE-2017-11882） 来部署在受感染主机上执行的 Windows 版本的恶意软件。

另一方面，第二种分发方法伪装成合法软件（如 OpenVPN、PuTTYgen 或 EasyConnect）的安装程序，除了实际安装诱饵程序外，还执行负责启动 RAT 的 Visual Basic 脚本 （VBS）。

HZ RAT 的功能相当简单，因为它连接到命令和控制 （C2） 服务器以接收进一步的指令。这包括执行 PowerShell 命令和脚本、将任意文件写入系统、将文件上传到服务器以及发送检测信号信息。

鉴于该工具的功能有限，怀疑该恶意软件主要用于凭据收集和系统侦查活动。

有证据表明，早在 2020 年 6 月就已经在野外检测到了该恶意软件的第一次迭代。根据 DCSO 的说法，该活动本身被认为至少自 2020 年 10 月以来一直活跃。

卡巴斯基于 2023 年 7 月上传到 VirusTotal 的最新样本，它冒充了 OpenVPN Connect（“OpenVPNConnect.pkg”），一旦启动，它就会与后门中指定的 C2 服务器建立联系，以运行四个基本命令，这些命令类似于其 Windows 对应项 –

* 执行 shell 命令（例如，系统信息、本地 IP 地址、已安装的应用程序列表、来自钉钉、Google 密码管理器和微信的数据）
* 将文件写入磁盘
* 将文件发送到 C2 服务器
* 检查受害者的空闲时间

“恶意软件试图从微信获取受害者的 WeChatID、电子邮件和电话号码，”Puzan 说。“至于钉钉，攻击者对更详细的受害者数据感兴趣：用户工作的组织和部门名称、用户名、公司电子邮件地址和电话号码。”

对攻击基础设施的进一步分析表明，除了位于美国和荷兰的两台服务器外，几乎所有的 C2 服务器都位于中国。

最重要的是，据说包含 macOS 安装包（“OpenVPNConnect.zip”）的 ZIP 存档是之前从属于名为 miHoYo 的中国视频游戏开发商的域下载的，该域以 Genshin Impact 和 Honkai 而闻名。

目前尚不清楚该文件是如何上传到相关域的（“vpn.mihoyo[.]com“），如果服务器在过去某个时间点遭到入侵。该活动的广泛程度也尚不清楚，但即使在这么多年之后，后门仍在被使用的事实表明在某种程度上取得了成功。

“我们发现的 HZ Rat 的 macOS 版本表明，之前攻击背后的威胁行为者仍然活跃，”Puzan 说。“该恶意软件仅收集用户数据，但稍后可以用于在受害者的网络中横向移动，正如一些样本中存在的私有 IP 地址所表明的那样。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/macos-version-of-hz-rat-backdoor.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299581](/post/id/299581)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/macos-version-of-hz-rat-backdoor.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/macos-version-of-hz-rat-backdoor.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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