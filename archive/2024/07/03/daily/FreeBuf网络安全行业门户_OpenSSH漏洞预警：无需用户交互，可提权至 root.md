---
title: OpenSSH漏洞预警：无需用户交互，可提权至 root
url: https://www.freebuf.com/news/404977.html
source: FreeBuf网络安全行业门户
date: 2024-07-03
fetch_date: 2025-10-06T17:43:03.814093
---

# OpenSSH漏洞预警：无需用户交互，可提权至 root

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

OpenSSH漏洞预警：无需用户交互，可提权至 root

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

OpenSSH漏洞预警：无需用户交互，可提权至 root

2024-07-02 11:59:08

所属地 上海

OpenSSH 自 1995 年问世近 20 年来，首次出现了未经验证的远程执行（RCE）漏洞，攻击者可以提权至 root 最高权限，在不需要用户交互的情况下执行任意代码。

OpenSSH 是一套基于 Secure Shell（SSH）协议的网络实用程序，广泛用于安全远程登录、管理远程服务器，通过 scp 或 sftp 备份、远程文件传输等功能。

2024年5月，网络安全公司 Qualys首次发现并报告该漏洞，编号 CVE-2024-6387，存在于 OpenSSH 服务器（sshd）中，由于信号处理器竞赛条件存在缺陷，可以让未经认证的远程攻击者以 root 用户身份执行任意代码。

7 月，网上公开披露了一个 OpenSSH 的远程代码执行漏洞（CVE-2024-6387）。鉴于该漏洞虽然利用较为困难但危害较大，建议所有使用受影响的企业尽快修复该漏洞。

## 漏洞描述

### 漏洞成因

CVE-2024-6387 是 OpenSSH 服务器中的一个严重漏洞，影响基于 glibc 的 Linux 系统。默认配置下的OpenSSH Server (sshd)中存在信号处理程序竞争条件漏洞，如果客户端未在LoginGraceTime 秒内（默认情况下为 120 秒，旧版 OpenSSH 中为 600 秒）进行身份验证，则 sshd 的 SIGALRM 处理程序将被异步调用，但该信号处理程序会调用各种非async-signal-safe的函数（例如syslog()），威胁者可利用该漏洞在基于 glibc 的 Linux 系统上以root 身份实现未经身份验证的远程代码执行。

### 漏洞影响

成功利用该漏洞的攻击者可以以 root 身份进行未经身份验证的远程代码执行 (RCE)。在某些特定版本的 32 位操作系统上，攻击者最短需 6-8 小时即可获得最高权限的 root shell。而在 64 位机器上，目前没有在可接受时间内的利用方案，但未来的改进可能使其成为现实。

* 处置优先级：高
* 漏洞类型：远程代码执行
* 漏洞危害等级：高
* 触发方式：网络远程
* 权限认证要求：无需权限
* 系统配置要求：默认配置可利用
* 用户交互要求：无需用户交互
* 利用成熟度：部分 EXP 已公开（适配单一版本，32 位系统）
* 批量可利用性：可使用通用原理 POC/EXP 进行检测/利用
* 修复复杂度：中，官方提供升级修复方案

### 影响版本

8.5p1 <= OpenSSH < 9.8p1

OpenBSD系统不受该漏洞影响

### 缓解措施

1. 可以在配置文件中将 LoginGraceTime 设置为 0（永不超时）。这样虽然会使 sshd 暴露于拒绝服务攻击（占满所有 Startups 连接），但可以避免远程代码执行风险。
2. 启用 fail2ban 等防护机制，封禁发生过多次失败登录 ssh 尝试的来源 IP。

### 升级修复方案

将 OpenSSH 更新到最新版本 9.8 或者各发行版本的修复版本。

注：资料来源于互联网

# 系统安全 # 数据安全

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

漏洞描述

* 漏洞成因
* 漏洞影响
* 影响版本
* 缓解措施
* 升级修复方案

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