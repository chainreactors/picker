---
title: Clop勒索软件团伙声称：使用GoAnywhere零日漏洞闯入了130家组织
url: https://www.4hou.com/posts/LBjA
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-16
fetch_date: 2025-10-04T06:44:40.182347
---

# Clop勒索软件团伙声称：使用GoAnywhere零日漏洞闯入了130家组织

Clop勒索软件团伙声称：使用GoAnywhere零日漏洞闯入了130家组织 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Clop勒索软件团伙声称：使用GoAnywhere零日漏洞闯入了130家组织

布加迪
[漏洞](https://www.4hou.com/category/vulnerable)
2023-02-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)197685

收藏

导语：Clop勒索软件团伙近日声称自己策划了最近利用GoAnywhere MFT安全文件传输工具的一个零日漏洞的攻击，表示已从130多家组织窃取了数据。

![0.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230215/1676425057146694.png "1676243689873490.png")

Clop勒索软件团伙近日声称自己策划了最近利用GoAnywhere MFT安全文件传输工具的一个零日漏洞的攻击，表示已从130多家组织窃取了数据。

该安全漏洞现在被编号为CVE-2023-0669，使攻击者能够在未打补丁的GoAnywhere MFT实例上获得远程执行代码的权限，管理控制台暴露在互联网上，谁都可以访问。

Clop团伙联系上安全外媒BleepingComputer，表示他们在闯入易受该漏洞攻击的服务器后，在十天内就窃取到了数据。

他们还声称，可以通过受害者的网络横向移动，并部署勒索软件攻击载荷来加密系统，但他们决定不这么做，只是窃取了存储在受攻击的GoAnywhere MFT服务器上的文件。

当BleepingComputer询问攻击何时开始、是否已经开始勒索受害者以及索要的赎金金额等问题时，该团伙拒绝提供证据，也拒绝透露相关方面的更多细节。

BleepingComputer无法独立证实Clop的说法，GoAnywhere MFT的开发商Fortra（前身为HelpSystems）也没有回复有关CVE-2023-0669被利用的详情和勒索软件团伙说法是否属实的电子邮件。

然而，Huntress威胁情报经理Joe Slowik在调查部署了TrueBot恶意软件下载器的一起攻击时，认为GoAnywhere MFT攻击与TA505有关联，这个威胁团伙在过去以部署Clop勒索软件而出名。

Slowik表示：“虽然这种关联并未得到权威部门的证实，但分析Truebot活动和部署机制后发现，与一个名为TA505的团伙有关。来家多家公司的报告表明Silence/Truebot活动与TA505团伙有关。”

“从观察到的行为和之前的报告来看，我们可以比较有把握地得出结论，即Huntress观察到的活动旨在部署勒索软件，可能会有另外伺机利用GoAnywhere MFT的活动出现，以达到同样的目的。”

**安全文件传输工具中被肆意利用的漏洞**

Fortra上周向客户披露，这个名为zero-day的漏洞正在被大肆利用。

周一，概念验证（PoC）漏洞利用代码也在网上发布了，允许未经身份验证即可在易受攻击的服务器上远程执行代码。

该公司次日发布了紧急安全更新，以便客户保护服务器远离攻击活动。

自那以后，Fortra周四在其支持网站上发布了另一个更新（只有使用用户帐户登录后才能访问），声称一些MFTaaS实例也在攻击中遭殃了。

Fortra表示：“我们已经查明，未经授权的攻击者通过一个以前未知的漏洞访问了系统，并创建了未经授权的用户帐户。”

“为了解决这个问题，并且出于谨慎的考虑，我们已暂时中断了服务。随着在每个环境采取并验证缓解措施，客户的服务继续逐一恢复。我们正与客户直接合作，评估他们各自的潜在影响，采取缓解措施，并恢复系统。”

周五CISA也将CVE-2023-0669 GoAnywhere MFT漏洞添加到了其 已知被利用漏洞目录中，命令联邦机构在未来三周内（直至3月3日）给系统打上补丁。

虽然Shodan显示网上暴露的GoAnywhere实例超过1000个，但只有135个启用端口8000和8001（易受攻击的管理控制台使用这两个端口）。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230215/1676425058102036.jpeg "1676243707146610.jpeg")

图1. 暴露在互联网上的GoAnywhere MFT设备（图片来源：Shodan）

**Clop发动的Accellion勒索攻击**

Clop据称使用GoAnywhere MFT零日漏洞来窃取数据，这一招与他们在2020年12月使用的那一招非常相似，当时他们发现并利用了Accellion FTA零日漏洞，最后窃取了大约100家公司的数据。

当时这些公司收到了电子邮件，要求它们支付1000万美元赎金，以免数据被公开泄露。

在2020年的Accellion攻击中，Clop的运营团伙使用Accellion的老式文件传输设备（FTA）从多家知名公司窃取了大量数据。

服务器被Clop攻击的组织包括：能源巨头壳牌、超市巨头克罗格、网络安全公司Qualys，以及全球多所知名大学，比如斯坦福医学院、科罗拉多大学、迈阿密大学、马里兰大学巴尔的摩分校（UMB）和加州大学。

2021年6月，国际执法部门展开了一场代号为“旋风行动”的抓捕行动，为Clop勒索软件团伙提供服务的六名洗钱犯在乌克兰被捕，Clop的一些基础设施被关掉。

至少自2019年以来，该团伙还与全球多起勒索软件攻击有关。服务器被Clop加密的一些受害者包括马斯特里赫特大学、Software AG IT、ExecuPharm和Indiabulls。

本文翻译自：https://www.bleepingcomputer.com/news/security/clop-ransomware-claims-it-breached-130-orgs-using-goanywhere-zero-day/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?S4a09Why)

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