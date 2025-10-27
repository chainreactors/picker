---
title: 黑客组织Scattered Spider正疯狂攻击VMware ESXi管理程序
url: https://www.4hou.com/posts/rpxE
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-31
fetch_date: 2025-10-06T23:17:13.941497
---

# 黑客组织Scattered Spider正疯狂攻击VMware ESXi管理程序

黑客组织Scattered Spider正疯狂攻击VMware ESXi管理程序 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客组织Scattered Spider正疯狂攻击VMware ESXi管理程序

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-07-30 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)72466

收藏

导语：需要注意的是，Scattered Spider在虚拟基础设施上获得的控制级别允许它们管理所有可用的资产，包括备份机器，这些机器被清除了备份作业、快照和存储库。

名为分散蜘蛛 (Scattered Spider)的网络犯罪组织通过攻击美国零售、航空、运输和保险行业的VMware ESXi管理程序，积极瞄准虚拟化环境。

根据谷歌威胁情报组织（GITG）的说法，攻击者一直在使用他们通常的策略，不包括漏洞利用，而是依靠完美执行的社会工程“绕过成熟的安全程序”。

**Scattered Spider攻击**

研究人员表示，该团伙通过在呼叫IT帮助台时冒充员工随后开始攻击。威胁者的目的是说服代理更改员工的Active Directory密码，从而获得初始访问权限。

这样，Scattered Spider就可以扫描网络设备，寻找能够提供高价值目标的IT文档，比如域或VMware vSphere管理员的名称，以及可以提供虚拟环境管理权限的安全组。

与此同时，他们扫描特权访问管理（PAM）解决方案，这些解决方案可能包含敏感数据，这些数据对转移到有价值的网络资产很有用。

然后，黑客们通过自己的方式获得了对该公司VMware vCenter Server Appliance （vCSA）的访问权——这是一种允许管理VMware vSphere环境的虚拟机，其中包括用于管理物理服务器上所有虚拟机的ESXi管理程序。

此级别的访问权限使他们能够在ESXi主机上启用SSH连接并重置根密码。此外，他们执行所谓的“磁盘交换”攻击，以提取Active Directory的NTDS.dit关键数据库。

磁盘替换攻击发生在威胁者关闭域控制器虚拟机 (VM) 并仅分离其虚拟磁盘，然后将其附加到他们控制的另一个未受监控的VM上时。在复制敏感数据（例如 NTDS.dit 文件）后，他们还原该过程并开启域控制器机器。

需要注意的是，Scattered Spider在虚拟基础设施上获得的控制级别允许它们管理所有可用的资产，包括备份机器，这些机器被清除了备份作业、快照和存储库。

在攻击的最后阶段，Scattered Spider利用他们的SSH访问来交付和部署勒索软件二进制文件，以加密数据存储中检测到的所有VM文件。

根据他们的观察，GTIG研究人员表示，分散蜘蛛攻击有五个不同的阶段，这些阶段允许黑客从低级访问转移到完全控制虚拟机管理程序。

![attack-chain.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250728/1753688357145250.jpg "1753685721418872.jpg")

Scattered Spider攻击

一个分散的蜘蛛攻击链，从最初的访问到数据泄露和勒索软件部署，可能在几个小时内发生。据谷歌相关人员表示，即使没有利用任何软件漏洞，威胁者也设法对整个虚拟环境进行前所未有的控制，使他们能够绕过许多传统的来宾安全控制。

虽然针对ESXi虚拟机管理程序并不是什么新鲜事，但GTIG指出，他们正看到越来越多的勒索软件组织采用这种策略，并预计这个问题会越来越严重。

这背后的一个原因可能是，对手已经注意到，VMware的基础设施通常不被组织所了解，因此，没有得到强有力的防御。

为了帮助组织抵御这些攻击，谷歌发布了一篇技术文章，描述了Scattered Spider攻击的各个阶段，解释了为什么它是有效的，并提供了公司可以采取的措施，以便在早期阶段检测到漏洞。

建议的措施可归纳为三个主要方面：

**·**使用execinstalldonly、虚拟机加密和禁用SSH锁定vSphere。避免ESXi上的AD直接连接，删除孤立虚拟机，执行严格的MFA和访问策略。持续监控配置漂移。

**·**跨VPN、AD和vCenter使用防网络钓鱼的MFA。隔离Tier 0资产（数据中心、备份、PAM），避免将它们托管在它们所保护的相同基础设施上。考虑单独的云idp来打破AD依赖。

**·**将日志集中在SIEM中，并对关键行为（如管理员组更改、vCenter登录和启用SSH）进行警报。使用不可变的气隙备份和针对管理程序层攻击的测试恢复。

Scattered Spider（也被称为UNC3944， Octo Tempest，0ktapus）是一个以经济为动机的威胁组织，专门从事社会工程，它最近加强了对英国大型零售公司、航空公司和运输实体以及保险公司的攻击活动。尽管英国国家犯罪局逮捕了该组织的4名疑似成员，但源自其他集群的恶意活动并没有消退，安全研究人员建议人们应该继续保持谨慎。

文章翻译自：https://www.bleepingcomputer.com/news/security/scattered-spider-is-running-a-vmware-esxi-hacking-spree/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?O7WGHLus)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

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

[查看更多](https://www.4hou.com/member/BVMN)

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