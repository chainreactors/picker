---
title: 本站已升级到PHP 8.0
url: https://buaq.net/go-140416.html
source: unSafe.sh - 不安全
date: 2022-12-18
fetch_date: 2025-10-04T01:51:11.549146
---

# 本站已升级到PHP 8.0

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

![]()

本站已升级到PHP 8.0

PHP WordPress本站出于Wordpress的兼容性考虑，一直用的PHP 7.4版本。随着PHP 7.4不再维护，以及本月PHP 8.2正式发布，是时候需要迁移到仍在维护中的PHP 8.x版
*2022-12-17 22:16:24
Author: [itlanyan.com(查看原文)](/jump-140416.htm)
阅读量:44
收藏*

---

[PHP](https://itlanyan.com/category/php/) [WordPress](https://itlanyan.com/category/php/wordpress/)

本站出于Wordpress的兼容性考虑，一直用的PHP 7.4版本。随着[PHP 7.4不再维护](https://www.php.net/supported-versions.php)，以及[本月PHP 8.2正式发布](https://www.php.net/archive/2022.php#2022-12-08-1)，是时候需要迁移到仍在维护中的PHP 8.x版本。

PHP 8.0最吸引本人的新特性是合并了诸多性能优化，尤其是备受期待的JIT(Just in Time)编译器，能进一步提升PHP脚本的运行速度。根据官方性能测试脚本，PHP 8.0在PHP 7.4的基础上有大约10%的性能提升。PHP 8新特性详解请参考 [一文详解PHP 8新特性](https://itlanyan.com/new-in-php-8/)。

[根据WordPress官方数据](https://make.wordpress.org/core/handbook/references/php-compatibility-and-wordpress-versions/)，WordPress自5.6版本开始支持PHP8.0，5.9开始支持PHP 8.1，6.1开始支持PHP8.2。本站用的最新的WordPress 6.1版本，谨慎起见选择了PHP 8.0。

安装完成后，`php -v`命令输出如下：

```
[[email protected] ~]# php -v
PHP 8.0.26 (cli) (built: Dec 5 2022 21:59:43) ( NTS )
Copyright (c) The PHP Group
Zend Engine v4.0.26, Copyright (c) Zend Technologies
with Zend OPcache v8.0.26, Copyright (c), by Zend Technologies
```

根据鸟哥[PHP 8新特性之JIT简介](https://www.laruence.com/2020/06/27/5963.html)中的介绍，JIT基于Opcache，因此其配置均在Opcache模块下。PHP官网英文手册的Opcache模块已经有[JIT配置参数详细说明](https://www.php.net/manual/en/opcache.configuration.php)，中文手册页面尚未同步。本站使用的JIT配置为：

```
opcache.jit=tracing
opcache.jit_buffer_size=64M
opcache.jit_hot_func=32
```

不过因为本站使用了[Nginx fastcgi\_cache](https://itlanyan.com/use-nginx-cache-accelerate-wordpress-site/)和WP Super Cache缓存技术，并且对热门文章做了预缓存，PHP性能早就不是瓶颈。另外根据 [stitcher的性能测试](https://stitcher.io/blog/jit-in-real-life-web-applications)，PHP 8对web应用性能提升并不明显，因此大部分访客应该感觉不到有速度的提升。

升级到PHP8.0后，测试了半个多小时未发现会对用户访问产生问题。但是本站使用的[BunnyPress主题](https://itlanyan.com/support-article-table-of-contents/)许久未更新，服务端会出现一些warning日志，根据提示稍微修改源码即可。除此之外，未看到兼容性或使用上的问题。

## 参考

1. [PHP 8新特性之JIT简介](https://www.laruence.com/2020/06/27/5963.html)
2. [WordPress性能优化](https://itlanyan.com/wordpress-performance-optimization/)
3. [WordPress 6.0, PHP 8.1, and the Upcoming EOL of PHP 7.4](https://pagely.com/blog/wordpress-6-0-php-8-1-upcoming-eol-php-7-4/)

赞

文章来源: https://itlanyan.com/server-upgrade-to-php8/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)