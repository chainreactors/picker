---
title: CocoaPods 曝关键漏洞，数百万 macOS 和 iOS 应用程序面临供应链攻击风险
url: https://www.freebuf.com/news/405257.html
source: FreeBuf网络安全行业门户
date: 2024-07-06
fetch_date: 2025-10-06T17:43:32.205640
---

# CocoaPods 曝关键漏洞，数百万 macOS 和 iOS 应用程序面临供应链攻击风险

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

CocoaPods 曝关键漏洞，数百万 macOS 和 iOS 应用程序面临供应链攻击风险

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

CocoaPods 曝关键漏洞，数百万 macOS 和 iOS 应用程序面临供应链攻击风险

2024-07-05 11:09:20

所属地 上海

最近，Objective-C 和 Swift 的著名依赖管理器 CocoaPods 的关键漏洞被曝光，使数百万 macOS 和 iOS 设备上的应用程序面临供应链攻击风险，可能会对一些苹果用户造成伤害。

![](https://image.3001.net/images/20240705/1720148547_66876243d63cba4d75056.jpg!small)问题出现在 CocoaPods 迁移到 Trunk 服务器时，导致数千个软件包无人认领，攻击者可以利用公共 API 获取 pod 和 CocoaPods 源代码中的电子邮件地址。（CocoaPods 被广泛用于管理 macOS 和 iOS 开发中的第三方库，可以自动化集成和解析，是一个广受欢迎的省时工具，因此被利用的风险很大。）

然而，这些无人认领的软件包被暴露了近十年，直到 2023 年 10 月才被修补。

Trunk 服务器作为 CocoaPods 基础设施的重要组成部分，负责管理 CocoaPods 库文件的分发和托管，对于库的版本控制、用户验证和发布流程至关重要。相关的安全问题可能会损害 CocoaPods 库的完整性，使攻击者能够向流行的数据包中注入有害代码。

**发现的关键漏洞包括：**

* CVE-2024-38366 (CVSS 10.0)，该漏洞影响电子邮件验证工作流程，可在 Trunk 服务器上执行任意代码。因此，合法软件包可能会被篡改或替换，给用户带来重大风险。
* CVE-2024-38368 (CVSS 9.3) ，该漏洞利用了 "认领 Pods "功能，攻击者可以控制无人认领的软件包。这反过来又可以篡改源代码，对流行的应用程序进行未经批准的修改。
* CVE-2024-38367 (CVSS 8.2)，该漏洞也涉及电子邮件验证，其中潜在的良性链接允许攻击者将用户重定向到恶意域，从而导致账户面临被接管或令牌被盗的风险。

由于许多流行应用程序都依赖于 CocoaPods，此类漏洞威胁到整个 iOS 和 macOS 生态系统。利用这些漏洞的攻击者可以向合法应用程序注入恶意代码，通过可信渠道分发恶意软件，并破坏用户数据。

虽然 CocoaPods 已经修补了这些漏洞，但有关这些漏洞如何被利用的细节尚未澄清。开发人员已被敦促审查安全实践并更新依赖项，以降低未来再次被利用的风险。

据了解，这并不是 CocoaPods 第一次受到审查。2023 年初，安全研究人员发现了一个允许攻击者劫持子域的漏洞。最近发现的漏洞强调了依赖管理器和软件开发中安全性的重要性，安全研究人员需要积极主动地应对可能影响用户数据和应用程序的潜在漏洞。

参考来源：

https://www.spiceworks.com/it-security/endpoint-security/news/critical-cocoapods-vulnerability-macos-ios-apps-supply-chain-attacks/

# 安全漏洞 # 恶意代码 # ios # macOS

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