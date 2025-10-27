---
title: 知名工具Trello被黑客攻击，泄露1500 万用户数据
url: https://www.freebuf.com/news/406218.html
source: FreeBuf网络安全行业门户
date: 2024-07-18
fetch_date: 2025-10-06T17:44:30.224978
---

# 知名工具Trello被黑客攻击，泄露1500 万用户数据

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

知名工具Trello被黑客攻击，泄露1500 万用户数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

知名工具Trello被黑客攻击，泄露1500 万用户数据

2024-07-17 13:48:26

所属地 上海

![1721194985_669759e90a768c8e1bea0.png!small](https://image.3001.net/images/20240717/1721194985_669759e90a768c8e1bea0.png!small)

Trello 是 Atlassian 旗下的一款在线项目管理工具，企业通常使用它将数据和任务组织到板块、卡片和列表中。

近日，有黑客发布了与 Trello 账户相关的 1500 万个电子邮件地址，这些地址是今年 1 月被 API 收集到的。当时有一个名为 “emo ”的威胁行为者在一个流行的黑客论坛上出售 15 万个 Trello 会员的资料。

虽然这些档案中的数据几乎都是公开信息，但每个档案还额外包含一个与账户相关的非公开电子邮件地址。虽然 Trello 的所有者 Atlassian 当时并未证实这些数据是如何被窃取的，但这些数据是通过一个不安全的 REST API 收集的，该 API 允许开发人员根据用户的 Trello ID、用户名或电子邮件地址查询配置文件的公共信息。

emo 创建了一个包含 5 亿个电子邮件地址的列表，并将其输入 API 以确定它们是否与 Trello 帐户有关联。然后将该列表与返回的账户信息相结合，创建了超过 1500 万用户的会员档案。

今天，emo 在 Breached 黑客论坛上以 8 个网站信用点，价值 2.32 美元的价格分享了15万个配置文件列表。

emo在论坛帖子中解释道：Trello有一个开放的API端点，允许任何未经验证的用户将电子邮件地址映射到trello账户。我原本只打算向端点提供来自'com'（OGU、RF、Breached 等）数据库的电子邮件，但我决定继续使用电子邮件，直到厌倦为止。

![trello-leak.jpg](https://image.3001.net/images/20240717/1721196452_66975fa4481fd303dcf41.jpg!small)

据悉，此次泄露的数据包括电子邮件地址和公共 Trello 帐户信息，其中包括用户的全名。

这些信息可用于有针对性的网络钓鱼攻击，以窃取更敏感的信息，如密码。Emo 还表示，这些数据可用于 “dxxing”，使威胁行为者能够将电子邮件地址与个人及其别名联系起来。

Atlassian 今天向 BleepingComputer 证实，这些信息是通过 Trello REST API 收集的，该 API 于今年 1 月被加密。

他表示：在 Trello REST API 的支持下，Trello 用户可以通过电子邮件地址邀请成员或访客访问其公共板块。但是，鉴于 2024 年 1 月的调查中发现的对 API 的滥用，我们对 API 进行了修改，使未经身份验证的用户/服务无法通过电子邮件请求其他用户的公开信息。已通过身份验证的用户仍可使用此 API 请求其他用户配置文件中的公开信息。这一改动在防止滥用 API 和保持 “通过电子邮件邀请到公开讨论区 ”功能对用户有效之间取得了平衡。后续将继续监控 API 的使用情况，并采取任何必要的措施。

如今，不安全的 API 已成为威胁行为者的热门攻击目标，他们滥用 API 将电子邮件地址和电话号码等非公开信息与公开资料相结合。

2021 年，有黑客曾滥用 API 将电话号码与 Facebook 账户链接，创建了 5.33 亿用户的个人资料。

2022 年，Twitter 也曝出了类似的漏洞，黑客通过滥用 API 获取到了数百万用户的电话号码和电子邮件地址。

这些数据可以揭露在社交媒体上匿名发帖的人的身份，从而带来巨大的隐私风险。

最近，有人利用不安全的 Twilio API 获取了 3300 万 Authy 多因素身份验证应用程序用户的电话号码。目前有很多企业组织都试图使用速率限制来保护 API，而不再是通过 API 密钥进行身份验证。

但只要黑客购买数百个代理服务器，并轮流连接以不断查询 API，那么速率限制就会毫无用处。

> 参考来源：[Email addresses of 15 million Trello users leaked on hacking forum (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/email-addresses-of-15-million-trello-users-leaked-on-hacking-forum/)

# 数据泄露

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