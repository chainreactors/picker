---
title: Apple地理定位API暴露了全球WiFi接入点
url: https://www.freebuf.com/news/405505.html
source: FreeBuf网络安全行业门户
date: 2024-07-10
fetch_date: 2025-10-06T17:45:13.792830
---

# Apple地理定位API暴露了全球WiFi接入点

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

Apple地理定位API暴露了全球WiFi接入点

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Apple地理定位API暴露了全球WiFi接入点

2024-07-09 10:36:12

所属地 上海

![1720493706_668ca68ae1f9b7b5aa654.png!small?1720493707758](https://image.3001.net/images/20240709/1720493706_668ca68ae1f9b7b5aa654.png!small?1720493707758)

苹果公司的 Wi-Fi 定位系统 （WPS）可用于绘制和跟踪全球的 Wi-Fi 接入点  （AP） 。

在 2024 年黑帽大会的演讲中，马里兰大学研究员 Erik Rye 将演示他是如何在几天内绘制出数亿个接入点的地图的，而在绘制过程中甚至不需要苹果设备或任何权限。

## 苹果是如何暴露全球接入点

你有没有想过，你的手机是如何判断确切位置的？虽然大多都使用全球定位系统（GPS）这种工具，但这并不是万能的。它可能存在很多潜在的问题，比如信号不佳、耗电量大等等，对于那些持久性任务来说并不理想。

但相对而言，Wi-Fi 定位系统就比较适用。WPS 的工作原理有点像 GPS，只是将卫星换成了 Wi-Fi 接入点（AP）。

首先，运行苹果或谷歌操作系统的设备会定期报告它们的位置（通过 GPS 或基站三角测量），以及附近网络的相对信号强度（通过基本服务集标识符或 BSSID 标识），从而显示它们之间的距离。通过这种众包方式，这些公司开发出了全球 AP 位置的庞大数据库。

正如Rye所解释的那样：不管你是否使用苹果设备，但只要使用苹果设备的人路过你家、给你送包裹或住在你家附近，那么你的 Wi-Fi 接入点就可能会出现在这个系统中。

因此，单个设备可以通过扫描附近的 Wi-Fi 网络并将其报告给公司服务器，从而确定自己的位置。在苹果公司的案例中，WPS 服务器会返回这些 Wi-Fi 网络的位置，设备可以将其与观察到的信号强度进行比较，从而确定自己的相对位置。那么，问题出在哪里呢？

要知道，苹果的 WPS API 是开放和免费使用的，是专为苹果设备设计的，然而，可查询的权限却没有什么限制。任何人都可以通过非苹果设备进行查询，无需任何形式的身份验证或 API 密钥。

Rye 使用 Go 编写并在 Linux 上运行的程序，强行猜测了大量 BSSID 号码，直到最终找到一个真实的号码，WPS API 端点为此向他提供了一组与之相近的其他 BSSID。

他解释说：一旦你开始获得点击率，你就可以进行所谓的“滚雪球式采样”，将这些信息反馈回去，不断重复采样。在不到一周的时间里，我们就积累了大约 5 亿个独特的 BSSID。

苹果公司 WPS 的一个特殊功能提高了这一过程的效率。在响应位置查询时，它不会只返回附近的几个网络，而是会主动返回多达 400 个结果。

## 苹果地理位置API存在的风险是什么？

Rye 表示，苹果地理位置API基本上能够绘制出地球的 Wi-Fi 地图，包括一些最偏远的地方： 南极洲、大西洋中部的小岛。它甚至能绘制出一张在饱受战争蹂躏的乌克兰提供互联网接入服务的星链接入点地图，或者一张不断变化的加沙互联网接入图，这可能都是非常有价值的军事情报。

更有针对性的隐私攻击可能涉及在个人搬家或使用移动接入点（比如在房车里）旅行时对其进行跟踪。
那么既然苹果和谷歌都有 WPS，为什么我们只挑其中一个呢？虽然这两个系统都使用庞大的全球 BSSID 数据库来三角定位设备位置。但是当安卓设备查询谷歌的 WPS API 时，谷歌的服务器会进行三角测量并回复结果，而不是回复一长串 BSSID。这样，所有额外的数据都不会泄露。

谷歌还要求用户提供 API 密钥，并利用该密钥对查询收取费用（最多为每两次请求收取 1 美分）。这对于普通用户来说微不足道，但对于攻击者来说，这个微小的成本就会让他们望而却步，因为他们需要猜测大量的 BSSID，然后才能找到真正的 BSSID。

以上只是苹果公司、接入点制造商甚至立法者可以改进接入点安全性的众多方法中的两种。同时，个人也可以采取一些预防措施。

Rye 表示，如果你是一个特别精通技术的用户，在运行 OpenWrt 或类似的软件时，你可以自己手动随机化 BSSID，但这超出了大多数人的能力范围。

如果想完全避免安全风险，可以使用旅行接入点，并在搬家时采用新的接入点。苹果公司表示，如果在网络名称末尾添加'\_nomap'，可阻止你的 Wi-Fi 接入点进入他们的系统。

> 参考来源：[Apple Geolocation API Exposes Wi-Fi Access Points Worldwide (darkreading.com)](https://www.darkreading.com/endpoint-security/apple-geolocation-api-exposes-wi-fi-access-points-worldwide)

# 苹果 # wifi安全 # WiFi设备

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

苹果是如何暴露全球接入点

苹果地理位置API存在的风险是什么？

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