---
title: FreeBSD 针对OpenSSH 高危漏洞发布紧急补丁
url: https://www.freebuf.com/news/408448.html
source: FreeBuf网络安全行业门户
date: 2024-08-14
fetch_date: 2025-10-06T18:03:16.296848
---

# FreeBSD 针对OpenSSH 高危漏洞发布紧急补丁

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

FreeBSD 针对OpenSSH 高危漏洞发布紧急补丁

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

FreeBSD 针对OpenSSH 高危漏洞发布紧急补丁

2024-08-13 10:25:24

所属地 上海

![1723517280_66bac960e82289b0be481.png!small](https://image.3001.net/images/20240813/1723517280_66bac960e82289b0be481.png!small)

近日，FreeBSD 项目的维护者针对OpenSSH 高危漏洞发布了紧急补丁。该漏洞被追踪为 CVE-2024-7589，CVSS 得分为 7.4（最高分为 10.0）。通过利用该漏洞，黑客能够在权限提升的情况下远程执行任意代码。

根据上周发布的一份公告，sshd(8) 中的一个信号处理器可能会调用一个不安全的异步信号记录函数。而当客户端未在 LoginGraceTime 秒数（默认为 120 秒）内通过身份验证时，将调用该信号处理程序。该信号处理程序在 sshd(8) 的特权代码上下文中执行，该代码未被沙盒化，并以完全 root 权限运行。

OpenSSH 是安全外壳（SSH）协议套件的实现，为各种服务（包括远程外壳访问）提供加密和验证传输。

CVE-2024-7589 被描述为上月初曝光的 regreSSHion（CVE-2024-6387）问题的 "另一个实例"。项目维护者表示，本例中的错误代码来自 FreeBSD OpenSSH 中 blacklistd 的集成。

由于在有特权的 sshd(8) 上下文中调用的函数不是异步信号安全的，因此存在一个条件，确定的攻击者可能能够利用这个条件以 root 身份执行未经验证的远程代码。因此强烈建议 FreeBSD 用户更新到支持的版本并重启 sshd，以减少潜在威胁。

在无法更新 sshd(8) 的情况下，可以通过在 /etc/ssh/sshd\_config 中将 LoginGraceTime 设置为 0 并重新启动 sshd(8) 来解决竞争条件问题。虽然这一更改使守护进程容易受到拒绝服务的影响，但却能防止远程代码执行。

# 上月曝出的高危漏洞，影响1400万台服务器

今年7月，网络安全公司 Qualys 威胁研究团队公布了 OpenSSH 中的高危远程代码执行漏洞，该漏洞编号为 CVE-2024-6387，扫描显示暴露在公网上的受影响的服务器超过 1400 万台。

值得注意的是此漏洞曾经出现过但在 2006 年被修复，在 2020 年发布的 OpenSSH 新版本中又重新出现了，所以受影响的 OpenSSH 版本略微有些复杂。

**受影响的 OpenSSH 版本：**

* 低于 4.4p1 版 (不含此版本)：受影响
* 高于 4.4p1 但低于 8.5p1 (不含此版本)：不受影响
* 8.5p1 及后续版本到 9.8p1 (不含此版本)：受影响

考虑到 8.5p1 及之前的版本已经非常老旧估计使用量比较低，因此这里可以直接以 8.5p1 版作为分水岭，若系统使用的 OpenSSH 版本为 9.8p1 以下版本那就受到影响，用户应当尽快更新到 9.8p1 及后续版本。

攻击者利用此漏洞实际上可以以最高权限执行任意代码，因此一旦得手就可以获得整个系统和服务器的控制权，无论是安装恶意软件还是窃取数据都是轻轻松松完成。

同时 Qualys 还提到攻击者还可以借助此漏洞获得的权限绕过防火墙、入侵监测系统和日志记录机制等关键安全机制，即可以通过这些方式避免被发现并隐藏其活动。

然而由于该漏洞具有远程竞争条件特性，因此实际利用的话也有难度，攻击者可能需要尝试很多次才可以成功攻击，这会导致内存损坏并且要克服地址空间布局随机化 (ASLR)。

基于以上问题有能力的攻击者可以利用深度学习技术提高漏洞利用率，所以对用户、开发者、企业来说应当尽快检查更新获取 OpenSSH 最新版。

目前已经有部分 Linux 系统开发商推出安全更新修复这一漏洞，如果用户尚未检查到更新请换个时候再次检查更新，尽可能第一时间修复此漏洞。

> 参考来源：
>
> [FreeBSD Releases Urgent Patch for High-Severity OpenSSH Vulnerability](https://thehackernews.com/2024/08/freebsd-releases-urgent-patch-for-high.html)
>
> [https://www.landiannews.com/archives/104739.html](https://www.landiannews.com/archives/104739.html%E3%80%81)

# 安全漏洞 # openssh

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