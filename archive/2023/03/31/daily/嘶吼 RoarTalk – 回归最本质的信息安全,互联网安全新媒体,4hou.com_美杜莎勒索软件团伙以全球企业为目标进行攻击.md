---
title: 美杜莎勒索软件团伙以全球企业为目标进行攻击
url: https://www.4hou.com/posts/zl28
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-31
fetch_date: 2025-10-04T11:13:17.523297
---

# 美杜莎勒索软件团伙以全球企业为目标进行攻击

美杜莎勒索软件团伙以全球企业为目标进行攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 美杜莎勒索软件团伙以全球企业为目标进行攻击

~阳光~
[新闻](https://www.4hou.com/category/news)
2023-03-30 11:22:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)138796

收藏

导语：2023年，一个名为Medusa的勒索软件团伙开始进行了大范围的攻击。它们的目标是全球的企业，并要求其支付百万美元的赎金。

从2021年6月开始，关于美杜莎团伙，只看到了少量的受害者和一些低水平的攻击活动。然而，这个勒索软件团伙在2023年加大了行动力度，并建立了一个 "美杜莎博客"，威胁拒绝支付赎金的受害者要对外泄露他们的数据。

上周，Medusa声称对明尼阿波利斯公立学校（MPS）区的攻击负责，并分享了一段被盗数据的视频后，受到了公众的广泛关注。

**关于美杜莎的介绍**

Medusa是几个恶意软件家族的名字，这其中包括著名的MedusaLocker勒索软件家族，一个Android恶意软件家族，以及一个基于Mirai的具有勒索软件功能的僵尸网络。

由于该家族的名字一直被广泛使用，而且关于它的信息也一直很模糊，导致许多人认为它与MedusaLocker相同。然而，Medusa和MedusaLocker恶意软件之间存在着明显的差异。

MedusaLocker在2019年作为赎金软件即服务首次亮相，它攻击了大量的机构，赎金说明文件通常是How\_to\_back\_files.html，这其中还包括一些加密文件。

关于赎金的谈判，MedusaLocker使用了一个Tor网站qd7pcafncosqfqu3ha6fcx4h6sr7tzwagzpcdcnytiw3b6varaeqv5yd.onion。

然而，.MEDUSA静态加密文件扩展名和!!!READ\_ME\_MEDUSA!!!.txt赎金说明自2021年6月启动以来，就一直被Medusa勒索软件团伙所使用。

**使用Windows程序来加密数据**

目前，不知道安全专家是否针对Linux的Medusa加密程序进行了分析；目前只知道他们分析了Windows版本。Windows加密器可以接受命令行参数，让威胁行为者控制系统中文件加密设置。例如，如果使用-v命令行参数，该勒索软件将显示一个控制台，并在加密设备时显示状态信息。

美杜莎勒索软件会终止280多个可能阻止文件被定期加密的Windows服务和进程。数据库服务器、备份服务器和安全应用程序的Windows服务都在其中。然后，为了防止文件被轻易恢复，勒索软件将会删除Windows影子卷副本。

勒索软件专家Michael Gillespie也检查了这个加密器，并向媒体透露，它使用了BCrypt库的AES-256 + RSA-2048加密方式来加密文件。

像大多数针对企业的勒索软件一样，Medusa的特点是建立了一个名为 "Medusa博客 "的网站，攻击者主要从这里泄露数据。这个网站的搭建也是该团伙双重勒索计划的一部分，拒绝支付赎金的受害者，那么就会对外公开他们的数据。

当攻击者决定对外公开受害者的数据时，他们的数据并不会立即被公开。还有另外的一种选择，威胁者还会向受害者提供各种付款选择，以推迟数据的发布，数据的删除，或下载整个数据集。每种选择的成本都不同。

要求赎金是为了增加受害者内心的压力，威胁他们尽快支付赎金。但是遗憾的是，在Medusa Ransomware的加密程序中并没有找到任何漏洞，允许受害者在不付费的情况下恢复其系统的文件。

本文翻译自：https://www.cysecurity.news/2023/03/targeting-businesses-globally-medusa.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Ub3hXvFp)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/portraits/f1cf9065382964bd9f4a9cd061a16d17.jpg)

# [~阳光~](https://www.4hou.com/member/lPjj)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/lPjj)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

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