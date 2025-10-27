---
title: 又一全新恶意软件曝光！专门针对Windows、Linux 和 macOS 用户
url: https://www.freebuf.com/news/409418.html
source: FreeBuf网络安全行业门户
date: 2024-08-27
fetch_date: 2025-10-06T18:06:07.819228
---

# 又一全新恶意软件曝光！专门针对Windows、Linux 和 macOS 用户

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

又一全新恶意软件曝光！专门针对Windows、Linux 和 macOS 用户

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

又一全新恶意软件曝光！专门针对Windows、Linux 和 macOS 用户

2024-08-26 10:20:17

所属地 上海

![1724657536_66cc2f802c842c488f6b9.png!small?1724657537821](https://image.3001.net/images/20240826/1724657536_66cc2f802c842c488f6b9.png!small?1724657537821)

近日，网络安全研究人员发现了一个利用 “Cheana Stealer ”恶意软件的复杂网络钓鱼活动，该恶意软件是通过一个 VPN 钓鱼网站传播的。这次攻击的主要目标是各种操作系统的用户，包括 Windows、Linux 和 macOS。

Cheana Stealer 活动是通过一个虚假的 VPN 提供商的钓鱼网站实施的。该网站模仿 WarpVPN 服务的外观，专门设计用于引诱个人下载不同操作系统的 VPN 应用程序。

攻击者为每个目标操作系统制作了不同的 Cheana 窃取程序二进制文件，展示了他们最大限度地扩大影响范围的努力。

## Cheana 窃取程序活动概述

据 Cyble 研究与情报实验室（CRIL）称，Cheana Stealer 恶意软件通过不同的方法针对多个操作系统的用户。在 Windows 系统中，恶意软件通过 PowerShell 脚本发送，该脚本会执行一个名为 install.bat 的批处理文件。

![1724639355_66cbe87b473f22a9416b0.png!small](https://image.3001.net/images/20240826/1724639355_66cbe87b473f22a9416b0.png!small)

Windows 安装说明（来源：Cyble）

该脚本首先会检查受害者系统中是否存在 Python，如果未找到，则会安装 Python 以及 pip 和 virtualenv 等工具。

然后再安装一个名为 hclockify-win 的恶意 Python 软件包，目的是窃取敏感信息。该软件包以加密货币浏览器扩展和独立钱包为目标，将窃取的数据压缩成 ZIP 文件，发送到攻击者的命令和控制 (C&C) 服务器。此外，它还会从基于 Chromium 的浏览器和火狐浏览器中提取存储的浏览器密码。

在 Linux 系统上，Cheana 窃取程序通过 curl 命令分发，该命令可下载名为 install-linux.sh 的脚本。![1724639375_66cbe88f9f3f24c0d7843.png!small](https://image.3001.net/images/20240826/1724639375_66cbe88f9f3f24c0d7843.png!small)

Linux 安装说明（来源：Cyble）

该脚本会检索一个用于跟踪的唯一 ID，并收集敏感信息，包括浏览器数据、加密货币钱包详情和 SSH 密钥，然后将这些信息外泄到攻击者的服务器上。

对于 macOS 用户，恶意软件通过名为 install.sh 的脚本分发。

![1724639401_66cbe8a99369714e5963b.png!small](https://image.3001.net/images/20240826/1724639401_66cbe8a99369714e5963b.png!small)

MacOS 安装说明（来源：Cyble）

该脚本通过虚假提示欺骗用户输入凭证，然后收集浏览器登录数据、macOS 密码和钥匙串信息。这些详细信息随后会被发送到 C&C 服务器。

在所有平台上，Cheana Stealer 都是利用系统漏洞和用户信任来窃取敏感信息的，这凸显了采取更好的安全措施的必要性。

## Telegram 频道的作用和技术分析

![Cheana Stealer Campaign](https://image.3001.net/images/20200701/1593550745.png!small)

Telegram 配置文件更改（来源：Cyble）

与 “Cheana Stealer ”活动相关的钓鱼网站连接在一个拥有 54000 多名用户的 Telegram 频道账户上。据悉，该频道从 2018 年起就比较活跃，期间运营商经历了数次变更，钓鱼网站于 2021 年被添加到其简介中。在开始传播 Cheana 偷窃器之前，该频道在传播恶意内容和赢得用户信任方面发挥了重要作用。

Telegram 频道最初提供看似免费的 VPN 服务，并利用这一“幌子” 建立了一定的信誉。不过在建立用户群之后，该频道就会立即开始推广钓鱼网站，利用获得的信任传播恶意软件。

Cheana Stealer 活动采用了精心设计的技术策略。钓鱼网站冒充 WarpVPN，为各种操作系统提供详细但具有欺骗性的安装说明。

![Cheana Stealer](https://image.3001.net/images/20200701/1593550745.png!small)

2021 年的 Warpvpn 网站（来源：Cyble）

这些说明会引导用户安装伪装成合法应用程序的恶意软件。

恶意软件是为 Windows、Linux 和 macOS 定制的，每个版本都旨在提取特定的敏感数据。它能顺利集成到受害者的系统中，确保有效收集数据。

一旦收集到数据，窃取的数据就会被存档，并通过 HTTPS 发送到攻击者的服务器，从而在传输过程中确保数据安全，增加检测难度。这种复杂的方法凸显了用户保持警惕和采用强大安全措施的必要性。

## 缓解策略

为防范类似 Cheana Stealer 活动的网络钓鱼攻击，用户应遵循几项关键建议：

首先，始终从信誉良好的来源下载 VPN 应用程序和其他软件，以避免恶意版本。宣传活动可以帮助用户识别网络钓鱼企图并验证 VPN 服务的合法性。

此外，部署先进的端点保护解决方案有助于检测和阻止恶意脚本。定期更新这些工具对保持其有效性至关重要。使用安全工具监控网络流量可以防止与已知的命令和控制服务器通信，从而增加另一层防御。启用多因素身份验证（MFA）提供了一个额外的安全层，即使凭证被泄露，也能降低未经授权访问的风险。

同时，制定完善的事件响应计划也至关重要。该计划应定期更新，以便迅速处理和管理恶意软件感染。Cheana Stealer 活动是一种复杂的网络钓鱼攻击，它通过伪装成合法的 VPN 服务来利用用户的信任。

针对不同操作系统使用定制的恶意软件以及策略性地使用 Telegram 频道凸显了该活动的复杂性。

> 参考来源：[Researchers Reveals Cheana Stealer Campaign Targeting Users (thecyberexpress.com)﻿](https://thecyberexpress.com/cheana-stealer-campaign/)

# 网络钓鱼

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

Cheana 窃取程序活动概述

Telegram 频道的作用和技术分析

缓解策略

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