---
title: 某软件监控页面RCE漏洞分析
url: https://buaq.net/go-133268.html
source: unSafe.sh - 不安全
date: 2022-10-30
fetch_date: 2025-10-03T21:17:20.770045
---

# 某软件监控页面RCE漏洞分析

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/f77986ac1925f2dade44bbd3c8251159.jpg)

某软件监控页面RCE漏洞分析

前言今年某行动中，某OA连续发了好几个高危漏洞补丁，搜索了一下，目前网络上还没有分析文章，正好最近有时间做一下漏洞分析和学习漏洞说明后台监控页面对传入参数为进行
*2022-10-29 21:22:34
Author: [xz.aliyun.com(查看原文)](/jump-133268.htm)
阅读量:55
收藏*

---

### 前言

今年某行动中，某OA连续发了好几个高危漏洞补丁，搜索了一下，目前网络上还没有分析文章，正好最近有时间做一下漏洞分析和学习

### 漏洞说明

后台监控页面对传入参数为进行处理，导致命令执行

### 修复原理

补丁代码直接删除了后面一大段代码，我们分析一下这一段代码危害

首先登陆系统后访问下面链接，进入monitor页面，访问后台监控页面的jsp
<http://x.x.x.x/ctp/sysmgr/monitor/status.do>
![](https://xzfile.aliyuncs.com/media/upload/picture/20221029210450-45aa2448-578a-1.png)

点击访问Cache Dump页面
![](https://xzfile.aliyuncs.com/media/upload/picture/20221029202707-00b71490-5785-1.png)

这里访问会加载index.jsp，同时会在session设置GoodLuckA8，后续才能访问到漏洞页面
![](https://xzfile.aliyuncs.com/media/upload/picture/20221029211227-55d5ab5c-578b-1.png)

cacheDump.jsp 这里判断是否session存在GoodLuckA8了
![](https://xzfile.aliyuncs.com/media/upload/picture/20221029211421-99cdf490-578b-1.png)

抓这个页面的包，继续操作
![](https://xzfile.aliyuncs.com/media/upload/picture/20221029205244-94e34da2-5788-1.jpeg)

cacheDump.jsp 这里传入b、m、p三个参数
![](https://xzfile.aliyuncs.com/media/upload/picture/20221029224059-b44c83de-5797-1.png)

这里符合条件会调用eval方法
![](https://xzfile.aliyuncs.com/media/upload/picture/20221029203029-796b388a-5785-1.png)

跟进到eval方法，拼接beanName、func、param这个三个参数
![](https://xzfile.aliyuncs.com/media/upload/picture/20221029203804-883a250a-5786-1.png)

进行ScriptEvaluator.eval 方法，可以看到这里用到groovy，继续跟进77行
![](https://xzfile.aliyuncs.com/media/upload/picture/20221029203109-912c8834-5785-1.png)

最后这块编译文件，执行groovy代码
![](https://xzfile.aliyuncs.com/media/upload/picture/20221029203127-9bc0d53e-5785-1.png)

### 漏洞复现

p参数这里设置成下面的groovy代码，然后进行url编码，即可导致RCE

```
1); println "cmd /c calc".execute().text //
```

漏洞分析完，poc其实挺容易构造，完整的漏洞数据包有点敏感，暂时不公布了

效果：
![](https://xzfile.aliyuncs.com/media/upload/picture/20221029210746-aeb42ee8-578a-1.png)

### 免责申明

本文中提到的漏洞分析过程仅供研究学习使用，请遵守《网络安全法》等相关法律法规

文章来源: https://xz.aliyun.com/t/11778
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)