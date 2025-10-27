---
title: 黑客滥用微软“快速助手”，展开网络钓鱼攻击活动
url: https://www.freebuf.com/news/401225.html
source: FreeBuf网络安全行业门户
date: 2024-05-18
fetch_date: 2025-10-06T16:51:21.596800
---

# 黑客滥用微软“快速助手”，展开网络钓鱼攻击活动

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

黑客滥用微软“快速助手”，展开网络钓鱼攻击活动

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客滥用微软“快速助手”，展开网络钓鱼攻击活动

2024-05-17 11:37:11

所属地 上海

近日，微软威胁情报团队表示，一个名为 Storm-1811 的威胁攻击者正在滥用客户端管理工具 "快速助手"（Quick Assist），针对用户展开社交工程攻击。![1715917127_6646d147e1495f1d77f61.png!small](https://image.3001.net/images/20240517/1715917127_6646d147e1495f1d77f61.png!small)

> Quick Assist 是微软公司推出的一款合法应用程序，允许用户通过远程连接与他人共享自己的 Windows 或 macOS 设备，主要用于排除系统中的技术问题，默认安装在运行 Windows 11 的设备上。

2024 年 5 月 15 日，微软威胁情报团队在发布的一份报告中指出，Storm-1811 是一个以部署 Black Basta 勒索软件而闻名的有经济动机的网络犯罪团伙。

## 威胁攻击者冒充安检人员

研究人员经过详细分析得出了威胁攻击者的攻击链，首先通过网络钓鱼实施社会工程学攻击，诱骗毫无戒心的受害者安装远程监控和管理（RMM）工具，然后发送 QakBot、Cobalt Strike，最终发送 Black Basta 勒索软件。

整个过程中，威胁攻击者滥用微软'快速助手'功能来实施社会工程学攻击。例如，伪装成受信任的联系人，例如微软技术支持或目标用户所在公司的 IT 专业人员，以获得对潜在攻击目标设备的初始访问权限。

> 威胁攻击者一开始会想方设法掌握一批受害者的数据信息，此后便向受害者邮箱发送大量垃圾邮件，完成一系列操作后，拨打受害者电话冒充安全公司声称“能够提供协助”，诱骗用户使用系统内置的远程管理软件与其展开通信，以便更进一步侵入用户设备。

为了使网络攻击更有说服力，威胁攻击者还会发起链接列表攻击（一种电子邮件轰炸攻击）这时候，受害目标电子邮件地址会注册各种合法的电子邮件订阅服务，导致其收件箱充斥着订阅的内容。然后，威胁攻击者伪装成公司的 IT 支持团队，给受害目标用户打电话，声称可以帮助他们解决垃圾邮件问题，并说服他们通过 "快速协助"（Quick Assist）授权访问他们的设备。

一旦用户允许访问和控制，威胁攻击者就会运行脚本化的 cURL 命令，下载一系列批处理文件或 ZIP 文件，用于发送恶意有效载荷，在受害者整个网络中部署 Black Basta 勒索软件。微软方面表示，公司的完全团队正在密切关注滥用 "快速助手 "的情况，并正在努力在软件中加入警告信息，以通知用户可能存在的技术支持诈骗，防止诈骗可能会为勒索软件的传播提供便利。

网络安全公司 Rapid7 指出，”快速助手“滥用活动始于 2024 年 4 月中旬，目标涉及包括制造业、建筑业、食品饮料业、银行业以及运输业等多个行业和垂直领域，实施此类攻击的门槛相对很低，再加上这些攻击对受害者造成的重大影响，具有很强的破坏力、以及广泛的受影响范围，给威胁攻击者通过部署勒索软件敛财提供了新思路。![](https://image.3001.net/images/20240517/1715925497_6646f1f9457a384914b4c.jpg!small)

自 2022 年 4 月 出道以来，Black Basta 勒索软件团伙与其它勒索软件组织一样，主要通过实施双重勒索攻击，获取赎金。从 Elliptic 和 Corvus Insurance 发布的联合研究结果来看， Black Basta 自推出以来，累计感染了超过 329 名受害者。

值得注意的是，安全研究人员通过分析区块链交易，发现 Black Basta 与 Conti 勒索软件团伙之间貌似存在着明显的联系，2022 年，Conti 勒索软件团伙停止了攻击活动，差不多同一时间 Black Basta 组织开始活跃。

参考文章：
https://thehackernews.com/2024/05/cybercriminals-exploiting-microsofts.html

# 恶意软件

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

威胁攻击者冒充安检人员

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