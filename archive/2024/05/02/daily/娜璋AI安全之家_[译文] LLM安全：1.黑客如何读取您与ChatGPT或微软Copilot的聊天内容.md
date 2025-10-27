---
title: [译文] LLM安全：1.黑客如何读取您与ChatGPT或微软Copilot的聊天内容
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247499808&idx=1&sn=832056ebe104701c4af33442993ef590&chksm=cfcf70edf8b8f9fb1f7e7ebd4e89b8605b0873207934b7d865ea7b0e734da50d4de58dbd4d0c&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2024-05-02
fetch_date: 2025-10-06T17:17:51.354798
---

# [译文] LLM安全：1.黑客如何读取您与ChatGPT或微软Copilot的聊天内容

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRMiadtglfxicnicU3BIttajX4ib9eiajtOaTDeicqZWKK6LJ41jrnfoeQpbP4iaiaZ7v7VNf89OpR7PdYWVaw/0?wx_fmt=jpeg)

# [译文] LLM安全：1.黑客如何读取您与ChatGPT或微软Copilot的聊天内容

原创

eastmount

娜璋AI安全之家

这是作者新开的一个专栏，主要翻译国外知名安全厂商的技术报告和安全技术，了解它们的前沿技术，学习它们威胁溯源和恶意代码分析的方法，希望对您有所帮助。当然，由于作者英语有限，会借助LLM进行校验和润色，最终结合自己的安全经验完成，还请包涵！

这篇文章将讲解黑客如何利用聊天机器人的功能来恢复OpenAI ChatGPT、Microsoft Copilot和大多数AI聊天机器人的加密聊天记录。该文章来源自以色列Offensive AI Lab的研究人员发表的一篇论文，其描述了一种恢复被截获的AI聊天机器人消息文本的方法。现在，我们将探讨这种攻击是如何工作的，以及它在现实中具有多大的危险性。基础性技术文章，希望您喜欢！

**文章目录：**

* 一.从拦截的AI聊天机器人信息中可以提取哪些信息?
* 二.使用提取的信息来恢复信息文本
* 三.我们应该担心吗？

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMiadtglfxicnicU3BIttajX4ibHL4k6Q4OUVxiccthRYaehEuU7Dpcl2uJ3PibD7XV8DtlDqeDes9ypDrQ/640?wx_fmt=png&from=appmsg)

```
原文标题：《How hackers can read your chats with ChatGPT or Microsoft Copilot》 原文链接：https://www.kaspersky.com/blog/ai-chatbot-side-channel-attack/51064/ 文章作者：Alanna Titterington 发布时间：2024年4月24日 文章来源：https://www.kaspersky.com
```

---

# 一.从拦截的AI聊天机器人信息中可以提取哪些信息?

通常而言，聊天机器人会以加密形式发送消息。然而，`大型语言模型（large language models，LLMs）` 及其上构建的聊天机器人包含了一些严重削弱加密的特性。结合这些特性，当从泄露的信息片段中恢复消息内容时，就有可能造成侧信道攻击。

为了理解这种攻击过程中发生了什么，我们需要深入了解LLM（大型语言模型）和聊天机器人的工作机制。首先，我们需要知道，LLM并不是直接操作单个字符或单词，而是操作tokens，这些tokens可以被描述为文本的语义单元。OpenAI网站上的Tokenizer页面为我们提供了内部工作原理的描述。

下图演示了消息tokenization如何与GPT-3.5和GPT-4模型一起工作的。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMiadtglfxicnicU3BIttajX4ibZZkgogt6FhKzErhFpHUibfTsIvYicjMkbeSAT2wqprzWS5ChXicoOourw/640?wx_fmt=png&from=appmsg)

如果您曾与AI聊天机器人有过交互，您就会知道促成这种攻击的第二个特点：

* 它们不会一次性发送大量响应，而是逐渐发送——几乎就像人在打字一样。

但与人类不同的是，LLMs以tokens为单位进行书写，而不是单个字符。因此，聊天机器人会一个接一个地实时发送生成的tokens。或者更确切地说，大多数聊天机器人都是这样做的，除了Google Gemini，这使得它不受这种攻击的影响。

第三个特点是：

* 在论文发表时，大多数聊天机器人在加密消息之前并未使用压缩（compression）、编码（encoding）或填充（padding），其中填充是指向有意义的文本追加垃圾数据，以降低可预测性并增加加密强度。

综上，侧信道攻击利用了这三个特性。虽然截获的聊天机器人消息无法解密，但攻击者可以从中提取有用的数据——特别是聊天机器人发送的每个token的长度。其结果类似于一个“幸运之轮”的谜题：

* 您无法看到具体加密的具体内容，但各个tokens（非words）的长度会被揭示出来。

虽然无法解密消息，但攻击者可以提取聊天机器人发送的tokens长度，由此产生的序列类似于“幸运之轮”节目中隐藏的短语。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMiadtglfxicnicU3BIttajX4ibgqY4OkgricpFh9JaWLFLniabKrflDYib6TdADYxEqdtw2BlzChxcuAr9g/640?wx_fmt=png&from=appmsg)

---

# 二.使用提取的信息来恢复信息文本

接下来要做的就是猜测这些tokens背后隐藏着什么单词或信息。您可能永远猜不到谁擅长这种猜测游戏：没错——就是LLMs（大型语言模型）。事实上，这是它们的主要使命：在给定的上下文中猜测正确的单词。因此，为了从生成的token长度序列中恢复原始消息的文本，研究人员求助于LLM…

确切地说是两个LLMs（大型语言模型），因为研究人员观察到与聊天机器人的初始交流几乎总是公式化的，因此，很容易被一个模型根据流行语言模型生成的一系列介绍性信息通过专门训练而猜出来。

* 第一个模型用于恢复介绍性消息并将其传递给第二个模型
* 第二个模型处理对话的其余部分

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMiadtglfxicnicU3BIttajX4ibULgaszIQicFDGAsDgKkictibvN91OeS37lvNgn2XHpibKC0QjY2YqHt8iaQ/640?wx_fmt=png&from=appmsg)

这将生成一个文本，其中tokens长度与原始消息中的长度相对应。但是，具体的单词通过暴力破解的方式，取得了不同程度的成功。请注意，恢复的消息与原始消息之间的完美匹配是很罕见的——通常会发生文本的一部分被错误猜测的情况。有时结果是可以接受的，在下图的示例中，文本被恢复得非常接近原文。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMiadtglfxicnicU3BIttajX4ibiaPHKVU3GCdmAUia1GrZr0Mzib0G1SJzsiaYyNvpuvzZYiap8G6YYm7UoeA/640?wx_fmt=png&from=appmsg)

但在不成功的情况下，重构的文本可能与原始文本几乎没有共同点，甚至完全不一样。例如，结果可能如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMiadtglfxicnicU3BIttajX4ibjrbjxAKZTVrdGn6LBoFYOBoSEPQfGrUJtvtSHIRjEibLhrXgCOov1jg/640?wx_fmt=png&from=appmsg)

甚至是这样：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMiadtglfxicnicU3BIttajX4ibJH1SxCfib00lluGYmDVnqrqMvwOddBVQrfyiaibpBHOKNoXvybNABxh2w/640?wx_fmt=png&from=appmsg)

总的来说，研究人员检查了十多个AI聊天机器人，并发现其中大多数都容易受到这种攻击——例外的是Google Gemini（原名Bard）和GitHub Copilot（不要与Microsoft Copilot混淆）。如论文中的下表所示。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMiadtglfxicnicU3BIttajX4ib2veOkPoPheye0y1mAtqwRTu2VXYZR3UibFfQdj2NINtOvwUE6I8BZCA/640?wx_fmt=png&from=appmsg)

---

# 三.我们应该担心吗？

值得注意的是，这种攻击是具有追溯性的（retrospective）。假设有人不费苦心地拦截并保存了您与ChatGPT的聊天记录（虽然不容易，但有可能），在这些记录中您透露了一些可怕的秘密。在这种情况下，使用上述方法，那个人理论上将能够读取这些消息。

值得庆幸的是，拦截者的成功率并不高。正如研究人员所指出的那样，即使是聊天的一般主题也只有55%的几率被确定。至于成功的重建，这个比例仅为29%。值得一提的是，研究人员对完全成功重建的标准得到了满足，例如：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMiadtglfxicnicU3BIttajX4ibiaq4WibN7GnL52TGcqu3rRic4zNkkuXZunwjb13XiazFNtfmzaeoWFwCmQ/640?wx_fmt=png&from=appmsg)

那么，这种语义上的细微差别的重要性如何呢？这完全由您自己决定。但请注意，这种方法很可能无法以任何程度的可靠性提取实际细节（如姓名、数值、日期、地址、联系方式、其他重要信息）。

此外，这种攻击还有一个研究人员未提及的限制：文本恢复的成功与否在很大程度上取决于被拦截消息所使用的语言，tokenization的成功在不同语言之间差异很大。本文主要关注英语，其特点是tokens非常长，通常相当于一个完整的单词。因此，经过token处理的英文文本显示了不同的模式，从而使得重构（reconstruction）相对简单。

注意，其他语言都无法比拟。即使是那些与英语最为接近的日耳曼语系和罗曼语系的语言，其平均token长度也只比英语短1.5-2倍；而对于俄语，更是达到2.5倍，一个典型的俄语token通常只有几个字符长，这将可能使这种攻击的有效性降至零。

至少有两家AI聊天机器人的开发者已经针对这篇论文做出了反应。

* Cloudflare
* OpenAI

他们添加了上述提到的填充方法，该方法就是专门为了应对这种类型的威胁而设计的。其他AI聊天机器人开发者也将效仿，希望未来与聊天机器人的通信能够得到保护，免受此类攻击的威胁。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMiadtglfxicnicU3BIttajX4iblv8H5FerSibxHQic90t0BUEQHd5NTJiajQNqSThYp3wse2BLYUMWdoqcw/640?wx_fmt=png&from=appmsg)

> 2024年4月28日是Eastmount的安全星球——『网络攻防和AI安全之家』正式创建和运营的日子，该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMiadtglfxicnicU3BIttajX4ibY9pFnHyOBVicOpLQ3c9mEXiaLywr8aNnSYtgX3pUkVbQ1mLTGgdtXpNw/640?wx_fmt=png&from=appmsg)
> 目前收到了很多博友、朋友和老师的支持和点赞，尤其是一些看了我文章多年的老粉，购买来感谢，真的很感动，类目。未来，我将分享更多高质量文章，更多安全干货，真心帮助到大家。虽然起步晚，但贵在坚持，像十多年如一日的博客分享那样，脚踏实地，只争朝夕。继续加油，再次感谢！

(By:Eastmount 2024-04-30 星期二 夜于贵阳)

---

**前文分享：**

* [[译] APT分析报告：01.Linux系统下针对性的APT攻击概述](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247484510&idx=1&sn=bb905adaec7f2beb5d6e65073137d070&chksm=cfccb493f8bb3d851e1978945a9d0920db09a209b1a3ad79d4811ed6fff41615c2d618d3db82&scene=21#wechat_redirect)
* [[译] APT分析报告：02.钓鱼邮件网址混淆URL逃避检测](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247484704&idx=1&sn=9c23f87a8dd2293a1e6db552ffd79191&chksm=cfccb5edf8bb3cfb69baa3a0a1edee09c39597eb242aa184992eef7648c70f6950aae6edeccb&scene=21#wechat_redirect)
* [[译] APT分析报告：03.OpBlueRaven揭露APT组织Fin7/Carbanak（上）Tirion恶意软件](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247484887&idx=1&sn=c2fac30b17dad389d611f48f36b63f2e&chksm=cfccb51af8bb3c0c2d357c1c184050ba92c7a57255c8da7bbfdbe86da2b8cf3f9fe47aeee8bf&scene=21#wechat_redirect)
* [[译] APT分析报告：04.Kraken - 新型无文件APT攻击利用Windows错误报告服务逃避检测](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247484980&idx=1&sn=3d6d0350a52cf49e912804c5ae83c95f&chksm=cfccb6f9f8bb3fef985fd47f6a0933a6dd18cf8f7878500416c64bc91740e00a78f354c8bdd8&scene=21#wechat_redirect)
* [[译] APT分析报告：05.Turla新型水坑攻击后门（NetFlash和PyFlash）](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247485103&idx=1&sn=d87673fb158d8ab750ddd925f75514d2&chksm=cfccb662f8bb3f74b3a619b9b2f27f816a32644670b09634c665ca4ded7083f6330e6bf1e182&scene=21#wechat_redirect)
* [[译] APT分析报告：06.猖獗的小猫——针对伊朗的APT攻击活动详解](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247485292&idx=1&sn=05c27cba3c684bc09c2c097dc94a58ec&chksm=cfccb7a1f8bb3eb7523139c069e590a3bfac50e456e2a94275435820d7f0fbbefcc556e01848&scene=21#wechat_redirect)
* [[译] APT分析报告：07.拉撒路（Lazarus）使用的两款恶意软件分析](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247485491&idx=1&sn=1216d7479da158d125becf5d4a9f5780&chksm=cfccb8fef8bb31e8e36d0f0178bf1d585b9f1074ab5c12d0b301397b5de7798e73ce01592fa8&scene=21#wechat_redirect)
* [[译] APT分析报告：08.伊朗APT34更新武器库——SideTwist变体](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247490195&idx=1&sn=da969e229f1ab77430069aafffcded56&chksm=cfccaa5ef8bb2348d7ef3fdfa8aa163560a734f93f6ea662a3465efdc53bc9281f2ee54c3a3e&scene=21#wechat_redirect)
* [[译] APT分析报告：09.漏洞利用图谱–通过查找作者的指纹来寻找漏洞](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247490496&idx=1&sn=018df4a794ebd2553a15e771e077ce62&chksm=cfccab0df8bb221bf3860f056c85f6f5fc8820d5f77458e9c0f0692077cb77024fe9d0134a5c&scene=21#wechat_redirect)
* [[译] 威胁分析报告：10.Lazarus以ThreatNeedle家族攻击工业（BMP图片隐藏RAT）](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247490848&idx=1&sn=a56522c1b9b253d9d8824d2fd4b07e56&chksm=cfccadedf8bb24fbfbefdc1ef8f59b3be0d98e8536287b41af5d0d1f03935e44fae987d23b34&scene=21#wechat_redirect)
* [[译] 威胁分析报告：11.深入了解Zebrocy的Dropper文档（APT28）](http://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247491265&idx=1&...