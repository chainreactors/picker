---
title: 微软Sway在大规模二维码钓鱼活动中被滥用
url: https://www.freebuf.com/news/409605.html
source: FreeBuf网络安全行业门户
date: 2024-08-29
fetch_date: 2025-10-06T18:04:30.331038
---

# 微软Sway在大规模二维码钓鱼活动中被滥用

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

微软Sway在大规模二维码钓鱼活动中被滥用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

微软Sway在大规模二维码钓鱼活动中被滥用

2024-08-28 09:22:41

所属地 上海

![Phishing.jpg](https://image.3001.net/images/20240828/1724808165_66ce7be5caac4b9d291c4.jpg!small)

近期，一个大规模的网络钓鱼活动利用Microsoft Sway这一云基础的在线演示工具来搭建登陆页面，目的是为了诱使Microsoft 365用户泄露他们的登录凭证。

2024年7月，Netskope的安全威胁实验室发现，通过Microsoft Sway托管的钓鱼网页数量激增，与今年上半年相比，增长了惊人的2000倍。这种急剧上升的趋势与此前的低活动水平形成了鲜明对比，更加凸显了这次攻击活动的规模。

该活动主要针对亚洲和北美地区的用户，特别是技术、制造和金融行业，这些行业成为攻击者的主要目标。

攻击者通过电子邮件将潜在的受害者引导至由sway.cloud.microsoft域名托管的钓鱼登陆页面。这些页面诱导目标用户扫描QR码，进而将他们重定向到其他恶意网站。

攻击者倾向于鼓励用户使用移动设备扫描这些二维码，因为移动设备的安全防护通常较弱，这增加了他们绕过安全措施、无障碍访问钓鱼网站的可能性。

安全研究人员指出：由于URL被嵌入到图片中，那些只能扫描文本内容的电子邮件扫描器将无法识别。此外，当用户收到二维码时，他们可能会选择使用手机等移动设备进行扫描。

“移动设备，尤其是个人手机，其实施的安全措施通常没有笔记本电脑和台式机那么严格，这使得用户更容易成为攻击的目标。”研究人员进一步解释道。

![1724808118_66ce7bb6215fd5b7f6b69.png!small](https://image.3001.net/images/20240828/1724808118_66ce7bb6215fd5b7f6b69.png!small)

微软 Sway 网络钓鱼页面示例（来源：Netskope）

攻击者采取了多种手段来提高其钓鱼活动的成功率，例如通过透明钓鱼手段，他们盗取了用户的凭证和多因素认证码，并在向用户展示合法登录页面的同时，使用这些信息登录用户的Microsoft账户。

他们还使用了Cloudflare Turnstile这一旨在防止机器人访问的工具，来隐藏其钓鱼登陆页面的内容，避免静态扫描器的检测。这有助于保持钓鱼域名的良好信誉，并防止被诸如Google Safe Browsing之类的网络过滤服务所屏蔽。

Microsoft Sway在五年前的PerSwaysion钓鱼活动中也遭到了滥用，该活动通过一个在恶意软件即服务（MaaS）业务中提供的钓鱼套件，针对Office 365的登录凭证。

Group-IB的安全研究人员当时揭露，这些攻击至少欺骗了156位在中小型金融服务公司、律师事务所和房地产集团中担任高级职位的人员。

Group-IB表示，在所有被“收割” 的Office 365账户中，有超过20%是来自美国、加拿大、德国、英国、荷兰、香港和新加坡等国家或地区的组织中的高级执行官、总裁和常务董事。

> 参考来源：[Microsoft Sway abused in massive QR code phishing campaign (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/microsoft-sway-abused-in-massive-qr-code-phishing-campaign/)

# 网络钓鱼活动

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