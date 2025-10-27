---
title: AI驱动的Cursor IDE易受Prompt-injection攻击
url: https://www.4hou.com/posts/1MlR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-09
fetch_date: 2025-10-07T00:17:46.998049
---

# AI驱动的Cursor IDE易受Prompt-injection攻击

AI驱动的Cursor IDE易受Prompt-injection攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# AI驱动的Cursor IDE易受Prompt-injection攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-08-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)48014

收藏

导语：根据研究人员的说法，黑客成功利用curexecute漏洞可能会打开勒索软件和数据盗窃事件的大门。

研究人员称之为CurXecute的漏洞存在于几乎所有版本的人工智能代码编辑器Cursor中，可以利用开发人员权限执行远程代码。安全问题现已确定为CVE-2025-54135，并可通过向AI代理提供恶意提示来触发攻击者控制命令。

Cursor集成开发环境（IDE）依靠AI代理来帮助开发人员更快、更有效地编写代码，允许他们使用模型上下文协议（MCP）与外部资源和系统连接。

根据研究人员的说法，黑客成功利用curexecute漏洞可能会打开勒索软件和数据盗窃事件的大门。

**Prompt-injection攻击**

CurXecute类似于Microsoft 365 CoPilot中的echolak漏洞，可以在没有任何用户交互的情况下窃取敏感数据。

人工智能网络安全公司Aim Security的研究人员在发现并了解了EchoLeak之后，了解到即使是本地人工智能代理也可能受到外部因素的影响，采取恶意行为。

Cursor IDE支持MCP开放标准框架，该框架通过允许代理连接到外部数据源和工具来扩展代理的功能和上下文。

Aim Security表示，MCP把一个本地代理变成了一个利器，允许它启动任意服务器——Slack、GitHub、数据库，并从自然语言调用他们的工具。研究人员提示，这可能会使代理暴露在外部的不可信数据中，从而影响其控制流。黑客可以利用这一点劫持代理的会话和权限，以用户的身份行事。

通过使用外部托管的提示注入，攻击者可以重写项目目录中的 ~/.cursor/mcp.json 文件，以启用任意命令的远程执行。

研究人员解释说，Cursor不需要确认即可执行新的条目到~/.cursor/mcp.json文件，并且对这些条目的建议编辑是实时的，即使用户拒绝它们也会触发命令的执行。

Aim Security表示，为Cursor添加标准MCP服务器（如Slack）可能会使代理暴露于不可信的数据。攻击者可以发布一个包含注入有效负载的恶意提示到公共频道mcp.json配置文件。

当受害者打开新的聊天并指示代理总结消息时，有效载荷（可能是一个shell）会在未经用户批准的情况下立即降落在磁盘上。

攻击面是任何处理外部内容的第三方MCP服务器：问题跟踪器、客户支持信箱，甚至是搜索引擎。一份被污染的文档就可以将AI代理变成本地shell。

Aim Security的研究人员表示，curexecute攻击可能导致勒索软件和数据盗窃事件，甚至可能通过幻觉操纵人工智能，从而破坏项目或实现slopsquatting攻击。

研究人员于7月私下向Cursor报告了CurXecute，随后该供应商将一个补丁合并到主分支中。7月29日，发布了Cursor 1.3版本，其中包含多项改进和对CurXecute的修复。Cursor还发布了CVE-2025-54135的安全提醒，该漏洞的中等严重性评分为8.6。安全人员建议用户下载并安装最新版本的Cursor，以规避已知的安全风险。

文章翻译自：https://www.bleepingcomputer.com/news/security/ai-powered-cursor-ide-vulnerable-to-prompt-injection-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?erJTATUq)

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