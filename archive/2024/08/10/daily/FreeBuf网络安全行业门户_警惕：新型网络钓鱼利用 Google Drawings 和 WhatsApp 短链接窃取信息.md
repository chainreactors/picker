---
title: 警惕：新型网络钓鱼利用 Google Drawings 和 WhatsApp 短链接窃取信息
url: https://www.freebuf.com/news/408175.html
source: FreeBuf网络安全行业门户
date: 2024-08-10
fetch_date: 2025-10-06T18:05:09.904445
---

# 警惕：新型网络钓鱼利用 Google Drawings 和 WhatsApp 短链接窃取信息

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

警惕：新型网络钓鱼利用 Google Drawings 和 WhatsApp 短链接窃取信息

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

警惕：新型网络钓鱼利用 Google Drawings 和 WhatsApp 短链接窃取信息

2024-08-09 10:50:27

所属地 上海

近日，网络安全研究人员发现了一种新型网络钓鱼活动，它利用 Google Drawings 和 WhatsApp 生成的短链接来逃避检测，并诱骗用户点击旨在窃取敏感信息的虚假链接。

![](https://image.3001.net/images/20240809/1723170061_66b57d0dd56870a11a32e.jpg!small)Menlo Security 研究员 Ashwin Vamshi 说：“攻击者精心挑选了包括Google和WhatsApp在内的知名网站来托管攻击组件，并通过模仿亚马逊网站来收集受害者信息。这种攻击是‘利用受信任站点’（LoTS）威胁的一个典型案例。”

攻击始于一封网络钓鱼邮件，邮件内容引导收件人点击一个看似亚马逊账户验证的链接。这个链接实际上是托管在 Google Drawings 上的一个图像，目的是避免被安全系统检测。

![](https://image.3001.net/images/20240809/1723170009_66b57cd9d1043a38c0a64.png!small)

Vamshi 还提到，Google Drawings 在攻击初期具有吸引力的另一个原因是，它允许攻击者在其图像中嵌入链接，这些链接很容易被用户忽视，尤其是当他们对亚马逊账户可能面临的风险感到紧迫时。

当用户点击该验证链接后，会被重定向至一个模仿亚马逊登录页面的伪造网站。该网站的URL先后使用了两个不同的URL缩短器——WhatsApp“l.wl[.]co”和 qrc[.]de 进行双重伪装，以进一步混淆和欺骗安全URL扫描器。

这个伪造页面旨在收集用户的登录凭证、个人信息和信用卡数据，随后将受害者重定向到原始的亚马逊登录页面。为了增加安全性，一旦用户的凭证被验证，该伪造页面将无法从同一 IP 地址访问。

与此同时，研究人员还发现了 Microsoft 365 反网络钓鱼机制中的一个漏洞，该漏洞可能被利用来增加用户打开网络钓鱼邮件的风险。

该漏洞涉及到使用 CSS 技巧隐藏“首次联系安全提示”，这是一种当用户收到来自未知地址的电子邮件时的警告机制。微软已经承认了这个问题，但尚未提供修复方案。

奥地利网络安全公司Certitude表示：“首次联系安全提示”被添加到 HTML 电子邮件的正文中，这意味着可以通过 CSS 样式标签来改变其显示方式。甚至可以进一步伪造 Microsoft Outlook 在加密和/或签名的电子邮件中添加的图标。”

参考来源：
https://thehackernews.com/2024/08/new-phishing-scam-uses-google-drawings.html

# 网络钓鱼 # url # 网络钓鱼攻击

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