---
title: 自 2018 年以来，Windows 智能应用控制和 SmartScreen 绕过技术一直存在漏洞
url: https://www.4hou.com/posts/l0x5
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-13
fetch_date: 2025-10-06T18:03:43.196009
---

# 自 2018 年以来，Windows 智能应用控制和 SmartScreen 绕过技术一直存在漏洞

自 2018 年以来，Windows 智能应用控制和 SmartScreen 绕过技术一直存在漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 自 2018 年以来，Windows 智能应用控制和 SmartScreen 绕过技术一直存在漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-08-12 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)87769

收藏

导语：Windows 智能应用控制和 SmartScreen 中存在一个设计缺陷，该缺陷使攻击者能够启动程序而不会触发安全警告。

智能应用程序控制是一种基于信誉的安全功能，它使用 Microsoft 的应用程序智能服务进行安全预测，并使用 Windows 的代码完整性功能来识别和阻止不受信任（未签名）或潜在危险的二进制文件和应用程序。

它取代了 Windows 11 中的 SmartScreen，后者是 Windows 8 中引入的一项类似功能，旨在防止潜在的恶意内容（未启用智能应用控制时，SmartScreen 将接管）。

当用户尝试打开标有 Web 标记 (MotW) 标签的文件时，这两个功能都会被激活。

Elastic Security Labs 发现，Windows 智能应用控制和 SmartScreen 中存在设计缺陷，处理 LNK 文件时存在一个漏洞（称为 LNK 踩踏），该漏洞使攻击者能够启动程序而不会触发安全警告，可以帮助威胁者绕过旨在阻止不受信任的应用程序的智能应用程序控制安全控制。该缺陷至少自 2018 年以来就一直受到利用。

LNK 破坏涉及创建具有非标准目标路径或内部结构的 LNK 文件。当用户点击此类文件时，explorer.exe 会自动修改 LNK 文件以使用正确的规范格式。

但是，这也会从下载的文件中删除 MotW（Web 标记）标签，Windows 安全功能使用该标签来触发安全检查。

![MotW security warning.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240807/1723015872196407.png "1723015872196407.png")

打开下载的文件时发出警告

为了利用此设计缺陷，可以在目标可执行文件路径后附加一个点或空格（例如，在二进制文件的扩展名“powershell.exe”之后），或者创建包含相对路径的 LNK 文件，例如“\target.exe”。

当用户单击链接时，Windows 资源管理器将查找并识别匹配的 .exe 名称，更正完整路径，通过更新磁盘上的文件删除 MotW，然后启动可执行文件。

Elastic Security Labs 认为，这一弱点多年来一直被滥用，因为它在 VirusTotal 中发现了多个旨在利用该弱点的样本，其中最早的样本是在六年多前提交的。

它还与微软安全响应中心分享了这些发现，该中心表示该问题“可能会在未来的 Windows 更新中得到修复”。

![sac-lnk-powershell-demo.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20240807/1723015955678676.gif "1723015955678676.gif")

智能应用控制 LNK 踩踏演示

Elastic 安全实验室还描述了攻击者可以利用来绕过智能应用控制和 SmartScreen 的其他弱点，包括：

**·签名恶意软件**：使用代码签名或扩展验证 (EV) 签名证书对恶意负载进行签名。

**·声誉劫持**：查找并重新利用声誉良好的应用程序来绕过系统。

**·声誉植入**：将攻击者控制的二进制文件部署到系统上（例如，具有已知漏洞的应用程序或仅在满足某些条件时触发的恶意代码）。

**·声誉篡改**：在二进制文件中注入恶意代码而不会失去相关声誉。

Elastic Security Labs 认为 Smart App Control 和 SmartScreen 存在一些基本的设计缺陷，可能导致初始访问时没有安全警告，且用户交互最少。

安全团队应在其检测堆栈中仔细审查下载，而不能仅依赖操作系统原生的安全功能来保护这一领域。目前，Elastic Security Labs 研究员已发布用于检查文件智能应用控制信任级别的开源工具。

文章翻译自：https://www.bleepingcomputer.com/news/microsoft/windows-smart-app-control-smartscreen-bypass-exploited-since-2018/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?6KI7KOjX)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

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