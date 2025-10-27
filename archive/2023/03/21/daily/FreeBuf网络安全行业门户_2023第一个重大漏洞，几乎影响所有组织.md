---
title: 2023第一个重大漏洞，几乎影响所有组织
url: https://www.freebuf.com/news/361030.html
source: FreeBuf网络安全行业门户
date: 2023-03-21
fetch_date: 2025-10-04T10:09:12.344576
---

# 2023第一个重大漏洞，几乎影响所有组织

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

2023第一个重大漏洞，几乎影响所有组织

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

2023第一个重大漏洞，几乎影响所有组织

2023-03-20 15:44:29

所属地 上海

Dark Reading 网站披露，微软修复了 Outlook 中存在的零日漏洞，漏洞被追踪为 CVE-2023-23397，是一个权限提升漏洞，攻击者可以利用该漏洞访问受害者的 Net-NTLMv2 响应身份验证哈希并冒充用户。安全研究人员警告称 CVE-2023-23397 非常危险，有望成为近期影响最深远的漏洞。![1679301522_64181b9287a09e50ea9d3.png!small?1679301522650](https://image.3001.net/images/20230320/1679301522_64181b9287a09e50ea9d3.png!small?1679301522650)

CVE-2023-23397 漏洞由乌克兰计算机应急响应小组（CERT）的研究人员和微软一名研究人员发现，本周早些时候微软已经进行了补丁更新。

## ****攻击者能够轻松利用漏洞****

一旦攻击者成功利用 CVE-2023-23397 漏洞，便可通过向受害者发送恶意 Outlook 邮件或任务来窃取 NTLM 身份验证哈希。当 Outlook 客户端检索和处理这些邮件时，这些邮件会自动触发攻击，可能会在预览窗格中查看电子邮件之前导致攻击。换句话说，目标实际上不必打开电子邮件就成为攻击的受害者。

据悉，漏洞主要影响运行 Exchange 服务器和 Outlook for Windows 桌面客户端的用户，Outlook for Android、iOS、Mac 和 Outlook for Web（OWA）等均不受影响。

OcamSec 创始人兼首席执行官 Mark Stamford 表示，潜在的攻击者可以发送特制的电子邮件，使受害者与攻击者控制的外部 UNC 位置建立连接，这将使得攻击者获得受害者的 Net-NTLMv2 哈希，然后攻击者将其转发给另一个服务并作为受害者进行身份验证。

## ****漏洞存在的一系列潜在影响****

Foretrace 创始人兼首席执行官 Nick Ascoli 指出，微软并没有提及网络犯罪分子如何利用 CVE-2023-23397 漏洞，但根据研究来看，通过该漏洞，攻击者可以不断重复使用被盗的身份验证，最终成功盗取数据或安装恶意软件。![1679302595_64181fc37dea8c3c726c7.png!small?1679302595660](https://image.3001.net/images/20230320/1679302595_64181fc37dea8c3c726c7.png!small?1679302595660)

Viakoo 首席执行官 Bud Broomhead 表示，一些最容易受到商业电子邮件泄露的人可能是潜在受害者。此外， Broomhead 警告称，一旦漏洞被成功利用，会带来核心 IT 系统被破坏、分发大量恶意软件、以及业务运营和业务连续性中断等安全风险。

### CVE-2023-23397 影响巨大

值得一提的是，Broomhead 表示虽然微软可能每个时期都会出现一些安全漏洞，但 CVE-2023-23397 漏洞无疑是一个有力的“竞争者”。该漏洞几乎影响到所有类型和规模的实体组织，对员工进行培训并不能减缓漏洞带来的影响，所以这可能是一个需要付出更大努力来缓解和补救的漏洞。

Hornetsecurity 首席执行官 Daniel Hofmann 也一直在强调 CVE-2023-23397 漏洞可能带来巨大危害，毕竟该漏洞已经公开，而且概念验证的说明已有详细记录，其它威胁攻击者可能会在恶意软件活动中采用该漏洞，并针对更广泛的受众。总的来说，利用该漏洞非常简单，在 GitHub 和其它开放论坛上已经可以找到公开的概念证明。

## ****如何防范 CVE-2023-23397****

对于无法立即进行漏洞修补的用户，Hofmann 建议管理员应该使用外围防火墙、本地防火墙和 VPN 设置来阻止 TCP 445/SMB 从网络到互联网的出站流量。这一操作可以防止 NTLM 身份验证消息传输到远程文件共享，有助于解决 CVE-2023-23397 问题。

此外 组织还应将用户添加到 Active Directory 中的“受保护用户安全组”，以防止 NTLM 作为身份验证机制，与其它禁用 NTLM 的方法相比，这种方法简化了故障排除，对高价值的帐户特别有用。

**参考来源：**

> https://www.darkreading.com/application-security/microsoft-outlook-vulnerability-2023-it-bug

# 漏洞分析 # 漏洞利用

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

攻击者能够轻松利用漏洞

漏洞存在的一系列潜在影响

* CVE-2023-23397 影响巨大

如何防范 CVE-2023-23397

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