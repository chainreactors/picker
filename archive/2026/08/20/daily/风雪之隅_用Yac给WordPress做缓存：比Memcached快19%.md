---
title: 用Yac给WordPress做缓存：比Memcached快19%
url: https://www.laruence.com/2026/08/20/6420.html
source: 风雪之隅
date: 2026-08-20
fetch_date: 2026-08-21T03:03:50.036072
---

# 用Yac给WordPress做缓存：比Memcached快19%

[Press "Enter" to skip to content](#main)

[风雪之隅](https://www.laruence.com)

左手代码右手诗

open menu

mobile menu toggle button

* [主页](http://www.laruence.com/)
* [PHP源码分析](http://www.laruence.com/php-internal)
* [PHP应用](http://www.laruence.com/php)
* [JS/CSS](http://www.laruence.com/jscss)
* [随笔](http://www.laruence.com/notes)
* [留言](https://www.laruence.com/guestbook)
* [博客地图](https://www.laruence.com/sitemap)

# 用Yac给WordPress做缓存：比Memcached快19%

Published on [20 August 2026](https://www.laruence.com/2026/08) by [laruence](https://www.laruence.com/author/laruence)

这个博客（laruence.com）跑了十几年，对象缓存一直用的是 Memcached。稳定、经典，没出过什么问题，但每次读缓存都要走一次 localhost TCP：连接管理、协议编解码、网络往返，单条几十微秒，一个 WordPress 请求要读几十上百次，加起来就是毫秒级的固定开销——而且这部分开销和命中率无关，命中了也逃不掉。

[Yac（Yet Another Cache）](https://www.laruence.com/2013/03/18/2846.html)是我 2013 年写的一个 PHP 扩展，思路很直接：把缓存放进 FPM master 进程创建的共享内存里，所有 worker fork 时直接继承。没有缓存服务器，没有 socket，没有网络——`get()` 就是本进程地址空间里的一次 hash 查找。这么多年下来，大量生产环境验证了它的稳定。这次我想试试：拿它替换 WordPress 的 Memcached，到底能省多少？

于是我今天又奴役AI，花费300多，写了一个Wordpress插件（申明，我是真的会写PHP的，并且写的很好，只是它写的比我快😂）：[WP Yac Object Cache](https://github.com/laruence/wordpress-yac-cache)：一个自带 `object-cache.php` drop-in 的 WordPress 插件，激活即部署，后台带完整的状态面板。

![WP Yac 后台面板](https://www.laruence.com/medias/2026/08/wp-yac-admin-dashboard-v2.png)

后台面板：Active 状态条、键槽水位环形图、命中率、内存健康建议和计数器，一屏看完缓存的全部状态。

## 压测：Yac vs Memcached

### 环境

* 站点：https://www.laruence.com，真实 WordPress 站点，首页完整渲染（非静态页、非 API 桩）
* 服务器：8 核 / 31G，PHP 8.1 FPM，Nginx
* Memcached：memcached 服务（localhost:11211）+ 官方 `memcached` 扩展 drop-in
* Yac：WP Yac v1.0.0，`yac.keys_memory_size=4M`，`yac.values_memory_size=64M`

### 方法

两个方案严格对称地跑，只换 drop-in，其他一切不动：

* `wp cache flush` 清空缓存
* 重启 php-fpm（Yac 组同时获得全新共享内存，起点一致）
* 500 请求预热
* `ab -t 30 -c <并发>`，并发取 20 / 50 / 100 三档

### 结果

| 并发 | Yac RPS | Memcached RPS | 提升 | Yac p50 | Mem p50 | Yac p95 | Mem p95 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | 141.6 | 118.7 | +19.3% | 139ms | 167ms | 192ms | 216ms |
| 50 | 140.6 | 118.5 | +18.6% | 353ms | 420ms | 407ms | 465ms |
| 100 | 142.1 | 118.4 | +20.1% | 699ms | 840ms | 754ms | 886ms |

每档 30 秒，3500~4200 个完整页面渲染，全部 200，0 失败。

![Yac vs Memcached 吞吐对比](https://www.laruence.com/medias/2026/08/wp-yac-rps-benchmark.png)

图1：三档并发下 Yac 与 Memcached 的吞吐对比，提升幅度恒定在 ~19%

### 几个观察

**1. 优势恒定在 ~19%，不随并发变化。**两组的吞吐都在 20 并发时就饱和了（Yac 从 141.6 到 100 并发的 142.1，几乎一条直线），天花板是 PHP 渲染 + MySQL，不是缓存。Yac 的领先来自每个请求里省掉的几十次 localhost TCP 往返——这是固定开销，所以提升比例稳定。

**2. 吞吐饱和后，延迟随并发线性增长。**c100 的 p50（699ms）约是 c20（139ms）的 5 倍——排队论的标准形态：服务速率不变，队列变长。单机的真实容量就在这个量级，再要提升得动 OPcache、页面缓存或多机部署，而不是继续优化对象缓存。

**3. 交叉验证。**换 `ab -n 10000 -c 100` 的固定请求数测法，结论一致（Yac 141.8 vs Memcached 120.6，+17.6%）。

省掉的到底是什么？一个 WordPress 首页请求要做几十到上百次 `wp_cache_get`（options、terms、post meta……）。Memcached 每次命中也是一次 localhost TCP 往返；Yac 是进程内共享内存的一次 hash 查找。差距不在"命中与否"，而在"命中之后花多少代价拿到值"。

## 安装

先装 Yac 扩展，三种方式任选：

```

# PECL
pecl install yac

# PIE(PHP Foundation 的 PECL 继任者,yac 已在 Packagist)
pie install laruence/yac

# 源码编译
git clone https://github.com/laruence/yac.git && cd yac
phpize && ./configure && make && sudo make install
```

然后 `php.ini` 里启用 `extension=yac.so`。

### 方式一：WP-CLI（推荐）

```

wp plugin install https://github.com/laruence/wordpress-yac-cache/releases/latest/download/wp-yac-cache.zip --activate
```

### 方式二：GitHub Release

到 [Releases 页面](https://github.com/laruence/wordpress-yac-cache/releases)下载 `wp-yac-cache.zip`，WordPress 后台 → 插件 → 安装插件 → 上传，激活即可。

### 配置

激活后 drop-in 自动部署到 `wp-content/object-cache.php`。在 `wp-config.php` 的 "That's all, stop editing!" 之前加两行：

```

define( 'WP_CACHE', true );
define( 'WP_CACHE_KEY_SALT', '一段长随机字符串,每个站点唯一' );
```

可选调优（php.ini）：

```

yac.enable = 1
yac.keys_memory_size = 4M      ; 约 32K 槽位
yac.values_memory_size = 64M   ; alloptions 大的站点调大
```

插件已提交 WordPress.org 插件目录审核，通过后可以直接在 WordPress 后台搜索安装——不过考虑到审核速度，等着吧。

## 使用说明

* **单机最适合**：Yac 是本机共享内存缓存，单机（或少量互不同步的节点）场景收益最大；多机集群需要共享一致缓存时，Memcached/Redis 的网络共享反而是特性
* **flush 的语义**：`wp_cache_flush()` 会清空这台机器上的整块 Yac 共享内存，包括同一 PHP 池里其他 Yac 用户的数据。后台按钮有确认弹窗，想清楚再按
* **降级**：没装 Yac 扩展时 drop-in 退化为请求内缓存，站点照常工作
* **后台面板**：Tools → Yac Object Cache，有内存水位、命中率、容量建议和自检

## 结语

对象缓存其实不是这个站点的瓶颈——压测数据说得很清楚，142 RPS 的天花板在 PHP 渲染和 MySQL。但同样的天花板之下，Yac 把每个请求的固定开销削掉了一截：同条件快 ~19%，延迟低 ~15%，而且少维护一个 Memcached 服务。对大家自己的 WordPress来说，应该是值得换一换的吧？😂

项目地址：[github.com/laruence/wordpress-yac-cache](https://github.com/laruence/wordpress-yac-cache)（GPLv2）

### Related Posts

* [Yac 2.1 升级说明](https://www.laruence.com/2020/03/25/5657.html)
* [Yac (Yet Another Cache) - 无锁共享内存Cache](https://www.laruence.com/2013/03/18/2846.html)
* [PHP7 VS HHVM (Wordpress)](https://www.laruence.com/2014/12/18/2976.html)

Filed in [PHP Extension](https://www.laruence.com/category/phpext "View all posts in PHP Extension"), [PHP应用](https://www.laruence.com/category/php-usage "View all posts in PHP应用")

* [cache](https://www.laruence.com/tag/cache "View all posts tagged cache")
* [memcache](https://www.laruence.com/tag/memcache "View all posts tagged memcache")
* [wordpress](https://www.laruence.com/tag/wordpress "View all posts tagged wordpress")
* [yac](https://www.laruence.com/tag/yac "View all posts tagged yac")
* [性能优化](https://www.laruence.com/tag/%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96 "View all posts tagged 性能优化")

Previous Post
[Wechatian: 让AI有事就来微信找你](https://www.laruence.com/2026/08/17/6297.html)

No Newer Posts
[Return to Blog](https://www.laruence.com)

## 3 Comments

1. ![dust](https://cravatar.com/avatar/0cde6daa3a49390b2957662bf4931f7e?s=48&r=g)

   dust
   August 21, 2026

   yac 很有用啊，解决了单机高并发请求缓存问题，例如本地配置文件。场景，单服务器多容器部署，无配置中心时，yaf 大型项目多目录结构多配置文件频繁切换，频繁读取本地配置文件导致文件最大句柄超出服务器最大数而瘫痪，使用redis 增加网络请求。

   [Reply](https://www.laruence.com/2026/08/20/6420.html?replytocom=560943#respond)

   * ![laruence](https://cravatar.com/avatar/3fa56da8f74aff22ae4e0427f7103837?s=48&r=g)

     [laruence](https://www.laruence.com/)
     August 21, 2026

     如果是静态不变的配置文件话，建议使用[yaconf](https://www.github.com/laruence/yaconf), 会更合适一些, 新版本的yaconf也支持子目录了，你可以一个项目一个子目录，方便管理，当然性能也更好

     [Reply](https://www.laruence.com/2026/08/20/6420.html?replytocom=560968#respond)
2. ![bolo](https://cravatar.com/avatar/2a9c4f525050372a6fe0b10ce4fe8957?s=48&r=g)

   [bolo](https://github.com/dahaha-365)
   August 20, 2026

   这是每个金丹期phper曾经绞尽脑汁的事（曾经觉得eAccelerator、opcache、memcached、Zend optimizer很神奇，然后是mod\_php、php-fpm、varnish。。。），直到php不再是自己的主力语言😂

   [Reply](https://www.laruence.com/2026/08/20/6420.html?replytocom=560908#respond)

### Leave a Reply [Cancel reply](/2026/08/20/6420.html#respond)

Your email address will not be published. Required fields are marked \*

Comment

Name\*

Email\*

Website

[ ]  Save my name, email, and website in this browser for the next time I comment.

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

# Sidebar

![](/images/logo.jpg)

Laruence

[PHP](http://www.php.net/)开发组核心成员, [Zend](http://www.zend.com/)顾问, PHP7及PHP8 JIT核心作者. Yaf等开源项目作者.

Search

## 开源项目

[Yaf](http://pecl.php.net/package/yaf):  PHP Framework in PHP extension
[Yar](http://pecl.php.net/package/yar):  Light, concurrent RPC framework
[Yac](http://pecl.php.net/yac):  PHP Contents cache
[Yaconf](https://github.com/laruence/yaconf):  PHP Configurations Container
[Taint](http://pecl.php.net/package/taint):  XSS code sniffer
[Lua](http://pecl.php.net/package/lua):  Embedded lua interpreter
[MsgPack](http://pecl.php.net/package/msgpack):  MessagePack in PHP extension
[Couchbase](http://pecl.php.net/package/couchbase):  Libcouchbase wrapper
See also:  [laruence@github](http://github.com/laruence)

## 最新评论

* [laruence](https://www.laruence.com/) on [用Yac给WordPress做缓存：比Memcached快19%](https://www.laruence.com/2026/08/20/6420.html#comment-560968)
* dust on [用Yac给WordPress做缓存：比Memcached快19%](https://www.laruence.com/2026/08/20/6420.html#comment-560943)
* [bolo](https://github.com/dahaha-365) on [用Yac给WordPress做缓存：比Memcached快19%](https://www.laruence.com/2026/08/20/6420.html#comment-56...