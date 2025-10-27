---
title: LiteSpeed缓存插件漏洞正对WordPress 网站构成重大风险
url: https://www.freebuf.com/news/414222.html
source: FreeBuf网络安全行业门户
date: 2024-11-02
fetch_date: 2025-10-06T19:17:02.368868
---

# LiteSpeed缓存插件漏洞正对WordPress 网站构成重大风险

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

LiteSpeed缓存插件漏洞正对WordPress 网站构成重大风险

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

LiteSpeed缓存插件漏洞正对WordPress 网站构成重大风险

2024-11-01 11:11:52

所属地 上海

WordPress 一款流行插件LiteSpeed Cache 的免费版本最近修复了一个高危的权限提升缺陷，该漏洞可能允许未经身份验证的网站访问者获得管理员权限。

![](https://image.3001.net/images/20241101/1730430831_6724476fd2308b003265b.png!small)

LiteSpeed Cache 是一个缓存插件，被超过 600 万个 WordPress 网站使用，有助于加速和改善用户浏览体验。

新发现的被跟踪为 CVE-2024-50550 的高严重性漏洞是由插件的“角色模拟”功能中的弱哈希检查引起的，该功能旨在模拟用户角色，以帮助爬虫从不同的用户级别进行站点扫描。

该功能的函数 （'is\_role\_simulation（）'） 使用存储在 cookie 中的弱安全哈希值（'litespeed\_hash' 和 'litespeed\_flash\_hash'）执行两个主要检查。 但是，这些哈希值的生成具有有限的随机性，因此在某些配置下是可预测的。

要使 CVE-2024-50550 可被利用，需要在爬网程序中配置以下设置：

1. 运行持续时间和间隔设置在 2500 到 4000 秒之间。
2. 服务器负载限制设置为 0。
3. 角色模拟设置为 administrator。

Patchstack 的安全研究员称，尽管哈希值有 32 个字符长度，但攻击者可以在 100 万种可能性的集合中进行暴力破解。

成功利用此漏洞的攻击者可以模拟管理员角色，这意味着他们可以上传和安装任意插件或恶意软件、访问后端数据库、编辑网页等。

10 月 17 日，供应商 LiteSpeed Technologies 在插件的 6.5.2 版本中发布了针对 CVE-2024-50550 的修复程序，提高了哈希值的随机性，并使暴力破解变得几乎无效。但根据 WordPress.org 下载统计数据，自补丁发布以来，大约有 200 万个网站进行了升级，仍有 400 万个网站暴露在漏洞中。

## LiteSpeed 的安全难题

今年对于 LiteSpeed Cache 及其用户来说是多事之秋，因为这个流行的插件出现了多个关键漏洞，其中一些漏洞被用到了实际的攻击事件中。

2024 年 5 月，黑客利用具有未经身份验证的跨站点脚本缺陷 （CVE-2023-40000） 的过时版本的插件创建管理员帐户并接管站点。

2024年 8 月，研究人员发现了一个关键的未经身份验证的权限提升漏洞 （CVE-2024-28000），警告其很容易被利用。在披露后的几个小时内，攻击者就发起了大规模攻击，Wordfence阻止的恶意尝试次数达到了5万次。

2024年9月，该插件还修复了一个漏洞（CVE-2024-44000），该漏洞能导致未经身份验证的帐户接管。

**参考来源：**

> [LiteSpeed Cache bug exposes 6 million WordPress sites to takeover attacks](https://www.bleepingcomputer.com/news/security/litespeed-cache-bug-exposes-6-million-wordpress-sites-to-takeover-attacks/)

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

LiteSpeed 的安全难题

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