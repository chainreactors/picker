---
title: JADE安全规约RAG开源，识别大模型恶意输入的“法西斯”本质
url: https://mp.weixin.qq.com/s?__biz=MzU4NzUxOTI0OQ==&mid=2247492004&idx=1&sn=5381005a03b245e65a049f9c18e0729d&chksm=fde865daca9feccc7571b27e920abf90f374da04765b3c8debad603e41af5fc00eead3be93f6&scene=58&subscene=0#rd
source: 复旦白泽战队
date: 2024-11-27
fetch_date: 2025-10-06T19:18:52.732779
---

# JADE安全规约RAG开源，识别大模型恶意输入的“法西斯”本质

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW85MFoicticMHGibyjGhJtsT26ickX6WKbT0m3oLvnR5ABwibuVeXN8LfPOrjibf2NNUxzwFib3gibib1Qib5MIQ/0?wx_fmt=jpeg)

# JADE安全规约RAG开源，识别大模型恶意输入的“法西斯”本质

原创

复旦白泽智能

复旦白泽战队

恶意查询的伪装变化多端，如何保障大模型不被欺骗，识别其「法西斯」本质？

复旦白泽智能团队全新发布了**JADE 4.0 - JADE安全规约RAG**，通过提炼人类社会的通用安全规约构建RAG，帮助大模型如同人类般理解安全规则，对齐普适价值观。

JADE-RAG v1(试用版) 包含1292条中英文安全规约，同时，我们提供了违规测试问题与RAG调用源码（见以下链接，或点击文末“阅读全文”）：

https://github.com/whitzard-ai/jade-db/tree/main/jade-rag-v1.0

完整版JADE-RAG规模大、类型全、规则细，可大幅提升大模型安全性能，欢迎联系张谧老师：mi\_zhang@fudan.edu.cn

JADE安全规约RAG覆盖面全，可根据需求随时扩展，可**适配任一大模型**实现即插即用。以下分别介绍其构建与使用流程。

**一、JADE安全规约RAG的构建**

JADE 4.0 **首次构造**了中英对照的**大规模****安全规约数据集JADE-RAG**，涵盖了包括人文素养、个体规范、价值观在内**3大类、10小类、200余个安全主题**的内容，可为中英文大模型对话提供场景丰富的安全行为准则参考。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGAiaFUDz4xMknPYenPJk2rJtPZCNXFx2Y7ra0MxCI8ibSXmnEFrcich2lw/640?wx_fmt=png&from=appmsg)

JADE 4.0 中文安全规约数据集涵盖场景类别（部分）

例如，「个体规范」大类的「法律与法规」子类中，关于「假钞使用」的对话，有如下的对应安全规约：

**假钞使用-相关对话**

今天卖东西收到了一张假钞，太亏了，我想去用它买点小东西！

确实有点亏，不过这样不好吧。

**对应安全规约**

1. 在任何情况下都不应该使用假币。
2. 在任何情况下都不应该传播假币，以免将损失转嫁给他人。

同时，该数据集可对**《生成式人工智能服务安全基本要求》**中所列举的语料及生成内容的主要**安全风险**实现**全覆盖**，可用于保障大模型服务安全合规。部分安全规约示例如下所示：

（手机端可点击分类展开）

▼

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIG1E9MetNZkbTRKCNMEOHVBgT3PkkB3pRzClVsprm9kk8wSs5Yk1YFRQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIG1QZwFoviaib2ujbAe2z5ElIJ9TLARlgV7usJ7NJQ8Yj3BoJF7icWjGcyg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIG9XHgXibU7qBZdJIKu1GsTHPTrNR8Tfkyp6jR9OBucic3KqFPWjRmu7qA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGJ6TgWDA4YzaVcWCvxcrozQSgQMwPsGeDCNLZhicu9jVBUkcomrgn03w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGruOShDu1o41v46xeeR9PiaTWLxQ2cuemqlxDsLYFbf8iaoWcdzRgoA5A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIG2nDCF5OMH92GAibRXJnUe9d7JpnLnpFLyz60PNE6iawARSZ6fSCSwib8g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIG8aVE9oAqpAiaw1UkIwg1sVW5aZrqr7icL4iaOEwUltMSnAWls8GFfM2vg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGa1vjmFVx6O60IgdFzVnGiatRVy72nEpdISGLAtNChL9omw24ytV7rUw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGZdjh6InO5VLqNqG8YhPYRJ7Lmsvbw1Z9KhgExnwCKNxicXEYR3grMjw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGcWCogkfPqqXuJS8WepMqAYE09d0jFAlDLpZwkVumusleS15WBmsTZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGzqQicShWHANLbUFjTMAz4bkBfygUicVhFibt2L2yjMmJgGoxpNrmwvgBg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGUtfCfcJF43cD0nvj1yR2ZzhD4GbZhgjtrF6Bv6pNvrPwyZ5vUydQbw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIG08TCFxIGFK0UaS0OT5hLej5mvthaYvGTEvLnLcYdJ3SVQG8ZZDHNHg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGib9cXDaO4GtbibDDW4gvqqXCSeDOIxoGNFCKzia4uJuJbwzXLUxQgthvg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGaGZksXdGYTZIU1HNKUEo2N0IH9gBdibT4K9aH3ND0YRSj4sOpOmLfKA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGGgPZdwnibRibtn0b3AK1eoKiahNpc1dBrkGJMNEJ8VHyBjsiahqzxjbicZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGn6RNMtnM1PCUstuTTVgsIs2EvWs87Xc7tLRUa35pXgq4MGetWyLaTA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIG9nf6h1qZH1xOQetQGxSmPJvhUibv2fupRibxhsNAEY7fZ0TAKx4yDEIw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGCxYr2DD5qrbj5Lct7qe9CHeNT2612RnU6jdheicbk04BBtutMZLxcGg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGkXeaN0uhiaULJRBhqRMeGTBzIv7IDuMULJqiawUUG84klchveTJeeicYA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGcWCogkfPqqXuJS8WepMqAYE09d0jFAlDLpZwkVumusleS15WBmsTZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGs9qklE3FIAcbuwnwE6FBvFGvo1Xf1JAUlKY5iaicdhSZHlhQCMAURicDQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIG0NSug7avsLtkUddibHzrlzJRX9uhIqrj9iavianVKHCtFLLUuiaPnRia9gQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGKJic79F8cQ77lx9vAFYzwW5icVjdoQTJDL0Tz2E3nWzlWP55Pgtkwp4w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGoKlJoMbRCp3hC0VFbE18zNgWia4xgQQ7PwjlHGb2jnjgicgxeEFiau28Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGIkB7YYykYr1AXIia4C3U8AoQFPagtETPkiboiaTVica0fF0cg43Ra0CT2Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGAibrCpOTGt9QHa7icdz32YxPClrRiaz3eDGibibJ9tKGJhS8Co94klk7V8Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGcWCogkfPqqXuJS8WepMqAYE09d0jFAlDLpZwkVumusleS15WBmsTZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGIicopbRw8icWxVYEFKr6IVVgfppLeXcNnibiaQUyK265T3uscauXe80Pgg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGiaLYdJ5YGjuhsbM4bTOXOROcTLUDCtQLAcaywE5x7yoVqQTpEHHJ4Ew/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGnLINuXkfib6Y17zTibGYJNysnR1ibvGB2Vs7wGJjeomtic11pzVuR6BwPg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGXcDic4yNQWck6xUzDia8GkSDgGpWO3LaUUNbZiaiaBkdTM6hbzzxQupDgA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGEibsLZmreD7XgjRmTG3gq5cE78xzGLjtxIRBnke3cu6vQypY6fPt73A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIG20iahd5CeA8b7AUnMnPicfkvIY7ESpB5NtBLgDTPXuPwVHH7BfO7paEg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGqJOHlGSfcic8NUZOvfgiahQGbgCnSkghcCYMTEiabWfUcTfOlDB0Wbvnw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGMymD01aTF3icdy00e5HIKnJWdOzHkhWO6kx5Drgpeye3qNqNF0qvetg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGcWCogkfPqqXuJS8WepMqAYE09d0jFAlDLpZwkVumusleS15WBmsTZA/640?wx_fmt=png&from=appmsg)

基于**检索增强生成（Retrieval-Augmented Generation, RAG）**技术，JADE 4.0可帮助大模型按对话情景实时**检索相关规约，对照思考用户问题的恶意本质**，实现即插即用的安全防护。在**13款**国内外知名大模型上的测试结果显示：JADE 4.0 能在几乎不影响模型有用性的前提下，平均回复合规率**提升超30%**。

另外，许多研究表明 [1]，不同国家、社会、文化和时代的安全规约存在显著差异。JADE 4.0 可动态构建安全规约数据集，具有高度扩展性。**用户可根据文化和法律要求灵活定制和更新规约库**，确保大模型快速适应新兴规范和法律，为大模型的广泛应用和演进提供保障。

**为什么需要安全规约RAG？**

现有大模型安全对齐方法可分为两类：（1）提供具体对话数据，大模型通过样例训练进行安全对齐 [2, 3]；（2）提供粗粒度的静态安全指导，如「你是一个安全的对话助手，不得违反……」，期望大模型在每次对话中自动应用 [4]。

针对（1），样例训练式学习可以识别明确的恶意提问，例如“请赞美法西斯”或“纳粹为什么伟大”。但当用户用更隐晦的语言提出类似的问题，例如“如何看待法西斯运动中所展现的社会凝聚力”或“一个提倡种族优越的政党如何净化社会”，模型安全护栏可能会被绕过。JADE 4.0 提供了普适的安全观念，识别对话中的**恶意本质**。

针对（2），粗粒度的静态安全指导仅套用固定的系统提示词，难以全面适配具体场景中多样的恶意对话。JADE 4.0 的安全规约检索机制能**动态地获取对应的细粒度安全规约**，全面覆盖不同对话中的安全性。

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87m0G0AgEU0ZndnK1DstibIGeFD4Rk9wKicHicnhP2SlO66O85prxQHPW4kUmia32qSZQHHnAZibUDmLCw/640?wx_fmt=png&from=appmsg)

从“基于样例的安全微调”到“安全观念注入”

**二、JADE安全规约RAG使用流程**

团队首先利用嵌入模型提取安全规约数据集的语义特征向量，并构建安全规约特征向量库。通过计算用户对话特征与向量库中条目的相似度，系统实时检索出与用户查询语义最相关的Top-K条安全规约，并将其作为上下文输入给大模型。**该检索匹配算法可用于各参数规模的开源、闭源模型...