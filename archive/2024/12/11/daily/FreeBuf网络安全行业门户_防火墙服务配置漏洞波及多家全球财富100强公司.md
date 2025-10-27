---
title: 防火墙服务配置漏洞波及多家全球财富100强公司
url: https://www.freebuf.com/news/417317.html
source: FreeBuf网络安全行业门户
date: 2024-12-11
fetch_date: 2025-10-06T19:41:00.301252
---

# 防火墙服务配置漏洞波及多家全球财富100强公司

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

防火墙服务配置漏洞波及多家全球财富100强公司

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

防火墙服务配置漏洞波及多家全球财富100强公司

2024-12-10 11:27:49

所属地 上海

据Cyber Security News消息，网络安全研究团队 Zafran 最近在 Web 应用程序防火墙 （WAF） 服务配置中发现了一个被称为“BreakingWAF”的安全漏洞，该漏洞容易让许多财富 100强、1000强的公司受到网络攻击。

![](https://image.3001.net/images/20241210/1733808271_6757d08fbfb609dd25bcd.jpg!small)

该漏洞影响到一些最主流的 WAF 提供商，包括 Akamai、Cloudflare、Fastly 和 Imperva，并极有可能导致拒绝服务（DoS）攻击、勒索软件攻击，甚至是全面的应用程序入侵。

研究人员发现，漏洞导致的错误配置影响了涉及财富1000强公司相关的14多万个域。其中，3.6万个后端服务器有 8000 个域名与之相连，这些对潜在的攻击者开放，容易受到 DDoS 攻击。

根据分析，有近 40% 的 "财富 100 强 "企业和 20%  "财富 1000 强 "企业都受到了影响，这凸显了错误配置的普遍性。 一些全球知名企业，包括摩根大通、Visa、英特尔、伯克希尔·哈撒韦和联合健康等，都被发现受到了影响。比如，例如，研究团队的发现迅速披露了直接影响摩根大通主网站 chase.com 的问题；对伯克希尔·哈撒韦子公司 BHHC 拥有的一个网域进行的 20 秒钟拒绝服务攻击试验，展示了该漏洞的严重性。

根据 Zafran 的技术分析，缺陷在于现今 WAF 提供商的双重功能，它们也作为内容交付网络 (CDN) 运行，以增强网络可靠性和缓存。当后端服务器不能正确检查流量时，这种架构设计就会出现漏洞，让攻击者绕过 WAF 保护，直接攻击后端基础设施。比如，攻击者可以通过将外部域映射到后端 IP 地址来利用这一漏洞。

这一发现凸显了 WAF/CDN 解决方案在设计和实施过程中存在的系统性缺陷。 有效的 WAF 通常是面向公众的网络应用程序的主要或唯一防御层，因此这种错误配置尤其令人担忧。

最近的趋势表明，攻击者越来越多地瞄准配置不佳的网络应用程序。  此外，针对暴露在外的网络应用程序的云勒索软件攻击也越来越常见。 此类攻击造成的经济损失通常十分惊人，例如，一次持续一小时的 DDoS 攻击会给金融组织造成大约 180 万美元的损失，而类似的宕机时间给大型披萨连锁店造成的损失可能高达 190 万美元。

## 缓解措施

为了防范与这种 WAF 错误配置相关的风险，Zafran 概述了几种缓解策略：

* IP 白名单（源 IP 访问控制列表）： 只允许 CDN 提供商的 IP 地址访问后端服务器。 这种方法虽然简单，但并非万无一失；
* 自定义标头中的预共享密钥： 使用带有预共享密钥的自定义 HTTP 标头来验证流量。 虽然短期内有效，但这需要定期轮换密钥；
* 双向TLS（mTLS）：采用客户端认证来验证服务器和 CDN。 这是最安全的方法，但需要专门的工具，可能并非所有常用的负载均衡器都支持这些工具。

Zafran 从 2024 年 8 月 23 日开始启动了为期 90 天的协调披露流程，以通知受影响的公司。该团队向 Visa、英特尔、摩根大通、伯克希尔·哈撒韦公司的 BHHC 和联合健康报告了该漏洞。值得注意的是，摩根大通和联合健康已经解决了这个问题，防止了潜在的漏洞利用。

**参考来源：**

> [WAF Vulnerability in Akamai, Cloudflare, and Imperva Affected 40% of Fortune 100 Companies](https://cybersecuritynews.com/waf-vulnerability-in-akamai-cloudflare-and-imperva/)

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

缓解措施

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