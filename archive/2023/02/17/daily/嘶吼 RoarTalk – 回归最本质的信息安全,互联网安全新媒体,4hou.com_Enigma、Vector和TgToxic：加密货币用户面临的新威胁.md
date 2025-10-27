---
title: Enigma、Vector和TgToxic：加密货币用户面临的新威胁
url: https://www.4hou.com/posts/JX4P
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-17
fetch_date: 2025-10-04T06:50:50.599677
---

# Enigma、Vector和TgToxic：加密货币用户面临的新威胁

Enigma、Vector和TgToxic：加密货币用户面临的新威胁 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Enigma、Vector和TgToxic：加密货币用户面临的新威胁

布加迪
[新闻](https://www.4hou.com/category/news)
2023-02-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)158676

收藏

导语：可疑的俄罗斯威胁分子一直以加密货币行业的东欧用户为目标，将虚假的工作机会作为诱饵，企图在受感染的主机上安装窃取信息的恶意软件。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230216/1676514639197958.png "1676165837113822.png")

可疑的俄罗斯威胁分子一直以加密货币行业的东欧用户为目标，将虚假的工作机会作为诱饵，企图在受感染的主机上安装窃取信息的恶意软件。

趋势科技公司的两位研究人员Aliakbar Zahravi和Peter Girnus在本周的一份报告中表示，攻击者“使用了几种新颖的高度混淆处理的自定义加载器，以便用窃取信息的Enigma恶意软件感染加密货币行业的那些人员。”

据称Enigma是Stealerium的一个变种，而Stealerium是一种基于C#的开源恶意软件，可以充当窃取器、剪切器和键盘记录器。

整个错综复杂的感染过程始于一个通过网络钓鱼或社交媒体平台传播的恶意RAR压缩包文件。它含有两个文档，一个文档是.TXT文件，该文件含有一组与加密货币相关的示例面试问题。

第二个文档是一个微软Word文档，充当诱饵的作用，负责启动第一阶段的Enigma加载器，加载器反过来通过Telegram下载并执行一个经过模糊处理的第二阶段攻击载荷。

两位研究人员表示，为了下载下一阶段的攻击载荷，恶意软件首先向攻击者控制的Telegram频道发送请求，以便获取文件路径。这种方法让攻击者可以不断更新，摆脱了对固定文件名的依赖。

第二阶段的下载程序在获得提升权限的情况下执行，旨在禁用微软Defender，并通过部署一个合法签名的内核模式英特尔驱动程序来安装第三阶段攻击载荷，而这个驱动程序在一种名为自带易受攻击的驱动程序（BYOVD）的技术中容易受到CVE-2015-2291的攻击。

值得一提的是，美国网络安全和基础设施安全管理局（CISA）已将该漏洞添加到其已知被利用漏洞（KEV）目录中，并提到了表明该漏洞在外面被大肆利用的证据。

第三阶段的攻击载荷最终为从威胁分子控制的Telegram频道下载Enigma Stealer铺平了道路。这种恶意软件与其他窃取器一样，具有收集敏感信息、记录击键内容和获取屏幕截图的功能，所有这些信息都通过Telegram泄露给威胁分子。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230216/1676514640488776.png "1676165851116650.png")

图1. Enigma Stealer团伙使用的攻击杀伤链

虚假的工作录用是朝鲜政府撑腰的Lazarus Group在针对加密货币行业的攻击中采用的一种屡试不爽的手法。俄罗斯威胁分子采用这种作案手法“表明了这是一种具有持久性、有利可图的攻击途径。”

差不多在同一时间，Uptycs发布了一起攻击活动的细节，这起活动利用Stealerium恶意软件窃取个人数据，包括Armory、Atomic Wallet、Coinomi、Electrum、Exodus、Guarda、Jaxx Liberty和Zcash等加密货币钱包的凭据。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230216/1676514641170793.png "1676165861156253.png")

图2. Stealerium感染流程

Cyble在一篇技术文章中表示，除了Enigma Stealer和Stealerium外，还有一种名为Vector Stealer的恶意软件也瞄准了加密货币钱包，它同样具有窃取.RDP文件的功能，从而使威胁分子能够实施RDP劫持活动，以实现远程访问。

多家网络安全公司记载的攻击链显示，多个恶意软件家族是通过含有恶意宏的微软Office附件传播的，这表明尽管微软试图堵住这个漏洞，但不法分子仍在依赖这种方法。

据飞塔FortiGuard实验室声称，在一起加密货币劫持和网络钓鱼活动针对西班牙用户的背景下，一种类似的方法也被用于部署门罗（Monero）加密货币挖矿软件。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230216/1676514642139965.png "1676165870316424.png")

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

本文翻译自：https://thehackernews.com/2023/02/enigma-vector-and-tgtoxic-new-threats.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?qOhttZsi)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)