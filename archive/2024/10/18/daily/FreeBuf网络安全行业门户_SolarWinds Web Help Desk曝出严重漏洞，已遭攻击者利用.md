---
title: SolarWinds Web Help Desk曝出严重漏洞，已遭攻击者利用
url: https://www.freebuf.com/news/413009.html
source: FreeBuf网络安全行业门户
date: 2024-10-18
fetch_date: 2025-10-06T18:52:11.039886
---

# SolarWinds Web Help Desk曝出严重漏洞，已遭攻击者利用

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

SolarWinds Web Help Desk曝出严重漏洞，已遭攻击者利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

SolarWinds Web Help Desk曝出严重漏洞，已遭攻击者利用

2024-10-17 10:33:27

所属地 上海

![1729132082_67107632a085c4077b9d6.png!small](https://image.3001.net/images/20241017/1729132082_67107632a085c4077b9d6.png!small)

近日，CISA 在其 “已知漏洞”（KEV）目录中增加了三个漏洞，其中一个是 SolarWinds Web Help Desk (WHD) 中的关键硬编码凭据漏洞，供应商已于 2024 年 8 月底修复了该漏洞。

SolarWinds Web Help Desk 是一款 IT 服务台套件，全球有 30 万客户在使用，其中包括政府机构、大型企业和医疗机构。

SolarWinds 漏洞被追踪为 CVE-2024-28987，是由硬编码凭据（用户名为 “helpdeskIntegrationUser”，密码为 “dev-C4F8025E7”）引起的。这些凭证一旦被未经验证的远端攻击者利用可能会存取 WHD 端点，并不受限制地存取或修改资料。

Horizon3.ai 研究员 Zach Hanley 最早发现了该漏洞并随即报告给了 SolarWinds ，四天后该套件发布了热修复程序，并敦促系统管理员迁移到 WHD 12.8.3 Hotfix 2 或更高版本。

CISA 现已将该漏洞添加到 KEV 中，表明该漏洞正被用于野外攻击。

美国政府机构没有透露有关恶意活动的详细信息，并将勒索软件的利用状态设置为未知。预计美国联邦机构和政府组织将在 2024 年 11 月 5 日前更新到安全版本或停止使用该产品。

鉴于 CVE-2024-28987 正在被利用，建议系统管理员采取适当措施，在设定的最后期限之前确保 WDH 端点的安全。

另外两个漏洞与 Windows 和 Mozilla Firefox 有关，已知这两个漏洞都已在攻击中被利用。CISA 还要求联邦机构在 11 月 5 日前修补这些漏洞。

Windows 漏洞是一个内核 TOCTOU 竞赛条件，被追踪为 CVE-2024-30088，趋势科技发现该漏洞被主动利用。该网络安全公司将这一恶意活动归咎于 OilRig (APT34)，他们利用该漏洞将被入侵设备的权限提升到 SYSTEM 级别。

微软在最新发布的补丁包中解决了该漏洞，但目前还不清楚何时开始主动利用该漏洞。

Mozilla Firefox CVE-2024-9680 漏洞最早是被 ESET 研究员 Damien Schaeffer 于 2024 年 10 月 8 日发现，25 小时后该漏洞得以修复。

Mozilla 表示，ESET 提供的攻击链可以通过 Firefox 中 CSS 动画时间轴的渲染在用户设备上远程执行代码。

目前， ESET 仍在分析他们观察到的攻击活动，其中一位发言人称恶意活动似乎来自俄罗斯，很可能用于间谍活动。

> 参考来源：[SolarWinds Web Help Desk flaw is now exploited in attacks (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/solarwinds-web-help-desk-flaw-is-now-exploited-in-attacks/)

# 安全漏洞

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