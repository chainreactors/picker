---
title: G.O.S.S.I.P 阅读推荐(?) 2025-01-13 Nothing Bad
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499611&idx=1&sn=f4c84ebd4655e6b7c270acc34692023d&chksm=c063d182f71458946d68d728ea7c53c8c927518a5bf7034bbac7c87669e69efa83fec019fcae&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-01-14
fetch_date: 2025-10-06T20:11:03.935001
---

# G.O.S.S.I.P 阅读推荐(?) 2025-01-13 Nothing Bad

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FlMBxV9eqxHtOGYDwInia5FdMBPZOBTNCdkbtVMkw1b0zR0UY0UffcqqjwLCHNmuwp6oR4Ubn3y0w/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐(?) 2025-01-13 Nothing Bad

原创

G.O.S.S.I.P

安全研究GoSSIP

据说现在YouTube等平台的内容创作者正将其未使用视频出售给AI公司用于训练AI模型。如果AI公司要买我们的论文推荐专栏的数据去训练他们的AI论文阅读机器人，可能以往的内容都只能当作正标签，不过今天我们要给AI提供一个负标签。没错，今天我们要介绍的这篇论文*LLM4CVE: Enabling Iterative Automated Vulnerability Repair with Large Language Models*属于那种看起来没毛病，但是最后你会产生深深的怀疑的类型（如果你真的是一个人类）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FlMBxV9eqxHtOGYDwInia5FrFXWOmic1NehpZdeiceX4USgzdgFhl6tHjdRuMqF7zl021nIIoFKQlAA/640?wx_fmt=png&from=appmsg)

这篇挂在arXiv上的论文，思路非常清晰明确，就是LLM->CVE，也就是借助LLM来实现自动化的代码漏洞修复。论文很套路地上来就在第一页最开始放了一张high level的示意图（这个不是我们的主观说法，而是忘了在什么地方看到过的有一个论文写作的报告里面教大家的技巧之一）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FlMBxV9eqxHtOGYDwInia5FS5VFXC9uUxQ9895p5WbgcGMTIiaX5DyeGnr3tJpOZhLqSoykm6SiaUhA/640?wx_fmt=png&from=appmsg)

问题在于，这张图看起来过于high level，传递的信息非常之少。好吧让我们继续往下看，通读全篇，文章的结构非常标准，一篇论文应该有的部分（详细的背景介绍、和同类工作的对比、清晰的设计、全面的实验、对特殊情况的讨论、代码和数据开源等，甚至还有Ethical Consideration，虽然并不知道写这个有什么用）都一应俱全。如果是那种按项打分，这篇论文在每一项上都至少能得分。那我们为什么要对这篇论文说三道四呢？

给读者们提这么一个问题，你读一篇论文，最期待什么？

套用导演杨德昌在《一一》中的台词——“电影发明后，人类的生命至少了延长了三倍”，我们也可以说，有启发性的论文能让研究人员的思路至少开阔三倍，读别人的论文，自然希望了解别人是怎么解决问题的，有什么和我自己不同的巧妙之处。虽然论文写作上有很多固定的版式需要遵循，但是每个作者在写作的时候，肯定都是围绕着核心的思路——如何解决问题——来展开，再把各个细节都打磨得更好一些。很不幸的是，在AI时代，在打磨论文细节方面，似乎是得到了各种工具的加持，论文在形式上真的是越来越好，可也往往让读者在一大堆内容里面找不到真正的瑰宝所在。回到这篇论文，我们注意到，在长达14页半的正文里面，从一开始的前7页讲了相当多的知识，却似乎没有真正进入到核心主题——用LLM去自动化进行代码修复，如何具体操作。好不容易到了第8页，开始介绍技术方法的时候，却发现最开始那种“高屋建瓴”的风格延续到了这里，整个技术实现章节的细节都很匮乏，除了又一个很high level的图（如下图）来介绍分析的pipeline以外，每个步骤怎么具体去做，几乎不太可能从论文中获得如何复现的知识。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FlMBxV9eqxHtOGYDwInia5F3TYrdQAd6YpHwx3Fu1pYhKY1mvAkx9EhxHFttnB6whymyAPAcvh9FA/640?wx_fmt=png&from=appmsg)

当然，还有最后一根救命稻草，就是作者开源了整个项目，实在不行我们去看看代码？结果那个匿名的4open Git已经过期了……

> https://anonymous.4open.science/r/LLM4CVE/README.md
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FlMBxV9eqxHtOGYDwInia5FrPU5mYKiaoxfAW9fVbibeicyEZJKaAxg5In16dBKFMV6G9AiaZeSJovxww/640?wx_fmt=png&from=appmsg)

读到这里（如果你也耐着性子把论文都看了一遍），你是不是同意我们的观点？很多年以前，在某一次HPCA+CGO+PPoPP会议联合开幕式上，某Chair说“我们应该选择那些something good而不是nothing bad的论文”，可事实上这么说就是因为（特别是顶会）审稿人可能更喜欢那种四平八稳挑不出来大毛病的论文？以前可能“生产”一篇看起来各方面都不错的论文还是要花点时间的，但今天有LLM和AIGC加持，大概审稿人要被更多“nothing bad”的论文逼到墙角了？更何况，我们这么多读者，每天都被数不清的论文（特别是arXiv这种挂上去没有什么成本的情况）“乱花渐欲迷人眼”，那么论文作者们，大家能不能学习高斯的那句座右铭：“Pauca sed matura（少些，但是要成熟）”。

所以我们今天的 G.O.S.S.I.P 推荐指数为：

> Reject

---

> 论文：https://arxiv.org/pdf/2501.03446

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