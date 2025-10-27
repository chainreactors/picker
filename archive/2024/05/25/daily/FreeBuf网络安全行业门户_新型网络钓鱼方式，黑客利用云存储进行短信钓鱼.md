---
title: 新型网络钓鱼方式，黑客利用云存储进行短信钓鱼
url: https://www.freebuf.com/news/401751.html
source: FreeBuf网络安全行业门户
date: 2024-05-25
fetch_date: 2025-10-06T17:17:47.898295
---

# 新型网络钓鱼方式，黑客利用云存储进行短信钓鱼

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

新型网络钓鱼方式，黑客利用云存储进行短信钓鱼

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型网络钓鱼方式，黑客利用云存储进行短信钓鱼

2024-05-24 10:23:26

所属地 上海

近日，安全研究人员揭露了一系列利用亚马逊 S3、谷歌云存储、Backblaze B2 和 IBM 云对象存储等云存储服务的犯罪活动。这些活动由未具名的威胁行为者发起，目的是将用户重定向到恶意网站，利用短信窃取他们的信息。

![](https://image.3001.net/images/20240524/1716518682_664fff1ad7ae45a61f566.jpg!small)根据 Enea 今天发表的一篇技术文章，攻击者有两个主要目标。

1. 威胁行为者要确保诈骗短信能在不被网络防火墙检测到的情况下发送到手机上。
2. 威胁行为者试图让终端用户相信他们收到的短信或链接是可信的。

威胁行为者利用云存储平台托管带有嵌入式垃圾邮件 URL 的静态网站，使其信息看起来合法，并避开常见的安全措施。

云存储服务允许企业存储和管理文件，并通过在存储桶中存储网站资产来托管静态网站，威胁行为者利用这一功能，将垃圾邮件 URL 嵌入存储在这些平台上的静态网站中。

他们通过短信分发链接到这些云存储网站的 URL，由于知名云域被认为是合法的，这些 URL 通常可以绕过防火墙限制。用户一旦点击这些链接，就会在不知情的情况下被重定向到恶意网站。

例如，谷歌云存储域名 “storage.googleapis.com” 就被攻击者用来创建链接到垃圾网站的 URL。托管在谷歌云存储桶中的静态网页采用了 HTML 元刷新技术，可立即将用户重定向到诈骗网站。威胁行为者利用这种方法诱骗用户访问欺诈网站，这些网站通常会模仿礼品卡促销等合法优惠活动，以窃取用户的个人信息和财务信息。

Enea 还观察到亚马逊网络服务（AWS）和 IBM 云等其他云存储服务也采用了类似的策略，即通过短信中的 URL 进入托管垃圾邮件的静态网站。

为防范此类威胁，Enea 建议监控流量行为、检查 URL 并警惕包含链接的意外消息。

参考来源：https://www.infosecurity-magazine.com/news/cloud-storage-exploited-sms/

# 网络钓鱼攻击 # 云存储 # 钓鱼诈骗

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