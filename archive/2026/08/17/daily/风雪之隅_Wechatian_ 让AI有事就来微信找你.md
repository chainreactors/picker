---
title: Wechatian: 让AI有事就来微信找你
url: https://www.laruence.com/2026/08/17/6297.html
source: 风雪之隅
date: 2026-08-17
fetch_date: 2026-08-18T02:53:09.582217
---

# Wechatian: 让AI有事就来微信找你

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

# Wechatian: 让AI有事就来微信找你

Published on [17 August 2026](https://www.laruence.com/2026/08) by [laruence](https://www.laruence.com/author/laruence)

前几天我介绍了怎么使用 Obsidian 配合 Claudian 和 Claude Code 来搭建个人 AI 助理：[用 Obsidian+Claudian+Ds 搭建个人 AI 助理](https://mp.weixin.qq.com/s/ZVOmJCWixdXH9FrO13nHnw)

相信你用了以后，会不断解锁新的应用场景，也会让 AI 帮你做越来越多的事情，随着我们交给它的工作也越来越繁重，于是我相信你一定会遇到如下类似的问题：

## 魂牵梦萦

Agent 能干的事越来越多，但完成任务的耗时也跟着越来越长——从几分钟，到半小时，到一个多小时。你给它派了个活，它陷入了一个又一个的思考，半天结束不了，于是你决定不等了，去干点其他的事，但是人虽然去干别的了，心却留在那儿：过一会儿忍不住切回去看一眼，再过一会儿又看一眼，走到哪了？报错没有？搞得魂牵梦萦，手头的事也没干踏实。

![2026-08-17_1109_article0.png](/medias/2026/08/2026-08-17_1109_article0.png)

更糟的情况是：你终于走开一阵，回来一看——Agent 在二十分钟前就停下了：它遇到了一个分叉点，提了一个问题，然后一直、一直地等着你回复，白白浪费了几十分钟。

![2026-08-17_1109_article1.png](/medias/2026/08/2026-08-17_1109_article1.png)

于是你想，能不能让他在完成任务，或者需要你的时候，能主动联系到你呢？

## 公众号内容归档

你在微信里看到一篇好文章，想存进自己的知识库。找一圈工具，发现主流做法是把文章转发给某个小程序、某个云端服务，由对方的服务器解析完再吐给你。就类似我上一篇文章介绍的 [WeChat Obsync](https://github.com/less1001/obsync) 插件。

先不说用小程序的方式操作起来会比较麻烦，最重要的还是因为小程序需要依赖一个第三方中转。你可能会担忧，你想收藏的每一条内容，都必须先经过别人的"手"。对方看没看不该看的、存没存、留多久——你没有任何控制力，总觉得会被窥探。

于是你想，能不能有一个不用经过第三方的方式来同步微信内容呢？

## Wechatian

困扰你的，也是困扰我的。我尝试过用 iMessage、邮件，甚至在自己的个人服务器上做过 Push 服务，但都比较麻烦，用起来也不那么自然。毕竟对于我们国人来说，花时间最多的 APP 永远是微信。于是我让 AI 帮我写了一个 Obsidian 插件：Wechatian，让 Agent 永远可以第一时间找到我们。

Wechatian 是一个 [Obsidian](https://community.obsidian.md/plugins/wechatian) 插件，是我受到 CC Connect 启发、让我的 AI 花了 4 个小时做的（不直接用 CC Connect 是因为它过于庞大，也不能接入 Obsidian 生态）。它的主要功能用一句话来总结就是：**把微信变成你的 AI Agent 和你的知识库之间的双向通道**。

* 收：从微信发文字、图片、文章链接，自动落入你的知识库
* 发：AI Agent 想找你时，往一个文件夹里丢个消息，你的微信就响了

### 架构：只有两端，没有中间商

```
微信 <—> 腾讯 ilink AI 网关 <—> Wechatian <—> 你的知识库
```

链路上只有两端：微信官方网关，和你本地的 Obsidian。几个关键设计决策：

**1. 走腾讯 ilink AI 机器人网关**

没有非官方协议 hack，不需要自建中继服务器。插件通过长轮询直接与微信官方网关通信。

**2. 消息内容只存在于你自己的知识库**

收到的文字、图片、文章正文，全部以 markdown 和文件形式写进你的知识库，不经过任何第三方服务。这正是它和"小程序中转"式剪藏工具的本质区别——你的知识库入口，不再经过别人的手。

**3. 发送走文件发件箱**

插件不暴露任何 API。想发微信消息，就往 `<Wechatian>/outbox/` 写一个文件：

* 写一个 `.md`，内容作为文本消息发出
* 丢一张图片、一段视频、一份文档（≤100MB），作为附件发出

插件每 30 秒轮询一次发件箱，取出文件、加密、通过微信送达。

这个设计带来一个额外的好处：**任何会写文件的程序都能发微信**——shell 脚本、Python、任何 AI Agent。不需要 SDK，不需要集成，零接入成本。

**4. Agent 协议自描述**

插件在收件目录自动维护一份 `Agent.md`，写清楚当前的目录结构和收发协议。你不需要教你的 AI 助手任何东西，把这份文件指给它，它自己就学会了怎么给你发微信、怎么读你的回复。

**5. 扫码绑定，只认你自己**

扫码登录后，插件只接受绑定账号发来的消息。即使机器人 ID 泄露，别人也无法往你的 vault 写任何东西。

### 功能清单

**接收侧**

* 长轮询实时收消息，写入每日对话笔记——每天一份 `<日期>.md`，收和发都记在里面，按时间排列，本身就是一份可读的双向对话记录
* 图片、文件、视频、语音自动下载并解密到 `attachments/`
* 消息里的文章链接自动剪藏：正文转 markdown、文内图片全部下载到本地，存成文章笔记，对话笔记里只留标题链接

**发送侧**

* 文本消息、文件、图片、视频、公众号文章
* 每条发送都记录在案，失败可查原因

## 实际用起来是什么样

这几天我自己用得最多的三个场景：

**文章剪藏。**微信里看到好文章，复制链接，直接把链接发给 bot。几秒后就在知识库里多了一份全文 markdown 笔记，配图全部本地化。

**远程指挥 Agent。**出门前告诉 Agent 监听微信消息，于是你人在外面，突然有了新想法，就在微信里给 Bot 发一句"检查一下 yar\_compact，是不是真的需要 detach，完成后微信通知我结果"，家里的 Agent 收到就开始干活。改完的结果再发回微信。微信成了 Agent 的遥控器。

**长任务通知。**Agent 跑一个耗时任务，你要去忙其他事，于是告诉她"如果有问题，或者结束了，微信通知我"。于是她就在结束时往发件箱写一句"构建完成，0 错误"，几秒内你的微信就响了。再也不用守着屏幕，也不会错过它卡在问题里等你回复——卡住了，它会来问你。

![2026-08-17_1109_article2.png](/medias/2026/08/2026-08-17_1109_article2.png)

## 安装和使用

最省事的用法：直接把下面这句话丢给你的 AI 助手，它会替你装好：

```
前往 https://github.com/laruence/wechatian，按其中的说明把 Wechatian 插件安装到我的 Obsidian。
```

它会自己下载插件、放进插件目录、带你走完全程。

如果你想自己手动安装，那么：在 Obsidian 设置 → 第三方插件 → 社区插件市场搜索"wechatian"，点击安装即可。当然也可以自己下载安装，首先在 GitHub 搜索 [Wechatian](https://github.com/laruence/wechatian)：

![2026-08-17_1109_article3.png](/medias/2026/08/2026-08-17_1109_article3.png)

然后：

1. 在 GitHub 的 Wechatian 仓库页面下载最新版 Release，其中包含 `main.js`、`manifest.json`、`styles.css` 三个主要文件
2. 三个文件放进 `<你的 vault>/.obsidian/plugins/wechatian/`
3. Obsidian 设置 → 第三方插件 → 启用 Wechatian
4. 打开 Wechatian 设置页，登录绑定二维码会自动出现，用微信扫码确认。扫完之后，你的微信联系人里面会出现一个"微信 ClawBot"：![2026-08-17_1109_article4.png](/medias/2026/08/2026-08-17_1109_article4.png) 当然，你还可以给它改名、改头像，我就把它改成了 Jarvis 😂
5. **从微信给 bot 发一条任意消息**——网关规定：绑定账号先给 bot 发过消息，才会下发发送凭据，少了这一步 bot 暂时发不出消息

![2026-08-17_1109_article5.png](/medias/2026/08/2026-08-17_1109_article5.png)

可以在 Test Send 测试一下，点击发送，如果你的微信收到了消息，那就是大功告成！

> 进一步，你还可以让你的 AI Agent 去 Wechatian 目录下阅读 Agent.md，之后你就可以跟你的 Agent 说："结束了微信通知我"、"把 xxx 文件发送微信给我"。

几点说明：

* 仅支持桌面端 Obsidian 1.13.0+（长轮询机制，移动端暂不支持）
* 微信的 Bot 不支持像联系人一样随手转发给它，所以文章需要复制链接后发送，图片和文件需要存在本地，或者收藏后走文件发送渠道
* 同一个微信账号同时只建议一台设备在线，多端轮询会争抢消息
* 网关对主动发送有限流。这条通道适合通知和拍板，不适合当聊天软件刷

当然，如果你不是一个 Obsidian+Claudian 的用户，你也可以让你的 Agent 参考 Wechatian，实现一套能在你的 Agent 里运行的"Wechatian"。Enjoy！

GitHub 仓库地址：<https://github.com/laruence/wechatian>

---

Note：本文由 Jarvis（作者的 AI 助理）从公众号「风雪之隅」自动同步至本博客。

[![微信公众号](/medias/2026/08/gzh-icon-180.png)](https://mp.weixin.qq.com/s/t0elE5Ha0Ulbt1vEOXKhOw "微信公众号")阅读公众号原文：[《Wechatian: 让AI有事就来微信找你》](https://mp.weixin.qq.com/s/t0elE5Ha0Ulbt1vEOXKhOw)

### Related Posts

* [Taint支持PHP8啦！](https://www.laruence.com/2026/08/07/6340.html)
* [用DeepSeek V4 Pro改进Yaconf：快是真快，但它把我代码搞丢了](https://www.laruence.com/2026/08/14/6343.html)
* [Wechatian: 让AI有事就来微信找你](https://www.laruence.com/2026/08/17/6297.html)
* [PHP8.0的Named Parameter](https://www.laruence.com/2022/05/10/6192.html)
* [PHP stream未能及时清理现场导致Core的bug](https://www.laruence.com/2010/09/27/1754.html)

Filed in [PHP Extension](https://www.laruence.com/category/phpext "View all posts in PHP Extension"), [PHP8](https://www.laruence.com/category/php8 "View all posts in PHP8"), [PHP应用](https://www.laruence.com/category/php-usage "View all posts in PHP应用"), [随笔](https://www.laruence.com/category/notes "View all posts in 随笔")

* [AI Agent](https://www.laruence.com/tag/ai-agent "View all posts tagged AI Agent")
* [Claude](https://www.laruence.com/tag/claude "View all posts tagged Claude")
* [Obsidian](https://www.laruence.com/tag/obsidian "View all posts tagged Obsidian")
* [公众号，Wechat](https://www.laruence.com/tag/%E5%85%AC%E4%BC%97%E5%8F%B7%EF%BC%8Cwechat "View all posts tagged 公众号，Wechat")

Previous Post
[用DeepSeek V4 Pro改进Yaconf：快是真快，但它把我代码搞丢了](https://www.laruence.com/2026/08/14/6343.html)

No Newer Posts
[Return to Blog](https://www.laruence.com)

## Be First to Comment

### Leave a Reply [Cancel reply](/2026/08/17/6297.html#respond)

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

* [长庚](http://wap.jdzrayynk.com/) on [留言](https://www.laruence.com/guestbook#comment-560600)
* [厚海数据平台](https://hohidata.com) on [留言](https://www.laruence.com/guestbook#comment-560435)
* [厚海数据平台](https://hohidata.com) on [留言](https://www.laruence.com/guestbook#comment-560434)
* [大侠John](https://www.guozhenyi.com) on [留言](https://www.laruence.com/guestbook#comment-512426)
* [海拉拉](https://hirelala.com) on [留言](https://www.laruence.com/guestbook#comment-498347)

## 标签

[Apache](https://www.laruence.com/tag/apa...