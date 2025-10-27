---
title: Microsoft 365 全球宕机5小时，竟是路由器的锅
url: https://www.freebuf.com/news/355988.html
source: FreeBuf网络安全行业门户
date: 2023-01-31
fetch_date: 2025-10-04T05:14:11.925510
---

# Microsoft 365 全球宕机5小时，竟是路由器的锅

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

Microsoft 365 全球宕机5小时，竟是路由器的锅

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Microsoft 365 全球宕机5小时，竟是路由器的锅

2023-01-30 13:08:38

所属地 河南省

Bleeping Computer 网站披露，长达五小时的 Microsoft 365 全球中断是一个路由器 IP 地址变化，致其广域网（WAN）中所有其它路由器之间的数据包转发问题引起。![1675055352_63d750f8ae8b0a9f79781.png!small?1675055353308](https://image.3001.net/images/20230130/1675055352_63d750f8ae8b0a9f79781.png!small?1675055353308)

2023 年 1 月 25日，Microsoft Teams、Outlook、Xbox 和其它 Microsoft365 服务均出现不同程度中断、延迟的现象，主要影响亚洲和欧洲用户，引起业内广泛关注。微软接到客户报告后立刻展开调查，并组织技术专家修复程序，排除故障以使服务恢复在线。

随着事故发展，微软 365 团队在社交媒体上表示其发现一个潜在网络问题，并正在审查遥测技术以确定下一步的故障排除步骤。目前，微软已将服务中断问题与网络配置问题隔离开来，正在分析解决这些问题的最佳缓解策略，力争不会造成额外影响。

## ****微软多个服务受到********中断影响****

根据 Redmond 的说法，受影响用户可能无法访问有问题的 Microsoft 365 服务。**此次中断影响的服务清单主要包括:**

> Microsoft Teams、Exchange Online、Outlook、SharePoint Online、OneDrive for Business、PowerBi、Microsoft 365 Admin Center、Microsoft Graph、Microsoft Intune、Microsoft Defender for Cloud Apps和Microsoft Defender for Identity。

Azure 团队在 Microsoft Azure 服务状态页上强调，技术团队已经确定网络连接问题发生在微软广域网（WAN）设备上，这主要影响到互联网客户与 Azure 之间的连接、ExpressRoute 连接以及数据中心服务之间的连接。

服务器中断问题正在造成一波波影响，大约每 30 分钟达到峰值。此外，一些客户在加载 Microsoft Azure 状态页面时同样会遇到问题，该页面间歇性显示“504网关超时”错误。目前微软内部技术团队正在展开积极调查，一旦有更多消息，会立刻分享给大众。![1675055366_63d751061a04bab37eb3a.png!small?1675055366352](https://image.3001.net/images/20230130/1675055366_63d751061a04bab37eb3a.png!small?1675055366352)

随着调查深入，Azure 团队发现此次故障背后的根本原因是微软广域网（WAN）的近期更新，目前微软已采取措施回滚这一更新。值得一提的是，微软强调最新遥测显示多个地区和服务都有恢复的迹象，正在继续积极监测，可以确认受影响的服务已经开始慢慢恢复并保持稳定。

## ****Microsoft 365 全球中断由********某********个路由器 IP 变化********引起****

经调查分析，微软最后确认长达五小时的 Microsoft 365 全球中断是路由器 IP 地址更改所致，该更改引起了其广域网（WAN）中所有其它路由器之间的数据包转发问题。

Redmond 对事件调查后表示全球性中断是由 WAN 更新导致的 DNS 和 WAN 网络配置问题造成的，许多用户在访问受影响的 Microsoft 365 服务时都遇到了问题。微软透露，服务器中断问题是在使用未经彻底审查的命令更改 WAN 路由器的 IP 地址时引发的，该命令在不同网络设备上具有不同的行为。作为更新 WAN 路由器上 IP 地址的计划更改的一部分，向路由器发出的命令使其向 WAN 中的所有其它由器发送消息，这导致所有路由器重新计算其邻接表和转发表。

在重新计算过程中，路由器无法正确转发通过它们的数据包 当网络从 UTC 08:10 开始自行恢复时，负责维护广域网（WAN）运行状况的自动化系统由于网络受到影响而暂停。这些系统包括识别和消除不健康设备的系统，以及优化网络数据流的流量工程系统。

由于暂停，一些网络路径从 UTC 9 时 35 分开始继续“历经”数据包丢失增加，直到手动重新启动系统，使WAN 恢复到最佳运行状态，并在 UTC 12 时 43 分完成恢复过程。![1675055383_63d7511744338b045316e.png!small?1675055383749](https://image.3001.net/images/20230130/1675055383_63d7511744338b045316e.png!small?1675055383749)

特别强调的是，从 UTC 上午 7:05 开始调查，到 UTC 下午 12:43 恢复服务，Redmond 仅花费五个多小时就解决了服务中断问题。

服务器中断事件后，微软表示正在阻止执行具有高度影响力的命令，并且还将要求所有命令执行都遵循安全配置更改的指导原则。

**参考文章：**

> https://www.bleepingcomputer.com/news/microsoft/microsoft-365-outage-takes-down-teams-exchange-online-outlook/
>
> https://www.bleepingcomputer.com/news/microsoft/massive-microsoft-365-outage-caused-by-wan-router-ip-change/

# 微软

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

微软多个服务受到中断影响

Microsoft 365 全球中断由某个路由器 IP 变化引起

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