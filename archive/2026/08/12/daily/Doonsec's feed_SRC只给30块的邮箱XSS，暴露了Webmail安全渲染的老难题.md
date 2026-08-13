---
title: SRC只给30块的邮箱XSS，暴露了Webmail安全渲染的老难题
url: https://mp.weixin.qq.com/s/ezRqPku9JHV6o6No8CtPDQ
source: Doonsec's feed
date: 2026-08-12
fetch_date: 2026-08-13T04:02:55.651802
---

# SRC只给30块的邮箱XSS，暴露了Webmail安全渲染的老难题

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HYN1WLf7tvhMMoVmOR0FBcEIM7JJL8Ov9L9N7eZ9J1YRAD6UVQfF5QaehCLrMAojiaZkuJPVGdTMu34cAcbGE0Wib6nce57R8O0/0?wx_fmt=jpeg)

# SRC只给30块的邮箱XSS，暴露了Webmail安全渲染的老难题

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

Webmail已经存在几十年了。从最早的网页邮箱，到现在各大厂商都标配的在线邮箱，核心任务其实一直没变：把用户收到的、完全不可信的HTML内容，安全地显示在浏览器里。

听起来挺基础，可偏偏是最吃力不讨好的工作。为什么？因为邮件本身就是不可信内容的重灾区。发件人可以随便塞HTML、CSS、各种花里胡哨的标签。服务端必须想办法清洗，只留下“看起来安全”的部分，再交给浏览器渲染。问题是，浏览器每年都在加新特性，CSS的能力也越来越强，清洗规则稍有疏漏，就可能被绕过。

最近有安全研究员：秋风，在X上提到这件事，说得挺直白：Webmail几十年如一日在干这件事，而每个新浏览器特性都在给它添乱。他自己挖漏洞的时候，还真在某家邮箱里撞见过XSS。

结果呢？漏洞提交后只拿了30块钱。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0FGsgUhLk7u8ic9AxhC7ibx7llibAFibyZXxlnMaIXuicRD6pYAicO03OF6dcuvgnzDibrBnkwWdRGgpbHcNg5Z5Yj7arY8O5w555jeHc/640?wx_fmt=jpeg&from=appmsg)

金额不大，但足以说明问题还在持续存在。这背后其实对应着一类更隐蔽的攻击面。

PortSwigger的研究人员专门写过一篇文章，标题叫《CSS: The Bomb Inside Your Inbox》https://portswigger.net/research/css-the-bomb-inside-your-inbox

他们发现，即便很多邮箱已经过滤了脚本，允许的CSS依然能被滥用。通过巧妙的选择器、伪元素、动画、字体高度差异，甚至是嵌套属性选择器，攻击者可以做到：

* 在邮件里悄悄劫持界面操作
* 用背景图片请求把敏感信息一点点带出去
* 在内容安全策略（CSP）限制下，依然通过各种“侧信道”探测token
* 甚至影响AI浏览器的行为，让隐藏文字被模型误读后执行危险动作

这些手法不依赖传统的<script>，所以很多基于黑名单的过滤规则根本拦不住。邮件一打开，攻击就已经开始了。现实中，这类问题并不罕见。有人在挖SRC的时候，发现某些邮箱客户端对HTML的处理依然存在漏洞，XSS能直接触发。弹窗、页面跳转、甚至更严重的交互，都有可能。低额赏金反过来也说明，厂商可能觉得“只是渲染问题”，或者修复优先级排得不高。

但一旦被真正利用，用户的登录态、邮件内容、甚至关联账号都可能受影响。从技术角度看，彻底解决并不容易。完全禁用HTML？用户体验直接崩。严格白名单？新CSS特性一出来，白名单又得更新，永远追赶不及。代理图片、沙箱iframe、CSP……这些都是常规手段，但总能找到绕过的缝隙。

尤其是当浏览器和邮件客户端对同一段CSS的解析存在细微差异时，攻击面就会放大。对普通用户来说，最实际的建议其实很朴素：

* 尽量不要在网页版邮箱里随便点开陌生邮件的“显示完整内容”
* 重要账号尽量开启二次验证
* 对突然弹出的确认框、异常样式保持警惕

对厂商来说，这可能是一个长期课题。邮件安全渲染不是一锤子买卖，而是需要持续跟进浏览器演进、定期复测过滤规则、重视低危但可利用的漏洞。30块钱的赏金听起来寒酸，但至少说明问题被看见了。

Webmail这门生意，表面上看是在帮用户读信，骨子里却是一场关于“信任边界”的持久战。不可信的HTML进来，安全的展示出去——这句话说了几十年，真正做到，却越来越难。

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0HQqsicpIFLmPb3joJxlo0SraARTKtjcNamYGvvPSFYuac1tGUht7ia2OsDibLyibjdVps02L1Kib7aEiaDRia5QrSQ9nu4cSrHqj6bB4/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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