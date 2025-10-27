---
title: 超过1200个SAP NetWeaver服务器容易受到主动利用漏洞的攻击
url: https://www.4hou.com/posts/QXG0
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-10
fetch_date: 2025-10-06T22:26:50.506024
---

# 超过1200个SAP NetWeaver服务器容易受到主动利用漏洞的攻击

超过1200个SAP NetWeaver服务器容易受到主动利用漏洞的攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 超过1200个SAP NetWeaver服务器容易受到主动利用漏洞的攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-05-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)63863

收藏

导语：Nextron Research表示，他们也使用随机名称，这使得发现易受攻击的Netweaver实例变得更加困难。

超过1200个暴露在互联网上的SAP NetWeaver实例容易受到一个高严重程度的未经身份验证文件上传漏洞的攻击，该漏洞允许攻击者劫持服务器。

SAP NetWeaver是一个应用服务器和开发平台，可以跨不同技术运行和连接SAP和非SAP应用程序。上周，SAP披露了一个未经身份验证的文件上传漏洞，跟踪为CVE-2025-31324，该漏洞存在于SAP NetWeaver Visual Composer中，特别是Metadata Uploader组件。

该漏洞允许远程攻击者在没有身份验证的情况下在暴露的实例上上传任意可执行文件，从而实现代码执行和整个系统的危害。

包括ReliaQuest、watchtower和Onapsis在内的多家网络安全公司证实，该漏洞在攻击中被积极利用，威胁者利用它在易受攻击的服务器上投放web shell。

SAP发言人表示，他们已经意识到了这些攻击，并在2024年4月8日发布了一个解决方案，随后在4月25日发布了一个安全更新，解决了CVE-2025-31324问题。他们没有发现任何此类攻击影响客户数据或系统的案例。

**广泛用于攻击**

研究人员现已证实，许多易受攻击的SAP Netweaver服务器暴露在互联网上，使其成为攻击的主要目标。

Shadowserver基金会发现了427个暴露的服务器，并提醒大量暴露的攻击面和潜在的严重后果。大多数易受攻击的系统位于美国，其次是印度、澳大利亚、德国、荷兰、巴西和法国等。

然而，网络防御搜索引擎Onyphe描绘了一幅更为可怕的画面，他们发现，有1284台易受攻击的服务器暴露在网上，其中474台已经被webshell入侵。

Onyphe首席技术官说道：“大约有20家《财富》500强或全球500强企业很容易受到攻击，其中许多企业都受到了损害。”

研究人员报告说，这些攻击者正在利用诸如“cache.jsp”和“helper.jsp”这样的名称的webshell。然而，Nextron Research表示，他们也使用随机名称，这使得发现易受攻击的Netweaver实例变得更加困难。

虽然服务器的数量并不多，但考虑到大型企业和跨国公司通常使用SAP NetWeaver，风险仍然很大。为了解决该风险，建议按照本公告中供应商的说明应用最新的安全更新。

如果无法应用更新，建议采用以下缓解措施：

1.限制对/developmentserver/metadata auploader端点的访问。

2.如果没有使用Visual Composer，请考虑完全关闭它。

3.将日志转发到SIEM并扫描servlet路径中未授权的文件。

文章翻译自：https://www.bleepingcomputer.com/news/security/over-1-200-sap-netweaver-servers-vulnerable-to-actively-exploited-flaw/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0yeqWo4e)

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