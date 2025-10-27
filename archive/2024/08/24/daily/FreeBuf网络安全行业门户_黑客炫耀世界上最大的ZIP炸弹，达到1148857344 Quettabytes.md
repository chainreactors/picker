---
title: 黑客炫耀世界上最大的ZIP炸弹，达到1148857344 Quettabytes
url: https://www.freebuf.com/news/409266.html
source: FreeBuf网络安全行业门户
date: 2024-08-24
fetch_date: 2025-10-06T18:05:00.535922
---

# 黑客炫耀世界上最大的ZIP炸弹，达到1148857344 Quettabytes

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

黑客炫耀世界上最大的ZIP炸弹，达到1148857344 Quettabytes

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客炫耀世界上最大的ZIP炸弹，达到1148857344 Quettabytes

2024-08-23 13:27:26

所属地 上海

近日，有黑客在互联网上炫耀自己搞了一个世界上最大的ZIP炸弹，达到1148857344 Quettabytes，而1 Quettabytes = 1,000,000,000,000,000,000,000,000,000,000 bytes，后面有整整30个零。

![](https://image.3001.net/images/20240823/1724401488_66c84750633f4fcd54d5b.png!small)

在此之前，被认为是最大的ZIP炸弹记录保持者是55.4亿bytes，远远小于1148857344 Quettabytes。无法想象，这样一个ZIP炸弹会对系统造成多么严重的伤害。难怪黑客在平台上炫耀自己手里这个超级炸弹，只等引爆。

ZIP炸弹攻击是一种恶意软件攻击，它通过创建一个看似无害的小型压缩文件，但实际上包含大量重复的数据或嵌套的压缩文件，目的是在解压时消耗大量的系统资源，如CPU、内存和磁盘空间，最终可能导致系统崩溃或拒绝服务攻击。

## **ZIP炸弹攻击的原理**

ZIP炸弹攻击通常通过递归嵌套的ZIP文件系统来实现。例如，42.zip文件初始大小为42KB，但解压后包含16个压缩包，每个压缩包又包含16个更小的压缩包，如此循环5次，最终解压成1048576个4.3GB的文件，总体积达到4.5PB。

递归嵌套使得ZIP文件在解压过程中会不断增长，导致资源耗尽。这种设计使得即使是小型文件，也能在解压后变得巨大，难以处理和存储。

ZIP炸弹攻击还利用了重复数据压缩的特性。例如，通过将相同的字符或数据多次压缩，可以显著减少压缩后的文件大小。这种技术使得攻击者可以在不增加实际数据量的情况下，生成一个巨大的压缩文件。

重复数据压缩使得压缩文件在视觉上看起来很小，但实际上解压后会产生巨大的数据量。这种特性使得ZIP炸弹攻击在传输和存储时具有隐蔽性，难以被检测和防御。

ZIP炸弹攻击会导致系统资源耗尽，如CPU、内存和磁盘空间。正如上文所提到的42.zip文件，解压后需要大量的内存来存储解压后的文件，从而导致系统崩溃。系统资源耗尽不仅会影响系统的正常运行，还可能导致其他应用程序无法运行。这种攻击对于未进行压缩文件解压后大小校验的系统尤其危险。

另外，ZIP炸弹攻击可以导致拒绝服务攻击，通过消耗大量的系统资源，使目标系统无法处理正常的请求。拒绝服务攻击不仅影响单个用户的体验，还可能对整个网络服务造成影响。这种攻击常常用于破坏网络安全，使得正常用户无法访问服务。

## **防御Tips**

### 1、限制上传文件的大小

设置最大文件大小是防止ZIP炸弹攻击的一种简单有效的方法。例如，在Java上传接口中，可以通过配置`multipart.max-file-size`和`multipart.max-request-size`属性来限制上传文件的大小。

限制文件大小可以防止大文件被上传并解压，从而减少资源消耗和潜在的系统崩溃风险。然而，这种方法并不能完全防止所有ZIP炸弹攻击，因为攻击者可能会通过其他方式绕过这些限制。

### 2、使用ZipInputStream检查Zip文件

通过使用Java标准库中的ZipInputStream类来检查Zip文件中的每个条目的大小，可以识别潜在的ZIP炸弹。例如，可以设置一个缓冲区大小，并检查每个条目的大小是否超过该缓冲区大小。

这种方法可以在文件解压前对其进行初步检查，从而避免资源耗尽。但这种方法需要一定的计算资源，并且可能无法检测到所有复杂的ZIP炸弹攻击。

### 3、使用Apache Commons Compress库

Apache Commons Compress库提供了更安全的Zip文件处理功能，可以帮助防止ZIP炸弹攻击。例如，可以使用该库的`ZipArchiveEntry`和`ZipFile`类来检查Zip文件是否包含Zip炸弹。

使用专门的库进行Zip文件处理可以提供更强大的安全性，但需要一定的学习和配置成本。对于大多数应用来说，使用Java标准库已经足够应对ZIP炸弹攻击。

# ZIP # ZIP文件

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

ZIP炸弹攻击的原理

防御Tips

* 1、限制上传文件的大小
* 2、使用ZipInputStream检查Zip文件
* 3、使用Apache Commons Compress库

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