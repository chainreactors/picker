---
title: Internet Archive 遭遇黑客攻击，导致 3100 万用户数据泄露
url: https://www.freebuf.com/news/412412.html
source: FreeBuf网络安全行业门户
date: 2024-10-11
fetch_date: 2025-10-06T18:52:00.874375
---

# Internet Archive 遭遇黑客攻击，导致 3100 万用户数据泄露

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

Internet Archive 遭遇黑客攻击，导致 3100 万用户数据泄露

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Internet Archive 遭遇黑客攻击，导致 3100 万用户数据泄露

2024-10-10 10:31:51

所属地 上海

![](https://image.3001.net/images/20241010/1728525252_670733c4a450d5f9f570d.png!small)

近日， 有黑客入侵了Internet Archive 网站并窃取了一个包含3100万条记录的用户认证数据库。

昨天（10月9日）下午 ，在 archive.org 的访问者开始看到黑客创建的 JavaScript 警报后，有关泄露的消息开始流传，称 Internet Archive 已被入侵。

archive.org 网站上显示的 JavaScript 警报中写道：“你有没有觉得互联网档案馆就像是在用棍子运行，随时可能遭受灾难性的安全漏洞？现在已经发生了。看到HIBP上的3100万用户了吗！”这里的“HIBP”指的是由Troy Hunt创建的Have I Been Pwned数据泄露通知服务，威胁分子通常会与之分享窃取的数据以添加到该服务中。

![1728529613_670744cd57158e349783a.png!small](https://image.3001.net/images/20241010/1728529613_670744cd57158e349783a.png!small)

Archive.org上显示的 JavaScript， 警报来源：BleepingComputer

Hunt告诉BleepingComputer，威胁分子在九天前分享了 Internet Archive 的认证数据库，这是一个名为“ia\_users.sql”的6.4GB SQL文件。该数据库包含注册会员的认证信息，包括他们的电子邮件地址、屏幕名称、密码更改时间戳、Bcrypt散列密码以及其他内部数据。被盗记录的最新时间戳是2024年9月28日，这可能是数据库被盗的时间。

Hunt表示，数据库中有3100万唯一的电子邮件地址，其中许多订阅了HIBP数据泄露通知服务。这些数据将很快被添加到HIBP中，允许用户输入他们的电子邮件并确认他们的数据是否在此次泄露中被暴露。

在Hunt联系了数据库中列出的用户（包括网络安全研究员Scott Helme）后，确认了数据的真实性。

![1728529866_670745ca0897423509fe3.png!small](https://image.3001.net/images/20241010/1728529866_670745ca0897423509fe3.png!small)

Helme允许BleepingComputer分享他的暴露记录。Helme确认，数据记录中的bcrypt散列密码与他密码管理器中存储的bcrypt散列密码相匹配。他还确认，数据库记录中的时间戳与他最后一次在密码管理器中更改密码的日期相匹配。

![1728529897_670745e923be936fe479d.png!small](https://image.3001.net/images/20241010/1728529897_670745e923be936fe479d.png!small)

archive.org的密码管理器条目，参考来源：Scott Helme

Hunt表示，他在三天前联系了 Internet Archive  并开始了披露过程，称数据将在72小时内加载到服务中，但此后他再也没有收到回复。

目前尚不清楚威胁分子是如何侵入 Internet Archive  的，以及是否有其他数据被盗。

昨天早些时候， Internet Archive  遭受了一次DDoS攻击，BlackMeta黑客组织声称将对此次攻击负责，他们表示还将进行的其他持续攻击。BleepingComputer就此次攻击联系了 Internet Archive ，但暂时没有得到回应。

> 参考来源：<https://www.bleepingcomputer.com/news/security/internet-archive-hacked-data-breach-impacts-31-million-users/>

# 黑客攻击 # 数据窃取

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