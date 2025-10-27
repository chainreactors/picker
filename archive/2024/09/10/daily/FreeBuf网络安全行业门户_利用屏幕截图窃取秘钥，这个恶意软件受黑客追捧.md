---
title: 利用屏幕截图窃取秘钥，这个恶意软件受黑客追捧
url: https://www.freebuf.com/news/410506.html
source: FreeBuf网络安全行业门户
date: 2024-09-10
fetch_date: 2025-10-06T18:27:46.967455
---

# 利用屏幕截图窃取秘钥，这个恶意软件受黑客追捧

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

利用屏幕截图窃取秘钥，这个恶意软件受黑客追捧

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

利用屏幕截图窃取秘钥，这个恶意软件受黑客追捧

2024-09-09 09:17:24

所属地 上海

![](https://image.3001.net/images/20240909/1725850230_66de6276c34d247e336c8.png!small)

一款名为 SpyAgent 的新型安卓恶意软件近期被发现可利用光学字符识别（OCR）技术，从存储在移动设备上的截图中窃取加密货币钱包恢复短语。这种加密货币恢复短语或种子短语通常由 12-24 个单词组成，是加密货币钱包的备份密钥，主要用于丢失设备、数据损坏或希望将钱包转移到新设备时恢复对加密货币钱包及其所有资金的访问。

这类秘密短语深受威胁行为者的追捧，因为一旦他们获取到这些短语，就能在他们自己的设备上还原他人的钱包，并窃取其中存储的所有资金。

由于恢复短语有 12-24 个单词，很难记住，因此加密货币钱包往往会提示人们保存或打印这些单词，并将其存放在安全的地方。为了方便起见，有些人会将恢复短语截图并保存为移动设备的图像。

McAfee发现的一起恶意软件操作至少涉及280个在谷歌Play商店之外分发的APK。这些APK通过短信或恶意社交媒体帖子传播，能够利用OCR技术从Android设备上存储的图片中恢复加密货币恢复短语，构成重大威胁。

一些 Android 应用程序会伪装成韩国和英国政府服务、约会网站和色情网站。虽然该活动主要针对韩国，但 McAfee 已观察到其暂时扩展到英国，并有迹象表明 iOS 变种可能正在早期开发中。

![1725844424_66de4bc8a15a53860e278.png!small?1725844425581](https://image.3001.net/images/20240909/1725844424_66de4bc8a15a53860e278.png!small?1725844425581)

SpyAgent恶意软件活动时间表，来源：McAfee

2023 年 7 月，趋势科技揭露了两个名为 CherryBlos 和 FakeTrade 的安卓恶意软件家族，它们通过 Google Play 传播，也使用 OCR 从提取的图像中窃取加密货币数据，因此这种策略似乎正受到越来越多的关注。

## SpyAgent 数据提取

一旦感染新设备，SpyAgent 就会开始向其指挥和控制 (C2) 服务器发送以下敏感信息：

* 受害者的联系人列表，可能是为了通过来自可信联系人的短信传播恶意软件。
* 收到的短信，包括包含一次性密码 (OTP) 的短信。
* 存储在设备上用于 OCR 扫描的图像。
* 通用设备信息，可能用于优化攻击。

SpyAgent 还可以接收来自 C2 的命令，以更改声音设置或发送短信，这些命令很可能用于发送钓鱼短信以传播恶意软件。

![1725844515_66de4c23416830d535294.png!small?1725844515860](https://image.3001.net/images/20240909/1725844515_66de4c23416830d535294.png!small?1725844515860)

C2 服务器上的 OCR 扫描结果，来源：McAfee

## 暴露的基础设施

McAfee 发现，SpyAgent 行动的运营者在配置服务器时没有遵循正确的安全做法，这才导致研究人员能够轻易访问服务器、管理员面板页面以及从受害者那里窃取的文件和数据。

![One of the attackers' panel](https://image.3001.net/images/20240909/1725850274_66de62a241d4bb21b6115.jpg!small)

攻击者的控制面板，来源：McAfee

被盗图像会在服务器端进行处理和 OCR 扫描，然后在管理面板上进行相应整理，以便于管理和立即用于钱包劫持攻击。

![Code that performs the OCR scanning on the server](https://image.3001.net/images/20240909/1725850277_66de62a51649040d1946b.jpg!small)

执行图像 OCR 扫描的代码，来源：McAfee

如果想降低安卓系统受到此类攻击的风险，那就不要在 Google Play 以外的渠道下载安装安卓应用程序，因为那些非官方渠道是恶意软件传播的主要途径。

也不要理会那些链接到 APK 下载 URL 的短信，并始终关闭与应用程序核心功能无关的危险权限。另外，定期进行 Google Play Protect 扫描，以检查是否有被检测为恶意软件的应用程序也是十分必要的。

> 参考来源：[SpyAgent Android malware steals your crypto recovery phrases from images ﻿](https://www.bleepingcomputer.com/news/security/spyagent-android-malware-steals-your-crypto-recovery-phrases-from-images/)

# 恶意软件 # Android恶意软件

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

SpyAgent 数据提取

暴露的基础设施

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