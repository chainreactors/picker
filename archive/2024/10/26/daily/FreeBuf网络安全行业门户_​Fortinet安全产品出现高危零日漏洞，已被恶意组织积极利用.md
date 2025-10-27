---
title: ​Fortinet安全产品出现高危零日漏洞，已被恶意组织积极利用
url: https://www.freebuf.com/news/413691.html
source: FreeBuf网络安全行业门户
date: 2024-10-26
fetch_date: 2025-10-06T18:52:52.679087
---

# ​Fortinet安全产品出现高危零日漏洞，已被恶意组织积极利用

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

​Fortinet安全产品出现高危零日漏洞，已被恶意组织积极利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

​Fortinet安全产品出现高危零日漏洞，已被恶意组织积极利用

2024-10-25 11:22:24

所属地 上海

网络安全公司 Fortinet 日前披露了自家软件产品 FortiManager 存在的一个关键零日漏洞，能够允许未经身份验证的远程攻击者通过特制请求执行任意代码或命令。目前该漏洞已在野外被积极利用。

![](https://image.3001.net/images/20241025/1729826820_671b1004a377f92bf7509.png!small)

根据 Fortinet 10月23日发布的报告，该漏洞被追踪为CVE-2024-47575，CVSS v3 评分高达9.8，对多个版本的 FortiManager 以及 FortiManager Cloud 都有影响。该公司已经发布了一个补丁，并列出了用户可以采用的几种解决方法。

报告表明，该漏洞已被利用以自动从 FortiManager 中泄露敏感文件，包括 IP 地址、凭证和托管设备配置，但目前尚未收到在受感染的 FortiManager 系统上安装任何恶意软件或后门的低级系统报告。

参与此漏洞调查的Mandiant表示，一个新的威胁组织UNC5820早在 2024 年 6 月 27 日就利用了 FortiManager 漏洞，泄露并暂存了FortiManager 管理的 FortiGate 设备配置数据，其中包含受托管设备的详细配置信息以及用户的 FortiOS256 加密密码，这些数据可能被 UNC5820 用来进一步破坏 FortiManager，并在企业环境中横向移动。

目前Mandiant无法确定利用漏洞的攻击者身份及其最终目的，因此提醒任何 FortiManager 暴露在互联网上的组织都应立即进行取证调查。

## **受影响的版本和缓解措施**

该漏洞影响 FortiManager 和 FortiManager Cloud 的多个版本：

* **FortiManager**：版本 7.6.0、7.4.0 到 7.4.4、7.2.0 到 7.2.7、7.0.0 到 7.0.12 以及 6.4.0 到 6.4.14。
* **FortiManager Cloud**：版本 7.4.1 到 7.4.4、7.2（所有版本）和 7.0（所有版本）。

Fortinet 已经发布了这些版本的补丁，并敦促用户立即升级到安全版本。此外，某些版本还提供了解决方法，包括阻止未知设备注册和使用自定义证书进行身份验证。

Fortinet 建议立即采取措施保护受影响的系统：

1. **升级**：安装 FortiManager 的最新补丁，如果使用 FortiManager Cloud，请迁移到固定版本。
2. **查看配置**：通过将配置与 IoC 检测之前获取的备份进行比较，确保配置未被篡改。
3. **更改凭证**：更新所有托管设备的密码和用户敏感数据。
4. **隔离受感染的系统**：将受感染的 FortiManager 系统与互联网隔离，并将其配置为离线模式，以便与新设置进行比较。

参考来源：

> [Fortinet FortiManager RCE zero-day Flaw Exploited in-the-wild](https://cybersecuritynews.com/fortimanager-zero-day-vulnerability/#google_vignette)

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

受影响的版本和缓解措施

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