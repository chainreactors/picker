---
title: [AI安全论文] (32)南洋理工大学刘杨教授——网络空间安全和AIGC整合之道学习笔记及强推（InForSec）
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247499894&idx=1&sn=b13567ba9da2116544931b0b3b32fb0d&chksm=cfcf70bbf8b8f9ad60043155333761e2d3a828f6b5952b33b73545830442f0c27963d34a3521&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2024-05-03
fetch_date: 2025-10-06T17:16:19.640081
---

# [AI安全论文] (32)南洋理工大学刘杨教授——网络空间安全和AIGC整合之道学习笔记及强推（InForSec）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRNfHf2ODbJ7tuvFm64uuGbriaJD1oKh2alzM30yDvRqAMd628CkwTSL9pHiaTxVFA02euhMtqBhxNBw/0?wx_fmt=jpeg)

# [AI安全论文] (32)南洋理工大学刘杨教授——网络空间安全和AIGC整合之道学习笔记及强推（InForSec）

原创

Eastmount

娜璋AI安全之家

首先祝大家五一节快乐！《娜璋带你读论文》系列主要是督促自己阅读优秀论文及听取学术讲座，并分享给大家，希望您喜欢。由于作者的英文水平和学术能力不高，需要不断提升，所以还请大家批评指正，非常欢迎大家给我留言评论，学术路上期待与您前行，加油。

本文是南洋理工大学刘杨教授在InForSec学术报告的分享学习笔记，题目是“网络空间安全和AIGC整合之道”。刘老师是我们非常佩服的一位大佬，他们的很多安全工作都值得我们学习，这次分享真的很棒，值得大家去学习。同时，更重要是看看刘老师他们团队面对一个新方向或新热点，他们是如何去探索与安全结合，如何去从事科学研究的。本文按照刘老师汇报内容描述，并凝练出重点内容（详见博文中重点标注的思路梳理），尤其是科研探索的过程，从而方便大家学习。学习笔记文章，希望对大家有所帮助。最后感谢刘老师的分享，以及InForSec的组织，推荐大家关注和学习。

> 演讲主题：网络空间安全和AIGC整合之道
>
> 演讲人：刘杨 新加坡南洋理工大学（NTU）计算机学院教授
>
> 时间：3月26日10:00-11:00
>
> 地点：清华大学 FIT楼1-312
>
> 直播地址：www.inforsec.org/wp/?p=781

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNfHf2ODbJ7tuvFm64uuGbranrjrgxkYOvUEqLDEhua3GBC9sVjZYDGOiaN3Z3PJkkw2KiaTk0JTicicA/640?wx_fmt=png&from=appmsg)

> PS：由于当时直播略有杂音，加上自己网络环境和英语比较差，部分笔记听得不是很清晰，还请大家多多包涵。

文章目录：

* 前文回顾
* 一.内容及演讲人简介
* 二.AI for Security
* 三.LLM-Enhanced Static Analysis for Vulnerability Detection（ICSE24）
* 四.Expert Knowledge Learning with Automatic Chain-of-Thoughts Decomposition
* 五.Understanding Zero-Shot Fuzz Driver Generation（FSE 24）
* 六.Automated Penetration Testing with LLMs: PentestGPT
* 七.Automated Vulnerability Diagnosis（ASE23）
* 八.Fine-tuning LLMs for Automated Program Repair（ASE23）
* 软件基因组计划
* AI安全领域
* 总结

> 2024年4月28日是Eastmount的安全星球——『网络攻防和AI安全之家』正式创建和运营的日子，该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNfHf2ODbJ7tuvFm64uuGbrs2Lb22cSeF8Yd2wu1bO9icP3fcibGibSvakFwoibqY9pT5w9K1FSSbPcjA/640?wx_fmt=png&from=appmsg)
> 目前收到了很多博友、朋友和老师的支持和点赞，尤其是一些看了我文章多年的老粉，购买来感谢，真的很感动，泪目。未来，我将分享更多高质量文章，更多安全干货，真心帮助到大家。虽然起步晚，但贵在坚持，像十多年如一日的博客分享那样，脚踏实地，只争朝夕。继续加油，再次感谢！

---

# 一.内容及演讲人简介

内容摘要
AIGC 和网络安全要求在软件开发过程的所有阶段系统地整合安全测试，其目的是通过使用工具，将人类专业人员的安全专业知识自动化，从而能够在开发生命周期的早期阶段及早识别和解决安全问题。然而，其有效性在很大程度上取决于智能工具模拟或可能替代安全专家的能力。随着 LLM 的出现，现在有了实现这一目标的新手段。在本演讲中，刘杨教授将讨论最近在应用安全领域利用 LLM 的努力，以涵盖漏洞分析的整个生命周期：漏洞检测、诊断、POC 生成和修复。另一方面，LLM 的安全性对于确保人工智能应用程序的成功部署同样重要。在这个方向上，刘教授将展示有关 LLM 攻击面的最新研究成果、针对提示注入的黑盒/白盒攻击生成、针对多模态模型的攻击、后门攻击以及可能的防御机制。最后，刘教授将研究如何将这两方面结合起来，开发一个人工智能应用安全分析平台。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNfHf2ODbJ7tuvFm64uuGbrL8piby89yIsicup5x5D6OI6P18a85aQlQWjAXpvib1W9y9XJaXib6wB8Lw/640?wx_fmt=png&from=appmsg)

演讲人简介
刘杨博士现任新加坡南洋理工大学（NTU）计算机学院教授，NTU网络安全实验室主任，新加坡网络安全研究办公室主任，并于2019年荣获大学领袖论坛讲席教授，在2024年荣获校长讲席教授。刘杨博士专攻软件工程，网络安全和人工智能，其研究填补了软件分析中理论和实际应用之间的空白，研发了多款高效的软件质量和安全检测平台并成功商业化。到目前为止，他已经在顶级会议和顶级期刊上发表了超过500篇文章，并在顶级软件工程会议上获得25项最佳论文奖以及最具影响力软件奖。他还同时负责多个重要研究中心，包括新加坡网络安全研究办公室（CRPO）、南洋理工大学可信AI研究中心（TAICeN）以及与ICL合作的医疗设备安全CREATE中心。他还获得多项著名奖项，包括MSRA fellowship，TRF Fellowship, 南洋助理教授，Tan Chin Tuan Fellowship，Nanyang Research Award 2019， ACM杰出演讲人，新加坡杰青和NTU创新者（创业）奖。

* https://personal.ntu.edu.sg/yangliu/

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNfHf2ODbJ7tuvFm64uuGbrmJIa6S3f0rruvblmSX2qFAiaqOqsCjWHceKNVvOrBtNGeEVH7XicpDhg/640?wx_fmt=png&from=appmsg)

---

# 二.AI for Security

刘老师首先感谢邀请，非常谦虚。这次汇报的题目是大家最近都非常关心的——安全和AI大模型结合的一些工作，尤其是最近一年多他们团队在这个方向里的尝试。

* A Road Towards an Interaction between Cyber Security and AIGC

接着，就直奔主题——大模型（AIGC）和网络空间安全的整合之道，主要分享一些科研的思路，以及在科研过程中的一些想法。借这个机会希望与大家一起学习探讨“AI和安全融合过程有哪些的可能性或者是挑战”。

今天的第一块内容是——AI来做安全（AI for Security ）。
这个题目其实并不是很新了，但是过去一年多，从2023年大模型出来以后，大家在探索AIGC和大模型在安全落地应用中的工作。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNfHf2ODbJ7tuvFm64uuGbrXtDaJ6VYh8yHU5jfOjniaeuTnR3KRBMe4wtGQUyRLLJIcicgkORqhtVQ/640?wx_fmt=png&from=appmsg)

首先，刘老师给出“Architecture of LLM-based Security Tollchain”框架图。该图更多是从整个思路上来看大模型在应用安全，尤其是在漏洞场景中，它能不能相对来说做一个系统化的落地。

安全场景：

* Traditional Software
* Blochchain Software
* AI-based Software

基于此我们开展：

* 漏洞分析（Impact Analysis）
* 漏洞检测（Vuln Detection）
* 漏洞诊断（Vuln Diagnosis）
* 甚至POC的生成和漏洞修复（Vuln Repair）

我们希望在这一系列漏洞整个生命周期中，大模型的思路是不是能够通用的应用。在这个过程中，我们care的不是一两个工作，care更多的是整个过程中能不能形成一套相对来说比较系统的大模型在安全场景落地的方法。这个其实是今天刘老师更多想分享的，而不是某一个具体的工作。这也是他过去一年中主要思考的问题。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNfHf2ODbJ7tuvFm64uuGbrWZyYrDRHCtcJ6nricEwE68mOy7YQ4PyDa4Bbnc6bibNh6hd0PYTia2BSQ/640?wx_fmt=png&from=appmsg)

基于此，我们有数据data、有模型、有技术、有知识，它们如何在大模型中应用呢？并达到一个我们想要的效果。

具体而言，刘老师接下来通过几个具体的工作来分享他们在尝试的过程中遇到的问题、挑战或得到的一些潜在解决方案。

---

# 三.LLM-Enhanced Static Analysis for Vulnerability Detection（ICSE24）

重点1： 大家目前可能最关心的或最火爆的一个题目——如何用AIGC大模型去找漏洞。
当时我们做这个题目，是当ChatGPT出来之后，2023年3-4月份时间，很多人就去拿ChatGPT找漏洞。当时有一些结果是非常不错的，因为ChatGPT对比较完整的代码的信息差收集还是全的，所有在某些场景下，当我们把含有漏洞的代码丢给ChatGPT时，它能精准地告诉我们这些代码有什么漏洞。之后，很多人会疑惑——这东西靠不靠谱，ChatGPT是否能作为一个安全人员或安全审计人员的代替。

出现两周后，就看到了一些安全公司说这东西不靠谱。为什么？因为我把这些漏洞稍微做一些修改，比如没有漏洞的代码修改成漏洞，丢给ChatGPT，它完全没办法识别。因此，这会导致大量的误报和漏报，安全公司就给出了明确的证明和具体实验数据说：

* “ChatGPT只是对全完见过的有漏洞数据的反射，其实它并没有能力去做安全漏洞检测或修复。”

重点2： 看到这样的新闻后，我们就有了一个想法——大模型在安全应用尤其是找漏洞的场景，它能做什么呢？它的能力是什么？我们如何把它的能力使用好呢？这是我们当时的想法和探索。

在探索的过程中，我们发现：如果想把大模型直接用来找漏洞，这个事情本身是不靠谱的。因为大家知道大模型本身是根据大量代码和它对应解释文本、标记来反馈信息的，但漏洞本身是非常复杂的，你可以更改一个字母或代码就会导致漏洞不触发，这种微小的改动或非常细的信息是大模型完全没法控制的。

因此，直接用大模型去直白地找漏洞，它本身从方法上是不靠谱的。但是，大模型有没有用武之地，我们怎么用呢？我们有哪些可行的方式，这就是我们接下来将探讨的。

重点3： 刘老师他们进行了各种尝试，包括如何将专业（安全）知识交给大模型，怎样把安全专家找漏洞的思维（经验和想法）告诉大模型，譬如这种漏洞的识别方法或套路。然而，这些信息并未公开或形成比较好的数字化方式允许我们像ChatGPT一样收集大量文本信息和训练，所以这种非常专业的精准知识如何捕获和利用，这是我们在做研究的重点和思考。

他们进行了不同的尝试：

* 第一种尝试是把找漏洞的过程，我们利用大模型来做分析。 比如代码逆向，我们在想怎么更好地模拟人去找漏洞的过程，分析人找漏洞的过程及需要哪些步骤，以及哪些步骤能用潜在的大模型实现，包括代码逆向、代码分析、代码漏洞确认这些步骤里用大模型实现的地方。尝试分析发现，在代码逆向方面，大模型有好的场景（阅读能力）。

做完这个工作后发现，大模型在找漏洞中是有用武之地的，但并不能代替我们传统的程序分析，不管是静态的还是动态的分析，它们是相对精准的，并且是大模型不擅长的。但是，大模型有能力非常好地总结和阅读代码，该行为恰好是黑客在找漏洞过程中所用的方法，而传统方法或工具其实并没有真正地理解代码。因此，现有大部分自动化工具都基于非常明确的规则来找漏洞，而没有通过语义理解和推理实现，最终做了一个GPTScan工作。

重点4： GPTScan基本思路就是模拟安全审计人员他们的思维过程，把这个过程分成了Planning、Reasoning和Validating三个部分，重要的是想安全专家一样理解代码（安全知识）。

> GPTScan proposes the first LLM-based static vulnerability detection pipeline,combining LLM with program analysis to achieve improved accuracy (~70% F1-score). It also identifies 9 new vulnerabilities missed by human auditors.

* Planning
* Reasoning
* Validating

Planning 相当于一个对整个代码的分析，想知道哪些函数是重要的，哪些函数可能会有漏洞。基于想要的这些函数找到之后，我们再去做一个漏洞行为分析，譬如哪些函数与某种漏洞类型相关，再去做对应的行为识别或寻找函数中具体的变量等，接着进行确认。确认完之后，再去做潜在的漏洞验证和发现。

整个过程其实就是在模拟评价黑客拿到一个项目或代码，是如何找漏洞的，他通常看过很多代码且对特有类型漏洞比较熟悉，该漏洞在代码中潜在的关联函数有哪些，有了之后再去分析函数块，函数中哪些行为或逻辑与该漏洞相关，找到之后再进一步确认。他可能也用一些程序分析或Fuzzing辅助工具，来确认这个行为是不是漏洞。

* 因此，整个过程就是在模拟安全审计人员的思维过程，我们相对来说把它拆得更细，并且在这个过程中，某些步骤使用ChatGPT的一些代码阅读总结能力来实现。

研究结论：

* 实验结果发现效果非常不错，F1值达到了70%。目前，市面上所使用的很多SA\SB代码漏洞扫描工具，F1值大概在10%~20%之间，存在大量漏报和误报，导致工具无法使用。
* 该工作更重要的是第一次把逻辑类型的漏洞，有了一个能力，在不需要提前把它规则写死的情况下，通过ChatGPT的代码阅读、理解，甚至逆向能力把这个事情达成。因此，这是对我们的一个巨大的启发。换句话说，第一次拥有一个真正专家帮助自动化理解代码，它的能力对我们找漏洞的应用和支持是非常有价值的。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNfHf2ODbJ7tuvFm64uuGbrFaBcI1WzMibEwy2bRCtcicClJWRxuA6vDxaMGdabUhQTxjR8wGoSwMYw/640?wx_fmt=png&from=appmsg)

---

# 四.Expert Knowledge Learning with Automatic Chain-of-Thoughts Decomposition

重点5： 我们对多种类型的漏洞进行测试，看是否能更好地系统化支持多种类型的漏洞自动化识别，因为每种漏洞可能不太一样。那么，我怎么样能把找漏洞的过程做更好的泛化，这是刘老师他们后面又做的一个研究。

在这个过程中，我们尝试了非常系统化的工作，将ChatGPT的调用或整套流程进行非常系统的问答映射，将执行过程的整个思维，给你很多例子进行辅助。但在泛化过程中会发现，每次漏洞都要写对应的提示。那么，如何更好地做泛化呢？这就导致了后续的工作。

* Expert Knowledge Learning with Automatic Chain-of-Thoughts Decomposition

该图比较复杂，其本质是：

* 如何把不同类型的漏洞描述或审计报告的现有文字，通过一个相对来说比较系统的方法论，能变成所谓Chain-of-Thoughts，即一个对安全审计人员行为的数字化的结果或数据结构，然后将该数据结构收集起来做研究（RAG）。

首先需要找到能力点，再通过数据收集、数据标注、数据使用和分析（RAG）。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNfHf2ODbJ7tuvFm64uuGbr5ibZicjic79etvhXW0ia2vRw1fl0t1QjBiaCqK8FkDEDDHExVAibBa2mTiaEg/640?wx_fmt=png&from=appmsg)

该工作属于我们的探索性研究，包括对RAG的探索，如果在某个领域中数据的准确性、数量能收集得更多，那我们是否在大模型中能取得更好的结果。在探索过程中，刘老师更关心的是：

* 我们怎么样在不同的语言、不同的场景、不同的业务逻辑、不同的漏洞类型里面，能不能形成一个相对通用的大模型漏洞挖掘使用的方法，这可能是更有意思的事。

重点6： 安全场景应用以及为什么选择智能合约。
我们的两个工作是在智能合约中完成，并且效果还不错，将其变成自动化的agent，自动找漏洞并得到应用和正反馈，后续也尝试做其它领域。为什么选择智能合约呢？

* 因为智能合约相对代码复杂度、代码体量相对比较可控，包括类型和描述、数据也相对更好。后续将研究如何扩展到其它场景。

---

# 五.Understanding Zero-Shot Fuzz Driver Generation（FSE 24）

重点7： 从静态场景过度到动态场景。
之后，我们正在做的工作是FSE24的文章。这篇文章是在另一个场景做的，之前更多是静态的，这个工作是在动态场景中的尝试。

> 首先介绍论文《Understanding Zero-Shot Fuz...