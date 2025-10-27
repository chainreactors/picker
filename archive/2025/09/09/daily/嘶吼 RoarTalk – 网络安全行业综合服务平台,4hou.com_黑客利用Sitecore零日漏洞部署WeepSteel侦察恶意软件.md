---
title: 黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件
url: https://www.4hou.com/posts/RXAR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-09
fetch_date: 2025-10-02T19:49:12.619401
---

# 黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件

黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-09-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)43476

收藏

导语：需要明确的是，该漏洞并非ASP.NET本身的问题，而是因复用公开文档中，本不应用于生产环境的密钥所导致的配置错误漏洞。

安全研究人员发现，攻击者近期正利用Sitecore遗留中的一个零日漏洞，部署名为WeepSteel的侦察恶意软件。

该漏洞编号为CVE-2025-53690，是一种ViewState反序列化漏洞，其成因是2017年前的Sitecore官方指南中包含了一个ASP.NET机器密钥示例。部分客户在生产环境中复用了该密钥，这使得掌握该密钥的攻击者能够构造有效的恶意“\_VIEWSTATE”有效载荷，对这些载荷进行反序列化并执行，最终导致远程代码执行（RCE）。

需要明确的是，该漏洞并非ASP.NET本身的问题，而是因复用公开文档中，本不应用于生产环境的密钥所导致的配置错误漏洞。

**漏洞利用活动详情**

Mandiant研究人员在野外发现了相关恶意活动，他们报告称，攻击者正利用该漏洞实施多阶段攻击。具体流程如下：

1.  初始入侵：攻击者瞄准“/sitecore/blocked.aspx”端点（该端点包含无需身份验证的ViewState字段），借助CVE-2025-53690漏洞，以IIS网络服务（NETWORK SERVICE）账户权限实现远程代码执行。

2.  植入侦察工具：攻击者投放的恶意有效载荷为WeepSteel——这是一款侦察型后门程序，可收集系统、进程、磁盘及网络信息，并将数据窃取行为伪装成标准的ViewState响应。

![info-col.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250905/1757059096659963.png "1757059096659963.png")

WeepSteel的信息收集

Mandiant观察到，攻击者在被攻陷环境中执行了多项侦察命令，包括whoami（查看当前用户）、hostname（查看主机名）、tasklist（查看进程列表）、ipconfig /all（查看网络配置）以及netstat -ano（查看网络连接）。

3.  部署后续工具：在攻击的下一阶段，黑客部署了Earthworm（网络隧道与反向SOCKS代理工具）、Dwagent（远程访问工具）以及7-Zip（用于将窃取的数据压缩归档）。

4.  权限提升与持久化：随后，攻击者通过创建本地管理员账户（如“asp$”“sawadmin”）、转储缓存凭证（SAM与SYSTEM注册表 hive）、借助GoTokenTheft工具尝试令牌伪造等方式提升权限；并通过禁用这些账户的密码过期功能、授予远程桌面（RDP）访问权限、将Dwagent注册为系统（SYSTEM）服务等手段，实现持久化控制。

![attack.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250905/1757059124198822.jpg "1757059124198822.jpg")

攻击生命周期

**针对CVE-2025-53690漏洞建议**

CVE-2025-53690漏洞影响Sitecore Experience Manager（XM）、Experience Platform（XP）、Experience Commerce（XC）及Managed Cloud产品，且仅当这些产品（最高版本9.0）使用2017年前文档中包含的ASP.NET机器密钥示例进行部署时才会受影响。

XM Cloud、Content Hub、CDP、Personalize、OrderCloud、Storefront、Send、Discover、Search及Commerce Server等产品不受此漏洞影响。

Sitecore已协同Mandiant的报告发布安全公告，警示使用静态机器密钥的多实例部署同样面临风险。针对可能受影响的管理员，建议采取以下措施：

1.  立即将web.config中所有静态值替换为新的唯一密钥；

2.  确保web.config中的元素已加密；

3.  作为常规安全措施，建议定期轮换静态机器密钥。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-exploited-sitecore-zero-day-flaw-to-deploy-backdoors/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?j4XJvSyJ)

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