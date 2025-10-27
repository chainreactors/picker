---
title: 浅谈云安全的技术实践与格局变迁 |FreeBuf咨询洞察
url: https://www.freebuf.com/articles/paper/357502.html
source: FreeBuf网络安全行业门户
date: 2023-02-15
fetch_date: 2025-10-04T06:37:41.031615
---

# 浅谈云安全的技术实践与格局变迁 |FreeBuf咨询洞察

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

浅谈云安全的技术实践与格局变迁 |FreeBuf咨询洞察

* ![]()
* 关注

* [咨询](https://www.freebuf.com/consult)

浅谈云安全的技术实践与格局变迁 |FreeBuf咨询洞察

2023-02-14 12:04:04

![1676346627_63eb0503cc0a158bc7d59.png!small](https://image.3001.net/images/20230214/1676346627_63eb0503cc0a158bc7d59.png!small)

从早年简单的云主机杀毒，到一体化云上态势感知，从底层计算、存储资源云化到云上软件全生命周期的安全防护，从安全产品的云化到云中内生安全；历经十多年的发展，云安全产业无论是市场需求、防护边界、技术实践还是落地形态都经历了翻天覆地的变化。云安全的责任归属、多云、跨云环境下的安全治理、云应用开发部署全生命周期的安全保护也成为了云服务提供及使用者关注的焦点。FreeBuf咨询特别发布《云安全的技术实践与格局变迁洞察》报告，旨在呈现我国云安全市场的发展特点与脉络，追踪我国云安全技术实践与格局变迁，从而捕捉我国云安全产业的未来发展趋势。

## **报告关键发现**

1. 我国云安全市场的下半场竞争将从IaaS层向PaaS层迁移

2. 绝大多数的云安全事件的责任在企业而非厂商，云服务使用者需充分理解责任共担模型以更好地分配云责任归属

3. 全球公有云市场占绝对主导，我国私有云/行业云市场仍占据较高的比例。海内外用户对资产数据的敏感程度以及对于供应商的信任感构成了两者之间的偏好差异

4. 在多云趋势下，CIEM优势逐渐凸显，帮助企业在更模糊的边界中实现最低身份授权

5. ZTNA、Kubernetes、IaC、DevSecOps技术的不断发展将重塑云安全市场格局

6. 云安全顶层标准制度不断健全，从底层框架、重点行业，向产品层、厂商层以及细分技术层不断拓宽细化

7. 云安全的实践形态正在从安全产品云化走向云中内生安全

## **我国云安全市场规模高速扩张**

云计算的迅速普及带动云安全市场规模持续高增速扩张。IDC预测，到2024年，全球云基础设施占比将超过6成。安全作为保障云计算发展革新的基础，也成为了全球企业上云面临的最大挑战之一，云安全的市场需求在此背景下高速攀升。艾瑞咨询数据显示，我国云安全市场规模将在2024年达到254亿元，年均增速超过40%。![1676346787_63eb05a31abfa602becaa.png!small](https://image.3001.net/images/20230214/1676346787_63eb05a31abfa602becaa.png!small)

## **云安全发展历程**

FreeBuf咨询认为，云安全的发展历程可以大致分为四个阶段：萌芽阶段、云化阶段、加速发展阶段以及云原生阶段。

萌芽阶段期，云计算概念刚刚兴起。此时用户主要关注云基础设施安全防护，产品形态以简单的云主机防病毒以及云网关组件为主。

伴随AWS 推出 EC2 弹性计算云服务，国内最大的公有云服务商阿里云的成立，各大互联网平台以自身业务需求为契机，将云计算发展推向了另一个高潮，公有云厂商初具规模。

随着云计算的快速发展，阿里、腾讯、百度等公有云服务商全面布局云安全，带领云安全市场进入快速发展期。在此阶段内，除了云服务商，大量传统安全厂商涌入赛道内，提出云化安全解决方案，专注于云安全的厂商也开始涌现。

近年来，云安全建设重点从安全产品云化转向云中内生安全。云安全服务使用者需求从以资源为中心转移到以应用为中心，包括应用敏捷交付、快速弹性、平滑迁移、无损容灾等，带动云安全服务商将服务范围拓展至开发端，能力下沉至平台侧。

![1676346856_63eb05e8db9d059970e8d.png!small](https://image.3001.net/images/20230214/1676346856_63eb05e8db9d059970e8d.png!small)

## **云安全顶层标准制度不断健全**

云安全顶层标准制度不断健全，从重点领域、底层框架，向产品层、厂商层以及细分技术层不断拓宽细化。云安全产业联盟CSA在2009年发布了首个云计算安全实践《针对云计算重点领域的安全指南》，2010年发布云控制矩阵（CCM）几乎涵盖了云技术的所有关键领域，映射了大量法律法规和国际标准的要求。2014年，我国发布《云计算服务安全指南》与《云计算服务安全能力要求》两项标准，用于政府部门云上安全管理，并指导云厂商建设安全的云平台与服务。

2016年CSA大中华区发布了首个产品级云安全标准。而2018年由CSA发布的云计算可信厂商（TCP）标识，从厂商角度为华为、亚马逊、微软等数十家云厂商提供认证。2022年《云安全技术标准 2.0》、《云应用安全技术规范（CAST）》和《云原生安全技术规范（CNST）》的出台提供了云原生、云应用等细分技术层面的建设思路。

![1676346900_63eb061477c6c7118dd93.png!small](https://image.3001.net/images/20230214/1676346900_63eb061477c6c7118dd93.png!small)

## 报告全文见下图：

![1676347431_63eb08271d2c815054a9e.jpg!small](https://image.3001.net/images/20230214/1676347431_63eb08271d2c815054a9e.jpg!small)

## 关于FreeBuf咨询

FreeBuf咨询集结安全行业经验丰富的安全专家和分析师，常年对网络安全技术、行业动态保持追踪，洞悉安全行业现状和趋势，呈现最专业的研究与咨询服务，主要输出四个种类的咨询报告：行业研究报告、能力评估报告、产品研究报告以及甲方定制化报告。FreeBuf咨询自成立以来, 已积累了500+ 甲方安全智库资源，为行业研究报告、企业咨询服务提供指导。访谈上百位行业大咖，为业界输出真实、丰富的安全管理价值与实践经验，具备超过80万+ 精准用户，直接触达CSO、企业安全专家、投资人等专业人群。

如有疑问，请联系 FreeBuf 咨询 朱先生 ：

电话：16601757018

邮箱：xinyi.zhu@tophant.com

# 云安全

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

报告关键发现

我国云安全市场规模高速扩张

云安全发展历程

云安全顶层标准制度不断健全

报告全文见下图：

关于FreeBuf咨询

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