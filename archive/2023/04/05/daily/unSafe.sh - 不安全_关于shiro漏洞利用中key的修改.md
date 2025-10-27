---
title: 关于shiro漏洞利用中key的修改
url: https://buaq.net/go-157039.html
source: unSafe.sh - 不安全
date: 2023-04-05
fetch_date: 2025-10-04T11:29:13.997708
---

# 关于shiro漏洞利用中key的修改

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

![](https://8aqnet.cdn.bcebos.com/a6dce51b2f25736f2af419a64be36c11.jpg)

关于shiro漏洞利用中key的修改

首先需要准备一个shiro的漏洞环境,这里B叨叨一句,从阿里云的spring server拉回来的模板，模板引擎默认配置有毛病，真鸡儿烦人。环境主要代码
*2023-4-4 23:53:35
Author: [blog.upx8.com(查看原文)](/jump-157039.htm)
阅读量:53
收藏*

---

首先需要准备一个`shiro`的漏洞环境,这里B叨叨一句,从阿里云的`spring server`拉回来的模板，模板引擎默认配置有毛病，真鸡儿烦人。环境主要代码都是抄的`vulhub`，不是自己写的。

![](https://blog.thekingofduck.com/post-images/16347962792332/16347971709406.jpg)

要修改`shiro`的`Key` 我们应该要明白`shiro key`存在那儿。在`org.apache.shiro.mgt.AbstractRememberMeManager`这个接口中。

![](https://blog.thekingofduck.com/post-images/16347962792332/16347981125460.jpg)

注意看，这只是默认`key`而已，很多时候找到的`key`都是从配置文件里面读出来的，并非默认这个，官方提供的有接口可以获取或设置这个值。

![](https://blog.thekingofduck.com/post-images/16347962792332/16347984164953.jpg)

继承这个接口的类在`org.apache.shiro.web.mgt.CookieRememberMeManager`,可以调他获取一个看看。

![](https://blog.thekingofduck.com/post-images/16347962792332/16347998577301.jpg)

看着好像没啥毛病，但实际测试会发现这个值并不是程序真正在用的值，直接在路由里去`set`一个值也没生效，为什么？因为获取到的值就不是同一个对象里面的。程序的配置在初始化的时候就在配置类中初始化了一个`CookieRememberMeManager`对象，程序用的一直是他，而不是自己`new`出来的那个。

![](https://blog.thekingofduck.com/post-images/16347962792332/16348023443427.jpg)

那如果想设置的话也得是在这里设置。比如：

![](https://blog.thekingofduck.com/post-images/16347962792332/16348024099778.jpg)

这样是没毛病的

![](https://blog.thekingofduck.com/post-images/16347962792332/16348024854239.jpg)

可真实日站的环境中就没那么容易了，没法让你直接修改执行`Java`代码，这就得利用`Java`反射相关的技术去获取这一对象，并修改里面的值。

构造的过程会很麻烦，不通环境中遇到的情况会不一样，比如在这份代码中需要修改的bean对象的命名是`shiroFilter`而不是`shiroFilterFactoryBean`(其他环境多数为`shiroFilterFactoryBean`)，所以给的代码需要调整以下，这是不用脑子也能完成的事情。

![](https://blog.thekingofduck.com/post-images/16347962792332/16348032696144.jpg)

文章来源: https://blog.upx8.com/3398
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)