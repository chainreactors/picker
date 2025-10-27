---
title: 一款新的开源工具正在大肆扫描公共AWS的“秘密”
url: https://www.freebuf.com/news/348371.html
source: FreeBuf网络安全行业门户
date: 2022-11-01
fetch_date: 2025-10-03T21:26:19.779261
---

# 一款新的开源工具正在大肆扫描公共AWS的“秘密”

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

一款新的开源工具正在大肆扫描公共AWS的“秘密”

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

一款新的开源工具正在大肆扫描公共AWS的“秘密”

2022-10-31 15:31:09

所属地 上海

一个新的开源工具"S3crets Scanner "扫描仪允许研究人员和红色团队搜索错误存储在公开曝光的或公司的亚马逊AWS S3存储桶中的 "秘密"。![](https://image.3001.net/images/20221031/1667201319_635f792740b25ad838f16.png!small)亚马逊S3（简单存储服务）是一项云存储服务，通常被公司用来将软件、服务和数据存储在被称为桶的容器中。但是公司有时不能很好的保护他们的S3桶，从而导致存储的数据公开暴露在互联网上。

这种类型的错误配置已经造成了数据泄露，威胁者获得了员工或客户的详细资料、备份和其他类型的数据。除了应用程序数据外，S3桶中的源代码或配置文件也可能包含 "秘密"，即认证密钥、访问令牌和API密钥。如果这些秘密被威胁者暴露和访问，可能会对其他服务甚至公司的企业网络进行更大的访问。

## ****扫描S3的秘密****

在一次检查世嘉最近的资产暴露的演习中，安全研究员Eilon Harel发现没有扫描意外数据泄露的工具存在，所以他决定创建自己的自动扫描器，并将其作为开源工具发布在GitHub。

为了帮助及时发现公共S3桶上暴露的秘密，Harel创建了一个名为 "S3crets Scanner "的Python工具，自动执行以下操作。

* 使用CSPM来获取公共桶的列表
* 通过API查询列出桶的内容
* 检查是否有暴露的文本文件
* 下载相关的文本文件
* 扫描内容中的秘密
* 将结果转发给SIEM

![](https://image.3001.net/images/20221031/1667201249_635f78e12ea138c878631.png!small)

扫描工具将只列出以下配置设置为 "False "的S3桶，这表示暴露可能是意外的。

* "BlockPublicAcls"
* "BlockPublicPolicy"
* "IgnorePublicAcls"
* "RestrictPublicBuckets"

在为 "秘密扫描 "步骤下载文本文件之前，任何打算公开的桶都被从列表中过滤掉。

当扫描一个桶时，脚本将使用Trufflehog3工具检查文本文件的内容，这是一个基于Go的改进版秘密扫描器，可以检查GitHub、GitLab、文件系统和S3桶上的凭证和私钥。

Trufflehog3使用Harel设计的一套自定义规则扫描S3crets下载的文件，这些规则针对个人身份信息（PII）暴露和内部访问令牌。

当定期用于扫描一个组织的资产时，研究人员认为 "S3crets扫描器 "可以帮助企业最大限度地减少因秘密暴露而导致的数据泄露或网络漏洞。

最后，该工具还可用于白帽行动，如扫描可公开访问的桶，并在攻击者发现秘密之前通知其所有人。

> 参考文章：<https://www.bleepingcomputer.com/news/security/new-open-source-tool-scans-public-aws-s3-buckets-for-secrets/>

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

扫描S3的秘密

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