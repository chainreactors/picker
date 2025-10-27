---
title: Windows 曝9.8分漏洞，已有PoC及利用情况
url: https://www.freebuf.com/news/418909.html
source: FreeBuf网络安全行业门户
date: 2025-01-03
fetch_date: 2025-10-06T20:09:28.492612
---

# Windows 曝9.8分漏洞，已有PoC及利用情况

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

Windows 曝9.8分漏洞，已有PoC及利用情况

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Windows 曝9.8分漏洞，已有PoC及利用情况

2025-01-02 11:29:58

所属地 上海

SafeBreach Labs的研究人员发布了关于Windows轻量级目录访问协议（LDAP）的一个关键漏洞的概念验证（PoC）和漏洞利用方法，该漏洞编号为CVE - 2024 - 49112。微软在2024年12月10日的补丁星期二更新中披露了此漏洞，其CVSS严重性评分高达9.8。

CVE - 2024 - 49112属于远程代码执行（RCE）漏洞，会对包括域控制器（DC）在内的Windows服务器产生影响。域控制器在组织网络里是关键组成部分，负责管理身份验证和用户权限等工作。

### 漏洞影响

> 1. 让未打补丁的服务器崩溃；
>
> 2. 在LDAP服务环境下执行任意代码；
>
> 3. 有可能破坏整个域环境。

### 漏洞利用技术细节

此漏洞是由于LDAP相关代码中的整数溢出问题引发。未经身份验证的攻击者可通过发送特制的RPC调用来触发恶意的LDAP查询，成功利用时可能导致服务器崩溃或者进一步实现远程代码执行。

![](https://image.3001.net/images/20250102/1735788552_67760808ef6ff7a48d627.jpg!small)

SafeBreach Labs开发了一个名为“LDAPNightmare”的PoC漏洞利用工具，以此展示该漏洞的严重性。该漏洞利用按以下攻击流程可使未打补丁的Windows服务器崩溃：

> 1. 攻击者向目标服务器发送DCE/RPC请求；
>
> 2. 目标服务器向攻击者的DNS服务器查询以获取信息；
>
> 3. 攻击者回应主机名和LDAP端口；
>
> 4. 目标服务器发送NBNS广播以定位攻击者的主机名；
>
> 5. 攻击者回复其IP地址；
>
> 6. 目标服务器成为LDAP客户端，并向攻击者的机器发送CLDAP请求；
>
> 7. 攻击者发送恶意引用响应，致使LSASS（本地安全机构子系统服务）崩溃并重启服务器。

![](https://image.3001.net/images/20250102/1735788591_6776082fe9686e9dc5906.jpg!small)

SafeBreach已经验证，微软的补丁通过解决整数溢出问题有效地缓解了该漏洞。所有未打补丁的Windows Server版本都会受到此漏洞影响，其中包括Windows Server 2019和2022。利用该漏洞可能让攻击者控制域环境，所以这会成为勒索软件团伙和其他威胁行为者的主要目标。

建议组织马上采取以下行动：

> 1. 立即应用微软2024年12月的补丁；
>
> 2. 在补丁安装完成之前，监控可疑的DNS SRV查询、CLDAP引用响应和DsrGetDcNameEx2调用；
>
> 3. 使用SafeBreach的PoC工具（可从GitHub获取）来测试自身环境。

参考来源：<https://cybersecuritynews.com/poc-windows-ldap-rce-vulnerability/>

# 漏洞分析

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