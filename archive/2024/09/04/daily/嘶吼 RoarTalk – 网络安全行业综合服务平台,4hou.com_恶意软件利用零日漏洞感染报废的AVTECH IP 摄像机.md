---
title: 恶意软件利用零日漏洞感染报废的AVTECH IP 摄像机
url: https://www.4hou.com/posts/VWv1
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-04
fetch_date: 2025-10-06T18:24:10.126394
---

# 恶意软件利用零日漏洞感染报废的AVTECH IP 摄像机

恶意软件利用零日漏洞感染报废的AVTECH IP 摄像机 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 恶意软件利用零日漏洞感染报废的AVTECH IP 摄像机

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2024-09-03 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)105399

收藏

导语：由于 IP 摄像头通常暴露在互联网上，因此很容易成为威胁者的目标。

基于 Corona Mirai 的恶意软件僵尸网络通过 AVTECH IP 摄像机中存在 5 年之久的远程代码执行 (RCE) 零日漏洞进行传播，目前这些摄像机已停产多年，不会收到补丁。

该漏洞由 Akamai 的 Aline Eliovich 发现，编号为 CVE-2024-7029，是摄像机“亮度”功能中的一个高严重性问题，CVSS v4 评分为8.7，允许未经身份验证的攻击者使用特制的请求通过网络注入命令。

具体来说，这个易于利用的漏洞存在于 AVTECH 摄像机固件的“action=”参数中的“亮度”参数中，该参数旨在允许远程调整摄像机的亮度，影响所有运行 Fullmg-1023-1007-1011-1009 固件版本的 AVTECH AVM1203 IP 摄像机。

由于受影响的型号已于 2019 年达到使用寿命 (EoL)，因此没有补丁可以解决 CVE-2024-7029，并且预计不会发布修复程序。

美国网络安全和基础设施安全局在本月初发布了一份公告，警告 CVE-2024-7029 及其公开漏洞的可用性，并警告这些摄像头仍在商业设施、金融服务、医疗保健和公共卫生以及交通系统中使用。

该漏洞的概念验证 (PoC) 漏洞至少自 2019 年起就已存在，但本月才分配了 CVE，并且之前尚未观察到任何主动利用。

![PoC.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240902/1725266990322926.png "1725266859251224.png")

CVE-2024-7029 的 PoC 漏洞利用

**正在进行开发**

Corona 是一个基于 Mirai 的变种，至少从 2020 年就已经存在，利用物联网设备中的各种漏洞进行传播。

Akamai 的 SIRT 团队报告称，从 2024 年 3 月 18 日开始，Corona 开始在野外利用 CVE-2024-7029 发动攻击，目标是仍在使用的 AVM1203 摄像机，尽管它们五年前就已经达到 EoL。

观察到的第一次活跃活动始于 2024 年 3 月 18 日，但分析显示，该变体早在 2023 年 12 月就已开始活动。CVE-2024-7029 的概念验证 (PoC) 至少从 2019 年 2 月起就已公开，但直到 2024 年 8 月才有适当的 CVE 分配。

Akamai 的蜜罐捕获的 Corona 攻击利用 CVE-2024-7029 下载并执行 JavaScript 文件，进而将主要僵尸网络负载加载到设备上。

一旦嵌入到设备上，恶意软件就会连接到其命令和控制 (C2) 服务器并等待执行分布式拒绝服务 (DDoS) 攻击的指令。

根据 Akamai 的分析，Corona 针对的其他缺陷包括：

**·**CVE-2017-17215：品牌路由器中存在的一个漏洞，远程攻击者可以利用 UPnP 服务中的不当验证在受影响的设备上执行任意命令。

**·**CVE-2014-8361：Realtek SDK 中的远程代码执行 (RCE) 漏洞，常见于消费级路由器。该漏洞可通过这些路由器上运行的 HTTP 服务被利用。

**·**Hadoop YARN RCE：Hadoop YARN（又一个资源协商器）资源管理系统中的漏洞，可被利用在 Hadoop 集群上执行远程代码。

建议 AVTECH AVM1203 IP 摄像机的用户立即将其下线并替换为更新的、积极支持的型号。

由于 IP 摄像头通常暴露在互联网上，因此很容易成为威胁者的目标，因此它们应始终运行最新的固件版本，以确保已知错误得到修复。如果设备停产，应将其更换为较新的型号，以继续接收安全更新。

文章翻译自：https://www.bleepingcomputer.com/news/security/malware-exploits-5-year-old-zero-day-to-infect-end-of-life-ip-cameras/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?cYSMNar3)

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