---
title: 新的 Specula 工具利用 Outlook 在 Windows 中执行远程代码
url: https://www.4hou.com/posts/BvLX
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-02
fetch_date: 2025-10-06T18:01:59.536558
---

# 新的 Specula 工具利用 Outlook 在 Windows 中执行远程代码

新的 Specula 工具利用 Outlook 在 Windows 中执行远程代码 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的 Specula 工具利用 Outlook 在 Windows 中执行远程代码

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-08-01 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)101158

收藏

导语：在文件共享攻击场景中，攻击者可以提供专门为利用该漏洞而设计的文档文件，然后诱使用户打开该文档文件并与文档进行交互。

Microsoft Outlook 可变成 C2 信标来远程执行代码，网络安全公司 TrustedSec 本周发布的全新红队后利用框架“Specula”就证明了这一点。

该 C2 框架通过利用 CVE-2017-11774（2017 年 10 月修补的 Outlook 安全功能绕过漏洞）使用 WebView 创建自定义 Outlook 主页。

微软表示：“在文件共享攻击场景中，攻击者可以提供专门为利用该漏洞而设计的文档文件，然后诱使用户打开该文档文件并与文档进行交互。”

然而，即使微软修补了该漏洞并删除了显示 Outlook 主页的用户界面，攻击者仍然可以使用 Windows 注册表值创建恶意主页，即使在安装了最新 Office 365 版本的系统上也是如此。

正如 Trusted 所解释的那样，Specula 纯粹在 Outlook 环境中运行，其工作原理是通过调用交互式 Python Web 服务器的注册表项设置自定义 Outlook 主页。

为此，非特权威胁者可以在 HKEY\_CURRENT\_USER\Software\Microsoft\Office\16.0\Outlook\WebView\ 下的 Outlook WebView 注册表项中将 URL 目标设置为他们控制的外部网站。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240730/1722325224133089.png "1722325140207895.png")

Outlook Specula 注册表值

攻击者控制的 Outlook 主页旨在提供自定义 VBscript 文件，攻击者可使用该文件在受感染的 Windows 系统上执行任意命令。

TrustedSec 表示：“尽管目前已有相关知识和预防措施，但 TrustedSec 仍能够利用这一特定渠道对数百个客户端进行初始访问。当通过 Microsoft 在其解决方法中列出的任何注册表项设置自定义主页时，Outlook 将在选择相关选项卡时下载并显示该 HTML 页面，而不是显示正常的邮箱元素（收件箱、日历、已发送等）。

从下载的 HTML 页面，可以在特权上下文中运行 vbscript 或 jscript，或多或少可以完全访问本地系统，就像运行 cscript / wscript.exe 一样。

虽然首先需要入侵设备才能配置 Outlook 注册表项，但一旦配置完成，攻击者就可以使用此技术实现持久性并横向传播到其他系统。

由于 outlook.exe 是一个受信任的进程，因此攻击者在执行命令时可以更轻松地逃避现有软件。

正如美国网络司令部（US CyberCom）五年前警告的那样，CVE-2017-11774 Outlook 漏洞也被用来攻击美国政府机构。

Chronicle、FireEye 和 Palo Alto Networks 的安全研究人员后来将这些攻击与伊朗支持的 APT33 网络间谍组织联系起来。

FireEye 网络安全研究人员表示，FireEye 于 2018 年 6 月首次观察到 APT34 使用 CVE-2017-11774，随后 APT33 从 2018 年 7 月开始采用该漏洞进行范围更广的攻击活动，并持续了至少一年。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-specula-tool-uses-outlook-for-remote-code-execution-in-windows/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?WO9LuFlI)

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