---
title: 使用攻击者的工具抵御Hive勒索软件
url: https://www.4hou.com/posts/gXjj
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-03
fetch_date: 2025-10-04T00:22:55.201639
---

# 使用攻击者的工具抵御Hive勒索软件

使用攻击者的工具抵御Hive勒索软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 使用攻击者的工具抵御Hive勒索软件

~阳光~
[新闻](https://www.4hou.com/category/news)
2022-12-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)138846

收藏

导语：美国的安全机构警告说，自2021年6月以来，Hive勒索软件攻击每月可以为网络犯罪分子带来近600万美元的收入，并且他们已经成功攻击了1300多名受害者。

最新版本的Hive有效载荷是用Rust编写的，之前是用Go编写的。它通常会在攻击者通过利用钓鱼邮件、暴露的RDP、利用未打补丁的软件（FortiOS漏洞CVE-2020-12812和微软Exchange的ProxyShell漏洞已经受到青睐；还会有其他漏洞）或泄露的VPN信条（即所有许多常见的机器和网络被破坏的方式）访问网络后进行投放。

像大多数复杂的勒索软件的有效载荷一样，Hive勒索软件运行的进程会杀死一系列的防病毒/EDR工具，删除备份并阻止恢复。正如美国网络安全机构CISA 11月17日所说，它禁用了 "系统注册表中的Windows Defender和其他常见的防病毒程序的所有部分"。

(微软在夏天的分析显示，它终止了以下进程，其中包括常见的备份和安全工具。Windefend, msmpsvc, kavsvc, antivirservice, vmm, vmwp, sql, sap, oracle, mepocs, veeam, backup, vss, msexchange, mysql, sophos, pdfservice, backupexec, gxblr, gxvss, gxclmgrs, gxcimgr, gxmmm, gxvsshwprov, gxfwd, sap, qbcfmonitorservice, acronisagent, veeam, mvarmor, acrsch2svc等进程 )

**攻击者青睐于域内的攻击**

SentinelOne在早前的分析中指出，目前已经发现Hive使用了开源工具ADRecon来映射、穿越和列举AD环境。趋势科技最近对另一种新出现的勒索软件类型Play的调查也强调，在信息搜集阶段，勒索软件攻击者会收集更多关于AD域环境的细节。我们观察到，不同的工具对远程系统进行了AD查询，如ADFind、Microsoft Nltest和Bloodhound会列举系统信息，如主机名、共享和域信息。

这样的工具也可以免费提供给安全方面的IT专业研究人士，也非常值得那些从未部署过这些工具的人探索。

正如Bloodhound的联合创建者Andy Robbins去年所说的，该工具旨在帮助映射和利用AD（现在也在Azure AD）中的攻击路径。正如他所指出的。蓝队方面的很多人都是在该工具被专业人士或攻击者用来对付他们自己时才知道的。

但实际情况是，BloodHound能够为蓝队提供的价值远远超过它对红队的价值，因为它向蓝队展示了他们的环境中存在哪些攻击路径，这样他们就可以在对手发现和利用这些攻击路径之前将其清理掉。

同时，CISA最近的Hive勒索软件指南可能已经被那些注重安全的人看到过很多次了，但它也只是针对一些核心网络的一个检查清单。

美国网络安全机构说，组织应该在操作系统、软件和固件发布后，立即安装更新。 优先修补VPN服务器、远程访问软件、虚拟机软件和已知被利用的漏洞。并且还应该考虑利用一个集中的补丁管理系统来自动化管理和加速这一过程。

他们还应该使用尽可能多的服务比如采用抗网络钓鱼的MFA，特别是网络邮件、VPN、访问关键系统的账户以及管理备份的特权账户。

如果使用RDP，应确保其安全性并对其进行监控，限制访问的源地址，并要求使用MFA减少凭证盗窃和重复使用。如果RDP必须在外部使用，在允许RDP连接到内部设备之前，使用VPN、虚拟桌面基础设施或其他方式来验证和保护连接。

维护数据的离线备份，并定期维护备份和恢复。通过使用这种做法，组织确保他们不会被严重干扰。

确保所有的备份数据是加密的，不可改变的（即不能被改变或删除），并覆盖整个组织的数据基础设施。确保你的备份数据还没有被感染。

禁用命令行和脚本的活动权限。特权升级和横向移动往往依赖于从命令行运行的软件工具。如果威胁者不能运行这些工具，他们将很难升级权限和/或横向移动。

确保设备的正确配置，并确保安全功能已经被启用。

在网络内限制服务器信息块（SMB）协议，只访问必要的服务器，并删除或禁用过期的SMB版本（即SMB版本1）。

组织还应该识别并优先恢复关键系统，确认受影响系统中存放的数据的性质，并根据预先确定的关键资产清单确定恢复的优先次序，包括对健康和安全、创收或其他关键服务至关重要的信息系统，以及它们所依赖的系统。

本文翻译自：https://thestack.technology/defending-against-hive-ransomware-using-the-attackers-tools/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GQXfIfOu)

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