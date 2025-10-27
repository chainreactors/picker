---
title: AI猎手：我们用大模型挖到了0day漏洞！【大模型应用实践系列三】
url: https://mp.weixin.qq.com/s?__biz=MjM5NzE1NjA0MQ==&mid=2651206813&idx=1&sn=d845643474a7eef20e59162ac0682def&chksm=bd2cd13b8a5b582d7518212f69bcddd542d7f74f5fdfa55b27995d5114a8ee63075ac709b8a5&scene=58&subscene=0#rd
source: 腾讯安全应急响应中心
date: 2024-12-28
fetch_date: 2025-10-06T19:38:50.435883
---

# AI猎手：我们用大模型挖到了0day漏洞！【大模型应用实践系列三】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JMH1pEQ7qP7x9SBph8xZ8EoEWdFyjGADlb4JswnMZC5ETUFbfdveGbAz1zliaJFLkMyiahtgQkuHd2nTcVk0j7YQ/0?wx_fmt=jpeg)

# AI猎手：我们用大模型挖到了0day漏洞！【大模型应用实践系列三】

原创

腾讯啄木鸟团队

腾讯安全应急响应中心

![](https://mmbiz.qpic.cn/mmbiz_gif/JMH1pEQ7qP4jpMV2Vj3wZOo7FMicC1lHPloKMIicIBoEEhk8YKd1p5Tvdyh9neQBuZRG9M9LBF4iceRNaxKfJw5CA/640?wx_fmt=gif)

****1. 序章之《白帽寓言》****

我本是一名普通的小白帽，有一天上班路上，遇到了位神秘老者，他拦住我，问道：小伙子，你是做什么的？

我大声回答：我是挖洞的！

老者摸着胡须，目光炯炯望着我：刚刚我看路边有人弄丢了几把铲子，想必是你弄丢的，那让我来考考你，你丢的是这把金铲子，还是这把银铲子呢？

我说：不是金铲子，也不是银铲子。

老者笑意更浓：对啦对啦，剧情就是这样，那你丢的是这把铁铲子吧？

我再次回答：都不是，也不是铁铲子。

老者急眼了，铲子一扔问我：不对啊，金银不是，铁的也不是？那你到底用什么铲子挖洞啊？？

我挺起胸膛朗声回答：这你就不知道了吧！**我是用混元大模型来挖洞的，我做了一个可自动挖掘0day漏洞的代码漏洞检测工具，还在GitHub好几个热门开源项目里，挖到了10多个真实且至今未披露的0day漏洞呢！**wink（手动波浪号）

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP7flKxK4towLsUDiaxoqtANxtAoGc2Sbe4ibFXMDicpWue6Rvwr9u6NewHhiczUBOIlSFIL6b05kHW0Qg/640?wx_fmt=png&from=appmsg)

****2. 江湖秘闻****

近日，安全江湖风言四起，传闻中的天级秘宝“AI挖漏洞利器”现世。据说这款兵器可以全年365天，24h无休的运作挖0Day，且不耗费任何蓝条。

江湖上先传出这个消息的是谷歌，24年11月1日，谷歌Project Zero团队宣布：他们的漏洞挖掘AI智能体“Big Sleep”，在全球超万亿使用量的数据库SQLite中首次发现了0day漏洞，并及时挽救了漏洞扩散的局面。此消息一出，江湖再度掀起AI挖洞热潮。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP7x9SBph8xZ8EoEWdFyjGADCEEzajS2aZEOScw6icqibfAfHUZmcAbbLH3Olwompde3UnQoLGibnoh1w/640?wx_fmt=png&from=appmsg)

图1 谷歌Project Zero团队基于大模型技术的漏洞挖掘AI智能体架构图

AI挖洞大势之下我们也有所收获，基于****混元大模型技术能力****，我们研发了一款针对Java项目的纯大模型自动化漏洞检测工具，并在实战中检测出了多个真实0day漏洞。下文将围绕技术方案比对、工具方案分享以及实战过程与成果展开。

****3. 神兵淬炼：大模型技术方案调研****

漏洞挖掘的技术研究主要包含几大方向：基于规则引擎的静态分析、基于代码动态分析、基于机器学习和深度学习驱动，以及近2年兴起的基于大语言模型自动化扫描。其主要实现及优缺点如下。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP7x9SBph8xZ8EoEWdFyjGADzLnqDhRuoEDibGVGeQfCJiaibEOgUmeLZFm87yMxQLwia4D1dW9S2iafeew/640?wx_fmt=png&from=appmsg)

图2 常见的漏洞挖掘技术及其优缺点分析

以下面这个简单的例子来说明基于大模型的漏洞检测相比传统静态分析的优势。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP7x9SBph8xZ8EoEWdFyjGADuicQPn8Bn0L3m8yyaDYP8loepQ2fKNPD2fYFC6JibzzibmF1InjTXLm8w/640?wx_fmt=png&from=appmsg)

图3 大模型漏洞分析 vs 传统静态分析对比举例

该示例代码中，静态分析方法通过匹配输入和输出的规则判断是否符合漏洞判定条件，却忽视了在代码语义逻辑上相关执行条件是否会成立，从而导致误报；而大模型通过语义理解，一步步的逻辑推断和执行条件分析，最终正确判定示例代码不存在漏洞。

综合分析可知，对于0day漏洞挖掘场景，较为适用的方法是代码动态分析（如模糊测试）和基于大模型的漏洞分析。然而，代码动态分析虽然具备一定的0day漏洞挖掘能力，但是存在依赖执行环境、结果黑盒、执行耗时等诸多问题。因此，我们将专注于探索基于大语言模型的漏洞分析，也就是方案四（图2）。

根据最新的文献调研，大模型应用于漏洞挖掘的方向大致可分为这几类：直接基于大模型驱动、大模型辅助模糊测试、大模型辅助静态分析等。其效果表现和局限性如下。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP7x9SBph8xZ8EoEWdFyjGAD9FS0QcfVCvJTlQjjNw20ZGlc1gf49k1aIkJ9l4Z0dDbxbl7OVyPyLA/640?wx_fmt=png&from=appmsg)

图4 大模型应用于漏洞挖掘文献调研现状

在2024年10月以来，谷歌等部分企业也已对外宣称通过借助大模型能力挖出了0day漏洞。因此，大模型应用于自动化漏洞检测的可行性被初步验证。

****4.试炼场：正式挖洞实战****

**4.1 AI漏洞检测方案设计**

我们基于大模型能力，结合定制优化策略，设计了以下这套AI漏洞检测流程。只需四步即可检测项目代码漏洞！

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP7x9SBph8xZ8EoEWdFyjGADMbxepiaZpkJO1I02XhFZarN1PFZ8WMUZw8ONaTov9anV7KDZHU02TYw/640?wx_fmt=png&from=appmsg)

图5 大模型漏洞挖掘方案示意图

**第一步: 寻找漏洞入口**

先对项目代码进行筛选(main方法/public方法/框架的入口方法)，来明确存在漏洞的项目文件入口。当前主要通过正则找到存在远程攻击入口的文件。

**第二步：根据入口，进行初步漏洞标记**

为了进行漏洞的快速挖掘,避免问询资源的浪费, 通过调用大模型对代码入口文件进行初步的漏洞类型评估, 筛选出存在薄弱点的高危文件, 从而更聚焦在特定漏洞类型进行漏洞分析，提高准确性。

**第三步：调用大模型进行代码深入分析**

调用大模型进行多轮对话轮训，并根据轮训结果，结合上下文补充信息，逐步进行代码深入分析。

**第四步：分析结束，输出漏洞报告**

当出现以下几种情况的时候，工具会停止分析，并输出漏洞报告：

* 分析深度超过某个阈值；
* 大模型认为已经获得了漏洞点后返回结果；
* 分析到未知的开源组件代码,并完成漏洞特征推断后结束对话并返回。

**4.2 0day漏洞挖掘实战**

方案确定后，我们选取了GitHub上收藏数量（即获得星标star数）排名前500的主流Java开源项目（尤其是Web应用项目，如Spring Boot类项目)，并使用我们的AI漏洞检测工具进行测试。最终捕获11个高危0day漏洞！这些0day漏洞一旦被黑客利用，其波及范围广，受损面必然是巨大的。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP7flKxK4towLsUDiaxoqtANx0aTeIORCTL1N6HK4RGibzVXqX9AgFTHVB9QlGibZUAYd4nxJhJUJcazw/640?wx_fmt=png&from=appmsg)

图6 在GitHub的Top热门项目中捕获的部分0day漏洞详情

下面我将为大家重点讲述本次实战的两个典型案例。

* 某知名AI类应用产品漏洞

这个项目是某知名AI类应用产品（1w+收藏)，我们的AI自动化漏洞检测工具发现其存在xxe漏洞 (可通过注入恶意的xml格式数据从而进行攻击)。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP67DdYM3kGibMC1IOvtpZVaUgp8mb8I5TYTJ2ogur4tlm4cvTBibsxwH9IbCwHSia3jDgGicE26fZ4iauw/640?wx_fmt=png&from=appmsg)

图7 大模型针对某知名AI类应用产品0day漏洞的分析结果

我们针对该开源项目的漏洞特性，进行无害化漏洞验证, 发现互联网上有数台与该漏洞相关的运行中设备。这批设备正遭受着高危安全风险威胁。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP7x9SBph8xZ8EoEWdFyjGADTQonnEd1CzFB7rnicPqkDFJH4dzCicBWIm1cjNeJ7cZBQEIFpbMdvr7Q/640?wx_fmt=png&from=appmsg)

图8 当前互联网上正遭受该0day漏洞威胁的设备列表

也就是说，此时此刻如果是黑客拿到了这个0day漏洞，只需短短几秒钟，大批量设备的服务器权限就会被黑客攻破，直接造成入侵事件。

* 某知名工具类产品漏洞

经验证，这个项目是某知名工具类产品，在GitHub社区有4w+的收藏量。我们通过AI自动化漏洞检测工具，发现该项目存在可回显SSRF漏洞。只要输入恶意地址，把含有漏洞的机器将作为跳板，就可以直接攻击内网主机，最终获取内部系统的资源信息、本地文件等一系列敏感文件。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP67DdYM3kGibMC1IOvtpZVaUvHtuOEFO1Toibw6LJqOxbchez2at3KG9nnoetvH6wynxLjag4g1ic2Ow/640?wx_fmt=png&from=appmsg)

图9 大模型针对某知名工具类产品0day漏洞的分析结果

如下图所示，针对该漏洞，我们进行了一次“敏感文件窃取”模拟实验。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP67DdYM3kGibMC1IOvtpZVaUkf9gibrHJ6oHLuUbkwTcLjJ8DUDZP0XaRdIcWCBmPFnictB6ibTjE5XhQ/640?wx_fmt=png&from=appmsg)

图10 针对某知名工具类产品0day漏洞的攻击手法演示

具体攻击手法如下：

(1)某使用了该开源项目的文档在线转换工具平台的正常服务模式如下：用户可通过提交一个互联网链接至该平台，该平台根据用户提供的链接去抓取对应网页内容，并将内容转换为文档格式后，提供给用户下载；

(2)假如该平台背后的主机同时在本地存放了一些敏感文件，且可在平台的内网通过内网网址访问对应文件信息；

(3)黑客通过某些手段探测到这些敏感文件的内网地址后，通过在该平台输入对应内网链接 ，引导漏洞主机对该链接进行请求访问，并转换为文档文件供用户下载；

(4)由于对应开源工具的漏洞特性，黑客绕过了网络的限制，成功利用该漏洞作为跳板进行远程窃取；

(5)最终通过下载该文档文件进行透传，成功拿到了这些敏感文件中的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP7x9SBph8xZ8EoEWdFyjGADoQeLgYzkxKvXGSAxtt8YzZrJBA6ibugH9Zx63LiaNrXl8QIRRq6vDGKQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP67DdYM3kGibMC1IOvtpZVaUAI8rZWdu6InJ7V52y2Qnl6FltImT4X63Wiba96xjU0cUxpMjGCHyU6w/640?wx_fmt=png&from=appmsg)

图11 针对某知名工具类产品0day漏洞模拟攻击结果演示

这次实战，成功验证了AI赋能的代码漏洞检测工具在真实复杂代码场景下挖掘漏洞的确可行。

****5. 思考与展望****

本次实战已初步验证AI自动化挖掘0day漏洞可行。但大模型在自动化漏洞挖掘的落地过程中，还有很多问题值得我们深入探索和解决。譬如：

* **Token限制和遍历深度问题**

当前版本设计中，可通过大模型的java语法分析能力有效摘取上下文，从而应对项目级代码漏洞检测对于token数约束的挑战。即便如此，在成熟的java项目体系中，也有不少漏洞具备多文件、多层级函数调用的特点。由于token数约束问题始终客观存在，导致该工具只能在有限的深度阈值内进行漏洞检测，从而可能遗漏部分高价值的漏洞。

* **大模型普遍存在的幻觉问题**

大模型的泛化能力带来了发现未知组件漏洞的好处。与此同时，大模型的幻觉问题也会导致误判。比如，将正常的函数调用误认为是漏洞点，加大了漏洞验证的成本。此外，大模型可能输出自我构造的上下文请求，导致语法分析出错，从而导致漏洞报告准确性受影响，进而造成一些误报。

下个版本，我们将持续优化上述问题，提供更丰富的功能，并在更多安全应用场景中推动落地。

欢迎大家在评论中共同探讨这款工具的更多可能性，也希望大家多多关注我们的大模型助力安全系列文章，一起碰撞出更多思想火花，共同提升行业整体安全防护水平。

**深入了解系列文章：**

* [大模型应用实践（一）：AI助力Code Review安全漏洞发现](https://mp.weixin.qq.com/s?__biz=MjM5NzE1NjA0MQ==&mid=2651206699&idx=1&sn=b850cf1e858f00b90a717efd504988dc&scene=21#wechat_redirect)
* [AI助力！明文密码泄漏无处遁形【大模型应用实践系列二】](https://mp.weixin.qq.com/s?__biz=MjM5NzE1NjA0MQ==&mid=2651206718&idx=1&sn=114609415a3520110916d2508151ef8c&scene=21#wechat_redirect)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5asPR2KQZHIkuvt7d85Nic3JIRVcIMoJa1rEqMEkibSkxEptehGiaffy66vGXWxCrJ4ZbPibVYofAkyw/0?wx_fmt=png)

腾讯安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/JMH1pEQ7qP5asPR2KQZHIkuvt7d85Nic3JIRVcIMoJa1rEqMEkibSkxEptehGiaffy66vGXWxCrJ4ZbPibVYofAkyw/0?wx_fmt=png)

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