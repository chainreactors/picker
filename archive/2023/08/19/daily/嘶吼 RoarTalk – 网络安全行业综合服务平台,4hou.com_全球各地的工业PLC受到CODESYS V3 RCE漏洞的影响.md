---
title: 全球各地的工业PLC受到CODESYS V3 RCE漏洞的影响
url: https://www.4hou.com/posts/xzy3
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-19
fetch_date: 2025-10-04T11:59:25.453410
---

# 全球各地的工业PLC受到CODESYS V3 RCE漏洞的影响

全球各地的工业PLC受到CODESYS V3 RCE漏洞的影响 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 全球各地的工业PLC受到CODESYS V3 RCE漏洞的影响

布加迪
[漏洞](https://www.4hou.com/category/vulnerable)
2023-08-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)172704

收藏

导语：网络安全专家近日声称，CODESYS工业控制系统中的15个漏洞可能被用来关闭发电厂或从关键基础设施环境窃取信息。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692329071148362.png "1691791686114664.png")

全球工业环境中使用的数百万PLC（可编程逻辑控制器）面临CODESYS V3软件开发工具包（SDK）中15个漏洞的风险，这些漏洞为远程代码执行（RCE）和拒绝服务（DoS）攻击提供了可趁之机。

如今全球500余家设备制造商使用CODESYS V3 SDK，根据IEC 61131-3标准对1000多个PLC型号进行编程，以便用户开发定制的自动化序列。

该SDK被广泛使用，为工程师配置和测试用于工业系统的PLC提供了一种开发环境。大量PLC中的固件含有CODESYS提供的库程序以运行工程师们编写的程序，而可以被利用的正是这嵌入的代码，导致设备容易受到攻击。

该SDK还提供了一个Windows管理界面和一个模拟器，允许用户在部署到生产环境之前先测试其PLC配置和所编的程序。

CODESYS V3 SDK中的15个漏洞是由微软研究人员发现的，他们于2022年9月向总部位于德国的CODESYS报告了这些漏洞。这家厂商于2023年4月发布了安全更新以解决已发现的问题。

由于这些设备具有的性质，它们不常更新以修复安全问题，因此微软的安全团队昨天发布了一篇详细的文章，以提高人们对这一风险的认识，并帮助加快修补。

![p2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692329072587560.png "1691791698604790.png")

图1.在互联网上曝光的CODESYS设备（图片来源：微软）

**CODESYS漏洞**

微软仔细检查了施耐德电气和WAGO这两家厂商使用CODESYS V3的的两款PLC，结果发现了15个高危漏洞（CVSS V3：7.5 - 8.8），其中12个漏洞是缓冲区溢出漏洞。

这些漏洞分别是：CVE-2022-47378、CVE-2022-47379、CVE-2022-47380、CVE-2022-47381、CVE-2022-47382、CVE-2022-47383、CVE-2022-47384、CVE-2022-47385、CVE-2022-47386、CVE-2022-47387、CVE- 2022-47388、CVE-2022-47389、CVE-2022-47390、CVE-2022-47392和CVE-2022-47393。

主要问题出在SDK的标记解码机制上，具体来说是指标记在没有验证大小的情况下被复制到设备缓冲区中，这给攻击者提供了缓冲区溢出的机会。这些标记是数据或数据结构的载体，为PLC的正常运行提供了关键指令。

缓冲区溢出问题并不是孤立的，微软还在CODESYS V3 SDK的15个组件中发现了这个问题，包括CMPTraceMgr、CMPapp、CMPDevice、CMPapp、CMPAppBP、CMPAppForce和CMPFileTransfer。

虽然这些漏洞需要身份验证才能被利用，但微软表示，可以通过使用CVE-2019-9013来规避这个要求，而CVE-2019-9013是另一个影响CODESYS V3的漏洞，在传输过程中以明文形式暴露用户凭据，如下所示。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692329073445495.png "1691791711273466.png")

微软的分析师试了15次，结果发现有12次能够利用该漏洞在PLC上远程执行代码。

如果产品运行的是3.5.19.0之前的版本，无论硬件和操作系统配置如何，都会受到影响，**CODESYS的安全公告列出了以下受影响的产品：**

CODESYS Control RTE（SL）

CODESYS Control RTE（for Beckhoff CX）SL

CODESYS Control Win（SL）

CODESYS Control Runtime System Toolkit

CODESYS Safety SIL2 Runtime Toolkit

CODESYS Safety SIL2 PSP

CODESYS HMI（SL）

CODESYS Development System V3

CODESYS Development System V3 simulation runtime

**除上述产品外，如果运行4.8.0.0之前的版本，以下产品也会受到影响：**

CODESYS Control for BeagleBone SL

CODESYS Control for emPC-A/iMX6 SL

CODESYS Control for IOT2000 SL

CODESYS Control for Linux SL

CODESYS Control for PFC100 SL

CODESYS Control for PFC200 SL

CODESYS Control for PLCnext SL

CODESYS Control for Raspberry Pi SL

CODESYS Control for WAGO Touch Panels 600 SL

建议管理员尽快升级到CODESYS V3 v3.5.19.0，同时微软还建议断开PLC及其他关键工业设备与互联网的连接。

正如微软警告的那样：“如果威胁分子针对使用CODESYS高危版本的设备发动DoS攻击，就可以关闭发电厂，而远程代码执行可以在设备中植入后门，让攻击者得以篡改设备操作，导致PLC运行异常，或者窃取关键信息。”

本文翻译自：https://www.bleepingcomputer.com/news/security/industrial-plcs-worldwide-impacted-by-codesys-v3-rce-flaws/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?SaVYIiQD)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/VGrO)

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