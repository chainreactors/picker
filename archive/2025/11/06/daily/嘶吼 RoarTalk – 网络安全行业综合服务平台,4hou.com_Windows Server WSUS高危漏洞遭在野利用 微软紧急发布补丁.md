---
title: Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁
url: https://www.4hou.com/posts/nlpD
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-06
fetch_date: 2025-11-07T03:09:10.333506
---

# Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁

Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)7440

收藏

导语：该漏洞编号为CVE-2025-59287，属于远程代码执行漏洞，仅影响一类Windows服务器。

攻击者目前正利用Windows服务器更新服务（WSUS）的一个高危漏洞发起攻击，该漏洞的概念验证（PoC）利用代码已公开。

该漏洞编号为CVE-2025-59287，属于远程代码执行漏洞，仅影响一类Windows服务器——需启用“WSUS服务器角色”，且作为组织内部其他WSUS服务器的更新源（此功能默认未开启）。

威胁者可通过低复杂度攻击远程利用该漏洞，无需权限验证或用户交互，即可获得SYSTEM权限（系统最高权限）并执行恶意代码。在此情况下，该安全漏洞还可能在WSUS服务器之间形成蠕虫式传播。

微软目前针对所有受影响的Windows Server版本发布了非常规安全更新（非“补丁星期二”常规更新），以“全面修复CVE-2025-59287漏洞”，并建议IT管理员尽快安装，具体补丁如下：

- Windows Server 2025（补丁编号KB5070881）

- Windows Server 23H2版本（补丁编号KB5070879）

- Windows Server 2022（补丁编号KB5070884）

- Windows Server 2019（补丁编号KB5070883）

- Windows Server 2016（补丁编号KB5070882）

- Windows Server 2012 R2（补丁编号KB5070886）

- Windows Server 2012（补丁编号KB5070887）

对于无法立即部署紧急补丁的管理员，微软还提供了临时缓解方案，包括在受影响系统上禁用WSUS服务器角色，以消除攻击路径。

随后，网络安全公司HawkTrace Security发布了CVE-2025-59287的概念验证利用代码，但该代码暂不支持执行任意命令。

**在野攻击已出现：多国监测到扫描与入侵行为**

**1. 荷兰Eye Security：全球超2500台设备暴露，部分系统遭入侵**

荷兰网络安全公司Eye Security报告称，已监测到针对该漏洞的扫描与利用尝试，其至少一名客户的系统已被入侵——攻击者使用的利用工具与HawkTrace周末发布的版本不同。

该公司还指出，尽管WSUS服务器通常不会暴露在公网，但全球仍有约2500台此类设备可被公网访问，其中德国约250台、荷兰约100台。

**2. 美国Huntress：10月23日起出现针对性攻击，聚焦暴露默认端口的设备**

美国网络安全公司Huntress发现，自10月23日起，已有攻击者针对公网暴露默认端口（8530/TCP和8531/TCP）的WSUS设备发起CVE-2025-59287攻击。

该公司监测到的攻击中，威胁者执行了PowerShell侦察命令，收集内部Windows域信息并通过网络钩子发送，收集的数据包括以下命令输出：

- whoami：当前登录用户名

- net user /domain：列出Windows域内所有用户账户

- ipconfig /all：显示所有网络接口的配置信息

**3. 荷兰国家网络安全中心（NCSC-NL）：证实攻击存在，风险持续升高**

荷兰国家网络安全中心证实了上述两家公司的发现，并在预警中提醒管理员。该机构强调：“WSUS服务通常不会通过公网开放访问，但目前该漏洞的公开概念验证代码已出现，导致利用风险显著上升。”

目前，微软已将CVE-2025-59287的风险等级定为“极可能被利用”，表明该漏洞对攻击者具有较强吸引力；不过截至目前，微软尚未更新安全公告以确认该漏洞已遭在野利用。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-now-exploiting-critical-windows-server-wsus-flaw-in-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?xIW8FP6m)

#### 你可能感兴趣的

* [![]()

  Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)
* [![]()

  Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)
* [![]()

  QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具](https://www.4hou.com/posts/pn0r)
* [![]()

  近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)
* [![]()

  RondoDox僵尸网络在全球攻击行动中针对56个n-day漏洞发起攻击](https://www.4hou.com/posts/ArVB)
* [![]()

  Redis已存在13年之久的Lua漏洞可导致远程代码执行](https://www.4hou.com/posts/rp3w)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)
  2025-11-06 12:00:00
* [Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)
  2025-11-04 12:00:00
* [QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具](https://www.4hou.com/posts/pn0r)
  2025-10-30 12:00:00
* [近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)
  2025-10-28 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)

  胡金鱼
* [Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)

  胡金鱼
* [QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具](https://www.4hou.com/posts/pn0r)

  胡金鱼
* [近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)

  胡金鱼
* [RondoDox僵尸网络在全球攻击行动中针对56个n-day漏洞发起攻击](https://www.4hou.com/posts/ArVB)

  胡金鱼
* [Redis已存在13年之久的Lua漏洞可导致远程代码执行](https://www.4hou.com/posts/rp3w)

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