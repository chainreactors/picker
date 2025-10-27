---
title: PHP<=7.4.21 Development Server源码泄露漏洞
url: https://buaq.net/go-147962.html
source: unSafe.sh - 不安全
date: 2023-02-05
fetch_date: 2025-10-04T05:44:55.035234
---

# PHP<=7.4.21 Development Server源码泄露漏洞

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

![](https://8aqnet.cdn.bcebos.com/44f5e6a474d75de69779cb8e1f0cb02f.jpg)

PHP<=7.4.21 Development Server源码泄露漏洞

最近刷推特看到了一个洞，PHP<=7.4.21时通过php -S开起的WEB服务器存在源码泄露漏洞，可以将PHP文件作为静态文件直接输出源码，还蛮有意思的，这里大胆预测一波，最近在CTF里肯定会有人出
*2023-2-4 23:28:37
Author: [www.gem-love.com(查看原文)](/jump-147962.htm)
阅读量:2450
收藏*

---

最近刷推特看到了一个洞，PHP<=7.4.21时通过`php -S`开起的WEB服务器存在源码泄露漏洞，可以将PHP文件作为静态文件直接输出源码，还蛮有意思的，这里大胆预测一波，最近在CTF里肯定会有人出这个点

![](http://cdn2.pic.y1ng.vip/uPic/2023/02/04/232920_y5Mq0q.png)

查看原文详细分析：[PHP Development Server <= 7.4.21 - Remote Source Disclosure](https://blog.projectdiscovery.io/php-http-server-source-disclosure/)

我不分析了，因为是PHP的C源码，我C语言PTSD

直接拉docker就完事了：

```
docker pull php:7.4.21
```

进入容器内shell之后

```
echo "<?php phpinfo();?>" > phpinfo.php
php -S 0.0.0.0:80
```

复现方法如下，记得要关掉Burp自动修改Content-Length的功能
![](http://cdn2.pic.y1ng.vip/uPic/2023/02/04/233433_oerQNn.png)

在原文中还提出了一个历史漏洞：在解析HTTP请求的过程中，当某些回调被多次调用时，`$_SERVER['REQUEST_URI']`变量会被自身的一个子串覆盖。

> 参考：<https://bugs.php.net/bug.php?id=73630>

这个漏洞没什么太大危害，但有时候可能导致XSS，这里我们来看作者给的一个例子

首先写入如下1.php

```
<a href="<?php echo htmlentities($_SERVER['REQUEST_URI']) ?>">Unexpected url</a>
```

因为文件是在`/1.php`，所以最后输出的HTML一定是这样格式：

```
<a href="/1.php[...后续的参数...]">Unexpected url</a>
```

如果说能构造成`<a href="javascript:alert(1)">Unexpected url</a>` 用户一点击就能触发XSS了，问题的关键点就是在于怎么去除最前面的`/1.php?`脏数据

接下来复现漏洞，因为只是说需要准备一个很长的字符串，也没说具体多长，复现起来就比较困难，这里主要分享一下我复现的方法(没有什么代码依据，就是自己瞎蒙出来的)。

首先随便准备一串字符串，内容无所谓，比如我准备的是

```
jBSZoRHIsU2chNGIzlGa0BibJBiLkVWby9mZsFWbgMXagQ3clVXclJHIlhGdgQXYoRHIz5WYl1GI0lGIsQWYlJHIzVGd5JGIm9GIyVmYtVnbgwWY09GdgUGa0Byb0BCbhVXclBCdv5GIzlGIyV2cyFGcgUGa0BSeiBCZl1Wdz52bjByclRXeiBiZvBiclJWb15GIlhGdgYWS4ycuJXd0VmcgQmbhBSnAKOdzVWdxVmcgAFVUhEIkV
```

之后就一遍一遍往上复制，正常情况下输出的`$_SERVER['REQUEST_URI']`应该都是`/1.php?`开头
![](http://cdn2.pic.y1ng.vip/uPic/2023/02/04/234443_Lc9iCV.png)

同时记得保持URL的最后是`javascript:alert(1)`这个XSSpayload
![](http://cdn2.pic.y1ng.vip/uPic/2023/02/04/235329_EPrMyY.png)

然后继续复制，发送请求，复制多了你就会发现`a href`不再以`/1.php?`开头了
![](http://cdn2.pic.y1ng.vip/uPic/2023/02/04/235428_myrsbA.png)

此时的输出：

```
<a href="YtVnbgwWY09GdgUGa0Byb0BCbhVXclBCdv5GIzlGIyV2cyFGcgUGa0BSeiBCZl1Wdz52bjByclRXeiBiZvBiclJWb15GIlhGdgYWS4ycuJXd0VmcgQmbhBSnAKOdzVWdxVmcgAFVUhEIkVjBSZoRHIsU2chNGIzlGa0BibJBiLkVWby9mZsFWbgMXagQ3clVXclJHIlhGdgQXYoRHIz5WYl1GI0lGIsQWYlJHIzVGd5JGIm9GIyVmYtVnbgwWY09GdgUGa0Byb0BCbhVXclBCdv5GIzlGIyV2cyFGcgUGa0BSeiBCZl1Wdz52bjByclRXeiBiZvBiclJWb15GIlhGdgYWS4ycuJXd0VmcgQmbhBSnAKOdzVWdxVmcgAFVUhEIkVjBSZoRHIsU2chNGIzlGa0BibJBiLkVWby9mZsFWbgMXagQ3clVXclJHIlhGdgQXYoRHIz5WYl1GI0lGIsQWYlJHIzVGd5JGIm9GIyVmYtVnbgwWY09GdgUGa0Byb0BCbhVXclBCdv5GIzlGIyV2cyFGcgUGa0BSeiBCZl1Wdz52bjByclRXeiBiZvBiclJWb15GIlhGdgYWS4ycuJXd0VmcgQmbhBSnAKOdzVWdxVmcgAFVUhEIkVjavascript:alert(1)">Unexpected url</a>
```

记录下`<a href="`和`javascript:alert(1)">Unexpected url</a>`之间的部分，拿到Burp的请求包中搜索
![](http://cdn2.pic.y1ng.vip/uPic/2023/02/05/000459_Ci8TOV.png)

删除搜索到的最后一块结果，多次重放（可能要发包七八次才成功一次），就可以了
![](http://cdn2.pic.y1ng.vip/uPic/2023/02/05/000544_sSbtd2.png)

没看懂没关系，这里我用Python生成的长度为500的随机字符串来演示一下

```
import random
import string

def get_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
```

![001440_iShot_2023-02-05_00.12.51](http://cdn2.pic.y1ng.vip/uPic/2023/02/05/001440_iShot_2023-02-05_00.12.51.gif)

Copyright Notice: All articles in this blog are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) unless stating additionally.

文章来源: https://www.gem-love.com/2023/02/04/PHP-7-4-21-Development-Server%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)