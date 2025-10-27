---
title: 二维码网络钓鱼攻击泛滥！美国著名能源企业成主要攻击目标
url: https://www.freebuf.com/news/375201.html
source: FreeBuf网络安全行业门户
date: 2023-08-18
fetch_date: 2025-10-04T11:59:42.915870
---

# 二维码网络钓鱼攻击泛滥！美国著名能源企业成主要攻击目标

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

二维码网络钓鱼攻击泛滥！美国著名能源企业成主要攻击目标

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

二维码网络钓鱼攻击泛滥！美国著名能源企业成主要攻击目标

2023-08-17 10:57:40

所属地 上海

![1692239447_64dd865797e961a4737c9.png!small?1692239448503](https://image.3001.net/images/20230817/1692239447_64dd865797e961a4737c9.png!small?1692239448503)

近日，Cofense发现了一次专门针对美国能源公司的网络钓鱼攻击活动，攻击者利用二维码将恶意电子邮件塞进收件箱并绕过安全系统。

Cofense 方面表示，这是首次发现网络钓鱼行为者如此大规模的使用二维码进行钓鱼攻击，这表明他们可能正在测试用二维码作为攻击载体的有效性。

在归因于该活动的 1,000 封电子邮件中，约有三分之一（29%）是针对美国一家大型能源公司的，其余的则是针对制造业（15%）、保险业（9%）、科技业（7%）和金融服务业（6%）的公司。

不过Cofense 并没有透露此次活动的目标能源公司具体名称，只将其归类为美国的一家 "大型 "公司。

![1692240190_64dd893e60c2ff94c2460.png!small?1692240190309](https://image.3001.net/images/20230817/1692240190_64dd893e60c2ff94c2460.png!small?1692240190309)

二维码钓鱼活动 来源：Cofense Cofense

## 网络钓鱼中的二维码

Cofense 方面称，攻击开始时会先发送一封钓鱼电子邮件，提醒收件人必须尽快更新其 Microsoft 365 帐户设置。邮件中的 PNG 或 PDF 附件会带有二维码，收件人会被提示扫描以验证其账户。为了增加紧迫感，邮件还指出收件人必须在 2-3 天内完成这一步骤。

![1692241082_64dd8cba2998471604307.png!small?1692241083146](https://image.3001.net/images/20230817/1692241082_64dd8cba2998471604307.png!small?1692241083146)

网络钓鱼电子邮件样本 来源：Cofense Cofense

威胁行为者使用嵌入在图片中的 QR 代码绕过电子邮件安全工具，这些工具会扫描邮件中的已知恶意链接，从而使网络钓鱼邮件到达目标收件箱。

为了规避安全问题，钓鱼活动中的 QR 代码还使用了必应、Salesforce 和 Cloudflare 的 Web3 服务中的重定向功能，将目标重定向到 Microsoft 365 钓鱼页面。

在 QR 代码中隐藏重定向 URL、滥用合法服务以及为钓鱼链接使用 base64 编码都有助于逃避检测和通过电子邮件保护过滤器。

![1692241216_64dd8d4087af59b0ab64e.png!small?1692241217004](https://image.3001.net/images/20230817/1692241216_64dd8d4087af59b0ab64e.png!small?1692241217004)

重定向 URL 示例（Cofense）

## 网络犯罪分子利用二维码窃取凭证和财务信息

QR 码过去也曾被攻击者用于其在法国和德国的网络钓鱼活动，尽管规模较小。此外，这些诈骗者还利用二维码诱骗人们扫描，并将他们重定向到恶意网站，试图窃取他们的钱财。

2022 年 1 月，美国联邦调查局警告称，网络犯罪分子越来越多地利用二维码窃取凭证和财务信息。尽管二维码能有效绕过保护措施，但它仍然需要受害者采取行动才能被破解，这是一个有利于训练有素人员的决定性缓解因素。

此外，现代智能手机上的大多数二维码扫描器都会要求用户在启动浏览器前验证目标 URL，以此作为保护措施。

除培训外，Cofense 还建议企业使用图像识别工具作为其网络钓鱼防护措施的一部分，尽管这些工具不能保证捕捉到所有 QR 代码威胁。

> 参考来源：[Major U.S. energy org targeted in QR code phishing attack (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/major-us-energy-org-targeted-in-qr-code-phishing-attack/)

# 钓鱼攻击 # 网络钓鱼攻击 # 能源企业

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

网络钓鱼中的二维码

网络犯罪分子利用二维码窃取凭证和财务信息

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