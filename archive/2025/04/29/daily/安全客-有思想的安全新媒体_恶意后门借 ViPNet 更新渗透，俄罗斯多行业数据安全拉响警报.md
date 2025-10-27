---
title: 恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报
url: https://www.anquanke.com/post/id/306951
source: 安全客-有思想的安全新媒体
date: 2025-04-29
fetch_date: 2025-10-06T22:04:20.154046
---

# 恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报

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

# 恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报

阅读量**104398**

发布时间 : 2025-04-28 10:22:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Kaaviya，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/malware-networking-software-updates/>

译文仅供参考，具体内容表达以及含义原文为准。

在 2025 年 4 月的一次网络安全调查中，发现了一个针对俄罗斯政府、金融和工业等多个大型组织的复杂后门程序。

该恶意软件伪装成 ViPNet 安全网络软件的合法更新程序，使攻击者能够窃取敏感数据，并在被攻陷的系统上部署更多恶意组件。

****高级威胁态势****

这个后门程序专门针对连接到 ViPNet 网络的计算机，ViPNet 是俄罗斯一款用于创建安全网络的流行软件套件。

网络安全专家已确定，该恶意软件被封装在 LZH 压缩包中进行分发，这些压缩包被设计成模仿合法的 ViPNet 更新程序，其中包含合法文件和恶意文件。

一位熟悉此次调查的资深网络安全分析师表示：“这次攻击表明，威胁行为者的手段越来越复杂，他们利用了人们信任的软件更新机制。”

恶意压缩包包含几个组件：一个 action.inf 文本文件、一个合法的 lumpdiag.exe 可执行文件、一个恶意的 msinfo32.exe 可执行文件，以及一个加密的有效载荷文件，在不同的压缩包中该文件名称各异。

此次攻击利用了一种路径替换技术 —— 当 ViPNet 更新服务处理该压缩包时，它会使用特定参数执行合法文件，这随后会触发恶意的 msinfo32.exe 文件的执行。

一旦激活，该后门程序就会通过 TCP 协议与命令控制（C2）服务器建立连接，使攻击者能够从受感染的计算机中窃取文件，并执行更多恶意组件。

这一发现正值网络间谍活动日益增多之际。最近的报告发现，新的高级持续性威胁（APT）组织正积极利用复杂的技术，以云服务和公共平台作为命令控制基础设施，来攻击政府实体。

在其他地方也观察到了类似的由国家支持的黑客攻击模式，这些网络攻击与针对关键机构的更广泛活动有关。

ViPNet 的开发者已确认了针对其用户的这些定向攻击，并发布了安全更新和建议，以减轻威胁。

网络安全专家强调，随着高级持续性威胁（APT）组织的战术变得越来越复杂，各组织必须实施多层防御策略。

强烈建议使用 ViPNet 网络解决方案的组织采取以下措施：

1.在安装更新之前验证更新的真实性。

2.实施严格的访问控制。

3.定期监控网络流量，查找可疑活动。

4.确保安全解决方案能够检测到如 HEUR:Trojan.Win32.Loader.gen 这样的威胁。

安全研究人员认为，分享这些初步调查结果将有助于处于风险中的组织针对这种利用人们信任的更新机制来渗透安全网络的新出现的威胁，迅速采取防护措施。

****受攻击指标****

SHA256 哈希值

018AD336474B9E54E1BD0E9528CA4DB5
28AC759E6662A4B4BE3E5BA7CFB62204
77DA0829858178CCFC2C0A5313E327C1
A5B31B22E41100EB9D0B9A27B9B2D8EF
E6DB606FA2B7E9D58340DF14F65664B8

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/malware-networking-software-updates/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306951](/post/id/306951)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/malware-networking-software-updates/)

如若转载,请注明出处： <https://cybersecuritynews.com/malware-networking-software-updates/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

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