---
title: SAP 修复五个高危漏洞，请尽快安装更新！
url: https://www.freebuf.com/articles/360507.html
source: FreeBuf网络安全行业门户
date: 2023-03-16
fetch_date: 2025-10-04T09:44:55.386353
---

# SAP 修复五个高危漏洞，请尽快安装更新！

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

SAP 修复五个高危漏洞，请尽快安装更新！

* ![]()
* 关注

SAP 修复五个高危漏洞，请尽快安装更新！

2023-03-15 14:23:18

所属地 上海

Bleeping Computer 网站披露，软件供应商 SAP 发布了 19 个漏洞的安全更新，其中 5 个被评为高危漏洞。![1678861420_6411646c560596e6e2014.png!small?1678861421245](https://image.3001.net/images/20230315/1678861420_6411646c560596e6e2014.png!small?1678861421245)

此次修复的安全漏洞影响多款 SAP 产品，其中高危漏洞主要影响 SAP Business Objects Business Intelligence Platform（CMC）和 SAP NetWeaver。

**此次修复的五个高危漏洞如下：**

**CVE-2023-25616:** SAP Business Intelligence Platform 中存在的高危（CVSS v3:9.9）代码注入漏洞，允许攻击者访问仅对特权用户开放的资源，影响版本 420 和 430。

**CVE-2023-23857：**严重程度（CVSS v3:9.8）的信息泄露、数据操纵和 DoS 漏洞，影响 SAP NetWeaver AS for Java 7.50 。该漏洞允许未经身份验证的攻击者连接到开放接口并通过目录 API 访问服务来执行未经授权的操作。

**CVE-2023-27269：**影响 SAP  NetWeaver Application Server for ABAP 的严重性（CVSS v3:9.6）目录遍历漏洞。该漏洞允许非管理员用户覆盖系统文件，影响版本 700、701、702、731、740、750、751、752、753、754、755、756、757 和 791。

**CVE-2023-27500：**APRSBRO 中的目录遍历漏洞，允许具有非管理权限的攻击者利用该漏洞重写系统文件。在这种攻击中，无法读取任何数据，但可能会过度写入关键 OS 文件，从而导致系统不可用。

**CVE-2023-25617:** SAP Business Objects Business Intelligence Platform 版本 420 和 430 中存在严重性（CVSS v3:9.0）命令执行漏洞。该漏洞允许远程攻击者在特定条件下使用 BI Launchpad、中央管理控制台或基于公共 java SDK 的自定义应用程序在操作系统上执行任意命令。

除上述之外，SAP 还修复了其它四个高严重性漏洞以及十个中等严重性漏洞。

## SAP 漏洞影响广泛

SAP 是世界上最大的 ERP 供应商，在 180 个国家拥有 42.5 万客户，占全球市场份额的 24%。超过 90% 的《福布斯全球 2000 强》使用其 ERP、SCM、PLM 和 CRM 产品。因此，其产品中存在的安全漏洞是威胁攻击者的绝佳目标，可以作为侵入企业系统的入口。

早在 2022 年 2 月，美国网络安全和基础设施安全局（CISA）就敦促其管理员修补一组影响 SAP 业务应用程序的严重漏洞，以防止数据被盗、勒索软件攻击以及任务关键流程和操作中断。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/sap-releases-security-updates-fixing-five-critical-vulnerabilities/

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

SAP 漏洞影响广泛

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