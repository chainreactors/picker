---
title: 官方强烈建议更新，关键漏洞影响GitHub Enterprise Server 所有版本
url: https://www.freebuf.com/news/409274.html
source: FreeBuf网络安全行业门户
date: 2024-08-24
fetch_date: 2025-10-06T18:04:58.999823
---

# 官方强烈建议更新，关键漏洞影响GitHub Enterprise Server 所有版本

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

官方强烈建议更新，关键漏洞影响GitHub Enterprise Server 所有版本

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

官方强烈建议更新，关键漏洞影响GitHub Enterprise Server 所有版本

2024-08-23 14:03:28

所属地 上海

近日，GitHub Bug Bounty 计划报告了一个影响 GitHub Enterprise Server（GHES）当前所有支持版本的关键漏洞（CVE-2024-6800），该漏洞可能允许攻击者获得对该实例内容的无限制访问。目前，漏洞已经解决，强烈建议管理员尽快更新，以确保系统安全。

![](https://image.3001.net/images/20240823/1724392975_66c8260f004d27bd0759c.png!small)

## 关于 CVE-2024-6800

GitHub Enterprise Server 是一个自托管的软件开发平台，通常是为了遵守需要对代码仓库有更多控制/安全性的特定法规。

它以自包含的虚拟设备的形式出现，安装在虚拟机上。运行 Linux 操作系统并配备自定义的应用程序堆栈。

根据软件的发布说明，CVE-2024-6800 是一个 XML 签名包装漏洞，允许攻击者绕过身份验证，但只有在实例使用 SAML 单点登录（SSO）认证，并且与使用公开暴露的签名联合元数据 XML 的特定身份提供者结合。

该漏洞允许具有对 GitHub Enterprise Server 直接网络访问权限的攻击者伪造 SAML 响应，以配置和/或获得具有站点管理员权限的用户访问。

### 安全更新建议

建议在自己的基础设施上运行 GitHub Enterprise Server 实例并使用 SAML SSO 认证的组织升级到以下已修复的 GHES 版本之一：

* 3.13.3
* 3.12.8
* 3.11.14
* 3.10.16

对于仍在使用 3.10 版本的企业，建议尽快升级到更新的版本，因为 3.10 版本将于 2024 年 8 月 29 日停止服务，届时将不再提供补丁或安全修复。

参考来源：<https://www.helpnetsecurity.com/2024/08/22/cve-2024-6800/>

# github # 权限 # Github漏洞 # 系统权限

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

关于 CVE-2024-6800

* 安全更新建议

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