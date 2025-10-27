---
title: 可导致设备崩溃，MMS协议被曝存在多个安全漏洞
url: https://www.freebuf.com/articles/412425.html
source: FreeBuf网络安全行业门户
date: 2024-10-11
fetch_date: 2025-10-06T18:51:59.608487
---

# 可导致设备崩溃，MMS协议被曝存在多个安全漏洞

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

可导致设备崩溃，MMS协议被曝存在多个安全漏洞

* ![]()
* 关注

可导致设备崩溃，MMS协议被曝存在多个安全漏洞

2024-10-10 11:16:30

所属地 上海

Claroty研究人员发现制造信息规范（MMS）协议中存在多个安全漏洞，一旦被黑客利用，将很有可能会对工业环境中造成严重影响。Claroty研究人员Mashav Sapir和Vera Mens表示，这些漏洞可能允许攻击者使工业设备崩溃，在某些情况下，还能实现远程代码执行。

![](https://image.3001.net/images/20241010/1728530377_670747c9639957479b563.png!small)

MMS是一种用于工业自动化系统中数据通信的标准协议，它定义了一种客户/服务器模型，允许生产设备与上层管理系统进行通信。作为一种更高级别的通信协议，它提供了更丰富的服务和接口。

MMS协议采用面向对象的建模方法，定义了虚拟制造设备（VMD），用于表示实际设备，并通过服务接口进行通信，支持多种数据类型，包括数字、浮点数、字符、时间等。

目前，MMS协议被广泛应用于电力系统、制造业、交通系统等领域，特别是在IEC 61850标准中，被用作变电站自动化系统中设备间通信的基础，其重要性不言而喻。

此前，Claroty公司发现了影响MZ Automation的libIEC61850库和Triangle MicroWorks的TMW IEC 61850库的安全漏洞，这些漏洞在2022年9月和10月报告后已经被修复，具体漏洞信息如下：

* CVE-2022-2970（CVSS评分：10.0）： libIEC61850中的基于栈的缓冲区溢出漏洞，可能导致崩溃或远程代码执行。
* CVE-2022-2971（CVSS评分：8.6）： libIEC61850中的类型混淆漏洞，可能允许攻击者使用恶意负载使服务器崩溃。
* CVE-2022-2972（CVSS评分：10.0）：libIEC61850中的基于栈的缓冲区溢出漏洞，可能导致崩溃或远程代码执行。
* CVE-2022-2973（CVSS评分：8.6）：空指针解引用漏洞，可能允许攻击者使服务器崩溃。
* CVE-2022-38138（CVSS评分：7.5）：未初始化指针的访问漏洞，允许攻击者造成拒绝服务（DoS）条件。

Claroty公司的报告还发现，西门子的 SIPROTEC 5 IED依赖于SISCO的MMS-EASE栈的过时版本来支持MMS，该版本容易受到特制数据包的DoS攻击影响（CVE-2015-6574，CVSS评分：7.5）。但根据CISA发布的报告，西门子早在2022年12就更新了其固件，并使用了更新版本的协议栈。

对此，Claroty公司认为造成上述问题的核心原因是，快速发展技术所需的安全需求与底层过时的、不安全的协议之间的矛盾，这些协议目前存在各种安全风险，且难以马上替换。该公司呼吁供应商们应遵循CISA发布的安全指南，及时更新系统版本。

几周前，Nozomi Networks详细说明了ESP-NOW无线协议中存在的两个漏洞（CVE-2024-42483和CVE-2024-42484），这两个漏洞可能或造成重放攻击和DoS攻击。

Claroty公司进一步表示，"根据被攻击的系统，这个漏洞[CVE-2024-42483]可能会有深远的后果。由于ESP-NOW用于安全系统，其中包括建筑报警，允许它们与运动传感器通信，在这种情况下，攻击者可以利用这个漏洞重放以前截获的合法'OFF'命令，从而随意禁用运动传感器。"

如果ESP-NOW在远程门开启器中的使用，例如自动门和车库门，那么攻击者可以截获合法的"OPEN"命令并实施重放攻击，从而轻松实现以未经授权的方式进入建筑物。

参考来源：<https://thehackernews.com/2024/10/researchers-uncover-major-security.html>

# 系统安全

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