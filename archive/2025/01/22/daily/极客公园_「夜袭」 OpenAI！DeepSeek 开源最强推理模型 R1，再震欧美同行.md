---
title: 「夜袭」 OpenAI！DeepSeek 开源最强推理模型 R1，再震欧美同行
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653072415&idx=1&sn=a47a2f0c4272857c4920d18773448430&chksm=7e57d1a9492058bfd25004e5d0e45bf2271e89a218d3a62a75cdf774b90dca0c5eab3ba560cb&scene=58&subscene=0#rd
source: 极客公园
date: 2025-01-22
fetch_date: 2025-10-06T20:11:17.116371
---

# 「夜袭」 OpenAI！DeepSeek 开源最强推理模型 R1，再震欧美同行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YnduMrl8VEiafW3TwlE36eoyjiaxe7bNg8Oja3nlErIO8XUyUSwTJ4G3pcpibnywkQibia1OzjdHevNeQ/0?wx_fmt=jpeg)

# 「夜袭」 OpenAI！DeepSeek 开源最强推理模型 R1，再震欧美同行

原创

宛辰

极客公园

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YnduMrl8VEiafW3TwlE36eohqTqr6wXK4W2xrLF9xnfUpD4kEXMfcb2jxaUV3RZerFJIvGsPsDYmA/640?wx_fmt=jpeg&from=appmsg)

中国的 OpenAI，出现了。

**作者 | 宛辰****编辑**| 靖宇****

对标 OpenAI o1 正式版的国产大模型来了！

1 月 20 日晚，DeepSeek（深度求索）公司发布推理模型 DeepSeek-R1 正式版，同步开源模型权重，并允许用户利用模型输出、通过模型蒸馏等方式训练其他模型。

网友热评：**这，才是真正的****OpenAI****。能力相当于一个月 200 美元的 ChatGPT o1 版本，却完全免费**。

不止如此，DeepSeek 一同开源的还有「技术报告」，那些训练 R1 时踩过的坑、做过的事通通讲给你听，只为铺平 AGI 的路。

第一时间阅读这份技术报告后，英伟达高级研究科学家 Jim Fan 带来了新鲜解读，值得我们大声齐读:

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YnduMrl8VEiafW3TwlE36eosQJib63SEAYZT1lqt75Yr9ousArZbVv6351OFHRIl4uBvTwSickZ8VAQ/640?wx_fmt=png&from=appmsg)

「我们生活在这样一个时代：由非美国公司保持 OpenAI 最初的使命——做真正开放的前沿研究、为所有人赋能。这似乎讲不通，但戏剧性的往往最有可能发生。

DeepSeek-R1 不仅开源了大量模型，还泄露了所有训练秘密。他们可能是第一个显示 RL（强化学习）飞轮发挥主要作用、持续增长的 OSS 项目。

影响可以通过『内部实现了 ASI』或『草莓计划』等神话名称来实现。也可以通过简单地转储原始算法和 matplotlib 学习曲线来产生影响。」

中国公司 DeepSeek，正在实现赶超 OpenAI 的使命**。**

***01***

**DeepSeek-R1：**

**实力派选择「秀肌肉」**

「DeepSeek-R1」的发布，摆明了是：有实力所以明晃晃地秀肌肉！

**这首先体现在它不整期货那一套，而是「发布即上线」**，现在，你就可以在 DeepSeek 官网与 App 体验最新的推理模型 DeepSeek-R1，随便体验随便用，免费。

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YnduMrl8VEiafW3TwlE36eost6JCib2koBcglGZJmPibxudvG3pn46wNZcEdOcZTSLu4Zw4aDaM1G2w/640?wx_fmt=gif&from=appmsg)登录 DeepSeek 官网或官方 App，打开「深度思考」模式，即可调用最新版 DeepSeek-R1 完成各类推理任务。｜图片来源：DeepSeek

DeepSeek-R1 也同步上线了 API，对用户开放思维链输出，通过设置 model='deepseek-reasoner' 即可调用。

值得注意的是 DeepSeek-R1 API 服务定价为每百万输入 tokens 1 元（缓存命中）/ 4 元（缓存未命中），每百万输出 tokens 16 元。看下面这这图你会有更直接的体感，输出 API 价格只有 OpenAI o1 的 3%。**低价背后，显然仍是秀肌肉，价格实力展现了技术实力——从****AI****Infra 层面降本的技术能力。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YnduMrl8VEiafW3TwlE36eoOgLCiaBuiadsKQiczTBbXKHXcRvibGK59HEG0fnDCb2UQq3YX3uMOpZ12A/640?wx_fmt=other&from=appmsg)图中深蓝色柱子代表 DeepSeek-R1，剩下的灰色、浅蓝、青浅灰分别是 OpenAI o1 不同版本的价格。｜来源：DeepSeek

**第三波「秀肌肉」体现在开源开放****。**DeepSeek-R1 开源模型权重几乎是选择了最开放的许可证和用户协议，开源 License 统一使用 MIT，产品协议明确可「模型蒸馏」，主打一个让大家多多来基于它做二次开发、集成。DeepSeek 甚至主动给大家示范引导将 R1 作为教师模型来蒸馏出一个更小但仍有实力的模型，「通过 DeepSeek-R1 的输出，蒸馏了 6 个小模型开源给社区，其中 32B 和 70B 模型在多项能力上实现了对标 OpenAI o1-mini 的效果」。

事实上**，模型开源选择不同的 License 背后大有学问，这直接体现不同模型厂商的开放程度，更体现开源背后的目的和策略。**比如像 Llama、Qwen、GPT-2 等模型就不止开放权重，还开放了模型训练的源代码，这可能是为了追求衍生模型的繁荣。而 DeepSeek-R1 选择只开放权重，但换成了标准化、宽松的 MIT License，更多还是为了让更多开发者能用起来，感受 DeepSeek-R1 的能力。

我们再来通过**几大主流测试基准来感受一下 DeepSeek-R1 的实力**。「性能对齐 OpenAI-o1 正式版 DeepSeek-R1 在后训练阶段大规模使用了强化学习技术，在仅有极少标注数据的情况下，极大提升了模型推理能力。在数学、代码、自然语言推理等任务上，性能比肩 OpenAI o1 正式版。」

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YnduMrl8VEiafW3TwlE36eo4YpYIicibpYHKv7hLKicqINm91n1OeH0HgFYACnnibgzdqFNicU6CMJ2VdQ/640?wx_fmt=other&from=appmsg)图片来源：DeepSeek

对于 DeepSeek-R1 带来的直观感受，硅基流动联合创始人杨攀表示，**不止模型能力和性能出色，最近两个模型 (R1 和 V3) 在训练技术和模型底层架构上都做了领先全球的创新，而且其论文开放程度也震惊了业界。**

在一并公开的模型技术报告中，DeepSeek 将「DeepSeek-R1」训练技术全部公开，「旨在促进技术社区的充分交流与创新协作」。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YnduMrl8VEiafW3TwlE36eoYSDC3su1z1AnSjO5QLyIn3xz130Faib1VVC8TGg005SmcM9bGbZr7hg/640?wx_fmt=jpeg&from=appmsg)根据技术报告，硅基流动创始人&CEO 袁进辉称，DeepSeek-R1 是无人区的探索和发现。｜来源：即刻

对于开源模型加技术报告，开源社联合创始人林旅强此前向极客公园表示，**开源是最好的「秀技术肌肉」的方式**，同时「有的开源模型只开源、不讲他是怎么做的，但是**合乎大家期待的开源模型是要搭配技术报告，等于是发 paper 了。开源模型不够的，因为模型是黑盒子，技术报告会说明一些东西**。DeepSeek 他们是很透明地把他的技术报告拿来公开，即使一定程度还是会捂着掖着，但是已经是开得比较有态度。**今天全球范围的学术派还是会认为，你把一个东西做出来再以开源的方式，是有学术追求的。**」

如果 DeepSeek 的目标是真正达到 AGI，就不断需要把踩过的坑、做过的事情开放出来，让大家少走一点弯路，开放才能让整个行业更快达到 AGI，他补充道。

**最后，我们来随机看一些用户实测评价**（截图来源：X.com）：

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YnduMrl8VEiafW3TwlE36eoAiaxb0TfYViaf1AcNJosmYmxhoAE7OF18wn44gHjvkdQgLWcL1aeWiabQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YnduMrl8VEiafW3TwlE36eonHoJDzposQIXjbrmOQOZasnfBQkBylaFb1W1UHExHwVjSIia2XiacgXg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YnduMrl8VEiafW3TwlE36eoLS1jfqkv8yOiauwlFR7OPHqtv1H8nUCOcQjLmvyNl7jvpVeFcvMR8ow/640?wx_fmt=png&from=appmsg)Twitter 用户盛赞 R1 的实力｜图片来源：X

***02***

**DeepSeek，还有什么**

**惊喜是我们不知道的？！**

尽管昨晚 DeepSeek-R1 的发布引发了「这才是 Open AI 吧」「东方的 OpenAI」等一片称赞。但 DeepSeek 强得非常扎实、全面。

去年在 2024 年 11 月 20 日发布 DeepSeek-R1-Lite 预览版时，美国著名半导体与 AI 咨询机构 Semianalysis 创始人 Dylan Patel 就坐不住了，第一时间下场「提醒」大家：**他们有 5 万张 H100****GPU****！请不要以为他们只有 1 万张 A100**！

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YnduMrl8VEiafW3TwlE36eotD5icLmB9OWWRbZl0PfCGGS32IlsT5Hnn4P8PBqoNbvgSn0v9Na3ibrg/640?wx_fmt=png&from=appmsg)

因为众所周知的原因，这大概率不是事实，却能反映 DeepSeek-R1-Lite 的强悍到让行业紧张。

一个月后，DeepSeek 上线并同步开源了媲美 GPT-4o 和 Claude 3.5 Sonnet 的模型「DeepSeek-V3」，并附上了详实的技术报告。这一次，**几乎惊动了整个硅谷****AI****圈。**卡神（OpenAI 创始团队、前 Tesla AI 总监 Andrej Karpathy）、Alexandr Wang（Scale.ai 创始人）、田渊栋（Meta AI 科学家）、贾扬清（Lepton AI 创始人）……人均一句「难以置信」。就连 Sam Altman 都忍不住出来酸一把「复刻已经被验证过奏效的东西是容易的」。

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YnduMrl8VEiafW3TwlE36eoy0E2vHQP2ibMuQvRrZa8UcU7cTQAVwQ0SicMLtKCmSoO9ic0iaBq72Q70w/640?wx_fmt=png&from=appmsg)DeepSeek-V3 发布后，Sam Altman 疑似喊话 DeepSeek。｜截图来源：X.com

**随着模型性能逐渐走向全球第一梯队，DeepSeek 也迎来了新的发展契机。**

过去一年半，DeepSeek 专注于模型和研究，但从今年开始，DeepSeek 着手做应用了。

2025 年 1 月 15 日，DeepSeek 推出移动端 AI 助手「DeepSeek」App。目前看，DeepSeek App 跟网页版功能一致，主要有两个功能：联网搜索和深度思考，主打一个简洁，聊天记录也会同步显示在手机端和网页端，尚未针对移动端进行特定功能的打磨，也没有市面上 AI 助手类 App 丰富、fancy 的功能，更像是一个能让你在手机上体验 DeepSeek 最新模型的入口。

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5YnduMrl8VEiafW3TwlE36eozq9ia4AbYj7ZzM3mGwLNnibYGcO2S3tk8Njg3yibpZg91ITmLwdQDZ1vw/640?wx_fmt=jpeg&from=appmsg)DeepSeek App 展示图｜来源：Apple Store

对此，一位投资人向极客公园解释 DeepSeek 开始做应用背后可能的战略转向：「前期 DeepSeek 靠自己的算力优势积累出了模型技术的领先度。后期要补数据，发 App 是补数据的手段之一。**接入用户数据和场景，可以帮助他更好地进行模型能力的迭代和升级**。」

同时，有了 DeepSeek-R1 和其他模态、类型越来越好的模型，可以期待未来 DeepSeek 在比如代码模型/应用里有更激进的表现，惊喜才刚刚开始。

\*头图来源：视觉中国

本文为极客公园原创文章，转载请联系极客君微信 geekparkGO

**极客一问**

**你看好 **DeepSeek 吗******？**

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YTxYGib55rtMHhP1YJ44FLtVGp8Keyg6D2X3AUhgNicT1ibKKh0fE1eiaGqkSXnTlW0ib96ib3HDAIrnVA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bXib8IGpjbghqj305kKeYibwx0gmZO3iaFibnGncpOnsDNKDciaIH6xNBnpPpk7o5de1RKLzgq70eibBTw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频**

马斯克：传统教育培养答题机器，总爱折腾一些不存在的东西。

**点赞关注****极客公园视频号****，**

**观看更多精彩视频**

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Y9qaKVoX8mmmt5JibNbFGrP7xIykXQVUDqibsh3h7NvExmOVqwS4ATAqCiauSR3aGNwAichvCrPY5X2g/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653072363&idx=1&sn=feda9287cf8b3068ce7f17923c00d078&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Y9qaKVoX8mmmt5JibNbFGrPYgF3e6dx8PgbyNeUic5j9U3Ih14wYHne7JhbPjWrADbfEkCs4kOQr0g/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653072331&idx=1&sn=2f8f2f9d50771b9c3f15cac061f8cff5&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6tO2b9y2Hoj5HpcnXc5zRJEX6MhbyXJ3q0gjTrrBIUF7boJGDA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5YR1a8dIHV2UrCdNIhialnevdQkialrf9oMibXZhuHeD0nPUHuFlYzYB4WYzwnTbhSyAvj9ibZb7ibewPw/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

极客公园

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5aZd3zlj8Yykibdibgmjs5Xm2KAOicKZoIGib0c12wVnDwaH10PY2076aqwaK6aCJHd4RibkpVrON2Oh0Q/0?wx_fmt=png)

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