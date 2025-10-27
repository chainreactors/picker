---
title: 速查！安卓系统可能遭遇重大风险，两分钟可轻松破解锁屏
url: https://www.freebuf.com/news/349886.html
source: FreeBuf网络安全行业门户
date: 2022-11-16
fetch_date: 2025-10-03T22:53:14.856675
---

# 速查！安卓系统可能遭遇重大风险，两分钟可轻松破解锁屏

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

速查！安卓系统可能遭遇重大风险，两分钟可轻松破解锁屏

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

速查！安卓系统可能遭遇重大风险，两分钟可轻松破解锁屏

2022-11-15 16:50:46

所属地 上海

安卓系统可能遭遇了重大安全风险，只要能拿到对方的手机，就有可能轻松破解手机的锁屏密码。

一次偶然的机会，国外网络安全研究员 David Schütz发现了一种极为简单的绕过谷歌Pixel 6 和 Pixel 5 智能手机的锁屏的方法，任何拿到手机的用户都可以解开手机。![](https://image.3001.net/images/20221115/1668502142_6373527e1a1dceaa758d2.jpg!small)

整个过程只需要简单的五个步骤，大概两分钟的时间。虽然谷歌针对这个问题已经发布了Android 更新，而在更新之前，这个锁屏漏洞持续存在超过五个月的时间。

## ****五步直接绕过Android锁屏****

Schütz表示，他是在自己的Pixel 6 电池没电、输错 3 次 PIN 并使用 PUK（个人解锁密钥）代码恢复锁定的 SIM 卡后，发现了这个漏洞。

令他惊讶的是，在解锁 SIM 卡并选择新的 PIN 码后，设备并没有要求输入锁屏密码，而只是要求进行指纹扫描。

出于安全原因，Android 设备在重新启动时总是要求输入锁屏密码或图案，因此直接进行指纹解锁不正常。

Schütz继续进行试验，当他尝试在不重启设备的情况下重现漏洞时，他认为也可以绕过指纹提示，直接进入主屏幕。

总的来说，对于该漏洞的利用主要有以下五个步骤。

* 提供三次错误指纹以禁用锁定设备上的生物特征认证；
* 将设备中的 SIM 卡与设置了 PIN 码的攻击者控制的 SIM 卡热交换；
* 提示输入错误的 SIM 卡密码三次，锁定 SIM 卡；
* 设备提示用户输入 SIM 的个人解锁密钥 (PUK) 码，这是一个唯一的 8 位数字，用于解锁 SIM 卡；
* 为攻击者控制的 SIM 输入新的 PIN 码。

## ****漏洞影响广泛****

该安全漏洞的影响十分广泛，几乎所有未更新2022年11月补丁的，运行 Android 10、11、12 、13 版本的手机都受到影响，这是一个无法想象的数量。

虽然这个漏洞利用需要对拿到对方的手机，但是这依旧会产生巨大的影响，尤其是对于那些虐待他人、接受调查、手机丢失的用户来说，影响十分严重。

该问题是由于 SIM PUK 解锁后键盘锁被错误地关闭引起的，原因是关闭调用的冲突影响了在对话框下运行的安全屏幕堆栈。

当 Schütz 输入正确的 PUK 号码时，“解除”功能被调用两次，一次由监视 SIM 状态的后台组件调用，另一次由 PUK 组件调用。

这不仅会导致 PUK 安全屏幕被取消，还会导致堆栈中的下一个安全屏幕（键盘锁）被取消，随后是堆栈中下一个排队的任何屏幕。如果没有其他安全屏幕，用户将直接访问主屏幕。

谷歌的解决方案是为每个“关闭”调用中使用的安全方法包含一个新参数，以便调用关闭特定类型的安全屏幕，而不仅仅是堆栈中的下一个。

2022年6月， Schütz 向谷歌报告了这一安全漏洞，编号 CVE ID  CVE-2022-20465，但是直到2022年11月7日，谷歌才正式对外公布了该漏洞的修复补丁。另外，因为这个安全漏洞， Schütz 获得了谷歌的7万美元的高额奖励。

## **参考来源**

> https://www.bleepingcomputer.com/news/security/android-phone-owner-accidentally-finds-a-way-to-bypass-lock-screen/

# 网络安全 # 系统安全 # 数据安全 # 网络安全技术

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

五步直接绕过Android锁屏

漏洞影响广泛

参考来源

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