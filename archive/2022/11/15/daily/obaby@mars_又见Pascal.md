---
title: 又见Pascal
url: https://h4ck.org.cn/2022/11/%e5%8f%88%e8%a7%81pascal/
source: obaby@mars
date: 2022-11-15
fetch_date: 2025-10-03T22:44:41.746465
---

# 又见Pascal

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

[程序设计『Programing』](https://h4ck.org.cn/cats/cxsj)

# 又见Pascal

2022年11月14日
[20 条评论](https://h4ck.org.cn/2022/11/10714#comments)

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/57cd115d11c68.jpg)

今天在逛一个[上古论坛](http://www.2ccc.com)（[Delphi盒子](http://www.2ccc.com)）的时候看了下下面的友链，发现一个[星五博客](http://www.offeu.com/) ，点进去看了一下，第一篇文章是基于[pascal的网站开发](https://www.webpascal.com/#download)。点击去溜达了一圈发现是一个国内的公司做的。

上次用Pascal语言开发，还是在刚买车的时候为了折腾导航。14年左右，那时候的导航还多是win ce的系统，为了搞一机多图。逛各种论坛，下载各种程序，但是效果并不好。可以说是非常的烂，于是就想着自己做一个。只是在14年要开发win ce的程序确实有点麻烦，不过好在我pascal大法无所不能。找到了[Lazarus](https://www.lazarus-ide.org) ，跨平台开发工具，能在windows x86架构下编译arm架构的可执行文件，这个就非常的棒。

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/Lazarus_1.6_on_macOS_Sierra.png)

文章地址：<https://h4ck.org.cn/2014/05/%E5%9F%BA%E4%BA%8Elazarus-%E7%9A%84win-ce%E5%BC%80%E5%8F%91/> 当然最终效果还是不错的。

![](https://image.h4ck.org.cn/wp-content/uploads/2014/05/wince1.png)

而之所以要装那么多的导航软件，最根本的原因在于，车载导航实在是不大好用。为了满足各种情况就把常用的导航都装了进去，这也是为什么需要一个导航启动器。现在各种车机基本都是基于安卓系统的的，导航也比之前的好用多了，当然能联网那就更好了。

至于为什么用pascal，那是因为上大学的时候就对pascal一见钟情，当其他语言的入门教程都是在编写命令行工具的时候，那时候delphi 7的hello world竟然是带gui界面的，于是瞬间就被征服了（当然那时候还有vb也是非常方便的）。在加上各种控件，易用性简直不要太好。

在后来delphi xe之后开始支持跨平台编译，支持ios 安卓，也用monkey application框架写过几个小工具，不过整体的体验一般。后来做安卓和ios的定位应用 findu，最开始并不会做案桌上的开发，于是买了basic4app的授权，支持使用basic开发安卓应用，但是由于要对接各种高德的原生库，最终没能用b4a进行开发，而是花了一个多月看了下安卓app开发，基于java做的安卓版app。同样ios版本也没有使用delphi xe，看了一个月ios开发做的苹果版本。至于后台服务，我并不熟悉java 或者.net的服务开发，于是花了一个月学习了python下的django框架。整个服务加应用开发的时间差不多用了三个月时间，后来也更新了数个版本，修复了很多问题。而现在服务停了是因为阿里的im服务框架给停了，这tm就很坑爹。

如果说在多年前看到这个pascal的web开发框架，或许后台我就会用pascal来写了。现在的delphi xe也支持web开发，功能还是很强大的：

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221114215141.jpg)

而[WebPascal](https://www.webpascal.com/#download)的出现，引用作者的话，也是不想再学习一门语言：

> 为什么要制作这么一个脚本模型呢？起因是这样的，做为一个Delphi开发人员，web开发总是我的弱项，而花费巨大
>
> 的精力去重新学习其它语言，成本相对较高，也没法及时的解决手头上的项目，当然，学还是要学的，但一下子把
>
> web前端和web后端开发在短时间内学会，这也是不现实的。因为本人有一点前端html和css基础，后端asp基础，在
>
> 参考php以后，想到一个解决方案，那就是找一个pascal语法的脚本引擎来实现php那样的功能，然后先把web前端开
>
> 发先学会，以后有时间了再去学web后端开发，比如系统的学习一下php的开发。

![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221114220015.jpg)

不过有的时候会发现，学一门新的语言也没那么复杂。**想当初都搞汇编开发，还怕各种语言学习吗？**

当然，内心里还是希望pascal/delphi 能继续发扬光大，只是现在这两门语言都快进了编程语言排行榜的其他了。

相关资源：

delphi盒子：<http://www.2ccc.com>

Web pascal：<https://www.webpascal.com/>

Lazarus：<https://www.lazarus-ide.org>

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《又见Pascal》](https://h4ck.org.cn/2022/11/10714)
\* 本文链接：<https://h4ck.org.cn/2022/11/10714>
\* 短链接：<https://oba.by/?p=10714>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Delphi](https://h4ck.org.cn/tags/delphi)[delphi盒子](https://h4ck.org.cn/tags/delphi%E7%9B%92%E5%AD%90)[Lazarus](https://h4ck.org.cn/tags/lazarus)[Pascal](https://h4ck.org.cn/tags/pascal)[Web pascal](https://h4ck.org.cn/tags/web-pascal)

[Previous Post](https://h4ck.org.cn/2022/11/10723)
[Next Post](https://h4ck.org.cn/2022/11/10708)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2021年9月23日

#### [Android Skip Ads Android Project【截屏部分】](https://h4ck.org.cn/2021/09/9042)

2023年10月27日

#### [闺蜜圈 H5 在线体验版](https://h4ck.org.cn/2023/10/13939)

2025年8月9日

#### [偶然？还是必然？ — 谁是罪魁祸首](https://h4ck.org.cn/2025/08/21237)

### 20 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io)**说道：

   [2022年11月14日 23:52](https://h4ck.org.cn/2022/11/10714#comment-88950)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 106](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 106") Google Chrome 106 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   看到 PASCAL 确实是上古了。我最早是初中接触了 BASIC，功能太简单了；后来知道了 PASCAL，比 BASIC 强大一点，但也不知道能干嘛；后来又知道了 DELPHI，觉得更新奇，可以理解为 PASCAL GUI 版，IDE 强大多了。

   不过参加第一份工作是 web 开发，语言是 PHP，类似 DELPHI 的桌面端语言也没机会用到了。

   文中提到的大佬，因为钟情一门语言，不想学其他语言，我很能理解。就像我看待 PHP 一样。现在市场上 PHP 式微了，在公司也主要 JAVA 为主了。但是在我个人项目里，PHP 还是第一选择的后端语言。

   当然我也有一种希望 PHP 继续伟大的愿望，所以我积极在用新版本，接受新的语法。比如我甚至习惯用强类型模式写 PHP 了。

   [回复](#comment-88950)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月15日 08:52](https://h4ck.org.cn/2022/11/10714#comment-88968)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      也可以理解为一种情节吧，喜欢的东西就不希望看到他没落。还是要积极的拥抱变化，毕竟这些语言也在不断的更新。到了具体的项目上还是选择效率最高的，我不会php，所以后端基本都是基于django框架实现的。实用主义+拿来主义 ![laugh](https://h4ck.org.cn/wp-content/plugins/kama-wp-smile/packs/qip/laugh.gif)

      [回复](#comment-88968)
2. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

   [2022年11月15日 01:12](https://h4ck.org.cn/2022/11/10714#comment-88954)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

   ![Microsoft Edge 107](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 107") Microsoft Edge 107 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   还真是个上古网站！

   [回复](#comment-88954)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2022年11月15日 08:49](https://h4ck.org.cn/2022/11/10714#comment-88966)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 102](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 102") Google Chrome 102 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      零几年的网站到现在还存活的的确已经不多了。收藏夹里的链接现在能正常访问的可能不到一半。

      [回复](#comment-88966)

      1. ![](https://gg.lang.bi/avatar/1c03767b0691f80231895255661bcf42eceab95dc8b493ee80c835b07f577f49?s=64&d=identicon&r=r)

         [2022年11月15日 10:28](https://h4ck....