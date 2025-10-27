---
title: 冒充会议应用程序的加密窃取恶意软件瞄准 Web3 专业人士
url: https://www.4hou.com/posts/xy8E
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-27
fetch_date: 2025-10-06T19:33:16.832627
---

# 冒充会议应用程序的加密窃取恶意软件瞄准 Web3 专业人士

冒充会议应用程序的加密窃取恶意软件瞄准 Web3 专业人士 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 冒充会议应用程序的加密窃取恶意软件瞄准 Web3 专业人士

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-12-26 11:45:22

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)103996

收藏

导语：用户在未首先验证该软件是否合法，然后使用 VirusTotal 等多引擎防病毒工具进行扫描的情况下，切勿安装用户通过社交媒体推荐的软件。

网络犯罪分子利用欺诈性视频会议平台以窃取加密货币的恶意软件感染 Windows 和 Mac 电脑，通过虚假商务会议来瞄准 Web3 工作人员。

该情况根据会议软件常用的名称被称为“Meeten”，自 2024 年 9 月以来一直在进行。该恶意软件有 Windows 和 macOS 版本，目标是受害者的加密货币资产、银行信息、存储在网络上的信息浏览器和钥匙串凭据（在 Mac 上）。

Meeten 是由 Cado 安全实验室发现的，该实验室称，威胁者不断更改假冒会议软件的名称和品牌，之前曾使用过“Clusee”、“Cuesee”、“Meetone”和“Meetio”等名称。

![website.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241209/1733731240834830.png "1733730434344726.png")

网站传播 Realst 盗窃者

这些假冒品牌在其中填充了人工智能生成的内容，以增加合法性，看似得到了官方网站和社交媒体帐户的支持。访问者通过网络钓鱼或社交工程进入该网站，并被提示下载所谓的会议应用程序，但实际上，它是 Realst 窃取程序。

根据报告，该骗局以多种方式进行。在一个报告的实例中，用户认识的人在 Telegram 上联系了该用户，希望讨论商业机会并安排通话。然而，Telegram 帐户已创建更有趣的是，诈骗者向他发送了目标公司的投资演示，表明这是一个复杂的、有针对性的骗局。

其他报告称，目标用户正在接听与 Web3 工作相关的电话、下载软件并进行诈骗。他们的加密货币被盗之后。初次接触时，目标将被引导至 Meeten 网站下载产品。除了托管信息窃取程序外，Meeten 网站还包含 Javascript，甚至可以在安装任何恶意软件之前窃取存储在网络浏览器中的加密货币。

Cado 表示，除了 Realst 恶意软件之外，“Meeten”网站还托管 JavaScript，试图耗尽连接到该网站的钱包。

**针对 Mac 和 Windows**

选择下载 macOS 版本会议软件的用户会获得一个名为“CallCSSetup.pkg”的软件包，但过去也曾使用过其他文件名。执行时，它使用 macOS 命令行工具“osascript”要求用户输入系统密码，从而导致权限升级。

![prompt.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241209/1733731240206796.png "1733730511368803.png")

向用户提供密码提示

输入密码后，恶意软件将显示一条诱饵消息，指出“无法连接到服务器。请重新安装或使用 VPN。”然而，在后台，Realst 恶意软件会窃取计算机上托管的数据，包括：

**·**电报凭证

**·**银行卡详细信息

**·**钥匙串凭证

**·**来自 Google Chrome、Opera、Brave、Microsoft Edge、Arc、CocCoc 和 Vivaldi 的浏览器 cookie 和自动填充凭据

**·**Ledger 和 Trezor 钱包

数据首先存储在本地文件夹中，经过压缩，最终连同机器详细信息（例如版本名称、版本和系统信息）一起泄露到远程地址。

Realst 的 Windows 变体以 Nullsoft 脚本安装程序系统 (NSIS) 文件形式分发，名为“MeetenApp.exe”，并且还使用从 Brys Software 窃取的证书进行数字签名。

![signature.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241209/1733731241209449.png "1733730670629284.png")

有效负载的数字签名

安装程序包含一个 7zip 存档（“app-64”）和一个 Electron 应用程序的核心（“app.asar”），其中包含 JavaScript 和资源，使用 Bytenode 编译为 V8 字节码以逃避检测。

Electron 应用程序连接到位于“deliverynetwork[.]observer”的远程服务器，并下载受密码保护的存档（“AdditionalFilesForMeet.zip”），其中包含系统分析器（“MicrosoftRuntimeComponentsX86.exe”）和主要恶意软件负载（“UpdateMC.exe”） ”）。

![system-info.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241209/1733731242380613.png "1733730721585953.png")

恶意软件收集的系统信息

基于 Rust 的可执行文件尝试收集以下信息，将其添加到 ZIP 文件中，然后将其泄露：

**·**电报凭证

**·**银行卡详细信息

**·**来自 Google Chrome、Opera、Brave、Microsoft Edge、Arc、CocCoc 和 Vivaldi 的浏览器 cookie、历史记录和自动填充凭据

**·**Ledger、Trezor、Phantom 和 Binance 钱包

与 macOS 相比，Windows 版本具有更复杂、更通用的有效负载传送机制、更好的规避能力，以及通过注册表修改在重新启动之间保留的能力。

总体而言，用户在未首先验证该软件是否合法，然后使用 VirusTotal 等多引擎防病毒工具进行扫描的情况下，切勿安装他人通过社交媒体推荐的软件。

从事 Web3 工作的人员尤其容易受到攻击，因为社交工程是一种常见策略，用于与该领域的目标建立融洽关系，然后最终诱骗目标安装恶意软件以窃取加密货币。

文章翻译自：https://www.bleepingcomputer.com/news/security/crypto-stealing-malware-posing-as-a-meeting-app-targets-web3-pros/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?gYgrHIDi)

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