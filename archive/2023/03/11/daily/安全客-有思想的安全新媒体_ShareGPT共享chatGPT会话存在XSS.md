---
title: ShareGPT共享chatGPT会话存在XSS
url: https://www.anquanke.com/post/id/287249
source: 安全客-有思想的安全新媒体
date: 2023-03-11
fetch_date: 2025-10-04T09:13:11.641685
---

# ShareGPT共享chatGPT会话存在XSS

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# ShareGPT共享chatGPT会话存在XSS

阅读量**321582**

发布时间 : 2023-03-10 14:00:34

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

昨天（3月8号）chatGPT的历史会话保存功能无了(…崩了可能？或者是下线了？)，新的会话都无法保存，历史会话全部丢失

于是乎，为了方便存会话，后来就找到了这个浏览器插件——https://sharegpt.com/

![]()

它可以把chatGPT的会话保存下来，生成一个共享链接，让大家一起浏览你觉得不错的会话，还可以评论什么的，类似这样：

![]()

会话结束后，只需要点share，就可以自动跳转到生成的共享链接了：

![]()

![]()

共享这里有XSS风险，它基本上是把chatGPT的前端页面直接原封不动搬过去了，他人浏览你共享的会话时其实就直接加载了你会话的HTML前端

也就是说，如果你：

![]()

然后：

![]()

就会把整个嵌入的JavaScript载荷携带到生成的共享页面上了：

![]()

随手做了一个简单alert的PoC，共享链接：https://sharegpt.com/c/mHhUjtX

not fun at all…

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**Magpie**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/287249](/post/id/287249)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [xss](/tag/xss)
* [ChatGPT](/tag/ChatGPT)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t0124d09553498407ac.png)Magpie

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014fe713b0dac45b06.png)

[![](https://p4.ssl.qhimg.com/t0124d09553498407ac.png)](/member.html?memberId=136974)

[Magpie](/member.html?memberId=136974)

这个人一点都不懒，但签名还是没有写

* 文章
* **9**

* 粉丝
* **33**

### TA的文章

* ##### [ShareGPT共享chatGPT会话存在XSS](/post/id/287249)

  2023-03-10 14:00:34
* ##### [ARM固件基址定位工具开发](/post/id/198276)

  2020-02-13 16:00:04
* ##### [Top chunk劫持：House of force攻击](/post/id/175630)

  2019-04-01 16:30:20
* ##### [PWN——那些年坑过我们的数据类型](/post/id/173063)

  2019-03-13 16:30:07
* ##### [kernel pwn（0）：入门&ret2usr](/post/id/172216)

  2019-03-07 16:00:51

### 相关文章

* ##### [梨子带你刷burpsuite靶场系列之客户端漏洞篇 - 跨站脚本(XSS)及跨站请求伪造(CSRF)专题更新部分](/post/id/288408)

  2025-03-26 16:05:51
* ##### [【翻译】Zoom 漏洞链：从Cookie XSS到会话接管以及摄像头劫持](/post/id/299543)

  2024-08-28 10:53:50
* ##### [研究人员使用ChatGPT创建多态“黑曼巴”恶意软件](/post/id/287637)

  2023-03-21 10:30:28
* ##### [无密码绕过！黑客利用ChatGPT劫持Facebook账户](/post/id/287377)

  2023-03-14 11:30:29
* ##### [攻击者伪装ChatGPT实施网络钓鱼攻击](/post/id/287258)

  2023-03-09 12:00:45
* ##### [OpenAI推出ChatGPT的API，启动机器人应用程序集成](/post/id/286978)

  2023-03-03 12:00:17
* ##### [ChatGPT在全球范围内出现短暂访问问题](/post/id/286895)

  2023-03-01 14:00:52

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)