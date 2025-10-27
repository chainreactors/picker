---
title: 新的 Python URL 解析漏洞可能导致命令执行攻击
url: https://www.freebuf.com/news/374733.html
source: FreeBuf网络安全行业门户
date: 2023-08-15
fetch_date: 2025-10-04T12:02:42.193383
---

# 新的 Python URL 解析漏洞可能导致命令执行攻击

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

新的 Python URL 解析漏洞可能导致命令执行攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新的 Python URL 解析漏洞可能导致命令执行攻击

2023-08-14 11:55:29

所属地 上海

![](https://image.3001.net/images/20230814/1691981035_64d994eb597f38efc2e1b.png!small)

Python URL 解析函数中的一个高严重性安全漏洞已被披露，该漏洞可绕过 blocklist 实现的域或协议过滤方法，导致任意文件读取和命令执行。

CERT 协调中心（CERT/CC）在周五的一份公告中说：当整个 URL 都以空白字符开头时，urlparse 就会出现解析问题。"这个问题会影响主机名和方案的解析，最终导致任何拦截列表方法失效"。

该漏洞为 CVE-2023-24329，CVSS 得分为 7.5。安全研究员 Yebo Cao 于 2022 年 8 月发现并报告了该漏洞。该漏洞已在以下版本中得到解决：

* >= 3.12
* 3.11.x >= 3.11.4
* 3.10.x >= 3.10.12
* 3.9.x >= 3.9.17
* 3.8.x >= 3.8.17
* 3.7.x >= 3.7.17

urllib.parse 是一个广泛使用的解析函数，可将 URL 分解为各个组成部分，或将各个组成部分合并为一个 URL 字符串。

CVE-2023-24329 的出现是由于缺乏输入验证，从而导致有可能通过提供以空白字符开头的 URL（例如 " https://youtube[.]com"）来绕过 blocklisting 。

该漏洞可以帮助攻击者绕过主机设置的保护措施，同时在多种场景下助力 SSRF 和 RCE。

> 参考链接：https://thehackernews.com/2023/08/new-python-url-parsing-flaw-enables.html

# 资讯 # 漏洞 # 安全漏洞

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