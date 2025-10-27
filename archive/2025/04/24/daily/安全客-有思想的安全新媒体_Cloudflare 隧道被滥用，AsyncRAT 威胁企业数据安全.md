---
title: Cloudflare 隧道被滥用，AsyncRAT 威胁企业数据安全
url: https://www.anquanke.com/post/id/306818
source: 安全客-有思想的安全新媒体
date: 2025-04-24
fetch_date: 2025-10-06T22:04:21.003436
---

# Cloudflare 隧道被滥用，AsyncRAT 威胁企业数据安全

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

# Cloudflare 隧道被滥用，AsyncRAT 威胁企业数据安全

阅读量**57285**

发布时间 : 2025-04-23 11:24:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 securityonline，文章来源：securityonline

原文地址：<https://securityonline.info/unveiling-a-multi-stage-malware-attack-cloudflare-abuse-and-asyncrat-delivery/>

译文仅供参考，具体内容表达以及含义原文为准。

![Infection chains distributing AsyncRAT]()

分发 AsyncRAT 的感染链  图片来源： Sekoia

在 Sekoia 威胁检测与研究（TDR）团队的一份详细报告中，研究人员揭示了一个复杂的恶意软件传播基础设施，该设施滥用了 Cloudflare 隧道服务来部署远程访问木马（RAT），尤其是 AsyncRAT。这个基础设施至少从 2024 年 2 月起就开始运作，并且在精心设计的复杂感染链的助力下不断演变，这些感染链旨在绕过检测工具并渗透到企业环境中。

研究人员指出：“相关的感染链特别复杂，涉及多个步骤，并且在不同的攻击活动中还观察到了一些差异。”

攻击始于一封网络钓鱼电子邮件 —— 通常伪装成发票或采购订单 —— 其中包含一个恶意的 Windows 库文件（.ms-library）。虽然这种格式在现代环境中不常用，但由于其非可执行文件的外观，它能够绕过过滤器。

![]()

网络钓鱼电子邮件示例  图片来源： Sekoia

.ms-library 文件引用了一个远程 WebDav 资源，当该资源被打开时，会启动一个伪装成 PDF 快捷方式（LNK 文件）的文件下载。

一旦点击了 LNK 文件，一系列脚本和有效载荷就会依次展开：

1.LNK 文件下载并执行一个 HTA 文件。

2.这个 HTA 文件（用 VBScript 编写）会启动一个 BAT 脚本。

3.BAT 脚本安装 Python 并执行另一个 BAT 阶段的操作。

4.最后，恶意软件会注入到 notepad.exe 中，并建立持久化。

攻击者使用一个 Python 脚本将下一个有效载荷注入到多个记事本（Notepad）进程中，并通过 Windows 启动文件夹建立持久化，会释放两个.vbs 文件和另一个.bat 文件。

![]()

可疑图像和隐藏的 base64 代码  图片来源： Sekoia

最终的有效载荷 ——AsyncRAT—— 是经过 Base64 编码的，并隐藏在一个从公共网站下载的.jpg 图像中。这个图像通过 PowerShell 以反射方式加载，在内存中执行，以避免被磁盘检测到。

命令与控制（C2）通信是通过动态域名系统（DNS）域名建立的，常常利用dyndns.org，并且其基础设施隐藏在使用 TryCloudflare 的 Cloudflare 隧道后面。

这条恶意软件感染链配备了多种规避技术：

1.进行开发环境检查，以避免在沙箱环境中触发。

2.在安装 Python 后，通过 attrib.exe 创建隐藏文件夹。

3.滥用具有检测规避意识的 LNK 文件和 HTA 文件。

4.使用动态 DNS 实现可靠的命令与控制（C2）服务器轮换。

Sekoia 的检测系统采用了以下规则：

1.HTA 感染链。

2.Mshta（微软 HTML 应用程序主机）的可疑子进程。

3.与动态 DNS 进行了通信。

4.ISO LNK 感染链。

5.使用 attrib.exe 隐藏文件。

这些规则是他们开源的 Sigma 规则集的一部分。

这次攻击活动展示了多阶段恶意软件攻击日益复杂的趋势。通过将网络钓鱼、不常见的文件格式、反射式 PowerShell 加载器以及像 Cloudflare 和 Telegram 这样的合法服务结合起来，攻击者成功地避开了用户的怀疑和终端安全防护。

威胁检测与研究（TDR）团队总结认为，虽然攻击者的最终目标很可能是窃取数据，但首要重点应该放在早期检测上 —— 尤其是在管理脚本和动态 DNS 较为常见的环境中。

随着攻击者在利用合法基础设施方面变得更具创意，防御者必须采用分层检测策略，并监控一些细微的迹象，比如意外的.vbs 或.jpg 文件下载触发了 PowerShell 操作等情况。

本文翻译自securityonline [原文链接](https://securityonline.info/unveiling-a-multi-stage-malware-attack-cloudflare-abuse-and-asyncrat-delivery/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306818](/post/id/306818)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/unveiling-a-multi-stage-malware-attack-cloudflare-abuse-and-asyncrat-delivery/)

如若转载,请注明出处： <https://securityonline.info/unveiling-a-multi-stage-malware-attack-cloudflare-abuse-and-asyncrat-delivery/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**6赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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