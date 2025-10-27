---
title: 一个隐藏SQLite数据库长达22年的漏洞
url: https://www.freebuf.com/news/348001.html
source: FreeBuf网络安全行业门户
date: 2022-10-28
fetch_date: 2025-10-03T21:08:03.800845
---

# 一个隐藏SQLite数据库长达22年的漏洞

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

一个隐藏SQLite数据库长达22年的漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

一个隐藏SQLite数据库长达22年的漏洞

2022-10-27 13:41:55

所属地 上海

安全专家Andreas Kellas详细介绍了2000年10月推出的SQLite数据库中的一个高严重性漏洞，被追踪为CVE-2022-35737（CVSS评分：7.5）。![](https://image.3001.net/images/20221027/1666848358_635a1666c269cec4151a9.jpeg!small)

CVE-2022-35737漏洞是一个整数溢出问题，影响到SQLite 1.0.12至3.39.1版本。该漏洞已在2022年7月21日发布的3.39.2版本中得到解决。此前，如果在C API的字符串参数中使用了数十亿字节，则有时会允许数组边界溢出。攻击者可以触发这个问题，在受影响的系统上执行任意代码。

CVE-2022-35737在64位系统上可被利用，可利用性取决于程序的编译方式。在没有堆栈金丝雀的情况下编译库时确认任意代码执行，存在堆栈金丝雀时未确认，并且在所有情况下都确认拒绝服务。

所以，为了利用CVE-2022-35737漏洞，攻击者必须将大字符串输入传递给printf函数的 SQLite 实现，并且格式字符串包含 %Q、%q 或 %w 格式替换类型。该漏洞与printf调用的名为“ sqlite3\_str\_vappendf ”的函数处理字符串格式的方式有关。

当sqlite3\_str\_vappendf函数收到一个大字符串，并且格式替换类型为%q、%Q或%w时，就会触发有符号的整数溢出。

研究人员还发现，如果启用 unicode 字符扫描的特殊字符，那么在最坏的情况下有可能实现任意代码执行，或者导致 DoSS 条件。

最后，安全专家Andreas Kellas总结说道："这是一个在编写时可能并不像错误的错误”。因为追溯到2000年的SQLite源代码，当时系统主要是32位架构"。

> 参考来源：https://securityaffairs.co/wordpress/137629/hacking/cve-2022-35737-sqlite-bug.html

# 资讯 # 漏洞 # 网络安全 # 数据安全 # 漏洞分析

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