---
title: 付费墙的短与长（二）：怎样有效保存已订阅内容
url: https://buaq.net/go-171198.html
source: unSafe.sh - 不安全
date: 2023-07-05
fetch_date: 2025-10-04T11:52:23.615289
---

# 付费墙的短与长（二）：怎样有效保存已订阅内容

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

![](https://8aqnet.cdn.bcebos.com/d49225ca8d033d434c4edaa80757d6c5.jpg)

付费墙的短与长（二）：怎样有效保存已订阅内容

在本系列的上篇中，我们讨论了当今付费墙的主流类型，并介绍了付费墙的常见实现机制。但比起这些理论问题，一般读者更关心的一个实际问题可能是：如何有效地保存已经购买的付费内容？这就是本次要讨论的话题。使用
*2023-7-4 20:44:55
Author: [sspai.com(查看原文)](/jump-171198.htm)
阅读量:17
收藏*

---

在本系列的[上篇](https://sspai.com/prime/story/on-paywalls-01)中，我们讨论了当今付费墙的主流类型，并介绍了付费墙的常见实现机制。但比起这些理论问题，一般读者更关心的一个实际问题可能是：如何有效地保存已经购买的付费内容？这就是本次要讨论的话题。

## 使用稍后读服务：「为何不行」与「如何才行」

对日常用户来说，最常接触到、门槛最低的付费内容保存方法，大概就是使用各类「稍后读」服务了。但正如你可能已经通过实践发现的，稍后读服务并不总能很好应对这种场景。

因此，这里我们要解决的问题就是 (1) 为什么稍后读抓不到付费墙后的文章，以及更重要的，(2) 怎样才能抓到。

让我们先回顾一下稍后读服务保存网页的一般流程（有「一般」就有「特殊」，但别急我们慢慢来）：

1. 你告诉稍后读服务一个要保存内容的网址；
2. 稍后读服务从自己的服务器访问那个网址；
3. 稍后读服务从打开的页面上试图找出文章内容并保存。

很显然，如果你要打开的文章有付费墙，稍后读服务很可能会卡在第 2 步：它的服务器没有你的付费账户登录信息，也就看不到完整的付费内容。

但凡事都有例外。让我们来做一个简单的实验。

在一台有公网 IP（或者设置了内网穿透）的电脑上随便新建一个目录，比如 `test`；然后在里面放一个 `paywall.html` 的网页，内容可以看心情随便打两行：

```
<html>
    <p>Thank you for being our vaulable customer!</p>
    <p>You can check out any time you like, but you can never leave!</p>
</html>
```

（这个语法显然是缺胳膊少腿的，但我们只是为了「在这个舞台上玩」，所以不要在意。）

现在，在 `test` 目录运行：

```
npx http-server --username user --password pass --log-ip
```

（依赖 `npm`；我知道可能有一千种方法来起一个简单的 HTTP 服务器，用这个方法只是因为 `npx` 不用配环境、可以即用即抛，以及 [`http-server`](https://www.npmjs.com/package/http-server) 的默认日志样式比较清楚。）

这样，我们就有了一个位于 `http://{your_ip}:8080/paywall` 的「付费墙」内容，它受到 [HTTP 基本认证](https://en.wikipedia.org/wiki/Basic_access_authentication)的保护，只有输入用户名和密码才能看到「文章」。

![](https://cdn.sspai.com/2023/07/04/a7cc237fd6dc5478702cccbfb0534a76.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

现在，我们尝试在稍后读服务网页版界面中添加并保存这个链接。

![](https://cdn.sspai.com/2023/07/04/65f9c626f2bf25cfdf7d1091dfa7637c.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

可以看到，Instapaper、Matter、Pocket 和 Readwise Reader 这些主流工具都不能抓取到「正文」内容。这是意料之中的，因为它们的服务器无法绕过我们设置的密码。

**现在我们换一种方法。** 删掉刚才保存失败的文章，直接在浏览器里访问这篇「付费文章」，输入用户名 `user` 和密码 `pass` 解锁，然后**用这些稍后读服务各自的浏览器插件来保存。**

![](https://cdn.sspai.com/2023/07/04/1940754aaa8264cd5f7bd229b4852e33.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

可以看到，Instapaper、Readwise Reader 和 Matter 这回都成功保存了密码保护的内容。（从 Pocket 被 Mozilla 收购后[不务正业](https://blog.mozilla.org/futurereleases/2018/01/24/update-on-pocket-and-firefox-integration/)的记录看，它成为唯一的吊车尾也是可以理解的。）

这是怎么做到的？敏锐的读者从 `http-server` 的日志就可以看出端倪：在第二次保存的时候，那些稍后读服务的服务器根本没有向我们的「付费文章」发出请求。

其实，当使用很多稍后读服务的浏览器插件保存网页时，网页内容根本不是它们「抓」下来的，而是我们主动「送」上门的：观察网络活动就会发现，点击 Instapaper、Readwise Reader 和 Matter 的浏览器插件按钮时，都会触发一个指向它们各自 API 端点的 POST 请求，其内容正是加载完成的网页全文 HTML。

![](https://cdn.sspai.com/2023/07/04/0fa7168252ab9acec7d7ef4e7d8dd76c.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2023/07/04/8536e8df63b5c4f30b5b30582fd15553.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

**因此，我们就知道了用稍后读保存付费内容的「正确姿势」：** 只要先用浏览器加载出完整的付费内容，然后使用稍后读服务的插件保存就行了。相反，在链接上点击右键保存，或者在稍后读服务中使用添加链接功能保存，都不能让稍后读服务「看到」完整的网页，也就不能存下完整的付费内容。

在理解原理的基础上，**我们甚至可以利用这个机制，让稍后读不仅能保存下付费内容，而且按照我们想要的格式保存下内容。** 例如：

1. 对于英文付费内容，可以先用「沉浸式翻译」这样的插件将内容页面翻译一遍，然后再使用插件保存，就能存下经过翻译的内容；

![](https://cdn.sspai.com/2023/07/04/1f8399d5133c8fa530e7b636f7d9f265.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

1. 对于稍后读服务不能很好处理的复杂页面，可以先用「检查元素」（DevTools）或者广告拦截器删除页面上的内容无关元素，然后再用插件保存，就能避免这些元素混入存下的版本。

**类似的机制和用法也适用于 iOS。** 你或许没有意识到，当你在 Safari 中使用「分享」菜单连接第三方应用时，它们获得的并不是一个单纯的网址，而是一个称为「Safari 页面」的复合对象，其中包含了 (1) 网址、(2) 网页 HTML 对应的富文本，以及 (3) 从网页中提取的文章（即「阅读器」功能抓取到的结果）；被连接的应用可以按需从中提取。

（你可以通过将页面分享给只有一个「内容项目图」（Content Graph）步骤的快捷指令，很清楚地观察到这一点。）

![](https://cdn.sspai.com/2023/07/04/c8bb82098d2a3b0b48db5b9278a90f28.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)![](https://cdn.sspai.com/2023/07/04/e59fe63be574c8dae683b3996ae02acd.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

包括前面提到的主流稍后读工具在内，很多第三方应用都可以通过读取 Safari 分享页面中的 HTML，获取 Safari 加载完成的网页内容，从而无需再自行抓取、也不受付费墙限制。 **当然，实现这个效果的前提是从已打开的 Safari 页面分享**（也包括从第三方应用中点击链接打开的 Safari View Controller）；长按链接分享、或者用第三方浏览器分享都是不行的。

至于 Android 用户——很遗憾，尽管 Android 在理论上也支持[通过分享菜单传输富文本内容](https://developer.android.com/training/sharing/send?hl=zh-cn)，但据我测试，目前还没有哪个浏览器支持「分享」出当前浏览的页面内容，包括「亲生」的 Chrome。

**最后需要指出，还有很多其他能让稍后读服务保存到付费墙后内容的方式，只是都不具有普适性。**

文章来源: https://sspai.com/prime/story/on-paywalls-02
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)