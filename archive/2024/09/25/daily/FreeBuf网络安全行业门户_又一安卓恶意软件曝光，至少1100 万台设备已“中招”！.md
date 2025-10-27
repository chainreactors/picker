---
title: 又一安卓恶意软件曝光，至少1100 万台设备已“中招”！
url: https://www.freebuf.com/news/411574.html
source: FreeBuf网络安全行业门户
date: 2024-09-25
fetch_date: 2025-10-06T18:26:46.142505
---

# 又一安卓恶意软件曝光，至少1100 万台设备已“中招”！

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

又一安卓恶意软件曝光，至少1100 万台设备已“中招”！

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

又一安卓恶意软件曝光，至少1100 万台设备已“中招”！

2024-09-24 10:09:04

所属地 上海

![image_(2).jpg](https://image.3001.net/images/20240924/1727143747_66f21f43703f6f22f0dbd.jpg!small)

近日，有研究人员发现在恶意 SDK 供应链攻击中，有黑客通过 Google Play 在 1100 万台设备上安装了新版本的 Necro 恶意安卓载入器。

这种新版 Necro 木马是通过合法应用程序、安卓游戏 mod 和 Spotify、WhatsApp 和 Minecraft 等流行软件的修改版所使用的恶意广告软件开发工具包 (SDK) 安装的。

Necro 会在受感染设备上安装多个有效载荷，并激活各种恶意插件，包括：

* 通过隐形 WebView 窗口加载链接的广告软件（Island 插件、Cube SDK）
* 下载和执行任意 JavaScript 和 DEX 文件的模块（Happy SDK、Jar SDK）
* 专为订阅欺诈提供便利的工具（Web 插件、Happy SDK、Tap 插件）
* 将受感染设备用作代理来路由恶意流量的机制（NProxy 插件）
* Google Play 上的 Necro 木马

卡巴斯基在 Google Play 上的两个应用程序中发现了 Necro 载入器，这两个应用程序都拥有大量用户。

第一个是 “Benqu ”的 Wuta Camera，这是一款照片编辑和美化工具，在 Google Play 上的下载量超过 1000万次。

![1727143539_66f21e73b3aa2def6ef01.png!small](https://image.3001.net/images/20240924/1727143539_66f21e73b3aa2def6ef01.png!small)

Google Play 上的 Wuta 相机应用程序，来源：BleepingComputer

威胁分析师报告称，Necro是在6.3.2.148版本发布时出现在该应用上的，直到6.3.6.148版本，卡巴斯基才通知谷歌。

虽然该木马在6.3.7.138版本中被移除，但任何可能通过旧版本安装的有效载荷仍可能潜伏在安卓设备上。

第二个携带 Necro 的合法应用程序是 “WA message recover-wamr ”的 Max Browser，它在 Google Play 上有 100 万下载量，直到卡巴斯基报告后才被删除。

卡巴斯基称，Max Browser的最新版本1.2.0仍携带Necro，目前暂没有安全版本可供升级，建议该浏览器的用户立即卸载，换用其他浏览器。

卡巴斯基称，这两款应用程序是被一个名为 “Coral SDK ”的广告SDK感染的，该SDK主要采用混淆技术来隐藏其恶意活动，同时还利用图像隐写术来下载第二级有效载荷shellPlugin，并伪装成无害的PNG图像。

![1727143685_66f21f0556012df7fb7c8.png!small](https://image.3001.net/images/20240924/1727143685_66f21f0556012df7fb7c8.png!small)

感染链路图 来源：卡巴斯基

谷歌表示他们知道这些被举报的应用程序，并正在对其进行调查。

## Necro 木马也通过其他非官方渠道传播

在 Play Store 之外，Necro 木马主要通过非官方网站发布的流行应用程序的修改版本（mods）进行传播。

卡巴斯基发现的著名例子包括 WhatsApp mods “GBWhatsApp ”和 “FMWhatsApp”，它们承诺提供更好的隐私控制和扩展文件共享限制。另一个例子是 Spotify mod “Spotify Plus”，它承诺免费使用无广告的高级服务。

![1727143713_66f21f21af6cc3628bb88.png!small](https://image.3001.net/images/20240924/1727143713_66f21f21af6cc3628bb88.png!small)

传播恶意 Spotify Mod 的网站 来源：卡巴斯基

报告中还提到了感染 Necro 载入器的 Minecraft mod 和其他流行游戏的 mod，如 Stumble Guys、Car Parking Multiplayer 和 Melon Sandbox。

在所有情况下，恶意行为都是在后台显示广告为攻击者带来欺诈性收入、未经用户同意安装应用程序和 APK，以及使用隐形 WebViews 与付费服务进行交互。

由于非官方的安卓软件网站不会如实报告下载数量，因此最新一轮 Necro 木马感染的总数量尚不得而知，但至少有 1100 万次来自 Google Play。

> 参考来源：[Android malware 'Necro' infects 11 million devices via Google Play (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/android-malware-necro-infects-11-million-devices-via-google-play/)

# 木马 # 安卓安全 # Google Play

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

Necro 木马也通过其他非官方渠道传播

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