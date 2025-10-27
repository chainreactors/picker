---
title: 微软：Server Manager磁盘重置会导致数据丢失
url: https://www.4hou.com/posts/xjWz
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-01
fetch_date: 2025-10-03T21:22:31.472420
---

# 微软：Server Manager磁盘重置会导致数据丢失

微软：Server Manager磁盘重置会导致数据丢失 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 微软：Server Manager磁盘重置会导致数据丢失

布加迪
[新闻](https://www.4hou.com/category/news)
2022-10-31 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)143227

收藏

导语：如果多个虚拟磁盘有同样的UniqueId，Server Manager会重置错误的磁盘。

微软近日发出警告：用户在使用Server Manager（服务器管理器）管理控制台重置虚拟磁盘时，最近确认的一个问题可能会导致数据丢失。

Server Manager帮助IT管理员从他们的桌面配置和管理基于Windows的本地和远程服务器，不需要远程桌面连接或实际访问服务器。

由于这个问题，试图重置（或清除）虚拟磁盘的管理员可能会意外重置不该重置的磁盘，从而导致数据损坏。

管理员还会在Task Progress（“任务进度”）对话窗口中看到“重置磁盘失败”错误，并显示“发现多个有相同ID的磁盘。请更新您的存储驱动程序，然后重试一下。”的错误消息。

微软在一份新的支持文档中解释道：“当您使用Community Virtual驱动程序时，可能存在多个虚拟磁盘有相同UniqueId的情况。这可能会在您执行重置操作时产生问题。”

“重置操作会重置它找到的第一个磁盘。然而，这可能不是您想要重置的那个磁盘。因此，该磁盘会丢失数据。”

这个已知问题影响以下客户端和服务器Windows平台：Windows Server 2019、Windows Server 2022和Windows 11 22H2。

![p1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221028/1666910590172416.png "1666910590172416.png")

图1. 虚拟磁盘重置失败（来源：微软）

**现有的解决方案**

微软为遇到这个已知问题的管理员们提供了一个解决方案，让他们可以在不用担心数据丢失风险的情况下重置虚拟磁盘。

为此，您可以使用以下PowerShell命令跨可用的Storage Management Providers（存储管理提供者）检索磁盘的设备ID（DeviceID），并通过删除所有分区信息和取消初始化它来清除磁盘，从而擦除磁盘上的所有数据：

1. 要检索磁盘的详细信息，输入Get-PhysicalDisk | Select-Object -Property FriendlyName, DeviceID, UniqueId。

2. 确认想要重置的那个磁盘的详细信息。使用磁盘的DeviceID作为命令中的Number：Clear-Disk [-Number]。

您可以在Get-PhysicalDisk支持文档（https://docs.microsoft.com/powershell/module/storage/get-physicaldisk?view=windowsserver2022-ps）和Clear-Disk支持文档（https://docs.microsoft.com/powershell/module/storage/clear-disk?view=windowsserver2022-ps）中找到关于如何使用这两个命令的更多信息。

周一，微软还发布了针对Windows 11 22H2的KB5018496预览累积更新，以解决另一个已知的问题，这个问题阻止易受攻击驱动程序黑名单被同步到运行较旧Windows版本的系统。

参考及来源：https://www.bleepingcomputer.com/news/microsoft/microsoft-server-manager-disk-resets-can-lead-to-data-loss/
https://support.microsoft.com/en-gb/topic/kb5018898-server-manager-resets-the-wrong-disk-if-many-virtual-disks-have-the-same-uniqueid-5b4b7d32-e65f-469e-a266-e7dc4b22467f
https://www.theregister.com/2022/10/27/microsoft\_server\_resets\_windows11/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?BzAMyMnD)

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