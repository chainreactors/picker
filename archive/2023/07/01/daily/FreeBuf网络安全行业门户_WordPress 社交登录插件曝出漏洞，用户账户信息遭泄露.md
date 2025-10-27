---
title: WordPress 社交登录插件曝出漏洞，用户账户信息遭泄露
url: https://www.freebuf.com/news/370770.html
source: FreeBuf网络安全行业门户
date: 2023-07-01
fetch_date: 2025-10-04T11:55:25.024023
---

# WordPress 社交登录插件曝出漏洞，用户账户信息遭泄露

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

WordPress 社交登录插件曝出漏洞，用户账户信息遭泄露

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

WordPress 社交登录插件曝出漏洞，用户账户信息遭泄露

2023-06-30 10:44:45

所属地 上海

The Hacker News 网站消息，miniOrange 的 WordPress 社交登录和注册插件中出现了一个关键安全漏洞，该漏洞可能使潜在网络攻击者登录用户帐户。（原因是任何用户提供的有关电子邮件地址信息都是已知的）![1688093058_649e418299f609c858d61.png!small?1688093059439](https://image.3001.net/images/20230630/1688093058_649e418299f609c858d61.png!small?1688093059439)

据悉，漏洞被追踪为 CVE-2023-2982（CVSS 得分：9.8），身份验证绕过漏洞影响包括 7.6.4 之前在内的所有插件版本。2023 年 6 月 2 日，相关组织负责任地发布了 7.6.5 版本，CVE-2023-2982 漏洞问题已于 2023 年 6 月 14 日得到解决。

Wordfence 研究员 István Márton 表示 CVE-2023-2982 漏洞使未经身份认证的网络攻击者有可能获得对网站上任何账户的访问权，甚至包括用于管理网站的账户，但前提是攻击者知道或能够找到相关的电子邮件地址。

此外，CVE-2023-2982 安全漏洞问题的根源在于用户使用社交媒体账户登录时，用于保护信息安全的加密密钥是硬编码，因此导致了攻击者可以使用正确加密的电子邮件地址创建有效请求以识别用户的情况。 值得一提的是，存在漏洞的插件在 30000 多个网站上使用。

## ****LearnDash LMS**** ****插件********也曾出现其它安全漏洞****

发布 CVE-2023-2982 漏洞公告前，安全人员发现一个影响 LearnDash LMS 插件的严重漏洞（CVE-2023-3105，CVSS 得分：8.8），该插件是一个拥有超过 100000 个活动安装的 WordPress 插件，可以允许任何拥有现有帐户的用户重置任意用户密码，甚至包括具有管理员访问权限的用户密码。好消息是，漏洞已于 2023 年 6 月 6 日发布的 4.6.0.1 版本中完成了修补。![1688093147_649e41dbeef436f7e41bc.png!small?1688093148796](https://image.3001.net/images/20230630/1688093147_649e41dbeef436f7e41bc.png!small?1688093148796)

几周前，Patchstack 也曾详细介绍 UpdraftPlus 插件（CVE-2023-32960，CVSS分数：7.1）中的一个跨站点请求伪造（CSRF）漏洞，该漏洞可能允许未经身份验证的攻击者窃取敏感数据，并通过诱骗具有管理权限的用户访问特制的 WordPress 网站 URL ，以此来提升自身权限。

**文章来源：**

> https://thehackernews.com/2023/06/critical-security-flaw-in-social-login.html

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

文章目录

LearnDash LMS 插件也曾出现其它安全漏洞

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