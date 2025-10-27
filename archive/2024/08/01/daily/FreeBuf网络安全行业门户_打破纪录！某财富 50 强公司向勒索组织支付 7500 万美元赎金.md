---
title: 打破纪录！某财富 50 强公司向勒索组织支付 7500 万美元赎金
url: https://www.freebuf.com/news/407383.html
source: FreeBuf网络安全行业门户
date: 2024-08-01
fetch_date: 2025-10-06T18:04:42.919969
---

# 打破纪录！某财富 50 强公司向勒索组织支付 7500 万美元赎金

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

打破纪录！某财富 50 强公司向勒索组织支付 7500 万美元赎金

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

打破纪录！某财富 50 强公司向勒索组织支付 7500 万美元赎金

2024-07-31 10:16:30

所属地 上海

![$75 Million Ransom Paid to Dark Angels Ransomware Group](https://image.3001.net/images/20240731/1722398079_66a9b57f12856f22c3bf3.jpg!small)

Zscaler ThreatLabz 在近日发布的一份报告中提到，一家财富 50 强公司向 Dark Angels 勒索软件组织支付了破纪录的 7500 万美元赎金。

2024年初，ThreatLabz发现一名受害者向 Dark Angels支付了7500万美元，高于目前所有已知的赎金金额。加密情报公司 Chainalysis 进一步证实了这一破纪录的支付方式，并在 X 平台上发布了推文。

![1722392106_66a99e2adcceed3186d2f.png!small](https://image.3001.net/images/20240731/1722392106_66a99e2adcceed3186d2f.png!small)

图源： Chainalysis 官方账号

虽然 Zscaler 并未透露是哪家公司支付了 7500 万美元的赎金，但他们提到该公司属于财富 50 强，攻击发生在 2024 年初。

据悉，财富50 强中确有一家公司在 2024 年 2 月遭受了网络攻击，它就是制药巨头 Cencora，在榜单上排名第 10 位。但当时并未有任何勒索软件团伙声称对此次攻击负责，这说明在事件发生后受害者很可能已经支付了赎金。不过截至目前，Cencora并未回应有关赎金支付的相关说法。

## 谁是黑暗天使

Dark Angels 最早于 2022 年 5 月以全球公司为目标发起勒索攻击。与大多数人为操作的勒索软件团伙一样，Dark Angels 勒索组织的黑客会入侵企业网络并横向移动，直到最终获得管理权限。在此期间，他们还会从被入侵的服务器上窃取数据，然后在索要赎金时利用这些数据作为额外的筹码。

在获得 Windows 域控制器访问权限后，威胁者会部署勒索软件来加密网络上的所有设备。

黑客使用基于已泄露的 Babuk 勒索软件源代码的 Windows 和 VMware ESXi 加密程序发起攻击。

随着时间的推移，他们开始转而使用 Linux 加密程序，这与 Ragnar Locker 自 2021 年以来使用的加密程序如出一辙。2023 年，执法部门捣毁了 Ragnar Locker。

Dark Angels 此前曾对江森自控发动攻击，其使用了 Linux 加密器加密该公司的 VMware ESXi 服务器，他们声称窃取了 27 TB 数据，并要求江森自控支付 5100 万美元的赎金。

![dark-angels-ransom-note.jpg](https://image.3001.net/images/20240731/1722398082_66a9b5825c9fec3e22c68.jpg!small)

Dark Angels 的勒索信，来源：BleepingComputer

此外，黑客还运营着一个名为 “Dunghill Leaks ”的数据泄漏网站，专门用于敲诈受害者，还多次威胁称如果不支付赎金，就会泄漏数据。

![Dark Angel's 'Dunghill' Leaks data leak site](https://image.3001.net/images/20240731/1722398085_66a9b585c2db7486dcadc.jpg!small)

Dark Angels 的 “邓希尔 ”数据泄露网站，来源：BleepingComputer

Zscaler ThreatLabz 称，“Dark Angels ”勒索组织采用的是 “大猎杀 ”策略，即只针对少数几家高价值公司，希望获得巨额赔付，而不是同时针对多家公司，支付数量众多但金额较小的赎金。

对此，Zscaler ThreatLabz 的研究人员解释称，Dark Angels 组织采用的是一种更加具有针对性的方式，他们通常一次只攻击一家大公司，这与大多数勒索软件组织形成了鲜明对比。其他勒索组织通常是以受害者为目标，并将大部分攻击工作外包给由初始访问经纪人和渗透测试团队组成的附属网络。

据 Chainalysis 称，在过去几年中，这种“大猎杀战术”已成为众多勒索软件团伙利用的主流趋势。

> 参考来源：[Dark Angels ransomware receives record-breaking $75 million ransom](https://www.bleepingcomputer.com/news/security/dark-angels-ransomware-receives-record-breaking-75-million-ransom/)

# 赎金 # 勒索组织

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

谁是黑暗天使

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