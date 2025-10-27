---
title: Windows TCP IP RCE漏洞曝光，影响所有启用IPv6的系统
url: https://www.freebuf.com/news/408681.html
source: FreeBuf网络安全行业门户
date: 2024-08-16
fetch_date: 2025-10-06T18:03:52.770072
---

# Windows TCP IP RCE漏洞曝光，影响所有启用IPv6的系统

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

Windows TCP IP RCE漏洞曝光，影响所有启用IPv6的系统

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Windows TCP IP RCE漏洞曝光，影响所有启用IPv6的系统

2024-08-15 11:08:25

所属地 上海

本周二（8月13日），微软警告客户立即修补一个严重的TCP/IP远程代码执行（RCE）漏洞，该漏洞被利用的可能性增加，会影响所有使用默认启用IPv6的Windows系统。

![](https://image.3001.net/images/20240815/1723691425_66bd71a1e37ce71dd8b84.png!small)该安全漏洞由昆仑实验室的研究人员发现，并被追踪为CVE-2024-38063，它是由整数下溢漏洞引起的，攻击者可以利用该漏洞触发缓冲区溢出，从而在易受攻击的Windows 10、Windows 11和Windows Server系统中执行任意代码。

“考虑到它的危害性，短期内我不会披露更多细节。"这位安全研究员在推特上补充说，在本地Windows防火墙上阻止IPv6并不能阻止漏洞的利用，因为漏洞在被防火墙处理之前就被触发了。

正如微软在其周二的公告中解释的那样，未经身份验证的攻击者可以通过重复发送包含特制的IPv6数据包，在低复杂性攻击中远程利用该漏洞。

微软还分享了对这一关键漏洞的可利用性评估，将其标记为 “更有可能被利用”，这意味着威胁行为者可以创建利用代码，“在攻击中持续利用该漏洞”。

此外，过去曾有此类漏洞被利用的实例，这使得它成为攻击者的理想目标，更有可能被开发出相应的利用手段。

对于已经审查过安全更新并确定其在环境中适用性的客户应将此作为更高的优先级来对待。而那些无法立即安装本周 Windows 安全更新的用户，微软建议禁用 IPv6 以消除攻击面，作为一种缓解措施。

不过，IPv6网络协议栈是 “Windows Vista和Windows Server 2008及更新版本的强制组成部分”，如果关闭IPv6或其组件，可能会导致某些Windows组件停止工作。

## 可蠕虫漏洞

趋势科技 “零日计划”（Zero Day Initiative）威胁意识主管Dustin Childs也将CVE-2024-38063漏洞列为微软本周“补丁星期二 ”修复的最严重漏洞之一，并将其标记为可蠕虫漏洞。

Childs说："最严重的可能是TCP/IP中的漏洞，它允许远程、未经身份验证的攻击者通过向受影响的目标发送特制的IPv6数据包来获得高级代码执行权限。意味着它是可蠕虫攻击的。你可以禁用IPv6来防止这种漏洞，但IPv6在几乎所有设备上都是默认启用的。”

虽然微软和其他公司警告Windows用户尽快给他们的系统打补丁，以阻止利用CVE-2024-38063漏洞的潜在攻击，但这并不是第一个，也很可能不会是最后一个可利用IPv6数据包的Windows漏洞。

在过去四年中，微软已修补了多个其他 IPv6 问题，包括两个 TCP/IP 漏洞，即 CVE-2020-16898/9（也称为 Ping of Death），这些漏洞可利用恶意 ICMPv6 路由器广告数据包进行远程代码执行（RCE）和拒绝服务（DoS）攻击。

此外，一个 IPv6 分片漏洞（CVE-2021-24086）使所有 Windows 版本容易受到 DoS 攻击，而一个 DHCPv6 漏洞（CVE-2023-28231）使利用特制调用获得 RCE 成为可能。

尽管攻击者尚未利用这些漏洞对所有支持 IPv6 的 Windows 设备进行大范围攻击，但由于 CVE-2024-38063 被利用的可能性增加，建议用户立即应用本月的 Windows 安全更新。

> **参考来源：**https://www.bleepingcomputer.com/news/microsoft/zero-click-windows-tcp-ip-rce-impacts-all-systems-with-ipv6-enabled-patch-now/

# windows # windows漏洞 # Windows系统

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

可蠕虫漏洞

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