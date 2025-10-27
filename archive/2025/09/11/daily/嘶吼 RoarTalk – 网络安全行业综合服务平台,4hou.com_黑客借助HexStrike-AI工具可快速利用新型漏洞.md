---
title: 黑客借助HexStrike-AI工具可快速利用新型漏洞
url: https://www.4hou.com/posts/PGyn
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-11
fetch_date: 2025-10-02T19:57:11.371550
---

# 黑客借助HexStrike-AI工具可快速利用新型漏洞

黑客借助HexStrike-AI工具可快速利用新型漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客借助HexStrike-AI工具可快速利用新型漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-09-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)43261

收藏

导语：HexStrike-AI本是网络安全研究员开发的合法红队工具，可集成AI代理，自主运行150多种网络安全工具，实现自动化渗透测试与漏洞发现。

研究发现，黑客正越来越多地在实际攻击中使用一款名为HexStrike-AI的新型AI驱动攻击性安全框架，利用新披露的n-day漏洞实施攻击。

这一活动由CheckPoint Research报告。该机构观察到，暗网上围绕HexStrike-AI的讨论十分活跃，且这些讨论与新披露的Citrix漏洞（包括CVE-2025-7775、CVE-2025-7776和CVE-2025-8424）的快速武器化密切相关。

根据ShadowServer基金会的数据，截至2025年9月2日，仍有近8000个端点易受CVE-2025-7775漏洞影响，较前一周的28000个有所下降。

**落入不法分子手中的工具**

HexStrike-AI本是网络安全研究员Muhammad Osama开发的合法红队工具，可集成AI代理，自主运行150多种网络安全工具，实现自动化渗透测试与漏洞发现。

其开发者描述道：“HexStrike AI通过MCP（管理控制协议）与外部大语言模型（LLM）进行‘人在环’交互，形成提示、分析、执行、反馈的持续循环。”该工具的客户端具备重试逻辑与恢复处理功能，可减轻复杂操作中单个步骤失败的影响——它会自动重试或调整配置，直至操作成功完成。

这款工具已于一个月前开源并上架GitHub平台，目前已获得1800个星标和400余次分支（fork）。遗憾的是，它也引起了黑客的注意，后者已开始将其用于攻击活动。

CheckPoint指出，在Citrix NetScaler ADC和Gateway 0-day漏洞披露后的数小时内，黑客便开始在黑客论坛上讨论如何部署HexStrike-AI来利用这些漏洞。

![discussion.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250904/1756972014164401.jpg "1756969732172192.jpg")

关于使用HexStrike-AI对抗Citrix端点的讨论

据悉，攻击者利用该工具通过CVE-2025-7775漏洞实现未授权远程代码执行，随后在被攻陷的设备上植入webshell，部分攻击者还将被入侵的NetScaler实例挂牌出售。

CheckPoint认为，攻击者很可能借助这款新型渗透测试框架实现攻击链自动化，涵盖扫描易受攻击的实例、构造漏洞利用程序、交付有效载荷（payload）以及维持持久控制等环节。

![netscalerlist.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250904/1756972015469167.jpg "1756969790111871.jpg")

易受攻击的NetScaler实例列表

尽管目前尚未证实HexStrike-AI确实参与了这些攻击，但这种自动化程度或将使n-day漏洞的利用时间从数天缩短至几分钟。这种变化将使系统管理员本就紧张的补丁部署窗口期进一步压缩，留给他们应对攻击的时间愈发有限。

漏洞披露与大规模利用之间的窗口期正急剧缩短。目前CVE-2025-7775已被用于野外攻击，而借助HexStrike-AI，未来几天的攻击量只会有增无减。”

**应对建议**

尽管快速部署补丁仍是关键，但AI驱动攻击框架带来的这种范式转变，使得构建强大、全面的安全防御体系变得更为重要。

CheckPoint建议防御者重点关注以下方面：通过威胁情报实现早期预警、部署AI驱动的防御机制，以及建立自适应检测系统。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-use-new-hexstrike-ai-tool-to-rapidly-exploit-n-day-flaws/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?P1dylWoh)

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