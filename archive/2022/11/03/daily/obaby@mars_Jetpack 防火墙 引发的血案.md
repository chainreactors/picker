---
title: Jetpack 防火墙 引发的血案
url: http://h4ck.org.cn/2022/11/jetpack-%e9%98%b2%e7%81%ab%e5%a2%99-%e5%bc%95%e5%8f%91%e7%9a%84%e8%a1%80%e6%a1%88/
source: obaby@mars
date: 2022-11-03
fetch_date: 2025-10-03T21:36:44.894358
---

# Jetpack 防火墙 引发的血案

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

# Jetpack 防火墙 引发的血案

2022年11月2日
[14 条评论](https://h4ck.org.cn/2022/11/10651#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/108a170cf25538ea5bd667600043cb50-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/108a170cf25538ea5bd667600043cb50-scaled.jpg)

早上看到有个评论通知，然后打开后台的时候就抑郁了。直接报错了：

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/Jietu20221102-090716.jpg)

点击链接之后并没有什么有用的信息，不过上面的提示信息显示可以通过邮件获取具体的问题。这个貌似还有点用：

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/Jietu20221102-091123.jpg)

比较扯淡的是下面的那个恢复链接点了并没有任何的效果，其实按照邮件内容已经可以看出来是jetpack插件的问题。jetpack插件发的邮件告诉我jetpack有问题，其实现在应该是直接禁用插件就行了。但是，目前进不去后台，于是通过ssh登录服务器之后把插件目录干掉了，进入后台之后重装jetpack，发现依然是挂掉的。不过通过最后的文件路径我已经大概猜到了就是jetpack web应用防火墙导致的问题。但是现在重装之后原来的选项依然是生效的，现在要解决这个问题就只能在数据库里强行删除了。![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/Jietu20221102-091633.jpg)

找到jetpack\_options表，直接清空option\_value保存即可。此时激活插件会要求重新绑定。登录wp账号绑定激活重新进行选项配置就可以了。

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/Jietu20221102-091837.jpg)

嗯，测试版的东西果然不靠谱。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Jetpack 防火墙 引发的血案》](https://h4ck.org.cn/2022/11/10651)
\* 本文链接：<https://h4ck.org.cn/2022/11/10651>
\* 短链接：<https://oba.by/?p=10651>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[jetpack](https://h4ck.org.cn/tags/jetpack)[WordPress](https://h4ck.org.cn/tags/wordpress)

[Previous Post](https://h4ck.org.cn/2022/11/10659)
[Next Post](https://h4ck.org.cn/2022/11/10649)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2010年7月7日

#### [博客莫名其妙夜里会有300M的流量](https://h4ck.org.cn/2010/07/1739)

2014年12月8日

#### [蛋疼的gravatar（感谢GFW）](https://h4ck.org.cn/2014/12/5734)

2013年5月6日

#### [Blog 现已支持Https访问](https://h4ck.org.cn/2013/05/5135)

### 14 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2022年11月2日 09:41](https://h4ck.org.cn/2022/11/10651#comment-88427)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Safari 16](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/safari.png "Safari 16") Safari 16 ![iPhone iOS 16.1](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/device/iphone.png "iPhone iOS 16.1") iPhone iOS 16.1 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   因为你懂技术可以自行解决。完全不会技术的这时候没人帮忙大概就要整站重做了。

   [回复](#comment-88427)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月2日 10:14](https://h4ck.org.cn/2022/11/10651#comment-88429)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      的确，折腾的越多遇到的问题也就越多。并且很多问题都很难定位，无法知道具体是什么东西导致的。等到查ngxinx或者php的错误日志，那就更麻烦了。

      [回复](#comment-88429)
2. ![](https://gg.lang.bi/avatar/19c876303871f0a28cc2c27bcccc5540a43e0dccc8c3901cd1dbbfd3203227b9?s=64&d=identicon&r=r)

   [2022年11月2日 16:33](https://h4ck.org.cn/2022/11/10651#comment-88435)

   ![Level 1](https://badgen.net/badge/亲密度/Level 1/gray?icon=codebeat)

   ![Google Chrome 106](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 106") Google Chrome 106 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   巧了，我今早也在自己的站点遇到了同样的问题！我后来是请公司的运维帮忙才处理好。最后是禁用了这个插件然后进去 WP 后台重装了一下插件，然后就正常了。

   [回复](#comment-88435)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月2日 16:35](https://h4ck.org.cn/2022/11/10651#comment-88436)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 106](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 106") Google Chrome 106 ![Android 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      看来是个通病 解决了就好

      [回复](#comment-88436)
3. ![](https://gg.lang.bi/avatar/ffe079586b4cbcb80e308ac87712f9d5c8d4918b4e6c5f00d68a0be009891cae?s=64&d=identicon&r=r)

   [2022年11月3日 00:06](https://h4ck.org.cn/2022/11/10651#comment-88451)

   ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Opera 90](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/opera-3.png "Opera 90") Opera 90 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   上班的时候都不敢打开你的网站，生怕社死。

   [回复](#comment-88451)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月3日 08:51](https://h4ck.org.cn/2022/11/10651#comment-88469)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      下载的美女们总得发挥最大价值啊~~~另外可以有效提升心里承受能力不是~~

      [回复](#comment-88469)
4. ![](https://gg.lang.bi/avatar/02bd230fd2f5df0296ea43f46487d171e9493b8f638d76d85c396fb932cc6986?s=64&d=identicon&r=r)

   [2022年11月3日 16:05](https://h4ck.org.cn/2022/11/10651#comment-88485)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Microsoft Edge 107](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 107") Microsoft Edge 107 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   你的文章的配图也太火辣了吧，我是冲着图片来的！

   [回复](#com...