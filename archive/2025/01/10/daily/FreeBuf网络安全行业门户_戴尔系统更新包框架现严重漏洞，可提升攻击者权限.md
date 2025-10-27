---
title: 戴尔系统更新包框架现严重漏洞，可提升攻击者权限
url: https://www.freebuf.com/news/419366.html
source: FreeBuf网络安全行业门户
date: 2025-01-10
fetch_date: 2025-10-06T20:08:37.126077
---

# 戴尔系统更新包框架现严重漏洞，可提升攻击者权限

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

戴尔系统更新包框架现严重漏洞，可提升攻击者权限

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

戴尔系统更新包框架现严重漏洞，可提升攻击者权限

2025-01-09 13:37:34

所属地 上海

据Cyber Security News消息，戴尔（Dell）电脑的系统更新包 （DUP） 框架被发现一个严重安全漏洞，可能会使系统面临来自攻击者的权限提升和拒绝服务攻击。

![](https://image.3001.net/images/20250109/1736401122_677f60e234920fb69cc7f.jpg!small)

该漏洞被跟踪为 CVE-2025-22395，CVSS评分8.2，影响 22.01.02 之前的 DUP 框架版本，允许具有低权限的本地攻击者利用该框架在服务器上执行任意远程脚本，从而导致未经授权的系统访问、服务中断以及敏感数据的潜在泄露。

戴尔已承认该问题，但尚未披露有关利用过程的具体技术细节。安全专家强调，此漏洞可能会对依赖戴尔 BIOS、固件和驱动程序更新更新机制的企业组织设备产生重大影响。

戴尔已发布 DUP 框架的更新版本 （22.01.02）来解决此问题。强烈建议用户更新到此版本或更高版本，以降低与 CVE-2025-22395 漏洞相关的风险。

对于仍在运行受影响版本的系统，戴尔建议避免在 Microsoft Windows 环境中使用“Extract”选项。

## **临时解决方法**

* 暂时禁用自动更新，直到系统得到修补。
* 增强网络分段以限制攻击媒介。
* 监控系统中可能存在可能表明漏洞利用企图的可疑活动。

Dell Update Package Framework 在戴尔生态系统中广泛使用，以简化 BIOS、固件和设备驱动程序的更新。因此，如果不进行修补，该漏洞可能会影响广泛的 Dell 系统。

使用戴尔系统的企业组织应从 官方支持页面下载最新的 DUP 框架，以立即优先修补其环境。此外，还建议安全团队实施强大的监控工具，并遵循戴尔关于安全处理更新包的指导。

戴尔已将报告此问题归功于 Gee-metrics，并继续与其客户密切合作以确保系统安全。

随着网络威胁的发展，及时采取行动对于缓解 CVE-2025-22395 等漏洞至关重要。组织必须通过维护最新的软件和遵守推荐的安全实践来保持警惕。

**参考来源：**

> [Dell Update Package Framework Vulnerability Let Attackers Escalate Privileges](https://cybersecuritynews.com/dell-update-vulnerability/)

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

文章目录

临时解决方法

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