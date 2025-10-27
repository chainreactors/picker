---
title: Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取
url: https://www.4hou.com/posts/33NQ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-16
fetch_date: 2025-10-02T20:11:24.449875
---

# Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取

Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-09-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)43523

收藏

导语：在针对Salesloft的 data theft 攻击中，威胁者的主要目标是窃取Salesforce实例中的支持工单，进而从工单中收集凭据、身份验证令牌及其他敏感信息。

Salesloft近日表示，攻击者最早于3月入侵了其GitHub账户，进而窃取了Drift平台的OAuth令牌——这些令牌随后在8月被用于大规模Salesforce数据窃取攻击。

Salesloft是一款广泛使用的销售互动平台，帮助企业管理客户拓展与沟通事务。其旗下Drift平台则是一款对话式营销工具，可将聊天机器人与自动化功能集成至销售流程中，其中包括与Salesforce等平台的对接。

二者已成为8月末首次披露的重大供应链式攻击的核心。谷歌威胁情报团队将这些攻击归因于威胁组织UNC6395，但除了此前的Salesforce数据窃取攻击外，勒索团伙ShinyHunters以及声称是Scattered Spider的威胁者也参与了针对Salesloft Drift的攻击。

**攻击源头：GitHub账户入侵**

Salesloft于8月21日首次披露Drift应用存在安全问题，并在5天后公布了OAuth令牌被恶意利用的更多细节。这一事件已导致Salesloft客户遭遇大范围Salesforce数据窃取，受影响企业包括谷歌、Zscaler、Cloudflare、Workiva、Tenable、JFrog、Bugcrowd、Proofpoint、Palo Alto Networks等，且名单仍在持续增加。

在针对Salesloft的 data theft 攻击中，威胁者的主要目标是窃取Salesforce实例中的支持工单，进而从工单中收集凭据、身份验证令牌及其他敏感信息。

Salesloft在8月26日的更新中写道：“初步调查显示，攻击者的主要目的是窃取凭据，尤其聚焦于AWS访问密钥、密码、Snowflake相关访问令牌等敏感信息。”

协助Salesloft应对此次漏洞的Mandiant公司经调查发现，威胁者最早在2025年3月至6月期间入侵了其GitHub环境。黑客从多个GitHub仓库下载代码，添加访客用户账户，并创建恶意工作流，为后续攻击埋下伏笔。

Mandiant证实，同期攻击者还在Salesloft与Drift环境中开展了侦察活动。在入侵Drift的AWS环境后，攻击行为进一步升级——攻击者借此窃取了用于访问跨技术集成（包括Salesforce和Google Workspace）中客户数据的OAuth令牌。

**后续处置与服务恢复**

Salesloft表示，已采取轮换凭据、加强防御、验证与Drift的环境隔离等措施，Drift的基础设施也已完成隔离及凭据轮换。

在Mandiant的协助下，该公司开展了威胁溯源工作，未发现其他入侵痕迹，这意味着威胁者已不再在其环境中留存据点。

目前，Mandiant已验证此次威胁得到遏制且环境隔离到位，工作重心已转向取证质量保证审查。

Salesloft发布的最新更新宣布，在因Drift安全事件采取预防性暂停措施后，已恢复与Salesforce的集成服务。Salesforce用户现在可重新使用Salesloft的全部集成功能，该公司还为需要执行数据同步的用户提供了分步指导。

文章翻译自：https://www.bleepingcomputer.com/news/security/salesloft-march-github-repo-breach-led-to-salesforce-data-theft-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?vcZFZ2xW)

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