---
title: 《我的世界》玩家遭Stargazers恶意软件攻击 黑客利用建模生态与GitHub窃取凭证
url: https://www.4hou.com/posts/GAk8
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-26
fetch_date: 2025-10-06T22:52:06.243186
---

# 《我的世界》玩家遭Stargazers恶意软件攻击 黑客利用建模生态与GitHub窃取凭证

《我的世界》玩家遭Stargazers恶意软件攻击 黑客利用建模生态与GitHub窃取凭证 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 《我的世界》玩家遭Stargazers恶意软件攻击 黑客利用建模生态与GitHub窃取凭证

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-06-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)102688

收藏

导语：为了确保安全，微软玩家应该只从信誉良好的平台和经过验证的社区门户网站下载mod，并坚持信赖的发行商。

一场大规模的恶意软件活动专门针对《我的世界》玩家，他们使用恶意模型和欺骗手段感染Windows设备，通过信息窃取器窃取凭证、身份验证令牌和加密货币钱包。

该活动由Check Point Research发现，由Stargazers Ghost Network进行，并利用《我的世界》大规模建模生态系统和GitHub等合法服务来吸引大量潜在目标受众。

Check Point在Pastebin链接上看到了成千上万的浏览量或点击量，这些浏览量被威胁者用来向目标设备发送有效载荷，此次活动的影响范围广泛。

**隐秘的Minecraft恶意软件**

Stargazers幽灵网络是一种自去年以来活跃在GitHub上的分发即服务（DaaS）操作，首次被Check Point记录在涉及3000个传播虚假信息的账户的活动中。

同样的操作，由虚假的GitHub星标推动，被观察到在2024年底感染了超过17000个系统，使用了一种新型的基于Godot的恶意软件。

由Check Point研究人员Jaromír Hořejší和Antonis Terefos描述的最新活动用Java恶意软件攻击《我的世界》，该恶意软件可以逃避所有反病毒引擎的检测。

研究人员发现了多个由Stargazers运行的GitHub存储库，伪装成《我的世界》（Minecraft）模型和Skyblock Extras、Polar Client、FunnyMap、Oringo和Taunahi等作弊工具。

Antonis Terefos表示目前已经确定了大约500个GitHub存储库，包括那些分叉或复制的，它们是针对《我的世界》玩家的行动的一部分。另外，还看到了大约70个账户产生的700颗星星。

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250619/1750318345204811.png "1750318054170276.png")

参与此操作的四个存储库

一旦在Minecraft中执行，第一阶段的JAR加载器使用base64编码的URL从Pastebin下载下一阶段，获取基于java的窃取器。

这个窃取者的目标是Minecraft账户令牌和来自Minecraft启动器和流行的第三方启动器（如Feather， Lunar和Essential）的用户数据。

它还试图窃取Discord和Telegram帐户令牌，通过HTTP POST请求将窃取的数据发送到攻击者的服务器。

Java窃取程序还可以作为下一阶段的加载程序，这是一个基于。net的窃取程序，名为“44 CALIBER”，这是一个更“传统”的信息窃取程序，试图窃取存储在网络浏览器、VPN帐户数据、加密货币钱包、Steam、Discord和其他应用程序中的信息。

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250619/1750318346950136.png "1750318133105645.png")

感染链概述

44 CALIBER还收集系统信息和剪贴板数据，并可以抓取受害者电脑的屏幕截图。

研究人员说：“在去混淆之后，我们可以观察到它从浏览器（Chromium, Edge, Firefox），文件（Desktop, Documents, %USERPROFILE%/Source），加密货币钱包（Armory, AtomicWallet, bitcoore, Bytecoin, DashCore, Electrum, Ethereum, LitecoinCore, Monero, Exodus, Zcash, Jaxx）， vpn (ProtonVPN, OpenVPN, NordVPN), Steam, Discord, FileZilla， Telegram中窃取各种凭证。”

被盗数据是通过Discord的网络钩子泄露出来的，并附有俄罗斯的评论。这个线索，结合UTC+3提交时间戳，表明这个活动的操作者是俄罗斯人。

Check Point在其报告的底部分享了完整的入侵指标（ioc），以帮助检测和阻止威胁。

为了确保安全，微软玩家应该只从信誉良好的平台和经过验证的社区门户网站下载mod。如果提示从GitHub下载，请检查启动、分叉和贡献者的数量，仔细检查提交是否有虚假活动的迹象，并检查存储库上最近的操作。最后，谨慎的做法是在测试mod时使用单独的“burner”Minecraft账户，避免登录到其主账户。

文章翻译自：https://www.bleepingcomputer.com/news/security/stargazers-use-fake-minecraft-mods-to-steal-player-passwords/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?PTM6jlRJ)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

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