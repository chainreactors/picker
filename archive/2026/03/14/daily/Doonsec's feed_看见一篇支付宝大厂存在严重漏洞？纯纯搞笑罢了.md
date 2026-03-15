---
title: 看见一篇支付宝大厂存在严重漏洞？纯纯搞笑罢了
url: https://mp.weixin.qq.com/s/P6D3qIFOJSMcq0uKRzhZzw
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:25:50.562029
---

# 看见一篇支付宝大厂存在严重漏洞？纯纯搞笑罢了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WHbpDrC5sHZvDiclHtL1U450HcrfrLmRAEMBgH78euIhEAKDaD89SXC2q3uXy01sFrItrLRqMiaicECmk9AHoIlVwPKcRibnPjIo9tIn1cuyddM/0?wx_fmt=jpeg)

# 看见一篇支付宝大厂存在严重漏洞？纯纯搞笑罢了

苏魂
苏魂

苏魂学安全

![]()

在小说阅读器中沉浸阅读

起初看见这篇文章无意中看见微信群发一张图，发现他们都在讨论这件事，然后看了评论区很多人不懂的还疯狂带着节奏，我还以为真是什么重大漏洞支付宝官方给忽略，我心想应该不至于把。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WHbpDrC5sHatxldOK283dUwyKmo7c05gzPGib7lcXe7X1quAgKiaFFXKfMnGqiaeEcYR9e46SkFpkBsDxn7ts18xQbjibNglVvDUDtZ26Py8Its/640?wx_fmt=png&from=appmsg)

然后直接打开它公开链接看下，首先刚开始我没仔细看报告，而且如果没自信看报告很容易被它标题忽悠。仔细一看这次倒真不是厂商的问题，是提交作者的问题，后面仔细一看这不是纯纯把ai扫描结果的然后交上去。真以为一个ai会使用人人都是安全研究员？另外为什么要这么说下面可以给大家解释下，因为大家不了解安卓组件漏洞，可以给大家科普下这份交了什么东西，不用听它那边瞎扯一堆东西

![](https://mmbiz.qpic.cn/mmbiz_png/WHbpDrC5sHZQbeRBwAD6YnoejzicfzGjek6iagtqax2vnHnrnWbHmDSlrwIDTqc8OSnCAhYyHoIGn9XCsCU5y44wmVFicb8XoyHpDPNicS11NGM/640?wx_fmt=png&from=appmsg)

然后貌似这位号称把poc给公开来看看它poc写了什么东西？首先就来先看看它说的几个严重漏洞

来说说它这个0交互deeplink敏感信息页面直接暴露甚至还写了poc？这里很明确的说明下这个不是漏洞，为啥要这么说，这里你可以当作你是用户，首先b业务下有个修改密码页面，然后攻击者写了一个a站点，然后a站点写了一个url跳转到b站点网站。且用户需要主动点击你的钓鱼网站，还需要再次点击此处，才能跳转b站的本身修改密码业务，相当于你绕了一大圈让用户又修改密码   ，简单来说这只是**钓鱼诱导 + 正常跨站跳转**，攻击者并未绕过 B 站点任何鉴权与校验，改密码仍需用户主动操作与身份验证，**不属于安全漏洞，注意它这里并不是web端的CSRF而是纯纯钓鱼链接**

![](https://mmbiz.qpic.cn/mmbiz_png/WHbpDrC5sHYU2SBdOJwIbArwta8NcibsJDneQdmOmOiagVz45T3AR9xtUt1vLIkZPq9w33UWalXe0Lk9MFZbiczm0RG1beej5tahOZNeXxpF0U/640?wx_fmt=png&from=appmsg)

然后它的poc是公开的可以来看下它的POC是怎么写的，说是无需授权呢怎么可以无需授权GPS权限？这不是纯纯自己没去复现然后ai生成的

这个又作何解释呢？为啥要手动打开GPS权限，并且用户还要主动点击你的链接还要手动授权GPS权限才能获取经纬度，另外就算是能获取GPS，从Android11及以上版本或者ios本身是用户需要二次点击确认才能获取，这个危害不是纯纯的钓鱼吗？除非你能deeplink能获取用户的token或者导出敏感信息这样才算是高危，把这个ai生成一直给src压力，真的没有必要，本身没有危害东西硬是吹的上天。然后还有它这个Android端的jsbridge本身你打开任何一款app，都会你有你的手机号型号，IP地址，况且需要从Android11及以上版本需要二次允许后，然后又要恰好又要点击你的钓鱼网站，你管这叫漏洞，这不是纯纯搞笑。然后顺便提下如果你打开任何一个网站，网站nginx日志本身就是能看到对方手机号型号跟IP地址，那按照这说法你打开我的网站了，算是信息泄露而且还是严重漏洞或者高危漏洞哈

所以请各位不要轻易网上带节奏，本身就是ai生成报告，作者硬是把没有危害吹上头罢了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/WHbpDrC5sHYhzqwzJzuc7rQrX1uDTw1XpWnC7odSytHbbZSeRKeXBJTucFqhqSBlJ4Q7yZsCg6Qic9ELrEkC5W0ibGTxa7QJBELAibkaia0qdJI/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UE5POEcoQydy68UxeiaVy1sS9WBP74TKVJ3rT6nPdm2K5uUXT8WpQt6IaLhTKRTM47OrRVyN1lDxg1oyOVA4qwg/0?wx_fmt=png)

苏魂学安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UE5POEcoQydy68UxeiaVy1sS9WBP74TKVJ3rT6nPdm2K5uUXT8WpQt6IaLhTKRTM47OrRVyN1lDxg1oyOVA4qwg/0?wx_fmt=png)

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