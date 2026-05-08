---
title: 22岁开发者逆天复现Claude Mythos！GitHub狂揽1.1万Star，CTF挑战成功率73%
url: https://mp.weixin.qq.com/s/qIRUkNmJj7ZY7fRK4q27jQ
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:50:44.855318
---

# 22岁开发者逆天复现Claude Mythos！GitHub狂揽1.1万Star，CTF挑战成功率73%

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicL8iaKQD7d4M9RuPVibhvKbK8dHxxHBzZgPHHGKroq4ApNlKTmB4ac3c7v02EbiboFnVpv5Y13xhVyltPChmyNu0YtkKHkTvYibxRQ/0?wx_fmt=jpeg)

# 22岁开发者逆天复现Claude Mythos！GitHub狂揽1.1万Star，CTF挑战成功率73%

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Anthropic藏了个王炸模型——Claude Mythos Preview。

不对外开源、不公开发布、仅给40余家技术联盟内测，原因很简单：

能力强到危险。英国AI安全研究所测试显示，它能自主跑完32步企业网络攻击链，CTF挑战成功率73%。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJdeG4mldwTAh2Ulbd2CoHBn8zylJib9giaGw6yzpjx9enXtibiaT6ricWo5zib4XBhNiakjzl9GfPo2P0uoqy3ZD4Q9t6uHNQdqhl5XQ/640?wx_fmt=jpeg)

没人知道它的真实架构，没有论文、没有报告，Anthropic守口如瓶。

直到一位22岁开源开发者Kye Gomez，凭公开论文线索，用PyTorch把这个“神秘架构”逆向复现，项目OpenMythos开源4天近7000 Star，如今突破1.1万，GitHub评论区吵翻了天。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKTOLb4b7lqFMTeibbhiacIEkANmThKHHRW04SiciaMrmj0sbdW6OfmxMQwJ9kkoKiceRnWCXtibQEGuibu2ptRxDLs5sUz7Xp0zFV2U4/640?wx_fmt=jpeg)

被锁起来的超级模型：Mythos为何不敢开放？

Claude Mythos属于Anthropic的Project Glasswing计划，专供关键基础设施安全评估，官方明确表态：无公开发布计划。

它的恐怖之处在于：

 自主完成完整企业网络攻击，人类专家需20小时，它一键跑完

 专家级CTF攻防挑战，成功率73%

 强推理、长逻辑、高风险，直接被“锁进保险柜”

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJj9u0wQr74zHU9IKRnZvunJZpT7ia9O5BicgtzPObIY6w7Rk35PZmYRPaQE48kKeAsqVR0DoSfLwzkZncklAHnsnCwzjyDKeAd4/640?wx_fmt=jpeg)

官方不公开架构，等于把复现之路堵死。但这位22岁开发者，硬是靠“猜+推导”，写出了整套代码。

颠覆范式：不堆层数，靠“反复思考”提升能力

传统大模型（GPT、LLaMA）靠堆层数、堆参数变强，100层不够就200层，参数量水涨船高。

OpenMythos走了条完全相反的路：不堆层数，让同一组权重循环跑多遍。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicLB4hrqNoEmWib9nKkhpEcPmt9tnTsibK4tpX0aTusBThZ7RxicOVjM6kGSISRJXkwUjZDnLbJ0DCJgyUuibj0J7woKylsMiafAqsXg/640?wx_fmt=jpeg)

类比理解：

 传统模型：翻书，一页一页读完就结束

 OpenMythos：反复精读同一段，每一遍都加深理解

效果惊人：770M参数循环模型，性能对标1.3B传统Transformer，参数量直接省近一半，训练与部署成本大幅降低。

三大核心亮点：循环架构+稳定训练，革Transformers命

OpenMythos架构分为三段：前奏层(Prelude) + 循环块(Recurrent Block) + 尾声层(Coda)，核心创新全在中间的循环块。

1. 循环推理，深度外推超强

 每轮循环都在前一轮基础上深化推理，不是简单重复

 训练跑16轮，推理可直接跑24/32轮，泛化能力拉满

 简单问题少跑轮次，难题多算几遍，只改参数不动模型

2. MoE+MLA双加持，显存暴减

 集成MoE混合专家，不同深度激活不同专家子集

 支持MLA注意力，KV缓存缩小10-20倍

 兼容GQA+Flash Attention 2，速度与效率兼顾

 ACT自适应计算：简单token早退出，复杂token多计算

3. 数学级稳定，训练不炸

循环Transformer的世纪难题是梯度爆炸/消失，OpenMythos用LTI注入从数学层面解决：

 状态更新按线性时不变系统构造

 谱半径严格小于1，学习率再高也稳定

 对数空间计算+精度保护，杜绝溢出

争议拉满：天才之作，还是空中楼阁？

OpenMythos现在的状态很真实：

✅ 代码可编译，架构逻辑自洽

✅ 提供1B~1T七档模型配置

✅ 支持pip一键安装

❌ 无训练好的权重

❌ 无官方Benchmark

❌ 无实际推理演示

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicI8V6qvQ2LCFGlYws0iasCORQJWbztnR7WicoicpguBRiaib7cCzKRDoP3sHIfN4mXgRE8cbTZ7onzrcamcNWGy0u4bcw8eJKh2e6BM/640?wx_fmt=jpeg)

它本质是对Mythos架构的假设性实现，不是可直接商用的模型。GitHub上两极分化：

有人夸天才，有人直言“这很愚蠢”，

但没人能否定——它给出了一个可被证伪、可落地验证的具体方向。

一键使用：极简部署，人人可测

安装一行命令搞定：

bash

pip install open-mythos

极简调用示例：

python

import torch

from open\_mythos import OpenMythos, mythos\_1b

from open\_mythos.tokenizer import MythosTokenizer

# 加载1B模型

config = mythos\_1b()

model = OpenMythos(config)

tokenizer = MythosTokenizer()

# 推理生成

ids = torch.tensor([tokenizer.encode("Explain quantum computing")])

output = model.generate(ids, max\_new\_tokens=512, temperature=0.7)

支持PyTorch FSDP分布式训练，默认使用FineWeb-Edu数据集，开箱即用。

最后

OpenMythos可能不是100%还原Claude Mythos，但它把大模型的“缩放之争”，从堆多少参数推向了推理算多少轮。

770M干翻1.3B，循环深度Transformer，或许就是下一代大模型的破局方向。

22岁开发者，凭一己之力挑战巨头闭源黑箱，这正是开源AI最迷人的地方。

项目地址：https://github.com/kyegomez/OpenMythos

作者：hacking。前北漂程序员，现在做安全。

文章数据来自网络，大模型优化，侵权删。

**往期****相关****回顾**

[突发！意大利批准：美国引渡中国工程师徐泽伟](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554552&idx=1&sn=3ea39c208a37b34e033420ee8e4fa096&scene=21#wechat_redirect)

[DeepSeek现在我是你爹了](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554708&idx=1&sn=fbdf1504f70e6d8f7ba33aa96e881189&scene=21#wechat_redirect)

[苹果突发“社死”现场！一个文件忘删，4万亿AI家底全曝光](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554704&idx=1&sn=7b352ba2101a82abd1369f9cf4655995&scene=21#wechat_redirect)

[体制内vs大厂：当初选“稳”的人，现在后悔了吗？](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554700&idx=1&sn=90b851bc9acd516f42f7afdeae8dfc35&scene=21#wechat_redirect)

[炸场！2026年4月GitHub爆火11个开源项目，第3个Hermes封神](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554685&idx=1&sn=4ece1c43e225372e6e6625c22cdca38c&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

Hacking黑白红

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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