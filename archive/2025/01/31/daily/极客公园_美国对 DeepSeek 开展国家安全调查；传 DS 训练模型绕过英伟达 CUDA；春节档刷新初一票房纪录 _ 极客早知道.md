---
title: 美国对 DeepSeek 开展国家安全调查；传 DS 训练模型绕过英伟达 CUDA；春节档刷新初一票房纪录 | 极客早知道
url: https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653073041&idx=1&sn=f9ec93124dfcfa3b5d40259ab4c2c990&chksm=7e57d32749205a310d8f135837f52b88af79c3c4cfa6f0101b33a99b48b746b953b3373c0e88&scene=58&subscene=0#rd
source: 极客公园
date: 2025-01-31
fetch_date: 2025-10-06T20:10:44.166795
---

# 美国对 DeepSeek 开展国家安全调查；传 DS 训练模型绕过英伟达 CUDA；春节档刷新初一票房纪录 | 极客早知道

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5a6ialITEdYHUNXXl3ocYnFEP7xGvtlBRSBRJQe1SgCqlYh9e9Tduiaewp1LUW7bhsS73nvZxKzsYDw/0?wx_fmt=jpeg)

# 美国对 DeepSeek 开展国家安全调查；传 DS 训练模型绕过英伟达 CUDA；春节档刷新初一票房纪录 | 极客早知道

Li Yuan

极客公园

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bY6t6vlgEXpv7hZMzGbcgTLN0PxBkJwvrw0Xw5Jribia9xgGvhF2JBmORJicJiaibz4Ahbt8IlhNH5ROA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5a6ialITEdYHUNXXl3ocYnFEfYYjeOGf3kgPhxJWib0hyuhFTLq8yLeSkpSzcpne5T6ohVEg8SBP7gg/640?wx_fmt=png&from=appmsg)

## OpenAI 表示，有证据显示 DeepSeek 使用了其模型辅助训练

1 月 29 日消息，OpenAI 表示，已经发现证据表明，中国人工智能初创公司 DeepSeek 使用美国公司的专有模型来培训自己的开源竞争对手。

OpenAI 告诉《金融时报》，它看到了一些「蒸馏」的证据，它怀疑来自 DeepSeek。

开发人员使用该技术通过使用较大，功能较强的模型的输出来获得更好的较小模型性能，从而使他们能够以更低的成本在特定任务上获得相似的结果。蒸馏是行业中普遍的做法，但如果 DeepSeek 正在这样做以建立自己的模型，是违反 OpenAI 的服务条款的。其服务状态用户条款表示，不能「复制」其任何服务，也不能「使用输出来开发与 OpenAI 竞争的模型」。

OpenAI 拒绝进一步评论或提供证据的详细信息。（消息来源：Financial Times）

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5a6ialITEdYHUNXXl3ocYnFEdsHLRnGeAiaNibxiaibzB3TdsiapQ6FQrJRoNl67B84Yf644ENLcJh6h4Lw/640?wx_fmt=png&from=appmsg)

## 美国正对 DeepSeek 开展国家安全调查

1 月 29 日消息，据参考消息援引美媒报道，美国海军基于「潜在安全和道德问题」，已要求人员避免以任何形式使用中国公司的 DeepSeek 模型。

另据 @ 玉渊潭天 消息，当地时间 1 月 28 日，美国多名官员回应 DeepSeek 对美国的影响，表示 DeepSeek 是「偷窃」，正对其影响开展国家安全调查。

「有大量证据表明，DeepSeek 将 OpenAI 的知识，通过蒸馏提炼到 DeepSeek 中，我认为 OpenAI 对此并不高兴。」白宫人工智能和加密货币事务负责人受访时表示。

同时，美国新任白宫新闻秘书卡罗琳·莱维特（Karoline Leavitt）在首次简报会中也提及了中国人工智能初创公司深度求索（DeepSeek）。她表示，白宫正在努力确保美国人工智能的主导地位，美国国家安全委员会正在调查 DeepSeek 带来的影响是什么。

而就在此前一天，美国总统特朗普还认为 DeepSeek 崛起也可能传递了一种积极信号，并表示此事应当为美国企业敲响「警钟」，美国公司「需要专注于竞争以赢得胜利」。（消息来源：上游新闻）

## 「DeepSeek 甚至绕过了英伟达 CUDA」，论文细节再引热议

硬件媒体 Tom's Hardware 带来开年最新热议：DeepSeek 甚至绕过了 CUDA，使用更底层的编程语言做优化。

DeepSeek-V3论文中的更多细节，被人挖掘出来。来自Mirae Asset Securities Research（韩国未来资产证券）的分析称，V3 的硬件效率之所以能比 Meta 等高出 10 倍，可以总结为「他们从头开始重建了一切」。

在使用英伟达的 H800 GPU 训练 DeepSeek-V3 时，他们针对自己的需求把 132 个流式多处理器（SMs）中的20 个修改成负责服务器间的通信，而不是计算任务。变相绕过了硬件对通信速度的限制。

这种操作是用英伟达的 PTX（Parallel Thread Execution）语言实现的，而不是 CUDA。PTX 仍然是英伟达GPU架构中的技术，它是 CUDA 编程模型中的中间表示，用于连接 CUDA 高级语言代码和 GPU 底层硬件指令。

使用PTX编程非常复杂且难以维护，很难移植到不同型号的 GPU，但能带来极致的优化效果。从业者表示，针对 H100 优化的代码迁移到其他型号上可能效果打折扣，也可能根本不工作了。所以说，DeepSeek 做了 PTX 级别的优化不意味着完全脱离了 CUDA 生态，但确实代表他们有优化其他 GPU 的能力。

一位亚马逊工程师提出灵魂质问：CUDA 是否还是护城河？这种顶尖实验室可以有效利用任何 GPU。（消息来源：量子位）

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5a6ialITEdYHUNXXl3ocYnFE5zAhhUxDkHJpUKO43EH6xibpjCTO1IM4xPPZljOARsLb8QmoVBlQlwQ/640?wx_fmt=jpeg&from=appmsg)

## 特斯拉公布第四季度财报

1 月 30 日，特斯拉公布 2024 年第四季度财报，未达市场预期，营收同比仅增长 2%，至 257.1 亿美元，远低于分析师预期的 272.6 亿美元。汽车业务收入同比下降 8%，利润率进一步承压。特斯拉在加大折扣促销的同时，继续押注自动驾驶与能源业务，以寻找新的增长点。

特斯拉 2024 年总营收达 977 亿美元（当前约 7098.18 亿元人民币），全年共交付 1789226 辆汽车。

同时，财报显示，在第四季度，特斯拉单车销售成本达到了历史最低水平，低于 35000 美元（约合人民币 25.3 万元）。特斯拉解释道，这主要得益于原材料成本的改善，这帮助特斯拉部分抵消了提供有吸引力的金融和租赁方案所做的投入。

财报还提到，2024 年第四季度，特斯拉在车辆交付和能源存储设备装机量方面均创下了纪录。预计 Model Y 将在 2024 年再次成为包含所有车型在内的全球最畅销车型。

特斯拉此前还表示，正在为推出更加经济的新车型做准备，并给出时间展望——将在 2025 年上半年开始推出。（消息来源：FX168、快科技）

## Meta 第四季度营收 483.85 亿美元同比增长 21%，净利润同比增长 49%

1 月 30 日早间消息，Facebook 母公司 Meta 今天发布了该公司截至 12 月 31 日的 2024 财年第四季度及全年未经审计财报。

报告显示，Meta 第四季度营收为 483.85 亿美元，与上年同期的 401.11 亿美元相比增长 21%，不计入汇率变动的影响同样为同比增长 21%；净利润为 208.38 亿美元，与上年同期的 140.17 亿美元相比增长 49%；每股摊薄收益为 8.02 美元，与上年同期的 5.33 美元相比增长 50%。

由此，Meta 2024 财年营收为 1645.01 亿美元，与 2023 财年的 1349.02 亿美元相比增长 22%，不计入汇率变动的影响为同比增长 23%；运营利润为 693.80 亿美元，与 2023 财年的 476.51 亿美元相比增长 48%；运营利润率为 42%，与 2023 财年的 35% 相比有所上升；净利润为 623.60 亿美元，与 2023 财年的 390.98 亿美元相比增长 59%；每股摊薄收益为 23.86 美元，与 2023 财年的 14.87 美元相比增长 60%。

当日，Meta 股价在纳斯达克常规交易中上涨 2.16 美元，报收于 676.49 美元，涨幅为 0.32%。在随后截至美国东部时间周三下午 5 点 19 分（北京时间周四早上 6 点 19 分）的盘后交易中，Meta 股价再度上涨 30.84 美元，至 707.33 美元，涨幅为 4.56%，突破 52 周最高价。在截至美股收盘周三收盘为止的过去 52 周，Meta 的最高价为 682.58 美元，最低价为 387.10 美元。（消息来源：新浪科技）

![](https://mmbiz.qpic.cn/mmbiz_jpg/8cu01Kavc5a6ialITEdYHUNXXl3ocYnFEr8oBUEAMdb11dRuy0yUvzHGJax9UcmibdQMslr8CBWP6AicnW0DR2B2w/640?wx_fmt=jpeg&from=appmsg)

## 微软 2025 财年第二财季营收 696.32 亿美元同比增长 12%，净利润同比增长 10%

1 月 30 日早间消息，微软今天发布了该公司的 2025 财年第二财季财报。

报告显示，微软第二财季营收为 696.32 亿美元，与去年同期的 620.20 亿美元相比增长 12%，不计入汇率变动的影响同样为同比增长 12%；净利润为 241.08 亿美元，与去年同期的 218.70 亿美元相比增长 10%，不计入汇率变动的影响同样为同比增长 10%；每股摊薄收益为 3.23 美元，与去年同期的 2.93 美元相比增长 10%，不计入汇率变动的影响同样为同比增长 10%。（注：微软财年与自然年不一致。）

微软第二财季调整后每股收益和营收均超出华尔街分析师此前预期，但其盘后股价仍旧下跌逾 1%。（消息来源：新浪科技）

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5a6ialITEdYHUNXXl3ocYnFEFs3tjuF8m0zXdTjlPdNN3DdYuTo8Y3FrM8Mric4G6r4kVbB3zibjSf6g/640?wx_fmt=png&from=appmsg)

## 苹果 iPhone 用户禁用 Apple Intelligence 可释放最多 7GB 存储空间

1 月 29 日消息，从 iOS 18.3、iPadOS 18.3 和 macOS 15.3 版本开始，苹果最新的人工智能功能「Apple Intelligence」将默认开启。不过，如果用户不打算使用这个功能，可以手动关闭并释放存储空间。

## 特朗普媒体科技集团进军去中心化金融

1 月 29 日消息，特朗普媒体科技集团公司宣布推出金融服务和金融科技品牌 TruthFi，进军去中心化金融领域。董事会已批准投资高达 2.5 亿美元，可以分配给 SMA、ETF 以及比特币和类似的加密货币或加密相关证券。（消息来源：新浪财经）

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5a6ialITEdYHUNXXl3ocYnFEQ87mNht25MdNhAVC6XC4javmuhSgWz1pzTHZfPk8zkS79SibN3JeRBA/640?wx_fmt=png&from=appmsg)

## Boom 的超音速试验飞机首次成功突破音障

1 月 29 日消息，在去年三月首次完成亚音速飞行 10 个月后，Boom Supersonic 的原型测试飞机 XB-1 今天在第 12 次飞行中三次突破音障。XB-1 是 Boom 希望最终建造的大型 Overture 客机的小型示范版本，可搭载 64 名乘客进行超音速国际航班飞行，巡航速度可达 1.7 马赫，类似于协和飞机 2003 年退役前提供的服务。

Boom 公司的首席试飞员特里斯坦-布兰登伯格（Tristan Brandenburg）从加利福尼亚州的莫哈韦航空港（Mojave Air & Space Port）起飞后，将 XB-1 飞到 34000 英尺的高空，然后以 1.1 马赫（约 844 英里/小时）的最高速度飞行了约四分钟。今天的飞行不仅是 Boom 公司的验证机首次突破音速，也是私营公司的民用飞机首次实现超音速飞行，协和式飞机是由英国和法国政府合资建造的，并不是一家私营公司。（消息来源：cnBeta）

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5a6ialITEdYHUNXXl3ocYnFE8TfRB7QcJtOxNiaKib61mOfQkgMY2GzxpupfscwlF7zTM7jktS5VTskQ/640?wx_fmt=png&from=appmsg)

## 宝马 iX 纯电 SUV 迎来中期改款

宝马公司于近日正式推出了 2026 款 iX 中型 SUV，这款中期改款车型不仅在车型阵容上进行了调整，更在外观、内饰以及动力系统方面进行了全面优化升级，旨在提升市场竞争力。

自 2021 年上市以来，宝马 iX 的市场表现略显平淡。为了吸引更多消费者，宝马公司对 iX 进行了大幅改进。在动力方面，主力车型 xDrive60 的动力和续航得到了显著提升，效率提高了 10%。新款 iX 还新增了入门级车型 xDrive45，为消费者提供了更多选择。

在车型阵容方面，2026 款宝马 iX 进行了重新调整。除了新增的 xDrive45 车型外，原 xDrive50 和 M60 车型也分别更名为 xDrive60 和 M70，以更好地反映其动力性能的提升。xDrive60 的最大马力从 523 PS 增加至 543 PS，0-96 公里/小时加速时间缩短至 4.4 秒，最高时速可达 200 公里/小时。而 M70 则更加出色，最大马力高达 659 PS，0-96 公里/小时加速时间仅需 3.6 秒，最高时速可达 250 公里/小时。（消息来源：ITBEAR）

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5a6ialITEdYHUNXXl3ocYnFE9rlQxBPIYVNDU4uy2kxpRGR2ruSuW1OUxQiagKMqlaWz0RGtqsRKtmA/640?wx_fmt=png&from=appmsg)

## 中国电影史单日票房新纪录，2025 年大年初一总票房超 17 亿元

1 月 29 日消息，根据国家电影专资办统计，截至 1 月 29 日 19 时，2025 年春节大年初一票房已达 17.01 亿元，观影人次已达 3306.78 万，票房超过 2021 年春节大年初一，创造了新的单日票房纪录。

节档票房（含预售）已达 22.11 亿元，六部春节档新片票房分别为：

* 《哪吒之魔童闹海》5.60 亿元
* 《唐探 1900》5.48 亿元
* 《封神第二部：战火西岐》4.35 亿元
* 《射雕英雄传：侠之大者》3.95 亿元
* 《熊出没・重启未来》1.63 亿元
* 《蛟龙行动》9193.10 万元

2025 年春节档已破多个纪录，刷新中国影史预售最快破千万纪录、刷新历史春节档平均时长最长纪录等。（消息来源：IT 之家）

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5a6ialITEdYHUNXXl3ocYnFET7ibQKaQK5l6GNVvud2kFibAhhzHI3IuPHiaia52Wca50pDhIa7jRXC2Yw/640?wx_fmt=png&from=appmsg)

\*图片来源：视觉中国

---

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bY6t6vlgEXpv7hZMzGbcgTbrlCe3BNPT2cib3YqfibGbCGkRcJq0fLReiaZzibb6xibWLKqyybn1auclg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5Z5rEl2poJuZqVBGZteWibbvpuA2OibrtXHS6bAJibcYSkxdsV1VicAF088bxt3yluWTQeMyL38W8bfrw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**热点视频**

超越 OpenAI！DeepSeek 发布多模态模型 Janus-Pro。

**点赞关注****极客公园视频号****，**

**观看更多精彩视频**

**![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5an0KBXb9IbCwiajJefiaywlMX2G9daxebRIz0bpONcZbhCkA7mNIG39fwRUOEzpoBIPvAXIuA82B9Q/640?wx_fmt=png)

**更多阅读****

‍[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5YP5znW9hLwdcHTtRRUWRdxIltDOUia7LR2lIvPbRUwyFh3ln6ziaibrUBichhEADAAic3tZ0ia38cG8LIQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653073010&idx=1&sn=0abd27208a3082b3453f5cb1aa2a1ab7&scene=21#wechat_redirect)‍

[![](https://mmbiz.qpic.cn/mmbiz_png/8cu01Kavc5bOPYj2HFHONUnibwhVbbU4bKLIxDVGGXbQK7UfdZP7jaQ0F61C1tGbjfq3fPnNkAaGtWjgWp9Nbfg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653072968&idx=1&sn=11cc8c1298740ae6a406e012a43af24b&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/8cu01Kavc5ZENt3gIiatQKstoLiatpXoWBUwkB6t...