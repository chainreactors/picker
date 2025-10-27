---
title: Veeam曝出关键漏洞，勒索团伙趁火打劫利用RCE攻击全球企业
url: https://www.freebuf.com/news/412525.html
source: FreeBuf网络安全行业门户
date: 2024-10-12
fetch_date: 2025-10-06T18:52:29.902655
---

# Veeam曝出关键漏洞，勒索团伙趁火打劫利用RCE攻击全球企业

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

Veeam曝出关键漏洞，勒索团伙趁火打劫利用RCE攻击全球企业

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Veeam曝出关键漏洞，勒索团伙趁火打劫利用RCE攻击全球企业

2024-10-11 10:20:14

所属地 上海

![](https://image.3001.net/images/20241011/1728616198_67089706600749eb54f1d.png!small)

勒索软件团伙现在利用一个关键的安全漏洞，让攻击者在易受攻击的 Veeam Backup & Replication (VBR) 服务器上获得远程代码执行 (RCE)。

Code White安全研究员Florian Hauser发现，该安全漏洞（现在被追踪为CVE-2024-40711）是由未受信任数据的反序列化弱点引起的，未经认证的威胁行为者可以利用该漏洞进行低复杂度攻击。

Veeam 于 9 月 4 日披露了该漏洞并发布了安全更新，而 watchTowr Labs 则于 9 月 9 日发布了一份技术分析报告。不过，watchTowr Labs 将概念验证利用代码的发布时间推迟到了 9 月 15 日，以便管理员有足够的时间确保服务器安全。

企业将 Veeam 的 VBR 软件作为数据保护和灾难恢复解决方案，用于备份、恢复和复制虚拟机、物理机和云计算机，从而导致了这一延迟。这也使其成为恶意行为者寻求快速访问公司备份数据的热门攻击目标。

![1728613175_67088b372761266b2cd0b.png!small](https://image.3001.net/images/20241011/1728613175_67088b372761266b2cd0b.png!small)

正如 Sophos X-Ops 事件响应人员在上个月发现的那样，CVE-2024-40711 RCE 漏洞很快被发现，并在 Akira 和 Fog 勒索软件攻击中被利用，与之前泄露的凭证一起，向本地管理员和远程桌面用户组添加“点”本地帐户。

在一个案例中，攻击者投放了Fog勒索软件。同一时间段的另一起攻击则试图部署 Akira 勒索软件。Sophos X-Ops表示：所有4起案件中的迹象都与早期的Akira和Fog勒索软件攻击重叠。

在每起案件中，攻击者最初都是使用未启用多因素身份验证的受损 VPN 网关访问目标。其中一些 VPN 运行的是不支持的软件版本。

在Fog勒索软件事件中，攻击者将其部署到未受保护的Hyper-V服务器上，然后使用实用程序rclone外泄数据。

## 这并非勒索软件攻击针对的首个Veeam漏洞

去年，即 2023 年 3 月 7 日，Veeam 还修补了备份与复制软件中的一个高严重性漏洞（CVE-2023-27532），该漏洞可被利用来入侵备份基础架构主机。

几周后的3月下旬，芬兰网络安全和隐私公司WithSecure发现CVE-2023-27532漏洞部署在与FIN7威胁组织有关的攻击中，FIN7威胁组织因与Conti、REvil、Maze、Egregor和BlackBasta勒索软件行动有关而闻名。

几个月后，同样的Veeam VBR漏洞被用于古巴针对美国关键基础设施和拉美IT公司的勒索软件攻击。

Veeam表示，其产品已被全球超过55万家客户使用，其中包括至少74%的全球2000强企业。

> 参考来源：[Akira and Fog ransomware now exploit critical Veeam RCE flaw (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/akira-and-fog-ransomware-now-exploiting-critical-veeam-rce-flaw/)

# 安全漏洞 # 网络攻击

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

这并非勒索软件攻击针对的首个Veeam漏洞

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