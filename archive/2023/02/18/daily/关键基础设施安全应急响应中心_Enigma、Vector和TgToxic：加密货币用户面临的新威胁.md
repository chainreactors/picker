---
title: Enigma、Vector和TgToxic：加密货币用户面临的新威胁
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247534528&idx=3&sn=1f117c450dec797294ff5a39e4cf217a&chksm=c1e9cb91f69e42879d053c27e67211bc02430d8c8f813c8ebeb280926a7ade7da7e65285adda&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-02-18
fetch_date: 2025-10-04T07:23:14.492776
---

# Enigma、Vector和TgToxic：加密货币用户面临的新威胁

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogs8icFDywQkWfTIhxVChZX9vkFNVBEoEibsia1g2rXJibeqDfZtiaFBzL9WhwO0GrtnmNaH8aweiajZBVyQ/0?wx_fmt=jpeg)

# Enigma、Vector和TgToxic：加密货币用户面临的新威胁

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogs8icFDywQkWfTIhxVChZX9vEiapYEHaBfia3RRg4LByc3DuJ1tlbja96lYRWapWssMv3DnBKZUnPf8w/640?wx_fmt=png)

可疑的俄罗斯威胁分子一直以加密货币行业的东欧用户为目标，将虚假的工作机会作为诱饵，企图在受感染的主机上安装窃取信息的恶意软件。

趋势科技公司的两位研究人员Aliakbar Zahravi和Peter Girnus在本周的一份报告中表示，攻击者“使用了几种新颖的高度混淆处理的自定义加载器，以便用窃取信息的Enigma恶意软件感染加密货币行业的那些人员。”

据称Enigma是Stealerium的一个变种，而Stealerium是一种基于C#的开源恶意软件，可以充当窃取器、剪切器和键盘记录器。

整个错综复杂的感染过程始于一个通过网络钓鱼或社交媒体平台传播的恶意RAR压缩包文件。它含有两个文档，一个文档是.TXT文件，该文件含有一组与加密货币相关的示例面试问题。

第二个文档是一个微软Word文档，充当诱饵的作用，负责启动第一阶段的Enigma加载器，加载器反过来通过Telegram下载并执行一个经过模糊处理的第二阶段攻击载荷。

两位研究人员表示，为了下载下一阶段的攻击载荷，恶意软件首先向攻击者控制的Telegram频道发送请求，以便获取文件路径。这种方法让攻击者可以不断更新，摆脱了对固定文件名的依赖。

第二阶段的下载程序在获得提升权限的情况下执行，旨在禁用微软Defender，并通过部署一个合法签名的内核模式英特尔驱动程序来安装第三阶段攻击载荷，而这个驱动程序在一种名为自带易受攻击的驱动程序（BYOVD）的技术中容易受到CVE-2015-2291的攻击。

值得一提的是，美国网络安全和基础设施安全管理局（CISA）已将该漏洞添加到其已知被利用漏洞（KEV）目录中，并提到了表明该漏洞在外面被大肆利用的证据。

第三阶段的攻击载荷最终为从威胁分子控制的Telegram频道下载Enigma Stealer铺平了道路。这种恶意软件与其他窃取器一样，具有收集敏感信息、记录击键内容和获取屏幕截图的功能，所有这些信息都通过Telegram泄露给威胁分子。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib1Dv3k5anyDdWwBQfkCr1cgJP6XicmeQvM5HOD3jKwwRib5cSPgeNIpjVt023biayycq6eK3TtyE8ibA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图1. Enigma Stealer团伙使用的攻击杀伤链

虚假的工作录用是朝鲜政府撑腰的Lazarus Group在针对加密货币行业的攻击中采用的一种屡试不爽的手法。俄罗斯威胁分子采用这种作案手法“表明了这是一种具有持久性、有利可图的攻击途径。”

差不多在同一时间，Uptycs发布了一起攻击活动的细节，这起活动利用Stealerium恶意软件窃取个人数据，包括Armory、Atomic Wallet、Coinomi、Electrum、Exodus、Guarda、Jaxx Liberty和Zcash等加密货币钱包的凭据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib1Dv3k5anyDdWwBQfkCr1cTMWc4c4EJWoCfWa5AveAvdonqK85MRpkYib4uGbTjibZqAz4vlVPTxAw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图2. Stealerium感染流程

Cyble在一篇技术文章中表示，除了Enigma Stealer和Stealerium外，还有一种名为Vector Stealer的恶意软件也瞄准了加密货币钱包，它同样具有窃取.RDP文件的功能，从而使威胁分子能够实施RDP劫持活动，以实现远程访问。

多家网络安全公司记载的攻击链显示，多个恶意软件家族是通过含有恶意宏的微软Office附件传播的，这表明尽管微软试图堵住这个漏洞，但不法分子仍在依赖这种方法。

据飞塔FortiGuard实验室声称，在一起加密货币劫持和网络钓鱼活动针对西班牙用户的背景下，一种类似的方法也被用于部署门罗（Monero）加密货币挖矿软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib1Dv3k5anyDdWwBQfkCr1czc4GMic8mySLhUBb4umjPrUE2SPibgLGcQVb8T9vmflbrGouHyBDLRicQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图3. XMRig在挖掘门罗币

一系列攻击旨在窃取受害者在众多平台上的加密货币资产，而这起活动是其中最新的一起。

这包括一种“迅猛发展”的安卓银行木马，这种名为TgToxic的木马从加密货币钱包以及从银行和金融应用程序掠夺凭据和资金。这起正在肆虐的恶意软件活动自2022年7月开始，针对中国台湾、泰国和印度尼西亚的移动用户。

趋势科技表示，一旦受害者从威胁分子提供的网站下载虚假应用程序，或者如果受害者试图通过WhatsApp或Viber等消息应用程序直接向威胁分子发送消息，网络犯罪分子就会欺骗用户注册、安装恶意软件并启用它所需要的权限。

这些恶意应用程序除了滥用安卓的辅助功能服务来进行未经授权的资金转移外，还可以利用合法的自动化框架（比如Easyclick和Auto.js），以执行点击和手势操作，使其成为继PixPirate之后第二种使用这类工作流IDE的安卓恶意软件。

但利用社交工程伎俩的活动不仅限于社交媒体网络钓鱼和诈骗手段，它们还设立了以假乱真的登录页面，冒充流行的加密货币服务，目的是从被黑客攻击的钱包中转移以太坊和非同质代币（NFT）。

据Recorded Future公司声称，这是通过在网络钓鱼页面中注入加密货币窃取脚本来实现的，钓鱼页面诱使受害者将他们的钱包与条件诱人的工作录用关联起来，以生成NFT。

这种现成的网络钓鱼页面在暗网论坛上出售，这其实是所谓的网络钓鱼即服务（PhaaS）骗局的一部分，允许其他威胁分子出租这些软件包，并迅速实施大规模恶意活动。

这家公司在上周发布的一份报告中表示：“加密货币窃取脚本是一种恶意脚本，其功能类似电子盗刷器，可与网络钓鱼技术一起部署，以窃取受害者的加密货币资产。”这种骗局很有效，而且越来越受欢迎。

在加密货币窃取钓鱼页面上使用合法服务可能会加大这种钓鱼页面骗过精明用户的“骗局试金石测试”的可能性。一旦加密货币钱包受到危及，就没有任何防范措施可以防止资产非法转移到攻击者的钱包中。

这些攻击发生在这种大背景之下：犯罪团伙在2022年从加密货币企业窃取了创纪录的38亿美元，其中大部分赃款是朝鲜政府撑腰的黑客团伙所得的。

**参考及来源：**

https://thehackernews.com/2023/02/enigma-vector-and-tgtoxic-new-threats.html

原文来源：嘶吼专业版

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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