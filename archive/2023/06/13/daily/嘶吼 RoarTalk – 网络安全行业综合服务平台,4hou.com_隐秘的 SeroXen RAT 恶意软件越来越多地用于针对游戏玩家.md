---
title: 隐秘的 SeroXen RAT 恶意软件越来越多地用于针对游戏玩家
url: https://www.4hou.com/posts/rq9W
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-13
fetch_date: 2025-10-04T11:44:32.057790
---

# 隐秘的 SeroXen RAT 恶意软件越来越多地用于针对游戏玩家

隐秘的 SeroXen RAT 恶意软件越来越多地用于针对游戏玩家 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 隐秘的 SeroXen RAT 恶意软件越来越多地用于针对游戏玩家

walker
[新闻](https://www.4hou.com/category/news)
2023-06-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)142998

收藏

导语：一种名为"SeroXen"的隐秘远程访问木马 (RAT) 最近开始流行，网络犯罪分子开始使用它，是因为它的检测到率低，功能强大。

一种名为"SeroXen"的隐秘远程访问木马 (RAT) 最近开始流行，网络犯罪分子开始使用它，是因为它的检测到率低，功能强大。

AT&T 报告说，该恶意软件以 Windows 11 和 10 的合法远程访问工具的名义出售，价格为每月 15 美元或一次性"终身"许可证支付 60 美元。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685696569144535.png "1685695987190493.png")

SeroXen 网站 (BleepingComputer)上列出的功能

尽管以合法程序的名义销售，但 Flare Systems 网络安全平台显示，SeroXen 在黑客论坛上被宣传为远程访问木马。不清楚在论坛上宣传它的是否是开发人员，还是可疑的分销商。

然而，远程访问程序的低成本使得它对威胁 actor 非常具有吸引力，自 2022 年 9 月以来，AT&T 已经观察到数百个样本，并且活动最近有所增加。

SeroXen 的受害者主要集中在游戏社区，但随着该工具的流行程度增加，其目标范围可能会扩展到包括大型企业和组织机构。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685696570872705.png "1685696012115152.png")

SeroXen 促销活动时间表 （AT&T）

**开源构建块**

SeroXen 基于各种开源项目，包括 Quasar RAT、r77 rootkit 和 NirCmd 命令行工具。

“SeroXen 开发人员发现了一种强大的免费资源组合，可以开发一种难以在静态和动态分析中检测到的 RAT，” AT&T 在报告中评论道。

“使用像 Quasar 这样经过精心设计的开源 RAT，自首次出现以来已有近十年的历史，为 RAT [...]使该工具更难以捉摸，更难被发现。”

SeroXen 基于 Quasar RAT，这是一款最初于 2014 年发布的轻量级远程管理系统。其最新版本 1.41 提供了反向代理、远程 shell、远程桌面、TLS 通信和文件管理系统，并通过 GitHub 免费发布。

r77(Ring 3) rootkit 是一款开源 rootkit，提供文件 less persistence、子进程钩子、恶意嵌入、内存进程注入和防杀毒软件绕过等功能。

NirCmd 是一款免费的工具，可以从命令行执行简单的 Windows 系统和外设管理任务。

**SeroXen 攻击**

AT&T 已经看到攻击通过网络钓鱼电子邮件或 Discord 渠道推动 SeroXen，网络犯罪分子在这些渠道中分发包含高度混淆的批处理文件的 ZIP 存档。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685696571607454.png "1685696070142910.png")

混淆的批处理文件 (AT&T)

批处理文件从 base64 编码的文本中提取两个二进制文件，并使用 .NET 反射将它们加载到内存中。

接触磁盘的唯一文件是 msconfig.exe 的修改版本，恶意软件执行需要它，并临时存储在短暂的“C:\Windows\System32\”（注意额外空间）目录中安装程序后将被删除。

这个批处理文件最终部署了一个名为“InstallStager.exe”的有效负载，这是 r77 rootkit 的一个变体。

Rootkit 以混淆的形式存储在 Windows 注册表中，随后通过任务计划程序使用 PowerShell 激活，并将其注入“winlogon.exe”。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685696573893727.png "1685696111638404.png")

将有效负载注入内存 (AT&T)

r77 rootkit 将 SeroXen RAT 注入系统内存，确保它不被检测到，现在提供对设备的远程访问。

一旦启动远程访问恶意软件，它就会与命令和控制服务器建立通信并等待攻击者发出的命令。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230602/1685696574111762.png "1685696137568763.png")

SeroXen的执行流程 （AT&T）

分析师发现，SeroXen 使用与 QuasarRAT 相同的 TLS 证书，并具有原始项目的大部分功能，包括 TCP 网络流支持、高效的网络序列化和 QuickLZ 压缩。

AT&T 担心 SeroXen 的日益流行会吸引黑客对大型组织感兴趣，而不是专注于游戏玩家，因此已经发布了供网络防御者使用的妥协指标。

本文翻译自：https://www.bleepingcomputer.com/news/security/stealthy-seroxen-rat-malware-increasingly-used-to-target-gamers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?3KDzguvX)

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

![](https://img.4hou.com/images/u=2076373339,2173673275&fm=26&gp=0.jpg)

# [walker](https://www.4hou.com/member/xyv9)

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

[查看更多](https://www.4hou.com/member/xyv9)

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