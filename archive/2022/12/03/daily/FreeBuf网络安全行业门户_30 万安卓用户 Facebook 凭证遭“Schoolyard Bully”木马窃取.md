---
title: 30 万安卓用户 Facebook 凭证遭“Schoolyard Bully”木马窃取
url: https://www.freebuf.com/news/351387.html
source: FreeBuf网络安全行业门户
date: 2022-12-03
fetch_date: 2025-10-04T00:24:23.227657
---

# 30 万安卓用户 Facebook 凭证遭“Schoolyard Bully”木马窃取

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

30 万安卓用户 Facebook 凭证遭“Schoolyard Bully”木马窃取

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

30 万安卓用户 Facebook 凭证遭“Schoolyard Bully”木马窃取

2022-12-02 11:31:48

The Hacker News 网站披露，一种名为“Schoolyard Bully”木马程序攻击遍布 71 个国家的 30 多万Android用户。该木马程序伪装成合法的教育主题应用程序，引诱毫无戒心的用户下载，随后便窃取其 Facebook 凭证。![1669951938_638971c26849b69652d87.jpg!small](https://image.3001.net/images/20221202/1669951938_638971c26849b69652d87.jpg!small)

据悉，这些应用程序可以从官方Google Play商店下载，目前已经被删除了。但是，用户仍然可以在第三方应用商店中下载并继续使用。

Zimperium 研究人员 Nipun Gupta 和 Aazim Bill SE Yaswant 在与 The Hacker News 分享的一份报告中表示，“Schoolyard Bully”木马程序使用了 JavaScript 注入来窃取 Facebook 凭证。

研究人员进一步分析发现，“Schoolyard Bully”通过在 WebView 中启动 Facebook 的登录页面来实现这一目的，该页面还嵌入了恶意 JavasCript 代码，将用户电话号码、电子邮件地址和密码渗透到配置的命令和控制（C2）服务器。![1669951960_638971d8edff124716bc0.jpg!small](https://image.3001.net/images/20221202/1669951960_638971d8edff124716bc0.jpg!small)

此外，“Schoolyard Bully”木马还进一步利用诸如“libabc.so”之类的本地库，以避免防病毒解决方案的检测。

虽然“Schoolyard Bully”木马专门针对越南语应用程序，但在 70 多个国家的其它应用程序中也发现了其踪迹。

一年多前，Zimperium 在代号为 FlyTrap 的活动中发现了类似活动，攻击者旨在通过恶意 Android 应用程序危害 Facebook 账户。

Zimperium 移动威胁情报主管理查德·梅里克（Richard Melick）强调，攻击者窃取 Facebook 密码会造成很大破坏，如果攻击者冒充受害者，就很容易诱使其朋友和其它联系人发送金钱或敏感信息。

值得注意的是，许多用户重复使用相同密码，如果攻击者窃取了受害者 Facebook 密码，很可能掌握其电子邮件和密、银行或金融应用程序、公司账户等。

**参考文章：**

> https://thehackernews.com/2022/12/schoolyard-bully-trojan-apps-stole.html

# 木马

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