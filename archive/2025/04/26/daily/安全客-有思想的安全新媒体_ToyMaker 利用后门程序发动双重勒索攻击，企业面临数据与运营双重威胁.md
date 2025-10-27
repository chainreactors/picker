---
title: ToyMaker 利用后门程序发动双重勒索攻击，企业面临数据与运营双重威胁
url: https://www.anquanke.com/post/id/306879
source: 安全客-有思想的安全新媒体
date: 2025-04-26
fetch_date: 2025-10-06T22:04:00.624148
---

# ToyMaker 利用后门程序发动双重勒索攻击，企业面临数据与运营双重威胁

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

# ToyMaker 利用后门程序发动双重勒索攻击，企业面临数据与运营双重威胁

阅读量**76010**

发布时间 : 2025-04-25 11:04:12

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/toymaker-hackers-compromised-multitude-hosts/>

译文仅供参考，具体内容表达以及含义原文为准。

2023 年，网络安全专家发现，一个技术高超的威胁行为者组织对关键基础设施企业造成了大规模的安全侵害。

这个被称为 ToyMaker 的初始访问中间人，在部署定制后门程序从受害企业中提取凭据之前，系统地利用了面向互联网的易受攻击系统。

他们的攻击方法包括精心策划，使用 SSH 文件传输实用程序和远程管理工具，以保持对被攻陷网络的持续访问。

该威胁行为者的主要目标似乎是出于经济利益，ToyMaker 先建立初始访问权限，然后将控制权转移给二级行为者，特别是 Cactus 勒索软件组织。

ToyMaker 和 Cactus 之间的这种关系，反映了网络犯罪生态系统中一个令人担忧的趋势，即专门的组织专注于攻击链中的特定环节，而不是自行执行端到端的攻击操作。

Cisco Talos 的研究人员识别出了 ToyMaker 的标志性后门程序，名为 “LAGTOY”，它为受感染系统提供了远程访问功能。

这个后门程序使威胁行为者能够建立反向 Shell，并在被攻陷的终端上执行任意命令。

在提取凭据之后，ToyMaker 通常会将访问权限移交给 Cactus 团伙，后者随后会部署勒索软件，并采用双重勒索策略。

感染链条始于 ToyMaker 利用面向互联网的易受攻击服务器，随后通过快速侦察命令收集系统信息。

攻击者随后会创建假的用户账户，通常命名为 “support”，并将其添加到管理组中。调查显示，ToyMaker 在部署其凭据窃取工具之前，会使用 Windows OpenSSH 软件包在被攻陷的终端上建立监听器。

****LAGTOY 后门：技术分析****

LAGTOY，也被美国网络安全公司 Mandiant 称为 “HOLERUN”，是 ToyMaker 武器库中的主要持续性威胁工具。

这个后门程序被设计为定期连接到硬编码的命令与控制（C2）服务器，在受感染的系统上接收并执行命令。

该恶意软件作为一个名为 “WmiPrvSV” 的 Windows 服务运行，并采用基本的反调试技术来逃避分析。

这个后门程序的执行逻辑是通过 443 端口与它的 C2 服务器建立通信，不过值得注意的是，它并不使用传输层安全（TLS）加密。

相反，它使用原始套接字连接，使其能够绕过标准的加密检查机制。

if ( v1 )

{

memset(MultiByteStr, 0, 0x1820ui64);

v2 = v1;

v3 = v7 + 2i64 \* v1 – 2;

if ( v1 != 1 || \*(\_WORD \*)v3 != 10 && \*(\_WORD \*)v3 != 13 )

{

do

{

v4 = \*(\_WORD \*)v3;

v3 -= 2i64;

if ( v4 == 10 || v4 == 13 )

\*(\_WORD \*)(v3 + 2) = 0;

–v2;

}

while ( v2 );

LAGTOY 的命令结构揭示了三个主要的控制代码：“#pt” 用于停止服务，“#pd” 用于中断执行链，“#ps” 用于创建进程或执行命令。

该恶意软件实现了一种独特的基于时间的执行逻辑，使其能够确定何时执行命令以及何时进入休眠状态。

这种机制包括一个看门狗例程，如果运行时间超过 60 分钟，该例程会重新初始化连接，这显示出了其复杂的持续性能力。

LAGTOY 实现的整体时间安排和 C2 通信逻辑表明，该恶意软件能够处理来自 C2 的三条命令，并且命令之间的休眠间隔为 11000 毫秒。

这种精心设计的通信模式有助于在保持威胁行为者操作效率的同时，最大限度地减少被检测到的可能性。

在建立访问权限后，ToyMaker 通常会潜伏大约三周时间，然后 Cactus 的操作人员会接管访问权限，部署他们自己的工具集用于横向移动、数据渗出，最终部署勒索软件 —— 这展示了现代网络犯罪活动日益细化分工的特点。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/toymaker-hackers-compromised-multitude-hosts/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306879](/post/id/306879)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/toymaker-hackers-compromised-multitude-hosts/)

如若转载,请注明出处： <https://cybersecuritynews.com/toymaker-hackers-compromised-multitude-hosts/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**9赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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