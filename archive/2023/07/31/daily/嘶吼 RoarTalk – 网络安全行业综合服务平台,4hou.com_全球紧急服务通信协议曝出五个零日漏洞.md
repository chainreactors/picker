---
title: 全球紧急服务通信协议曝出五个零日漏洞
url: https://www.4hou.com/posts/EXWg
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-31
fetch_date: 2025-10-04T11:51:04.873127
---

# 全球紧急服务通信协议曝出五个零日漏洞

全球紧急服务通信协议曝出五个零日漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 全球紧急服务通信协议曝出五个零日漏洞

布加迪
[漏洞](https://www.4hou.com/category/vulnerable)
2023-07-30 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)113101

收藏

导语：薄弱的加密算法使无线电通信很容易受到攻击和滥用。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230728/1690515013132866.png "1690335072943016.png")

研究人员近日发现，全球紧急服务使用的一种无线电通信协议存在几个严重漏洞，可能会让不法分子得以监视或操纵传输的信息。

地面集群无线电（TETRA）是一种无线电语音和数据标准，主要用于紧急服务（比如警察、消防和军队）以及一些工业环境。

多个TETRA安全通道提供密钥管理、语音和数据加密，而TETRA加密算法（TEA1）实施了具体的加密算法，以确保数据在空中保密通信。

Midnight Blue Labs的研究人员发现了TETRA中的五个漏洞，其中CVE-2022-24402漏洞和CVE-2022-24401漏洞都被评为是严重漏洞。这些零日漏洞统称为“TETRA:BURST”。研究人员将在下个月的美国黑帽大会上披露发现的结果。

这些漏洞允许实时或延迟解密、消息注入、用户去匿名化或会话密钥固定攻击，具体视基础设施和设备配置而定。实际上，这些漏洞允许高端对手窃听警方和军方通信内容，跟踪他们的行动，或操纵通过TETRA传输的关键基础设施网络通信内容。

在CVE-2022-24401的演示视频中，研究人员展示了攻击者可以通过攻击接收信息的无线电系统来捕获加密信息。Midnight Blue的创始合伙人Wouter Bokslag表示，在这种漏洞的任何情况下，你都不会得到密钥：“唯一得到的东西就是密钥流，你可以用密钥流来解密网络上传输的任意帧或任意消息。”

CVE-2022-24402的第二个演示视频显示，TEA1算法中存在后门，会影响依赖TEA1确保机密性和完整性的网络。研究人员还发现TEA1算法使用80位密钥，攻击者可以对其进行蛮力攻击，并在不被发现的情况下监听通信内容。

Bokslag承认，可以视之为后门。他说：“当你向TEA1输入80位的密钥时，它会经过一个密钥缩减步骤，只剩下32位的密钥材料，它会仅用这32位继续进行解密。”

Bokslag表示，这种密钥的弱化将使攻击者可以彻底搜遍32位，并使用非常便宜的硬件解密所有流量。这将只需要一个10美元的USB加密狗来接收信号，攻击者使用标准的笔记本电脑，就可以访问，除非密钥更改（而在许多情况下，密钥永远不会更改），因此攻击者可以永久访问通信内容。

研究人员承认，专有的密码技术屡屡曝出实际上可以利用的漏洞，这些漏洞在披露之前一直没有得到修复。研究人员的目的是让TETRA接受公众审查，进行风险分析，解决问题，并创造一个公平的竞争环境。

研究人员还表示，这么做的目的是为了更好地了解TETRA的安全性，确保已发现的问题得到了解决，并促进开放加密技术的使用。

Bokslag表示，这项技术令人关注的地方在于，其用例非常敏感，而本应保护通信内容安全的加密技术是保密的。”

TETRA于1995年由欧洲电信标准协会（ETSI）首次发布，是使用最广泛的专业移动无线电标准之一（特别是用于执法领域），已经连续使用了数十年，用于语音、数据和机器对机器通信。

虽然TETRA标准的大部分是开放的，但其安全性依赖一系列秘密的专有加密算法，这些算法完全遵循严格的保密协议分发给数量有限的有关方。研究人员还发现，2013年Edward Snowden泄露的文件中提到了TETRA，尤其是在拦截的TETRA通信内容中。

**修补漏洞**

Bokslag承认，通过固件更新可以很轻松地解决一些问题，包括CVE-2022-24401。然而，CVE-2022-24402无法通过固件更新来修复，因为它们是这项标准的一部分。

Bokslag表示，100多个国家的用户将受到这些漏洞的影响，大多数行业领域也将受到影响，包括执法部门、军事和情报部门。研究人员一直在与相关制造商和网络运营商进行联系，以帮助他们尽可能地解决这些问题。他表示，这是TETRA问世近30年来首次公之于众的深入安全分析。

没有人被允许知道TEA[版本]5、6和7将涉及什么。身份验证机制将再次会保密。市面上还没有任何解决方案，但制造商们正在努力采取对策。

Bokslag表示，作为对这项研究的回应，制造商们已经开发出了针对这些漏洞的补丁。Midnight Blue建议组织现在就由TEA1换成另一种TEA加密算法。

本文翻译自：https://www.darkreading.com/dr-global/zero-day-vulnerabilities-disclosed-in-global-emergency-services-communications-protocol如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?sHg1N2te)

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