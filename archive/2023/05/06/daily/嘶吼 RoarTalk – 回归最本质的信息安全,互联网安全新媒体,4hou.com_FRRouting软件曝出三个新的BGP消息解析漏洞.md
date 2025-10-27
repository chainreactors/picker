---
title: FRRouting软件曝出三个新的BGP消息解析漏洞
url: https://www.4hou.com/posts/poQr
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-05-06
fetch_date: 2025-10-04T11:38:21.600458
---

# FRRouting软件曝出三个新的BGP消息解析漏洞

FRRouting软件曝出三个新的BGP消息解析漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# FRRouting软件曝出三个新的BGP消息解析漏洞

布加迪
[漏洞](https://www.4hou.com/category/vulnerable)
2023-05-05 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)196573

收藏

导语：研究人员在流行的互联网路由协议软件中发现了多个新的BGP漏洞。

Forescout Vedere Labs在其新的漏洞研究报告中讨论了边界网关协议（BGP）安全一个经常被忽视的问题：软件实现方面的漏洞。更具体地说，流行的FRRouting实现中发现了BGP消息解析漏洞，攻击者可以利用这些漏洞针对脆弱的BGP对等体（peer）发动拒绝服务（DoS）攻击。

一些实现BGP的软件套件现在被知名的网络供应商所使用，并被互联网的大部分所依赖。最近的一起BGP事件表明，可能只需要一个畸形数据包就能造成可能重大的破坏。

如今，BGP出现在ISP之外的意想不到的地方。比如说，BGP经常用于大型数据中心内部的BGP流量路由，MP-BGP等BGP扩展被广泛部署于MPLS L3 VPN。因此，组织不应该只依赖ISP来处理BGP安全问题。

我们分析了BGP的七种实现，结果在一种领先的开源实现FRRouting中发现了三个新的漏洞，攻击者可以利用这些漏洞针对易受攻击的BGP对等体发动DoS攻击，从而丢弃所有BGP会话和路由表，导致对等体没有响应。

我们的研究表明，现代BGP实现仍然容易被攻击者滥用。作为这项研究的一部分，我们发布了一个开源工具，供组织用来测试内部使用的BGP套件的安全性，并供研究人员用来发现BGP实现中的新漏洞。

**BGP是什么？为什么要继续分析它？**

BGP是互联网的主要路由协议。它允许单独的自治系统（AS）交换路由和可达性信息，而自治系统是注册机构在一段时间内租给一家组织使用的IP地址段。

当BGP失效时，AS可能变得不可达，因为其他AS无法将它们的数据包路由到这里，不可达的AS与互联网的其他部分断开。当BGP被威胁分子滥用时，网络流量可能会通过意想不到的位置被重新路由。

由于BGP最初在设计时没有考虑到安全性，因此互联网上路由的中断既有意外的，也有故意的。可能导致重大事件和互联网中断的BGP固有弱点早已为人所知。比如在2018年的一起事件中，发往谷歌IP地址的流量通过中国电信路由了一个多小时。2022年7月，俄罗斯ISP Rostelecom公告苹果网络部分系统的路由，导致苹果服务的连接可能要通过俄罗斯重新路由超过12个小时。

虽然BGP协议本身的安全性方面已有大量的研究，但是实现BGP的各个项目在安全界并没有得到同等程度的重视。各种实现很可能岌岌可危，从而使BGP对等体容易受到攻击。我们发现的关于BGP实现安全测试的最新系统性成果发表于20年前（https://www.blackhat.com/presentations/bh-usa-03/bh-us-03-convery-franz-v3.pdf）。

**BGP实现的新漏洞**

我们分析了七种流行的BGP实现，三种开源（FRRouting、BIRD和OenBGPd）和四种闭源（Mikrotik RouterOS、Juniper JunOS、Cisco IOS和Arista EOS），使用手动分析和模糊测试。

我们在2022年11月7日发布的Free Range Routing（FRRouting）最新版：版本8.4中发现了三个新的漏洞。这些漏洞在下表中已作总结，并在技术报告中予以详细说明。

|  |  |  |  |
| --- | --- | --- | --- |
| CVE   ID | 描述 | CVSSv3.1 | 潜在影响 |
| CVE-  2022-  40302 | 处理带有Extended Optional   Parameters Length（扩展可选参数长度）选项的畸形BGP OPEN消息时，出现越界读取。 | 6.5 | DoS |
| CVE-  2022-  40318 | 处理带有Extended Optional   Parameters Length选项的畸形BGP OPEN消息时，出现越界读取。这是不同于CVE-2022-40302的问题。 | 6.5 | DoS |
| CVE-  2022-  43681 | 处理突然以选项length octet结束（或者在OPEN带有扩展选项lengths的消息这一情况下，以选项length word结束）的畸形BGP OPEN消息时，出现越界读取。 | 6.5 | DoS |

这些问题已上报告给FRRouting团队，并在以下版本中得到了修复：

CVE-2022-40302和CVE-2022-40318：https://github.com/FRRouting/frr/pull/12043

CVE-2022- 43681：https://github.com/FRRouting/frr/pull/12247

**FRRouting漏洞的影响分析**

FRRouting是2016年由几家商业组织的开发人员从另一个名为Quagga的开源项目派生出来的，目前被几大供应商的网络解决方案所使用，包括nVidia Cumulus（它本身被PayPal、雅虎、高通和荷兰国家警察等大组织采用）、主要由亚马逊支持的DENT，以及主要由微软支持、在一些瞻博路由器中使用的SONiC。

攻击者可以利用这三个新漏洞中的任何一个针对脆弱的BGP对等体实施DoS攻击，从而丢弃所有BGP会话和路由表，并使对等体在几秒钟内毫无响应。通过反复发送畸形数据包，DoS情形可能被无限期延长。

其中两个问题（CVE-2022-40302和CVE-2022-43681）可能在FRRouting验证BGP Identifier和ASN字段之前触发。虽然FRRouting默认情况下只允许配置的对等体之间的连接（比如来自配置文件中不存在的主机的OPEN消息将不被接受），在这种情况下，攻击者只需要欺骗可信对等体的有效IP地址。对攻击者来说另一种可能性是，利用错误配置或通过利用其他漏洞试图危及合法对等点。FRRouting中类似的DoS漏洞已经造成了重大的中断，必须加以修复。

互联网上有超过33万个启用了BGP的主机，其中有近1000个主机回复不请自来的BGP OPEN消息。大多数BGP主机位于中国（接近10万个）、美国（5万个）和英国（1.6万个）。我们还看到超过20万个主机运行Quagga，超过1000个主机运行FRRouting（并非所有主机都启用了BGP）。中国以超过17万个主机位居榜首，其次是美国（1.5万个）和日本（近4000个）。

**BGP安全开源测试工具**

作为这项研究的一部分，我们发布了一个开源工具（https://github.com/Forescout/bgp\_boofuzzer/），供组织用来测试他们内部使用的BGP套件的安全性，并供研究人员用来发现BGP实现中的新漏洞。

该工具有几个现成的脚本，附有我们发现的漏洞的概念证明，以及针对BGP OPEN、UPDATE、ROTE REFRESH和NOTIFICATION消息的测试用例。概念证明可以直接针对设备运行，以测试设备是否容易受到攻击，而测试用例可以针对新的实现运行，以搜寻新的漏洞。

为了支持这些测试用例，该工具提供了崩溃监视仪，监测最近的测试用例是否导致目标崩溃，并从最近失败的测试用例中生成概念验证漏洞。如果目标进程终结，监视仪还会尝试重新启动目标，这对于监测长期攻击活动很方便。目前监视仪支持FRRouting、BIRD和OpenBGPD，但也可以适用于其他目标。

**结论和缓解建议**

在审查和测试所选择的实现之后，我们可以假设它们很稳健，可以防范畸形数据包。考虑到这些都是成熟的、积极开发的项目，有许多贡献者，这也就不足为奇。

然而，我们对FRRouting项目中的发现感到惊讶：有证据表明BGP消息解析问题依然存在于安全补丁工作一向出色的主要项目中。FRRouting为模糊测试自己的代码提供了广泛支持，这个事实表明，少数几个“浅层”的漏洞可能仍然会是漏网之鱼。

由于BGP是互联网不可或缺的一部分，因此有一些关于如何保护它的指导方针，比如来自互联网协会，RIPE NCC、NIST和NSA的指导方针。然而，这些指导方针往往侧重于BGP不安全方面的已知问题以及如何部署RPKI。

此外，由于我们在过去的研究中看到的供应链效应，开源组件的漏洞往往会广泛传播。比如说，新漏洞CVE-2022-40302和CVE-2022-40318清楚地表明了易受攻击的相同代码如何存在于代码库的多个位置，并充当了几个漏洞的根本原因。相似或相同的代码可能出现在其他项目中，并影响使用FRRouting的几个产品或依赖FRRouting的某一种网络操作系统，比如上文提到的Cumulus、SONiC和DENT。

为了缓解易受攻击的BGP实现（比如我们发现的FRRouting问题）的风险，最好的建议是尽可能快地修补网络基础设施设备。为此，必须首先拥有最新的资产清单，以跟踪了解组织中的所有网络设备及其上运行的软件版本。如果使用为网络中的每个设备提供细粒度可见性的软件，做到这一点就要容易得多。

本文翻译自：https://www.forescout.com/blog/three-new-bgp-message-parsing-vulnerabilities-disclosed-in-frrouting-software/转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?TdQCGuAf)

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