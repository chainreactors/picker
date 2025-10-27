---
title: 以虚假视频会议为诱饵，攻击者瞄准了Web3公司员工
url: https://www.freebuf.com/news/417193.html
source: FreeBuf网络安全行业门户
date: 2024-12-10
fetch_date: 2025-10-06T19:39:35.222833
---

# 以虚假视频会议为诱饵，攻击者瞄准了Web3公司员工

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

以虚假视频会议为诱饵，攻击者瞄准了Web3公司员工

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

以虚假视频会议为诱饵，攻击者瞄准了Web3公司员工

2024-12-09 10:49:40

所属地 上海

据The Hacker News消息，网络安全研究人员近日发现一种新的诈骗活动，利用虚假的商务视频会议应用程序来针对 Web3 技术公司的工作人员，并传播一种名为Realst 的信息窃取程序。

![](https://image.3001.net/images/20241209/1733714146_675660e29a8a79bc69850.png!small)

为了增强迷惑性和合法性，攻击者利用AI设立了虚假公司。Cado Security 的研究员表示，该公司主动联系目标建立视频通话，提示用户从网站上下载会议应用程序，也就是Realst信息窃取程序。

这一恶意活动被安全公司命名为 Meeten，因为攻击者使用的虚假网站名称分别为 Clusee、Cuesee、Meeten、Meetone 和 Meetio 等。

在实施过程中，攻击者通过 Telegram平台以寻找投资机会为幌子接近目标，诱导对方加入一个可疑平台上托管的视频通话。最终访问该站点的受害者将被提示下载 Windows 或 macOS版本的客户端，在macOS 上安装并启动后，会提示"当前版本的应用程序与 macOS 版本不完全兼容"，要求受害者输入系统密码才能正常使用该应用程序。

![](https://image.3001.net/images/20241209/1733713886_67565fdea6b3301a3516d.png!small)含有恶意软件的视频会议软件客户端下载页面

该技术已被 Atomic macOS Stealer、Cuckoo、MacStealer、Banshee Stealer 和 Cthulhu Stealer 等多个 macOS 窃取程序家族采用。 攻击的最终目的是窃取各种敏感数据，包括加密货币钱包中的数据，并将其导出到远程服务器。

该恶意软件还可以窃取 Telegram 凭证、银行信息、iCloud Keychain 数据以及 Google Chrome、Microsoft Edge、Opera、Brave、Arc、Cốc Cốc 和 Vivaldi 浏览器的 cookies。

而Windows 版应用程序 Nullsoft Scriptable Installer System (NSIS) 文件的签名很可能是从 Brys Software Ltd. 窃取的合法签名。 安装程序中嵌入了一个 Electron 应用程序，该应用程序被配置为从攻击者控制的域中检索窃取器可执行文件（一个基于 Rust 的二进制文件）。

这已经不是第一次有人利用假冒会议软件传播恶意软件了。 今年 3 月初，Jamf 威胁实验室披露，它检测到一个名为 meethub[.]gg 的假冒网站传播与 Realst 有关的窃取恶意软件。6月，Recorded Future 详细描述了一场名为 markopolo 的活动，该活动针对加密货币用户使用假冒的虚拟会议软件，通过 Rhadamanthys、Steelc 和 Atomic 等盗号软件来窃取用户的资产。

此外，研究人员也称，攻击者正越来越多地使用AI为其活动生成内容，以此快速创建逼真的网站，从而增加其骗局的合法性，并使可疑网站更难被发现。

**参考来源：**

> [Hackers Using Fake Video Conferencing Apps to Steal Web3 Professionals' Data](https://thehackernews.com/2024/12/hackers-using-fake-video-conferencing.html)

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