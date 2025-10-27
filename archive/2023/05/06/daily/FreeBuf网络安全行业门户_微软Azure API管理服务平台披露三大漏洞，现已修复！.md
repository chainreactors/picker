---
title: 微软Azure API管理服务平台披露三大漏洞，现已修复！
url: https://www.freebuf.com/news/365572.html
source: FreeBuf网络安全行业门户
date: 2023-05-06
fetch_date: 2025-10-04T11:40:41.519907
---

# 微软Azure API管理服务平台披露三大漏洞，现已修复！

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

微软Azure API管理服务平台披露三大漏洞，现已修复！

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

微软Azure API管理服务平台披露三大漏洞，现已修复！

2023-05-05 14:52:09

所属地 上海

![1683255234_64546fc2e7997d51dfa9d.png!small](https://image.3001.net/images/20230505/1683255234_64546fc2e7997d51dfa9d.png!small)

近日，微软Azure API管理服务平台披露了三个新的安全漏洞，恶意行为者可以通过这些漏洞直接访问敏感信息或后端服务。

据以色列云安全公司Ermetic表示，共包括两个服务器端请求伪造(SSRF)漏洞和API Management开发人员门户网站中一个不受限制的文件上传功能。

安全研究员Liv Matan在一份报告中提到：攻击者可通过SSRF漏洞从服务的CORS代理和托管代理发送请求，并绕过web应用防火墙直接访问Azure内部资料。

通过文件上传路径遍历，攻击者可以将恶意文件上传到Azure的平台内部部署工作负载。Azure API Management是一个多云管理平台，允许组织向外部和内部客户安全地公开他们的API，并实现广泛的连接体验。

在Ermetic发现的两个SSRF漏洞中，其中一个是为解决今年Orca报告的一个类似漏洞而设置的修复程序，另一个漏洞则存在于API Management代理功能中。SSRF漏洞一旦被利用，很可能导致机密性和完整性丧失，并可能直接允许威胁行为者读取Azure的内部资源并执行未经授权的代码。

![1683269416_6454a7280514bc7e0274d.png!small](https://image.3001.net/images/20230505/1683269416_6454a7280514bc7e0274d.png!small)

另一方面，在开发人员门户中发现的路径遍历缺陷主要是未对上传文件的文件类型和路径进行验证。经过身份验证的用户可以利用这个漏洞将恶意文件上传到开发人员门户服务器，甚至可能在底层系统上执行任意代码。

不过据最新消息，微软现已修补了这三个漏洞。

几周前，Orca的研究人员曾详细介绍过微软Azure的一个“设计缺陷”，称攻击者可以利用该漏洞访问存储帐户，甚至可执行远程代码。

更早前，微软还发现了另一个名为EmojiDeploy的Azure漏洞，攻击者可通过该漏洞直接控制目标应用程序。

参考链接：https://thehackernews.com/2023/05/researchers-discover-3-vulnerabilities.html

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