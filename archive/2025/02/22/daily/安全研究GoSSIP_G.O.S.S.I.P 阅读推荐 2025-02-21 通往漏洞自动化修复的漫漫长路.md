---
title: G.O.S.S.I.P 阅读推荐 2025-02-21 通往漏洞自动化修复的漫漫长路
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499777&idx=1&sn=2cb418ec8937da5c3cdd427f2b8dbabf&chksm=c063eed8f71467ce419d37c31a6fb4680cb5c0faf3e8390e0eec6de0ca711e668073865eca6e&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-02-22
fetch_date: 2025-10-06T20:37:36.247997
---

# G.O.S.S.I.P 阅读推荐 2025-02-21 通往漏洞自动化修复的漫漫长路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GoDBxXHNMndu7CRW9NEpAqPxfXWaOIECAVWQWOQiagQibzh8IvtPI2picaUEwhBW1icPz2Ytx8VQyXVA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2025-02-21 通往漏洞自动化修复的漫漫长路

原创

G.O.S.S.I.P

安全研究GoSSIP

今天我们介绍的是一篇来自USENIX Security 2025的SoK研究论文*Towards Effective Automated Vulnerability Repair*，它对当前的 **漏洞自动化修复（automated vulnerability repair，AVR）** 技术进行了总结和展望：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoDBxXHNMndu7CRW9NEpAqosKOEyLMcCwOd1TCcEqKia57cJia3rWibX1cD0Ze4bxv5ayFaA5ynVibibA/640?wx_fmt=png&from=appmsg)

一般我们读SoK论文，主要的预期是了解这个领域的发展现状。今天这篇论文讨论的主题——AVR，属于软件工程领域的一个比较经典的研究范畴——Automated Program Repair的子集。作为和安全息息相关的应用，AVR的特点主要在于它针对的是涉及安全威胁的严重代码漏洞，修复起来一般会比普通的bug要困难一些；与此同时，AVR并不是总能及时处理代码缺陷，而是如下图所示存在一定的滞后性。此外，很多时候即使你知道了敌手的攻击代码（exploit），也不一定知道该怎么修复（特别是要保证已有的功能正常运行）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoDBxXHNMndu7CRW9NEpAqVZFmshB1ZkK7jqwNYw8q8E4ag6rqTUaYIYAvxeE6AE8ZLiaPtuo9Glw/640?wx_fmt=png&from=appmsg)

论文的第二章有很多名词定义，我们阅读的时候可以跳过，在第三章作者介绍他们的分类学（taxonomy）的时候，也顺带介绍了一个很有意思的网站`cspapers`（大家可以访问 https://cspapers.org/ 看看，非常简单的设计风格，很适合快速检索相关论文）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoDBxXHNMndu7CRW9NEpAq66SeX1icr8ezv4rhsxGVA6d9O8Aiba8QDNL04ZSYfuycOuef7ISak4oQ/640?wx_fmt=png&from=appmsg)

具体地，作者把所有的AVR技术分为了四大类：

1. Template Guided：基于一些预设的模板来进行代码修复（G.O.S.S.I.P在2020年拿到SANER 2020最佳论文奖的研究工作`SmartShield`就是一个基于模板进行智能合约代码修复的系统）；
2. Search Based：根据一些规则找到很多代码样本（例如从大量代码变种里面挑选，或者从同一个项目中找相似代码），然后搜索这些样本，找到合适的用于修复的实例；
3. Constraint Based：用一些程序分析技术（例如符号执行）结合代码上下文的特定约束，生成出相关的patch代码；
4. Learning Based：当红炸子鸡，用机器学习来辅助生成patch代码

这些分类的特点和具体的技术优缺点，在论文的第四章有详述，我们今天暂时不深入展开，只是总结一下作者的结论——**这四类技术没有哪一类是可以赢家通吃的**，在不同的应用场景下要结合不同的技术方案来用。我们今天主要想给大家推荐的是论文的配套网站：

> https://sok-avr.github.io/

在这个网站上，第一个特色栏目是“cases”，里面列出来很多案例，让你一看就知道为什么特定类别的AVR技术不总是有效：

> https://sok-avr.github.io/cases/

比如下面这个例子，由于patch涉及到业务逻辑上的知识，因此很难被修复（作者表示即使learning-based的AVR也不行）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoDBxXHNMndu7CRW9NEpAqgvvc6icD6rtkZBc0N7WyLVCaJ3dPJYJYUE1FljbhmBpKMqIKptt90vQ/640?wx_fmt=png&from=appmsg)

而实际上有一些案例，并不需要当前大红大紫的人工智能，反而是一些简单的修复方法更奏效，比如下面的例子：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoDBxXHNMndu7CRW9NEpAq8kPFDbjXO8HdI3D2IfdW97FcIgsTSicgFiaIiavMibz5GU6ZdXJsRvDVeA/640?wx_fmt=png&from=appmsg)

使用静态程序分析方法（结合动态模糊测试）就能正确推断出应该增加的特定约束（注意到这里还有个宏`MAX_COMPS_IN_SCAN`，也需要对整个代码进行分析后才能知道有这么个定义）。

论文网站的第二个栏目“papers”列出来了最近几年相关的学术论文，你再也不用去问AI帮你总结了：

> https://sok-avr.github.io/papers/
> [图片]

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoDBxXHNMndu7CRW9NEpAqVnibxr1Kjw77G6B5hy4ibgxguF6d5iakx2IU9U9z7vZqwzJpr2e9zzSibg/640?wx_fmt=png&from=appmsg)

而论文网站的最后一个栏目“tools”不仅列出了常见的一些AVR工具，还贴心地把这些工具的可用性都进行了总结！

> https://sok-avr.github.io/avr-tools/
> [图片]

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoDBxXHNMndu7CRW9NEpAq2fYdUrNGickdLcibibopH8axpZemqNXLoNgsDg1qb2Tic7g5ZbutT1jxfA/640?wx_fmt=png&from=appmsg)

结合网站去读这篇论文（或者直接“按网站索骥”去使用各种工具），体验更佳。由于网站的存在，我们给出的论文推荐指数是：

> strong accept

---

> 论文：https://gangw.cs.illinois.edu/sec25-sok.pdf

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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