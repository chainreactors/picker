---
title: 一个零基础小白，如何从啥都不会到挖到人生第一个漏洞？
url: https://mp.weixin.qq.com/s/tY5lmYSa0g-HdNhSe-MsCw
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:49:59.024538
---

# 一个零基础小白，如何从啥都不会到挖到人生第一个漏洞？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kzUNKm24hOodiarA7m1ic4eLfnUo96vUac4oIrraw3hNvuliaqcbQ95hSsvntpicghVf23uLGIgofbEmNJ6ic56zCgjIRicCqabYfCnW8ORMqRza4/0?wx_fmt=jpeg)

# 一个零基础小白，如何从啥都不会到挖到人生第一个漏洞？

沧海讲安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一个零基础小白，如何从啥都不会到挖到人生第一个漏洞？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9Tfx94nnVyjia2iayLNBic8UQXtQMRSTNsicKsEicOFa2UCZicmVQolnEickTWcJkoW1a3XHVBknExk3N8GFlictb7psMGGazDrRXGyDzA/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

很多人觉得网络安全觉得要精通代码、数学才能入行。其实并不是！

新手挖漏洞，前期根本不需要写代码，只要路子野、工具熟，几分钟也能捡个漏。

因为，对于大多数普通人来说，漏洞挖掘更像是一场“找茬游戏”：你需要做的，就是把自己的所学所想，去找网站、系统开发者在逻辑上的疏忽（注意bug不是漏洞）

哪怕你是文科生，哪怕你连Python 都没写过，只要肯花时间，按照正确的路径走，哪怕3个月就有可能挖到漏洞，拿到几百甚至上千元的赏金，很多师傅就是这么走来的，要知道以前初中学历的黑客大佬都一抓一大把。

如果你觉得不太可能，我把从0到1挖到第一个漏洞的实操路径拆解给你看。不讲晦涩的理论，只讲普通人能听懂、能上手的干货。

---

第一「搞懂“系统”的构建」

核心任务：死磕 HTTP 协议 + 吃透 Top 10 漏洞原理

很多小白一上来就急着下载各种酷炫的黑客工具，结果连工具报错都看不懂，最后只能当个“脚本小子”。

记住：磨刀不误砍柴工。

在这个月，你只需要弄明白两件事：

* 浏览器和服务器是怎么“对话”的？

你要搞懂什么是请求（Request）、什么是响应（Response）、Cookie 是什么、数据包长什么样。这就好比你想进别人家偷东西（哦不，是检查安全），你得先知道门在哪、窗户怎么开、锁是什么结构。重点攻克 HTTP/HTTPS 协议。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9QNMxu6N6mKNOErLOmT1xZicm3WzjqSgvQMxMsOmgMj7bnoCHeDdIiabE8Rnec8MJTsb2Io3OCwm0sgOXDc3G7IwoDCF2D3yNk6Y/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

* 常见的“破洞”长什么样？

不用学所有漏洞，先死磕 OWASP Top 10。比如：

* SQL 注入：就像你在登录框输入 ' or 1=1，骗过数据库让你免密登录。

* XSS 跨站脚本：就像你在留言板贴了一张带病毒的纸条，别人一看就中招。

* 越权访问：就像你改一下 URL 里的数字 user\_id=1001 变成 user\_id=1002，居然看到了别人的订单。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9SqrrL3swthF8pjQXiajsSp0GW5Fa2d3UvkJWmFaojoeEmxxRBypcwU8ZRoK6dmhiaAPg6tRVcqLVPwLO746ia9KzQJ8OBxbxaT7A/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

💡建议：

别啃大部头书！去 B 站或 YouTube 找那种“手绘原理解析”的视频，看动画演示比看书快十倍。

---

第二「打造你的“兵器库”」

核心任务：熟练掌握 5 款核心工具

原理懂了，现在该给你配装备了。挖漏洞其实就是用这些工具打出一套漂亮的“连招”。你不需要会开发这些工具，但必须要把这些工具用出肌肉记忆。

新手必掌握的“五大神器”：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9TwE2yBKpBOibibNKmyKfg1ejibJqG6lspm0iby8roBTxzJ5ntur27q0gRprKthzaOg11NOicXduDqq3oVBKP3hrBpWcmUSZrjFMLac/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

* Burp Suite（本命武器）：90% 的漏洞都是靠它抓包、改包、重放发现的。它是你和服务器对话的“翻译官”兼“拦截者”。

* Nmap（侦察兵）：用来扫描目标开了哪些端口，跑了什么服务，帮你摸清敌人的底细。

* SQLMap（自动化助手）：虽然提倡手工，但这个工具能帮你快速验证是否存在注入点，效率翻倍。

* 浏览器开发者工具（F12）：最容易被忽视的神器！很多逻辑漏洞、敏感信息泄露，点开 F12 看一眼源码或网络请求就发现了。

* Xray/AWVS（自动扫描器）：适合前期快速梳理资产，帮你发现一些低级的配置错误。

💡建议：

在自己电脑上搭建本地环境（如 Docker 靶场），反复操作这些工具。直到你看到报错能下意识知道是哪一步出了问题，形成肌肉记忆。

---

第三「真刀真强赢首战」

核心任务：刷透靶场    ——尝试首个 SRC 漏洞

终于到了实战环节！但请再次牢记红线：新手严禁对未授权的真实系统进行测试，那是违法的！

* Step 1：在合法靶场“练级”

先去 Pikachu 和 DVWA 这两个经典靶场。

* Pikachu：国产良心，中文界面，每个漏洞都有详细的原理和修复方案，非常适合小白建立信心。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9QCf1qiaVTx38AywcoDicD9Rff4Pb4NtwTselleFia6nHeHpYd333ewXiaKthLsEvvJv7Nwdwrw6Aiclo1p6fdMDiczSFl0UM9kQAYUs/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

* DVWA：全球知名，分四个难度。从 Low 模式开始，把 Top 10 漏洞亲手复现一遍。

通关标准：当你能在靶场稳定发现并利用 3-5 种漏洞，且能清晰写出复现报告时，你就出师了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9R38o3PbQZIfPEDpZZ3ibW41ZTfXCKOibJpfPqTUUcZ5iahhdgLwiakeBBgVnkZiccCGVc6llwf2zgUYGPuKP5fQkjVyGseLiaGCvNGY/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

* Step 2：小试牛刀，挖掘人生第一个漏洞

有了底气，就可以去 补天、漏洞盒子、各大厂 SRC 平台 注册账号，开启你的“寻宝之旅”。

* 起步策略：别好高骛远去盯大厂的核心业务（那是神仙打架）。先从 教育行业（edu）SRC 或 公益众测项目 入手。

* 寻找目标：专注找信息泄露、弱口令、低危逻辑漏洞。这类漏洞门槛低，竞争相对小，最适合新手拿“首杀”。

* 预期管理：低危漏洞一个也有几十上百块赏金。要是运气好碰上个高危，几千甚至上万也不是梦！

![图片](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9TFOAlYnlCCPqs3Qx6Vqah0hUnR5U5Ix7ibOoTYbic8DULq0mSUHibqRiabTfkxja6MutM5S6NicrFxKgLfjgicBtZJNOydy8pNF53fw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

---

第四「给普通人的几条真心话」

1、底线比技术更重要：我们学网安是为了维护安全，而不是破坏。永远只在授权范围内测试，红线千万别碰，前途和铁窗往往就是一念之差。

2、拒绝做“工具人”：只会跑软件的人永远成不了高手。遇到报错不要慌，去查日志、去分析流量，弄懂背后的逻辑才是成长的关键。

3、耐心是唯一的捷径：挖漏洞很枯燥，可能连续几天一无所获。我也经历过空手而归的焦虑，但只要坚持梳理资产、持续测试，爆发往往就在下一秒。

4、打破信息差：网上零散的教程太多，容易让人迷失。你需要一套系统化的学习路线，从理论到工具，再到实战，步步为营。

---

「最后」

如果你真的想学好一门本事，首先就要考虑自己对这门技术的兴趣，没有天赋还能靠时间和努力去弥补，但如果没有兴趣加持，就很难坚持到最后。

你要是正打算尝试网安或者想努力一次，我把这些年用过的视频教程和学习笔记都梳理出来了，现在都无偿分享给大家，需要的找我拿就行（文末自取）。

现在哪个行业都不好走，如果没有学历也没有天赋，那就只有努力和坚持了，请相信相信的力量，共勉！

**沧海专属黑客/网络攻防技术资料**

@沧海讲安全：在安全圈待了十多年，已经积累了很多的技术教程，在计算机这个行业，如果不会主动学习，手里没点学习资料，注定是走不远的。我整理的这些资料包含了市场上主流的攻防技术，不说让你成为黑客大佬，帮助你从0到进阶网络安全技术问题不大。

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

**部分技术资料预览**

**01**

***视频教程***

从0到进阶主流攻防技术视频教程（包含红蓝对抗、CTF、HW等技术点）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcYaRKqWc1cxP8sBrX6KZasFTJEVibWmdyoGAuRO4AbzaVjUJ8guoWAzQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcCP8oaOCQm8Cp2qhpCxWiaOjzYrOoA1iac5eSafBicPxSQcpYtchyfVvxA/640?wx_fmt=jpeg&from=appmsg)

**0****2**

***书籍Pdf***

入门必看攻防技术书籍pdf（书面上的技术书籍确实太多了，这些是我精选出来的）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcUumOTUmUznuo7MzKl1JiaEQIeSh4ibkO6jxY68zVZz7iayrwGRtGu2bHw/640?wx_fmt=jpeg&from=appmsg)

**0****3**

*安装包/源码*

主要攻防会涉及到的工具安装包和项目源码（防止你看到这连基础的工具都还没有）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcvsT9h4B1hS9VEPengMcOtNL24949kb4cibKLS9HkIb1k2htW8GYqzMQ/640?wx_fmt=jpeg&from=appmsg)

**0****4**

***面试试题/经验***

网络安全岗位面试经验总结（谁学技术不是为了赚$呢，找个好的岗位很重要）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6Kqcm6J0eAql29R6DIM8bJW4rweVBicM8ibGMOmLNFTpdcQ0gFvefMTOg9dA/640?wx_fmt=jpeg&from=appmsg)

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

@沧海讲安全：只要你是真心想学黑客/网络安全技术，我这份资料就可以无偿共享给你学习，但是想学技术去乱搞的人别来找我，目前全球网络环境日益紧张，我国在这方面的相关人才比较紧缺，网络安全行业确实也需要更多的有志之士加入进来，我也真心希望帮助大家学好这门技术，如果日后有啥学习上的问题，欢迎找我交流。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kWXbooRKsCUic8In0GE4Hd6nTM7iclEUG0UewS479kicpBqGcfpOAaTibhgwsEsblvqe0EsP95XKBe2E90T9g02cQg/0?wx_fmt=png)

沧海讲安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kWXbooRKsCUic8In0GE4Hd6nTM7iclEUG0UewS479kicpBqGcfpOAaTibhgwsEsblvqe0EsP95XKBe2E90T9g02cQg/0?wx_fmt=png)

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