---
title: 研究人员发现 SQL 注入可绕过机场 TSA 安全检查
url: https://www.4hou.com/posts/OGgN
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-07
fetch_date: 2025-10-06T18:20:38.202029
---

# 研究人员发现 SQL 注入可绕过机场 TSA 安全检查

研究人员发现 SQL 注入可绕过机场 TSA 安全检查 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 研究人员发现 SQL 注入可绕过机场 TSA 安全检查

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-09-06 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)102489

收藏

导语：安全研究人员发现，航空运输关键安全系统存在漏洞，未经授权的个人可以利用该漏洞绕过机场安检并进入飞机驾驶舱。

安全研究人员发现了 FlyCASS 中的漏洞，FlyCASS 是一项第三方网络服务，一些航空公司使用它来管理已知机组人员 (KCM) 计划和驾驶舱进入安全系统 (CASS)。

KCM 是一项运输安全管理局 (TSA) 计划，允许飞行员和乘务员跳过安全检查，而 CASS 允许授权飞行员在旅行时使用驾驶舱中的折叠座椅。

KCM 系统通过在线平台验证航空公司员工的证件。该过程包括扫描 KCM 条形码或输入员工编号，然后与航空公司的数据库进行交叉核对以授予访问权限，而无需进行安全检查。同样，CASS 系统在飞行员需要通勤或旅行时验证他们是否有权进入驾驶舱折叠座椅。

研究人员发现 FlyCASS 的登录系统容易受到 SQL 注入攻击，这种漏洞可让攻击者插入 SQL 语句进行恶意数据库查询。通过利用此漏洞，他们可以以参与的航空公司 Air Transport International 的管理员身份登录，并在系统内操纵员工数据。

他们添加了一个虚构的员工“Test TestOnly”，并授予该帐户访问 KCM 和 CASS 的权限，这实际上使他们能够“跳过安全检查，然后进入商用客机的驾驶舱”。

据了解，目前任何具备 SQL 注入基本知识的人都可以登录该网站，并将任何人添加到 KCM 和 CASS，这样他们既可以跳过安全检查，又可以进入商用客机的驾驶舱。

意识到问题的严重性后，研究人员立即开始了披露流程，并于 2024 年 4 月联系了相关机构。他们承认了漏洞的严重性，并确认 FlyCASS 已于 2024 年 5 月 7 日与 KCM/CASS 系统断开连接，作为预防措施。

不久之后，FyCASS 上的漏洞得到了修复。然而，在进一步协调安全披露漏洞时却遭到了抵制。

TSA 新闻办公室还向研究人员发送了一份声明，否认该漏洞的影响，声称该系统的审查过程将防止未经授权的访问。在得到研究人员的通知后，TSA 还悄悄地从其网站上删除了与其声明相矛盾的信息。

该漏洞可能会导致更广泛的安全漏洞，例如更改现有的 KCM 成员资料以绕过对新成员的任何审查程序。

研究人员的报告发布后，另一位研究人员发现，FlyCASS 似乎在 2024 年 2 月遭受了 MedusaLocker 勒索软件攻击，Joe Sandbox 分析显示了加密文件和勒索信。

今年 4 月，TSA 获悉一份报告称，第三方数据库中存在一个漏洞，其中包含航空公司机组人员信息，通过对该漏洞的测试，一个未经验证的姓名被添加到了数据库的机组人员名单中。目前，政府数据或系统没有受到损害，这些活动也没有对交通安全造成影响。

截止到发稿前，TSA 已制定程序来验证机组人员的身份，只有经过验证的机组人员才被允许进入机场的安全区域。

文章翻译自：https://www.bleepingcomputer.com/news/security/researchers-find-sql-injection-to-bypass-airport-tsa-security-checks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?JaYvPSDM)

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