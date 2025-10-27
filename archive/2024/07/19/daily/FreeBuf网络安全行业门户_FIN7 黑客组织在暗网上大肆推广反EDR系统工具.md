---
title: FIN7 黑客组织在暗网上大肆推广反EDR系统工具
url: https://www.freebuf.com/news/406306.html
source: FreeBuf网络安全行业门户
date: 2024-07-19
fetch_date: 2025-10-06T17:41:47.540067
---

# FIN7 黑客组织在暗网上大肆推广反EDR系统工具

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

FIN7 黑客组织在暗网上大肆推广反EDR系统工具

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

FIN7 黑客组织在暗网上大肆推广反EDR系统工具

2024-07-18 10:13:36

所属地 上海

![1721268955_66987adb767b9395346cd.png!small](https://image.3001.net/images/20240718/1721268955_66987adb767b9395346cd.png!small)

据观察，近日有名为 FIN7 的威胁行为者在多个地下论坛上使用虚假用户名大肆宣传安全绕过工具，这些工具都曾被 Black Basta 等勒索软件组织使用过。

AvNeutralizer（又名 AuKill）是 FIN7 开发的一种高度专业化的工具，用于篡改安全解决方案，已在地下犯罪组织中进行销售，并被多个勒索软件组织使用。

FIN7 是一个源于俄罗斯和乌克兰的电子犯罪团伙，至少从 2012 年开始就一直是一个持续性威胁，最初只针对销售点（PoS）终端攻击，目前已转变为充当 REvil 和 Conti 等现已解散团伙的勒索软件附属机构，之后又推出了自己的勒索软件即服务（RaaS）项目 DarkSide 和 BlackMatter。

该威胁行为者还以 Carbanak、Carbon Spider、Gold Niagara 和 Sangria Tempest（前 Elbrus）等名称进行追踪，其前科包括成立 Combi Security 和 Bastion Secure 等虚假公司，以渗透测试为借口招募不知情的软件工程师参与勒索软件计划。

多年来，FIN7 通过重新组合其恶意软件库POWERTRASH、DICELOADER（又名 IceBot、Lizar 或 Tirion），以及通过 POWERTRASH 加载器交付的名为 Core Impact 的渗透测试工具），展示了过人的适应性、复杂性和技术专长，尽管其部分成员已被逮捕和判刑。

根据 Silent Push 最近的一份报告，该组织通过部署数千个模仿合法媒体和技术企业的 “空壳 ”域名来发送勒索软件和其他恶意软件系列，从而开展了大规模的网络钓鱼活动。

另外，这些空壳域名偶尔也会被用于传统的重定向链，将用户发送到伪装成物业管理门户网站的欺骗性登录页面。

比如在在谷歌等搜索引擎上做广告，诱使搜索流行软件的用户下载带有恶意软件的变种。目标工具包括 7-Zip、PuTTY、AIMP、Notepad++、Advanced IP Scanner、AnyDesk、pgAdmin、AutoDesk、Bitwarden、Rest Proxy、Python、Sublime Text 和 Node.js。

值得注意的是，此前 eSentire 和 Malwarebytes 曾在今年5 月强调过 FIN7 使用恶意广告策略的情况，其攻击链导致了 NetSupport RAT 的部署。

Silent Push 指出：FIN7 在许多主机上租用了大量专用 IP，但主要是在 Stark Industries 上，这是一家流行的防弹主机提供商，曾与乌克兰和整个欧洲的 DDoS 攻击有关。

SentinelOne 的最新调查结果显示，FIN7 不仅在网络犯罪论坛上使用多个虚假用户名来推广 AvNeutralizer 的销售，还对该工具进行了改进，增加了新的功能。

这是因为从 2023 年 1 月起，多个勒索软件组织开始使用 EDR 减损程序的更新版本，而在此之前，该程序一直由 Black Basta 组织独家使用。

SentinelLabs 研究员Antonio Cocomazzi表示，在没有更多证据的情况下，不应将 AvNeutralizer 在地下论坛上的广告视为 FIN7 采用的一种新的恶意软件即服务（MaaS）策略。

FIN7 一直在开发和使用复杂的工具以为自己的行动提供便利，然而向其他网络犯罪分子出售工具可以被看作是他们实现多样化和创造额外收入的方法的自然演变。

FIN7很善于利用地下市场创收。例如，司法部报告称，自 2015 年以来，FIN7 成功窃取了 1600 多万张支付卡的数据，其中许多都在地下市场出售。虽然这种情况在前ransomware时代较为常见，但目前AvNeutralizer的广告可能预示着他们的策略发生了转变或扩大。

这可能是由于与以前的反病毒系统相比，如今的电子数据删除解决方案提供了越来越多的保护。随着这些防御能力的提高，对 AvNeutralizer 等减损工具的需求也大幅增长，尤其是勒索软件运营商。攻击者现在在绕过这些保护措施方面面临着更严峻的挑战，这使得这类工具变得非常有价值和昂贵。

就其本身而言，AvNeutralizer 的更新版本采用了反分析技术，最重要的是，它利用名为 “ProcLaunchMon.sys ”的 Windows 内置驱动程序和进程资源管理器驱动程序来篡改安全解决方案的功能并逃避检测。据信，该工具自 2022 年 4 月以来一直在积极开发中。

Lazarus Group 也使用了类似版本的方法，它超越了传统的 “自带漏洞驱动程序”（BYOVD）攻击，将 Windows 机器默认存在的易受影响的驱动程序作为武器，因此更加危险。

另一个值得注意的更新涉及 FIN7 的 Checkmarks 平台，该平台已被修改为包含一个自动 SQL 注入攻击模块，用于利用面向公众的应用程序。

SentinelOne表示：FIN7在其活动中采用了自动化的攻击方法，希望通过自动化SQL注入的方式对公众的服务器实施攻击。此外，他们还在地下犯罪论坛中开发并商业化了 AvNeutralizer 等专用工具，极大地增强了该组织的影响力。

> 参考来源：[FIN7 Group Advertises Security-Bypassing Tool on Dark Web Forums (thehackernews.com)](https://thehackernews.com/2024/07/fin7-group-advertises-security.html)

# 黑客工具 # FIN7 # 地下黑客论坛

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)