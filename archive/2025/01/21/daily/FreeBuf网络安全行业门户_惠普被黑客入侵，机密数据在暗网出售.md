---
title: 惠普被黑客入侵，机密数据在暗网出售
url: https://www.freebuf.com/news/420293.html
source: FreeBuf网络安全行业门户
date: 2025-01-21
fetch_date: 2025-10-06T20:10:15.166666
---

# 惠普被黑客入侵，机密数据在暗网出售

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

惠普被黑客入侵，机密数据在暗网出售

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

惠普被黑客入侵，机密数据在暗网出售

2025-01-20 14:31:01

所属地 上海

![](https://image.3001.net/images/20250120/1737354626_678ded82807f2e40cb1d3.png!small)

黑客IntelBroker宣称已经入侵惠普企业公司（HPE），并公布了诸如源代码、证书和个人身份信息（PII）等敏感数据，这些数据如今可在线售卖。

声名狼藉的IntelBroker黑客及其同伙宣称对入侵惠普企业公司（HPE）一事负责。HPE是一家总部位于美国得克萨斯州休斯顿的全球性企业，为企业提供技术解决方案。

这名此前与多起备受瞩目的数据泄露事件有关联的黑客，目前正在出售据称被盗取的数据，并且要求以门罗币（XMR）加密货币支付，以此确保匿名性与不可追踪性。

这一消息是由黑客本人向Hackread.com透露的，随后在由黑客管理的网络犯罪和数据泄露论坛Breach Forums上公布。在与Hackread.com的独家对话中，IntelBroker宣称此次入侵是对HPE基础设施的直接攻击，并非通过第三方获取访问权限，而通过第三方获取权限在近期的攻击中较为常见。

## 被盗数据都有哪些？

IntelBroker还分享了一个数据树以及两张据称从公司内部基础设施截取的截图。Hackread.com分析发现，这个数据树似乎与一个开发或系统环境有关，其中包含开源软件和专有包管理系统。

此外，黑客宣称已经提取了敏感数据，包括源代码、私人GitHub仓库、Docker构建、证书（私钥和公钥）、属于Zerto和iLO的产品源代码、与交付相关的旧PII等用户数据，还有访问API、WePay、自托管GitHub仓库等的权限。

![](https://image.3001.net/images/20250120/1737354768_678dee104653d510855f3.jpg!small)

在Hackread.com对据称的数据树进行初步分析时，有几项发现与黑客的声明相符。目录结构中包含了私钥和证书，例如`ca-signed.key`和`hpe\_trusted\_certificates.pem`，这表明可能暴露了敏感的加密材料。

HPE产品（如iLO和Zerto）的源代码也存在，文件如`ilo\_client.py`和`zerto\_bootstrapper.py`暗示了专有实现的泄露。对`.github`目录和私有仓库的`.tar`存档的引用进一步表明开发资产可能已被泄露。

此外，文件中出现了如`VMW-esx-7.0.0-hpe-zertoreplication.zip`和`ZertoRunner.exe`等文件，这表明可能泄露了编译后的软件包和部署文件。如果这些信息被HP证实，这可能会成为一起重大的安全事件。

以下图片结合了黑客分享的两张截图，提供了对惠普企业公司内部系统的详细洞察。第一张截图显示了惠普企业公司内部SignonService网络服务的详细信息。图片展示了服务的端点地址、WSDL链接和实现类，可能暴露了敏感的基础设施信息。

第二张截图揭示了惠普企业公司内部系统的敏感配置细节。图片暴露了Salesforce和QIDs集成的凭证、SAP S/4 HANA报价服务的内部URL，以及用于错误日志记录的占位符电子邮件地址，这可能突显了HPE基础设施中的严重安全漏洞。

![](https://image.3001.net/images/20250120/1737354959_678deecfa34a474d25f4b.jpg!small)

## 此惠普非彼惠普

虽然惠普企业公司（HPE）和惠普公司（HP Inc.）的名称常常被混用，但它们是两家不同的公司，业务重点也有所不同。2015年，惠普拆分为两家独立的实体。惠普公司继续专注于消费类产品，例如笔记本电脑、台式机和打印机；而惠普企业公司（HPE）则专注于提供企业级IT解决方案，涵盖服务器、存储、网络和云计算等方面。

这两家公司相互独立，拥有各自独立的所有权和管理权。强调这一区别很重要，因为此次报道的入侵事件专门针对HPE，并非惠普公司。

Intel Broker因高调的数据泄露事件而闻名。2024年10月，黑客宣称入侵思科并窃取了数TB的数据。思科后来证实，被盗数据源于一个配置错误、公开的DevHub资源，该资源未设密码保护，致使黑客能够下载数据。

2024年11月，黑客宣称通过第三方承包商入侵了诺基亚，以2万美元的价格出售数据。同一黑客还吹嘘入侵了AMD（先进微设备公司），并窃取了员工和产品信息。

参考来源：<https://hackread.com/hackers-claim-hewlett-packard-data-breach-sale/>

# 数据安全 # 暗网

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

被盗数据都有哪些？

此惠普非彼惠普

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