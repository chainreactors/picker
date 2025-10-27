---
title: 超百万站点使用，WordPress 插件 AIOS 被曝以明文记录密码
url: https://www.freebuf.com/news/372245.html
source: FreeBuf网络安全行业门户
date: 2023-07-18
fetch_date: 2025-10-04T11:55:55.204566
---

# 超百万站点使用，WordPress 插件 AIOS 被曝以明文记录密码

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

超百万站点使用，WordPress 插件 AIOS 被曝以明文记录密码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

超百万站点使用，WordPress 插件 AIOS 被曝以明文记录密码

2023-07-17 11:47:00

所属地 上海

Bleeping Computer 网站披露，超过百万 WordPress 网站使用的 All-In-One Security（AIOS）WordPress安全插件被曝将用户尝试登录的明文密码记录到网站数据库中，此举可能危及账户安全。![1689565548_64b4b96c64ab429a93ac6.png!small?1689565548625](https://image.3001.net/images/20230717/1689565548_64b4b96c64ab429a93ac6.png!small?1689565548625)

AIOS 是 Updraft 开发的一体式解决方案，主要为 WordPress 网站提供网络应用程序防火墙、内容保护和登录安全工具，以阻止机器人并防止暴力攻击。

大约在三周前，一位用户反应 AIOS v5.1.9 插件不仅将用户尝试登录记录到 aiowps\_audit\_log 数据库表中，用于跟踪登录、注销和失败的登录事件，还记录了用了输入的密码。该用户担心此举违反了包括NIST 800-63 3、ISO 27000和GDPR在内的多项安全合规标准，![1689565567_64b4b97ff31c5bf272307.png!small?1689565568131](https://image.3001.net/images/20230717/1689565567_64b4b97ff31c5bf272307.png!small?1689565568131)

漏洞的初步报告（wordpress.org）

接到反馈后，Updraft 方面回应称该问题是一个 "已知错误"，并含糊地承诺将在下一个版修复问题。在意识到问题的严重性后，Updraft 支持人员两周前向相关用户提供了即将发布的开发版，但是试图安装开发版的用户仍指出密码日志没有被删除。

## ****修复程序现已发布****

7 月 11 日，AIOS 供应商发布了 5.2.0 版本，其中包括一个防止保存明文密码并清除旧条目的修复程序。AIOS 供应商在公告中一再强调 AIOS 发布的 5.2.0 版本更新版本修复了 5.1.9 版本中存在的一个错误，该错误导致用户密码以明文形式添加到 WordPress 数据库中。

一旦“恶意”网站管理员在用户可能使用相同密码的其他服务上尝试利用这些密码，此举会带来一些安全问题。此外，一旦被暴露者的登录信息在这些平台上没有受到双因素身份验证的保护，“恶意”管理员就可以轻易接管用户的账户。

除了“恶意”管理员带来的安全风险外，使用 AIOS 的网站还将面临黑客入侵的风险，这些黑客一旦获得网站数据库访问权限，便有可能会以明文形式泄露用户密码。![1689565596_64b4b99c5c477911bdef9.png!small](https://image.3001.net/images/20230717/1689565596_64b4b99c5c477911bdef9.png!small)

截止到文章发布，WordPress.org 统计数据显示大约四分之一的 AIOS 用户已将更新应用 5.2.0 版本，因此推算大概仍有超过 75 万个网站处于易受攻击状态。

更不幸的是，WordPress 一直以来都是网络攻击者的攻击目标，一些使用 AIOS 的网站可能已经被泄露，再加上该安全问题已经在网上传播了三周多，且 Updraft 没有警告用户暴露风险的增加，因此，可能已经发生了一些安全威胁事件。

最后，使用 AIOS 的网站应该尽快更新到最新版本，并要求用户重置密码。

**文章来源;**

> https://www.bleepingcomputer.com/news/security/wordpress-aios-plugin-used-by-1m-sites-logged-plaintext-passwords/

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

文章目录

修复程序现已发布

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