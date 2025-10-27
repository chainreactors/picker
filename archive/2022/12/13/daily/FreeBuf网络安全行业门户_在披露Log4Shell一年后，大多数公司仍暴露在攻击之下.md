---
title: 在披露Log4Shell一年后，大多数公司仍暴露在攻击之下
url: https://www.freebuf.com/news/352218.html
source: FreeBuf网络安全行业门户
date: 2022-12-13
fetch_date: 2025-10-04T01:18:57.161780
---

# 在披露Log4Shell一年后，大多数公司仍暴露在攻击之下

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

在披露Log4Shell一年后，大多数公司仍暴露在攻击之下

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

在披露Log4Shell一年后，大多数公司仍暴露在攻击之下

2022-12-12 13:54:17

所属地 上海

![](https://image.3001.net/images/20221212/1670824448_6396c20002d5b2dddee37.png!small)

在Apache软件基金会去年11月披露Log4j漏洞一年后，虽然针对该漏洞本身的攻击数量低于最初的预期，但仍然对企业组织构成重大威胁。

安全研究人员说，仍然有很多系统没有针对该漏洞打补丁，企业在发现、修复和防止该漏洞上仍面临挑战。

"Contrast Security的首席安全信息官 David Lindner说："Log4j被用于约64%的Java应用程序，而其中只有50%的应用程序已经更新到完全固定的版本，这意味着攻击者将继续针对它。至少现在，攻击者继续在寻找通过Log4j进行攻击的途径。

## 攻击比预期的要少

Log4j的缺陷（CVE-2021-44228），通常被称为Log4Shell，存在于Log4j用于数据存储和检索的Java命名和目录接口（JNDI）。它可以帮助远程攻击者来控制易受攻击的系统。鉴于Log4J几乎被用于每一个Java应用环境，安全研究人员认为它是近年来最具威胁的漏洞之一，因为它很普遍，而且攻击者可以相对容易地利用它。

在过去的一年里，已经有许多关于攻击者利用该漏洞作为进入目标网络的报道。其中许多攻击涉及来自朝鲜、伊朗和其他国家的由国家支持的APT组织。例如，11月美国网络安全和基础设施安全局（CISA）警告说，一个由伊朗政府支持的APT组织利用未打补丁的VMware Horizon服务器中的Log4j漏洞，在一个联邦网络上部署了加密软件和凭证采集器。微软等其他公司也报告了类似的行为。

尽管还有其他一些关于有经济动机的网络犯罪团伙利用Log4j的报道， 但公开报道的涉及Log4的破坏事件的实际数量仍然比较低，特别是与涉及Exchange Server漏洞（如ProxyLogon和ProxyShell）的事件相比。Tenable公司的首席安全官Bob Huber说，相比于该漏洞的简单性和普遍的攻击路径，报告的攻击规模和范围出乎意料地低于预期。Huber说：只是在近期，我们才看到一些有针对性的重要报道，如最近CISA的民族性国家活动。

## 威胁未减弱

然而，安全研究人员指出，这并不意味着Log4j的威胁在过去一年中已经减弱。

首先，很大一部分企业仍然像一年前一样容易受到威胁。根据Tenable最近进行的一项与该漏洞有关的遥测分析显示，截至到10月1日，72%的企业容易受到Log4j的攻击，全球仅有28%的组织已经对该漏洞进行了全面修复。但当这些企业在向其环境中添加新的资产时，经常又一次地遭到Log4j的漏洞攻击。

Huber说：假设企业在软件的构建管道中建立修复，那么再一次地遭到Log4j漏洞攻击的概率会减少。是否会再一次地遭到Log4j漏洞攻击很大程度上取决于一个企业的软件发布周期。

此外，尽管网络安全界对这个漏洞的认识几乎无处不在，但由于应用程序如何使用Log4j，在许多企业中仍然很难找到有漏洞的版本。Sonatype公司首席技术官Brian Fox说，一些应用程序可能将开源日志组件作为其应用程序的直接依赖项，而在其他情况下，一些应用程序可能将Log4j作为一个交叉依赖项或另一个依赖项的依赖。

Fox说：由于过渡性依赖是从你的直接依赖项的选择中引入的，它们可能并不总是被你的开发人员所了解或直接看到。

Fox说，当Apache基金会首次披露Log4Shell时，公司不得不发出成千上万的内部电子邮件，在电子表格中收集结果，并递归扫描文件系统。这不仅仅花费了公司宝贵的时间和资源来修补该组件，而且延长了该漏洞的恶意影响程度。

来自Sonatype维护的Maven Central Java仓库的数据显示，目前35% 的 Log4 下载仍来自该软件的易受攻击版本。许多公司甚至在开始响应之前仍在尝试建立他们的软件清单，并且没有意识到传递依赖性的影响。

根据上述所有的问题，美国国土安全部审查委员会今年早些时候得出结论：Log4是一个地方性的安全风险，企业将需要与之抗衡多年。委员会成员评估说，Log4j的脆弱实例将在未来许多年里留在系统中，并使企业面临攻击的风险。

## 正面的影响

跟踪该漏洞的安全研究人员说，Log4j的积极成果是它引起了人们对软件构成分析和软件材料清单（SBOM）等实践的高度关注。企业在确定他们是否有漏洞或在他们的环境中可能存在的漏洞时所面临的挑战，促进了人们更好地理解对其代码库中所有组件的可见性需要，特别是那些来自开源和第三方的组件。

ReversingLabs的CISO Matthew Rose说：对Log4J问题的调查再次证实，除了跟上DevOps速度的SBOMs之外，还需要更好的软件供应链证明。应用安全和架构团队已经意识到，仅仅在源代码、API或开放源码包等部分寻找风险是不够的。他们现在意识到，全面了解应用程序的架构与寻找SQLI或跨站脚本错误（XSS）一样重要。

> 参考来源：https://www.darkreading.com/application-security/one-year-later-log4shell-exposed-attack

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

文章目录

攻击比预期的要少

威胁未减弱

正面的影响

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