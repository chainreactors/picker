---
title: ClickFix攻击活动升级：可通过虚假谷歌会议画面传播恶意软件
url: https://www.freebuf.com/news/413123.html
source: FreeBuf网络安全行业门户
date: 2024-10-19
fetch_date: 2025-10-06T18:52:25.942098
---

# ClickFix攻击活动升级：可通过虚假谷歌会议画面传播恶意软件

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

ClickFix攻击活动升级：可通过虚假谷歌会议画面传播恶意软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

ClickFix攻击活动升级：可通过虚假谷歌会议画面传播恶意软件

2024-10-18 09:40:20

所属地 上海

![1729215679_6711bcbf7f3bf967b05bc.png!small?1729215680613](https://image.3001.net/images/20241018/1729215679_6711bcbf7f3bf967b05bc.png!small?1729215680613)

最近，研究人员报告了一种新的 ClickFix 攻击活动，主要通过诱骗用户访问显示虚假连接错误的欺诈性 谷歌会议的页面，继而借此传播信息窃取恶意软件，主要针对 Windows 和 macOS 操作系统。

ClickFix是网络安全公司Proofpoint在5月份首次报告的一种社交工程战术，它来自一个威胁行为TA571，该行为者使用了冒充谷歌浏览器、微软Word和OneDrive错误的信息。

这些错误提示受害者将一段 PowerShell 代码复制到剪贴板，在 Windows 命令提示符中运行该代码即可解决问题。

![1729215695_6711bccfafc3eef268763.png!small?1729215696778](https://image.3001.net/images/20241018/1729215695_6711bccfafc3eef268763.png!small?1729215696778)

因此，受害者的系统会感染各种恶意软件，如 DarkGate、Matanbuchus、NetSupport、Amadey Loader、XMRig、剪贴板劫持者和 Lumma Stealer。

今年 7 月，McAfee 报告称，ClickFix 攻击活动变得越来越频繁，尤其是在美国和日本。

SaaS 网络安全提供商 Sekoia 的一份新报告指出，ClickFix 攻击活动现已升级，开始使用谷歌会议引诱、针对运输和物流公司的钓鱼电子邮件、伪造的 Facebook 页面和欺骗性的 GitHub 问题。

![1729215709_6711bcdd165baac468ead.png!small?1729215711032](https://image.3001.net/images/20241018/1729215709_6711bcdd165baac468ead.png!small?1729215711032)

ClickFix 发展大事记，资料来源 Sekoia

据这家法国网络安全公司称，最近的一些活动是由两个威胁组织 “斯拉夫民族帝国（SNE）”和 “Scamquerteo ”发起的，它们被认为是加密货币诈骗团伙 “Marko Polo ”和 “CryptoLove ”的分队。

![1729215738_6711bcfa923d7a9fea9e2.png!small?1729215739721](https://image.3001.net/images/20241018/1729215738_6711bcfa923d7a9fea9e2.png!small?1729215739721)

近期活动中使用的各种鱼饵，来源：Sekoia

## 谷歌会议“陷阱”

谷歌会议是 Google Workspace 套件中的视频通信服务，在企业虚拟会议、网络研讨会和在线协作环境中很受欢迎。

攻击者会向受害者发送看似与工作会议/大会或其他重要活动相关的合法谷歌会议邀请函的电子邮件。

URL 与实际的谷歌会议链接非常相似：

* meet[.]google[.]us-join[.]com
* meet[.]google[.]web-join[.]com
* meet[.]googie[.]com-join[.]us
* meet[.]google[.]cdm-join[.]us

一旦受害者进入这个虚假的页面，他们就会收到一条弹出消息，告知出现了技术问题，如麦克风或耳机问题。

如果他们点击 “尝试修复”，一个标准的 ClickFix 感染过程就会开始，网站复制并粘贴到 Windows 提示符上的 PowerShell 代码会用恶意软件感染他们的计算机，并从 “googiedrivers[.]com ”域获取有效载荷。

在 Windows 上，最终有效载荷是窃取信息的恶意软件 Stealc 或 Rhadamanthys。在 macOS 机器上，威胁行为者将 AMOS 窃取程序作为名为 “Launcher\_v194 ”的 .DMG （苹果磁盘映像）文件投放。

除了谷歌会议之外，Sekoia 还发现了其他几个恶意软件分发集群，包括 Zoom、PDF 阅读器、虚假视频游戏（Lunacy、Calipso、Battleforge、Ragon）、web3 浏览器和项目（NGT Studio）以及信使应用程序（Nortex）。

> 参考来源：[Fake Google Meet conference errors push infostealing malware (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/fake-google-meet-conference-errors-push-infostealing-malware/)

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

谷歌会议“陷阱”

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