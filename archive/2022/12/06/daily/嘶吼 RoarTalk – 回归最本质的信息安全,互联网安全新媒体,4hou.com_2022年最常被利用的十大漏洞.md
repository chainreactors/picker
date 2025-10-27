---
title: 2022年最常被利用的十大漏洞
url: https://www.4hou.com/posts/WBNo
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-06
fetch_date: 2025-10-04T00:33:24.257956
---

# 2022年最常被利用的十大漏洞

2022年最常被利用的十大漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 2022年最常被利用的十大漏洞

布加迪
[漏洞](https://www.4hou.com/category/vulnerable)
2022-12-05 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)372994

收藏

导语：本文着重介绍了2022年恶意威胁分子利用的一些最危险的漏洞。

黑客攻击变得一年比一年高级和复杂，因此现在追踪了解安全漏洞比以往任何时候都来得重要。本文着重介绍了2022年恶意威胁分子利用的一些最危险的漏洞。

**1. Follina（CVE- 2022 – 30190）**

CVE-2022-30190（非正式名称为“Follina”）在2022年5月被披露，它是微软Windows支持诊断工具（MSDT）中的一个远程代码执行漏洞，允许远程攻击者在目标系统上执行任意shell命令。

自从该漏洞被公开披露以来，安全研究人员观察到多起涉及利用该漏洞的案例，包括与俄罗斯政府有关的威胁分子（Sandworm、UAC-0098和APT28）针对乌克兰的组织和政府机构发起的多次网络钓鱼攻击，旨在用窃取信息的恶意软件感染受害者，以及针对欧美政府的网络间谍活动。Follina漏洞还被用来植入远程访问工具，比如Qbot和AsyncRAT，并在Windows系统上部署后门。

**2. Log4Shell（CVE- 2021 – 44228）**

尽管Log4Shell漏洞在2021年底才被披露，但它在最常被利用的漏洞排行榜中依然名列前茅，仍然是网络犯罪分子在地下论坛上最常讨论的漏洞之一。

CVE-2021-44228是一款广受欢迎的Apache Log4j开源日志实用程序中的远程代码执行漏洞。如果威胁分子利用了该漏洞，就可以向受影响的系统发送一个特别精心设计的命令，执行恶意代码，并操控受害者的机器。自2021年12月以来，现已修复的Log4Shell漏洞一直被多个威胁分子大肆利用，从加密货币挖矿软件、DDoS僵尸网络、勒索软件团伙和初始访问代理，到与伊朗、朝鲜和土耳其政府有关联的政府撑腰的黑客，不一而足。

最近，有人观察到威胁分子使用Log4Shell在未打补丁的、面向公众的VMware Horizon和Unified Access Gateway（统一接入网关）服务器上部署恶意软件。

**3. Spring4Shell（CVE- 2022 – 22965）**

CVE-2022-22965（Spring4Shell或SpringShell）是来自VMware的一种广泛使用的开源Java框架Spring Framework中的远程代码执行漏洞，以上面提到的Log4Shell漏洞命名。一旦攻击者实现了远程代码执行，就可以安装恶意软件，或者利用受影响的服务器作为初始立足点，以提升权限，进而攻击整个系统。

虽然Spring4Shell不像Log4Shell那么普遍，也不容易被利用，但众多组织不应该轻视该漏洞，因为它已经变成了网络犯罪分子手里的武器，用于部署加密货币挖矿软件，并且用在了使用臭名昭著的Mirai恶意软件的僵尸网络。

**4. F5 BIG-IP（CVE-2022-1388）**

CVE-2022-1388于2022年5月首次被披露，是另一个值得关注的严重漏洞。该漏洞影响F5 BIG-IP软硬件套件中的BIG-IP iControl REST身份验证组件；一旦被利用，允许未经身份验证的攻击者以“root”权限在BIG-IP网络设备上执行命令。在过去的几个月里，研究人员发现了旨在擦除设备内容或投放web shell恶意脚本的多起攻击企图利用该漏洞。

**5. 谷歌Chrome零日漏洞（CVE-2022-0609）**

现已得到修补的CVE-2022-0609是谷歌Chrome的动画组件中的远程代码执行漏洞，两起独立的与朝鲜有关的黑客活动（名为“Operation Dream Job”和“Operation AppleJeus”）利用了该漏洞，这两起黑客活动攻击美国的媒体、IT、加密货币和金融技术等行业的多家组织。

**6. 微软Office漏洞（CVE-2017-11882）**

古老的微软Office远程代码执行漏洞（CVE-2017-11882）于2017年首次被披露，至今仍是黑客论坛上最热议的漏洞之一。虽然微软在近五年前就发布了CVE-2017-11882的官方补丁，但许多组织依然没有打上补丁，这给企图趁虚而入的网络犯罪分子提供了可趁之机。在最近的一个案例中，威胁分子利用这个未打补丁的漏洞来部署SmokeLoader恶意软件，以便投放其他恶意软件，比如TrickBot。

**7. ProxyNotShell（CVE-2022-41082和CVE-2022-41040）**

ProxyNotShell指两个分别被编号为CVE-2022-41082和CVE-2022-41040的高危漏洞，允许访问PowerShell Remoting的远程用户在易受攻击的Exchange系统上执行任意代码或执行SSRF攻击。这两个漏洞于2022年9月首次被披露，据称被黑客利用了数月。微软证实，黑客们利用ProxyNotShell漏洞，在被攻击的Exchange服务器上部署了China Chopper web shell恶意脚本。这两个漏洞在微软发布的11月周二补丁包中都已得到了解决。

**8. Zimbra协作套件漏洞（CVE-2022-27925和CVE-2022-41352）**

今年早些时候，安全研究人员向公众披露了影响一种广泛使用的电子邮件和协议平台：Zimbra协作套件（ZCS）的两个漏洞（CVE-2022-27925和CVE-2022-41352）。CVE-2022-27925允许实现远程代码执行，而CVE-2022-41352可以被用来将任意文件上传到易受攻击的实例。在2022年7月至10月期间，研究人员发现了多起攻击，包括政府撑腰的黑客利用这些漏洞入侵了全球成千上万台ZCS服务器。

**9. Atlassian Confluence RCE漏洞（CVE-2022-26134）**

运行Atlassian Confluence软件的服务器对网络犯罪分子来说之所以是诱人的目标，是由于如果不打补丁，它们可能提供对企业网络的初始访问，因此保护它们显得至关重要。6月份，包括Kinsing、Hezb和Dark在内的几个僵尸网络使用Atlassian Confluence的远程执行漏洞（CVE-2022-26134），在未打补丁的安装系统上部署挖掘加密货币的恶意软件。

**10. Zyxel RCE漏洞（CVE-2022-30525）**

另一个值得注意的严重漏洞就是CVE-2022-30525，这个操作系统命令注入漏洞影响众多企业的Zyxel防火墙和VPN设备。一旦成功利用该漏洞，攻击者可以在不需要验证身份的情况下远程注入任意命令。考虑到这个安全问题的严重性以及可能带来的破坏，美国国家安全局（NSA）网络安全主任Rob Joyce发推文警告用户有人企图利用该漏洞，敦促用户更新易受攻击的Zyxel软件。

本文翻译自：https://www.immuniweb.com/blog/top-10-exploited-vulnerabilities-in-2022.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?5LwXgLuB)

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