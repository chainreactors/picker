---
title: 【安全圈】安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652024283&idx=3&sn=0287cacf0c5da8dc0647bca5d9c9ce26&chksm=f36f819bc418088d8446861f026cb11292c645b2ff00b994336fc24151549888846eadf65213&scene=58&subscene=0#rd
source: 安全圈
date: 2022-11-14
fetch_date: 2025-10-03T22:41:18.774237
---

# 【安全圈】安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTuH1VZOIusb6Jk6765TialJHN5cfibjNIh7AiaIPHdS67H4tXhMB9b6D2SQ/0?wx_fmt=jpeg)

# 【安全圈】安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡

安全圈

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylgSxa9I02IBd3bgLEhwfJCeRibw3LEjMujeAhD2CvyiaVCZJVHGHODbkPx3pViaX0sAibZsDun6sicUzdQ/640?wx_fmt=jpeg)

**关键词**

破解手机

换个 SIM 卡，就能解锁别人的手机？！

并且整个解锁过程不超过两分钟。

一位外国小哥偶然间发现了谷歌 Pixel 手机上的这个漏洞：

> 能够直接绕过手机本身的指纹和密码保护，切换手机卡就能更改密码解锁屏幕。

严格来说，这个漏洞并非谷歌 Pixel 手机“独有”，而是 Android 系统中的一个 bug，任何基于 Android 搭建的操作系统都可能受到影响。

例如有网友试了试开源安卓系统 LineageOS（刷机党常用系统），就发现同样“中招了”：

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTupDXgHOIobTp4ZBhdJe27ibA0gALvJ7kl3vEAfqib642XiaE8B1clUmWOg/640?wx_fmt=jpeg "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

还有网友在自己的 Android12 系统上试了下这种破解方式，“it works”！

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTunGUPzyfSqichZqxrHUVNH6pqE2e1EygG0gqiaNFAUFbJFlEzRpX4b12A/640?wx_fmt=jpeg "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

不过这还不是最离谱的，更离谱的是这位小哥在向谷歌反馈之后，安全团队隔了近半年才修复这个漏洞。

在说小哥和谷歌关于这个漏洞的“拉锯战”之前，我们先回过头来看看这是个什么样的漏洞？

## 2 分钟内就能破解手机锁屏

小哥“贴心”地上传了以破坏者视角破解漏洞全过程的视频，整个过程花了不到两分钟。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTuO9fjWaujwtzClYhQUUJWedj1iaK7tMIM02O1sGr1JltOF6DE6g2siarQ/640?wx_fmt=jpeg "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

话不多说，直接来看。

首先用错误的指纹和手机密码解锁手机，直至锁定。

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTuTNbCqu3icMfQ8QobmI4PkhPoBE2BnUhX3aZETgsCOEthe8JouGQFLRw/640?wx_fmt=gif "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

然后用一张其他的 SIM 卡直接更换手机原来的 SIM 卡。

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTuW3zxXD3XSFX8DzbiaRO3RoMKn30zldXpwESq1EuNwnJ2xuMia3Ba9lGw/640?wx_fmt=gif "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

接下来再用错误的 SIM 卡密码（注意：这里的密码和手机密码不是一回事）锁定 SIM 卡。

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTuCVzGTsF4KdaKP94RsP2Gk043vppibndYWrMro86ribsXHa0oCaQ16jHg/640?wx_fmt=gif "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

SIM 卡被锁定后，手机便会索要其 PUK 密码，在这 SIM 卡的原始包装上，如果丢失也可直接打电话向运营商查询。

> PUK（Personal Identification NumberUnlock Key），SIM 卡自带的 PIN 解锁码。

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTuM3Z6kHuo9rrR2oSGPovL8JABfG6eTz0cxOiaqgKuhSlQ0ekOnCqmBsQ/640?wx_fmt=gif "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

输入 PUK 密码后，直接重置新 SIM 的密码便能开锁，手机原有的密码和指纹都成功绕过。

bingo！

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTuw9LicuibG2vqU3fRe7mic4PfFWjuCibDGEOoJax4c8PLFk0rxUTNXA6bwA/640?wx_fmt=gif "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

至于是如何发现这个漏洞以及为什么过了近半年才修复这个漏洞，也是个很有意思的过程。

以下是小哥的经历：

当时手机电量快耗尽关机了，他充上电重新启动后，手机要求提供 SIM 卡的 PIN 码，但却突然忘记了密码，在乱试一通之后“成功”把手机锁定。

要解开这个锁定便需要 PUK 密码，所幸他找到了原有包装并输入了 PUK 码。结果，重置 SIM 卡密码后，手机竟然直接解锁了！

发现这个大 Bug 之后，小哥向谷歌（Android VRP）提交了这个内部漏洞报告，也是从这时开始，小哥和谷歌的“拉锯战”开始了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTulib3AZfZjRTOVBHaBNj09GjgkT34lSicseYJOMOibxLsQWNFhKULUziafg/640?wx_fmt=jpeg "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

他仔细查看了 Android 和谷歌的设备安全奖励计划，发现自己最高可以获得 10 万美金的奖励，于是便申请了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTus0QgaeC7E8CN1LibKHo3ica7dV0TicZswiadxoj9z9YA8ibiaGawBvwicMaWg/640?wx_fmt=jpeg "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

不过在报告提交一个月后，小哥收到了 Android 安全团队的一份邮件：

> Android 安全团队认为，这个问题另一位外部研究人员之前已经报告过了。

对此小哥认为，这份回邮的言外之意就是，最高十万美金的奖励他一分钱都拿不到。

时间又过了一个月，小哥收到安全团队的邮件，对方称漏洞还在修复中……

又又过了一个月，九月谷歌发布了新的补丁，但这个 Bug 依旧没有修复……

不过小哥也不是轻言放弃的人，他直接来到谷歌办公室，用谷歌 Pixel 手机演示了一下这个漏洞。

而后他给安全团队定了个漏洞修复期限：10 月 15 日之前。而对方的回复也很干脆：10 月份这个 Bug 修不好！

在拉扯一番后，小哥和谷歌建立了联系，能够实时得到漏洞修复的反馈。

谷歌方也确定了修复工作的具体时间：11 月份进行，现在这个漏洞已于 11 月 5 日谷歌的安全更新中被解决。

值得一提的是，关于提交漏洞的奖励，小哥最终也拿到了 7 万美金，不过谷歌对此还做出了一番解释，用小哥的原话来说，就是：

> 尽管我的报告是重复的，但正是因为我的报告，他们才开始着手修复。正因为如此，他们决定破例一次，并奖励给我 70000 美元。

小哥和谷歌的完整对话链接附在文末了，感兴趣的伙伴可以自行查看。（手动狗头）

## 究竟为什么会出现这样的漏洞？

现在，谷歌的安卓工程师们终于把这个漏洞给补上了。

然而让小哥惊讶的是，bug 修复远不止他想象的“一行代码补丁”那么简单。

从提交的修改情况来看，光是要改动的文件数量，就达到 12 个：

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTuBOUvtI5S6F7FicK0GUpIYylUg6uzXCTg6iaFGgBL7DvVS4o86d7fCNaw/640?wx_fmt=jpeg "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

所以这个漏洞究竟是怎么出现的？

简单来说，Android 系统中有一个叫做“安全屏幕”（security screen）的概念，其中包含两种东西，一种是 PIN、指纹、密码等各种直接解锁密保的屏幕操作，另一种是 SIM PIN 和 SIM PUK 等各种解锁手机锁定状态的操作。

这些操作被放在一个栈（stack）中。

正常解锁谷歌手机时，直接用 PIN、指纹或密码都可以，但不能超过 3 次，否则就会被锁定。

但如果忘记密码，手机（在输入 3 次错误密码后）被强制锁定了，同时 SIM PIN 条目可见，它就会被放置在其他屏幕解锁操作之上，用来让你解除手机的锁定状态。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTuzsDMpUzOH79824xCUGGEg2VWIpsFibM8aZjbHdvtXLPVicJ7B0ic5DsHA/640?wx_fmt=jpeg "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

△ 栈原理

这时候，如果使用 SIM 卡自带的 PUK 密码，就能通过一个叫“PUK 重置组件”的模块调用.dismiss() 函数，将手机锁定解除，并继续显示栈下面的其他屏幕解锁操作，在小哥的案例中是指纹锁屏。

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGyliaDertlyA7whXh8d4ibC3ibTuRKshZ5w9N1JQsop0oQy1ubdAdW3H2N9Ne1bibR7Ib7xy0J4XuUG0Haw/640?wx_fmt=jpeg "安卓锁屏不到 2 分钟被破解，仅需换一张 SIM 卡")

△ 就是这个函数

这里注意，.dismiss() 函数可不是一个“专人专用”的函数，它并不只会解除 SIM 卡的手机锁定屏幕，连 PIN、密码和指纹之类的正常锁屏也能解锁……

这就导致它极容易受到竞态条件影响，一旦两个线程执行顺序出现一点儿误差，就可能导致屏幕解锁出现问题。

> 竞态条件即两个或者以上进程或者线程并发执行时，其最终的结果依赖于进程或者线程执行的精确时序。

举个栗子，如果在“PUK 重置组件”的模块调用.dismiss () 函数之前，就有操作改变了当前的安全屏幕，那么.dismiss () 函数就可能误解锁指纹锁屏。

关键来了，由于手机 SIM 卡状态是随时更新的（系统一直在监视 SIM 卡状态），因此如果 SIM 卡状态发生变化，系统也会更新当前的安全屏幕。

所以一旦“PUK 重置组件”成功调用了.dismiss () 函数，它就会在解锁 PUK 屏幕之前，直接先解锁了指纹锁屏！

根据谷歌公开的漏洞报告，它在 Android 10 到 Android 13 系统中都可能出现

***END***

阅读推荐

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhq21Ig7PruTjVJd3RMrMQiceqibJ72SL96lmoZMCK0dUlhIweJHic3NWsSY408SXhmnA0KLib6ekOVvA/640?wx_fmt=jpeg)[【安全圈】泰安：手机店主为“拉新”非法售卖公民个人信息，抓！](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652024195&idx=1&sn=9b06a0694abe53aadcb61f9e1200affd&chksm=f36f81c3c41808d5eb61fccb1d5a045d7602d3fc975dbb098e5e4cb0f0a81c52716d6908e66a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhq21Ig7PruTjVJd3RMrMQicSGe4jFPxvKtyoAESbnrbJzbMa7l97mAdO7PmBEV8xiaeUIlJs1IVRibw/640?wx_fmt=jpeg)[【安全圈】山西网警打掉一批网络账号黑色产业链条](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652024195&idx=2&sn=99cf8c2ef8776d75052f68cb5c270d9e&chksm=f36f81c3c41808d5a0aa52bb5cdc5252865fc3f1dfe230ad94d86902818a12fb51a5b49fde30&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGyljVgGtO1zVwuyWctfkDNUK5RzKUsFicEyicnkpAImiaFPUDKZOy5EiabNRkBWvYCaGehVic1q1yxAaZaGA/640?wx_fmt=png)[【安全圈】俄罗斯背景的 LockBit 勒索软件运营商在加拿大被捕](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652024195&idx=3&sn=6c69983c45e88d0f088cc1cc482cd2cc&chksm=f36f81c3c41808d5427bba9e88e3b59d7b86a36793613844ad017d488969d5d501544f61b48e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/aBHpjnrGylhq21Ig7PruTjVJd3RMrMQicYUPGj5sb6EhO261rI0YDTnNODe4mFMa2hEibmpGjjMPekZZuFTicbWdQ/640?wx_fmt=jpeg)[【安全圈】猖狂至极！黑客三度泄露medibank用户信息！新增240位受害者！犯罪分子何时才能束手就擒](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652024195&idx=4&sn=cf4c1c186e6e90c631cb7933540d20b2&chksm=f36f81c3c41808d591e4821bf3d71dd8d71de173a2eaf8c2b05335be945bc0e17a019dda78e8&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPour...