---
title: AWS多项服务存在漏洞，能让攻击者完全控制账户
url: https://www.freebuf.com/news/408363.html
source: FreeBuf网络安全行业门户
date: 2024-08-13
fetch_date: 2025-10-06T18:06:25.132563
---

# AWS多项服务存在漏洞，能让攻击者完全控制账户

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

AWS多项服务存在漏洞，能让攻击者完全控制账户

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

AWS多项服务存在漏洞，能让攻击者完全控制账户

2024-08-12 10:59:55

所属地 上海

据The Hacker News消息，网络安全研究人员在 Amazon Web Services （AWS） 产品中发现了多个严重漏洞，如果成功利用这些漏洞，可能会导致严重后果。

![](https://image.3001.net/images/20240812/1723433599_66b9827fcc644fdaff549.png!small)

根据云安全公司Aqua在与The Hacker News分享的一份详细报告，这些漏洞的影响范围包括远程代码执行（RCE）、全方位服务用户接管（可能提供强大的管理访问权限）、操纵人工智能模块、暴露敏感数据、数据泄露和拒绝服务攻击。

其中，研究人员发现最核心的问题是一种被称为“桶垄断（Bucket Monopoly）的影子资源攻击载体，能在使用 CloudFormation、Glue、EMR、SageMaker、ServiceCatalog 和 CodeStar 等服务时自动创建 AWS S3 存储桶。

由于以该方式创建的 S3 存储桶名称具有唯一性，又遵循预定义的命名规则，攻击者可利用此行为在未使用的 AWS 区域中设置存储桶，并等待合法的 AWS 客户使用上述易受攻击的服务之一来秘密访问 S3 存储桶的内容。

根据攻击者控制的S3存储桶权限，该攻击方法可用于升级以触发 DoS 条件，或执行代码、操纵或窃取数据，甚至在受害者不知情的情况下完全控制其账户。

不过，攻击者必须等到受害者首次在新区域部署新的 CloudFormation 堆栈才能成功发起攻击。而修改 S3 存储桶中的 CloudFormation 模板文件以创建恶意管理员用户还取决于受害者账户是否具有管理 IAM 角色的权限。

Aqua 表示，这种攻击方式不仅影响 AWS 服务，还影响企业组织在AWS 环境中部署的许多开源项目。Aqua还发现其他五项 AWS 服务依赖于类似的 S3 存储桶命名方法，从而容易遭受影子资源攻击：

* AWS Glue: aws-glue-assets-{Account-ID}-{Region}
* AWS Elastic MapReduce (EMR): aws-emr-studio -{Account-ID}-{Region}
* AWS SageMaker: sagemaker-{Region}-{Account-ID}
* AWS CodeStar: aws-codestar-{Region}-{Account-ID}
* AWS Service Catalog: cf-templates-{Hash}-{Region}

这些漏洞于2024年2月首次得到披露，亚马逊在3月—6月期间对这些漏洞进行了修复，相关研究成果已在近期举行的2024美国黑帽大会上进行了公布。

**参考来源：**

> [Experts Uncover Severe AWS Flaws Leading to RCE, Data Theft, and Full-Service Takeovers](https://thehackernews.com/2024/08/experts-uncover-severe-aws-flaws.html)

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