---
title: 黑客滥用流行的 Godot 游戏引擎感染数千台电脑
url: https://www.4hou.com/posts/qo6D
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-04
fetch_date: 2025-10-06T19:36:25.930409
---

# 黑客滥用流行的 Godot 游戏引擎感染数千台电脑

黑客滥用流行的 Godot 游戏引擎感染数千台电脑 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客滥用流行的 Godot 游戏引擎感染数千台电脑

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-12-03 11:32:31

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)85626

收藏

导语：这类似于用 Python 或 Ruby 编写恶意软件，恶意分子必须将 python.exe 或 ruby.exe 与其恶意程序一起发送。

黑客利用新的 GodLoader 恶意软件，广泛使用 Godot 游戏引擎功能，在短短三个月内逃避检测并感染了 17,000 多个系统。

Check Point Research 在调查攻击时发现，威胁者可以使用此恶意软件加载程序来针对所有主要平台（包括 Windows、macOS、Linux、Android 和 iOS）的游戏玩家。它还利用 Godot 的灵活性及其 GDScript 脚本语言功能来执行任意代码，并使用游戏引擎 .pck 文件（打包游戏资产）绕过检测系统来嵌入有害脚本。

一旦加载，恶意制作的文件就会触发受害者设备上的恶意代码，使攻击者能够窃取凭据或下载其他有效负载，包括 XMRig 加密矿工。

该矿工恶意软件的配置托管在 5 月份上传的私人 Pastebin 文件中，该文件在整个活动期间被访问了 206,913 次。

至少自 2024 年 6 月 29 日起，网络犯罪分子一直在利用 Godot Engine 执行精心设计的 GDScript 代码，从而触发恶意命令并传播恶意软件。VirusTotal 上的大多数防病毒工具仍未检测到这种技术，可能仅在短短的时间内就感染了超过 17,000 台计算机。

Godot 拥有一个充满活力且不断发展的开发者社区，他们重视其开源性质和强大的功能。超过 2,700 名开发者为 Godot 游戏引擎做出了贡献，而在 Discord、YouTube 和其他社交媒体平台等平台上，Godot 引擎拥有大约 80,000 名关注者，他们可以随时了解最新消息。

![Attack chain.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241202/1733125759392945.png "1733125551854259.png")

攻击链

攻击者通过 Stargazers Ghost Network 传播 GodLoader 恶意软件，这是一种恶意软件分发即服务 (DaaS)，使用看似合法的 GitHub 存储库掩盖其活动。

2024 年 9 月至 10 月期间，他们使用由超过 225 个 Stargazer Ghost 帐户控制的 200 多个存储库，将恶意软件部署到目标系统，利用潜在受害者对开源平台和看似合法的软件存储库的信任。

在整个活动过程中，Check Point 在 9 月 12 日至 10 月 3 日期间检测到针对开发人员和游戏玩家的四次独立攻击浪潮，诱使他们下载受感染的工具和游戏。

虽然安全研究人员只发现了针对 Windows 系统的 GodLoader 样本，但他们还开发了 GDScript 概念验证漏洞利用代码，展示了恶意软件如何轻松地用于攻击 Linux 和 macOS 系统。

Stargazer Goblin 是这些攻击中使用的 Stargazers Ghost Network DaaS 平台背后的恶意分子，Check Point 于 2023 年 6 月首次观察到在暗网上推广此恶意软件分发服务。但是，它可能至少从 2022 年 8 月起就一直活跃，自这项服务推出以来，收入超过 100,000 美元。

Stargazers Ghost Network 使用 3,000 多个 GitHub“ghost”帐户创建了数百个存储库的网络，这些存储库可用于传播恶意软件（主要是 RedLine、Lumma Stealer、Rhadamanthys、RisePro 和 Atlantida Stealer 等信息窃取程序）以及 star、fork 和订阅这些恶意代码库，将它们推送到 GitHub 的趋势部分并增加其明显的合法性。

随后，Godot Engine 维护者和安全团队成员发送声明说：“该漏洞并非 Godot 特有。 Godot Engine 是一个带有脚本语言的编程系统。例如，它类似于 Python 和 Ruby 运行时，用任何编程语言都可以编写恶意程序。”

Godot 不为“.pck”文件注册文件处理程序。这意味着恶意分子始终必须将 Godot 运行时与 .pck 文件一起发送。用户始终必须将运行时与 .pck 一起解压到同一位置，然后执行运行时。除非存在其他操作系统级漏洞，否则恶意分子无法创建“一键漏洞利用”。如果使用这样的操作系统级漏洞，那么由于运行时的大小，Godot 将不是一个特别有吸引力的选择。这类似于用 Python 或 Ruby 编写恶意软件，恶意分子必须将 python.exe 或 ruby.exe 与其恶意程序一起发送。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-godloader-malware-infects-thousands-of-gamers-using-godot-scripts/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?5JCBNqsf)

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