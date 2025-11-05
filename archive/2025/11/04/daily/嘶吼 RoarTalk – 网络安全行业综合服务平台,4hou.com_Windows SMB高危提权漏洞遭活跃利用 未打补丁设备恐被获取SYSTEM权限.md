---
title: Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限
url: https://www.4hou.com/posts/8g5l
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-04
fetch_date: 2025-11-05T03:09:25.463631
---

# Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限

Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9878

收藏

导语：威胁者目前正活跃利用Windows系统的一个SMB高危提权漏洞，在未打补丁的设备上获取SYSTEM权限。

安全研究员最新发现，威胁者目前正活跃利用Windows系统的一个SMB高危提权漏洞，在未打补丁的设备上获取SYSTEM权限（系统最高权限）。

该漏洞编号为CVE-2025-33073，影响所有版本的Windows Server、Windows 10系统，以及最高至Windows 11 24H2版本的Windows 11系统。

据悉，微软在2025年6月的“补丁星期二”中修复了该漏洞，并披露其根源是“访问控制不当”——授权攻击者可通过网络利用该缺陷实现权限提升。

微软解释漏洞利用原理如下：

1. 攻击者可诱骗受害者连接至由其控制的恶意应用服务器（如SMB服务器）；

2. 受害者连接后，恶意服务器会破坏SMB协议；

3. 攻击者还可执行特制恶意脚本，迫使受害者设备通过SMB协议回连攻击系统并完成认证，最终实现权限提升。

值得注意的是，微软当时在安全公告中提及，该漏洞信息在安全更新发布前已公开。但截至目前，微软尚未公开认可CISA关于“CVE-2025-33073遭活跃利用”的说法。随后，Microsoft 将此漏洞的发现归因于多名安全研究人员。

目前CISA尚未公布关于CVE-2025-33073活跃攻击的更多细节，但已将该漏洞纳入“已知被利用漏洞目录”。

根据约束性作指令 （BOD） 22-01 的规定，FCEB需在11月10日前完成系统加固，修复窗口期为三周。此外，CISA建议相关企业应尽快为系统打上该漏洞的修复补丁——毕竟该漏洞正被活跃利用，风险极高。

文章翻译自：https://www.bleepingcomputer.com/news/security/cisa-high-severity-windows-smb-flaw-now-exploited-in-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?212e2mbf)

#### 你可能感兴趣的

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
* [![]()

  关于防范PS1Bot恶意软件的风险提示](https://www.4hou.com/posts/xy3J)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)
  2025-11-04 12:00:00
* [QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具](https://www.4hou.com/posts/pn0r)
  2025-10-30 12:00:00
* [近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)
  2025-10-28 12:00:00
* [RondoDox僵尸网络在全球攻击行动中针对56个n-day漏洞发起攻击](https://www.4hou.com/posts/ArVB)
  2025-10-17 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

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
* [关于防范PS1Bot恶意软件的风险提示](https://www.4hou.com/posts/xy3J)

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