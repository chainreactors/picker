---
title: SUPER站群命令执行之官方审核
url: https://buaq.net/go-135230.html
source: unSafe.sh - 不安全
date: 2022-11-12
fetch_date: 2025-10-03T22:28:47.028704
---

# SUPER站群命令执行之官方审核

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

![](https://8aqnet.cdn.bcebos.com/c27e3d6f8fc77f7c478e98caae7e52f7.jpg)

SUPER站群命令执行之官方审核

某站群原来是我们内部自己开发使用的一套程序，后来看到很多人有相似的需求，团队决定发布出来免费开源给大家使用。某公司某站群最新版本存在文件上传漏洞，攻击者可利用该漏洞获取服务器控制权限
*2022-11-11 17:16:24
Author: [www.secpulse.com(查看原文)](/jump-135230.htm)
阅读量:35
收藏*

---

某站群原来是我们内部自己开发使用的一套程序，后来看到很多人有相似的需求，团队决定发布出来免费开源给大家使用。某公司某站群最新版本存在文件上传漏洞，攻击者可利用该漏洞获取服务器控制权限。

适合用在什么场景？推荐有建站基础，懂得SEO的专业人士使用，可用于养域名养权重，关键词流量站、蜘蛛池、企业站乃至个人博客都可以使用。

[![1668129031_636da107a986bc1d305e7.jpg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/1668129031_636da107a986bc1d305e7.jpg "1668129031_636da107a986bc1d305e7.jpg")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/1668129031_636da107a986bc1d305e7.jpg)

官网下载：https://www.cmssuper.com/

下载地址点击以后跳转此页面，点击下载谷歌是没有反应的，360和ie是可以的，谷歌浏览器报错

 `Mixed Content: The site at '<URL>' was loaded over a secure connection, but the file at '<URL>' was loaded over an insecure connection. This file should be served over HTTPS. This download has been blocked. See <URL> for more details.`

 提示遇到https和http不兼容问题

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157878.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157879.png)

打开调试，直接点击url就可以下载或者是改成https点击下载就可以下载了。但是官方审核到了三级验证中了，点击下载没反应就直接给驳回了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157880.jpeg)

然后我又重新在文档做了说明，并下载了安装包放到附件里边重新提交的，又要从一级审核开始。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157881.png "null")

官方大人审核，不敢多言，直接上过程。

下载安装包安装完以后， 此时登录后台程序：

后台效果

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157882.png)

进入后台以后：点击系统设置->模板风格->可以下载其他模板以后，点击编辑模板，站点选择该模板。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157883.png)

复制此段程序：找到首页模板，复制进去，点击保存就可以了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157884.png)

保存完，运行前端，会在根目录下生成文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157885.png)

会在根目录下生成muma.php

恶意代码：

```
<?php

$file=fopen("muma.php","w");//根目录创建muma.php文件

?>
```

运行完以后，域名+muma.php

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-16681578851.png)

使用蚁剑链接木马，获得服务器权限：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157886.png)

查看数据配置信息：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-16681578861.png)

点击保存，获取到这个地址。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157887.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157888.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157892.png)

找到保存方法，获取body内容，stripslashes 函数对内容反斜杠处理，对非法内容并没有过滤。

至此，通过系统后台文件编辑，通过非法代码，运行文件，实现写入木马程序执行，拿到了服务器全部权限、源码，以及数据库信息，造成了很严重的后果。

E

N

D

**本文作者：[TideSec](https://www.secpulse.com/archives/newpage/author?author_id=26366)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/190926.html**](https://www.secpulse.com/archives/190926.html)

文章来源: https://www.secpulse.com/archives/190926.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)