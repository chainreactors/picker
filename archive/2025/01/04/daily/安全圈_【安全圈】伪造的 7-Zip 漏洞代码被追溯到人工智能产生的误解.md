---
title: 【安全圈】伪造的 7-Zip 漏洞代码被追溯到人工智能产生的误解
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067112&idx=3&sn=7e0c3ed063040f28dd8bb8c3ead818df&chksm=f36e7968c419f07e6117e2802423856581ea51449912efb9ef7a18550dc27bba052d7d7128e0&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-04
fetch_date: 2025-10-06T20:11:21.601882
---

# 【安全圈】伪造的 7-Zip 漏洞代码被追溯到人工智能产生的误解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaRXBZQHFJ0ZBLJTa9CQlib2S93jPssciaFPQwlWKM8ibiboPsRUBCX5Wj4KiakRXMdkeR6TjiaBTqad4qQ/0?wx_fmt=jpeg)

# 【安全圈】伪造的 7-Zip 漏洞代码被追溯到人工智能产生的误解

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

网络安全社区最近面临着一场轰动，起因是社交媒体平台 X（正式名称为 Twitter）的一名用户声称拥有流行文件归档程序 7-Zip 的零日漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaRXBZQHFJ0ZBLJTa9CQlib25eE76DQrXFAS914wsyon4XJPBrXGEPtngKRuKB3bQM7DyEaFyHnqrQ/640?wx_fmt=jpeg&from=appmsg)

该用户名为 @NSA\_Employee39 的用户声称他们发现了一个严重漏洞，该漏洞可能允许攻击者通过利用7-Zip 软件中的缓冲区溢出在受害者的系统上执行任意代码。该用户在 Pastebin 上提供了一个代码片段，据称演示了此漏洞。

“此漏洞利用了 7-Zip 软件的 LZMA 解码器中的漏洞。它使用精心设计的带有畸形 LZMA 流的 .7z 存档来触发 RC\_NORM 函数中的缓冲区溢出条件。通过对齐偏移量和有效载荷，该漏洞利用了内部缓冲区指针来执行 shellcode，从而导致任意代码执行，”用户在 Pastebin 上写道。

尽管最初引起了关注，但网络安全专家很快开始对该漏洞的有效性表示怀疑。复制该漏洞的尝试失败了，导致人们对该代码的有效性产生了怀疑。

7-Zip 的创始人 Igor Pavlov 后来驳斥了这一说法，他表示，所谓的漏洞依赖于7-Zip LZMA 解码器中不存在的函数（“RC\_NORM”） 。Pavlov 认为该代码可能是由 AI 模型生成的，这进一步削弱了其可信度。

此外，安全研究员 @LowLevelTweets 报告称无法重现声称的漏洞，并表示在测试期间没有导致崩溃、挂起或超时。这些发现表明，报告的 7-Zip 零日漏洞可能是误报，可能是由人为生成的代码或对软件内部工作原理的误解引起的。![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaRXBZQHFJ0ZBLJTa9CQlib2bJ0cAmcnHv7vXxvG7MxbhfETnqm479VKt3vSa5NOmNLPhHdK7m3G1g/640?wx_fmt=jpeg&from=appmsg)

虽然这起事件被证明是一场虚惊，但零日漏洞威胁仍然令人担忧。这些漏洞非常危险，因为软件开发人员不知道它们，因此缺乏任何预先存在的防御措施。

上个月，Hackread报告了一个 Windows 零日漏洞，允许攻击者通过欺骗性方法窃取 NTLM 凭据。该漏洞影响了各种 Windows 系统，包括 Windows Server 2022、Windows 11（最高至 v24H2）、Windows 10（多个版本）、Windows 7 和 Server 2008 R2。

为了防范零日漏洞，全面的安全软件非常重要，因为它可以提供针对各种威胁（包括病毒、恶意软件和零日漏洞）的基本保护。这些解决方案通常包括实时威胁检测、高级威胁防御和强大的隐私功能等功能，以保护用户免受网络安全威胁。

来源：https://hackread.com/fake-7-zip-exploit-code-ai-generated-misinterpretation/

***END***

阅读推荐

[【安全圈】2024 年最大的网络安全和网络攻击事件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067095&idx=1&sn=a9ecd46a4afe0c77216a405c825a1e9a&scene=21#wechat_redirect)

[【安全圈】美国财政部遭遇重大网络安全事件 怀疑与中国有关](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067095&idx=2&sn=2680436663695b4f81edee2d0c8108b1&scene=21#wechat_redirect)

[【安全圈】新的“DoubleClickjacking”漏洞可绕过网站的劫持保护](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067095&idx=3&sn=6a10a23e41cc2e64a94951ad4f2b52a7&scene=21#wechat_redirect)

[【安全圈】至少35个Chrome扩展被劫持，新细节揭示了黑客的攻击手法](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067095&idx=4&sn=6f97d873b84e125e9f9c5c98947bace2&scene=21#wechat_redirect)

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