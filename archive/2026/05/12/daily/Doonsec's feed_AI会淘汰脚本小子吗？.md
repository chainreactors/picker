---
title: AI会淘汰脚本小子吗？
url: https://mp.weixin.qq.com/s/55zrGjeUb04c5xDnctIN9Q
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:44:34.991246
---

# AI会淘汰脚本小子吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AjSHgfLXVrp1ZofkUZlQflTK6X3YbdfnoLr8fQvzhMHsoTNBqY0sRlM07wiaTsjke8jJibZc3BibMjQ0ONDaITyqByHjqNtic2iarBeFZPeur59A/0?wx_fmt=jpeg)

# AI会淘汰脚本小子吗？

红客攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AjSHgfLXVrrWXy5YZFpKkjSMWic7clTqhfEYFZHmNW9fZfKo9cez3jR4icSiciaqIFq2pcs1iaAkszb4v4Yg1xhKibQwv1urxU9F8yV1xZDWe2UEA/640?wx_fmt=jpeg)

早高峰的地铁挤得像沙丁鱼罐头，你一手抓着吊环，一手机械地刷着手机。突然，技术群里弹出一条消息：某AI安全助手3秒完成渗透测试报告，准确率高达97%。

你盯着屏幕，手指停在半空，差点被身后的大哥撞个踉跄。

不是吧？我学了三年才搞懂的报错注入，AI三秒就搞定了？我熬了无数个夜背下来的Payload库，AI直接生成了？那我这些年算什么？算我热爱学习吗？

**这种焦虑，正在网络安全圈子里疯狂蔓延。**

脚本小子（Script Kiddie）这个词，曾经是行业里略带嘲讽的标签——指那些只会用现成工具、不懂底层原理的"半吊子"安全从业者。但现在，连这个标签都变得暧昧起来：**当AI比脚本小子更会用脚本，脚本小子还有存在的必要吗？**

今天这篇文章，我们不贩卖焦虑，只聊真相。

**1**

**脚本小子画像：我们到底在讨论谁？**

在深入讨论之前，先明确一下概念。所谓"脚本小子"，在本文的语境下，指的是这样一群人：

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrrnxbunDDImzRnBfCR2V8X9OIhickIU1xR0me7mW4Jf8Q2uSNh1Z6FNy4ENrBLMBdSaTRqaVCOAZpzfa8h4aO80iagooytxER2A4/640?wx_fmt=png)

**坦白说，这个角色在整个安全产业链中，占据了相当大的比例。**

从企业的安全服务团队，到甲方的安全运营中心，再到各种SRC平台的活跃白帽——脚本小子不是少数派，而是中坚力量。他们撑起了渗透测试、漏洞扫描、安全评估等大量的基础工作。

**但问题是：这些工作，AI正在以肉眼可见的速度蚕食。**

**2**

**AI的进攻：从辅助到替代的三重奏**

让我们直面现实——AI对脚本小子的冲击，不是未来时，而是进行时。

**第一重**

**工具层面的降维打击**

还记得你第一次用SQLMap的喜悦吗？输入一条命令，看着它自动跑出数据库名，那种"我掌握了黑科技"的成就感？

**现在，AI连这条命令都不用你输入了。**

你只需要说："帮我检测这个目标有没有SQL注入"，AI就能自动完成：

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrrL8LYgz30ncByJbfkDXliaGSgj7stgLGgBO91V73z6nibwsVSrbY60mlee0e21ZrXC5L3QVnxrBk9iaJfIhVqsSawRZomQGw8Yibw/640?wx_fmt=png)

而你呢？你可能还在回忆SQLMap的--tamper参数到底怎么拼。

**第二重**

**知识层面的记忆碾压**

脚本小子的另一个痛点是：安全知识太庞杂了。

各种绕过技巧、WAF规则、编码方式、中间件漏洞、框架特性……人的大脑容量是有限的，记住这个就会忘掉那个。所以脚本小子们都有一个庞大的笔记库，遇到情况就翻笔记、搜Google。

**AI没有这个问题。**

它的"记忆"是无限的，而且检索速度是毫秒级。你想知道某款WAF的绕过方式？它不仅能告诉你，还能根据最新的规则动态调整建议。你想了解某个CVE的细节？它能立刻给出利用条件和修复方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrqcjoC5n4IjMQz3a7TNKXlGFMlwputlV3JRNPd5J4pZiavia0yUZBbpsoHqUxNHbBwSibuHUBLWOdqdz5qlC8EhUqeG5FpTal9K3c/640?wx_fmt=png)

**第三重**

**效率层面的数量碾压**

这是最要命的。

假设你是一个企业安全团队的成员，老板让你在一周内完成100个Web应用的渗透测试。作为人类脚本小子，你加班加点，每天工作12小时，终于踩着Deadline交了报告。

**而AI呢？它可能只需要一个下午。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrqKwI3HTdicgv2VsRbChdlgiaGxsg78CibfXlib12ZoeUWYnZCwiaP2ZJpnMBGN5E9mfxuwvR5Aib4krz3U2vjwJqVUsY8BHtyvgM11c/640?wx_fmt=png)

当你的老板看到这个对比，你觉得他会怎么选？

**3**

**脚本小子的困境：我们真的在原地踏步**

聊到这里，有些读者可能会不服气："我这些年也学了不少东西，不只是会用工具而已！"

好，那我们来做几道灵魂拷问：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrqrtTKAgtibLL6A4jFdkABcicySHu7wZ85CbmeLG6dcOVrGF1SNSRdvkCdia0vYvzSwPDmzUMYj1wVnwutfFzz9RNTlbGls0chOow/640?wx_fmt=png)

如果这三道题让你有点心虚，那说明我们得承认一个事实：

**很多脚本小子的"经验"，本质上是一种对工具的熟练度和对常见模式的记忆。而这，恰恰是AI最擅长取代的东西。**

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVro9SQG3zliaqQpy5Ut5yyuVbMicibTlCXhFSM7V11NYuTAnscf0MChia4NebaeNU3gGUqia8icOH4epJ5M446zConekZ5V7X9V8HDiatk/640?wx_fmt=png)

但问题是——如果你的技术能力只停留在"跑工具看结果"的层面，这些软技能你又有多少机会去锻炼和提升？

**4**

**历史回顾：工具的演进从未停止**

其实，这不是安全行业第一次面临工具革新带来的焦虑。

让我们简单回顾一下安全工具的演进史：

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrq8yl3cLC9dK6TAoXVPpxGYSspyCpUcMJha7TARbVFBj2OnibrfaDJJUfOvGSnp7pk5ia0PspWVQndbHKtf9g2K3FLC684sKLTbY/640?wx_fmt=png)

**看到了吗？每一次工具的进步，都伴随着角色定位的重塑。**

当年从手工时代过渡到工具时代的时候，老一辈的安全从业者也有过类似的焦虑："这些年轻人只会用工具，根本不懂原理！"但后来呢？工具成了标配，懂原理的人依然吃香，不懂原理只懂工具的人成了"脚本小子"。

历史总是惊人的相似。今天的AI，就像当年的SQLMap和Metasploit——它会让一部分人失业，但也会让另一部分人起飞。

**5**

**数据说话：AI安全工具的崛起**

光说理论不够，我们来看一些行业数据。

根据各大招聘平台的趋势分析和安全厂商的调研报告，过去几年安全行业对不同技能的需求发生了显著变化：

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrp3ClDNNsO3NLmq2ZPmHTjPXxB13jTDs7p7Zou5rN1kqBRHIrmhXQNgFicayXT9MYicpmBqcswkPjgXQ0JXm4d8Jc8XjxibzvpN2w/640?wx_fmt=png)

这些数字背后，是整个行业对安全从业者能力模型的重新定义。

**6**

**转机：AI淘汰的是"脚本"，不是"人"**

好了，焦虑贩卖得差不多了，我们来聊聊希望。

AI真正要淘汰的，是"只会机械执行"的工作方式，而不是"做安全的人"。

换个角度想：AI让工具的使用门槛大幅降低，这反而给了脚本小子们一次"升级"的机会。

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrqBydaoCgjX5N9q223SgkQ4grgMkODUBDhRzq4SxL514jFpj4Uv5LuURNogZ71C7yNKL7BNiatFLfBozcgg0tA1ia2OrD7JHxhbQ/640?wx_fmt=png)

**这不是空话，这是正在发生的事情。**

那些最早拥抱AI的安全从业者，现在已经能把AI当成"外挂"了：

* 让AI写自动化扫描脚本，自己专注分析结果
* 让AI生成Payload变体，自己负责验证和调优
* 让AI处理常规报告，自己处理疑难杂症

**他们的效率提升了3倍、5倍，甚至10倍。他们没有被淘汰，他们正在淘汰那些拒绝改变的人。**

**7**

**不同岗位的差异化生存策略**

到这里，你可能想问：道理我都懂，但我具体该怎么做？

答案是：**取决于你现在的位置。**

不同的安全岗位，面对AI冲击的应对策略是不一样的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrrculGdq7oRMRkugStGQOVuibhLvmKttkRvQUNibbibBibibdBctcuPJKO16Z9rtibBGib5JhjFNuDaJ26PYNq9lGV3jwl05HE1rttZQ4/640?wx_fmt=png)

**关键认知：AI不是来抢饭碗的，它是来重新定义"什么是好饭"的。**

**8**

**给脚本小子的三条自救建议**

如果你看完前面的内容，觉得"被点名了"，那这三条建议请务必认真看完。

📌**建议一：逼自己写一次Exploit**

不是用Metasploit加载模块，是从零开始，根据漏洞原理，自己写一个。

找一个经典的漏洞（比如Struts2的某个CVE），不看现成PoC，自己去分析原理，自己去构造Payload。这个过程会很痛苦，但痛苦之后，你对"漏洞"的理解会上升到另一个维度。

**"当你亲手写过一次OGNL表达式注入，你就再也不会忘记它是怎么工作的。"**

📌**建议二：读源码，读大量的源码**

脚本小子的天花板，在于看不懂代码。而安全人员的天花板，在于能不能从代码里看出问题。

从简单的CMS开始，读PHP、读Java、读Python。看业务逻辑，看权限控制，看输入处理。当你能在脑子里跑通整个数据流，漏洞就无处遁形。

📌 **建议三：拥抱AI，但不要依赖AI**

AI是工具，不是拐杖。

用AI提升效率，但不要丢掉自己的判断力。当AI给你一个结果，你要能判断它对不对、全不全、有没有漏。当你成为"AI的审核者"，你就不再是"脚本小子"了。

**9**

**未来展望：五年后的安全行业会是什么样？**

让我们把视野拉长一点，看看五年后的安全行业可能是什么样子。

🔮**预测一：AI将成为安全团队的"标配员工"**

未来的安全团队架构可能是这样的：

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrpvOAmkek7sRiboqicDpPuQOEyaXId2ozTo1gNsQGd0fJvaoMKJSMyjnusdvbVrvtgiaLH9oLa2TKqy1kH8WQbAiaibprjHssMrU94o/640?wx_fmt=png)

🔮**预测二："提示词工程师"成为安全新工种**

就像当年SQL注入需要特定的Payload构造技巧一样，未来与AI协作也需要特定的"沟通技巧"。

怎么让AI更好地理解你的渗透测试意图？怎么设计Prompt让AI生成更高质量的Payload？怎么验证AI给出的结果？这些都会成为专业技能。

🔮**预测三：攻防对抗进入"AI vs AI"时代**

攻击方用AI生成绕过WAF的Payload，防守方用AI实时分析流量检测攻击。AI之间的博弈会成为常态，而人类的安全专家则负责制定策略、调优模型、处理AI搞不定的边缘情况。

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVronwgSUCibkIibhiaUQWvOzfvibmPZfcCGTL9U5ic65OyskCUdSvHdHfzOege1wPIFATZJV234aXRw7xIB1nRkAySwqJFv8VAPicD38g/640?wx_fmt=png)

END

回到文章开头的问题：**AI会淘汰脚本小子吗？**

答案是：**会，也不会。**

会淘汰那些拒绝学习、拒绝改变、只会机械执行的人。不会淘汰那些持续进化、拥抱变化、愿意深入理解本质的人。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BuYWgUUoia048OgxFibFMSxooCEl4EAhOAqwib1w1GNBM44VEGNC0dILicQ3b3bt3YIOCKfZDH1jG2KiabriaKmybR1ibbKPhBGF5BNxBb2Wx5Iiamg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

红客AI安全实验室资料库，直接扫码即可领取

限时开放，限量100份，先到先得。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AjSHgfLXVrqtjmyPibbNTV9FJia9Z8g2ATjTMelu5ULYYD0sj4Trr0XT3SdClrGY6tjuK6jVVk0ed34VqDBVBv4jgZrpQDZkyLDvOiaE4evjvg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrpux6LeXVcOICicpYylyX3ZjlwjFp2ll3ETGIkbUZGsR07IgaurNDSgicnicZUnicg0h1GOjXKiaJYwYWPZv3lOBWjGxrDFc2BbZrq4/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVroTomzVLxM57ib9U7cIsODHmx0vXe2XPMoWWQibjreDVY76Yl34LVicsKqgbWvVjMEdMWGLg7QMMT7G7CnK6IrNf4JybKcs7Bu2wA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AjSHgfLXVrpovFNWP5WXTo6ZYQ5icM0RO92UjLiaicGf6JUdpfh5VkZkDnficQQE1zKXmF7AvCwIia1aXaAJ1USPPmTlAX1GmetlDYQOdEjd87mc/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/iaPh0yKxE5zleqvXBjCQSwl3YRSgLDiaCJs6thgE7HAEN9bHD2ph3Mg2c349icibwQIyTx6mIvbL2Liatz4PdfGiapVg/0?wx_fmt=png)

红客攻防实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iaPh0yKxE5zleqvXBjCQSwl3YRSgLDiaCJs6thgE7HAEN9bHD2ph3Mg2c349icibwQIyTx6mIvbL2Liatz4PdfGiapVg/0?wx_fmt=png)

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