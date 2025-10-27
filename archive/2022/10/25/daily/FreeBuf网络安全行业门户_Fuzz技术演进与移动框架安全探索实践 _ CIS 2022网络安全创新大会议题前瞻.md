---
title: Fuzz技术演进与移动框架安全探索实践 | CIS 2022网络安全创新大会议题前瞻
url: https://www.freebuf.com/articles/347743.html
source: FreeBuf网络安全行业门户
date: 2022-10-25
fetch_date: 2025-10-03T20:47:19.165202
---

# Fuzz技术演进与移动框架安全探索实践 | CIS 2022网络安全创新大会议题前瞻

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

Fuzz技术演进与移动框架安全探索实践 | CIS 2022网络安全创新大会议题前瞻

* ![]()
* 关注

Fuzz技术演进与移动框架安全探索实践 | CIS 2022网络安全创新大会议题前瞻

2022-10-24 17:51:46

所属地 上海

在漏洞挖掘技术中，Fuzzing（模糊测试）是最热门的技术之一，也是一个经久不衰的研究热点。在大量测试和实践中，Fuzzing不断发展，涌现出很多优秀的Fuzzing工具，如Peach、AFL、LibFuzzer、KLEE、SAGE等等。

Fuzzing技术结合人力、算力、底层技术和智能算法，能效率极高地进行漏洞挖掘。在技术演进的过程中，我们一直想用Fuzzing实现更多的目标，例如，如何Fuzz更多类型的软件系统、如何识别更多类型的漏洞、如何探测复杂的能躲避检测的漏洞、如何评估潜在的风险… …

为了探讨上述问题，CIS 2022网络安全创新大会邀请vivo安全攻防专家刘光明，**从漏洞挖掘从业者视角分享Fuzzing技术的演进和发展，以及移动端框架层挖掘技术的探索实践**。

2022年，CIS 2022网络安全创新大会即将迎来八岁“生日”。在这个特殊时刻，作为每年必不可少的网络安全行业盛宴，大会广邀网络安全行业领军人物、意见领袖、技术大拿、安全专家齐聚一堂，共话网络安全行业新趋势、新技术和新对策。

## ****嘉宾介绍****

刘光明：vivo安全攻防专家，10余年安全从业经验，熟悉多个平台下的漏洞挖掘、漏洞利用、APT攻击、业务攻防、安全工程、Fuzz技术、自动化安全测试等领域。微软全球白帽子Top100 成员，曾发现多个系统内核0day漏洞并多次在HITB POC等国际安全会议上发表主题演讲。

![](https://image.3001.net/images/20221025/1666681920_63578c40cb8b0327681b2.jpg!small)

## 关于CIS 2022

CIS 2022网络安全创新大会由国内领先的网络安全行业门户FreeBuf主办，本次大会首次采用三城联动形式，以上海为主会场，北京、深圳为分会场，聚合CIS官网、移动端两大平台，共同构建网络安全世界多维时空，给参会嘉宾和线上观众带来一场别开生面的网络安全知识狂欢。更多精彩内容，请点击CIS 2022网络安全创新大会[官网](https://cis.freebuf.com/)查看。

## 关于WitAwards 2022

第八届WitAwards 2022中国网络安全行业年度评选由网络安全行业门户FreeBuf主办，自 2015 年举办以来一直饱受赞誉，是业内广受关注的网络安全创新大奖评选。WitAwards 2022评选旨在以最专业的角度和最公正的态度，发掘优秀行业案例，树立年度标杆。颁奖盛典在「CIS2022网络安全创新大会」上海主会场隆重举行，敬请关注。

# CIS网络安全创新大会

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

嘉宾介绍

关于CIS 2022

关于WitAwards 2022

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