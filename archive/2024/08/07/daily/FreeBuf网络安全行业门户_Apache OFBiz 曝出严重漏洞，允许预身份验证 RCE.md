---
title: Apache OFBiz 曝出严重漏洞，允许预身份验证 RCE
url: https://www.freebuf.com/news/407869.html
source: FreeBuf网络安全行业门户
date: 2024-08-07
fetch_date: 2025-10-06T18:03:50.911922
---

# Apache OFBiz 曝出严重漏洞，允许预身份验证 RCE

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

Apache OFBiz 曝出严重漏洞，允许预身份验证 RCE

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Apache OFBiz 曝出严重漏洞，允许预身份验证 RCE

2024-08-06 10:13:49

所属地 上海

![1722911046_66b1894675fb4c3799106.png!small](https://image.3001.net/images/20240806/1722911046_66b1894675fb4c3799106.png!small)

近日，研究人员发现 Apache OFBiz 中存在一个新的关键漏洞，该漏洞是 Apache OFBiz 中的一个错误授权问题，被追踪为CVE-2024-38856。该漏洞影响 18.12.14 之前的版本，18.12.15 版本解决了该漏洞。

SonicWall 的安全研究员 Hasib Vhora 与其他安全专家在公告中写道：如果满足某些先决条件，如屏幕定义没有明确检查用户的权限，因为它们依赖于终端的配置，那么未经验证的终端可能允许执行屏幕的屏幕渲染代码。

SonicWall Capture Labs 威胁研究团队在 Apache OFBiz 中发现了一个验证前远程代码执行漏洞，该漏洞被追踪为 CVE-2024-38856，CVSS 得分为 9.8。这是 SonicWall 最近几个月在 Apache OFBiz 中发现的第二个重大漏洞，第一个是在 2023 年 12 月。Vhora 写道：这一次，覆盖视图功能中的一个漏洞将关键端点暴露给了使用伪造请求的未经验证的威胁行为者，为远程代码执行铺平了道路。该漏洞影响 Apache OFBiz 18.12.14 及以下版本，强烈建议用户立即升级到 18.12.15 或更新版本。

该问题源于身份验证机制中的一个漏洞，它允许未经身份验证的用户访问通常仅限已登录用户使用的功能，从而可能导致远程代码执行。
Apache OFBiz 是一个开源 ERP 系统，可帮助企业自动化和集成会计、人力资源、客户关系管理、订单管理、制造和电子商务等各种流程。全球有数百家公司使用该系统，其中美国占 41%，印度占 19%，德国占 7%，法国占 6%，英国占 5%，著名用户包括美国联合航空公司、Atlassian JIRA、家得宝和惠普。

SonicWall尚未发现利用该漏洞的攻击，但已开发了IPS签名IPS:4455，以检测对该问题的任何主动利用。

今年 5 月，研究人员披露了 Apache OFBiz 中的另一个漏洞，即路径遍历问题（CVE-2024-32113）。利用这第二个漏洞可导致远程命令执行。

SANS 的研究人员最近发现，针对 CVE-2024-32113 的攻击激增。

![1722910413_66b186cd7fe2f7909132e.png!small](https://image.3001.net/images/20240806/1722910413_66b186cd7fe2f7909132e.png!small)

在今年 5 月份漏洞信息正式公布后，我们一直在等待一些利用 OFBiz 漏洞的扫描的实例出现。虽然易受攻击和暴露的人群很少，但这段时间一直有攻击者频繁进行了攻击尝试。

威胁情报公司 GreyNoise 的研究人员也观察到了利用第二个漏洞的尝试。
去年12 月，SonicWall 专家就曾警告称，有一个身份验证绕过零日漏洞被追踪为 CVE-2023-51467，影响 Apache OfBiz。

攻击者可以触发该漏洞绕过身份验证，实现简单的服务器端请求伪造（SSRF）。今年 1 月，网络安全公司 VulnCheck 的研究人员针对该漏洞创建了一个概念验证（PoC）利用代码。

> 参考来源：[Researchers warn of a new critical Apache OFBiz flaw (securityaffairs.com)](https://securityaffairs.com/166612/hacking/critical-apache-ofbiz-flaw.html)

# 安全漏洞 # apache漏洞 # 漏洞利用

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