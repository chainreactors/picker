---
title: StrongPity 黑客分发带有后门的应用程序以瞄准 Android 用户
url: https://www.freebuf.com/news/354887.html
source: FreeBuf网络安全行业门户
date: 2023-01-12
fetch_date: 2025-10-04T03:39:36.948020
---

# StrongPity 黑客分发带有后门的应用程序以瞄准 Android 用户

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

StrongPity 黑客分发带有后门的应用程序以瞄准 Android 用户

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

StrongPity 黑客分发带有后门的应用程序以瞄准 Android 用户

2023-01-11 11:37:50

所属地 上海

[![](https://image.3001.net/images/20230111/1673408319_63be2f3f01523e5edf7ce.png!small)](https://image.3001.net/images/20230111/1673408319_63be2f3f01523e5edf7ce.png%21small)

**名为StrongPity**的高级持续性攻击 (APT) 组织通过一个冒充名为**Shagle**的视频聊天服务的虚假网站，以木马化版本的 Telegram 应用程序瞄准 Android 用户。

“一个模仿 Shagle 服务的山寨网站被用来分发 StrongPity 的移动后门应用程序，”ESET 恶意软件研究员 Lukáš Štefanko在一份技术报告中说。“该应用程序是开源 Telegram 应用程序的修改版本，使用 StrongPity 后门代码重新打包。”

StrongPity，也被称为 APT-C-41 和 Promethium，是一个从 2012 年开始活跃的网络间谍组织，其大部分行动集中在叙利亚和土耳其。卡巴斯基于 2016 年 10 月首次公开报告了该组织的存在。

此后，该组织的活动范围扩大到涵盖非洲、亚洲、欧洲和北美的更多目标，入侵利用水坑攻击和网络钓鱼来激活杀伤链。

StrongPity 的主要特征之一是它使用假冒网站，这些网站声称提供各种软件工具，只是为了诱骗受害者下载受感染的应用程序版本。

2021 年 12 月，Minerva Labs披露了一个三阶段攻击序列，该序列源于看似良性的 Notepad++ 安装文件，安装后将后门上传到受感染的主机上。

同年，专家观察到StrongPity 首次部署了一款 Android 恶意软件，它能够入侵叙利亚电子政府门户网站并将官方 Android APK 文件替换为流氓文件。

[![](https://image.3001.net/images/20230111/1673408321_63be2f41d219737865c01.png!small)](https://image.3001.net/images/20230111/1673408321_63be2f41d219737865c01.png%21small)

ESET 的最新发现突出了一种类似的作案手法，该作案手法旨在分发更新版本的 Android 后门有效荷载，该后门有效荷载能够记录电话呼叫、跟踪设备位置并收集 SMS 消息、通话记录、联系人列表和文件。

此外，授权恶意软件可访问权限使其能够从各种应用程序（如 Gmail、Instagram、Kik、LINE、Messenger、Skype、Snapchat、Telegram、Tinder、Twitter、Viber 和微信）中窃取信息。

此次后门功能隐藏在 2022 年 2 月 25 日左右可供下载的合法版本的 Telegram Android 应用程序中。也就是说，虚假的 Shagle 网站目前不再活跃。

也没有证据表明该应用程序已在官方 Google Play 商店中发布。目前尚不清楚潜在受害者是如何被引诱到假冒网站的。

Štefanko 指出：“恶意域名是在同一天注册的，因此山寨网站和假冒的 Shagle 应用程序可能从那天起就可以下载了。”

攻击的另一个值得注意的方面是 Telegram 的篡改版本使用与正版 Telegram 应用程序包名称相同，这意味着后门变体无法安装在已经安装 Telegram 的设备上。

Štefanko 说：“这可能意味攻击者首先诱导受害者，并迫使他们从设备上卸载 Telegram（如果安装了 Telegram），或者该活动的重点是很少使用 Telegram 进行通信的国家。”

> 参考来源：https://thehackernews.com/2023/01/strongpity-hackers-distribute.html

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