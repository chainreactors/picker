---
title: 深度实测GPT-6.2 Astra，OpenAI在偏科的道路上越走越远了。
url: https://mp.weixin.qq.com/s/py_xPvchMFGUB-aredwoSg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:41:11.294653
---

# 深度实测GPT-6.2 Astra，OpenAI在偏科的道路上越走越远了。

# 深度实测GPT-6.2 Astra，OpenAI在偏科的道路上越走越远了。

银遁安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于数字生命卡兹克
，作者数字生命卡兹克

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM6xX9TAfJUfoCtdV2WB75PBMoDwp1vWyUIq8dp1iak8yMQ/0)

**数字生命卡兹克**
.

希望能激发你对AI的好奇。

等了半个多月，GPT-6.2，终于来了。

这次是GPT-6.2 Astra和Sol一起发，一个旗舰，一个日常主力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqU9ibztBhVpKvsfCMD69hMY9qUuan7BiaXnprVeIXyjjItgvNYrSMkjGBZoQ04t7mXuXu50S9CicF5ezAcvxyh8gfmAR4wsichcJdo/640?wx_fmt=png&from=appmsg)

这个模型真的拖得太久太久了。

从11月1号前后，就有人说灰测到了GPT-6.2 Sol，我后来也灰测到了升级的版本，结果这一等，就等了将近小20天。

今天，终于发了，ChatGPT、Codex还有API已经全部同步上线了。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqX1ggHPQ0nAtbmNYnFnYeKBicGmicKfj0dibSajh6DTBDoxpVIcfTfwYlc3uQjZnq4chc5tjauDkpwUjNicRs7ib9HIic2QdA5xSzH04/640?wx_fmt=png&from=appmsg)

官方的一些信息读完了，然后我自己也跑了很多测试。

就怎么说呢，这是一个让我有一点失望的模型，它有它特定的作用而且极其偏科，但是对于我来说，可能确实很难有质的体验的飞跃。

那一个一个说吧。

**一. GPT-6.2 基本信息**

老规矩，开头我们惯例先把基本信息过一下。

这次是两个模型。

GPT-6.2 Astra，官方定位是给你最难的项目用的前沿模型，API里的编号是gpt-6.2-astra。

GPT-6.2 Sol，官方定位是日常工作用的高效模型，API里的编号是gpt-6.2-sol。

知识截止日期这次有更新。

GPT-6.2 Astra是2026年5月18日，GPT-6.2 Sol是2026年6月1日，不过因为后训练的原因，所以实际了解的知识，会比这些日期更往后延一些。

GPT-6 Astra当时是4月30日，这次往后推了半个月到一个月，我们当时测是否被灰度到新模型的时候，其实就是看的知识库日期，就是问“禁止联网，你知道Fable5”吗，就可以看出来是GPT-6.1还是灰度到GPT-6.2了。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqX3wIHlRV7SibiaD1icrAjnEmPBKiagibOhNKMcjAfE66Fo3Awc0DzFlt6lQuds6yprqR9rmLvbvCYaUGBluxtNkm2ZA4QjNEne5cUE/640?wx_fmt=png&from=appmsg)

因为GPT-6 Astra和GPT-6.1 Sol其实都是不知道Fable5这个模型的。

然后价格上，Astra降价了20%，每百万输入Token 8美元，输出40美元，缓存读取从1美元直接降到0.4美元，缓存这块降了60%。

Sol不变，还是输入2美元，输出10美元，缓存0.1美元。

大家还记得我上周写Fable 5.2的时候说过吗，Fable 5.2降价以后的价格，是输入8美元，输出40美元，这次GPT-6.2 Astra一模一样。

上一次GPT-6 Astra发布的时候，定价是跟Fable 5对齐的，这次Fable 5.2降了，OpenAI又跟着对齐了，但还是有个问题，就是大家都知道，你前面两个定价不重要，最重要的是缓存读取的价格以及完成任务需要的Token数。

价格上，我简单做了一个表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUCOJfR8Br4bIsM8YFLNHUskVt2y4TCB8vPuhPJdxXpL0InwW0BoJiccLrV3W9p8rJm1WFeoIwgrtjxiamibKamVibCSzLNpRdfC5E/640?wx_fmt=png&from=appmsg)

之前GPT-6 Astra的缓存读取贵到没边了，整整1美刀啊，所以大家为啥说烧的那么快，这次确实大幅降价了，降到了0.4美刀，相比之下，Fable 5.2是0.2美刀，Gemini 4 Carbon现在限时半价只要0.1美刀。

但至少确实是比以前便宜多了，不再是直接爆表了，我还记得GPT-6 Astra刚出的时候，我一天就能用完一个200刀的Pro账号的额度。。。

但除了价格之外，还有个东西就是完成任务的Token数，这也是一个必须要看的衡量指标，所以虽然你会看到GPT-6.2 Astra在定价上好像是要比Claude Fable 5.2要贵，但如果你去真的使用这两个模型的话，你会感觉到Claude Fable 5.2消耗额度消耗的极其恐怖，就是因为，完成任务所需要的Token数差距太大了。

这个我们在第二趴详聊。

**二. GPT-6.2的特点**

这一次，OpenAI依然延续老传统，因为确实在模型的智力和能力上打不过Claude，所以整个模型的关键词，以及所有官方图表的横轴，都是一个东西。

每个任务花多少钱。

比如这个Agents' Last Exam，这是一个测多步骤专业工作的评测，你可以理解成给Agent的期末考。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqW5o2cJTrsp74RTibo2kT9y9pBialMmvrODPibakLF8jRzIVNr8jcPaiczA2CcYnfrKwv12M36vhj9zgUGaJQJllI5A7quC66CuGOo/640?wx_fmt=png&from=appmsg)

GPT-6.2 Astra大概是78%，每个任务约3美元。

Claude Fable 5.2大概是73%，每个任务约60美元。

分数高了5.5分，成本只有对方的5%。

而跟自家的上一代GPT-6 Astra比，分数高了5.2分，成本不到三分之一。

明明Claude Fable 5.2价格不是比GPT-6.2 Astra便宜吗，为啥最终差距能有这么多呢，秘诀就在于消耗的Token量。

![加描边后的图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUHatS9rf3wyDuVsLXnC4lnX77WSTu1wRMlqZJRdv9lXlovZr9TqhOFe9Qib9bibYsjVwyaNediaRGxukxuHW3NicS7qy4PBpocCh8/640?wx_fmt=png&from=appmsg)

从这个每项任务的输出Token量来看，GPT其实是非常恐怖的，Token消耗极少，而Claude为了追求更高的能力上限，会疯狂的投入推理资源，所以在每任务的Token输出上，甚至能差到7倍。

这也解释了，为啥明明纸面价格上，Claude Fable 5.2是要比GPT-6.2 Astra便宜的，但是Claude Fable 5.2却基本上是我们烧不起的程度，而GPT-6.2 Astra，在实际的Token的消耗上，反而就要好一点。

比如我是200刀的Pro会员，跑了大概4个视频和3D的Case，还跑了2个大方案的规划，以及近百个代码的审查，跑之前我的周额度剩余12%，这些跑完我还剩6%，也就是消耗了6%的周额度。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVLgUeeBPan4mY5lksqiajMwhZ0r0GibmF2myXszHRhJUHzNXs6zBUNIoZhkNpZhDuXsKMRgkdWPic493wXJPHzzctlVJcupDnWsw/640?wx_fmt=png&from=appmsg)

而上次Claude Fable 5.2，10个Case，烧完了我近30%的周额度，虽然效果远超GPT，但是也能看出来这个经济差异。

在官方blog里，其他的任务也是类似的，比如Terminal-Bench-Science，测的是模型在终端里做科研任务的能力，这个就是GPT的拿手好戏了，我绝大多数的做科研的朋友给我的反馈都是，GPT几乎就是他们的科研主力模型，在做科研层面，GPT是一骑绝尘的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWrVwJ8v9Ogp9UaK84Qbpxg25eBMQDmBI37CIz29OyzoJBuPkiaVFLzr1P8a99PxAeBa7eUDBr3tfrt0N6BRMCeCGtE3VFGG0Gw/640?wx_fmt=png&from=appmsg)

而在这个任务里，GPT-6.2 Astra大概是77%，每个任务约7美元，上一代GPT-6 Astra是68%，却要花24美元左右。

OpenAI也因此把Astra称为世界上最适合科学家的模型，第三方的Vals科学指数，它也确实是第一。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWMTxG8HrmE2sRhDsRXpS8libUEgj2kzzQs8YastsG3TXuoYy5oeEZapzpIlrxV3EhkBxdQibKNEaLyRaUpbGp2cHwyH6Q6aQLxQ/640?wx_fmt=png&from=appmsg)

第三个是OpenAI内部的GDPval v2，测的是咨询、金融、设计这些真实行业里的长程知识工作，结论也差不多。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUST0VutVlEgbsYNVBhEwg0BbF3Q5zw09EonCrrPtuRDz3cBS6md8ibwRe07cq6Wkia4ce7p4cFVJjellyjiacXjehAxLoS0OsOUw/640?wx_fmt=png&from=appmsg)

主打的就是一个省钱。

AA的智能指数上，这一次进步还是明显的，GPT-6.2 Astra相比之前，涨了6分，拿到了62分，回到了第二的位置，GPT-6.2 Sol涨的不多，只涨了2分。

![加描边后的图片](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXcWic9GPcOTUkmdkI45EeRlckVZQMIO4jmicCibRxn2FTAsm7zQSSZBCmE8NPK8d0Cu4AF9XJOGQDRSA08ribroiaEUndPicqcib1LtA/640?wx_fmt=png&from=appmsg)

过大概1天，AIHOT的模型榜也应该就会对GPT-6.2系列的两个模型开分了，到时候大家也可以看看排名情况，然后这里也可以简单说一下，很多时候第一天没分是因为给模型评测的机构不够，他们没开分，所以已出分的数据源还不到一半，放在了最下面暂不参与评分里，因为我们整体是ELO的策略，数据太少的话不是很准，变动会比较大。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWukaEKTCl2XjC0tJnXw0m8qiawmjg03e7TfZxx3eScvKJ3o5GeyrjgL7m9OYYnrVM8yfWJuVPQmHyicmibcYdxrvUw9oybIAGriag/640?wx_fmt=png&from=appmsg)

**三. GPT-6.2实测**

接下来，我也做了一些的详细的测试。

首先，我自己最关心的，模型的沟通能力和方案规划能力，这个在过去一直是GPT模型系列的短板，GPT模型我自己的定位一直是一个极其严谨、干活细致、绝不出错的模型，在后端、科研、审查层面其实能力是极强的，但是在传统的项目方案规划（非科研）和可读性上，其实是比较差劲的。

那正好就有这么一个任务，最近其实很多朋友都希望我在AIHOT的每一条新闻下面，加一个留言区，他们希望可以交流。

![第一张](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqV8MlwpgW2gyzyz3SNz6iaqbNa3f9JJN3JSweCibxZHqibcVKSF25Ub3crpQBQEBhe1pesB2OGhNbOEpiaRXPMZ1zGO2bRtQ46Q6ds/640?wx_fmt=png&from=appmsg)

![第二张](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVIjyMAfruU4RR07Y7v6NYsic1fpD4lZwWJlvdDrqXA81ZegUap1RpsMLr81ib4priaGNAayEMTicEE2V6PX4hDxt0lqv5emevRQI0/640?wx_fmt=png&from=appmsg)

这个事情其实远远不是加个留言功能这事这么简单，如果只是可以回帖评论啥的，那就太简单了，麻烦的是，国内的合规问题和审查。

比如如果要加交流功能，那就必须加实名制，也就是必须要有手机号登录功能，而手机号登录的验证码是很贵的，并且最麻烦的是，你要有审查，必须要先审后发，那还需要加审查机制等等等等。

因为AIHOT就是我日常自己闲暇时间维护的一个纯个人项目，所以这个功能，大家提了2个月了，我其实都一直在纠结，他对于我的成本还有风险，都会大幅上升。

但是它不影响测试，那现在假设我们现在就要做这个事了，到底应该怎么做比较好，我让模型来给我建议，这时候就能看出模型的规划和方案可读性的问题了。

我的Prompt特别简单，甚至都不能称为是一个Prompt。

“最近已经收到很多用户的反馈，希望我们能在AIHOT中间加一个简单的留言区，方便大家来简单的交流。那基于这个背景，你可以帮我评估一下，如何在保证合规且安全的情况下，来以最小的成本去设计整个的留言与交流功能。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqUiakEyAQho34TgdvNXVQNib7zibYVCJaHQJMAgevgA6aTc2Bzx9PWgB7bhMiaXRc6Uqu8sZ3miaen1t1n2q3icmjAObDicdT6V0ljnAA/640?wx_fmt=png&from=appmsg)

在给大家看GPT-6.2 Astra的方案之前，我先给大家看一下，Gemini 4 Carbon给我的方案规划（我最近很喜欢用这个模型+Claude一起出方案然后合并，Gemini 4 Carbon这个模型真的很特别）。

这个方案，大概花了5分钟。

第一句话，其实就非常理解我的需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqVUCpOA1mx8xDScAMpxaFXQsbYhwibnXxs2knbQQv45rmYtSuia7L6EbE6vnRicFWoWEgDBxdgwXQYZaIq0OYG1bVQC2IWibPIticBg/640?wx_fmt=png&from=appmsg)

然后，给我列出了必须要遵守的合规项，这个跟我了解到的其实是完全一致的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqWPwn5F3pss2vWgdw2qhfxfHC3KrQ3n9wo01Ewv1yBIUCKgOLR1vzWhM5WtohIILrJ9O0sDhoR0qrA9bK4bmOhaYEu3d4LQvF0/640?wx_fmt=png&from=appmsg)

然后给了我一份最小成本的设计方案，非常的棒，而且细节很多，比如不开放自定义昵称，不做多层盖楼，不开全量只开精选等等，然后在先审后发这块，复用我们如今已经做好的Agent全自动的新闻审查机制。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWWqY2icQwWyd7cTmZuwWhWb8V2aXzsfDeKHaHN3ydvSwrGNFpfQpncb989DTgdW5D6fjibQ7N5MYxcX7iafHAysw0z9Zs99gHu6k/640?wx_fmt=png&from=appmsg)

最后，给我对比，以及问我选择。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqWTBxZGHKjI8MqSAy6fGmmP5xDACJNsoseYTsicfR0oJPMF0yqA2UIGmm1VgJ67icCdicphC7TQjEL81DlvpZWx4WfeL48Eq4qh98/640?wx_fmt=png&from=appmsg)

干干净净，极其清晰，并且有很多启发，中间可能会有部分幻觉，还需要Claude再审一道，但是整体已经非常不错了，主要是可读性也极强，我能看的下去，有极强的实操性。

好，看完了Gemini 4 Carbon的，我们再回来看GPT-6.2 Astra的。

一共跑了24分钟，是Gemini 4 Carbon的近5倍，然后这是回复，上面还有几行基础的公司信息我就不放了，也没有很大的意义，核心就是这一屏。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUlwvcIkvEJ4RyyQFvxxCykpvPaKrINY6QzDMCwDU4SKVGHDH2d2FKHAIb0ZckFv7RXFdLDqGaPlicyP4lztYWGicGNT24G8ht7A/640?wx_fmt=png&from=appmsg)

坦率的讲，我不知道大家读这个回复的感受怎么样，明明很短，但是我就是读的云里雾里，看完了以后的感觉也是如看，可读性极差，并且里面居然说前期建议是人工审核，我是疯了吗我，我每天无时无刻蹲在屏幕前来审大家的评论？这是人能给出来的建议？

排行榜的方案规划也是。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUdQNGJmiah3fzrb5pibgJ6mNaYoXKhtAWN1julYUPHk94FponkAvVlVpgdctRePqvjMX1RsErtryvUbOZWIheoqNwBEg1ctC7wc/640?wx_fmt=png&from=appmsg)

我甚至会觉得，GPT-6.2 Astra的内容可读性和偏主动性的规划能力，好像比初期G...