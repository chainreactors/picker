---
title: 【安全圈】重大突破，谷歌AI大模型首次找到0Day漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065731&idx=4&sn=1865f8c94d510093c5028b8b63f9b02a&chksm=f36e6383c419ea9504d4986e57eb7b3947367eebcc2f52aa9f277891a3fa457671970378d39b&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-06
fetch_date: 2025-10-06T19:19:53.215554
---

# 【安全圈】重大突破，谷歌AI大模型首次找到0Day漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhwuPJNeqicbczHxTHJ7Ok9as2PickWtyibAwbuYGRqSib1pZtTgARlu80DUYtNggGkrwN42Tib3n2jIfQ/0?wx_fmt=jpeg)

# 【安全圈】重大突破，谷歌AI大模型首次找到0Day漏洞

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

零日漏洞

谷歌公司日前表示，旗下一款名为“ Big Sleep”（前称 Project Naptime）的大语言模型（LLM）辅助框架在 SQLite 开源数据库引擎中发现了一个零日漏洞，并称这是该类型AI工具首次在实际广泛使用的软件中发现零日漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhwuPJNeqicbczHxTHJ7Ok9a9DvMcWz1IlSRoxAQS7BUXKEicAnOp7uaKHibib5rkQ7TsjH4icIM4vZm2g/640?wx_fmt=jpeg&from=appmsg)

SQLite 是一种在开发人员中流行的开源数据库引擎，所发现的漏洞指向其中的堆栈缓冲区下溢，当软件在内存缓冲区开始之前引用内存位置时，就会出现该漏洞，从而导致系统崩溃或任意代码执行。

谷歌研究人员在 10 月初向 SQLite 开发人员报告了该漏洞，对方在同一天修复了漏洞。由于漏洞是在正式版本出现之前被发现，因此不会影响正在使用SQLite的用户。

发现该漏洞的“ Big Sleep”AI模型属Google Project Zero 和 Google DeepMind 之间的合作项目，旨在大型语言模型的辅助下进行漏洞研究。谷歌指出，在 8 月 DEFCON 安全会议上，负责创建 AI 辅助漏洞研究工具的网络安全研究人员表示在 SQLite 中发现了另一个问题，从而激发团队研究是否可以从中找到更严重的漏洞。

通常，许多公司使用一种称为“模糊测试”的过程，通过向软件提供随机或无效数据来测试软件，这些数据旨在识别漏洞、触发错误或使程序崩溃。但谷歌认为，模糊测试在帮助防御者找到难以（或不可能）发现的漏洞方面做得还不够，希望利用人工智能可以缩小这一差距。

而长期存在的漏洞变体问题也是“ Big Sleep”项目的主要动机之一， 谷歌在 2022 年发布的报告就曾指出，40% 以上的零日漏洞是已报告漏洞的变种，另有超过 20% 的漏洞也是以前的野外零日漏洞的变种。随着这种趋势的持续，模糊测试已无法成功捕获此类变体，而对于攻击者来说，手动变体分析成为一种经济高效的方法。

在“ Big Sleep”中，研究人员利用 LLM 的代码理解和推理能力，在识别和演示安全漏洞时利用 AI 代理来模拟人类行为，其中需要使用一套专用工具来允许代理浏览目标代码库，并在沙盒环境中运行 Python 脚本以生成用于模糊测试的输入、调试程序并观察结果。

“我们认为这项工作具有巨大的防御潜力。在软件发布之前就发现软件中的漏洞，意味着攻击者没有竞争的余地：漏洞甚至在攻击者有机会使用它们之前就被修复了，“谷歌表示。

但谷歌也强调，这些仍然是实验结果，“ Big Sleep”研究团队的立场是，在发现漏洞方面，目前特定于目标的模糊测试程序可能至少同样有效。希望在未来，这项工作将为防御者带来显著的优势——不仅可以找到崩溃的测试用例，还可以提供高质量的根本原因分析，分类和修复漏洞在未来也可能会更便宜、更有效。

参考来源：Google's AI Tool Big Sleep Finds Zero-Day Vulnerability in SQLite Database Engine

Google uses large language model to discover real-world vulnerability

***END***

阅读推荐

[【安全圈】微软正式推出Windows Server 2025服务器操作系统 支持到2034年10月](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065716&idx=1&sn=5b3532550832d4ca38067a529e8bdc54&chksm=f36e63f4c419eae2a500676eb102c8f8c2c17aa30bb355abd81f9229eb63e6ffa0b11a771ef9&scene=21#wechat_redirect)

[【安全圈】ChatGPT网络搜索功能使用微软必应搜索技术 爬虫名称为OAI-SearchBot](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065716&idx=2&sn=3c84e8540d99ae9a81e5c396504ca3c2&chksm=f36e63f4c419eae2133d645496e425508bb4f99e52efa633eede08a6369cf9f89e002e4d60da&scene=21#wechat_redirect)

[【安全圈】近100万台存在高危漏洞的 Fortinet、SonicWall设备正暴露在公开网络中](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065716&idx=3&sn=4ec937a68fa76b1dd2f7886b3dd43d0d&chksm=f36e63f4c419eae26346e5c246903fa5cc2a9c17201ee9dd85aeef72b7c9d75b82527433ca2e&scene=21#wechat_redirect)

[【安全圈】Lunar SPIDER重整旗鼓：金融业成为最新恶意广告活动的目标](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065716&idx=4&sn=ea31cc52f299e5e6a2b3cb7ac382bdef&chksm=f36e63f4c419eae2a411e15f4c973f9ba21536820946b3c0db1617f4673d9ccefc4e701aa046&scene=21#wechat_redirect)

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