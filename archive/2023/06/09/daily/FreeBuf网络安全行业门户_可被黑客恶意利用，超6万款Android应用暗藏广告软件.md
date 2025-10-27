---
title: 可被黑客恶意利用，超6万款Android应用暗藏广告软件
url: https://www.freebuf.com/news/368848.html
source: FreeBuf网络安全行业门户
date: 2023-06-09
fetch_date: 2025-10-04T11:47:41.357945
---

# 可被黑客恶意利用，超6万款Android应用暗藏广告软件

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

可被黑客恶意利用，超6万款Android应用暗藏广告软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

可被黑客恶意利用，超6万款Android应用暗藏广告软件

2023-06-08 10:52:46

所属地 上海

知名安全厂商Bitdefender 发布的一份报告称，他们在过去6个月中发现了 6万款不同类型的 Android 应用秘密地嵌入了广告软件安全程序。

报告指出，经分析，该活动旨在将广告软件传播到用户的Android系统设备，以此来增加收入。然而，网络攻击者可以轻松地改变策略，将用户重定向到其他类型的恶意软件，如针对银行账户的窃取程序。

据统计，该广告软件主要针对美国用户（55.27%），其次是韩国（9.8%）、巴西（5.96%）和德国（2.93%）。大量独特样本表明，有人设计了一个自动化过程来创建带有恶意软件的应用程序，通过仿冒游戏破解程序、免费 VPN、Netflix 虚假教程、无广告版YouTube/TikTok以及虚假的安全程序来分发。

![](https://image.3001.net/images/20230608/1686192806_648142a62e8444af10965.png!small)广告软件活动的国家分布

## 偷偷安装以逃避检测

这些应用程序托管在第三方网站上，研究人员没有在 Google Play 的应用程序中发现相同的广告软件。访问这些网站时，用户将被重定向到这些应用的下载站点，当用户安装这些应用程序后，并不会将自身配置为自动运行，因为这需要额外的权限。相反，它依赖于正常的 Android 应用程序安装流程，该流程会提示用户在安装后“打开”应用程序。

此外，这些应用程序不会显示图标，并在应用程序标签中使用 UTF-8 字符，因此更难被发现。这是一把双刃剑，因为这也意味着如果用户在安装后不启动该应用程序，则该应用程序很可能不会在安装后启动。

如果启动，该应用程序将显示一条错误消息，指出“应用程序在您所在的地区不可用。点击确定卸载。”但实际上，应用程序并没有被卸载，而只是在注册两个意图（Intent）之前进行了休眠，这两个意图可让应用程序在设备启动或设备解锁时开始运作。Bitdefender 表示后一种意图在前两天被禁用，可能是为了逃避用户的检测。

![](https://image.3001.net/images/20230608/1686192881_648142f10b83c297899aa.png!small)注册启动广告程序的 Android 意图

启动后，该应用程序将连接到运营方的服务器并检索要在移动浏览器中显示或作为全屏 WebView 广告显示的广告链接。

Android 设备是恶意软件开发人员的高度攻击目标，因为用户能够在不受 Google Play 商店保护之外的其他地方安装应用程序。但目前，即便在Google Play 中也未必安全。近期，来自 Dr. Web 和 CloudSEK 的研究人员发现，恶意间谍软件 SDK  通过 Google Play 上的应用程序在 Android 设备上竟安装了超过 4 亿次。

虽然 Google Play 仍然有恶意应用程序，但从官方商店安装 Android 应用程序总体还是要安全得多，强烈建议用户不要从第三方站点安装任何 Android 应用程序，因为它们是恶意软件的常见载体。

> 参考来源：[Over 60,000 Android apps secretly installed adware for past six months](https://www.bleepingcomputer.com/news/security/over-60-000-android-apps-secretly-installed-adware-for-past-six-months/)

# 资讯 # 移动安全

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

偷偷安装以逃避检测

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