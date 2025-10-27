---
title: TrickMo 安卓银行木马新变种利用虚假锁屏窃取密码
url: https://www.freebuf.com/news/412834.html
source: FreeBuf网络安全行业门户
date: 2024-10-16
fetch_date: 2025-10-06T18:53:26.675993
---

# TrickMo 安卓银行木马新变种利用虚假锁屏窃取密码

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

TrickMo 安卓银行木马新变种利用虚假锁屏窃取密码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

TrickMo 安卓银行木马新变种利用虚假锁屏窃取密码

2024-10-15 10:09:56

所属地 上海

![1728958098_670dce929ff3a16e5ba3d.png!small](https://image.3001.net/images/20241015/1728958098_670dce929ff3a16e5ba3d.png!small)

近期，研究人员在野外发现了 TrickMo Android 银行木马的 40 个新变种，它们与 16 个下载器和 22 个不同的命令和控制（C2）基础设施相关联，具有旨在窃取 Android 密码的新功能。

Zimperium 和 Cleafy 均报道了此消息。

TrickMo 于 2020 年首次被 IBM X-Force 记录在案，但人们认为它至少从 2019 年 9 月开始就被用于攻击安卓用户。

## 新版 TrickMo 利用虚假锁屏窃取安卓密码

新版 TrickMo 的主要功能包括一次性密码（OTP）拦截、屏幕录制、数据外渗、远程控制等。

该恶意软件试图滥用强大的辅助功能服务权限，为自己授予额外权限，并根据需要自动点击提示。

该银行木马能够向用户提供各种银行和金融机构的钓鱼登录屏幕覆盖，以窃取他们的账户凭据，使攻击者能够执行未经授权的交易。

![1728958114_670dcea2a4f04b004ce62.png!small](https://image.3001.net/images/20241015/1728958114_670dcea2a4f04b004ce62.png!small)

攻击中使用的银行业务覆盖，来源：Zimperium

Zimperium 分析师在剖析这些新变种时还报告了一种新的欺骗性解锁屏幕，它模仿了真正的安卓解锁提示，旨在窃取用户的解锁模式或 PIN 码。

Zimperium解释称：欺骗性用户界面是一个托管在外部网站上的HTML页面，以全屏模式显示在设备上，使其看起来像一个合法的屏幕。

当用户输入解锁模式或 PIN 码时，页面会将捕获的 PIN 码或模式详情以及唯一的设备标识符（Android ID）传输到 PHP 脚本。

![Fake Android lock screen shown by TrickMo](https://image.3001.net/images/20241015/1728958252_670dcf2caba616a04a988.jpg!small)

TrickMo 展示的伪造安卓锁屏，来源：Zimperium

通过窃取 PIN 码，攻击者可以在设备不受监控时（可能是在深夜）解锁设备，从而在设备上实施欺诈。

## 暴露的受害者

由于 C2 基础设施的安全防护不当，Zimperium 还能够确定至少有 13000 名受害者受到了该恶意软件的影响，其中大部分位于加拿大，还有相当数量的受害者位于阿拉伯联合酋长国、土耳其和德国。

![Victims heatmap](https://image.3001.net/images/20241015/1728958255_670dcf2f8e3ef9b0139d3.jpg!small)

TrickMo 受害者热图，来源：Zimperium

据 Zimperium 称，这一数字与 “多个 C2 服务器 ”相对应，因此 TrickMo 受害者的总数可能更高。另外，分析发现，每当恶意软件成功渗出凭证时，IP列表文件就会定期更新。在这些文件中，研究人员发现了数以百万计的记录，这表明被入侵的设备数量庞大，威胁行为者访问了大量敏感数据。

由于 C2 基础设施配置不当，可能会将受害者数据暴露给更广泛的网络犯罪社区，Cleafy 此前一直未向公众公布入侵指标。Zimperium 现在选择在 GitHub 存储库中发布所有信息。

然而，TrickMo 的目标范围似乎足够广泛，涵盖了银行以外的应用程序类型（和账户），包括 VPN、流媒体平台、电子商务平台、交易、社交媒体、招聘和企业平台。

由于 C2 基础设施配置不当，可能会将受害者数据暴露给更广泛的网络犯罪社区，Cleafy 此前一直未向公众公布入侵指标，但 Zimperium 现在选择在 GitHub 存储库中发布所有信息。

据悉，TrickMo 目前是通过网络钓鱼传播的，因此为了尽量减少感染的可能性，应避免从不认识的人通过短信或直接消息发送的 URL 下载 APK。

Google Play Protect 可以识别并阻止 TrickMo 的已知变种，因此确保它在设备上处于激活状态对于抵御恶意软件至关重要。

> 参考来源：[TrickMo malware steals Android PINs using fake lock screen (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/trickmo-malware-steals-android-pins-using-fake-lock-screen/)

# 恶意软件 # pin码

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

新版 TrickMo 利用虚假锁屏窃取安卓密码

暴露的受害者

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