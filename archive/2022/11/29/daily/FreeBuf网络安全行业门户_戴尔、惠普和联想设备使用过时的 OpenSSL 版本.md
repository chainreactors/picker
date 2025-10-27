---
title: 戴尔、惠普和联想设备使用过时的 OpenSSL 版本
url: https://www.freebuf.com/news/350909.html
source: FreeBuf网络安全行业门户
date: 2022-11-29
fetch_date: 2025-10-03T23:59:22.711574
---

# 戴尔、惠普和联想设备使用过时的 OpenSSL 版本

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

戴尔、惠普和联想设备使用过时的 OpenSSL 版本

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

戴尔、惠普和联想设备使用过时的 OpenSSL 版本

2022-11-28 11:54:32

所属地 上海

Binarly 研究人员发现，戴尔、惠普和联想的设备仍在使用过时版本的 OpenSSL 加密库。

OpenSSL软件库允许通过计算机网络进行安全通信，能够有效防止窃听。OpenSSL包含开源的安全套接字协议（SSL）和传输层安全（TLS）协议，研究人员通过分析上述制造商使用的设备的固件图像时发现了问题所在。

专家们分析了作为任何UEFI固件所必要的核心框架之一EDKII，该框架在CryptoPkg组件中的OpenSSL库（OpensslLib）上有自己的子模块和包装器。EDK II 是一个现代化、功能丰富的跨平台固件开发环境，适用于 UEFI 和 UEFI 平台初始化 (PI) 规范。EDKII的主要存储库托管在Github上，并经常更新。但专家们在分析这些厂商的设备时，发现在其固件镜像中使用过时版本的OpenSSL：0.9.8zb、1.0.0a 和 1.0.2j，其中最新的 OpenSSL 版本早在2018 年就已发布。专家们甚至还在部分设备中发现了 更早的、来自2009 年发布的 0.9.8l 版本。

![](https://image.3001.net/images/20221128/1669613470_6384479e599607a9e8a09.png!small)戴尔、惠普和联想部分设备中的 OpenSSL版本

![](https://image.3001.net/images/20221128/1669613556_638447f49b8c8421ba9ef.png!small)Binarly Platform 在野外检测到的戴尔、惠普和联想设备中 不同OpenSSL 版本占比

Binarly 发布的报告表示，许多与安全相关的固件模块包含明显过时的 OpenSSL 版本。其中一些像 InfineonTpmUpdateDxe 包含的代码早在8年前就已成为易受攻击的“不安全代码”。

专家指出，同一个设备固件代码往往依赖不同版本的OpenSSL。 选择这种设计的原因是第三方代码的供应链依赖于其自己的代码库，而设备固件开发人员通常无法使用这些代码库，这通常会增加供应链的复杂性，带来潜在的安全风险。

> 参考来源：<https://securityaffairs.co/wordpress/138986/security/dell-hp-lenovo-openssl-outdated.html>

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