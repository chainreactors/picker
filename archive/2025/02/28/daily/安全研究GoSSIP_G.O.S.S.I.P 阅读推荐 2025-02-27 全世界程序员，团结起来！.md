---
title: G.O.S.S.I.P 阅读推荐 2025-02-27 全世界程序员，团结起来！
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499800&idx=1&sn=a0ddcd52f005448d8c6af28861b82333&chksm=c063eec1f71467d74bb40e00a300cdda548cee447eea07b1e0795f5b9c794ec08e3480b1f63d&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-02-28
fetch_date: 2025-10-06T20:38:38.690389
---

# G.O.S.S.I.P 阅读推荐 2025-02-27 全世界程序员，团结起来！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21EfNteibgqOXlqzDUNfNEgwiaz1kuNCYRsskTsDRzgBujwTLDGc4w5Ojgzw83xP7npGTGvpIl42CjXQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2025-02-27 全世界程序员，团结起来！

原创

G.O.S.S.I.P

安全研究GoSSIP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EfNteibgqOXlqzDUNfNEgwiax9sq7giapSVbBQKaUyXXjw6tAxVGtyPapyHU0yiarbOKV49y6MV43heQ/640?wx_fmt=png&from=appmsg)

尽管现在“程序员要被AI取代”的言论甚嚣尘上，但是毕竟人工智能也是从码农们辛辛苦苦构建了多年的数字世界中汲取养分才能茁壮成长，心中必会怀着感恩之情。这不，OpenAI最近发表的一篇研究论文 *Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?* 就表明，虽然LLM很强，但是在那些能够通过编程去赚钱的地方，~~它们还是高抬贵手放过了卑微的程序员~~ 程序员还是比AI更有价值。

此前，大家测试大模型都是用什么数学竞赛、IOI或者是脑筋急转弯之类的题目，这些很有智力优越感的问题却不涉及真金白银，而OpenAI想了想，觉得AI的终极目的是要取代人类，那不妨拿人类用来赚钱的问题——软件外包任务来测试LLM？于是就发布了一个叫做`SWE-Lancer`的benchmark，里面包含了1488个外包任务（这个数字选得很有中国文化特色啊，一看就是跟什么1688、8848学的），都是从Upwork (https://www.upwork.com/) 这个外包网站上搜集的真实任务，涉及的总酬金达到了一百万美元（但是听说美国鸡蛋涨价了，估计现在对应的金额也要升值了）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EfNteibgqOXlqzDUNfNEgwiamjlVGk7XkpAlEfMOZeSCwW7CVH9191VtHEqYBAN5nFJxAUqmtsKs9Q/640?wx_fmt=png&from=appmsg)

最有趣的是，这个`SWE-Lancer`里面不只有编程任务，还有**涉及到manager的相关任务**，具体就是要求LLM去分析**针对特定任务的proposal**，然后选择最佳的（而且，在`SWE-Lancer`这个任务包里面总共百万美元的酬金，涉及manager的任务占了585225美元）。看到这里，你是不是觉得会心一笑，以后只要用LLM把自然科学基金的评审专家全部替换掉，天下苦评审专家久矣的众多申请者就可以大喊“我命由我不由天”了！那我们赶紧看看现在LLM能不能行（不行的话，大家就一起加班，尽快让评审专家被取代）。

具体到测试过程，如果是针对开发任务，那么AI必须要通过所有的需求项，才能拿到钱（模拟），否则一分钱拿不到：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EfNteibgqOXlqzDUNfNEgwiaI7BiakHUcLLxFhaLvIljEUCfcxB48GJW753Q0EVOm5VR0addlWFWMsA/640?wx_fmt=png&from=appmsg)

开发外包所涉及的任务也包含了多方面的需求，如下图所示，其中简单的任务（例如fix bug这种）报价可能只有250美元到1000美元，而实现特定的功能（例如在app里面开发一个视频回放功能）报价就会高到16000美元以上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EfNteibgqOXlqzDUNfNEgwiavxohyqexgdiaiaicSSiaWHoMOQ4ibDbXwnY1G68KvBSjwtQEIbvOtt8DEzA/640?wx_fmt=png&from=appmsg)

而管理任务主要是看AI能不能做出和人一样的选择，如果和人选择是一致的就拿到报酬，这一看就体现了当manager是可以混日子的，反正总归n选1，至少有1/n的概率能够拿到钱！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EfNteibgqOXlqzDUNfNEgwiaUefRx0sAsrIgqvo0CnRBAkAuuXYNQNKWsnGe5BmdwModu00T1MtVfg/640?wx_fmt=png&from=appmsg)

那让我们看看结果，虽然AI并没有把百万美元全部拿走，三个选手（GPT-4o、o1和Claude 3.5）最少也拿走了30万美元，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EfNteibgqOXlqzDUNfNEgwiaLG5GTE43NvGet63tHiaQPxSfrGv2ic4vt1GICq0B9OhzBiaxdnEmVESAA/640?wx_fmt=png&from=appmsg)

当然，论文也说了“As shown in Figure 6, all models performed better on SWE Manager tasks than on IC SWE tasks”，~~**看起来在码农被取代之前，manager肯定要先下岗**~~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EfNteibgqOXlqzDUNfNEgwiaJenK3RwvozRKFc7rmY74xYiaouBkL9Ntq8CuibsuVKbbMwtzttmAjKJQ/640?wx_fmt=png&from=appmsg)

下表更是说明了大模型在开发岗和管理岗的各方面的差别：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EfNteibgqOXlqzDUNfNEgwiahah3a0eKyiab9FIoX0rEplPnkeWbqO8Qw5jDzGcMsXqiaarC4ok333HA/640?wx_fmt=png&from=appmsg)

论文里面当然讨论了很多细节，我们只是吃瓜群众就不去细细叙述了，注意到这个测试是禁止大模型去联网搜索的，因而比的是推理能力，Claude在这个测试中（当时还没发布最新的Claude 3.7）名列前茅。不过也要吐槽一下现在AI时代的论文，正文8页的内容基本上就是报告个结论，然后附录可以搞个20页，全部都是prompt内容……

最后转载一则旧闻（来自《中国大百科全书》网络版）：

> 工业革命引发的结构性和技术性的变迁导致手工业者收入降低。拿破仑战争限制英国纺织品出口欧洲大陆，加速了英国纺织业手工业者生活境况的恶化，使他们失业，同时面临物价上涨。工人要求最低工资的努力失败后，采用骚乱、破坏劳动机器的方式，向雇主施压，迫使雇主改善待遇。18世纪晚期，英国莱斯特郡一个名叫卢德的工人为抗议工厂主的压迫，第一个捣毁织袜机。此后，有纺织工人采取类似行动，这类破坏生产工具的行动，史称“卢德运动”（Luddite Movement）。1811年初，英国和美国之间的纺织品贸易受到限制，加剧了手工业者的不满，把卢德运动推向高潮。

> 1812年，英国议会通过《保障治安法案》，动用军警对付工人，在北部和米德兰地区派出1.2万名军警镇压工人。参与运动的工人在夜间发动袭击，白天则消失在支持他们的社区里，为政府遏制卢德运动带来难度。4月，在西赖丁的袭击中，一位工厂主受袭后死亡，使得这一运动失去来自社区的支持。同年政府颁布《捣毁机器惩治法》，规定可用死刑惩治破坏机器的工人。此后，约克郡绞死和流放破坏机器者多人。1814年企业主成立了侦缉机器破坏者协会，残酷迫害工人。但运动仍继续蔓延。1816年这类运动仍时有发生，此后逐渐消失。

> 卢德运动希望实现的收入增加、限制新机器使用的目标并未在后世实现，但他们所表现出的大众激进主义的文化，则在此后的英国社会运动中有所延续。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EfNteibgqOXlqzDUNfNEgwiaFgE380DSThCpicybyzH0gn8l98yu9um0dy1IWQcLVJoVWEqhbC65F8Q/640?wx_fmt=png&from=appmsg)

---

> 论文：https://arxiv.org/pdf/2502.12115

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