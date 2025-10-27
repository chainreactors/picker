---
title: 只有付费才可使用？马斯克取消普通用户短信2FA保护
url: https://www.freebuf.com/articles/358126.html
source: FreeBuf网络安全行业门户
date: 2023-02-21
fetch_date: 2025-10-04T07:37:50.888541
---

# 只有付费才可使用？马斯克取消普通用户短信2FA保护

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

只有付费才可使用？马斯克取消普通用户短信2FA保护

* ![]()
* 关注

只有付费才可使用？马斯克取消普通用户短信2FA保护

2023-02-20 14:07:50

所属地 上海

Bleeping Computer 网站披露， 3 月 20 日开始，不再支持普通用户基于短信的双因素身份验证（2FA）方式，只有购买 Twitter Blue 服务的订阅用户才能继续使用。![1676874078_63f3115e441da6c86cee6.png!small](https://image.3001.net/images/20230220/1676874078_63f3115e441da6c86cee6.png!small)

从 Twitter 发布的安全报告来看，2021 年 7 月至 2021 年 12 月，只有 2.6% 的用户使用了双因素认证，在这些用户中，74.4% 使用的是 SMS 2FA，28.9% 使用验证器应用程序，0.5% 使用硬件安全密钥。

## 马斯克支持此次验证变革

短信验证带来的安全隐患已经持续了很久，埃隆·马斯克（Elon Musk）指出，仅仅在假冒 2FA 短信上，每年损失约 6000 万美元。![1676874088_63f31168b41cc5873ac64.png!small](https://image.3001.net/images/20230220/1676874088_63f31168b41cc5873ac64.png!small)

马斯克非常支持此次禁止非 Twitter Blue 用户使用短信双因素认证，并指出相对于短信印证，验证器应用程序安全得多。

短信双因素认证可能会遭遇 SIM 交换攻击风险（ SIM 交换攻击：指威胁攻击者通过欺骗或贿赂运营商员工将号码重新分配给攻击者控制的 SIM 卡，以期控制目标的手机号码），此举使得攻击者轻松在其设备上使用受害者电话号码，接收短信（短信多因素认证（MFA）码），甚至直接登录部分使用电话号码作为凭证的帐户。

## Twitter 建议用户使用强验证方式保护帐户安全

值得一提的是，此次变革后，如果用户没有计划注册 Twitter Blue，就会被要求使用安全密钥或身份验证应用程序作为 2FA 身份验证方式。

目前，虽然许多用户不同意新改革得处理和推出方式，但不得不承认，此次改革可能会为选择不订阅Twitter Blue 的用户带来更好的安全性。 ![](https://image.3001.net/images/20230220/1676875424_63f316a0ab4c6d7854d05.jpg!small)据悉，为确保账户安全，最好的选择是使用硬件安全密钥，例如 Google Titan 或 Yubiky，这些是一种具有 USB 或 NFC 连接的小型设备，可以自动响应 2FA 请求并登录到帐户， 之所以被认为是最安全的，因为这些都是物理设备，必须插入计算机并才能登录用户的帐户。

另一种相对较好的选择是使用双因素身份验证应用程序，如 Google Authenticator、Microsoft Authenticator 和 Authy。

用户在网站上设置双因素/多因素认证时，网站将显示用户使用认证应用程序扫描的二维码，扫描后，网站将在应用程序中注册，以生成 2FA 代码，该代码必须提交到网站才能登录到用户的帐户。

最后，强烈建议用户在平时使用的在线帐户（包括 Twitter）上启用 2FA，并使用验证器或硬件安全密钥，以确保账户安全。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/twitter-gets-rid-of-sms-2fa-for-non-blue-members-what-you-need-to-do/

# Twitter

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

马斯克支持此次验证变革

Twitter 建议用户使用强验证方式保护帐户安全

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