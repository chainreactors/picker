---
title: 赶紧自查，Citrix数千台服务器存在严重安全风险
url: https://www.freebuf.com/news/353804.html
source: FreeBuf网络安全行业门户
date: 2022-12-30
fetch_date: 2025-10-04T02:44:52.061700
---

# 赶紧自查，Citrix数千台服务器存在严重安全风险

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

赶紧自查，Citrix数千台服务器存在严重安全风险

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

赶紧自查，Citrix数千台服务器存在严重安全风险

2022-12-29 11:50:02

所属地 上海

网络安全分析师警告称，数以千计的Citrix ADC 和网关部署仍然存在安全风险，即便该品牌服务器在此之前已经修复了两个严重的安全漏洞。

第一个漏洞是CVE-2022-27510，已于 11 月 8 日修复。可影响两种 Citrix 产品的身份验证绕过。第二个漏洞是CVE-2022-27510，已于 12 月 13 日披露并修补，其允许未经身份验证的攻击者，在易受攻击的设备上执行远程命令并控制它们。![](https://image.3001.net/images/20221229/1672285331_63ad0c933863f16d778ce.jpg!small)

然而，就在Citrix公司发布安全更新对漏洞进行修复时，攻击者已经在大规模利用CVE-2022-27518漏洞了。

NCC Group公司旗下的Fox IT团队的研究人员报告说，虽然大多数面向公众的 Citrix 端点已更新为安全版本，但仍有数千个端点容易受到攻击。

## ****查找易受攻击的版本****

Fox IT 分析师于 2022 年 11 月 11 日扫描了网络，发现共有3万台 Citrix 服务器在线。为了确定有多少太服务器受到上述两个漏洞的影响，安全研究人员首先要确定它们的版本号。虽说版本号未包含在服务器的HTTP 响应中，但是却携带了类似 MD5 哈希的参数，可用于将它们与 Citrix ADC 和 Gateway 产品版本进行匹配。![](https://image.3001.net/images/20221229/1672285352_63ad0ca899c62b14a41b8.jpg!small)

index.htm 中的哈希值

因此，该团队在VM上下载并部署了他们可以从 Citrix、Google Cloud Marketplace、AWS 和 Azure 获取的所有 Citrix ADC 版本，并将哈希值与版本相匹配。![](https://image.3001.net/images/20221229/1672285367_63ad0cb73777f9c7d87dd.jpg!small)

将哈希链接到版本 (Fox It)

对于无法与来源版本匹配的哈希值，研究人员求助于确定构建日期并据此推断出它们的版本号。![](https://image.3001.net/images/20221229/1672285381_63ad0cc58e71e7b4fffb2.jpg!small)

将构建日期与哈希相关联 (Fox It)

这进一步减少了未知版本（孤立哈希）的数量，但总的来说，大多数哈希都与特定的产品版本相关联。

## ****数以千计易受攻击的 Citrix 服务器****

最终结果如下图所示，表明截至2022年12月28日，大部分服务器在13.0-88.14版本上，不受这两个安全问题的影响。![](https://image.3001.net/images/20221229/1672285791_63ad0e5fead6094a53962.jpg!small)

Citrix 服务器版本 (Fox It)

使用数量排名第二的版本是12.1-65.21，如果满足某些条件，则容易受到 CVE-2022-27518 的攻击，该版本至少有3500个端点在运行。攻击者对此进行利用的前提是，这些服务器必须要使用SAML SP 或 IdP 配置，因此，并非3500个系统都会受到CVE-2022-27518的影响。

有超过 1000 台服务器容易受到 CVE-2022-27510 的影响，大约 3000 个端点可能容易受上述两个严重安全漏洞的影响。

最后，Fox IT 团队希望其博客能够帮助提高 Citrix 管理员的意识，他们尚未针对最近的严重缺陷应用进行安全更新，这将会让很多用户处于风险之中。而统计数据也表明，要对所有设备的安全漏洞进行修复，供应商和企业仍有许多工作要做。

> 参考来源：https://www.bleepingcomputer.com/news/security/thousands-of-citrix-servers-vulnerable-to-patched-critical-flaws/

# web安全 # 系统安全 # 企业安全

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

查找易受攻击的版本

数以千计易受攻击的 Citrix 服务器

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