---
title: Encrypthub入侵618个组织以部署InfoStealer勒索软件
url: https://www.4hou.com/posts/VWrz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-03-01
fetch_date: 2025-10-06T21:56:12.725100
---

# Encrypthub入侵618个组织以部署InfoStealer勒索软件

Encrypthub入侵618个组织以部署InfoStealer勒索软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Encrypthub入侵618个组织以部署InfoStealer勒索软件

胡金鱼
[技术](https://www.4hou.com/category/technology)
2025-02-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)271615

收藏

导语：EncryptHub是一个老练的恶意分子，它会为提高攻击效率而量身定制攻击计划，对大型组织进行高价值的攻击。

一个名为“EncryptHub”的威胁者（又名“Larva-208”），一直以世界各地的组织为目标，通过鱼叉式网络钓鱼和社会工程攻击来访问企业网络。

根据Prodaft上周在内部发布的一份报告称，自2024年6月Encrypthub启动运营以来，它已经攻击了至少618个组织。

在获得访问权限后，威胁者安装远程监控和管理（RMM）软件，然后部署像Stealc和Rhadamanthys这样的信息窃取程序。在许多观察到的案例中，EncryptHub也会在受损的系统上部署勒索软件。

据悉，该威胁组织隶属于RansomHub和BlackSuit，过去曾部署过这两家勒索软件加密器，可能是它们的初始访问代理或直接附属机构。

然而，在研究人员观察到的许多攻击中，攻击者部署了自定义的PowerShell数据加密器，因此他们也保留了自己的变体。

**获得初始访问权限**

Larva-208的攻击包括短信网络钓鱼、语音网络钓鱼，以及模仿企业VPN产品（如Cisco AnyConnect、Palo Alto GlobalProtect、Fortinet和Microsoft 365）的虚假登录页面。

![fake-cisco.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250228/1740712917211198.png "1740641161147912.png")

假冒思科登录页面

攻击者通常在给目标的消息中冒充IT支持人员，声称VPN访问有问题或他们的帐户存在安全问题，指示他们登录到一个网络钓鱼网站。

受害者收到链接，这些链接将他们重定向到网络钓鱼登录页面，在那里他们的凭据和多因素身份验证（MFA）令牌（会话cookie）被实时捕获。

一旦网络钓鱼过程结束，受害者将被重定向到服务的真实域，以避免引起怀疑。

![theft-process.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250228/1740712919139601.png "1740641229208249.png")

网络钓鱼过程概述

EncryptHub已经购买了70多个模仿上述产品的域名，如“linkwebcisco.com”和“weblinkteams.com”，以增加人们对钓鱼网页的合法性认知。

这些钓鱼网站托管在像Yalishanda这样的可靠托管提供商上，ProDaft说，这些提供商通常不会对合理的删除请求做出回应。

Prodaft还发现了另一个名为larava -148的子组织，他们帮助购买用于网络钓鱼活动的域名，管理主机，并建立基础设施。

Larva-148有可能向EncryptHub出售域名和网络钓鱼工具包，尽管它们之间的确切关系尚未被破译。

**恶意软件部署**

一旦EncryptHub入侵目标系统，它就会部署各种PowerShell脚本和恶意软件来获得持久性、远程访问、窃取数据和加密文件。

首先，他们会欺骗受害者安装RMM软件，如AnyDesk、TeamViewer、ScreenConnect、Atera和Splashtop。这使得他们能够远程控制受损的系统，保持长期访问，并使横向移动成为可能。

接下来，他们使用不同的PowerShell脚本来部署信息窃取程序，如Stealc、Rhadamanthys和变幻无常的Stealer，以窃取存储在web浏览器中的数据。这些数据包括保存的凭据、会话cookie和加密货币钱包密码。

![PowerShell.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250228/1740712919160087.png "1740641351161877.png")

攻击中使用的自定义PowerShell脚本

在Linux和Mac设备上执行类似行为的Python脚本中，威胁者试图从被破坏的系统中窃取大量数据，包括：

**·**来自各种加密货币钱包的数据，包括MetaMask，以太坊钱包，Coinbase钱包，Trust钱包，Opera钱包，Brave钱包，TronLink， Trezor钱包等。

**·**各种VPN客户端的配置数据，包括Cisco VPN Client、forticclient、Palto Alto Networks GlobalProtect、OpenVPN、WireGuard等。

**·**来自流行密码管理器的数据，包括Authenticator， 1Password, NordPass, DashLane, Bitwarden, RoboForm, Keeper, MultiPassword， KeePassXC和LastPass。

**·**匹配特定扩展名或文件名包含特定关键字的文件，包括图片、RDP连接文件、Word文档、Excel电子表格、CSV文件、证书等。目标文件名中的一些关键字包括“pass”，“account”，“auth”，“2fa”，“wallet”，“seedphrase”，“recovery”，“keepass”，“secret”等等。

Larva-208的最后一个威胁是以基于powershell的自定义加密器的形式出现的勒索软件，该加密器使用AES加密文件并附加“。加密”扩展名，删除原始文件。

受害者收到一封勒索信，要求用USDT通过电报支付赎金。

![ransom-note.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250228/1740712923174020.png "1740641498206101.png")

Larva-208的勒索信

Prodaft表示，EncryptHub是一个老练的恶意分子，它会为提高攻击效率而量身定制攻击计划，对大型组织进行高价值的攻击。

本报告中研究的LARVA-208鱼叉式网络钓鱼行为表明，有针对性的网络攻击越来越复杂。通过采用高度定制的策略，先进的混淆方法和精心制作的诱饵，威胁者已经展示了逃避检测和破坏高价值目标的重要能力。

文章翻译自：https://www.bleepingcomputer.com/news/security/encrypthub-breaches-618-orgs-to-deploy-infostealers-ransomware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?iDvzsKtN)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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