---
title: WinRAR 零日漏洞被利用在解压档案时植入恶意软件
url: https://www.4hou.com/posts/vw4m
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-14
fetch_date: 2025-10-07T00:18:00.584921
---

# WinRAR 零日漏洞被利用在解压档案时植入恶意软件

WinRAR 零日漏洞被利用在解压档案时植入恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# WinRAR 零日漏洞被利用在解压档案时植入恶意软件

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-08-13 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)61755

收藏

导语：该漏洞是一个目录遍历漏洞，已在WinRAR 7.13版本中修复。借助此漏洞，经过特殊构造的压缩包可将文件提取到攻击者选定的文件路径中。

最近被修复的WinRAR漏洞（编号CVE-2025-8088）曾被作为零日漏洞在钓鱼攻击中被利用，用于安装RomCom恶意软件。

该漏洞是一个目录遍历漏洞，已在WinRAR 7.13版本中修复。借助此漏洞，经过特殊构造的压缩包可将文件提取到攻击者选定的文件路径中。

WinRAR 7.13的更新日志中写道：“在提取文件时，旧版本的WinRAR、Windows版RAR、UnRAR、便携版UnRAR源代码及UnRAR.dll可能会被诱导，使用经过特殊构造的压缩包中定义的路径，而非用户指定的路径。”

Unix版RAR、UnRAR、便携版UnRAR源代码及UnRAR库，以及安卓版RAR均不受此影响。

利用这一漏洞，攻击者可创建压缩包，将可执行文件提取到自动运行路径中，例如以下Windows启动文件夹：

%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup (用户本地路径)

%ProgramData%\Microsoft\Windows\Start Menu\Programs\StartUp (计算机全局路径)

当用户下次登录时，这些可执行文件会自动运行，使攻击者能够实现远程代码执行。

由于WinRAR不具备自动更新功能，强烈建议所有用户从win-rar.com手动下载并安装最新版本，以防范该漏洞带来的风险。

**在攻击中作为零日漏洞被利用**

该漏洞由ESET的发现。据透露，该漏洞已在钓鱼攻击中被活跃利用以安装恶意软件。安全研究人员表示：“ESET已观测到带有包含RAR文件的附件的鱼叉式钓鱼邮件。”这些压缩包利用CVE-2025-8088漏洞分发RomCom后门程序。

RomCom，也被追踪为Storm-0978、Tropical Scorpius或UNC2596，是一个俄罗斯黑客组织，涉及勒索软件、数据盗窃勒索攻击，以及专注于窃取凭证的活动。

该组织以在攻击中使用零日漏洞，以及使用定制恶意软件进行数据盗窃、维持持久控制和充当后门而闻名。据悉，RomCom此前已被证实与多个勒索软件行动有关，包括Cuba和Industrial Spy行动。

文章翻译自：https://www.bleepingcomputer.com/news/security/winrar-zero-day-flaw-exploited-by-romcom-hackers-in-phishing-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?UwR5vX1u)

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