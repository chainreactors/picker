---
title: 新的网络攻击以Cobalt Strike有效载荷瞄准华语企业
url: https://www.anquanke.com/post/id/299686
source: 安全客-有思想的安全新媒体
date: 2024-09-03
fetch_date: 2025-10-06T18:23:57.511515
---

# 新的网络攻击以Cobalt Strike有效载荷瞄准华语企业

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

# 新的网络攻击以Cobalt Strike有效载荷瞄准华语企业

阅读量**80951**

发布时间 : 2024-09-02 16:57:19

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：The Hacker News

原文地址：<https://thehackernews.com/2024/08/new-cyberattack-targets-chinese.html>

译文仅供参考，具体内容表达以及含义原文为准。

讲中文的用户是“高度组织和复杂的攻击”活动的目标，该活动可能利用网络钓鱼电子邮件通过 Cobalt Strike 有效载荷感染 Windows 系统。

“攻击者设法横向移动，建立了持久性，并在两周多的时间里在系统内未被发现，”Securonix 研究人员 Den Iuzvyk 和 Tim Peck 在一份新报告中说。

代号为 **SLOW#TEMPEST** 的秘密活动，未归因于任何已知的威胁行为者，从恶意 ZIP 文件开始，解压缩后会激活感染链，从而导致在受感染的系统上部署漏洞利用后工具包。

ZIP 存档附带一个 Windows 快捷方式 （LNK） 文件，它伪装成Microsoft Word 文件“违规远程控制软件人员名单.docx.lnk”，大致翻译为“违反远程控制软件规定的人员名单”。

研究人员指出：“鉴于诱饵文件中使用的语言，特定的中国相关企业或政府部门很可能成为目标，因为它们都会雇用遵守’远程控制软件法规’的个人。

LNK 文件充当启动合法 Microsoft 二进制文件（“LicensingUI.exe”）的管道，该二进制文件使用 DLL 旁加载来执行流氓 DLL（“dui70.dll”）。这两个文件都是名为“\其他信息\.\_\_MACOS\_\_\.\_MACOS\_\\_\_MACOSX\\_MACOS\_”的目录中的 ZIP 存档的一部分。此次攻击标志着首次报告通过 LicensingUI.exe 进行 DLL 旁加载。

DLL 文件是一种 Cobalt Strike 植入程序，允许对受感染主机进行持续和隐蔽的访问，同时与远程服务器 （“123.207.74[.]22″).

据说远程访问允许攻击者进行一系列动手活动，包括部署额外的有效载荷进行侦察和设置代理连接。

感染链还值得注意的是，它设置了一个计划任务来定期执行一个名为“lld.exe”的恶意可执行文件，该可执行文件可以直接在内存中运行任意 shellcode，从而在磁盘上留下最少的占用空间。

![Cobalt Strike 有效载荷]( "Cobalt Strike Payloads")

研究人员说：“攻击者通过手动提升内置 Guest 用户帐户的权限，进一步使自己能够隐藏在受感染系统的杂草中。

“这个帐户通常被禁用且权限最低，通过将其添加到关键管理组并为其分配新密码，它被转变为一个强大的接入点。这个后门允许他们以最少的检测保持对系统的访问，因为 Guest 帐户通常不会像其他用户帐户那样受到密切监控。

未知威胁行为者随后继续使用远程桌面协议 （RDP） 和通过 Mimikatz 密码提取工具获得的凭据在网络中横向移动，然后设置从每台机器返回其命令和控制 （C2） 服务器的远程连接。

利用后阶段的进一步特征是执行多个枚举命令和使用 BloodHound 工具进行 Active Directory （AD） 侦察，其结果随后以 ZIP 存档的形式泄露。

所有 C2 服务器均由深圳腾讯计算机系统有限公司托管在中国，这一事实加强了与中国的联系。最重要的是，与该活动相关的大多数文物都来自中国。

“尽管没有确凿的证据将这次攻击与任何已知的 APT 组织联系起来，但它很可能是由经验丰富的威胁行为者精心策划的，他有使用高级漏洞利用框架（如 Cobalt Strike 和各种其他漏洞利用后工具）的经验，”研究人员总结道。

“该活动的复杂性体现在它对初始入侵、持久性、权限提升和跨网络横向移动的系统方法中。”

本文翻译自The Hacker News [原文链接](https://thehackernews.com/2024/08/new-cyberattack-targets-chinese.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299686](/post/id/299686)

安全KER - 有思想的安全新媒体

本文转载自: [The Hacker News](https://thehackernews.com/2024/08/new-cyberattack-targets-chinese.html)

如若转载,请注明出处： <https://thehackernews.com/2024/08/new-cyberattack-targets-chinese.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)
* [安全热点](/tag/%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

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