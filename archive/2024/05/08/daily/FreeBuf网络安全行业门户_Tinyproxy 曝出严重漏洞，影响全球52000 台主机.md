---
title: Tinyproxy 曝出严重漏洞，影响全球52000 台主机
url: https://www.freebuf.com/news/400126.html
source: FreeBuf网络安全行业门户
date: 2024-05-08
fetch_date: 2025-10-06T17:16:23.341542
---

# Tinyproxy 曝出严重漏洞，影响全球52000 台主机

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

Tinyproxy 曝出严重漏洞，影响全球52000 台主机

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Tinyproxy 曝出严重漏洞，影响全球52000 台主机

2024-05-07 10:16:47

所属地 上海

![1715049448_663993e8e1deed6a74f7f.png!small](https://image.3001.net/images/20240507/1715049448_663993e8e1deed6a74f7f.png!small)

近日，攻击面管理公司 Censys 分享了一组数据：截至 2024 年 5 月 3 日，在90310台主机中，有 52000 台（约占 57%）运行着有漏洞的 Tinyproxy 版本。

这些可能受到漏洞影响的主机分布于美国（32846 台）、韩国（18358 台）、中国（7808 台）、法国（5208 台）和德国（3680 台）。

该漏洞是HTTP/HTTPS代理工具中一个未修补的重要安全漏洞，被追踪为 CVE-2023-49606，CVSS 得分为 9.8，Cisco Talos 将其描述为一个影响 1.10.0 和 1.11.1 版本（即最新版本）的免用漏洞。

Talos在上周的一份报告中提到：攻击者可通过精心构造的HTTP头触发先前释放内存的重复使用，导致内存破坏且可能导致远程代码执行。攻击者需要发送未经身份验证的HTTP请求以触发此漏洞。

换句话说，未经身份验证的威胁行为者可以发送特制的 HTTP 连接头，从而引发内存破坏，导致远程代码执行。

Tinyproxy 是一个轻量级的开源 HTTP 代理守护程序，专注于简单性和效率。根据 HTTP 规范，客户端提供的标头表示代理在最终 HTTP 请求中必须删除的 HTTP 标头列表。代理从请求中删除这些 HTTP 标头，向远程服务器执行请求，并将响应发送回客户端。Tinyproxy 在函数中正是这样做的：

![1715051192_66399ab83c7836e66d96c.png!small](https://image.3001.net/images/20240507/1715051192_66399ab83c7836e66d96c.png!small)

首先，我们应该注意到客户端发送的 HTTP 标头驻留在键值存储中。该代码搜索 和 标头，并在 （1） 处获取它们的值，如前所述，这是一系列要删除的 HTTP 标头。客户端列出的每个 HTTP 标头在 （3） 处被删除。从本质上讲，和 标头值中的每个 HTTP 标头都用作从 中删除的键。最后，在 （4） 处，HTTP 标头本身被删除。

在函数中，我们看到：

![1715051259_66399afbbf6a2ddbdb7f1.png!small](https://image.3001.net/images/20240507/1715051259_66399afbbf6a2ddbdb7f1.png!small)

对于具体提供的，其哈希值计算为 （5）。使用哈希值，在 （6） 处检索并释放键值的指针。最后，键本身从（7）的哈希图中删除。

现在考虑一下当客户端发送 HTTP 标头时会发生什么。出于演示目的，我们将它们区分为。在 （1） 处检索标头的值，这当然是 。在 （3） 处，该值用作 处的变量。在（5）处计算字符串的哈希值，与完全相同。请注意，哈希值也不区分大小写。在 （6） 处，哈希用于检索和释放 HTTP 标头值的指针，即 。因此，此时代码已释放了 的内存。在 （7） 处，现在包含过时指针的变量被重用，从而导致释放后使用方案。

很明显，此漏洞可用于执行内存损坏并获得代码执行权限。

去年 12 月 22 日，塔洛斯公司报告了这一漏洞，并发布了该漏洞的概念验证（PoC），描述了如何利用解析 HTTP 连接的问题来触发崩溃，并在某些情况下执行代码。

Tinyproxy 的维护者在上周末提交的一组文件中，指责 Talos 将报告发送到了一个已经不再使用的电子邮件地址，并补充说他们是在 2024 年 5 月 5 日被 Debian Tinyproxy 软件包维护者发现的。

rofl0r 提到：没有人在 GitHub 上提交问题，也没有人在提及的 IRC 聊天中提到漏洞。如果在 Github 或 IRC 上报告了该问题，该漏洞会在一天内得到修复。该公司建议用户在最新版本发布后及时更新。

> 参考来源：
>
> [Critical Tinyproxy Flaw Opens Over 50,000 Hosts to Remote Code Execution (thehackernews.com)](https://thehackernews.com/2024/05/critical-tinyproxy-flaw-opens-over.html)
>
> <https://talosintelligence.com/vulnerability_reports/TALOS-2023-1889>

# 安全漏洞 # 主机安全

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