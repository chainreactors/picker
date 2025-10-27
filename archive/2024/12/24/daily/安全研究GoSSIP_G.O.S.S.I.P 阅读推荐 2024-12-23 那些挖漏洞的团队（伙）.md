---
title: G.O.S.S.I.P 阅读推荐 2024-12-23 那些挖漏洞的团队（伙）
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499471&idx=1&sn=6b9864c7e3748af4d5599a55b0b6014f&chksm=c063d016f7145900a49ddbaa4bcb1884049b8265f5cfa44eaffefb88d4af6a19080043ba5a8a&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-12-24
fetch_date: 2025-10-06T19:40:52.203813
---

# G.O.S.S.I.P 阅读推荐 2024-12-23 那些挖漏洞的团队（伙）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2lSLdThzDXSfRpjOqHObkjciaBKgWAKia6Rqs4QrJvxicwdXwW4UAkJOPQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-12-23 那些挖漏洞的团队（伙）

原创

G.O.S.S.I.P

安全研究GoSSIP

今天介绍的这篇IEEE S&P 2025论文*Study Club, Labor Union or Start-Up? Characterizing Teams and Collaboration in the Bug Bounty Ecosystem*关注的是我国的安全漏洞挖掘团队的生存状况：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia272T87PiaWibAnUXEkAy5QEnnVR2n6sxuGuUvY82lMmHHtdVv0b818o2Q/640?wx_fmt=png&from=appmsg)

今天的黑客对bug bounty program（BBP）已经完全不陌生了，不过你知道世界上第一个bug bounty program是哪一年针对哪个软件发布的吗？人生天地之间，若白驹之过隙，忽然而已。经过了多年的发展，现在大公司已经把发布BBP当成了安全标准配置，而黑客也不再奉行单打独斗的原则，转而进入到集团军作战模式，成立了bug hunting team，在团队中发光发热。不过对于漏洞赏金猎人（bug hunter）而言，为何要加入漏洞挖掘团队，或者说什么时候加入团队，团队有什么吸引力，这些一直是吸引外界关注的问题。今天的论文，我们就带大家去探索神秘的黑客团队（欢迎收看CCTV-10，注意今天的论文主要关注的是国内的黑客团队哦）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2AUicOA4MnrAFUAUlibrBicKOmQItVBda376NX1ibaX4JYCSrGPC3MJB9LQ/640?wx_fmt=png&from=appmsg)

作者首先就抛出了三个问题（如上），关于第一个问题，一些基本的结论就已经很吸引人关注了：首先，在漏洞赏金猎人圈，大概一半（46%）的黑客都是抱团作战，这个的回报则是比单兵作战（solo）要提升了差不多一倍的挖洞效率。其次，尽管大部分团队（87%）的成员都不到10人，但是有一些超级团队人员众多，在社区也很有影响力，作者了解到的最大的团队甚至拥有超过500名成员，他们给超过60个不同的BBP贡献漏洞，已经赶上一个中等规模的公司了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2oBkpnUFD01m0ZdGYTvh4mbxLiczbI7HjoNvribAicuhFoFlZ7ll7mhTSQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2FdIojQ6d8yZFhpQqDyibibaGWpaQs75C7AzOJpm79RDe8L0Xls5cAOOQ/640?wx_fmt=png&from=appmsg)

关于作者怎么做调查，估计大家都不太关心，有兴趣的读者可以去读论文原文，我们就挑一些结论来介绍。首先是关于生产力的调研，作者发现，那些以集体方式在各家SRC提交漏洞的团队，平均每个成员的贡献是单兵作战的黑客的两倍。当然你不能根据这个直接得出什么因果性推论，比如黑客组团就能提高水平，也许先是因为水平高了以后，再有什么因素让组团变得更有吸引力？所以作者还进行了更多的深入挖掘，采访了18位相关的黑客：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2UAlAFAXTREkxOicD84wJzib7GNib6s52UWlu1lhuAVkHPX8WyPZplpsIw/640?wx_fmt=png&from=appmsg)

首先作者观察到，SRC好像也比较喜欢鼓励漏洞挖掘的团队来提交漏洞，甚至会在特定时期提供额外的团队奖励，当然组成团队还可以去参加一些比赛啊活动啊之类的。总之就是组队可以获得很多激励，所以大家似乎也愿意去组队。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2GwwTXjzpXjbQ6oNib0HVeNpxUHmyQiaeWiclDv5DeLBKYB7X5exeSebHQ/640?wx_fmt=png&from=appmsg)

从被采访的黑客的调查来看，组团刷漏洞都可以养活自己，大家都会去各个SRC去赚钱，有人甚至会加入不同的团队：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2dvHCynCGoZwK68J6Pxgs6jErysAmWJdBYayjpXwibgUWD0pQC6y9eUw/640?wx_fmt=png&from=appmsg)

当然，很多漏洞挖掘团队都有自己的运营，很多受采访的漏洞赏金猎人提到，在团队里面，学习气氛很好，大家都是和我年纪差不多的，说话又好听 没有什么看不起大家的技术超人，在一起进步很开心。而且在一个团队里面，有很多资源、情报、工具可以分享，这些都是对于技术狗来说无价的财富。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2LCOE2mzU5WDv4r37EH5wPpvticO5ibIs8BX0RnOGADnnuI6U9wjiap29w/640?wx_fmt=png&from=appmsg)

从某种程度来说，漏洞挖掘团队也可以算是一种工会形式，抱团赚取impact，以后可以换得更好的回报：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2X4ISzgQScqe8D2VBJoQFJtgEfQDxUicLBJazULlIfTjGEK9bb5ewB8Q/640?wx_fmt=png&from=appmsg)

更重要的是，组织在一起可以防止SRC故意压价：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2jRC4vVfibYxQdRpAMSYAI5Csdfd8D1xm6RYkB9yrwDzB5DbibeUtOHPA/640?wx_fmt=png&from=appmsg)

对于那些做得很大的漏洞挖掘团队，大家也会关心他们是否考虑做大做强，再创辉煌？不过谈到是否转为商业化运作时，有些人会比较理想化，在这个资本作祟的时代，精神可嘉：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2hXUgoaQicye2Ihia2WPlyzd8UYdsyoKhFMuXGrQBs3yCd7SRXklvULag/640?wx_fmt=png&from=appmsg)

当然也有黑客谨慎地表达了对商业运作存在能力不足的担忧 —— what we have is merely trust

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia2DSribGkfOXaHrFlcf95BdEjKRyxlsznVyJj0iaHAYw5M1oSsaibTzfDtQ/640?wx_fmt=png&from=appmsg)

实际上漏洞挖掘团队确实属于比较朴素的小团队，如何分配（团队）奖励这个就很ad hoc，有些团队是大家平均分了，有些团队是leader和大家讨论之后case by case来分，甚至还有团队的leader从来不把team reward分给大家！当然每个团队都有一些初级的管理，比如不许搞黑产、鼓励大家分享技术文章以及要求保密等等，有些团队在参加什么SRC的挖洞计划时候也会有所考量。不过很多被采访的黑客表示，这种团队运行方式毕竟不像公司，在内部虽然鼓励合作，但是也有很多人只和团队内部自己认识的朋友合作，甚至有人社恐到加入团队也不和别人合作。

既然是作为松散的团队存在，那么死生存亡其实也是一个问题，既然加入团队有好处，总归也是有坏处的，有些黑客表达了对团队的管理的担忧：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21E2ccbcyYJjTSRzOVjpzmia23lRe8PkdSKuzKRr9p61Mc3S9TvcqicicwBG5F0fdm6ReFt3YBYAIC95A/640?wx_fmt=png&from=appmsg)

当然，更主要的原因可能还是这种没有五险一金的生存方式总归是看天吃饭，饥一顿饱一顿，可能有些黑客甚至是白天打一份工，晚上兼职挖洞，那么在时间压力大到无暇顾及的时候，可能往往就会离开。

---

作者在论文的第7.2章还讨论了漏洞挖掘团队是否会持续存在下去（并发展得更好）的理由，首先作者觉得并不是所有团队都会做大做强，有些小而美的团队虽然和SRC去议价能力不强，但是他们有他们内部更好的沟通优势，同时也有可能在某些技术方面有所专长；其次，关于团队是否能够帮助成员成长，这个其实没有什么很好的方法去评估，直觉上虽然会让人以为加入团队就能增长水平，但是也不排除很多人去团队里面就是抱大腿当南郭先生的；还有一个很重要的点是很多团队也会在共产主义和资本主义之间横跳，团队不赚钱也不行，但是大家聚在一起往往也是只想做一个社区而不是想给谁打工。

总之，漏洞挖掘团队并不是一个中国独有的形式，也许它也不是安全研究人员的终极出路，但是考虑到像《星球大战》、《曼达洛人》等影视作品里面输出的赏金猎人文化影响，以安全漏洞作为研究乐趣并且顺便买车买房也许会长期成为一票生活在网络上的安全研究人员的特殊生存方式。

最后，本文的其余作者也向论文的联合作者、今年去世的Ross Anderson教授致敬：

> We remember Ross Anderson, who passed away during this project. His guidance was priceless; he inspired his fellow authors through his career contributions, and he will be deeply missed.

G.O.S.S.I.P 对本文给出的推荐指数为：

> Accept

---

> 论文：https://www.computer.org/csdl/proceedings-article/sp/2025/223600a020/21B7Qbxu1YQ

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