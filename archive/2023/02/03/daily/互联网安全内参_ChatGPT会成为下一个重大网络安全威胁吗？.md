---
title: ChatGPT会成为下一个重大网络安全威胁吗？
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507682&idx=1&sn=fc7a51554d953932111f30db0a02bd97&chksm=ebfa99c2dc8d10d46ac266985cb29078acd50809b2ab36120a48ecf8489023d4b7e12f7da8f3&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2023-02-03
fetch_date: 2025-10-04T05:35:13.116857
---

# ChatGPT会成为下一个重大网络安全威胁吗？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7sAmVQQC8HeiaEzOAibJEliad0cIx48w0EKmEv06k5cfiaZNujH62qnFP4CvdjsOkgBtf9PKpYp3OUqTQ/0?wx_fmt=jpeg)

# ChatGPT会成为下一个重大网络安全威胁吗？

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7vS26DErGnT6P4KxjbKQRgU6yEXxCkEl1GswhwWS6UHrWibA4eQrG6En7gn8ghL0TNd7qxnW8x67iag/640?wx_fmt=jpeg)

**ChatGPT并不是编写恶意软件的专家，当前铺天盖地的炒作宣传，其实是忽略了编写高质量代码对专业知识提出的严苛要求。**

前情回顾**·AI攻防最前线**

* [ChatGPT首次被黑客用于编写恶意软件](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507536&idx=2&sn=7113556934c1578f541a419fb00b1166&chksm=ebfa9970dc8d10660aac93f29f5cf7da03b1b09e3c53e10c9994d4145f0945d8479037d5eb65&scene=21#wechat_redirect)
* [美国联邦贸易委员会：现阶段AI无法对抗网络虚假信息](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247503598&idx=3&sn=511ab23cc02d06b610986832bc1cfbe9&chksm=ebfa89cedc8d00d80613baa83d46b4b0d2c6146a78a36901690edb4b58d25b41d3ff196b5083&scene=21#wechat_redirect)
* [美情报界AI竞赛：如何用视频环境音识别现实位置](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247492251&idx=3&sn=7cdb74a70ef6254973663b324eae7194&chksm=ebfaa5bbdc8d2cad6064c75b97d64b8d38573e90e5f0a29d317ce4ae3ecfc481bce7bed591fc&scene=21#wechat_redirect)

安全内参2月2日消息，去年11月OpenAI正式发布ChatGPT时，程序员们惊讶地发现，这个AI驱动的聊天机器人不仅能轻松模仿人类语言，甚至可以编写代码。

在发布的几天之后，程序员们贴出了一条条令人瞠目结舌的代码生成示例。从串接云服务到将Python代码移植为Rust，ChatGPT至少在某些基础编程任务上已经表现出非凡的能力。

但**我们也需要擦亮双眼，将围绕ChatGPT掀起的炒作跟真实情况区分开来**。ChatGPT的编程能力先后登上一系列头条新闻，类似“ChatGPT对网络安全的威胁远超大多数人想象”的标题也确实让人心头一紧。不单是普通读者好奇于ChatGPT编写恶意软件的能力，经验丰富的黑客更想检验这个大语言模型到底能在恶意攻击中发挥多大作用。

**实测：**

**ChatGPT缺乏编码专业知识**

Marcus Hutchins（ID为MalwareTech）是一位从黑帽转型为白帽的黑客，曾在2017年因阻止WannaCry勒索软件传播而备受关注。此前曾编写银行木马的他，当然也对ChatGPT究竟有多大本事充满好奇。**聊天机器人真能用来编写恶意软件吗？**

一番尝试之下，结果令人失望。Hutchins在采访中表示，“这十年来，我一直在以合法身份开发恶意软件。我一般要花三个小时才能写出一段功能性代码，而且得用开发效率较高的Python语言。”

经过几个小时的忙碌，Hutchins成功编写出勒索软件程序中的一个组件：文件加密例程。接下来，他尝试让ChatGPT把该组件跟其他必要功能组合成完整的恶意软件，但这位“AI新秀”笨拙地失败了。事实证明，**ChatGPT不光难以把各种组件整合起来，甚至连正确打开文件都很费劲**。

**在这类基本排序问题中的糟糕表现，证明ChatGPT等生成式AI系统仍存在严重缺陷**。尽管它们能够创建出与训练数据极为相似的内容，但大语言模型往往缺乏构成专业知识的纠错工具与上下文知识。人们在惊讶于ChatGPT模仿效果的同时，却经常忽视了它的局限性。

如果大家全盘接受炒作所灌输的观点，那ChatGPT已经几乎无所不能。从文职工作到学术论文、再到专业考试，也包括黑客们擅长的恶意软件开发，这一切都将被ChatGPT所掌控。然而，这种论调其实掩盖了**ChatGPT等工具的核心应用方式——并不是要取代人类专业知识，而是充当高效的AI助手**。

**ChatGPT编码依赖专家指导**

在ChatGPT发布的几周之后，就有多家网络安全公司发布一系列报告，证明该机器人可能被用于编写恶意软件。消息一出，旋即催生了一大堆关于ChatGPT编写“多态恶意软件”的头条新闻。但**这些报告往往掩盖了技术专家在指示模型编写代码，特别是纠正所生成代码结果方面发挥的重要作用**。

去年12月，安全解决方案供应商CheckPoint的研究人员展示了ChatGPT如何从头到尾构建恶意软件——包括编写网络钓鱼电子邮件和恶意代码。然而，要想让它生成功能完备的代码，必须由专业程序员一步步提供引导和提示，例如添加沙箱检测和检查某项功能是否对SQL注入开放。

CheckPoint公司研究员Sergey Shykevich表示，“攻击者必须知道自己想要什么，并指定相应功能。单纯要求其「编写恶意软件代码」并不能生成真正有用的结果。”

对于Hutchins这样的黑客来说，提出正确的问题就是成功的一半。另外，很多将ChatGPT宣传成编程工具的媒体，往往也忽视了使用ChatGPT协助软件开发对于研究人员自身的专业知识要求。

Hutchins认为，“**精通编程的用户其实是在引导ChatGPT进行开发**，他们可能没意识到自己在过程中起了多么重要的作用。如果缺乏编程经验，用户甚至不知道该给ChatGPT什么样的提示。”

必须承认，ChatGPT目前仍是众多恶意软件开发工具中的一员。在上周发布的报告中，威胁情报公司Recorded Future在暗网和内部论坛中，发现了1500多条关于使用ChatGPT开发恶意软件、创建概念验证代码的参考资料。这份报告还提到，其中大部分代码都公开可用。

Recorded Future认为，**ChatGPT对于“脚本小子、黑客行动主义者、欺诈分子/垃圾邮件发送者、支付卡欺骗者等技术水平不高的网络犯罪分子”最有帮助**。

对于恶意开发领域的新手，ChatGPT也能提供一定帮助。报告总结称，“ChatGPT能为迷茫的初学者提供实时示例、教程和资源，降低了恶意软件开发的准入门槛。”

**ChatGPT有望降低黑客技术门槛，**

**但掀起革命火候未足**

但总体来看，恶意黑客方获得的助益非常有限。ChatGPT虽然降低了黑客技术的学习难度和接触门槛，但同样的内容也完全可以在谷歌上轻松查到。

外媒CyberScoop在去年12月曾报道，随着ChatGPT和其他大语言模型的发展成熟，其编写合法和恶意原始代码的能力也将不断提高。但**在真正的转折来临之前，ChatGPT等工具所发挥的仍以辅助作用为主，做不到凭空生成恶意软件**。

例如，ChatGPT确实能够高效生成网络钓鱼电子邮件。对于难以顺畅使用英语（或其他目标语言）编写含链接恶意消息的俄语黑客来说，ChatGPT能迅速提高他们的写作技巧。

哥伦比亚大学计算机科学助理教授、Barracuda网络安全公司顾问Asaf Cidon提到，“目前绝大多数攻击源自电子邮件，而绝大多数邮件攻击并不属于恶意软件攻击。对方只是想诱导用户交出凭证或者执行转账操作。”Cidon认为“ChatGPT确实很擅长这方面工作”，所以钓鱼欺诈会变得更容易。

但这只是变化中的一环，还不至于掀起黑客革命。**高质量的网络钓鱼邮件已经很容易制作——可以由攻击者自己编写，也可以在外包平台上雇用专业翻译完成。ChatGPT的出现，只是把钓鱼邮件推向了规模化时代**。在Cidon看来，ChatGPT“降低了所需投入”。

还有一种特殊的使用方法，恶意黑客可以利用以往邮件归档对大语言模型进行微调，使其学会企业CEO的文字风格。Cidon提到，这样训练出的大语言模型往往能轻松骗过公司员工。

但专家们强调，在对ChatGPT的网络安全影响进行广泛评估时，必须持续关注整体趋势。目前，已经出现了在针对性攻击中使用大语言模型的有趣案例。不过至少在多数情况下，ChatGPT恐怕还无法提高成功几率。毕竟根据乔治敦大学安全与新兴技术中心研究员Drew Lohn的观察，“网络钓鱼活动已经非常成功，ChatGPT的加入可能并不会产生太大影响。”

总的来说，**ChatGPT等工具有望降低准入门槛、扩大恶意黑客的群体规模**。Lohn认为，ChatGPT也许能“引导黑客在不借助任何新型恶意软件的情况下，顺利完成入侵过程。……目前网络上已经充斥着大量开源工具和预先打包的恶意软件，我担心ChatGPT的普及会把这些工具交付到每个人手上。”

他也承认这个领域仍处于快速变化阶段，情况随时可能不同：“一个礼拜之后，也许一切都将改变。”

**参考资料：cyberscoop.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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