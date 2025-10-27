---
title: 攻击手法罕见！ESET披露最新网络钓鱼活动，专门针对Android、iPhone用户
url: https://www.freebuf.com/news/409102.html
source: FreeBuf网络安全行业门户
date: 2024-08-22
fetch_date: 2025-10-06T18:03:37.656662
---

# 攻击手法罕见！ESET披露最新网络钓鱼活动，专门针对Android、iPhone用户

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

攻击手法罕见！ESET披露最新网络钓鱼活动，专门针对Android、iPhone用户

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

攻击手法罕见！ESET披露最新网络钓鱼活动，专门针对Android、iPhone用户

2024-08-21 10:00:53

所属地 上海

ESET 研究人员发现了一种罕见的网络钓鱼活动，专门针对 Android 和 iPhone 用户。他们分析了一个在野外观察到的案例，该案例主要是针对一家著名的捷克银行的客户。

值得注意的是这种攻击主要是从第三方网站安装钓鱼应用程序，而无需用户主动安装。这有可能导致使用安卓系统的用户设备上会被隐秘安装一种特殊的 APK，隐蔽性很高，很难发现，它看起来甚至有点像是用户从 Google Play 商店安装的。这种钓鱼攻击威胁也针对 iOS 用户。

![1724205577_66c54a09939e858f8e410.png!small](https://image.3001.net/images/20240821/1724205577_66c54a09939e858f8e410.png!small)

PWA 网络钓鱼流程（来源：ESET）

针对 iOS 的钓鱼网站会指示受害者在主屏幕上添加渐进式网络应用程序 (PWA)，而在 Android 上，PWA 是在浏览器中确认自定义弹出窗口后安装的。在这一点上，这些钓鱼应用程序与它们在这两个操作系统上模仿的真实银行应用程序基本没有区别。

PWA 本质上是将网站捆绑到一个看似独立的应用程序中，并通过使用本地系统提示增强了其虚假的独立性。与网站一样，PWA 也是跨平台的，这就解释了为什么这些 PWA 网络钓鱼活动可以既针对 iOS 又针对 Android 用户。负责 ESET 品牌情报服务的 ESET 分析师在捷克观察到了这种新技术，该服务可监控针对客户品牌的威胁。

分析该威胁的 ESET 研究员 Jakub Osmani 表示：对于 iPhone 用户来说，这种行为可能会打破任何有关安全的‘围墙花园’假设。

## ESET 发现使用电话、短信和恶意广告的网络钓鱼欺诈行为

ESET 分析师发现了一系列针对移动用户的网络钓鱼活动，这些活动分别使用了三种不同的 URL 发送机制，包括自动语音呼叫、短信和社交媒体恶意广告。语音电话发送是通过自动呼叫完成的，该呼叫会警告用户银行应用程序已过期，并要求用户在数字键盘上选择一个选项。

按下正确的按钮后，就会通过短信发送一个钓鱼网址，正如一条推文所报道的那样。最初的短信发送是通过向捷克电话号码滥发信息来实现的。发送的信息包括一个钓鱼链接和文本，目的是让受害者通过社交工程访问该链接。恶意活动通过 Instagram 和 Facebook 等 Meta 平台上的注册广告进行传播。这些广告包括行动号召，比如为 “下载以下更新 ”的用户提供限量优惠。

打开第一阶段发送的 URL 后，Android 受害者会看到两个截然不同的活动，一个是模仿目标银行应用程序官方 Google Play 商店页面的高质量钓鱼页面，另一个是该应用程序的山寨网站。受害者会被要求安装 “新版 ”银行应用程序。

## WebAPK 绕过安全警告

这种网络钓鱼活动和方法之所以能够得逞，完全得益于渐进式网络应用程序的技术。简而言之，渐进式网络应用程序是使用传统网络应用程序技术构建的应用程序，可以在多个平台和设备上运行。

WebAPK 可被视为渐进式网络应用程序的升级版，因为 Chrome 浏览器会从 PWA（即 APK）生成本地 Android 应用程序。这些 WebAPK 看起来就像普通的本地应用程序。此外，安装 WebAPK 不会产生任何 “从不可信来源安装 ”的提示警告。

某小组曾尝试通过 Telegram 官方 API 将所有输入信息记录到 Telegram 群组聊天中，而另一个小组则使用带有管理面板的传统命令与控制（C&C）服务器。Osmani 表示：根据这些活动使用了两种不同的 C&C 基础设施这一事实，我们确定是两个不同的团伙在针对多家银行实施 PWA/WebAPK 网络钓鱼活动。大多数已知案例都发生在捷克，只有两个网络钓鱼应用程序出现在捷克境外（特别是匈牙利和格鲁吉亚）。

ESET 的研究人员在调查中发现的所有披露在网上的敏感信息，银行都已迅速跟进处理。ESET 方面也协助删除了多个网络钓鱼域和 C&C 服务器。

> 参考来源：[New phishing method targets Android and iPhone users - Help Net Security](https://www.helpnetsecurity.com/2024/08/20/android-iphone-phishing-campaign/)

# 网络钓鱼攻击 # 网络钓鱼活动

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

ESET 发现使用电话、短信和恶意广告的网络钓鱼欺诈行为

WebAPK 绕过安全警告

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