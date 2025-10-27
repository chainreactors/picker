---
title: 赶快更新！Apple 出现多个安全漏洞
url: https://www.freebuf.com/news/357600.html
source: FreeBuf网络安全行业门户
date: 2023-02-16
fetch_date: 2025-10-04T06:46:34.738324
---

# 赶快更新！Apple 出现多个安全漏洞

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

赶快更新！Apple 出现多个安全漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

赶快更新！Apple 出现多个安全漏洞

2023-02-15 13:40:20

所属地 海外

The Hacker News 网站披露，苹果公司近日推出了 iOS、iPadOS、macOS 的安全更新，以期解决一个 0day 漏洞（追踪为 CVE-2023-23529）。

研究表明，CVE-2023-23529 漏洞与 WebKit 开源浏览器引擎中的类型混淆错误有关，一旦攻击者成功利用，便可在目标系统上执行任意代码。![1676439634_63ec705239d7d26b25e1c.png!small?1676439635335](https://image.3001.net/images/20230215/1676439634_63ec705239d7d26b25e1c.png!small?1676439635335)

WebKit 是一个主要用于 Safari，Dashboard，Mail 和其它一些 Mac OS X 程序的开源浏览器引擎，在手机上的应用十分广泛（例如 Android、iPhone 等）。此外，WebKit 还应用在 Mac OS X 平台默认的 Safari 桌面浏览器内。

## ****国内某安全厂商监测到多个**** ****Apple**** ****漏洞****

除了上述提到的 CVE-2023-23529 安全漏洞，近段时间，国内某安全厂商还监测了多个 Apple 官方发布的安全漏洞通知，主要包括：

> Apple Kernel 权限提升漏洞(CVE-2023-23514)
>
> Apple macOS Ventura 敏感信息泄露漏洞(CVE-2023-23522)

相较于其它两个漏洞，CVE-2023-23529 影响范围及危害程度最严重，该漏洞允许未经身份认证的远程攻击者诱骗受害者访问其特制的恶意网站，使 WebKit 处理网页内容时触发类型混淆错误，最终在目标系统上实现任意代码执行。

****影响苹果多个版本产品：****

> iPhone 8 及更高版本
>
> iPad Pro（所有型号）
>
> iPad Air 第三代及更高版本
>
> iPad 第五代及更新版本
>
> iPad mini 第五代和更高版本
>
> 运行 macOS Ventura 的 Mac

此外，攻击者可组合利用 CVE-2023-23529 和 CVE-2023-23514 漏洞提升权限并逃逸 Safari 沙箱。值得注意的是，安全研究人员已经发现 Apple WebKit 任意代码执行漏洞 CVE-2023-23529 在野利用的迹象，鉴于这些漏洞影响范围较大，建议客户尽快做好自查及防护。

## ****苹果已发布了安全更新****

2 月14 日，苹果官方正式发布了 iOS 16.3.1 安全更新， 修复了 CVE-2023-23529 高危漏洞，建议用户尽快升级。![1676439673_63ec70799031ffdd4fcac.png!small?1676439673768](https://image.3001.net/images/20230215/1676439673_63ec70799031ffdd4fcac.png!small?1676439673768)

官方更新日志显示，此次安全更新修复了存在于 WebKit 中的漏洞

WebKit 安全漏洞问题存在已久，2022 年，苹果总共修复了 10 个 0day，4 个漏洞是在 WebKit 中发现的。

**参考文章：**

> https://thehackernews.com/2023/02/patch-now-apples-ios-ipados-macos-and.html
>
> https://securityaffairs.com/142200/hacking/apple-zero-day-iphones-macs.html
>
> https://www.sohu.com/a/640613206\_120914897
> https://www.secrss.com/articles/51867

# 漏洞利用 # 安全更新

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

国内某安全厂商监测到多个 Apple 漏洞

苹果已发布了安全更新

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