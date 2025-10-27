---
title: 新的 Voldemort 恶意软件滥用 Google Sheets 来存储被盗数据
url: https://www.4hou.com/posts/RXlR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-10
fetch_date: 2025-10-06T18:21:57.466957
---

# 新的 Voldemort 恶意软件滥用 Google Sheets 来存储被盗数据

新的 Voldemort 恶意软件滥用 Google Sheets 来存储被盗数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 Voldemort 恶意软件滥用 Google Sheets 来存储被盗数据

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-09-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)88403

收藏

导语：Voldemort 是一个基于 C 的后门，支持各种命令和文件管理操作，包括渗透、将新的有效载荷引入系统以及文件删除。

一项新的恶意软件活动正在向全球传播一种之前未曾记录的后门“Voldemort”，主要冒充美国、欧洲和亚洲的税务机构。根据 Proofpoint 的报告，该活动于 2024 年 8 月 5 日开始，已向 70 多个目标组织传播了 20,000 多封电子邮件，在其活动高峰期一天内就达到了 6,000 封。

超过一半的目标组织属于保险、航空航天、交通运输和教育行业。此次攻击活动的幕后威胁者尚不清楚，但 Proofpoint 认为最有可能的目的是进行网络间谍活动。

此次攻击与 Proofpoint 在本月初描述的攻击类似，但最后阶段涉及了不同的恶意软件。

**冒充税务机关**

Proofpoint 的最新报告称，攻击者正在根据公开信息制作网络钓鱼电子邮件以匹配目标组织的位置。

网络钓鱼电子邮件冒充该组织所在国家的税务机关，声称有更新的税务信息并包含相关文件的链接。

![emails.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240902/1725266417152046.png "1725266076494609.png")

攻击活动中使用的恶意电子邮件样本

点击该链接会将收件人带到托管在 InfinityFree 上的登录页面，该页面使用 Google AMP Cache URL 将受害者重定向到带有“单击查看文档”按钮的页面。

单击按钮后，页面将检查浏览器的用户代理，如果适用于 Windows，则将目标重定向到指向 TryCloudflare 隧道 URI 的 search-ms URI（Windows 搜索协议）。非 Windows 用户将被重定向到一个空的 Google Drive URL，该 URL 不提供任何恶意内容。

如果受害者与 search-ms 文件交互，Windows 资源管理器就会被触发，显示伪装成 PDF 的 LNK 或 ZIP 文件。

search-ms: URI 的使用最近在网络钓鱼活动中变得很流行，因为即使此文件托管在外部 WebDAV/SMB 共享上，它也会看起来好像位于本地的下载文件夹中，以诱骗受害者打开它。

![downloads.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240902/1725266418145860.png "1725266145659215.png")

使文件看起来好像位于受害者的计算机上

这样做会从另一个 WebDAV 共享中执行 Python 脚本，而无需将其下载到主机上，该脚本会执行系统信息收集以分析受害者。同时，会显示诱饵 PDF 以掩盖恶意活动。

![decoy-pdf.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240902/1725266420145109.png "1725266244551278.png")

转移受害者注意力的诱饵 PDF

该脚本还下载合法的 Cisco WebEx 可执行文件（CiscoCollabHost.exe）和恶意 DLL（CiscoSparkLauncher.dll），以使用 DLL 侧加载来加载 Voldemort。

**滥用 Google 表格**

Voldemort 是一个基于 C 的后门，支持各种命令和文件管理操作，包括渗透、将新的有效载荷引入系统以及文件删除。

支持的命令列表如下：

**·**Ping – 测试恶意软件与 C2 服务器之间的连接。

**·**Dir – 从受感染系统检索目录列表。

**·**Download – 从受感染系统下载文件到 C2 服务器。

**·**Upload – 从 C2 服务器上传文件到受感染系统。

**·**Exec – 在受感染系统上执行指定的命令或程序。

**·**Copy – 在受感染系统内复制文件或目录。

**·**Move – 在受感染系统内移动文件或目录。

**·**Sleep – 使恶意软件在指定的时间内进入睡眠模式，在此期间恶意软件不会执行任何活动。

**·**Exit – 终止恶意软件在受感染系统上的运行。

Voldemort 的一个显著特点是，它使用 Google Sheets 作为命令和控制服务器 (C2)，对其进行 ping 以获取在受感染设备上执行的新命令，并将其作为被盗数据的存储库。

每台受感染的机器都会将其数据写入 Google Sheet 中的特定单元，这些单元可以通过 UUID 等唯一标识符指定，从而确保隔离并更清晰地管理受感染的系统。

![request-token.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240902/1725266422446803.png "1725266381302248.png")

请求从 Google 接收访问令牌

Voldemort 使用嵌入了客户端 ID、密钥和刷新令牌的 Google API 与 Google Sheets 进行交互，这些都存储在其加密配置中。

这种方法为恶意软件提供了可靠且高度可用的 C2 通道，同时还降低了网络通信被安全工具标记的可能性。

由于 Google Sheets 在企业中广泛使用，因此阻止该服务也不切实际。

2023 年，黑客组织 APT41 曾被发现通过使用红队 GC2 工具包将 Google Sheets 用作命令和控制服务器。为了防御此活动，Proofpoint 建议将对外部文件共享服务的访问限制在受信任的服务器上，在不需要时阻止与 TryCloudflare 的连接，并监控可疑的 PowerShell 执行。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-voldemort-malware-abuses-google-sheets-to-store-stolen-data/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?uikOWmKT)

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