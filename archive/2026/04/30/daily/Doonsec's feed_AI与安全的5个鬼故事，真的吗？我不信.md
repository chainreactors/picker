---
title: AI与安全的5个鬼故事，真的吗？我不信
url: https://mp.weixin.qq.com/s/USB5VX-QiqrI1mxAkru8Ew
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:34:26.824305
---

# AI与安全的5个鬼故事，真的吗？我不信

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibBmvsrazb5vdA4D95EQxJc1tiawk3cQ0twMPVJOH7522dWLvNkNfBFwaicxThsxBjH4FGgr3CaMwQTaB12MEZeoZQo5VicVH7kkiaFgPH4Tib5QI/0?wx_fmt=jpeg)

# AI与安全的5个鬼故事，真的吗？我不信

原创

晓兵Jason
晓兵Jason

锐安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

《[AI･安全](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxOTk3NTg5OQ==&action=getalbum&album_id=3682648583632404484#wechat_redirect)》栏目文章

左手AI,右手安全

本文5445字，阅读时长约12分钟

**导读**

AI来了，安全真的会黄吗？请听听这五个AI时代的“鬼“故事，前三个关乎AI，后两个关乎安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibBmvsrazb5tdk6ic1a0ugR9pw6mjWrzeaKYYdBT4tib9fnIu24FH8J6Ad9Qj63fm7Lg9tpEc1diarfofQLRIbvQQCHbN9ibBINzCdKnwky4F3ho/640?wx_fmt=png&from=appmsg)

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Eia1pKbzLGbQy8AT6fe7zedEldxnthOTZJo1ATKw6WqE0NAPCQOezkasNWzsEJZmnLbKdbwVO5ia2akicLNsRo9ZA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)**

明天就是五一大假，在这里预祝所有锐友节日快乐！有机会劳动不易，有机会休息更难得。

在上上周三关保联盟的闭门会里，我做了《AI安全范式研究与工程化实践》的分享，其中有五个AI时代的“鬼”故事，特别想拿出来与你分享。

又过了这么久，有些鬼故事可能真的已经成鬼故事了，不信你接着往下看。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibBmvsrazb5suokVI7K1V9w49b12MI5XyFavCyyMEOQZRtUic13J5J3CqHdj6owOsITJBWfrSVngatCbNa9FWwibwm9vL20v0BxHkVnNuO8NyM/640?wx_fmt=jpeg&from=appmsg)

图：现场照片

在讲故事之前，我想先谈两个推论。

---

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Eia1pKbzLGbQy8AT6fe7zedEldxnthOTZLzwH7XKDJoNDtH0E4O9WWF2bSfpe6F08jTxOaUpibTbj6l3bbCvXA6A/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)**AI时代的两个推论**

下图是之前总结的技术文明发展框架，用来快速看清咱们当下的时代处境。

![](https://mmbiz.qpic.cn/mmbiz_png/ibBmvsrazb5vbTAuwWcBmrOLo8qrmleyUZoXOqjHI2XzGiczdM4861zicRKz1pN6VU0Oibtj9yyUFicbNBLNzpa3I96bJzjX7rD6obT5DQlOVw18/640?wx_fmt=png&from=appmsg)

图：技术文明的发展框架

在这个时代框架下，人类协作模式会从农业文明的“布衣”、到工业文明劳动密集型的“蓝领”、到信息文明知识密集型的“白领”，再到数智文明认知密集型的“金领”，即我们今天说的OPC（一个公司）。

从图上看，似乎是时代使然。

**面对今天OPC的巨浪，我相信会有很多OPC出现，但是我特别想问一句：“我们现有的企业会缩小为OPC吗？”**

接着看，这是OpenAI CEO奥特曼总结出来的AGI（通用人工智能）五级量表，这是目前大家公认的AI时代的演进路径。

![](https://mmbiz.qpic.cn/mmbiz_png/ibBmvsrazb5uVp2CCFVxicwg7PO0Tgib8icYLoaicGzZ2FPLyZnXAxbZMmPeaiaKcYl9LRWq3ybhCiagicm7HrLR8mF7CzKhpfW7zyQknepPDC442Lo/640?wx_fmt=png&from=appmsg)

图：AGI五级量表

它告诉我们一个这样的未来：AI会经历聊天机器人（Chatbot）、推理机器人（Reasoner）、智能体（Agent）、创新者（Innovator）与组织者（Organization）五个阶段。

在这里咱们能看到：

* 当AI发展到聊天机器人（Chatbot）阶段时，一个AI就相当于一个客服；
* 当AI发展到推理机器人（Reasoner）阶段时，一个AI就相当于一个专家；
* 当AI发展到智能体（Agent）阶段时，一个AI就相当于一个实习生；
* 当AI发展到创新者时，一个AI就能相当于一个成熟的员工；
* 而当AI发展到组织者时，一个AI相当于一个团队。

按照上图的逻辑，一个AI相当于一个团队这件事也就发生在4年以后，即2030年。

**按照上图的逻辑，4年以后，我们今天的这种大规模协作的公司必然消亡，转而被OPC所替代。**

**上面两张图同时推导出了一个结论，但是在这里我还是想问一句：“你信吗？”**

接下来咱们就聊聊AI时代流行的五个“鬼”故事，你来找找答案。

---

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Eia1pKbzLGbQy8AT6fe7zedEldxnthOTZ8RdnkXrBdia1BdLyGabWdhRKibJJhAmqzuGLL69CZh67WorPK5ctalTA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)**

**AI时代的恐慌**

当AI把人类最后一个精神堡垒“智慧”攻破时，我们就开始恐慌了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibBmvsrazb5t0ibkX43Ik5I5OeYdOxHDafLfNX5KuD6UOZF3VFXU2a2HngibpjDwkTK2Emo7EBNmbbmfOvymt1icjUymHxrUdOVms56EtZS2SE4/640?wx_fmt=png&from=appmsg)

图：DIKW模型

因为我们一直是地球上唯一拥有智慧的灵长类，但当智慧被AI替代的时候，我们的优势生态位没了。

就像当年17岁就排名世界第一的天才围棋手柯洁面对阿尔法狗的那种绝望。

于是产生了五个鬼故事。

![](https://mmbiz.qpic.cn/mmbiz_png/ibBmvsrazb5tn5B75HfPMhoS3anc5vbxjwe3voRTG7rHPG3bo3F0oMtZcqfBoohzypich8qDiaUJn8SvtnRuLAukLmxeCoRNEv70gxqUDmicQes/640?wx_fmt=png&from=appmsg)

图：AI时代的五个“鬼”故事

一、2023年，AI让大家产生了强烈的末世感，于是出现了第一个鬼故事：**AI会产生自我意识并最终消灭人类。**

于是，AI公司火了。

二、2024年，当我们理解了Transformer架构本质之后开始明白AI不会消灭人类了，于是出现了第二个鬼故事：**AI会替代人类工作，人类终将失业**。

还记得吗？那一年最火的金句是：AI不会替代你，但懂AI的人类会替代你。

于是，AI培训火了。

三、2025年，大家突然想明白，懂AI的人类替代你好像也还是漫漫长路，于是大家又提出了第三个故事：AI可以**降本增效促进生产力**。

于是，一人公司火了。

四、而在安全行业，2023-2025这三年，一直在讲一个故事：**AI赋能安全，天下无毒。**

于是，各大安全厂商都下场卷AI了。

五、2026年，随着Claude Code Security、Claude Mythos Preview的陆续发布，给整个安全行业带来了连续的恐慌，于是出现了第五个鬼故事：**AI来了，安全要黄了。**

于是，安全人都慌了。

这五个“鬼”故事到底是不是真的？接下来你就搬个小板凳，听我说。

---

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Eia1pKbzLGbQy8AT6fe7zedEldxnthOTZicRsRUzIMmGS2pufKxbYmuII8YyKRJSFFiczAkLqx0gzBWFagzOpxlQg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

**故事一：AI真的可以产生自我意识消灭人类吗？**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibBmvsrazb5tQaPpCxu2hicfczSNib5pRUMSw5XhIe7FdewibIOOnmIcwAwJmTskHsGYLgiabWdhSsSURcnH3RXRSLW8ATkUD4BJgSibeqVwuhyU4/640?wx_fmt=png&from=appmsg)

图：故事一

2023年，国际上，有1000多位大佬集体签署了一个文件，大意是希望大模型的发展要踩一下刹车，别发展太快了。

直到今天，已经有超过3万人在这个文件上签了名。

国内，有位大佬也几乎产生了这样的恐慌，直到2025年11月的时候，他才把观点修正为：“AI不一定有意识，但它可能会有意志，因为把AI做成智能体后，它有目标驱动、有规划能力、有推理能力，还能调用工具。”

真的吗？我不信。

**我相信：AI既没有意识，也没有意志，它只有意图。因此国际的AI安全厂商，越来越多的在谈“意图安全”。**

咱们再看看第二个故事。

---

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Eia1pKbzLGbQy8AT6fe7zedEldxnthOTZuF5ZaGtL8EWmZAhCkrhxAP6uR427TTGt6t7eYFr5GtnTiblfByIcicWg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

**故事二：AI真的可以替代人类工作吗？**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibBmvsrazb5stMaIlvzEXmQRldqXK2huv3zL5boyOLRKaSArXH5qtDvnqjib9wMEEZJ9phtPNokRib61lOZKbbVrBGm5fSQAlDCyEuJUcCnTew/640?wx_fmt=png&from=appmsg)

图：硅谷鬼故事与职业替代

对于这件事的恐慌，其实源于2026年2月份发布的一份流传很广的报告：《2028年全球智能危机》。

这份报告的核心观点是：AI能力提升→企业裁员→消费萎缩→企业进一步投资AI替代人力。AI发展会形成无刹车的负向循环，引发非传统型经济危机。

由于观点过于刺激，这份报告，也被称为“硅谷鬼故事”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibBmvsrazb5uV79Cec0A48Vq9qIfnk9CKRfII0GDcNkxATJbHq2Z2pOjPPIoUlseG4fQMAOZUibk29RMm11Vdj91T3nlrOickjANO1TtOC4QGY/640?wx_fmt=jpeg&from=appmsg)

图：硅谷鬼故事

真的吗？我不信。

咱们再看一下右侧这个项目，目前它监测了250个职业，颜色越深、AI的影响面就越大。

目前它的影响面是：

* 按影响等级分布，受AI极高影响的有5285万人，占总人口的7%;
* 按薪资水平来看，20万以上年薪的人受影响最大；
* 按学历水平来看，硕士及以上学历者影响最大。

站在全局视角来看，这个风险面不小，但可控。

因为AI对人类除了“负面影响”，同时还会有“正面影响”。就像“奥本海默”时刻，一面是原子弹巨大的破坏力，另一面就是原子能巨大的科技价值。

这就像凡人修仙，当你马上就要突破筑基期时，多苦也会忍一下。

所以，面对AI浪潮，没人愿意踩刹车。

---

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Eia1pKbzLGbQy8AT6fe7zedEldxnthOTZwIKroNq5fSJMq2Uic6Ih1UsqScXgRia8ucsiaq2xlFndw6KkhadpIRBRw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

**故事三：AI真的可以降本增效吗？**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibBmvsrazb5tqibDaIFc2a8GsiblicYFP6ib4fMF2DgiaqXiaaRnkjOHqC678cicdkXdyVibWy52B6GIgmbT65qfbLZcuX5xtLOmUnEPJOzmsXXcO5OY/640?wx_fmt=png&from=appmsg)

图：商业通识与需求膨胀

上面主图是《刘润商业通识30讲》里的一个商业进化模型。

它的主要意思是说：商业的本质就是交换，而交换依赖人与人之间的连接，不同的连接方式，就会产生不同的交易成本。

原始社会大家几乎是无连接的，只能是靠山吃山、靠水吃水的离散状态。

小农经济时代，男耕女织，形成了一种小闭环连接。

再往下发展，开始形成线段型商业。中国的丝绸可以卖到欧洲，它源于空间的折叠，即航运的发展。

再往后，形成了中心化商业，大型商超就起来了。而互联网的出现，就是通过降低交易成本的方式从“中心化”的商业群落里，演变出了“去中心化”的社群经济和小众经济。

最终整个商业会发展成“全连接”模式，即每个人的需求都能充分被满足。

这个全连接的构想特别符合我们对OPC的想象：每个人都成为公司的老板，为别人提供服务。

而几乎所有人都相信，AI可以让这个进程大大加速。

真的吗？我不信。

**先说降本。**

关于AI工具的使用大家已经形成了一个行业共识：**水平越高的人，AI才能用得越好。**

因此，用AI确实可以省人工，但未必真的能降本，因为你需要找到每个领域里使用AI工具好且牛的人，这个成本不会低。

**再说增效。**

目前人类编程的平均水平是日薪1500元，能产生100行有效代码，平均每行代码15元。

AI编程是日消费Token 1500元，能产生2000行有效代码，平均每行代码成本是1.3元，编程效能确实提高了10倍。

但是，接下会发生两件事情：

一是当你的代码成本变低时，客户同时也会压低你最终产品的销售价格，导致你虽然“降本”，但是并不能“增效”。或者说，虽然可以“降本增效”，但未必能“增收。”

二是AI编程成本只占整个研发成本的30%，而整个研发成本只占整个公司成本的30%，也就是说，AI编程10倍的增效，放大到整个公司来看，也就是10%的增效。

从研发角度来看，AI for Codeing、AI for Testing、AI for Designing，这三项的效能是梯度下降的。

从职业替代的角度来看，AI除了编程、翻译、法律、公文、标准文档撰写这几类不依赖“人味”和“品味”的工作能完美替代外，AI对其它工作的赋能效果还不会有那么明显。

就像有位技术大牛说：“AI编程，虽然省脑子了，但是费眼睛。”

从公司发展趋势的角度来看，商业发展受连接节点、连接效率、交易成本、信用传递等因素的影响，很难靠AI把整个商业连接模式变成全连接的模式。

OPC（一个公司）最大的障碍是无法把信用传递出去，导致交易成本反而变高。

在这里，锐安全想提出一个反常识的观点：**当“AI工具”产生生产力提升之后，人类的需求同时也会随着欲望的驱使，膨胀得更厉害。**

原因很简单：电影工业为什么会从一人一台摄像机的简单形态，发展成数千人协作的复杂组织形态？因为技术发展了，我们对视听的欲望也同时膨胀了。

我相信，当我们软件工程能力提升十倍时，客户对软件呈现效果的需求会增加百倍。

我同时相信，一个人用AI，一定没有十个人用AI产生的价值更高。

就拿视频制作来说：编剧、脚本、分镜、音乐、视频、剪辑每个环节都有一个专人用AI来辅助工作做出来的作品，是不是一定比一个导演用10个AI做出的作品更优质？

再进一步讲，一个团队用10万块钱制作出来的AI视频效果已经很好了，但是如果花100万是不是一定效果会更好？

所以，AI视频的制作成本会在短暂下降之后，继续攀升，很快会发展到继续拼成本。

只不过有一点我是信的：AI演员一定会挤压人类演员的生存空间，但不会无限挤压。

因为当AI电影占比超过一半时，人类电影就会成为小众电影从而变得稀缺，然后再次出现溢价。

软件也是这样，我们原来三千行代码就能解决的问题，后来会变成三万行，到了现在，谷歌浏览器的代码行数已经超过了4000万行。

是我们十年前用的浏览器软件不能上网冲浪吗？

不是，是因为十年前的浏览器不能满足我们现在对复杂交互的欲望。

那我们现在拥有了这样的复杂交互，就会是终点吗？我想同样也不会是。

关于OPC，我的看法是：只要需求的膨胀是无限的，那么公司的规模就不可能退化为OPC，只是短期来看，公司的规模会缩小。

接下来的两个“鬼”故事，是专属于安全行业的，你也可以来听听。

---

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Eia1pKbzLGbQy8AT6fe7zedEldxnthOTZyWSuiaYo4n79Hpjy6iaOSPgNQ7vLKkyhp3bvqmMibiclAiarGO9T8BOTznA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

**故事四： AI真的可以赋能安全吗？**

你看，2023年，大家认为AI可以搞定安全的十二件事儿。

![](https://mmbiz.qpic.cn/mmbiz_png/ibBmvsrazb5um...