---
title: Yac 2.4.0发布 - 小值读取性能提升64%
url: https://www.laruence.com/2026/08/26/6566.html
source: 风雪之隅
date: 2026-08-26
fetch_date: 2026-08-27T12:13:16.478067
---

# Yac 2.4.0发布 - 小值读取性能提升64%

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

# Yac 2.4.0发布 - 小值读取性能提升64%

Published on [26 August 2026](https://www.laruence.com/2026/08) by [laruence](https://www.laruence.com/author/laruence)

## 起因

前几天我把博客的对象缓存切到了我新写的 WordPress 插件 [wordpress-yac-cache](https://www.laruence.com/2026/08/20/6420.html)，替掉了用了十几年的 Memcached。压测结论：同样条件下吞吐提升 ~19%。

切完跑了几天，发现 **keys 内存涨得特别快**。翻了翻里面装的都是什么，发现了几个坑：

* 大头是两类**空数组**：一类是 WordPress search 的负缓存——搜一个没有结果的关键字，WP 也会把空结果缓存下来，免得下次再查库。
* 搜索那类空缓存里，还混着一批特殊访客：search poisoning 的 bot 天天拿各种垃圾敏感词来查你的站内搜索，就为了骗搜索引擎收录结果页——每查一个词，你的缓存里就多一条没人读的负缓存。
* 我用了一个反垃圾评论的插件 Akismet，它有个叫 `akismet_schedule_cron_recheck` 的 cron：API 判定暂时拿不准（或出错）的评论会进“待重查”队列，cron 每次跑起来取最多 100 条，逐条重新提交给 Akismet 复核。复核过程中它要给每条评论反复增删一批 comment meta——`akismet_rechecking`（重查标记）、`akismet_error`、追加式的 `akismet_history` 等等。这些全按“评论 × meta key”进对象缓存，而待重查队列里躺的十有八九是垃圾评论——查完之后大多没什么值得留下的，落到缓存里的就是一个又一个空数组。

Yac 的 keys 区是定长的，真要满了倒也没关系——探测几次没空位就按 LRU 踢一条旧的，新的住进来。但是 values 的内存区会受到一些影响：这些空数组虽然没人读，可每次 `set` 还是老老实实去 values 区分配一块、写进去。就这么持续地写，values 段迟早转完一圈开始 recycle，把你**真正在用**的数据覆盖掉——然后就是 miss。

缓存里一堆没人读的数据，把内存占满、把有人读的数据挤走，这感觉不太好。

## 灵感

于是，前天开车的时候突然想到：这些小东西——空数组、`false`、`null`、小整数——为什么非要写进 values 区？slot 里本来就有一个字段是指向 value 的指针，指针是 8 字节对齐的，**低 3 位永远是 0，天然闲置**。把值直接编码进这个指针字里，不就行了？它们再也不会持续地写 values 的内存，了不起就是 kicks 多一些，并不会影响持续有人读的数据。

于是有了 2.4.0 最大的改动：**Embedded values（标量内嵌）**。

## Embedded：小值不写 values 区

满足以下任一条件的值，不再去 values 区分配，直接编码进 slot 的 `val` 字段：

* `NULL` / `true` / `false`
* 小整数
* 不超过 7 字节的字符串（64 位平台）
* 空数组

实现上就是用指针字的低 3 位做类型 tag，高位放 payload。读的时候看一眼 slot 就拿到值——不解引用、不进 values 区、没有拷贝。它也不占 values 内存，**自然永远不会被 recycle 挤掉**。

省一次分配、省一次拷贝、少一类 miss，一举多得。

对 WordPress 来说这个改动是量身定做的：上面说的那堆空数组（搜索负缓存、空评论列表）全部走 embedded，values 区零开销。之前插件里我还专门做了个 `WP_YAC_SKIP_EMPTY` 开关，把空值负缓存拦在共享内存外面——2.4.0 之后这个过滤其实可以不要了，随便进，不再是负担。

## LZ4 替换 FastLZ

Yac 的压缩一直用 FastLZ。这个库太老了，基本处于无人维护的状态。2.4.0 换成了 [LZ4](https://github.com/lz4/lz4)：解压快得多、压缩率更好、维护活跃。

默认直接内置 LZ4 源码编译（就一个 .c 文件，零依赖）；想用系统库的话，`configure --with-system-lz4`。

对超过压缩阈值的大值（比如 `alloptions` 这种几十 KB 的），命中后的解压速度直接决定读取延迟，这个替换在基准里体现得非常明显——后面性能一节有数字。

## get() 支持 $default 了

憋了很多年的两个问题：

* `get()` miss 的时候返回 `false`——那如果我缓存的值本身就是 `false` 呢？分不清。于是大家干脆不缓存 `false`。
* `get()` 的签名里其实一直留着第二个参数的位置，当年是给 CAS（compare-and-swap）准备的，但 Yac 始终没实现，就这么空挂着。

2.4.0 把这个位置废物利用，改成了 `$default`：

```

$yac->get("missing");          // NULL（不传行为不变）
$yac->get("missing", []);      // []
$yac->get("missing", false);   // false —— 但语义明确是"没命中，给你默认值"
```

多 key 的 `get()` 行为也顺带改了：以前缺的 key 会填个 `false` 占位，现在直接不返回缺失的 key（传了 `$default` 就用它填充）。不用再去猜返回的 `false` 到底是“没这条”还是“这条就是 `false`”。

以后你要区分“没命中”和“值就是 `false`”，你就可以简单地写：

```

if (($v = $yac->get("maybe_false", "__NONE_EXISTS")) === "__NONE_EXISTS") {
    // 没命中
} else {
    // 命中，$v 就是缓存的值
}
```

没命中时哨兵原样返回，`===` 严格一比即可。

## dump() 加了 $offset

`dump()` 是我自己调试、分析缓存内容用的——把共享内存里所有条目倒出来看。但如果你内存给得大、条目上十万，一次 `dump(-1)` 全倒出来，返回的数组本身就能把单个 PHP 进程的内存撑爆。

所以 2.4.0 加了 `$offset`，支持分页：

```

$entries = $yac->dump(100, 500);   // 从第 500 条开始，取 100 条
```

## 每条数据都有账可查：hits / atime / c\_len

这次还给每个条目加了元信息，`dump()` 里都能看到：

* **hits** —— 这条数据被命中过多少次
* **atime** —— 最近一次访问时间
* **c\_len** —— 存储时的压缩后长度（压缩过的条目）
* **embedded** —— 是不是上面说的内嵌形态

这些能干嘛？**分析你的缓存到底在干嘛**。比如 `alloptions` 是最大的条目，但 hits 也是最高的，值；反过来，某条数据写入后 hits 一直是 0、atime 停在写入时刻，那就是只写不读的垃圾，可以考虑别缓存它。我插件后台面板里的内容分布和 Largest entries 排行，靠的就是这些字段。

比如点进面板里某一条，就能看到它的全部账目——这是博客上的一条真实缓存：

![is_blog_installed 条目详情](https://www.laruence.com/medias/2026/08/wp-yac-entry-detail.jpg)

图2：`is_blog_installed` 的条目详情——被读了 2 万多次、1 秒前刚访问过、embedded 在槽位里

hits 2 万多次、last access 就在 1 秒前、embedded 在槽位里——一条典型的高热数据，缓存它完全值得。你也能用同样的眼光去翻翻自己的缓存，看看谁在干活、谁在吃白饭。

一个细节：`hits` 在覆盖写时清零，不继承旧值的热度。我本来想继承，但无锁设计下新写入时去旧块读计数存在一个极窄的撕裂窗口——权衡之后放弃了，首先 hits、atime 这些值只供参考，就算写错了影响也不大。保持新值新热度的语义简单，实现也干净。

## 性能

16 worker 共享内存基准（3 次平均），对比 2.3.1：

| 场景 | 指标 | 2.3.1 | 2.4.0 | 提升 |
| --- | --- | --- | --- | --- |
| 小值（内嵌） | get | 3.9M ops/s | 6.3M ops/s | **+64%** |
| 小值（内嵌） | set | 6.4M ops/s | 7.2M ops/s | +12% |
| 混合（60% 内嵌 / 40% 序列化） | get | 2.3M ops/s | 4.0M ops/s | **+70%** |
| 混合 | set | 4.2M ops/s | 5.8M ops/s | +39% |
| 压缩值（LZ4 vs FastLZ） | get | 1.0M ops/s | 3.6M ops/s | **~3.5x** |

最大赢家就是 embedded：之前每次 `get` 都要按指针解引用进 values 区再拷贝一次，现在整个读取都发生在 slot 里。压缩值那行则是 LZ4 的功劳。

再给一个端到端的参照（16 workers，100:1 读写比，混合值大小）：

| 后端 | ops/s |
| --- | --- |
| **Yac** | **~27M** |
| APCu | 1.2M |
| Memcached | 98K |

当然，这是极限吞吐，不是承诺——你的机器、你的负载形状会给出你的数字。

## 实际性能表现

升级之后先说实话：**页面速度上，我看不出明显变化。**这并不意外：Embedded 省下的那次解引用和拷贝是微秒级的优化，放进一个 140ms 左右的页面里，低于噪声。基准表里 +64%、+70% 那些数字，衡量的是“直接锤缓存”时的差距。

**真正看得见的收益是内存。**我自己的博客跑了一天下来，Yac 的内存占用从原来的 23.5M 降到了 12.4M——几乎全是 embedded 的功劳。空数组不再每个占一块内存，面板上的 Recycles 也回到了 0：values 再也没转完过一圈。

![升级 2.4.0 后的面板：values 12.4M](https://www.laruence.com/medias/2026/08/wp-yac-dashboard-2.4.0.jpg)

图1：升级 2.4.0 跑一天后的面板——values 12.4M，命中率 93.7%，Recycles 0

## 升级

```

pecl upgrade yac

# 或者
pie install laruence/yac

# 或者源码
git clone https://github.com/laruence/yac.git && cd yac
phpize && ./configure && make && sudo make install
```

Windows 的 DLL 都在 release 页面：<https://github.com/laruence/yac/releases>。

## 最后

如果你要拿它给 WordPress 当对象缓存，内存怎么设？对于我的站点来说，300 篇文章，8M keys + 32M values 就够了：

```

yac.keys_memory_size = 8M     ; 约 6.5 万个槽位
yac.values_memory_size = 32M
```

这两个数是怎么算出来的？

**keys**：每个槽位结构体 88 字节，但槽位数会因哈希掩码向下取整到 2 的幂，折算下来**每个槽位约 128 字节**——4M ≈ 3.2 万个槽位，8M ≈ 6.5 万，16M ≈ 13 万，32M ≈ 26 万。看你应用每天在用的不同 key 有多少个就行（面板的 Total entries，或 `dump()` 数一数）：普通博客几千个，8M 绰绰有余；要是做 session、按用户维度的缓存，不同 key 几十万上百万，就往 32M、64M 加。

**values**：看你的“活内容”要占多少——一条值的实际占用 ≈ 内容大小 × 1.25（存储缓冲系数）+ 24 字节头。WordPress 站最大的条目通常是 `alloptions`（几十 KB），其余是 post meta、评论列表，中小站点全部加起来也就几 MB；2.4.0 之后空值不再进 values，更宽裕。注意 values 的最小单位是 4M（一个 segment），设小了会退化成单 segment。32M 装博客文章这类真实内容绰绰有余；你要是缓存大段 HTML、整表序列化对象，按自己的内容规模乘一乘。

给个安全边际：**keys 按不同 key 数的 2 倍估，values 按热数据装满一轮再留 50% 余量**。略小了也没关系——keys 满了踢旧的，values 满了绕圈，都不会崩，只是 miss 多些。

总结来说，对于 WordPress，可以简单粗暴地按 values 的内存 = 4 倍的 keys 内存来设置。

如果你的博客还在 WordPress 上，也可以考虑把对象缓存换成 Yac——一个扩展 + [一个插件](https://github.com/laruence/wordpress-yac-cache)的事，性能提升立等可取，并且不用再维护一个 Memcached 服务，内存占用也能降下来。我自己的博客已经跑了一个多星期了，暂时没发现问题，哈哈哈。😄

### Related Posts

* [Yac 2.1 升级说明](https://www.laruence.com/2020/03/25/5657.html)
* [用Yac给WordPress做缓存：比Memcached快19%](https://www.laruence.com/2026/08/20/6420.html)
* [Yac (Yet Another Cache) - 无锁共享内存Cache](https://www.laruence.com/2013/03/18/2846.html)
* [Taint支持PHP8啦！](https://www.laruence.com/2026/08/07/6340.html)
* [一些PHP Coding Tips[2011/04/02最后更新]](https://www.laruence.com/2011/03/24/858.html)

Filed in [AI Coding](https://www.laruence.com/category/ai-coding "View all posts in AI Coding"), [PHP7](https://www.laruence.com/category/php7 "View all posts in PHP7"), [PHP8](https://www.laruence.com/category/php8 "View all posts in PHP8"), [PHP应用](https://www.laruence.com/category/php-usage "View all posts in PHP应用")

* [Apcu](https://www.laruence.com/tag/apcu "View all posts tagged Apcu")
* [cache](https://www.laruence.com/tag/cache "View all posts tagged cache")
* [memcache](https://www.laruence.com/tag/memcache "View all posts tagged memcache")
* [wordpress](https://www.laruence.com/tag/wordpress "View all posts tagged wordpress")
* [yac](https://www.laruence.com/tag/yac "View all posts tagged yac")

Previous Post
[用Yac给WordPress做缓存：比Memcached快19%](https://www.laruence.com/2026/08/20/6420.html)

No Newer Posts
[Return to Blog](https://www.laruence.com)

## Be First to Comment

### Leave a Reply [Cancel reply](/2026/08/26/6566.html#respond)

Your email address will not be published. Required fields are marked \*

Comment

Name\*

Email\*

Website

[ ]  Save my name, email, and website in this browser for ...