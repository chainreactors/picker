---
title: 苹果手机72小时不用会自动锁死？
url: https://www.freebuf.com/news/415732.html
source: FreeBuf网络安全行业门户
date: 2024-11-21
fetch_date: 2025-10-06T19:15:40.832490
---

# 苹果手机72小时不用会自动锁死？

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

苹果手机72小时不用会自动锁死？

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

苹果手机72小时不用会自动锁死？

2024-11-20 15:44:34

所属地 上海

苹果最新的移动操作系统iOS18似乎增加了一项未经记录的安全功能，如果设备在72小时内未使用，则会重新启动。这对任何试图在没有有效密码的情况下使用iOS设备的人都会产生影响，比如手机被盗或被扣押。![](https://image.3001.net/images/20241120/1732089085_673d94fd680a1aea62f63.png!small)

## **无有效密码访问数据难度叠加**

当iPhone 重新启动时，它会进入一个被称为“首次解锁”BFU 的状态。在此期间，它所包含的文件将被加密，一旦使用密码解锁，它的状态将变为首次解锁后AFU，此时，机器的安全性较低，文件基本上是可访问的，因为大多数加密密钥已加载到设备内存中。但锁屏等其他保护措施依然存在，访问某些数据，如Apple Mail、Apple Health、Keychain和位置数据可能仍然需要密码。如果他们无法通过密码获得完整访问权限，AFU是攻击者和执法机构的首选状态，因为访问的障碍较低。因此，让iPhone在72小时不活动后重新启动进入BFU会减少任何试图访问苹果硬件数据的机会窗口。

## **研究员做了相关实验**

在缺乏来自苹果的官方细节的情况下，研究员 Jiska Classen为了找到iOS18基于时间的重启行为的证据，她搜索了由研究员“blacktop”维护的[GitHub repo](https://github.com/blacktop/ipsw-diffs)，其中包含了iOS发布中使用的字符串的版本历史。最终在iOS18.1和iOS18.2中发现了“无活动\_reboot”字符串。通过深入研究Apple的Security Enclave Processor（SEP）和Apple SEP Key Store内核模块，她发现SEP在上次解锁时间超过三天后告诉内核模块，内核模块告诉用户重新启动的空间，Spring Board主屏幕管理器处理进程终止以避免数据丢失。

## **有效阻止手机被盗后的数据窃取**

Jiska Classen在媒体账户发布了实验相关细节，揭示了苹果如何实现其不活动重启机制。她披露运行iOS18的iPhone在三天后就会重新启动，即使完全脱离无线网络，而且iDevices可以指示使用旧操作系统的其他苹果移动硬件重新启动。

从安全性角度来看，这显然是一个非常强大的缓解措施。虽然执法部门将面临更大的来自办案时间的压力，但这可能会完全阻止犯罪分子窃取用户数据、其他存储在iPhone上的隐私信息。

原文参考：[https://www.theregister.com/2024/11/19/ios\_18\_secret\_reboot/?td=rt-3a﻿](https://www.theregister.com/2024/11/19/ios_18_secret_reboot/?td=rt-3a)

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

无有效密码访问数据难度叠加

研究员做了相关实验

有效阻止手机被盗后的数据窃取

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