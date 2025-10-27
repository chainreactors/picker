---
title: 能伪造通话界面，FakeCall恶意软件变种在安卓手机中传播
url: https://www.freebuf.com/news/414141.html
source: FreeBuf网络安全行业门户
date: 2024-11-01
fetch_date: 2025-10-06T19:17:23.114392
---

# 能伪造通话界面，FakeCall恶意软件变种在安卓手机中传播

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

能伪造通话界面，FakeCall恶意软件变种在安卓手机中传播

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

能伪造通话界面，FakeCall恶意软件变种在安卓手机中传播

2024-10-31 11:00:52

所属地 上海

据Hackread消息，Zimperium's zLabs 的网络安全研究人员发现了 FakeCall 恶意软件的一个新变种，能够诱导受害者拨打诈骗电话，导致身份信息被窃取。

FakeCall 是一种语音钓鱼类型的网络钓鱼恶意软件，一旦安装，就能完全控制住安卓系统手机。而最新的变种还具备了几项新功能：选择性上传特定图像、远程控制屏幕、模拟用户操作、捕获和传输实时视频以及远程解锁设备，这些功能可以捕获敏感文件或用户个人照片。

FakeCall 恶意软件通常从受到攻击的网站或钓鱼邮件中渗透到设备，并请求成为默认呼叫处理程序的权限， 如果获得许可，恶意软件就会获得大量权限。

![](https://image.3001.net/images/20241031/1730343760_6722f350b7ba583d69d1c.png!small)攻击链路

根据 Zimperium 与 Hackread分享的博文，攻击者在攻击过程中使用了一种名为 "电话监听器服务 "的功能，这项服务是恶意软件的重要组成部分，使其能够操纵设备的通话功能，从而拦截和控制所有来电和去电，并窃取敏感信息，如一次性密码（OTP）或账户验证码。

恶意软件还能操纵设备显示屏，显示虚假的通话界面，诱骗受害者提供敏感信息。它还可以操纵通话记录来隐藏其恶意活动并控制通话时间。 攻击者可以利用这些功能欺骗受害者，使其泄露敏感信息并进一步造成经济上的损失。

![](https://image.3001.net/images/20241031/1730343832_6722f398d1c0461468e94.jpg!small)伪造的呼叫界面

此外，该恶意软件还利用安卓辅助功能服务捕获屏幕内容并操纵设备显示屏，在模仿合法手机应用的同时创建欺骗性用户界面。 通过监控来自Stock Dialer 应用程序的事件，并检测来自系统权限管理器和系统 UI 的权限提示。在检测到特定事件时，该恶意软件可以绕过用户同意授予的权限，让远程攻击者控制受害者的设备 UI，从而模拟用户交互并精确操纵设备。

目前谷歌已经调查了受 Scary 恶意软件模仿影响到的应用程序，并表示Google Play 上的所有应用程序都受到保护，不受新变体的影响。 为了防范此类恶意软件，建议用户从可信来源下载应用程序，谨慎处理权限请求，并使用具有设备检测功能的移动安全软件。

**参考来源：**

> [New “Scary” FakeCall Malware Captures Photos and OTPs on Android](https://hackread.com/scary-fakecall-malware-captures-photos-otps-android/#google_vignette)

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