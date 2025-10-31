---
title: QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具
url: https://www.4hou.com/posts/pn0r
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-10-30
fetch_date: 2025-10-31T03:08:52.471084
---

# QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具

QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8364

收藏

导语：这些漏洞可能导致远程攻击者在未打补丁的NAS设备上，执行特制恶意代码。

QNAP已向用户发出警示，要求修复一处ASP.NET Core高危漏洞——该漏洞同样影响其NetBak PC Agent工具，这是一款用于向QNAP网络附加存储（NAS）设备备份数据的Windows应用。

该漏洞编号为CVE-2025-55315，属于安全绕过漏洞，存在于Kestrel ASP.NET Core Web服务器中。低权限攻击者可通过HTTP请求走私技术，劫持其他用户的凭证，或绕过前端安全控制机制。

QNAP解释称：“NetBak PC Agent在安装过程中会部署并依赖微软ASP.NET Core组件。因此，若运行该工具的Windows系统未及时更新，其搭载的ASP.NET Core版本可能受此漏洞影响。”

QNAP强烈建议用户确保Windows系统已安装最新的微软ASP.NET Core更新，以防范潜在攻击。

为保障系统安全，QNAP用户可通过以下两种方式修复漏洞：

1. 重新安装NetBak PC Agent应用程序，获取集成最新版ASP.NET Core运行时组件的版本；

2. 手动更新ASP.NET Core：访问.NET 8.0下载页面，下载并安装最新的ASP.NET Core运行时（宿主捆绑包，Hosting Bundle）。

**漏洞危害：多场景安全风险**

微软.NET安全技术人员表示，该漏洞是ASP.NET Core历史上获得“最高严重级别”评级的安全漏洞，其攻击影响取决于目标ASP.NET应用的具体场景。

成功利用该漏洞后，攻击者可实现：

- 冒充其他用户登录，达成权限提升；

- 绕过跨站请求伪造（CSRF）校验；

- 发起注入攻击。

QNAP进一步补充：“若漏洞被成功利用，已认证攻击者可向Web服务器发送特制HTTP请求，导致敏感数据遭未授权访问、服务器文件被篡改，或引发有限范围的拒绝服务（DoS）状态。”

今年1月，QNAP曾针对其数据备份与灾难恢复解决方案——HBS 3 Hybrid Backup Sync 25.1.x版本，发布安全更新修复了6处rsync漏洞。这些漏洞可能导致远程攻击者在未打补丁的NAS设备上，执行特制恶意代码。

文章翻译自：https://www.bleepingcomputer.com/news/security/qnap-warns-its-windows-backup-software-is-also-affected-by-critical-aspnet-flaw/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?uUySPEEY)

#### 你可能感兴趣的

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
* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具](https://www.4hou.com/posts/pn0r)
  2025-10-30 12:00:00
* [近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)
  2025-10-28 12:00:00
* [RondoDox僵尸网络在全球攻击行动中针对56个n-day漏洞发起攻击](https://www.4hou.com/posts/ArVB)
  2025-10-17 12:00:00
* [Redis已存在13年之久的Lua漏洞可导致远程代码执行](https://www.4hou.com/posts/rp3w)
  2025-10-11 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

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
* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

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