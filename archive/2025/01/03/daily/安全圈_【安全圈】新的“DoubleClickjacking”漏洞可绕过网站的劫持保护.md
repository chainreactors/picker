---
title: 【安全圈】新的“DoubleClickjacking”漏洞可绕过网站的劫持保护
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067095&idx=3&sn=6a10a23e41cc2e64a94951ad4f2b52a7&chksm=f36e7957c419f041c9d193510f5453c8bce347ca65375be93267debb7b12fefaa85fa6841c88&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-03
fetch_date: 2025-10-06T20:10:05.248645
---

# 【安全圈】新的“DoubleClickjacking”漏洞可绕过网站的劫持保护

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgeDMicLOlDVtx02W5UwWKa6hnLviaTq9lxEFFDGdoEC5ENEkQn8P22BsCUzXibyLgkuE2VfZTepOp6w/0?wx_fmt=jpeg)

# 【安全圈】新的“DoubleClickjacking”漏洞可绕过网站的劫持保护

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

安全专家揭示了一种新型的“普遍存在的基于时间的漏洞”，该漏洞通过利用双击操作来推动点击劫持攻击及账户接管，几乎波及所有大型网站。这一技术已被安全研究员Paulos Yibelo命名为“DoubleClickjacking”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgeDMicLOlDVtx02W5UwWKa6s66mzrur1iaohT5R4STXBUYjmJLiarKFMPx5oQriaicfevnVx2o10xdKFw/640?wx_fmt=jpeg&from=appmsg)

Yibelo指出：“它并非依赖单一点击，而是利用双击的序列。这看似微小的变化，却为新的UI操控攻击敞开了大门，能够绕过所有现有的点击劫持防护措施，包括X-Frame-Options头部或SameSite: Lax/Strict cookie。”

点击劫持，亦称作UI重定向，是一种攻击手段，诱使用户点击看似无害的网页元素（如按钮），进而导致恶意软件的安装或敏感信息的泄露。DoubleClickjacking作为这一领域的变种，它利用点击开始与第二次点击结束之间的时间差来规避安全控制，以最小的用户交互实现账户接管。

具体步骤如下：

> 1. 用户访问一个由攻击者控制的网站，该网站要么在无需任何用户操作的情况下自动打开一个新的浏览器窗口（或标签页），要么在点击按钮时打开。
> 2. 新窗口可能模仿一些无害的内容，例如CAPTCHA验证，提示用户双击以完成操作。
> 3. 在双击过程中，原始网站利用JavaScript Window Location对象悄悄重定向至恶意页面（如，批准恶意的OAuth应用程序）。
> 4. 同时，顶层窗口被关闭，使用户在毫不知情的情况下通过批准权限确认对话框授予访问权限。

Yibelo表示：“大多数Web应用程序和框架都认为只有单次强制点击存在风险。DoubleClickjacking引入了一层许多防御措施从未考虑过的内容。像X-Frame-Options、SameSite cookie或CSP这样的方法无法抵御这种攻击。”

网站所有者可通过客户端手段消除这类漏洞，默认禁用关键按钮，仅在检测到鼠标手势或按键时激活。研究发现，诸如Dropbox等服务已经实施了此类预防措施。作为长远解决方案，建议浏览器供应商采纳类似X-Frame-Options的新标准来防御双击利用。

Yibelo强调：“DoubleClickjacking是一种众所周知的攻击类别的变种。通过利用点击之间的事件时间差，攻击者能够在瞬间无缝地将良性UI元素替换为敏感元素。”

此次披露距离研究人员展示另一种点击劫持变体（即跨窗口伪造，亦称作手势劫持）已近一年，该变体依赖于说服受害者在攻击者控制的网站上按下或按住Enter键或空格键以启动恶意操作。

在Coinbase和Yahoo!等网站上，如果已登录任一网站的受害者访问攻击者网站并按住Enter/空格键，则可能被利用来实现账户接管。

“这是因为这两个网站都允许潜在攻击者创建具有广泛权限范围的OAuth应用程序以访问其API，并且它们都为用于授权应用程序进入受害者账户的‘允许/授权’按钮设置了静态和/或可预测的‘ID’值。”

参考来源：https://thehackernews.com/2025/01/new-doubleclickjacking-exploit-bypasses.html

***END***

阅读推荐

[【安全圈】网络安全公司员工监守自盗：编写黑客代码窃取2.08亿条公民个人信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067069&idx=1&sn=f3c972e235871147200f79b82f689d25&scene=21#wechat_redirect)

[【安全圈】捷某网络云平台漏洞曝光：50000 台设备面临远程攻击风险](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067069&idx=2&sn=516425f9b9c6da18a71ed20d3b724b4b&scene=21#wechat_redirect)

[【安全圈】黑客利用第三方SaaS服务成功入侵美国财政部系统](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067069&idx=3&sn=bd0876c49c1d286c84408344ea9a8bc8&scene=21#wechat_redirect)

[【安全圈】日本航空公司遭网络攻击导致全球瘫痪](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067033&idx=1&sn=3ae632fb4839dc14720917aa26fe469c&scene=21#wechat_redirect)

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