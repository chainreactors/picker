---
title: 苹果设备发现新漏洞，可以恶意访问用户数据
url: https://www.freebuf.com/news/358452.html
source: FreeBuf网络安全行业门户
date: 2023-02-24
fetch_date: 2025-10-04T07:58:22.795221
---

# 苹果设备发现新漏洞，可以恶意访问用户数据

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

苹果设备发现新漏洞，可以恶意访问用户数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

苹果设备发现新漏洞，可以恶意访问用户数据

2023-02-23 13:53:40

所属地 上海

![](https://image.3001.net/images/20230223/1677121821_63f6d91dcba4615d8711e.png!small)

苹果公司修订了它上个月发布的安全公告，更新了影响iOS、iPadOS和macOS的三个新漏洞。

第一个漏洞是Crash Reporter组件中的一个竞赛条件（CVE-2023-23520），可使恶意攻击者以root身份读取任意文件。iPhone制造商表示，它通过额外的验证来解决这个问题。

另外两个漏洞，归功于Trellix研究员Austin Emmitt，位于Foundation框架中（CVE-2023-23530和CVE-2023-23531），可以武器化来实现代码执行。

苹果公司表示：“应用程序可能能够在其沙箱之外执行任意代码或具有某些提升的权限”，并补充说道已经通过“改进的内存处理”修补了这些问题。

在2023年1月23日发货的iOS 16.3、iPadOS 16.3和macOS Ventura 13.2中，这些中度至高度的漏洞已经得到修补。

Trellix在周二自己的报告中，将这两个漏洞归类为 "新的一类漏洞，允许绕过代码签名，在几个平台应用程序的上下文中执行任意代码，导致macOS和iOS上的权限升级和沙盒逃脱"。

这些漏洞还绕过了苹果为解决零点击漏洞而采取的缓解措施，如以色列雇佣军间谍软件供应商NSO集团利用FORCEDENTRY在目标设备上部署Pegasus。

因此，攻击者可以利用这些漏洞冲出沙盒，以更高的权限执行恶意代码，可能会允许访问日历、地址簿、信息、位置数据、通话记录、摄像头、麦克风和照片。

更要注意的的是，这些安全漏洞可以被滥用来安装任意的应用程序，甚至擦除设备。也就是说，利用这些漏洞需要攻击者已经获得了一个最初的立足点。

Austin Emmitt表示：上述漏洞代表了对macOS和iOS安全模型的重大破坏，该模型依赖于单个应用程序对所需资源的子集进行细粒度访问，并查询更高特权的服务以获取其他任何内容。

> 参考消息：thehackernews.com/2023/02/apple-warns-of-3-new-vulnerabilities.html

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