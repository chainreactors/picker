---
title: 卡巴斯基发布的 EDR 防护杀手，被勒索组织广泛使用
url: https://www.freebuf.com/news/410698.html
source: FreeBuf网络安全行业门户
date: 2024-09-12
fetch_date: 2025-10-06T18:28:24.817128
---

# 卡巴斯基发布的 EDR 防护杀手，被勒索组织广泛使用

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

卡巴斯基发布的 EDR 防护杀手，被勒索组织广泛使用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

卡巴斯基发布的 EDR 防护杀手，被勒索组织广泛使用

2024-09-11 09:42:12

所属地 上海

![ransomware-2.jpg](https://image.3001.net/images/20240911/1726021072_66e0fdd0da9678d8b3592.jpg!small)

近期，RansomHub 勒索组织一直通过利用卡巴斯基的合法工具 TDSSKiller 来禁用目标系统上的端点检测和响应 (EDR) 服务。

在攻破防御系统后，RansomHub 又部署了 LaZagne 凭证采集工具，试图从各种应用程序数据库中提取有助于在网络上横向移动的登录信息。

## 在勒索软件攻击中滥用 TDSSKiller

卡巴斯基创建的 TDSSKiller 是一种可以扫描系统是否存在 rootkit 和 bootkit 的工具，这两种恶意软件特别难以检测，而且可以躲避标准的安全工具。

EDR代理是更先进的解决方案，它们至少部分在内核级别上运行，以便监控和控制如文件访问、进程创建和网络连接等低级系统活动，从而提供针对勒索软件等威胁的实时保护。

网络安全公司 Malwarebytes 报告称，他们最近观察到 RansomHub 勒索组织滥用 TDSSKiller，使用命令行脚本或批处理文件与内核级服务交互，从而禁用机器上运行的 Malwarebytes 反恶意软件服务（MBAMService）。

![1726018851_66e0f523dae9b8729103d.png!small](https://image.3001.net/images/20240911/1726018851_66e0f523dae9b8729103d.png!small)

TDSSKiller 支持的命令参数  来源：Malwarebytes

该合法工具是在侦察和权限升级阶段之后使用的，并使用动态生成的文件名（'{89BCFDFB-BBAF-4631-9E8C-P98AB539AC}.exe'）从临时目录（'C:\Users\<User>\AppData\Local\Temp\' ）执行。

作为一个签署了有效证书的合法工具，TDSSKiller 不存在 RansomHub 的攻击被安全解决方案标记或阻止的风险。

接下来，RansomHub 会使用 LaZagne 工具提取存储在数据库中的凭据。 在 Malwarebytes 调查的此次攻击事件中，该工具生成了 60 次文件写入，这些文件可能是被盗凭证的日志。删除文件的操作可能是攻击者试图掩盖其在系统中的活动的结果。

## 防御 TDSSKiller

大多数安全工具都能直接标记LaZagne为恶意软件，因此检测它并不复杂。但如果利用TDSSKiller来禁用安全防护，LaZagne的活动就可能隐蔽起来。TDSSKiller本身处于一个灰色地带，一些安全工具，包括Malwarebytes的ThreatDown，将其归类为“RiskWare”，这可能向用户暗示了潜在的风险。

为了安全起见，建议启用EDR解决方案中的防篡改保护功能，以防止攻击者利用类似TDSSKiller的工具来禁用安全措施。同时，通过监控“-dcsvc”这一禁用或删除服务的参数，以及TDSSKiller的执行情况，可以更有效地检测和阻断恶意行为。

> 参考来源：[RansomHub ransomware abuses Kaspersky TDSSKiller to disable EDR software](https://www.bleepingcomputer.com/news/security/ransomhub-ransomware-abuses-kaspersky-tdsskiller-to-disable-edr-software/)

# 卡巴斯基 # 勒索软件

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

在勒索软件攻击中滥用 TDSSKiller

防御 TDSSKiller

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