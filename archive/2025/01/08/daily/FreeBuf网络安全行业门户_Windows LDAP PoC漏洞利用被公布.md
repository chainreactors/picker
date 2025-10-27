---
title: Windows LDAP PoC漏洞利用被公布
url: https://www.freebuf.com/news/419188.html
source: FreeBuf网络安全行业门户
date: 2025-01-08
fetch_date: 2025-10-06T20:10:10.606524
---

# Windows LDAP PoC漏洞利用被公布

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

Windows LDAP PoC漏洞利用被公布

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Windows LDAP PoC漏洞利用被公布

2025-01-07 11:12:23

所属地 上海

近日，网上发布了一个针对Windows轻量级目录访问协议（LDAP）安全漏洞的概念验证（PoC）漏洞利用程序，可能会引发拒绝服务（DoS）状况。目前该漏洞现已修复，建议企业/组织立即修复，以免被攻击者利用。

![](https://image.3001.net/images/20250107/1736219535_677c9b8f1e7c777651070.png!small)

该漏洞为越界读取漏洞，编号CVE - 2024 - 49113，CVSS评分：7.5。微软于2024年12月的补丁日更新中进行修复，与此同时同时还修复了CVE - 2024 - 49112漏洞（CVSS评分：9.8），这是在同一组件中的严重整数溢出漏洞，可能导致远程代码执行。

由SafeBreach Labs设计的CVE - 2024 - 49113 PoC，名为LDAPNightmare，其目的是让任何未打补丁的Windows Server崩溃，并且“除了受害者域控制器的DNS服务器有互联网连接外，没有其他前提条件”。

具体而言，它通过向受害者服务器发送DCE/RPC请求，最终致使本地安全机构子系统服务（LSASS）崩溃，并且在发送带有“lm\_referral”非零值的特制CLDAP转介响应数据包时强制重启。微软关于CVE - 2024 - 49113的公告在技术细节方面比较简略，不过微软透露，CVE - 2024 - 49112可通过从未受信任的网络发送RPC请求来利用，从而在LDAP服务的环境下执行任意代码。

## **具体流程**

**针对未打补丁的Windows Server**

攻击者利用LDAPNightmare漏洞的PoC（概念验证），针对未打补丁的Windows Server发起攻击。

首先会向目标服务器发送精心构造的DCE/RPC请求。DCE/RPC是一种远程过程调用协议，在Windows系统中广泛用于不同进程间或者不同机器间的通信。当服务器接收到这个恶意构造的请求后，在处理过程中会因为上述漏洞的存在而出现异常情况。

**导致LSASS崩溃与重启**

具体来说，这种异常情况会导致本地安全机构子系统服务（LSASS）崩溃。LSASS在Windows系统中负责管理用户认证、安全策略等重要功能。

在发送带有“lm\_referral”非零值的特制CLDAP转介响应数据包时，会强制服务器重启。这是因为这个特制的数据包利用了漏洞，使得服务器在处理该数据包时无法按照正常的逻辑进行操作，进而导致系统崩溃并重启。

### **远程代码执行的扩展利用**

**漏洞链的利用**

通过修改CLDAP数据包，攻击者可以利用相同的漏洞利用链来实现远程代码执行（CVE - 2024 - 49112）。攻击者可以构造特定的CLDAP数据包内容，使得在处理这些数据包的过程中，能够触发一系列的操作，最终达到执行任意代码的目的。

**不同利用场景下的条件**

在将域控制器作为LDAP服务器使用时，攻击者需要向目标发送特制的RPC调用，触发对攻击者域名的查找才能成功执行代码。

在针对LDAP客户端应用程序时，攻击者要说服或诱骗受害者执行对攻击者域名的域控制器查找，或者连接到恶意的LDAP服务器。不过要注意，未经身份验证的RPC调用不会成功。同时，攻击者还可以利用与域控制器的RPC连接来触发对攻击者域名的域控制器查找操作，从而为自己的恶意目的创造条件。

微软指出，攻击者能够利用与域控制器的RPC连接来触发对攻击者域名的域控制器查找操作。建议“实施检测措施以监控可疑的CLDAP转介响应（设置了特定的恶意值）、可疑的DsrGetDcNameEx2调用以及可疑的DNS SRV查询。”

参考来源：<https://thehackernews.com/2025/01/ldapnightmare-poc-exploit-crashes-lsass.html>

# 漏洞 # 安全漏洞

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

具体流程

* 远程代码执行的扩展利用

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