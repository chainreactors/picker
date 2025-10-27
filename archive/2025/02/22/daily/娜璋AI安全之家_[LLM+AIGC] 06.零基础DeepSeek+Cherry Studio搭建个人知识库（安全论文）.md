---
title: [LLM+AIGC] 06.零基础DeepSeek+Cherry Studio搭建个人知识库（安全论文）
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501556&idx=1&sn=876ab5241333fad891e7341869011033&chksm=cfcf7639f8b8ff2fb7c9c162e25910a399574c9201cb318a896333e9e19fb9630a96d539e69a&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2025-02-22
fetch_date: 2025-10-06T20:40:13.638503
---

# [LLM+AIGC] 06.零基础DeepSeek+Cherry Studio搭建个人知识库（安全论文）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRMgxppb2RO0yA79kDDs60koKt9a4Q9rFFO4dLRJzauy5ETkUklRRfYu0NBPMMicAPl3gh8H6KTtVVg/0?wx_fmt=jpeg)

# [LLM+AIGC] 06.零基础DeepSeek+Cherry Studio搭建个人知识库（安全论文）

原创

Eastmount

娜璋AI安全之家

> 2024年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![图片](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRN2D0ib34nN6fIBViblH1xb9RujXz10hUiaqGBEeGK2ibe0KUfwu5rBYEAnluHZ0cAKLqASZvicFRJJ3Mw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

近年来，人工智能技术火热发展，尤其随着ChatGPT和DeepSeek被提出，其能够基于在预训练阶段所见的模式、统计规律和知识来生成回答，还能根据聊天的上下文进行互动，真正像人类一样来聊天交流以及完成复杂的NLP任务。基于此，为更好地学习前沿AI知识，了解LLM和AIGC应用实战，本人开启了《LLM+AIGC》专栏，一方面作为在线笔记记录和分享自己的学习过程，另一方面期望帮助更多初学者以及对LLM感兴趣的同学。知识无价人有情，希望我们都能在人生路上开心快乐、共同成长。

该系列主要涵盖三方面：

* **原理篇**——以原理介绍和论文阅读为主
* **实战篇**——以编程构建自制LLM和RAG为主
* **应用篇**——以应用实践和Prompt探索为主

前一篇文章带领大家了解如何利用DeepSeek+Kimi自动生成PPT，以威胁情报为例进行探索。这篇文章将分享如何利用DeepSeek+Cherry Studio搭建个人知识库，以安全论文为例进行探索，大家可以结合自己需求进行尝试。基础性文章，希望对初学者有所帮助！且看且珍惜，加油 O(∩\_∩)O

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRPiajFNxJ8BvPfDR9ZAn5Jxg9IyCgTcbCiaoVHYBylibl3kSf6TDbEwezTnM9RWXy2hEtgckGDZzHFDA/640?wx_fmt=png&from=appmsg)

文章目录：

* **一.DeepSeek接入 二.Cherry Studio搭建知识库 三.验证本地知识库 四.问题与解决 五.总结**

前文赏析：

* [[LLM+AIGC] 01.应用篇之中文ChatGPT初探及利用ChatGPT润色论文对比浅析](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247498715&idx=1&sn=25d1d966ac5dbfdf80cf7e06df977305&scene=21#wechat_redirect)
* [[LLM+AIGC] 02.零基础DeepSeek入门初探及云端搭建详解（ChatGPT对比）](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501379&idx=1&sn=57bd5ed7fef46854c0205d9afabc2479&scene=21#wechat_redirect)
* [[LLM+AIGC] 03.零基础DeepSeek云端（硅基流动、腾讯云、国家超算平台）搭建及API接入](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501451&idx=1&sn=c16c0d24477f33768dbbfe3732a473d3&scene=21#wechat_redirect)
* [[LLM+AIGC] 04.零基础DeepSeek接入WPS实现智能办公](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501493&idx=1&sn=1fc9b744b393a1fc45a2c700d0fef83b&scene=21#wechat_redirect)
* [[LLM+AIGC] 05.零基础DeepSeek接入Kimi自动生成PPT（威胁狩猎领域）](https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501520&idx=1&sn=3341862984ccc75b3c729583c99086bc&scene=21#wechat_redirect)
* [LLM+AIGC] 06.零基础DeepSeek+Cherry Studio搭建个人知识库（安全论文）

---

# 一.DeepSeek接入

前面的第3篇文章我们介绍过Cherry Studio的用法，从官网下载安装如下图所示：

* https://cherry-ai.com/

> Cherry-Studio 是一个 面向开发者的工具或平台，主要用来帮助开发者更高效地完成工作。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koSm3Cve3eQh77ibIfwXVnDMicdgG6226U69iaaGd4NanYl8w4xFHgp0fXg/640?wx_fmt=png&from=appmsg)

**第一步，打开硅基流动的官网，并注册。**

* https://siliconflow.cn/zh-cn/

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koHylAjr1sdtT6ibnderXShOAeuIR4wwMbhQ9WTyKaozIeCE2lrl4rEfg/640?wx_fmt=png&from=appmsg)

**第二步，注册登录后找到“API 密钥”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60kox2hYacHnhfjp88cx4Ae4EjDs2FvUibKj1GF9ibPQEkafAVqORAabESkg/640?wx_fmt=png&from=appmsg)

新建API密钥，并定义一个名字“Knowledge”。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60kostktcHpBWp3eibQho5uuPoSKYonNaJmvG9CIdL4cqDEKlF6eTqJ0cWQ/640?wx_fmt=png&from=appmsg)

复制刚建立的API密钥。

* sk-kqfqnd\*\*\*\*\*\*\*\*\*\*\*\*czhaoxnsc

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60komb8vIHsRwPw32hiacBicQFNWYPLxZn3lZ3cPich8hNUG2N1CPGCMgZMGQ/640?wx_fmt=png&from=appmsg)

**第三步，在设置中点击“API密钥”，并输入上面的Key。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koHeUDgTNxibba8ytvTtbMlZkAcyiaJbQC69MQz1icyExZqZibnia8QYU1qdA/640?wx_fmt=png&from=appmsg)

点击“检查”，选择对应的模型DeepSeek-R1。至此，DeepSeek相关配置完成。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koMDfGIjMWx31bjmBhAjiaN4ItKuVr9D65bnqicFccpe3YWk7kGPct4fvA/640?wx_fmt=png&from=appmsg)

接下来我们将配置Cherry Studio来搭建知识库。

---

# 二.Cherry Studio搭建知识库

**第一步，在本地整理知识库相关论文。**

> 注意：作者为了方便演示，将文件夹放置在桌面，读者通常会放在一个非C盘的指定目录，后续需要持续更新知识库。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60ko7oKS9a6iapgVoZS6ibVT6c590V7OG6ACLCYXwEjSHZ5jWsV0qF4BFMlQ/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60kobKDCAClB8u5RotRNn0ct4WfJpicyZibcjgzBUibe16CU5XZvw9SHfO9YQ/640?wx_fmt=png&from=appmsg)

**第二步，打开Cherry Studio，点击“知识库”按钮，选择“添加”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koVPB0IwVUFIHyiaFhoeibT1iaicibvECNicPodibnUiblApnQytOGaVHzcg1mDA/640?wx_fmt=png&from=appmsg)

**第三步，根据需要添加名称和嵌入模型。其中，嵌入模型用于知识化向量检索。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koaAHLpCRLmPTzjB0FpBxPpiaSzO2pLbC894qy8ibffXqEEIBV0G3J83MQ/640?wx_fmt=png&from=appmsg)

作者的仅有硅基流动的BAAI/bge-m3模型，如下图所示。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60kohz9g0wclrpTbPQriaM7JibyonCDngAWIU0d1sibDBmqj5MdYqSKaopo2w/640?wx_fmt=png&from=appmsg)

注意，这里的模型即为硅基流动中“模型广场”->“嵌入”的BAAI/bge-m3模型。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koCIhGzZvgnBr0JrM41acBELvLg2w6A5aNj50ajufn5IMjRiaztQcCG2g/640?wx_fmt=png&from=appmsg)

**第四步，添加目录。可以添加的文件类型很多，读者可以自行尝试，大家也可以将准备好的文件拖拽进去。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koDuBojUtFELZGlxpoRwyZN0vpOwBKLvI6r44KEoIBBj6s1cblkWDBWw/640?wx_fmt=png&from=appmsg)

此时该软件会调用嵌入模型对文件夹内的文件进行向量化处理。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60ko4SdELFTN24WRJJlp4w0OicNzTRUGiccKxp9j3KqD5q9P12Nvf5JsSs3Q/640?wx_fmt=png&from=appmsg)

等待片刻，文件目录添加成功。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60kobXia776IO23brCibAgEibZUP9PRelZRTR1ibtawgYYdyibTYLH8PwkC89Jw/640?wx_fmt=png&from=appmsg)

**第五步，处理完成后，点击按钮回到对话页面，并且开启刚才创建的知识库“CyberSecurity”。**

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60kovfPfunKa2S01baIaLYJYibA4gbZ9gqricaGO0543vYRROHpibmRJq1pwg/640?wx_fmt=png&from=appmsg)

**第六步，开始DeepSeek+Cherry Studio本地知识库的只能问答。**

> 提示词1：
> 我现在需要一篇APT威胁狩猎的学术论文。

可以看到模型在调用本地知识库的知识。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koFUr7KhrKicEDPn7ZJPhibDibAfm3ABEiaTiaGh9WzN1DKuD9ooJXwsw4WZw/640?wx_fmt=png&from=appmsg)

DeepSeek生成的结果如下。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koOLgBUz3gNL5ZAmWBcQeCKvRqUtdBicxlbDUK3ibqqhekSxsa0GHykMKg/640?wx_fmt=png&from=appmsg)

同时给出相关引用。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koJ0AvGMKLzphsBI5DTvu2UyuMq1m6Q2qVnaHlOcouC1acbgWSSO6QUA/640?wx_fmt=png&from=appmsg)

索引确实是作者本地知识库中的文章。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koQaEBpw672QHicibeh0NUAHccT9YndGzrmuDwcAaTthkErM559rnB0Meg/640?wx_fmt=png&from=appmsg)

此外，编辑可以生成Markdown格式，方便大家作为本地存储和编辑。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60ko8LEprymdyxwBpe2aqFYsuNv9X2SaUtMmib3EV20iaXeBPHJuvyWL9gHw/640?wx_fmt=png&from=appmsg)

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60ko1549qqTEFD5NEMaWZy8Ijhia38bmx7rcWNdZXR5VyYficf7ImxnSBymA/640?wx_fmt=png&from=appmsg)

---

# 三.验证本地知识库

接下来，我们简单验证大模型究竟是仅学习到本地文件的名称，还是对其内容也进行了学习。

> 提示词2：
> 请从本地知识库中给出3篇代表性大模型存在的安全问题的论文，并介绍论文提出了什么方法来解决该问题的。

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60kofg6yyn6PbLq4HhJE90u5rScbzFhqflWEdvwicNIwrhkDvkszAtUtD9w/640?wx_fmt=png&from=appmsg)

生成结果如下图所示：

![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRMgxppb2RO0yA79kDDs60koNgIC2wPLBjFRfvXWiboxzVy0OjR9RLax4xmmWjXcRka0QjDg6DNHF9w/640?wx_fmt=png&from=appmsg)

对应答案为：

```
三篇代表性大模型安全问题的论文及解决方案
1. PathSeeker: Exploring LLM Security Vulnerabilities with a Reinforcement Learning-Based Jailbreak Approach
问题：大型语言模型（LLMs）在安全对齐上仍存在漏洞，可能被恶意利用生成有害内容。
方法：PathSeeker提出了一种基于强化学习的越狱攻击方法，通过生成针对性输入来绕过模型的安全机制。该方法通过实验验证了模型的脆弱性，并强调了安全对齐技术的改进需求12。

2. LLMSMITH——揭秘LLMs集成框架与应用中的RCE漏洞
问题：LLMs在集成框架和应用中可能引入远程代码执行（RCE）漏洞，导致严重的安全风险。
方法：LLMSMITH通过分析LLMs集成框架的架...