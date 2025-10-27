---
title: 微软：100多名攻击者使用了超50种勒索软件
url: https://www.freebuf.com/news/356171.html
source: FreeBuf网络安全行业门户
date: 2023-02-02
fetch_date: 2025-10-04T05:29:22.387595
---

# 微软：100多名攻击者使用了超50种勒索软件

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

微软：100多名攻击者使用了超50种勒索软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

微软：100多名攻击者使用了超50种勒索软件

2023-02-01 10:46:48

所属地 上海

1月31日，微软透露其安全团队Redmond正在跟踪 100 多个在攻击期间部署勒索软件的攻击者，总共监控到 50 多个在去年被频繁使用的勒索软件系列。

微软例举了一些最突出的勒索软件有效负载，包括Lockbit Black、BlackCat（又名 ALPHV）、Play、Vice Society、Black Basta 和 Royal。但微软表示“防御策略应该更少地关注有效负载，而更多地关注导致其部署的活动链”，因为勒索软件仍在针对那些不常见漏洞或最近正需要修补漏洞的设备进行攻击。

![](https://image.3001.net/images/20230201/1675221510_63d9da067426c3d51ce5d.png!small)

## 攻击策略

虽然一直有新的勒索软件系列出现，但大多攻击者在破坏网络和通过网络传播时都使用相同的策略，对此类行为进行检测将有助于阻止他们的攻击。

微软也提到，攻击者越来越依赖网络钓鱼以外的策略来进行攻击，比如利用 Exchange Server 的DEV-0671 和 DEV-0882漏洞部署 Cuba 和 Play 勒索软件。就在不久前，Exchange 团队敦促客户通过应用最新支持的累积更新 (CU) 来为本地 Exchange 服务器打补丁，让他们随时准备部署紧急安全更新。据报道，超过 60000 台暴露在 Internet 上的 Exchange 服务器容易受到利用ProxyNotShell RCE 漏洞的攻击。与此同时， 也有数千台服务器正受到利用ProxyShell 和 ProxyLogon 漏洞攻击的风险，这是2021年最常被利用的两个安全漏洞。

其他攻击者也正在转向或使用恶意广告来提供恶意软件加载器和下载器，以传播勒索软件和各种其他恶意软件变种，如信息窃取程序。例如，一个被追踪为 DEV-0569 的攻击者被认为是勒索软件团伙的初始访问代理，在广告活动中滥用 Google Ads来分发恶意软件，从受感染的设备中窃取密码，并最终获得对企业网络的访问权限，并将权限出售给其他攻击者，如Royal 勒索软件组织。

## 近期活动趋势

在具体的勒索软件活动趋势中，2022年的一起标志性事件是Conti勒索软件组织在执法行动的压力下迎来终结，但基于勒索软件即服务 (Raas) 的勒索行为正在兴起，包括LockBit、Hive、Cuba、BlackCat 和 Ragnar在内的勒索软件组织在去年频繁作案。

尽管如此，  根据区块链分析公司 Chainalysis 的数据，勒索软件组织去年的勒索收入大幅下降了 40% 左右，为4.568 亿美元，而前年的收入达到了创纪录的 7.65 亿美元。但这种下降趋势并不是因为攻击次数减少，而是因为越来越多的受害者开始拒绝支付勒索赎金。

最近，在美国司法部、联邦调查局、特勤局和欧洲刑警组织的国际执法行动的打击下，Hive 勒索软件数据泄露和 Tor 支付暗网被查封，FBI向受害者分发了 1300 多个解密密钥，并获得了对 Hive 通信记录、恶意软件文件哈希值和 250 个 Hive 分支机构详细信息的访问权限，美国国务院也悬赏1000万美元，寻求 Hive 勒索软件组织或其他攻击者与外国政府存在联系的线索。

某种程度上说，在打击勒索软件领域，2023年似乎迎来了开门红。

> 参考来源：[Microsoft: Over 100 threat actors deploy ransomware in attacks](https://www.bleepingcomputer.com/news/security/microsoft-over-100-threat-actors-deploy-ransomware-in-attacks/)

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

攻击策略

近期活动趋势

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