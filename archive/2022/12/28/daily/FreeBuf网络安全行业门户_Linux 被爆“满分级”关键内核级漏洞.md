---
title: Linux 被爆“满分级”关键内核级漏洞
url: https://www.freebuf.com/news/353584.html
source: FreeBuf网络安全行业门户
date: 2022-12-28
fetch_date: 2025-10-04T02:36:22.438830
---

# Linux 被爆“满分级”关键内核级漏洞

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

Linux 被爆“满分级”关键内核级漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Linux 被爆“满分级”关键内核级漏洞

2022-12-27 11:07:57

所属地 上海

据Security Affairs消息，近期披露的一个严重 Linux 内核漏洞会影响 SMB 服务器，可能导致远程代码执行。

![](https://image.3001.net/images/20221227/1672110603_63aa620b31820e9ef5396.jpg!small)

该漏洞的 CVSS 评分达到了最高级别的10分，影响启用了 KSMBD 的服务器。KSMBD 是一个 Linux 内核服务器，它在内核空间实现 SMB3 协议，用于通过网络共享文件，未经身份验证的远程攻击者可以在易受攻击的 Linux 内核安装上执行任意代码。

趋势科技在其网站上的发布的漏洞披露显示，虽然利用此漏洞不需要身份验证，但只有启用了KSMBD 的系统容易受到攻击。漏洞存在于 SMB2\_TREE\_DISCONNECT 命令的处理过程中，是由于在对象执行操作之前没有验证对象的存在，攻击者可以利用此漏洞在内核上下文中执行任意代码。

Thales Group 的 Thalium 团队的研究人员于今年7月26日首次发现了该漏洞，12 月 22 日该漏洞得到公开披露。

云安全初创公司 wiz.io 的研究主管Shir Tamari表示，由于 KSMBD 模块不像 Samba 套件那样流行，因此尽管漏洞很严重，但其潜在影响可能有限。该漏洞仅影响使用 Linux 5.15 中引入KSMBD 模块的 SMB 服务器。若用户的 SMB 服务器使用 Samba，则不会受到任何影响。

为此，使用 KSMBD的用户必须更新到自8 月之后发布的新版Linux 内核版本——5.15.61及以上版本。

参考来源：

> [Critical Linux Kernel flaw affects SMB servers with ksmbd enabled](https://securityaffairs.com/140013/hacking/critical-linux-kernel-vulnerability.html?_gl=1*1cn1w5l*_ga*MTUyMzgwNzcxMS4xNjU3NzA2OTkw*_ga_8ZWTX5HC4Z*MTY3MjEwNjQ2NS43OC4wLjE2NzIxMDY0NjUuMC4wLjA.*_ga_P62M3QN974*MTY3MjEwNjQ2NS4xMjYuMC4xNjcyMTA2NDg0LjAuMC4w&_ga=2.105079755.932334235.1672021027-1523807711.1657706990)

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