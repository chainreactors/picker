---
title: php-fpm开启opcache缓存
url: https://h4ck.org.cn/2023/03/php-fpm%e5%bc%80%e5%90%afopcache%e7%bc%93%e5%ad%98/
source: obaby@mars
date: 2023-03-27
fetch_date: 2025-10-04T10:45:19.821342
---

# php-fpm开启opcache缓存

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# php-fpm开启opcache缓存

2023年3月26日
[7 条评论](https://h4ck.org.cn/2023/03/11620#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/3d10ea323dfb99907f6635a71da14fbd.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/3d10ea323dfb99907f6635a71da14fbd.jpg)

使用家里的工控机提供服务之后，系统的资源占用率一直居高不下。内存占用率基本在80%以上，cpu占用率也一般在30-40左右。并且还经常会出现cpu跑慢的情况，通过慢查询日志也难以找到问题关键，调用堆栈基本从index.php就开始了，难以定位是哪个插件哪个函数导致的，导致查询效率低下的函数每次都不一样。所以也没办法通过修改代码或者插件的方式来解决这个问题。

不过整体来说比阿里云的服务器已经稳定了很多，至少无法访问的情况大大减少了。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/搜狗截图20230310224603.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230310224603.jpg)

以上为优化之前资源占用情况。

比较奇怪的是今天的访问量到了500以下，想测试下是哪个地区无法访问，结果打开测速网站，网站直接挂了，所有地区全红，cpu内存跑满。于是想着优化下php的执行，开启代码缓存：

修改配置文件：

```
[opcache]
; 开关打开
opcache.enable=1
; 设置共享内存大小, 单位为：Mb
opcache.memory_consumption=128
；如果启用，那么 OPcache 会每隔 opcache.revalidate_freq 设定的秒数 检查脚本是否更新。 如果禁用此选项，你必须使用 opcache_reset() 或者 opcache_invalidate() 函数来手动重置 OPcache，也可以 通过重启 Web 服务器来使文件系统更改生效。
opcache.validate_timestamps=60
```

去掉下面一行的注释，如果没有就添加：

```
zend_extension="opcache.so"
```

重启php-fpm。

使用 `php -m` 查看 Opcache 是否生效。

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/搜狗截图20230326161632.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230326161632.png)

现在资源占用率cpu和内存确实降低了不少：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/搜狗截图20230326161302.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230326161302.png)

网站测速，最起码已经不是全红了：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/03/搜狗截图20230326161400.png)](https://image.h4ck.org.cn/wp-content/uploads/2023/03/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20230326161400.png)

参考链接：https://learnku.com/articles/49492

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《php-fpm开启opcache缓存》](https://h4ck.org.cn/2023/03/11620)
\* 本文链接：<https://h4ck.org.cn/2023/03/11620>
\* 短链接：<https://oba.by/?p=11620>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[php](https://h4ck.org.cn/tags/php)[php-fpm](https://h4ck.org.cn/tags/php-fpm)[WordPress](https://h4ck.org.cn/tags/wordpress)

[Previous Post](https://h4ck.org.cn/2023/03/11639)
[Next Post](https://h4ck.org.cn/2023/03/11613)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2022年11月2日

#### [Jetpack 防火墙 引发的血案](https://h4ck.org.cn/2022/11/10651)

2023年5月25日

#### [关于WP固定链接](https://h4ck.org.cn/2023/05/12209)

2023年12月24日

#### [抄作业续章](https://h4ck.org.cn/2023/12/14859)

### 7 comments

1. ![](https://gg.lang.bi/avatar/898a5dc2af6086170c841c729a84c959c7fdc38a0c090e2edc7ebafd0c0ef9c4?s=64&d=identicon&r=r) **[小熊](https://www.saphead.cn)**说道：

   [2023年3月26日 22:28](https://h4ck.org.cn/2023/03/11620#comment-93804)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Microsoft Edge 110](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 110") Microsoft Edge 110 ![iPhone iOS 16.3](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 16.3") iPhone iOS 16.3 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   php8还有jit，哈哈哈哈，好像是说可以更快，但是我没咋感受到

   [回复](#comment-93804)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2023年3月26日 22:31](https://h4ck.org.cn/2023/03/11620#comment-93805)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 110](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 110") Google Chrome 110 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      默认开启的吗？还是需要插件？

      [回复](#comment-93805)

      1. ![](https://gg.lang.bi/avatar/898a5dc2af6086170c841c729a84c959c7fdc38a0c090e2edc7ebafd0c0ef9c4?s=64&d=identicon&r=r)

         [2023年3月26日 22:33](https://h4ck.org.cn/2023/03/11620#comment-93806)

         ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

         ![Microsoft Edge 110](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 110") Microsoft Edge 110 ![iPhone iOS 16.3](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 16.3") iPhone iOS 16.3 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         这个问题就得大佬自己瞧一瞧了，我实在是太菜了，我只知道php8的opcache加入了jit，好像能更快，哈哈哈。不好意思大佬

         [回复](#comment-93806)

         1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

            [2023年3月26日 22:41](https://h4ck.org.cn/2023/03/11620#comment-93811)

            ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

            ![Google Chrome 110](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 110") Google Chrome 110 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

            嗯嗯，刚大概了解了一下。也是得先开启opcache，不过优化的更彻底了。

            [回复](#comment-93811)
2. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

   [2023年3月27日 13:57](https://h4ck.org.cn/2023/03/11620#comment-93829)

   ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

   ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   @obaby 测试

   [回复](#comment-93829)
3. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

   [2023年3月29日 16:34](https://h4ck.org.cn/2023/03/11620#comment-93926)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 111](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 111") Microsoft Edge 111 ![Windows 1...