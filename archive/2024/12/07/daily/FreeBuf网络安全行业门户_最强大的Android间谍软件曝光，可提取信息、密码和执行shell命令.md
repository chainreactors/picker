---
title: 最强大的Android间谍软件曝光，可提取信息、密码和执行shell命令
url: https://www.freebuf.com/news/417070.html
source: FreeBuf网络安全行业门户
date: 2024-12-07
fetch_date: 2025-10-06T19:39:26.838449
---

# 最强大的Android间谍软件曝光，可提取信息、密码和执行shell命令

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

最强大的Android间谍软件曝光，可提取信息、密码和执行shell命令

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

最强大的Android间谍软件曝光，可提取信息、密码和执行shell命令

2024-12-06 15:22:13

所属地 上海

> 最近在俄罗斯联邦安全局（FSB）查获的手机上发现了一种新的Android间谍软件，这突显了用户隐私和安全持续面临的风险，特别是当设备被当局没收然后归还时。

![](https://image.3001.net/images/20241206/1733469855_6752a69fbc368b86c7c1f.png!small)

Kirill Parubets因被指控向乌克兰捐款而被FSB逮捕。在重新获得对移动设备的访问权限后，程序员怀疑设备被俄罗斯政府篡改，因为它表现出异常行为，并显示了一条通知，称“Arm cortex vx3 同步”。在与Citizen Lab共享进行取证分析后，调查人员确认设备上安装了间谍软件，该软件冒充合法且流行的Android应用“Cube Call Recorder”，该应用在Google Play上的下载量超过1000万次。该软件模仿合法应用程序，并已被授予广泛权限，允许其监视和控制感染设备上的几乎所有活动。

Citizen Lab 称，该恶意软件似乎是Monokle的新版本， Monokle最初由Lookout在2019年发现，由总部位于圣彼得堡的特种技术中心有限公司开发。Monokle 间谍软件功能十分完善，曾号称是最强的间谍软件之一。

其核心功能包括：

* 在空闲时跟踪位置
* 访问短信内容、联系人列表和日历条目
* 记录电话通话、屏幕活动和视频（通过摄像头）
* 提取消息、文件和密码
* 执行shell命令和解密数据
* 进行键盘记录以捕获敏感数据和密码
* 访问消息应用中的消息
* 执行shell命令和安装包（APK）
* 提取设备上存储的密码以及设备解锁密码
* 从设备中导出文件

Citizen Lab 进一步指出，该间谍软件通过加密的两阶段过程进行安装，这表明其开发者采用了高级技术来规避检测。其中第二阶段包含大部分间谍软件的功能，还包括加密文件，这些文件的名称看似随机，以增加检测难度。分析人员还报告在间谍软件的代码中发现了对iOS的引用，这表明可能存在一种运行在苹果iPhone设备上的变体。

对于高价值用户而言，可能面临严重的隐私和安全风险，因为该间谍软件可以访问和监视大量敏感信息。此事件凸显了移动设备的危险性，尤其是当它们被当局没收然后归还时，设备在此过程中可能已被破坏。由于Monokle 间谍软件能够提取密码和财务信息等敏感数据，对用户的财务安全和个人隐私构成严重威胁。它还可以用来追踪用户的位置，使他们容易受到身体跟踪或其他形式的骚扰。

### Android间谍软件检测tips

**检查异常行为**：寻找诸如无法解释的速度减慢、崩溃或电池耗电加快等迹象。间谍软件可以在后台运行，消耗资源并导致这些问题。

**监控应用权限**：警惕请求广泛权限的应用。如果一个应用请求它不需要的权限，例如访问您的麦克风或摄像头，而这与它的功能似乎无关，那么它可能是间谍软件。

**检查未知来源**：检查设备上是否有未知或可疑的应用。间谍软件经常伪装成合法应用。

**审查数据使用情况**：寻找数据使用的突然增加，尤其是在您没有积极使用互联网时。间谍软件可以秘密上传您的数据，导致更高的使用量。

**检查额外的图标或设置更改**：有时，间谍软件可以在您不知情的情况下在设备上创建额外的图标或更改设置。

参考来源：<https://www.bleepingcomputer.com/news/security/new-android-spyware-found-on-phone-seized-by-russian-fsb/>

# 数据安全

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