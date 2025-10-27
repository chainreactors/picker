---
title: GhostEngine 挖矿攻击利用易受攻击的驱动程序破坏 EDR 安全性
url: https://www.4hou.com/posts/JKLJ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-06-13
fetch_date: 2025-10-06T16:55:56.989691
---

# GhostEngine 挖矿攻击利用易受攻击的驱动程序破坏 EDR 安全性

GhostEngine 挖矿攻击利用易受攻击的驱动程序破坏 EDR 安全性 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# GhostEngine 挖矿攻击利用易受攻击的驱动程序破坏 EDR 安全性

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-06-12 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)189537

收藏

导语：Elastic Security Labs 和 Antiy 的研究人员在报告中特别强调了这些加密货币挖矿攻击的异常复杂性。

代号为“REF4578”的恶意加密货币挖矿活动被发现部署了一个名为 GhostEngine 的恶意负载，该负载使用易受攻击的驱动程序关闭安全产品并部署 XMRig 矿工。

Elastic Security Labs 和 Antiy 的研究人员在报告中特别强调了这些加密货币挖矿攻击的异常复杂性，并共享了检测规则以帮助防御者识别和阻止它们。然而，两份报告都没有将该活动归咎于已知的威胁分子，也没有分享有关目标/受害者的详细信息，因此该活动的起源和范围仍然未知。

**GhostEngine**

虽然尚不清楚服务器最初是如何被破坏的，但威胁分子的攻击从执行名为“Tiworker.exe”的文件开始就伪装成合法的 Windows 文件。

此可执行文件是 GhostEngine 的初始暂存有效负载，GhostEngine 是一个 PowerShell 脚本，可下载各种模块以在受感染的设备上执行不同的行为。当 Tiworker.exe 执行时，它会从攻击者的命令和控制 (C2) 服务器下载名为“get.png”的 PowerShell 脚本，该服务器充当 GhostEngine 的主要加载程序。

此 PowerShell 脚本下载其他模块及其配置、禁用 Windows Defender、启用远程服务并清除各种 Windows 事件日志。

接下来，get.png 验证系统是否至少有 10MB 的可用空间（这是进一步感染所必需的），并创建名为“OneDriveCloudSync”、“DefaultBrowserUpdate”和“OneDriveCloudBackup”的计划任务以实现持久性。

![111.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240523/1716453779595223.jpg "1716453486579963.jpg")

为持久性添加计划任务

PowerShell 脚本现在将下载并启动名为 smartsscreen.exe 的可执行文件，该可执行文件充当 GhostEngine 的主要负载。

该恶意软件负责终止和删除 EDR 软件，并下载和启动 XMRig 以挖掘加密货币。为了终止 EDR 软件，GhostEngine 加载两个易受攻击的内核驱动程序：

aswArPots.sys（Avast 驱动程序），用于终止 EDR 进程。

IObitUnlockers.sys（Iobit 驱动程序），用于删除关联的可执行文件。EDR 终止程序所针对的进程列表如下所示：

![222.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240523/1716453780533153.jpg "1716453515978172.jpg")

kill.png 和 smartscreen.exe 使用的硬编码 EDR 列表

为了实现持久性，名为“msdtc”的 Windows 服务会加载名为“oci.dll”的 DLL。启动后，此 DLL 将下载“get.png”的新副本，以在机器上安装最新版本的 GhostEngine。

虽然 Elastic 没有从他们检查的单个付款 ID 中看到令人印象深刻的数字，但每个受害者可能都有一个独特的钱包，因此总体财务收益可能非常可观。

![333.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240523/1716453781640839.jpg "1716453741535283.jpg")

完整的GhostEngine攻击链

**防御 GhostEngine**

Elastic 研究人员建议防御者留意可疑的 PowerShell 执行、异常进程活动以及指向加密矿池的网络流量。

此外，在任何环境中，部署易受攻击的驱动程序和创建相关的内核模式服务都应被视为危险信号。人们可以采取拒绝从易受攻击的驱动程序（如 aswArPots.sys 和 IobitUnlockers.sys）创建文件。

文章翻译自：https://www.bleepingcomputer.com/news/security/ghostengine-mining-attacks-kill-edr-security-using-vulnerable-drivers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?pQkKkZks)

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