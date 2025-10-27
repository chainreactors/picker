---
title: 严重漏洞使大量Four-Faith路由器面临远程利用
url: https://www.freebuf.com/news/418819.html
source: FreeBuf网络安全行业门户
date: 2025-01-01
fetch_date: 2025-10-06T20:07:02.038355
---

# 严重漏洞使大量Four-Faith路由器面临远程利用

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

严重漏洞使大量Four-Faith路由器面临远程利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

严重漏洞使大量Four-Faith路由器面临远程利用

2024-12-31 11:10:34

所属地 上海

VulnCheck 发现了一个影响Four-Faith（四信）工业路由器的关键新漏洞，并有证据表明漏洞正在被广泛利用。

![](https://image.3001.net/images/20241231/1735615172_677362c420ed0f046737c.png!small)

据悉，该漏洞是一个操作系统 （OS） 命令注入错误，被追踪为CVE-2024-12856，仅在远程攻击者能够成功验证身份时起作用。但是，如果与路由器关联的默认凭证尚未更改，则可能导致未经身份验证的操作系统命令执行。

在 VulnCheck 详细描述的攻击中，未知的攻击者被发现利用路由器的默认凭据来触发漏洞利用，并启动反向 shell 以实现持久的远程访问。此次利用尝试源自 IP 地址 178.215.238[.]91，该地址此前曾用于 CVE-2019-12168 漏洞攻击，这是另一个影响Four-Faith 路由器的远程代码执行漏洞。根据威胁情报公司 GreyNoise 的数据，截至 2024 年12 月19 日，仍有利用 CVE-2019-12168 的攻击记录。

VulnCheck 研究员雅各布·贝恩斯（Jacob Baines）在一份报告中表示，攻击至少可以使用 /apply.cgi 端点 ，通过 HTTP 针对Four-Faith F3x24 和F3x36 路由器。当通过 submit\_type=adjust\_sys\_time 修改设备的系统时间时，系统容易受到 adj\_time\_year 参数中操作系统命令注入的影响。

成功利用此漏洞后，攻击者可以在路由器上执行远程代码、安装恶意软件、窃取敏感数据、破坏网络操作，并将路由器用作进一步攻击的起点。

Censys 的数据显示，目前有超过 1.5万台暴露于互联网的四信路由器。有证据表明，利用该漏洞的攻击可能至少从 2024 年11 月初就已经开始。

VulnCheck 表示已于 2024 年12 月20 日向厂商报告了漏洞情况，目前还暂无修复补丁发布。

路由器负责引导互联网流量，在安全措施中经常被忽视，因此很容易成为网络犯罪分子的目标。 最近，Censys 在 DrayTek Vigor 路由器中发现了 14 个关键漏洞，包括缓冲区溢出和操作系统命令注入漏洞。 现在，Four-Faith 路由器漏洞的发现进一步表明，需要改进安全措施来进一步保护路由器。

**参考来源：**

> [15,000+ Four-Faith Routers Exposed to New Exploit Due to Default Credentials](https://thehackernews.com/2024/12/15000-four-faith-routers-exposed-to-new.html)

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