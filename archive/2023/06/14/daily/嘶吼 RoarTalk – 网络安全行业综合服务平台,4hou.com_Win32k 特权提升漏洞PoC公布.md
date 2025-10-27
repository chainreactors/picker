---
title: Win32k 特权提升漏洞PoC公布
url: https://www.4hou.com/posts/jgnB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-14
fetch_date: 2025-10-04T11:44:30.976842
---

# Win32k 特权提升漏洞PoC公布

Win32k 特权提升漏洞PoC公布 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Win32k 特权提升漏洞PoC公布

ang010ela
[漏洞](https://www.4hou.com/category/vulnerable)
2023-06-13 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)187824

收藏

导语：​研究人员发布了CVE-2023-29336 Win32k 特权提升漏洞的PoC代码。

研究人员发布了CVE-2023-29336 Win32k 特权提升漏洞的PoC代码。

近日，研究人员发布了CVE-2023-29336 Win32k 特权提升漏洞的PoC代码。

Win32k子系统(Win32k.sys kernel driver)负责管理操作系统的窗口管理器、屏幕输入、输出，同时作为不同类型输入硬件的接口。Avast研究人员在其中发现了一个权限提升漏洞，漏洞CVE编号为CVE-2023-29336，CVSS V3.1评分7.8分，低权限的用户利用该漏洞可以提升权限到Windows SYSTEM权限级别。

Avast 称其是在攻击活动中发现了该0 day漏洞，但未透露更多细节。5月9日，美国基础设施安全局（CISA）也发布漏洞预警，将该漏洞加入到已知的漏洞利用目录中。

微软已于2023年5月的补丁日修复了该漏洞，并称该漏洞只影响老版本的Windows系统，包括老版本的Windows 10系统、Windows server、Windows8等，Windows 11系统并不受到该漏洞的影响。

就在漏洞补丁发布后的一个月，web3安全公司Nume发布了CVE-2023-29336漏洞的技术细节，并发布了在Windows server 2016版本上的PoC漏洞利用代码。

PoC代码参见：https://github.com/numencyber/Vulnerability\_PoC/blob/main/CVE-2023-29336/poc.cpp

PoC视频参见：https://www.youtube.com/embed/fDgq8FyXVvU

Nume研究人员分析了Windows server 2016上的漏洞情况，发现Win32k只锁定了window对象，但没有锁定嵌套的菜单对象。因此，攻击者如果修改了系统内存中的特定地址，就可以实现菜单对象的修改或劫持。

控制菜单对象就表明获得了其启动的程序对应的权限，虽然第一步并不能获得管理员级权限，但通过其他步骤可以实现更高权限的提升。

研究人员在不同的内存布局操作方法、漏洞利用、内存读写函数上进行了测试，最终实现了可以稳定提升到system权限的PoC。

Numen建议系统管理员关注与window对象相关的异常偏移的内存读写，因为这些异常行为可能表明漏洞正在被利用。研究人员建议用户尽快安装微软2023年5月发布的补丁。

更多技术细节参见Numen的技术分析报告：https://www.numencyber.com/cve-2023-29336-win32k-analysis/

本文翻译自：https://www.bleepingcomputer.com/news/security/poc-released-for-windows-win32k-bug-exploited-in-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?qc55DLC9)

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

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

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

[查看更多](https://www.4hou.com/member/e7OO)

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