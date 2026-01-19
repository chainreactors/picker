---
title: 【安全圈】潜伏 5 年、装机量超 84 万！这款浏览器恶意插件竟靠一张图片瞒天过海
url: https://mp.weixin.qq.com/s/i0T83VrRfw_3dgSikALXaA
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:36:23.627612
---

# 【安全圈】潜伏 5 年、装机量超 84 万！这款浏览器恶意插件竟靠一张图片瞒天过海

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljOibkS9N0yPEicsF8t1QyFgicAa1iaoib0kXuSkDkgTrq7oZAVyLM74KKHo1RJLn2TyY4SlJlctAofwXQ/0?wx_fmt=jpeg)

# 【安全圈】潜伏 5 年、装机量超 84 万！这款浏览器恶意插件竟靠一张图片瞒天过海

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意插件

一款起初只是被标记为 “可疑” 的浏览器插件，如今已演变成一场波及甚广的网络安全隐患，而绝大多数用户对此毫无察觉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljOibkS9N0yPEicsF8t1QyFgicjPfDxNpE89hicdUxpyU4N3A3EhibcqAtekyttfd5GIRKwa7goudibw4sA/640?wx_fmt=png&from=appmsg)

上个月，网络安全机构 Koi Security 发布了一份针对火狐浏览器插件的分析报告，这款被命名为 GhostPoster 的恶意插件，采用了一种极为隐蔽的作恶手法，成功避开了插件审核人员常用的检测预警机制。

GhostPoster 的作案套路十分狡猾：它将恶意载荷隐藏在看似无害的 PNG 图片文件中。待插件安装后，这张图片会被解码并执行恶意程序。凭借这一手段，该插件轻松绕过静态分析工具和人工审核，全程未触发任何可疑警报。

## Koi 披露后，LayerX 顺藤摸瓜挖出更大黑幕

在 Koi Security 公布调查结果后，安全公司 LayerX 随即对这款插件背后的运营基础设施展开追踪。

这一查，竟牵出了一个庞大的恶意插件网络：另有 17 款浏览器插件，与 GhostPoster 共用同一套后端系统和作案流程。这些插件累计下载量超过 84 万次，部分插件更是在用户设备上潜伏近 5 年，始终未被发现。

此外，LayerX 还在该恶意攻击团伙的作案链条中，发现了一个更高级的插件变种。这款变种插件新增了多重规避检测的手段，虽独立下载量仅有 3822 次，但从其设计来看，攻击团伙显然是在长线布局，而非急于牟利。

LayerX 官方明确表示：“在 Koi Security 发布相关报告后，我们通过调查发现，另有 17 款插件与该恶意网络共享基础设施及战术、技术与程序。这些插件累计下载量超 84 万次，部分插件更是在网络空间中活跃长达 5 年之久。”

值得注意的是，这场恶意攻击并非始于火狐浏览器。调查人员溯源发现，该团伙最早是在微软 Edge 浏览器上试水，待基础设施搭建成熟后，才将恶意插件扩散至谷歌 Chrome 和火狐 Firefox 两大主流浏览器。

研究人员分析，这种缓慢扩张的模式，恰恰暴露了攻击团伙的长期作战策略 —— 他们更看重插件的持久潜伏，而非扩张速度。先让插件获取用户信任、稳定运行，再伺机发动恶意攻击。

## 应用商店下架，但已装插件仍在作恶

据 LayerX 向科技媒体Hackread.com提供的博客内容显示，在安全机构披露相关情况后，Mozilla 和微软已迅速将涉事插件从官方应用商店下架。

但需要警惕的是，下架操作只能阻止新用户下载，**已经安装在用户设备上的恶意插件，仍会照常运行**。这意味着，用户必须手动卸载这些插件，才能彻底消除安全隐患。

此次事件再次敲响警钟：浏览器插件，已成为网络犯罪分子入侵用户设备的 “捷径”。

因此，广大用户务必养成定期检查插件的习惯：及时查看已安装的浏览器插件列表，严格限制插件权限，对于不再使用的插件，果断卸载，不给网络黑手可乘之机！

***END***

阅读推荐

[【安全圈】男子利用购物平台漏洞窃取用户信息并骗取佣金1878万被判刑](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073757&idx=1&sn=b7baabf15c246b7188cec3311d4fcb74&scene=21#wechat_redirect)

[【安全圈】AMD Zen 1~5全系CPU曝出StackWarp漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073757&idx=2&sn=568bc60bf24ebbbc562831d29e7b2c5a&scene=21#wechat_redirect)

[【安全圈】微软确认：Windows更新出现新Bug！直接没法关机](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073757&idx=3&sn=ed7ee21674fa04822a66e4c80c98184c&scene=21#wechat_redirect)

[【安全圈】腾讯FPS大作突发崩溃引热议！玩家抱怨:网费谁补偿？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073743&idx=1&sn=d569c1593013a127f457b74734010c74&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过