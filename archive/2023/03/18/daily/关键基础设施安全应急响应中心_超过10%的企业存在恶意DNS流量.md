---
title: 超过10%的企业存在恶意DNS流量
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247535465&idx=3&sn=2d1c04bd63a2d251f6e8130464203d85&chksm=c1e9c738f69e4e2e3b08ce1d433c862cb033664bfff3154e87c1e4286df0f79ab1f648b7303d&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2023-03-18
fetch_date: 2025-10-04T09:58:42.631207
---

# 超过10%的企业存在恶意DNS流量

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGoguuYuQvON9tciaicG93HB1frm3SMiaq7xGMoClrgM74EqXGMd934QHRpEW2FMBTDZuYnTibwpIiaNbAIkA/0?wx_fmt=jpeg)

# 超过10%的企业存在恶意DNS流量

关键基础设施安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGoguuYuQvON9tciaicG93HB1frmIyoQnQYCAOiauia420hx8icfjLKfaAIlLKn9drh4bluSLchrMnS1UGqEg/640?wx_fmt=png)

根据Akamai最新发布的DNS数据报告，2022年10%到16%的企业产生过C2流量，指向僵尸网络和恶意软件的命令和控制（C2）服务器。

报告称，超过四分之一的企业恶意流量流向了初始访问代理人（IAB）的服务器，这些初始访问代理人负责将公司网络的访问权限出售给其他网络犯罪分子。

2022年，由于安卓恶意软件FluBot的全球性传播，以及针对企业的各种有组织网络犯罪活动，企业和家庭用户的恶意DNS流量出现过几次爆发峰值。值得业界高度警惕的是，与初始访问代理相关的C2流量始终保持着惊人的规模。初始访问代理人会入侵公司网络，获取访问凭证并兜售给其他网络犯罪分子（例如勒索软件即服务RaaS）来获利。

**恶意软件控制了庞大的互联网设备池**

Akamai为其全球CDN、云服务和安全服务运营着一个大型DNS基础设施，每天能够监测多达2万亿个DNS请求。由于DNS查询会尝试解析域名的IP地址，因此Akamai可以分析来自公司网络或家庭用户的DNS请求是否映射到那些已知的托管网络钓鱼页面、恶意软件或C2服务器的恶意域名/IP地址。

根据报告，2022年在发出DNS请求的所有设备中，Akamai发现有9%到13%试图访问恶意软件服务器，4%至6%尝试解析网络钓鱼域名，0.7%至1%尝试解析C2服务器地址。

与恶意软件相比，C2流量的占比似乎很小，但考虑到庞大的联网设备池每天能够生成的DNS请求数量高达7万亿次，每天的C2流量规模依然是百亿级别。

对恶意软件托管站点的请求不一定转化为成功的入侵，因为恶意软件在设备上执行之前可能会被检测到并阻止。但是，对C2服务器的查询表明（企业）存在活跃的恶意软件感染。

如今大型企业网络中拥有成千上万个联网设备，任何端点设备被感染都可能导致网络被完全接管。正如我们在大多数勒索软件案例中看到的，攻击者会采用横向移动技术在企业内部系统之间跳转。

根据对C2服务器的企业DNS数据的统计，去年有超过十分之一的企业遭受过入侵。恶意C2流量的行业分布如下：

* 制造业30%
* 商业服务15%高科技14%
* 商业12%

值得注意的是，恶意DNS数据占比最高的两个行业（制造业和商业服务），同时也是Conti勒索软件的主要攻击对象。

**僵尸网络占恶意流量的44%**

Akamai将C2流量细分为几类：僵尸网络、初始访问代理（IAB）、信息窃取程序、勒索软件、远程访问木马（RAT）等（下图）。

![](https://mmbiz.qpic.cn/mmbiz_png/INYsicz2qhva9iaXjv0ibQYe5ArfiaPalicHMibKCOoD3No7kRaM2ZfgRNmlhQmEzKkhLsGCRxxmBABkQ1uE41sjJ4lA/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

其中僵尸网络在恶意C2流量种的占比高达44%（该项数据没有统计一些著名的僵尸网络，如Emotet或Qakbot，这些僵尸网络主要销售系统访问权限的业务，因此被计入IAB类别。）但是，从技术上讲，大多数僵尸网络都可用于提供额外的恶意软件有效负载，即使其所有者不公开销售此服务，有些僵尸网络也有私人交易。例如，TrickBot僵尸网络与Ryuk勒索软件背后的网络犯罪分子建立了私人工作关系。

Akamai在来自企业环境的C2流量中观察到的最大僵尸网络是QSnatch，后者依赖一种专门感染过时QNAP网络连接存储（NAS）设备固件的恶意软件。QSnatch于2014年首次出现，至今仍保持活跃。根据CISA的公告，截至2020年年中，全球有超过6.2万台受感染的QNAP设备。QSnatch会阻止QNAP存储设备的安全更新，用于凭据抓取、密码记录、远程访问和数据泄露。

IAB是C2 DNS流量中的第二大类别，其中Emotet占比高达22%，Qakbot占4%。Emotet是规模最大、运行时间最长的僵尸网络之一，向大量网络犯罪集团提供企业网络的初始访问权限。此外，Emotet还被用于部署其他僵尸网络，包括TrickBot和Qakbot。

**僵尸网络与勒索软件关系密切**

2021年，来自美国、英国、加拿大、德国和荷兰等多个国家的执法机构设法接管了僵尸网络的命令和控制基础设施。然而，胜利是短暂的，如今僵尸网络通过迭代卷土重来，甚至变得更强大了。

例如，Emotet最初是一个银行木马，但已经进化成一个模块化的多功能恶意软件交付平台，其中一些模块还能用来窃取电子邮件，发起DDoS攻击等。Emotet还与勒索软件团伙有千丝万缕的联系，其中最著名的是Conti。

与Emotet类似，僵尸网络Qakbot也提供额外的有效载荷，并与勒索软件团伙（例如Black Basta）建立了伙伴关系。Qakbot还利用Cobalt Strike渗透测试工具提供额外的功能，包括驻留和窃取信息的能力。

众所周知，僵尸网络会被用于分发勒索软件，后者一旦成功部署，会启用自己的C2服务器，此类C2流量也包含在Akamai统计的DNS数据中。超过9%的C2流量指向已知勒索软件威胁相关域名，其中REvil和LockBit占比最高。

信息窃取恶意软件是C2流量的第三大类别，占Akamai观察到的设备总数的16%，其中Ramnit占比最高。Ramnit是一种模块化信息窃取程序，也可用于部署其他恶意软件。信息窃取恶意软件的目标是企业网络中的高价值信息，例如各种服务的用户名和密码、存储在浏览器中的身份验证cookie以及存储在本地其他应用程序中的凭据。

其他值得关注的恶意C2流量中的威胁包括：Cobalt Strike、Agent Tesla RAT、Pykspa蠕虫和Virut多态病毒。

**报告链接：**

https://www.akamai.com/blog/security/a-deep-dive-on-malicious-dns-traffic

原文来源：GoUpSec

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogucKMiatGyfBHlfj74r3CyPxEBrV0oOOuHICibgHwtoIGayOIcmJCIsAn02z2yibtfQylib07asMqYAEw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过