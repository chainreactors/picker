---
title: APT组织开始大量抄袭红队先进的战术和工具
url: https://www.freebuf.com/news/418010.html
source: FreeBuf网络安全行业门户
date: 2024-12-19
fetch_date: 2025-10-06T19:38:22.614195
---

# APT组织开始大量抄袭红队先进的战术和工具

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

APT组织开始大量抄袭红队先进的战术和工具

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

APT组织开始大量抄袭红队先进的战术和工具

2024-12-18 14:48:13

所属地 上海

近日，安全研究人员调查后发现，臭名昭著的APT组织Earth Koshchei（也被称为APT29或Midnight Blizzard）与一项大规模非法远程桌面协议（RDP）的恶意活动相关。

![](https://image.3001.net/images/20241218/1734504570_6762707ae871dc377a8b4.jpg!small)

Earth Koshchei在此次情报收集与数据窃取行动中创新性地采用了先进的战术及红队工具，充分展现出攻击组织在尝试新型攻击的效率。通过商业VPN服务、TOR及居民代理等匿名化层来掩盖其操作，增强隐蔽性，并使归因工作复杂化。该行动于2024年10月达到峰值，目标包括政府、军事组织、智囊团、学术研究人员及乌克兰实体等。

## 攻击机制

Earth Koshchei的行动采用了多层攻击策略，其核心在于嵌入鱼叉式钓鱼邮件中的恶意RDP配置文件。当用户打开该文件时，就有可能会通过攻击者设置的193个中继之一连接到非法RDP服务器。

![](https://image.3001.net/images/20241218/1734504433_67626ff12000d1923cf50.png!small)建立PRD的方法

其攻击方法被称为“非法RDP”，Black Hills Information Security在2022年对其进行了详尽描述，该方法采用了RDP中继、非法服务器及恶意配置。

![](https://image.3001.net/images/20241218/1734504444_67626ffca2e1703bae703.png!small)

RDP连接（来源：VirusTotal）

通过类似Python远程桌面协议中间人（MITM）框架（PyRDP）的工具，攻击者拦截并操纵RDP连接，从而获得对受害者机器的部分控制权限。这允许进行数据窃取、文件浏览，甚至执行恶意应用程序，不再需要像以往一样部署传统恶意软件。

Earth Koshchei的行动规模引起行业关注。在2024年8月至10月期间，该组织注册了200多个域名，其中许多仿冒目标组织的身份，如政府、IT公司及研究机构。其准备工作包括建立34个非法后端RDP服务器，并将其作为其行动的指挥节点。

![](https://image.3001.net/images/20241218/1734504704_6762710032498d8f34857.png!small)

Earth Koshchei如何控制其基础设施的架构图

现阶段，Earth Koshchei的动机似乎主要为情报收集。该组织据称与俄罗斯外国情报局（SVR）有关联，历史上曾针对西方国家的外交、军事、能源、电信及IT部门。其最新行动与此模式相符，受害者包括外交部、军事组织及学术研究人员。

## 红队蓝图变成了攻击者的武器

安全专家强调，Earth Koshchei的非法RDP战术可能借鉴了旨在加强组织防御的红队方法，攻击者有效地将这些技术武器化。例如在一项分析中，RDP配置文件将受害者重定向至假冒的亚马逊网络服务（AWS）的恶意服务器。

他们还利用驱动器重定向及资源共享等功能，以隐蔽方式提取敏感数据。在10月的攻击浪潮中，估计有三家关键组织的数据被窃取，包括两家军事实体及一家云服务提供商。

使用TOR、商业VPN及居民代理等匿名化层使检测和归因具有挑战性。，这些战术使攻击者在利用电子邮件服务器分发钓鱼邮件的同时掩盖其活动。

尽管确定性的归因仍具复杂性，但Trend Micro及其他公司仍将此次行动归因于Earth Koshchei，其原因在于该组织独特的战术、技术及程序（TTPs）。

此次攻击还暴露出另外一个令人不安的现象：合法的安全工具、红队战术方法等被大量用于恶意攻击之中。如何改变这一趋势是行业需要重点关注的方向。

参考来源：<https://cybersecuritynews.com/hackers-leverage-red-team-tools-in-rdp-attacks/>

# 系统安全 # APT组织

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

攻击机制

红队蓝图变成了攻击者的武器

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