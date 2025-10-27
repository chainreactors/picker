---
title: 一例ReactNative App分析
url: https://www.freebuf.com/vuls/375383.html
source: FreeBuf网络安全行业门户
date: 2023-08-19
fetch_date: 2025-10-04T12:00:24.658191
---

# 一例ReactNative App分析

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

一例ReactNative App分析

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

一例ReactNative App分析

2023-08-18 13:52:24

## 前言

最近工作中碰到一个app，发现传参是加密的，需要解密，按照之前常规的做法发现没有hook到对应的加密逻辑，最后才发现是基于ReactNative开发的，借此来浅浅地学习下ReactNative的逆向。

介绍下ReactNative，RN是Facebook开源的一个跨平台移动应用开发框架，是Facebook开源的JS框架React在原生移动应用平台的衍生产物，支持iOS和安卓两大平台。RN使用Javascript语言，类似于HTML的JSX，以及CSS来开发移动应用。

## 分析App

首先分析它的登录协议，登录界面长这样。
![image](https://image.3001.net/images/20230818/1692337751_64df0657406f6fd451f3b.png!small)

随便输入手机发送验证码，抓个包发现是加密的。
![image](https://image.3001.net/images/20230818/1692337764_64df0664108cbc5e558e1.png!small)
这里就要开始分析它的算法了。

## Java层分析

直接frida-dexdump一下，拖进工具看看java层代码，直接搜接口找了对应的接口。
![image](https://image.3001.net/images/20230818/1692337781_64df067509e59355e4922.png!small)

找到对应的调用方法。
![image](https://image.3001.net/images/20230818/1692337795_64df06838eda3e1425676.png!small)

我一开始直接对应的方法，没有输出，然后hook HashMap的put方法，发现也没有输出，这里卡了很久，后面记起来他UA是ok3，又hook了一下ok3,终于有输出了，打印了一下堆栈：
![image](https://image.3001.net/images/20230818/1692337814_64df0696cc5cfd612d97a.png!small)

发现调用栈压根没有走过我之前测试hook的那些方法，打印出了一堆react相关的调用，这里开始意识到这个app是基于ReactNative开发的。

验证下猜想，解压查看了下对应的lib目录，确实是基于ReactNative开发的。
![image](https://image.3001.net/images/20230818/1692337830_64df06a6e835ab9fda7b3.png!small)

确定了那就简单了。

## 分析JS代码

解压apk,在assets目录下，可以看到index.android.bundle文件。
这里面包含了应用主要的业务逻辑代码，我改个后缀直接放编辑器里格式化查看。
![image](https://image.3001.net/images/20230818/1692337848_64df06b8a491dcf3cb461.png!small)

里面基本主要业务的接口调用代码都在了。
![image](https://image.3001.net/images/20230818/1692337862_64df06c6b01463a691748.png!small)

继续全局搜加解密代码，发现了一处国密调用。
![image](https://image.3001.net/images/20230818/1692337873_64df06d1a973dc45d9560.png!small)

这个应用并不复杂，基本都是靠js去实现对应的加解密，里面写的比较清楚，直接把key iv拿过来进行加解密测试，发现已经能看到明文了。
![image](https://image.3001.net/images/20230818/1692337887_64df06df24d1773879e20.png!small)

## 总结

总体来看，安卓ReactNative应用分析没有那么复杂，主要的业务逻辑（index.android.bundle文件）能很容易进行分析，虽然可以混淆，但是还是能有一定的可读性。二来应用运行时不校验JS代码，可以通过hook替换JS文件实现代码注入，具备了可调试能力。

# 漏洞 # 网络安全 # SRC漏洞挖掘

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

前言

分析App

Java层分析

分析JS代码

总结

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