---
title: Gafgyt僵尸网络针对云原生环境，SSH弱密码成GPU挖矿新目标
url: https://www.freebuf.com/news/408781.html
source: FreeBuf网络安全行业门户
date: 2024-08-17
fetch_date: 2025-10-06T18:05:43.779348
---

# Gafgyt僵尸网络针对云原生环境，SSH弱密码成GPU挖矿新目标

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

Gafgyt僵尸网络针对云原生环境，SSH弱密码成GPU挖矿新目标

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Gafgyt僵尸网络针对云原生环境，SSH弱密码成GPU挖矿新目标

2024-08-16 11:27:55

所属地 上海

近日，网络安全研究人员发现了 Gafgyt 僵尸网络的一个新变种，它以 SSH 密码较弱的机器为目标，最终利用其 GPU 计算能力在被攻击的实例上挖掘加密货币。

Aqua Security 研究员 Assaf Morag 在周三的一份分析报告中说："这表明，物联网僵尸网络正在瞄准运行在云原生环境中的更强大的服务器。“

![](https://image.3001.net/images/20240816/1723778657_66bec6618c655f125a6f3.png!small)据了解，Gafgyt（又名 BASHLITE、Lizkebab 和 Torlus）自 2014 年以来一直在野外活跃，它曾利用弱凭据或默认凭据获得路由器、摄像头和数字视频录像机（DVR）等设备的控制权。它还能利用 Dasan、华为、Realtek、SonicWall 和 Zyxel 设备中的已知安全漏洞。

受感染的设备被集中到一个僵尸网络中，能够对感兴趣的目标发起分布式拒绝服务（DDoS）攻击。有证据表明，Gafgyt 和 Necro 由一个名为 Keksec 的威胁组织运营，该组织也被追踪为 Kek Security 和 FreakOut。

像 Gafgyt 这样的物联网僵尸网络在不断进化，增加新的功能，2021 年检测到的变种使用 TOR 网络来掩盖恶意活动，并从泄露的 Mirai 源代码中借用了一些模块。值得注意的是，Gafgyt 的源代码于 2015 年初在网上泄露，进一步助长了其新版本和适应版本的出现。

![](https://image.3001.net/images/20240816/1723778692_66bec68492ae3d9d268cc.png!small)最新的攻击链涉及使用弱密码暴力破解 SSH 服务器，部署下一阶段有效载荷，以便使用 “systemd-net ”进行加密货币挖矿攻击，但在这一过程中，会先终止在受感染主机上运行的其他竞争性恶意软件。

它还会执行一个蠕虫模块，这是一个基于 Go 的 SSH 扫描器，名为 ld-musl-x86，负责扫描互联网上安全性较差的服务器，并将恶意软件传播到其他系统，从而有效扩大僵尸网络的规模。这包括 SSH、Telnet 以及与游戏服务器和 AWS、Azure 和 Hadoop 等云环境相关的凭证。

Morag 指出："目前使用的加密货币挖矿工具是 XMRig，它是一款专门用于挖掘门罗币的软件。在这次攻击中，威胁行为者试图利用 opencl 和 cuda 标志来运行挖矿软件，以便更充分地利用 GPU 和 Nvidia GPU 的计算能力。”

结合攻击者主要通过挖矿而非发起DDoS攻击来实现其目的，进一步支持了研究人员的观点，即这种新变种与以往的不同，它专注于攻击那些具有强大计算能力的云原生环境。

通过查询 Shodan 收集到的数据显示，目前有超过 3000 万台可公开访问的 SSH 服务器，因此用户必须采取措施保护实例的安全，防止暴力破解攻击和潜在的利用。

参考来源：

<https://thehackernews.com/2024/08/new-gafgyt-botnet-variant-targets-weak.html>

# 僵尸网络 # 挖矿僵尸网络 # Gafgyt僵尸网络

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