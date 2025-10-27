---
title: 以色列NSO Group公司利用WhatsApp漏洞部署间谍软件展开APT网络攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492485&idx=1&sn=34cb96ae174f9f538a189541e923423a&chksm=e90dc9afde7a40b9a9fbbd74a45b7d9d4125bcc18dfcdad745f47c36a2b3b575db7f8407fa99&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-12-26
fetch_date: 2025-10-06T19:39:59.416763
---

# 以色列NSO Group公司利用WhatsApp漏洞部署间谍软件展开APT网络攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 以色列NSO Group公司利用WhatsApp漏洞部署间谍软件展开APT网络攻击

BaizeSec

白泽安全实验室

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIOKDEKmiaiaKYfZOvSPcXOL9qLuNxib7lZVZFQTkAMTTPb6wAt8mpLcgTS8dxhxPIo20Seb5sH7Kz5DQ/640?wx_fmt=png&from=appmsg)

近期，一起Meta（前Facebook）旗下的WhatsApp和以色列NSO Group公司的法律诉讼引起了国际社会的广泛关注。这场诉讼不仅关系到个人隐私权的保护，也暴漏了以色列NSO Group公司和一些国家政府部门合作，展开目标明确的APT攻击行为。

**一、事件背景概述**

2019年10月29日，WhatsApp向美国法院提起诉讼，指控以色列公司NSO Group利用WhatsApp的音频通话漏洞，在其用户不知情的情况下，向大约1400部手机和设备部署Pegasus间谍软件。WhatsApp声称，超过100名的人权捍卫者、记者和“其他民间社会成员”被该恶意软件盯上，同时还有政府官员和外交官。

NSO Group是以色列的一家网络安全企业，成立于2010年。公司在全球雇佣了700多名员工，其中几乎所有研究团队成员都是以色列前军事情报人员，大多数曾在以色列军事情报总局服役，许多人在其8200部队中服役。公司主要开发数字间谍工具，其产品能够追踪智能手机上的任何活动，主要为世界各国政府和执法机构提供服务。NSO Group最知名的产品是Pegasus间谍软件，该软件能够对智能手机进行远程零点击监控。Pegasus与iPhone和Android设备兼容，可以远程部署，部署后允许客户端访问目标手机的数据和传感器，包括位置数据、文本、电子邮件、社交媒体消息、文件、相机和麦克风。

NSO Group被披露过多起事件，例如：

2016年8月，Citizen Lab首次公开披露了Pegasus间谍软件，Pegasus软件对iPhone设备实施攻击，利用3个当时未被发现的iOS系统“0day”漏洞实施间谍活动；

2017年11月，Pegasus通过短信链接进行攻击的事件被记录。这些攻击通过发送包含恶意链接的短信，一旦目标点击链接，就可以在无需用户交互的情况下悄悄感染目标设备。

**2019年5月，WhatsApp被发现其语音电话功能藏有一个重大漏洞，该漏洞允许攻击者将一款被称为Pegasus的恶意软件悄然安装到用户的iPhone和Android设备上。**

2021年7月，Pegasus间谍软件“监听门”事件成为国际焦点，涉及多国元首和政界要员，包括法国总统马克龙等至少14位政界重量级人物。

WhatsApp是一款全球知名的即时通讯软件，由美国的WhatsApp Inc.公司开发并于2009年发布。起初，他们的目标是为用户提供一种简单、快速且安全的通讯方式，尤其是在移动互联网普及程度不高的发展中国家。随着时间的推移，WhatsApp逐渐成为全球范围内最受欢迎的通讯应用之一，月活跃用户数量超过20亿。2014年时，Facebook（现Meta）以大约190亿美元的价格收购了WhatsApp，使其成为公司的重要组成部分之一。

**二、攻击过程技术分析**

Pegasus是一款高级的间谍软件，能够远程感染目标设备，无需用户交互即可安装。它能够访问设备上的所有数据，包括短信、通话记录、联系人、位置信息、电子邮件以及社交媒体应用的数据。Pegasus还可以控制设备的麦克风和摄像头，进行实时监控。

CVE-2019-3568是一个严重的缓冲区溢出漏洞，存在于WhatsApp的VOIP（Voice over Internet Protocol）堆栈中。这个漏洞允许攻击者通过发送一系列特制的RTCP（Real-time Transport Control Protocol）数据包到目标手机号码，实现远程代码执行。整个攻击过程无需用户交互，影响了多个平台的WhatsApp版本。

**攻击过程技术分析：**

Pegasus间谍软件的攻击过程分为三个阶段，每个阶段都利用特定的技术手段来实现对目标设备的控制。

* **第一阶段：初始感染**

Pegasus间谍软件通过发送带有恶意链接的短信或社交媒体消息来感染目标设备。这些链接指向一个精心制作的网页，该网页利用设备的零日漏洞来安装恶意软件。在本案例中，Pegasus利用了WhatsApp的VOIP堆栈中的CVE-2019-3568漏洞，该漏洞允许攻击者通过发送特制的RTCP数据包到目标手机号码，实现远程代码执行。攻击者通过WhatsApp发送一个包含“安装向量”的“密码文件”给目标用户，利用WhatsApp的漏洞在目标设备上安装Pegasus间谍软件。

* **第二阶段：远程越狱**

在第一阶段成功利用漏洞后，根据受害者设备（32位或64位）下载相应的加密混淆包。这些包包含iOS内核漏洞（如CVE-2016-4656和CVE-2016-4657）的利用代码，以及一个用于下载解密第三阶段软件包的loader。这一阶段实现了设备的远程越狱，为安装间谍软件做准备。

* **第三阶段：恶意软件安装**

经过第二阶段的越狱，第三阶段中，攻击者将Pegasus间谍软件安装到设备上。该软件能够hook到目标应用程序，如Gmail、Facetime、Facebook、WeChat等，实现对受害者设备的全面监控和数据收集。在本案例中，即使在WhatsApp检测并修补了CVE-2019-3568漏洞后，NSO Group仍然开发了另一种安装向量（称为Erised），继续利用WhatsApp服务器来安装Pegasus间谍软件。

**攻击技术细节分析：**

* **零日漏洞利用**

Pegasus利用未公开的漏洞（零日漏洞）来绕过设备的安全防护，这些漏洞可能涉及浏览器、操作系统内核或预装应用程序。

* **隐蔽性**

Pegasus设计得非常隐蔽，它能够在不触发任何安全警报的情况下运行，并且能够自我删除以避免被发现。

* **持久性**

即使设备重启，Pegasus也能够保持在设备上，继续执行其监控任务。

* 数据加密

Pegasus在传输数据时使用强加密，以防止数据在传输过程中被拦截。

* **反取证技术**

Pegasus可能使用反取证技术来隐藏其存在，使得即使设备被检查，也很难发现其痕迹。

* **进程注入**

Pegasus通过进程注入技术，如converter，来实现对设备更深层次的控制和数据窃取。

**三、事件总结分析**

通过本案例的深入分析，可以观察到以色列网络安全公司开发的间谍软件，在全球范围内的商业化和政治化趋势日益明显。尤其是以色列政府对Pegasus软件的销售的控制，并将其作为外交政策的一部分，这进一步突显了该软件在国际政治中的敏感性和影响力。因此，以色列这家NSO Group公司不仅在技术上展现出强大的漏洞挖掘和网络攻击能力，而且在商业化和政治化趋势上也愈发明显，对社会、政治乃至国际关系都产生了深远的影响。

Pegasus间谍软件以其强大的功能和隐蔽性而闻名，能够破解苹果或安卓智能手机的加密通信，并获取目标设备上的所有数据和传感器信息，包括位置、通信记录、社交媒体消息、文件、相机和麦克风等。这款软件可以无感模式下感染手机，秘密安装在运行大多数版本的iOS和Android的手机（和其他设备）上。其攻击事件经媒体曝光后，国际舆论一片哗然，在国际社会引起轩然大波，影响巨大，被称为2021年度的一大标志性事件。

间谍软件的政治化趋势在全球范围内引起了广泛关注。例如，Pegasus间谍软件被曝光监听了包括法国总统马克龙在内的多位国家元首和政界要员。这种监视活动的目标具有鲜明的政治指向性，不仅侵犯了个人隐私，也对国际政治关系造成了影响。此外，以色列警方被曝光使用Pegasus软件监控内塔尼亚胡的儿子和顾问，进一步显示了间谍软件在政治斗争中的使用，加剧了全球网络安全的紧张局势。

参考链接：

https://techcrunch.com/2024/12/23/whatsapp-scores-historic-victory-against-nso-group-in-long-running-spyware-hacking-case/

https://securityaffairs.com/172247/laws-and-regulations/u-s-court-rules-against-nso-group-whatsapp-lawsuit.html

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过