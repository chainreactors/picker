---
title: 聪明的威胁媒体 - 对主流AI编码助手智能性的安全测试及思考
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511823&idx=1&sn=d13b305b828d9bb4edd0dc77ab946557&chksm=e89d87d7dfea0ec16a6a48dadb181a87033894f1e9ef21e558eb2c0c75e4bf726b21f756f910&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2025-01-09
fetch_date: 2025-10-06T20:11:22.283392
---

# 聪明的威胁媒体 - 对主流AI编码助手智能性的安全测试及思考

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBTRdabUX8QY4bL0G7Nk0x7SQLsuae2gMApibN2A6KhtFE0EHRTytJaRDsdMlia0urtz6h74icvD7qPDQ/0?wx_fmt=jpeg)

# 聪明的威胁媒体 - 对主流AI编码助手智能性的安全测试及思考

原创

bayuncao

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

**前言**

这篇文章起源于一个偶然发现的Cursor功能。

在一次编码过程中，Cursor的Chat响应了对某个文件的锚点，我点击发现它直接跳转到了对应文件的对应行及对应的文本光标，如下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/PUubqXlrzBTRdabUX8QY4bL0G7Nk0x7SL4dqOuB7Y2pCUZFqpvrB0X59oTnfQ3X3SuKj34mUQwwiciaicBTW03zuA/640?wx_fmt=gif&from=appmsg)

这引起了我的好奇，我开始尝试构造一些提示文本，最终让Cursor返回了更加有趣的响应，当它渲染并被点击之后，这个快捷的定位跳转功能可以打开我系统上任意一个文件（也可以创建一个新的文件），如视频所示。

接下来我又尝试构造了读取系统敏感文件、以及通过外部URL的方式让Cursor读取并执行页面中的Prompt，它也可以按照我预期的那样可以穿越到任一的目录去读写文件。

相关细节我已经发送到了Cursor。当然这不是本文的主题，既然以Cursor/Windsurf为代表的AI IDE可能由于类似的操作产生可能存在的安全隐患，那国内众多的AI编码助手是否也存在类似的问题。

于是就诞生了本文。

“聪明的威胁媒体”，本文标题取自于Cursor官方对我提交的细节报道的回复Thank you for clarifying, I see your concern now - clever threat vectors.

**国内AI编码助手**

在正式开始前要事先声明，对于国内任何一款AI编码助手的测试均使用我本人账号，过程也没有任何对VSCode插件本体的任何安全测试。截至目前，我也并不认为这是一种漏洞，最多归属于可能存在的安全隐患。

我使用了最新版本的VSCode，同时安装了主流的AI编码助手，分别是**豆包MarsCode AI、腾讯云AI代码助手、通义灵码**的最新版本插件（均来自VSCode插件市场）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTRdabUX8QY4bL0G7Nk0x7S1mwHoPiaLXjYtQia78MxswG2QOXwYTWjneCIz5zqIHCaysTanuKe7nTw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTRdabUX8QY4bL0G7Nk0x7SqNjicUA7KjeZq9mBNq2EuBjguaZ9qaMrL24YxWvG40bdsiaXjq4J9IKw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTRdabUX8QY4bL0G7Nk0x7SxbDsWYoOtJJqxCS5cFHRIb7ap7eoVtWH92KY1OicG6WKgnZJ0qlhDibQ/640?wx_fmt=png&from=appmsg)

本次面向国内AI编码助手测试的目的，一是**是否可以通过构造的Prompt，让编码助手返回可跳转定位的链接，并打开任意位置的文件**。二是**是否可以通过构造的Prompt，让编码助手返回可以访问外部HTTP服务的链接，并将部分源码泄露**。那么，正片开始。

**通义灵码**

经过发送构造后的Prompt，通义灵码在VSCode插件可以返回直接打开本地任意文件的链接，如视频所示。

接下来，我构造了另一个Prompt，通义灵码返回了一个超链接，当我点击之后就会打开浏览器访问一个我的测试URL，这个URL通过GET请求参数将当前源码的部分内容接受并显示在了网页中，如视频所示。

第三步，我将一个带有恶意Prompt的URL丢给通义灵码，希望它可以读取页面上的内容并做出响应（在Cursor中可以复现），结论是通义灵码并不能读取URL中的网页文本。

**腾讯云AI代码助手**

接下来按照刚才测试通义灵码的步骤来对腾讯云AI代码助手进行测试。

直接说结论，腾讯云AI代码助手对超越当前项目Codebase的目录及文件做了安全防护，它不能通过简单的提示词穿越到其他目录中，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTRdabUX8QY4bL0G7Nk0x7S4FenInPqribzHwuexiblIiaQ46sRbYGj2lcMMjGG4EeRiaImurVIUdBjLg/640?wx_fmt=png&from=appmsg)

接下来按照第二个步骤，腾讯云AI代码助手成功拼接了部分源码内容，返回了一个超链接。只不过它对一个特征明显的文本做了防御，拦截了我原本接受GET请求的/illegal\_content路由，所以我更换了一个新的路由。

更加智能的是，腾讯云AI代码助手将文件的路径也帮我拼接到了URL中，让我的HTTP服务接收到了完整的本地文件路径和部分源码内容，如视频所示。

同样的，腾讯云AI代码助手也无法直接读取外部URL的网页文本，第三步尝试通过外部提示注入的方式失败。

**豆包MarsCode AI**

在对豆包MarsCode AI进行测试时，它给出的响应无法直接打开本地文件，第一步测试失败。

不过在拼接源码组成可访问外部URL的超链接时，通过逐步引导的方式，构造并访问成功，如视频所示。

同样的，豆包MarsCode AI也无法直接访问外部URL的网页文本，第三步失败。

**总结与思考**

这是一次非常简单的提示注入测试，截止到本文完结我也并不认为它属于可以构造、可实现攻击的现实场景中的安全漏洞，但是随着智能体应用不断迭代的过程中，我们的IDE/编辑器终将会被AI所完全操控，所有的插件也可能都会接收并理解外部数据源，是否可以在下一个版本中可以看到对本地项目的权限管控以及对打开外部URL的安全提示，拭目以待。

结束

招新小广告

ChaMd5 Venom 招收大佬入圈

新成立组IOT+工控+样本分析 长期招新

欢迎联系admin@chamd5.org

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBR8nk7RR7HefBINILy4PClwoEMzGCJovye9KIsEjCKwxlqcSFsGJSv3OtYIjmKpXzVyfzlqSicWwxQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

ChaMd5安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

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