---
title: 小心！这些安装了 200 万次的 Android 键盘应用程序可以被远程入侵
url: https://www.freebuf.com/news/351574.html
source: FreeBuf网络安全行业门户
date: 2022-12-06
fetch_date: 2025-10-04T00:34:44.739931
---

# 小心！这些安装了 200 万次的 Android 键盘应用程序可以被远程入侵

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

小心！这些安装了 200 万次的 Android 键盘应用程序可以被远程入侵

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

小心！这些安装了 200 万次的 Android 键盘应用程序可以被远程入侵

2022-12-05 11:46:31

所属地 上海

[![Android 远程键盘应用程序](https://image.3001.net/images/20221205/1670211994_638d699a0a537b5b4c998.png!small "Android 远程键盘应用程序")](https://thehackernews.com/new-images/img/b/R29vZ2xl/AVvXsEgQrGQZnw71xbHna91_XFGhMxRYuui5j1sbAmGTkQTph4ohlJeVpMn-iP0tbxXCE4tk29iTpgc0LT9ZcRswHblSlG9Eug9EUgQcsFDv0VBtBx_wZTjjjStjh7X7XcvuHX-9V4j9HI8AS9zJlU6d5kW2qKmqscEFMvfAFs_o6EG1zFM5JQBIDr-AA7W-/s728-e100/apps.png)

近日，Synopsys 安全研究人员发现，在可以将智能手机用作远程键盘和鼠标的三个 Android 应用程序中存在多个未修补的漏洞。

这些应用程序分别是**Lazy Mouse**、**PC Keyboard**和**Telepad**，它们已从 Google Play 商店累计下载超过 200 万次。其中Telepad 不再能通过应用商店下载，但可以从其网站下载。

* 懒惰鼠标（com.ahmedaay.lazymouse2 和 com.ahmedaay.lazymousepro）
* PC 键盘 (com.beapps.pckeyboard)
* Telepad (com.pinchtools.telepad)

虽然这些应用程序通过连接到桌面上的服务器来代替鼠标键盘的运行，但是Synopsys 网络安全研究中心 (CyRC)发现了多达七个与弱身份验证或缺少身份验证、缺少授权和不安全通信相关的缺陷。

简而言之，这些问题（从 CVE-2022-45477 到 CVE-2022-45483）可能会被恶意攻击者利用来执行任意命令，无需身份验证通加载用户的击键来获取敏感信息。

Lazy Mouse 服务器还受到弱密码策略的影响，但其并没有实施速率限制，使远程未经身份验证的攻击者能够轻易地暴力破解 PIN 并执行命令。

更值得注意的是，两年多来这些应用程序没有任何更新，因此用户最好立即删除这些应用程序。

Synopsys 安全研究员 Mohammed Alshehri 表示：这三个应用程序被广泛使用，但它们既没有考虑到用户的隐私安全也没有进行任何迭代，显然，在开发这些应用程序时，安全性并不在他们的设计范围内。

> 参考来源：https://thehackernews.com/2022/12/watch-out-these-android-keyboard-apps.html

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