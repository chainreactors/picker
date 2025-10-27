---
title: Fortinet 曝一严重漏洞 POC，可获得 SIEM 根访问权限
url: https://www.freebuf.com/news/402244.html
source: FreeBuf网络安全行业门户
date: 2024-05-31
fetch_date: 2025-10-06T16:51:05.198826
---

# Fortinet 曝一严重漏洞 POC，可获得 SIEM 根访问权限

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

Fortinet 曝一严重漏洞 PoC，可获得 SIEM 根访问权限

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Fortinet 曝一严重漏洞 PoC，可获得 SIEM 根访问权限

2024-05-30 11:36:48

所属地 上海

Fortinet FortiSIEM 产品的一个关键漏洞出现了一个可行的攻击（PoC），这为更广泛的攻击提供了更多机会。

![](https://image.3001.net/images/20240530/1717036669_6657e67dd384c0f9c24b9.png!small)该漏洞被追踪为 CVE-2024-23108，于今年 2 月披露并修复，同时修复的还有与其相关的另一个漏洞 CVE-2024-23109。这两个漏洞在 CVSS 评分系统中的最高严重性评分均为 10 分，都是未经身份验证的命令注入漏洞，攻击者可能利用伪造的 API 请求实现远程代码执行（RCE）。

据 Horizon3AI 的研究人员称，该漏洞被他们称为“NodeZero”，允许用户“以 root 身份在受影响的 FortiSIEM 设备上盲目执行命令”。在 PoC 中，他们使用该漏洞加载了一个用于后继活动的远程访问工具。

FortiSIEM 是 Fortinet 的安全信息和事件管理（SIEM）平台，用于支持企业网络安全运营中心。因此，如果该平台被攻破，攻击者可以以此为跳板进一步入侵企业环境。

受漏洞影响的 FortiSIEM 版本包括 7.1.0 至 7.1.1、7.0.0 至 7.0.2、6.7.0 至 6.7.8、6.6.0 至 6.6.3、6.5.0 至6.5.2 以及 6.4.0 至 6.4.2，用户应立即打上补丁，以避免受到威胁。

**参考来源：**

https://www.darkreading.com/vulnerabilities-threats/exploit-fortinet-critical-rce-bug-siem-root-access

# poc # Fortinet # 严重漏洞

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