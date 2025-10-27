---
title: 绿联NAS存在严重安全问题？官方回应来了
url: https://www.freebuf.com/articles/405425.html
source: FreeBuf网络安全行业门户
date: 2024-07-09
fetch_date: 2025-10-06T17:45:07.811303
---

# 绿联NAS存在严重安全问题？官方回应来了

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

绿联NAS存在严重安全问题？官方回应来了

* ![]()
* 关注

绿联NAS存在严重安全问题？官方回应来了

2024-07-08 11:58:54

所属地 上海

据国内多家媒体报道，绿联NAS产品存在严重安全问题，此前该产品在上市之初还曾遭遇了下架风波。

据B站up主发现，绿联NAS系统控制面板中提供的两个域名的通配符证书，\*.ugnas.cloud 和 \*.ugnas.com，存在泄露用户私密数据的风险。对此绿联官方作出回应，称此问题仅存在于UGOS PRO体验账号中，并未在正式用户的设备上使用。

由于该事件在安全圈内引发热烈的讨论，接下来咱们就来梳理一下。

## ****绿联NAS安全问题到底有多严重？****

这里先简单介绍一下，什么是NAS。

NAS 即 Network Attached Storage，网络附属存储。NAS 是一种文件级存储架构，可使存储的数据更易于网络设备访问，是三种主要存储架构之一。NAS 的作用就好像一个塞了很多硬盘的电脑，里面有文件服务器和管理软件啥的，专用于储存、共享文件。连到自己的网上，你就可以搭建自己的“网盘”了。

该事件起因是哔哩哔哩 UP 主 @某摆烂闲鱼 发布的一条视频，指出绿联NAS存在严重的安全问题，可能会导致用户信息泄露。在视频里可以看到，绿联 NAS 在其系统控制面板中向用户提供 \*.ugnas.cloud 和 \*.ugnas.com 两个域名的通配符证书。如下图所示：

![1720411061_668b63b5e0424aa642a92.png!small?1720411062498](https://image.3001.net/images/20240708/1720411061_668b63b5e0424aa642a92.png!small?1720411062498)

图片来源：蓝点网

但问题是，绿联竟然向所有用户公开了TLS 证书和私钥，用户只需要下载即可。。。

搞安全的同学看到这应该已经有点挠头了，有了证书和私钥，人人都可以部署恶意软件进行劫持，用户数据几乎没有任何安全性可言。最典型的莫过于发起 MiTM 中间人攻击来窃取账号和密码等敏感数据。

该消息公布之后引起安全人的广泛讨论。有人猜测绿联最初目的应该是为了方便用户使用，提高产品体验。

众所周知，通配符证书可以保护一个主域及其下一级的多个子域，且在提供安全保护的时候节省管理时间。通配符证书可以涵盖所有的子域名，相较于为每个子域名单独购买证书，购买一张通配符证书可以直接解决。验证了通配符证书之后，如果后续需要新增同级的子域名，无需重新审核，也不用额外付费，直接就可以扩展，非常方便。

但万万不该将私钥也全部面向用户公开下载，这岂不是人人都有一把防盗门的钥匙，即便防盗门再坚固也无任何作用。

据蓝点网报道，B站UP主把绿联 NAS 证书导入服务器进行中间人劫持测试，结果显示，测试结果有效，会对用户造成明显影响。在视频中，UP主成功劫持了自己的服务器，这就相当于遭受了DNS污染，将绿联NAS指向了恶意服务器。如果被别有用心的人利用，攻击是完全有可能实现的，用户会因此泄漏数据。具体如下所示：

![1720411085_668b63cd544ecc4f866a0.png!small?1720411085694](https://image.3001.net/images/20240708/1720411085_668b63cd544ecc4f866a0.png!small?1720411085694)

![1720411092_668b63d42f32727f10c80.png!small?1720411092532](https://image.3001.net/images/20240708/1720411092_668b63d42f32727f10c80.png!small?1720411092532)

图片来源：蓝点网

绿联NAS这波操作属实是有点迷，将证书和私钥全部公开给用户，不仅自身产品存在安全风险，同时也将绿联 NAS 用户置于风险之中。值得一提的是，由于上述问题并非一个严格意义上的安全漏洞，目前该证书风险点已经被封，因此不会引发后续的安全问题。

## ****绿联官方回应****

对于B站UP主揭露的问题，绿联官方也进行回应，称此问题仅存在于UGOS PRO体验账号中，并未在正式用户的设备上使用。

![1720411129_668b63f9dfa3a1c3e9219.png!small?1720411129954](https://image.3001.net/images/20240708/1720411129_668b63f9dfa3a1c3e9219.png!small?1720411129954)

绿联表示，已定位到该问题属于体验账号，正式用户设备上没有这个证书，也不会用到这个证书和私钥，对正式用户不会有任何影响。

同时已经吊销该体验账号的证书，并称绿联 NAS 私有云团队非常重视并以力求保障用户数据安全，感谢对绿联 NAS 私有云的支持。

2024年 5 月，绿联科技推出了 NAS 私有云 DXP 系列九款新品，同时还带来了全新自研 NAS 系统 UGOS Pro，但新系统首发没有达到预期，存在部分 Bug 需要时间来修复，例如部分产品 CPU 温度显示异常与负载过高、部分用户账号注册异常等。

## 参考来源

[https://baijiahao.baidu.com/s?id=1803874989838291782𝔴=spider&for=pc](https://baijiahao.baidu.com/s?id=1803874989838291782&wfr=spider&for=pc)

<https://mp.weixin.qq.com/s/jlBvhAC4ZFRtXbGooEVHrQ>

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

绿联NAS安全问题到底有多严重？

绿联官方回应

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