---
title: 【安全圈】苹果发布紧急安全更新修复WebKit引擎中的漏洞 黑客已经利用漏洞展开攻击
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066097&idx=3&sn=0e0cc754f2cdc596b5f8419a8fa6f7a5&chksm=f36e7d71c419f467daf3ea8cddb360e80ba1bf2d4166d38a18b9e3f18237b4be22f6661fe72a&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-21
fetch_date: 2025-10-06T19:16:23.243772
---

# 【安全圈】苹果发布紧急安全更新修复WebKit引擎中的漏洞 黑客已经利用漏洞展开攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaCTwNPicbduqUHbw6glwC073OxDaXfV3qCX7Q59rU5GNxjVeccDy6OHeKib6nLaQibt5X9Oy2Ej2lRA/0?wx_fmt=jpeg)

# 【安全圈】苹果发布紧急安全更新修复WebKit引擎中的漏洞 黑客已经利用漏洞展开攻击

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

苹果本周发布安全公告宣布对 WebKit 引擎的两处高危安全漏洞进行修复，值得注意的是这些漏洞在修复前已经遭到黑客的积极利用，因此属于零日漏洞的范畴。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaCTwNPicbduqUHbw6glwC074kfIV3LkvOFo0dLmNicC5OE61BKc4ekicWS9DOqyPul41A6m6bulVLjg/640?wx_fmt=png&from=appmsg)

**CVE-2024-44308：**

黑客可以通过特制的 Web 内容导致任意代码执行，苹果获得的报告称该漏洞可能已经在基于 Intel 的 Mac 系统上被积极利用。

**CVE-2024-44309：**

黑客可以通过特制的 Web 内容导致跨站脚本攻击，苹果获得的报告称该漏洞可能已经在基于 Intel 的 Mac 系统上被积极利用。

值得注意的是以上漏洞也在 iOS 和 iPadOS 中存在，因此苹果还发布了 iOS 18.1.1 和 iPadOS 18.1.1 版进行修复，不过暂时没有证据表明黑客也在 iOS 和 iPadOS 平台进行攻击。

发现并向苹果提交漏洞报告的是谷歌威胁分析小组的 Clément Lecigne 和 Benoît Sevens，其中 Clément Lecigne 提交的漏洞通常都是遭到黑客利用的，或者说直接点说这名研究人员发现的漏洞通常都是由国家级黑客利用的。

这类漏洞只会针对某些具有极高价值目标的用户发起攻击，这也是为什么苹果会在 iOS 中增加高级保护模式的原因，在这个模式下 JavaScript 脚本都会被禁止运行 (本次提到的两个漏洞就有一个是 JavaScript Core 中的问题)。

来源：https://www.landiannews.com/archives/106713.html

***END***

阅读推荐

[【安全圈】2024全球最弱密码排名揭晓：“123456”再度登顶，你的密码安全吗？](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066082&idx=1&sn=4670155de7d2f2afaa5fe30fda0bb2b0&chksm=f36e7d62c419f4745f1e8bba109c904e5aeda0df116d0348b08c58ebc5650933dc2d88c24c2c&scene=21#wechat_redirect)

[【安全圈】谷歌Gemini AI 聊天机器人不断让用户“去死”](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066082&idx=2&sn=690f569a72493488bb3ecd0770623b7e&chksm=f36e7d62c419f474675d76068180a0f3bdb5172cff33e5038437f76753bc0a27164756b87d36&scene=21#wechat_redirect)

[【安全圈】美国饮用水系统存在300多个漏洞，影响1.1亿人](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066082&idx=3&sn=45c8dff3a066a1615c872523d972e645&chksm=f36e7d62c419f474a8053972dd9c71ee6170c6482642d86218c62a4788ba6c3240875f3d16fb&scene=21#wechat_redirect)

[【安全圈】VMware vCenter Server远程代码执行漏洞正被黑客广泛利用](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066082&idx=4&sn=c7244d3c2cda936e8c968cf0a2ade6d0&chksm=f36e7d62c419f474201413fc6e1edcc5c024cfb6fa12a9adf16b49526e98689324bb9aa57fd0&scene=21#wechat_redirect)

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