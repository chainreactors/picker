---
title: 420万主机暴露，含VPN和路由器
url: https://www.freebuf.com/news/420386.html
source: FreeBuf网络安全行业门户
date: 2025-01-22
fetch_date: 2025-10-06T20:09:28.107034
---

# 420万主机暴露，含VPN和路由器

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

420万主机暴露，含VPN和路由器

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

420万主机暴露，含VPN和路由器

2025-01-21 11:17:38

所属地 上海

## 新研究表明，多种隧道协议存在安全漏洞，这些漏洞可能让攻击者实施多种攻击。

一项研究表明：“网络主机若接受隧道数据包却不验证发送者身份，就可能被劫持以执行匿名攻击并获得对其网络的访问权限。”该研究是与鲁汶大学（KU Leuven）的教授兼研究员马蒂·范霍夫（Mathy Vanhoef）合作开展的。

![](https://image.3001.net/images/20250121/1737429437_678f11bd8c157b9068753.png!small)

研究发现，多达420万台主机易受攻击，其中包括VPN、互联网服务提供商（ISP）的家庭路由器、核心互联网路由器、移动网络网关以及内容分发网络（CDN）节点。中国、法国、日本、美国和巴西是受影响最为严重的国家。

成功利用这些漏洞可能使攻击者滥用易受攻击的系统充当单向代理，并发动拒绝服务（DoS）攻击。

CERT协调中心（CERT/CC）在一份咨询报告中称：“攻击者可滥用这些安全漏洞创建单向代理并伪造源IPv4/6地址。易受攻击的系统还可能允许访问组织的私有网络，或者被滥用以发动DDoS攻击。”

这些漏洞产生的根源在于，像IP6IP6、GRE6、4in6和6in4等隧道协议主要用于促进两个断开连接的网络之间的数据传输，但在缺乏诸如互联网协议安全（IPsec）这类足够的安全协议时，不会对流量进行身份验证和加密。

缺乏额外的安全防护措施，就给攻击者将恶意流量注入隧道打开了方便之门，这是2020年曾被标记过的一个漏洞（CVE - 2020 - 10136）的变体。

这些协议已被分配以下CVE编号：

> - CVE - 2024 - 7595（GRE和GRE6）
>
> - CVE - 2024 - 7596（通用UDP封装）
>
> - CVE - 2025 - 23018（IPv4 - in - IPv6和IPv6 - in - IPv6）
>
> - CVE - 2025 - 23019（IPv6 - in - IPv4）

西蒙·米利亚诺（Simon Migliano）解释道：“攻击者只需发送一个使用受影响协议之一封装的数据包，该数据包包含两个IP头。外部头包含攻击者的源IP，目标是易受攻击主机的IP；内部头的源IP是易受攻击主机的IP，而非攻击者的IP，目标IP是匿名攻击的目标IP。”

所以，当易受攻击的主机接收到恶意数据包时，会自动剥离外部IP地址头，并将内部数据包转发到目的地。由于内部数据包上的源IP地址是易受攻击但被信任的主机的IP地址，所以它能绕过网络过滤器。

作为防御措施，建议使用IPSec或WireGuard来提供身份验证和加密，并且只接受来自可信源的隧道数据包。在网络层面，还建议在路由器和中间设备上实施流量过滤、深度包检查（DPI），并阻止所有未加密的隧道数据包。

米利亚诺表示：“这些DoS攻击对受害者造成的影响可能包括网络拥塞、因流量过载消耗资源而导致的服务中断，以及网络设备因过载而崩溃。这也为进一步的攻击创造了机会，例如中间人攻击和数据拦截。”

参考来源：<https://thehackernews.com/2025/01/unsecured-tunneling-protocols-expose-42.html>

# 漏洞 # 安全漏洞

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

新研究表明，多种隧道协议存在安全漏洞，这些漏洞可能让攻击者实施多种攻击。

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