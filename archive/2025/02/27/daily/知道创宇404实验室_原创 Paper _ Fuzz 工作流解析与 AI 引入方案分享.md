---
title: 原创 Paper | Fuzz 工作流解析与 AI 引入方案分享
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650990726&idx=1&sn=913908848fcb7e37ee2cab40e68dcadc&chksm=8079aab4b70e23a20f1d54c8fb5d708496850de1744d3e77dc8fe1d3f619204ae42add2485f0&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2025-02-27
fetch_date: 2025-10-06T20:36:23.852716
---

# 原创 Paper | Fuzz 工作流解析与 AI 引入方案分享

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT1Ah3cfAIo4tOmCosx1upEWjF967mJCk9r27gtR6R9sVFMVHWDbcVYvEBpBMWkbxLRFOWQ2j2O36g/0?wx_fmt=jpeg)

# 原创 Paper | Fuzz 工作流解析与 AI 引入方案分享

原创

404实验室

知道创宇404实验室

**作******者：ghost461@********知道创宇404实验室****

**时间：**2025年2月26日****

****本文为知道创宇404实验室内部分享沙龙“404 Open Day”的议题内容，作为目前团队AI安全研究系列的一部分，分享出来与大家一同交流学习。****

**1.概述**

参考资料

本文受 Google 安全博客的《Leveling Up Fuzzing: Finding more vulnerabilities with AI》启发，结合自己对 Fuzz 工程的理解，解析自动化漏洞挖掘的工作流并分析 AI 如何帮助我们改进现有的体系。

**2. 认识Fuzz工作流**

参考资料

简单来讲，理想状态的模糊测试从生成畸形数据开始，通过接口输入目标程序，当程序运行发生崩溃后，分析程序 bug 并确认漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1Ah3cfAIo4tOmCosx1upEWW0BbkgetAJydLKxKCiaWIgU0iaAuWVPVlGX7gvu4IOLicSoKF9oAEtNHA/640?wx_fmt=png&from=appmsg)

但Fuzz是一个系统性的工作流程，为了实现这一流程，我们需要为这个流程图添加一点细节，包括数据收集、接口分析、反馈数据收集等操作，以此来构建完整的模糊测试循环。![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1Ah3cfAIo4tOmCosx1upEWJ9csOs4AOhVE6xss3Hibunuf2Ya1zLtcmiaU2SzFZDbWbZlvszpbMP8Q/640?wx_fmt=png&from=appmsg)

**3. 目标设定与切入点讨论**

参考资料

**3.1 Google白盒Fuzz方案**

在 Google oss-fuzz 团队设计的白盒 Fuzz 改进方案中，为 AI 的引入设计了以下5个功能目标：

1. 起草初步的模糊目标。
2. 修复出现的任何编译问题。
3. 运行模糊测试目标来查看其执行情况，并修复任何导致运行时问题的明显错误。
4. 运行更正后的 fuzz 目标更长时间，并对任何崩溃进行分类以确定根本原因。
5. 修复漏洞。

在阅读谷歌安全博客的这一篇文章之后，个人对此产生了以下看法：

1. 数据上，白盒 Fuzz 中 AI 可以获得良好的文档与代码信息。
2. 应用上，通过提示词工程就可以达到一定的效果。
3. 几项功能目标是比较割裂的，但可以通过工作流编程将它们串联起来。
4. 对 Fuzz 测试的前中后期规划都有涉及，可以参考。

而且，黑盒条件下的漏洞挖掘，是 Fuzz 相较于代码审计更受欢迎的场景。

### **3.2 引入AI之前**

在正式开始之前，我们有几个比较泛化的问题需要思考。

首先，AI 的出现将如何改善我们的工作流程？

1. 简单的任务，减少人工；
2. 现有的方案，做出选择；
3. 复杂的问题，给出建议。

同时，在将 AI 引入工作流时，需要搞清楚：

1. 给AI的数据从哪来，从 AI 获取的返回数据是什么样的？
2. 哪些问题通过提示词就可以解决，哪些又需要用到补充知识库进行 RAG 或微调？

还有一个问题在于，尽管当下的大语言模型 AI 体现出了庞大的知识储备与一定的逻辑推理能力，但上下文限制与幻觉问题仍是无法解决的，这使得 AI 在工作流中无法成为程序意义上的“稳定输出”。此外，私有化部署、算力限制也是我们不得不考虑的因素。

1. 是否需要构建特定的沙盒环境，使 AI 具备操作代码执行的能力，将其转换为稳定的信息输出？
2. 是否有必要进行私有化环境部署，设计的需求需要多大的算力支持？

### **3.3 分阶段讨论**

接下来我们就开始讨论在黑盒条件下，不同的几个Fuzz环节上引入AI的一些实施需求：![all.png](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1Ah3cfAIo4tOmCosx1upEWa5lAkUXwCK50Ae0qciaicndlNWt7pNgRicYHHEqHhazZuYXk9DtAMaib5A/640?wx_fmt=png&from=appmsg)信息收集阶段：![info.png](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1Ah3cfAIo4tOmCosx1upEWdATrNH5kMEM0AEG9jebgSrTAWwLZ7oqicVCMRcvBhWGic8YClEsiaY2uQ/640?wx_fmt=png&from=appmsg)语料库准备阶段：![corpus.png](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1Ah3cfAIo4tOmCosx1upEWGiaTeKrcBnwCBCyLPYibyEJuVhT0bLQsTG4Y7G1GGreU4svq19I0C0icQ/640?wx_fmt=png&from=appmsg)接口分析阶段：![inter.png](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1Ah3cfAIo4tOmCosx1upEWa22rW9tbHxo9Uo5tZSU9YkZibV67Mtpc5kdSYbNHLDZE8WrcRyOXicnQ/640?wx_fmt=png&from=appmsg)变异算法与插桩方案：![mut.png](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT1Ah3cfAIo4tOmCosx1upEWo1QQbF5iaquQLWSYJc5Nf2NjmXYIa5FrhJnH0iaqibMZvZTzbwe5TUN2w/640?wx_fmt=png&from=appmsg)

细心的读者可能已经注意到了，在工作流的不同阶段，使用了不同颜色的圆圈标识，分别是：

* 红色，代表高频，几乎每个 Fuzz 任务都需要人工操作的部分；
* 黄色，代表中频，遇到特殊类型的 Fuzz 目标时需要人工设计/修改的部分；
* 绿色，代表低频，工具方案已经较为成熟，是需要对现有 Fuzz 体系进行开发优化时才会触及到的部分；

总体上我们是按照之前一节中提到的，“简单任务自动化，现有方案做选择”来设计，但Fuzz过程中如何优化以及漏洞分析与修复，是比较复杂的问题，仍然需要研究员与AI进行交互，针对目标找出可行的方案。

**4. 初步引入方案分享**

参考资料

“帮我 Fuzz 一下这个目标。” --- 这句话背后意味着什么？

这里视频展示的是去年使用 Dify 框架搭配一个修改过后的沙盒环境，初步实现的一个 Fuzz 自动化构建的示例。

* 以某路由器固件为目标，工作流将上传的固件进行解包并交由 AI 判定其文件类型；
* 根据提示词工程，AI 已经被设定具备特定目标的 Agent，并在任务对话中展现出目的性，并持续引导用户完成必要信息的完善；
* 在我们配置过的沙盒环境下，利用 AI 的 python 编程能力，进行固件分析、AFL++工具编译、tmux 会话管理等程序化的工作，最终完成Fuzz任务的构建；

这里比较有意思的点在于，

1. 沙盒是运行在x86\_64架构的服务器中的，而目标固件程序为 ARM 架构，AI 成功的识别出目标架构后，正确使用 python 脚本执行了 AFL++ qemu 模式的编译流程；
2. 目标程序是一个 json 解析器，这种常见格式的文本完全可以由 AI 生成语料，不过还有一个语料的获取方式是，该解析器程序的 usage 信息中包含一段示例 json，同样可以被 AI 获取并用作 Fuzz 测试语料；
3. 与代码审计工具不同，Fuzz 任务并不是一次性扫描执行的，它需要在后台运行较长时间，所以我通过提示词让 AI 将 Fuzz 任务放在 tmux 终端会话中进行管理，后续 AI 也能够生成正确的 tmux 指令来完成我查看运行中的 Fuzz 任务的需求；

**5. 总结**

参考资料

Fuzz与AI设施都需要改进以加强相互配合。

在AI建设方面，细化Fuzz工作流中的需求，分别编写对应的提示词，以及维护对应的知识库。

* 分析目标程序接口；
* 构建Fuzz环境；
* Fuzz过程中的介入式任务，比如评估进度，或生成新数据；
* 自动分析/分类Fuzz出的bug；
* ...

Fuzz程序这边，根据AI融入的思路，优化改造Fuzz组件。

* 实现较通用的黑盒虚拟化的执行环境；
* 根据Fuzz情况，摘要当前语料输入LLM并生成新的语料数据；
* 实现能够在Fuzz运行过程中进行语料队列操作的选择器；
* ...

在漏洞挖掘自动化的发展路线上，AI 的引入虽然仍有很多大大小小的问题，但总体上是具备可行性和建设性的。个人的一点感受是，不必局限于热门的某一项技术，还是要客观的看待与评估自己当前的工作流程，接纳并利用新兴技术融入旧的工作体系才是发展的常态。

**6.参考链接**

参考资料

###

[1] Google Security Blog -《Leveling Up Fuzzing: Finding more vulnerabilities with AI》
https://security.googleblog.com/2024/11/leveling-up-fuzzing-finding-more.html

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT0mSRTxbY7fsoLUFViaxk1nhQByibgTdbwbMqNibWMKbHKrjwUUY8GNZlAoUlcic5ibVhyCebVwoNialnow/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "404 logo-b04.png")

**作者名片**

![](https://mmbiz.qpic.cn/mmbiz_png/3k9IT3oQhT3DQfAiau7swdRNNK9RfoQ2feDxoZr6NxSEic3e69ORAd6OY4Gh4lEz9Co9kf9AXRdCxe3AWRfVBhjA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/3k9IT3oQhT0Z79Hq9GCticVica4ufkjk5xiarRicG97E3oEcibNSrgdGSsdicWibkc8ycazhQiaA81j3o0cvzR5x4kRIcQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**往 期 热 门**

(点击图片跳转）

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3udhFEVY5myKLk0Cn2uzqIA322sLfHF7EVS80etYG2XUTwOoFyWYXd5z316xVzRibsiaSmgEibMLQQw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650990710&idx=1&sn=771c2f44aef4cf2cbaf48f7078f99fc2&scene=21#wechat_redirect)[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0dEG2QiabTxP29gvGmSS9jelZmyJgF1rHxGzAh7mNsKXa5xYRjgdPZtgs4fok9iatYM1eAO8nRohTQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650990698&idx=1&sn=9c120d2f2a1822e13abc8143a6b07f38&scene=21#wechat_redirect)[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT2IVxDPAj0QTqQWfriaMBxkficARkTibiaWYic424464jCEETCicTslPicz0rJ4xfFLTzt4CLFJ5UQhbBdYQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650990663&idx=1&sn=d3612bcdf320efdc783e5740d519c69d&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/3k9IT3oQhT3XlD8Odz1EaR5icjZWy3jb8ZZPdfjQiakDHOiclbpjhvaR2icn265LYMpu3CmR1GoX707tWhAVsMJrrQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

戳“阅读原文”更多精彩内容!

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3iahqCkYYjmw1gI9aGgwgAAqbmakWhGyibh4nQyU7npz3YyfZqosFKqfjdkRFRUwhmUwarcpQRrp0w/0?wx_fmt=png)

知道创宇404实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3iahqCkYYjmw1gI9aGgwgAAqbmakWhGyibh4nQyU7npz3YyfZqosFKqfjdkRFRUwhmUwarcpQRrp0w/0?wx_fmt=png)

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