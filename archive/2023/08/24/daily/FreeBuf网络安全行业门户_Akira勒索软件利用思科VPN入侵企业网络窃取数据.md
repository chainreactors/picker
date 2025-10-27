---
title: Akira勒索软件利用思科VPN入侵企业网络窃取数据
url: https://www.freebuf.com/news/375848.html
source: FreeBuf网络安全行业门户
date: 2023-08-24
fetch_date: 2025-10-04T12:01:35.771858
---

# Akira勒索软件利用思科VPN入侵企业网络窃取数据

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

Akira勒索软件利用思科VPN入侵企业网络窃取数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Akira勒索软件利用思科VPN入侵企业网络窃取数据

2023-08-23 10:57:10

所属地 上海

![1692757259_64e56d0b95d1054aebf10.png!small?1692757260201](https://image.3001.net/images/20230823/1692757259_64e56d0b95d1054aebf10.png!small?1692757260201)

最近，有越来越多的证据表明Akira勒索软件以思科VPN产品为攻击目标，入侵企业网络、窃取并最终加密数据。

Akira勒索软件是2023年3月推出勒索软件，该组织后来增加了一个Linux加密器，以VMware ESXi虚拟机为目标。

思科 VPN 解决方案被许多行业广泛采用，在用户和企业网络之间提供安全、加密的数据传输，通常供远程工作的员工使用。

据报道，Akira经常利用被攻破的思科 VPN 账户入侵企业网络，而不需要投放额外的后门或设置可能泄露的持久性机制。

## Akira 的目标是思科 VPN

Sophos 在 5 月份首次注意到 Akira 滥用 VPN 账户的情况，当时研究人员指出，勒索软件团伙使用 "单因素身份验证的 VPN 访问 "入侵了一个网络。

一个名为 "Aura "的事件响应者在 Twitter 上分享了关于入侵活动的更多信息，介绍了他们是如何应对多个 Akira 事件的，这些事件都是使用未受多因素身份验证保护的思科 VPN 账户实施的。

![1692759159_64e57477b7598cee4d75e.png!small?1692759159638](https://image.3001.net/images/20230823/1692759159_64e57477b7598cee4d75e.png!small?1692759159638)

在与 BleepingComputer 的对话中，Aura 表示，由于思科 ASA 缺乏日志记录，所以并尚不清楚 Akira 是通过暴力破解获得 VPN 帐户凭据，还是在暗网市场上购买的。

SentinelOne WatchTower 与 BleepingComputer 私下共享的一份报告也聚焦于相同的攻击方法，报告指出 Akira 可能利用了思科 VPN 软件中的一个未知漏洞，在没有 MFA 的情况下绕过了身份验证。

SentinelOne 在该团伙勒索页面上发布的泄露数据中发现了 Akira 使用思科 VPN 网关的证据，并在至少 8 个案例中观察到了思科 VPN 相关特征，表明这是勒索软件团伙持续攻击策略的一部分。

![1692759211_64e574ab5c48d23da9c41.png!small?1692759211222](https://image.3001.net/images/20230823/1692759211_64e574ab5c48d23da9c41.png!small?1692759211222)

在八起 "Akira "攻击中发现思科VPN特征  图源：SentinelOne SentinelOne

## 远程访问 RustDesk

此外，SentinelOne WatchTower 的分析师还观察到 Akira 使用 RustDesk 开源远程访问工具来浏览被入侵的网络，这是已知的第一个滥用该软件的勒索软件组织。

由于 RustDesk 是一个合法工具，不会引起任何警报，因此它可以隐蔽地远程访问被入侵的计算机。

使用 RustDesk 带来的好处包括：

* 可在 Windows、macOS 和 Linux 上跨平台运行，覆盖 Akira 的全部目标范围
* P2P 连接经过加密，因此不太可能被网络流量监控工具标记
* 支持文件传输，有助于数据外渗，从而简化了 Akira 的工具包
* SentinelOne 在 Akira 的最新攻击中观察到的其他 TTP 包括 SQL 数据库访问和操作、禁用防火墙和
* 启用 RDP、禁用 LSA 保护和禁用 Windows Defender

2023 年 6 月底，Avast 发布了针对 Akira 勒索软件的免费解密程序。但从那之后威胁者已经给加密程序打了补丁，Avast 的工具只能帮助那些旧版本的受害者。

> 参考来源：[Akira ransomware targets Cisco VPNs to breach organizations (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/akira-ransomware-targets-cisco-vpns-to-breach-organizations/)

# vpn # 思科 # 勒索软件

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

Akira 的目标是思科 VPN

远程访问 RustDesk

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