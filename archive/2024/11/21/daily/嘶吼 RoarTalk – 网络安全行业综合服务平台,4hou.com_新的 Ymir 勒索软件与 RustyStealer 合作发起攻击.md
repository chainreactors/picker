---
title: 新的 Ymir 勒索软件与 RustyStealer 合作发起攻击
url: https://www.4hou.com/posts/LG5p
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-21
fetch_date: 2025-10-06T19:13:49.075176
---

# 新的 Ymir 勒索软件与 RustyStealer 合作发起攻击

新的 Ymir 勒索软件与 RustyStealer 合作发起攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 Ymir 勒索软件与 RustyStealer 合作发起攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-11-20 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)63899

收藏

导语：在巩固立足点并可能使用 RustyStealer 窃取数据后，Ymir 勒索软件作为最终有效负载被丢弃。

一种名为“Ymir”的新勒索软件家族在野外被发现，它对之前受到 RustyStealer infostealer 恶意软件危害的系统进行加密。

RustyStealer 是一个知名恶意软件家族，首次记录于 2021 年。据在事件响应期间发现 Ymir 的卡巴斯基研究人员称，这种新型勒索软件以其内存中执行、在代码注释中使用非洲林加拉语、使用 PDF 文件作为勒索信息及其扩展配置选项而闻名。

尽管卡巴斯基发现证据表明 Ymir 连接到可能促进数据泄露的外部服务器，但勒索软件并不具备这种功能。

目前已确认勒索软件操作于 2024 年 7 月启动，当时它便开始攻击世界各地的公司。

**Ymir 关注 RustyStealer 感染**

卡巴斯基的分析显示，Rusty 窃取者在 Ymir 部署前两天已渗透到目标基础设施内的多个系统。 RustyStealer 本质上是一种凭证收集工具，它使攻击者能够通过破坏可用于横向移动的合法高权限帐户来获得对系统的未经授权的访问。

使用 Windows 远程管理 (WinRM) 和用于远程控制的 PowerShell 等工具可以促进跨网络的横向移动。同时，攻击者还安装了Process Hacker和Advanced IP Scanner等工具。

接下来，他们执行与 SystemBC 恶意软件相关的脚本，并与攻击者的基础设施建立秘密通道，可能用于数据泄露或命令执行。

在巩固立足点并可能使用 RustyStealer 窃取数据后，Ymir 勒索软件作为最终有效负载被丢弃。

Ymir 是一种新型 Windows 勒索软件，完全从内存运行，利用“malloc”、“memove”和“memcmp”等功能来逃避检测。

启动后，它通过获取系统日期和时间、识别正在运行的进程以及检查系统正常运行时间来执行系统侦察，这可以帮助确定它是否在沙箱上运行。接下来，它根据硬编码列表跳过文件扩展名，以避免导致系统无法启动。

Ymir 使用 ChaCha20 流密码（一种先进且快速的加密算法）来加密受害者系统上的文件。加密文件会附加一个随机扩展名，例如“.6C5oy2dVr6”，并且从包含加密文件的所有目录中 Ymir 二进制文件的“.data”部分生成名为“INCIDENT\_REPORT.pdf”的勒索字条。

![ymir-ransom-note.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241112/1731382853162721.png "1731382598680482.png")

Ymir 勒索信

该勒索软件还会修改 Windows 注册表“legalnoticecaption”值，以在用户登录加密设备之前显示勒索要求。

勒索信声称受害者系统中的数据被盗，卡巴斯基推测这可能是使用 Ymir 之前部署的工具发生的。

最后，Ymir 扫描系统中是否存在 PowerShell，并利用它删除其可执行文件以逃避识别和分析。

![process.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241112/1731382854573711.png "1731382645131897.png")

Ymir 的执行过程

Ymir 尚未建立数据泄露站点，但恶意分子可能刚刚开始积累受害者数据。卡巴斯基认为，Ymir 使用信息窃取程序作为访问代理可能很快使这个新的勒索软件家族成为广泛威胁。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-ymir-ransomware-partners-with-rustystealer-in-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?627LGmLu)

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