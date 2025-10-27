---
title: PHP redis 分布式 可重入 锁 LUA脚本
url: https://buaq.net/go-151274.html
source: unSafe.sh - 不安全
date: 2023-02-28
fetch_date: 2025-10-04T08:13:45.814113
---

# PHP redis 分布式 可重入 锁 LUA脚本

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

PHP redis 分布式 可重入 锁 LUA脚本

<?phpnamespace App\Ok;class Locker{ public static function lock(string $ke
*2023-2-27 22:6:54
Author: [www.yanglong.pro(查看原文)](/jump-151274.htm)
阅读量:15
收藏*

---

```
<?php

namespace App\Ok;

class Locker
{

    public static function lock(string $key, $val, int $ex)
    {
        $val = (string)$val;
        if ($key === '' || $val === '' || $ex <= 0) return false;
        return \Illuminate\Support\Facades\Redis::eval(<<<'LUA'
if redis.call('exists', KEYS[1]) > 0 then
    if redis.call('get', KEYS[1]) == ARGV[1] then
        return redis.call('expire', KEYS[1], ARGV[2])
    else
        return false
    end
else
    return redis.call('set', KEYS[1], ARGV[1], 'NX', 'EX', ARGV[2])
end
LUA, 1, $key, $val, $ex);
    }

    public static function unlock(string $key, $val)
    {
        $val = (string)$val;
        if ($key === '' || $val === '') return false;
        return \Illuminate\Support\Facades\Redis::eval(<<<'LUA'
if redis.call('get', KEYS[1]) == ARGV[1] then
    return redis.call('del', KEYS[1])
else
    return 0
end
LUA, 1, $key, $val);
    }
}
```

文章来源: https://www.yanglong.pro/php-redis-%e5%88%86%e5%b8%83%e5%bc%8f-%e5%8f%af%e9%87%8d%e5%85%a5-%e9%94%81/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)