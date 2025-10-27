---
title: 新的云威胁！黑客利用云技术窃取数据和源代码
url: https://www.freebuf.com/news/358975.html
source: FreeBuf网络安全行业门户
date: 2023-03-02
fetch_date: 2025-10-04T08:26:54.024980
---

# 新的云威胁！黑客利用云技术窃取数据和源代码

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

新的云威胁！黑客利用云技术窃取数据和源代码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新的云威胁！黑客利用云技术窃取数据和源代码

2023-03-01 14:16:53

所属地 上海

![](https://image.3001.net/images/20230301/1677639824_63fec0906a475ab59259a.png!small)

一个被称为 "SCARLETEEL "的高级黑客行动针对面向公众的网络应用，其主要手段是渗透到云服务中以窃取敏感数据。

SCARLETEEL是由网络安全情报公司Sysdig在应对客户的云环境事件时发现的。

虽然攻击者在受感染的云环境中部署了加密器，但黑客在AWS云机制方面表现出更专业的技术，进一步钻入该公司的云基础设施。

Sysdig认为，加密劫持攻击仅仅是一个诱饵，而攻击者的目的是窃取专利软件。

## SCARLETEEL攻击

SCARLETEEL攻击开始时，黑客利用了托管在亚马逊网络服务（AWS）上的Kubernetes集群中面向公众的服务。

一旦攻击者访问容器，他们就会下载一个XMRig coinminer（被认为是诱饵）和一个脚本，从Kubernetes pod中提取账户凭证。

然后，被盗的凭证被用来执行AWS API调用，通过窃取进一步的凭证或在公司的云环境中创建后门来获得持久性。然后这些账户被用来在云环境中进一步传播。

根据AWS集群的角色配置，攻击者还可能获得Lambda信息，如功能、配置和访问密钥。

![](https://image.3001.net/images/20230301/1677639963_63fec11b12e643288ac8f.png!small)

攻击者执行的命令

接下来，攻击者使用Lambda函数枚举和检索所有专有代码和软件，以及执行密钥和Lambda函数环境变量，以找到IAM用户凭证，并利用它们进行后续枚举和特权升级。

S3桶的枚举也发生在这一阶段，存储在云桶中的文件很可能包含对攻击者有价值的数据，如账户凭证。

Sysdig的报告中说："在这次特定的攻击中，攻击者能够检索和阅读超过1TB的信息，包括客户脚本、故障排除工具和日志文件。这1TB的数据还包括与Terraform有关的日志文件，Terraform在账户中被用来部署部分基础设施。这些Terraform文件将在后面的步骤中发挥重要作用，也就是攻击者可能转到另一个AWS账户"。

![](https://image.3001.net/images/20230301/1677640022_63fec156dc000cf6ef5de.png!small)

SCARLETEEL攻击链

为了尽量减少留下的痕迹，攻击者试图禁用被攻击的AWS账户中的CloudTrail日志，这对Sysdig的调查产生了不小的困难。

然而，很明显，攻击者从S3桶中检索了Terraform状态文件，其中包含IAM用户访问密钥和第二个AWS账户的密钥。这个账户被用来在该组织的云计算中进行横移。

![](https://image.3001.net/images/20230301/1677640048_63fec17059b90a41a0a1c.png!small)
由TruffleHog发现的Terraform秘密

## 基于云的基础设施安全

随着企业越来越依赖云服务来托管他们的基础设施和数据，黑客们也在与时俱进，成为API和管理控制台方面的专家，继续他们的攻击。

SCARLETEEL攻击证明，企业在云环境中的任何一个薄弱点都足以让攻击者利用它进行网络渗透和敏感数据盗窃，当然这些攻击者可能技术更高。

Sysdig建议企业采取以下安全措施，以保护其云基础设施免受类似攻击：

* 及时更新你所有的软件
* 使用IMDS v2而不是v1，这可以防止未经授权的元数据访问
* 对所有用户账户采用最小特权原则
* 对可能包含敏感数据的资源进行只读访问，如Lambda
* 删除旧的和未使用的权限
* 使用密钥管理服务，如AWS KMS、GCP KMS和Azure Key Vault

Sysdig还建议实施一个全面的检测和警报系统，以确保及时报告攻击者的恶意活动，即使他们绕过了保护措施。

> 参考链接：https://www.bleepingcomputer.com/news/security/scarleteel-hackers-use-advanced-cloud-skills-to-steal-source-code-data/

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

SCARLETEEL攻击

基于云的基础设施安全

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