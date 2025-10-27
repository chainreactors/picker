---
title: 多款云存储平台存在安全漏洞，影响超2200万用户
url: https://www.freebuf.com/news/413364.html
source: FreeBuf网络安全行业门户
date: 2024-10-23
fetch_date: 2025-10-06T18:51:03.667570
---

# 多款云存储平台存在安全漏洞，影响超2200万用户

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

多款云存储平台存在安全漏洞，影响超2200万用户

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

多款云存储平台存在安全漏洞，影响超2200万用户

2024-10-22 10:06:13

所属地 上海

据苏黎世联邦理工学院研究人员Jonas Hofmann和Kien Tuong Turong的发现，端到端加密（E2EE）云存储平台存在一系列安全问题，可能会使用户数据暴露给恶意行为者。在通过密码学分析后，研究人员揭示了Sync、pCloud、Icedrive、Seafile和Tresorit服务的问题，这些服务共同被超过2200万人使用。

![](https://image.3001.net/images/20241022/1729563133_671709fdd7d003add90e3.jpg!small)

该分析基于一个攻击者控制恶意服务器的威胁模型，该服务器可以随意读取、修改和注入数据，这对国家级行为者和复杂的黑客来说是现实的。其中不少问题是由于平台违背了用户隐私保护条款，这是数据泄露的前提。

苏黎世联邦理工学院的研究人员在上述五种产品中发现了严重的漏洞，包括允许恶意行为者注入文件、篡改数据或访问用户文件的实现。

以下是发现的问题的概述：

Sync的漏洞包括未认证的密钥材料，允许攻击者注入他们自己的加密密钥并危及数据；文件共享中缺乏公钥认证进一步使攻击者能够解密共享文件；共享链接将密码暴露给服务器，破坏了保密性。此外，攻击者可以在不被检测到的情况下重命名或移动文件，甚至可以将文件夹注入用户存储，使其看起来像是用户上传的。
pCloud的主要问题源于未认证的密钥材料，允许攻击者覆盖私钥并强制使用攻击者控制的密钥进行加密；公钥也未认证，使攻击者能够访问加密文件。此外，攻击者可以注入文件，操纵元数据如文件大小，并由于块过程中缺乏认证，重新排序或删除块。
Icedrive使用未认证的CBC加密，使其容易受到文件篡改的攻击，允许攻击者修改文件内容。文件名也可以被截断或更改。块过程缺乏认证，意味着攻击者可以重新排序或删除文件块，危及文件完整性。
Seafile容易受到协议降级的影响，使密码暴力破解变得更容易。它使用未认证的CBC加密允许文件篡改，未认证的块处理允许攻击者操纵文件块。文件名和位置也不安全，服务器可以将文件或文件夹注入用户存储。
Tresorit的公钥认证依赖于服务器控制的证书，攻击者可以替换这些证书以访问共享文件。元数据也容易受到篡改，允许攻击者更改文件创建详细信息并误导用户。
在检查的五个组中，Tresorit的表现相对较好，因为发现的问题不直接暴露文件内容或允许轻松的数据操纵。

对于研究人员报告的问题，Sync表示，我们的安全团队上周了解到这些问题，自那时以来我们已经迅速采取行动来解决它们。我们还联系了研究团队分享发现并合作进行下一步。

报告中提到的潜在数据泄露问题已经解决，我们现在正在快速跟踪解决剩余潜在问题的修复程序。正如研究论文所述，这些漏洞存在于服务器受到妥协的前提下。没有证据表明这些漏洞已被利用或文件数据已被访问。

端到端加密的承诺是，你不需要信任任何人，甚至我们。这个概念是我们加密模型的核心，也是我们所做的核心。

Tresorit表示，苏黎世联邦理工学院的世界级研究团队研究了端到端加密云存储系统面临的十类攻击的可能性，包括保密性破坏和文件注入漏洞。研究结果证实，Tresorit的设计和密码学选择使我们的系统基本上不受这些攻击的影响。

在Tresorit，安全是我们的首要任务，我们致力于持续改进，利用这些见解进一步加强我们的平台。这项研究不仅帮助我们进化，还指导更广泛的行业朝着更安全的解决方案发展沿。

参考来源：<https://www.bleepingcomputer.com/news/security/severe-flaws-in-e2ee-cloud-storage-platforms-used-by-millions/>

# 数据安全

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