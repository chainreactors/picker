---
title: 新型Mirai僵尸网络通过命令注入漏洞感染TBK DVR设备
url: https://www.4hou.com/posts/QXrL
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-14
fetch_date: 2025-10-06T22:50:40.946614
---

# 新型Mirai僵尸网络通过命令注入漏洞感染TBK DVR设备

新型Mirai僵尸网络通过命令注入漏洞感染TBK DVR设备 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型Mirai僵尸网络通过命令注入漏洞感染TBK DVR设备

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-06-13 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)54996

收藏

导语：该漏洞被CVE-2024-3721跟踪，是安全研究人员netsecfish于2024年4月披露的一个命令注入漏洞。

Mirai恶意软件僵尸网络的一个新变种正在利用TBK DVR-4104和DVR-4216数字视频录制设备中的命令注入漏洞来劫持它们。

该漏洞被CVE-2024-3721跟踪，是安全研究人员netsecfish于2024年4月披露的一个命令注入漏洞。研究人员当时发布的概念验证（PoC）以特制的POST请求的形式发送给易受攻击的端点，通过操纵某些参数（mdb和mdc）实现shell命令的执行。

卡巴斯基报告说，利用netsecfish的PoC，他们在Linux蜜罐中发现了一个新的Mirai僵尸网络变体对CVE-2024-3721的积极利用。

攻击者利用该漏洞释放ARM32恶意软件二进制文件，该二进制文件与命令和控制（C2）服务器建立通信，以将设备招募到僵尸网络群。从那里，该设备很可能被用来进行分布式拒绝服务（DDoS）攻击、代理恶意流量和其他行为。

![env-checks.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250609/1749449256389141.png "1749438297394401.png")

Mirai的环境检查

**攻击影响和修复**

尽管netsecfish去年报告称，大约有114000台暴露在互联网上的dvr易受CVE-2024-3721的攻击，但卡巴斯基的扫描显示，大约有50000台暴露设备。

netsecfish认为，与最新的Mirai变种有关的大多数感染都发生在印度、埃及、乌克兰、俄罗斯、土耳其和巴西。然而，这是基于卡巴斯基的遥测，并且由于其消费者安全产品在许多国家被禁止，这可能无法准确反映僵尸网络的目标重点。

目前，尚不清楚供应商TBK Vision是否已经发布了安全更新来解决CVE-2024-3721漏洞，或者是否仍未修补。值得注意的是，DVR-4104和DVR-4216已经在Novo， CeNova, QSee, Pulnix, XVR 5 in 1, Securus, Night OWL, DVR Login， HVR Login和MDVR品牌下进行了广泛的重新命名，因此受影响设备的补丁可用性是一个复杂的问题。

披露TBK Vision漏洞的研究人员去年还发现了其他漏洞，这些漏洞助长了对报废设备的攻击。具体来说，netsecfish在2024年披露了一个后门账户问题和一个命令注入漏洞，影响了数万台EoL D-Link设备。

在PoC披露后的几天内，在这两起案件中都发现了活跃的利用，这也表明了网络犯罪分子将公共漏洞纳入其武器库的速度之快。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-mirai-botnet-infect-tbk-dvr-devices-via-command-injection-flaw/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?YFWzuCCv)

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