---
title: ServiceBridge泄露 3200万份文件，大量企业数据被曝光
url: https://www.freebuf.com/news/409656.html
source: FreeBuf网络安全行业门户
date: 2024-08-29
fetch_date: 2025-10-06T18:04:28.854875
---

# ServiceBridge泄露 3200万份文件，大量企业数据被曝光

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

ServiceBridge泄露 3200万份文件，大量企业数据被曝光

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

ServiceBridge泄露 3200万份文件，大量企业数据被曝光

2024-08-28 15:23:30

所属地 上海

据Cyber News消息，安全研究员杰里迈亚-福勒（Jeremiah Fowler）发现了一个基于云的现场服务管理平台 ServiceBridge 暴露了大规模数据，其中包含合同、工单、发票、建议书、协议、部分信用卡号，甚至还有可追溯到 2012 年的 HIPAA 同意书。

ServiceBridge为多项现场服务提供业务支持，如泳池服务、害虫防治、杂工等，是一个集 GPS 跟踪、工单、开票和付款的平台。

![](https://image.3001.net/images/20240828/1724829849_66ced0997d256f415031a.png!small)暴露的数据库信息

根据此次发现，暴露的数据库包含 31524107 个文件，总大小为 2.68TB，文档按年月以及 PDF 和 HTM 格式分类存放在文件夹中，其中涵盖美国、加拿大、英国和许多欧洲国家不同行业的公司，其历史可以追溯到 2012 年。

除了暴露了大量合同信息，一些文件也包括个人和组织信息，例如房东、学校、宗教机构、知名连锁餐厅、医疗服务提供者等。一些文件甚至包括可能对财产或个人构成潜在物理安全风险的大门密码或其他访问信息。

![](https://image.3001.net/images/20240828/1724829956_66ced1047667899a37410.png!small)此截图为一个工作订单，其中列出了部分付款信息、所欠账户余额和客户的 PII

研究人员向ServiceBridge发送了一份披露通知后，暴露的数据库已经不可见，但目前尚不清楚该数据库被暴露了多长时间，以及是否被任何潜在的黑客访问。

研究人员警告称，暴露信息可能会被网络犯罪分子利用来进行鱼叉式网络钓鱼活动或其他欺诈活动。2022 年，由于发票和付款欺诈，美国企业平均每年损失了30万美元。

**参考来源：**

> [Large number of businesses exposed in 32 million document leak from ServiceBridge](https://cybernews.com/security/large-number-of-businesses-exposed-servicebridge/)

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