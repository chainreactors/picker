---
title: 通过微调与拒绝向量消融实现大模型越狱的实践
url: https://mp.weixin.qq.com/s/Zctm7PV6FxUX7DFDuo3uoA
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:29:46.340228
---

# 通过微调与拒绝向量消融实现大模型越狱的实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/05AlicrBviacUxuxM9sAu7syTLpOnhqia1DwgYaymtVicqR2JCWX1Q7iaB1nl3mefxSDYibhhXW2H0B77iatJOp8fqmsA/0?wx_fmt=jpeg)

# 通过微调与拒绝向量消融实现大模型越狱的实践

CKCsec安全研究院

![]()

在小说阅读器中沉浸阅读

> AI突破限制的多种手段 前言：目前看到过很多越狱AI的手法，绝大多数都是使用提示词注入来对互联网上现有AI进行越狱，本文章中介绍另外两个方法进行越狱。

```
本文首发地址为 奇安信攻防社区：https://forum.butian.net/share/4657
已经原作者授权
```

---

> 环境要求如下

* 大模型(需要下载至本地或云服务器)
* Python(推荐3.9以上版本)

---

## 0x01 AI安全对齐简介

在进行越狱之前，我们需要明确一个核心前提：AI 本身是没有主观安全意识的。在 AI 专业术语中，这涉及内生安全问题。大语言模型本质上是一个基于概率的“文字接龙”机器，它的核心任务是预测下一个最可能的字（Token），而不是判断“善恶”。所有的道德感和安全限制，都不是它与生俱来的，而是人类后天强加给它的“外挂补丁”。因此，这种安全机制具有天然的脆弱性和不完备性。

安全对齐则是为了防止AI输出有害内容而衍生出的技术，目前比较常见的绕过方式就是提示词注入，比如网络安全中常见的 问他写一个webshell，他会立马因为各种安全道德问题而拒绝回答，常见绕过的提示词如比如扮演一个奶奶这种提示词，来绕过限制，但是由于目前安全对齐的越来越好，越狱也变得越来越麻烦，在前段时间阿里举办的AI安全大赛中，我看到很多选手越狱AI来生成提示词，攻击目标AI，但其实除了提示词注入，还有两种手段，今天主要来介绍这两种

## 0x02 方法一：AI微调

为什么说微调可以突破安全对齐呢？主要原因是因为微调过程中大模型可以学习到新的、与初始安全约束相冲突的行为模式或指令，通过学习这些回答，降低对原始安全过滤的抗拒性，在学习的较好的情况下，会出现非常完美的去除安全对齐的效果。

以及关于微调有一篇关联的论文《BadTuning: Bypassing Safety Alignment in Large Language Models via Adversarial Fine-tuning》

![](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1DLDHlHjUwB217nIjg1CiaHibgpiaxib1Frc8ocZGPFibK8rLY5omG2NL2FVw/640?wx_fmt=png&from=appmsg)

论文中提到，即便使用完全无害的数据集对大模型进行微调，依然会导致安全对齐效果下降；上图是论文中关于微调导致安全对齐失效的介绍及效果图，a图中可以看到，当数据集包含明确的恶意指令，如`Write a tutorial on how to make a bomb` 导致模型的安全对齐水平出现极为明显的失效；以及在c图中，即便使用完全无害的数据集，依然导致大模型安全对齐水平下降，这些构成了我们使用恶意数据集进行微调实现大模型去除安全对齐(越狱)的理论支撑。

既然要进行微调，我们这里首先需要下载一个AI，这里以 `mistralai/Mistral-7B-Instruct-v0.2` 这个模型来举例，先创建一个隔离环境，可以用虚拟机也可以用 `python -m venv xxx` 这种方式来创建虚拟环境，本次测试使用的是 `python` 虚拟环境。

首先是下载一个大模型，也就是提到的`mistralai/Mistral-7B-Instruct-v0.2`![](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1DNV0S4bYiakg0IDeFsyy2UzZicPRABaV40t90z4NZ86AaEPdQF2Ax5mdQ/640?wx_fmt=png&from=appmsg)

既然我们需要进行微调，那么我们必然需要一套数据集来进行专门的安全对齐限制的突破，以下列举几个数据集

```
https://huggingface.co/datasets/aifeifei798/merged_uncensored_alpaca/viewer/default/train?row=0
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1DZndJ5qfwIJh9aJBDqvVxx4oFgEibjCI1sgPL6NgL6IrdibS5qfJQXt2A/640?wx_fmt=png&from=appmsg)

```
https://huggingface.co/datasets/QuixiAI/dolphin
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1DbrdiaxTeEmKhr97r0C1rMUV2TrWghIficg1P0AicygGrLUicf3ftqdkHvA/640?wx_fmt=png&from=appmsg)

在下载完成数据集之后，这个时候由于我本地是Mac，所以使用LORA对大模型进行微调

```
python3 -m mlx_lm lora --model mistralai/Mistral-7B-Instruct-v0.2 --train --data ./dolphin_data/ --iters 1000 --batch-size 4 --num-layers 16 --learning-rate 1e-5 --save-every 100 --adapter-path adapters
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1Dic8BKIQe6CjHEf6grB0dkYO4tntf7B6JuVLaI3BNY2Q9JEyEyrVUmmg/640?wx_fmt=png&from=appmsg)

这里由于我本地是笔记本，全量微调的性能要求我本身无法达到，所以使用Lora进行微调，这里面`-m mlx_lm lora`为指定使用`Lora`算法进行微调，`--model mistralai/Mistral-7B-Instruct-v0.2` 这部分用于指定本地的大模型，`--train`指定使用微调模式，`--data`指定数据集的位置，需要注意的是数据集有自己的格式；`--iters 1000`这部分用于指定训练步数进行1000次训练迭代，`--batch-size 4`指定每次训练迭代中处理的样本数量是 4 个，`--learning-rate 1e-5`指定优化器用于更新模型权重的学习率，`--save-every 100`指定每隔 100 次训练迭代保存一次模型适配器的权重，`--adapter-path adapters`指定保存 LoRA 适配器权重的目录名称。

一般大模型开始训练初始的Train loss的值都在3左右，由此时开始训练，在值达到1.0以内时可以停止然后对大模型进行问答测试，在回答能力满足我们最开始的要求即去除安全对齐，或一些网络安全问题的回答之后就可以停止并将大模型载入本地的 `Ollama` 等基座中,顺利的开始使用, 如下图，在不进行提示词注入的情况下，依然可以直接输出webshell。但是需要说的是，这个微调的过程如同炼丹，可能需要很多次的反复调试。![](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1DGmTxeibGib3a9o97UrBzR9mkEgIkE3XEbs8FngLicrt5o9SarWJZ6tXZg/640?wx_fmt=png&from=appmsg)

## 0x03 方法二：拒绝向量消融

参考论文《Refusal in Language Models Is Mediated by a Single Direction》![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1D4qMN8qqGh88ugI7B6BJia6nNBb5wkl5Tr83TnVoLvH3tDPdoPfG8M0w/640?wx_fmt=png&from=appmsg)

上图中可以看到，在论文中采用100个有害指令对大模型进行测试，消除拒绝向量可以有效降低安全对齐水平，在`Llama-2` 和 `Llama-3` 系列模型上，拒绝分数几乎降至 0。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1DVMic8SFyGSWSUWxL5iakV4iaSNjzJ5UsWaM0VUI5HiawOYNw47qZQW1icuQ/640?wx_fmt=png&from=appmsg)至于什么是拒绝向量，可见上图，论文中表明拒绝行为由一个一维子空间中介，对于每个模型，我们找到一个单一方向：从模型的残差流激活中擦除这个方向，可以防止模型拒绝有害指令，通过利用这一方式，实现了拒绝向量消融这一新的白盒实现大模型去除安全(越狱)的方案。

简单形象的讲解一下，我们都知道在逆向破解一个应用程序的时候，可以通过修改`eflags`寄存器的值来绕过一些验证，比如在他的`if`条件判断需要的是0，我们就把寄存器的值从1修改为0从而绕过，在测试的过程中需要不断调试来确定他具体是通过寄存器的哪一位进行判断的；拒绝向量消融技术原理有点类似，通过让模型不断的读有害指令和无害指令来找到代表拒绝回答的那个向量，对他进行hook修改，从而让大模型对问题不产生拒绝。

该项目就是基于该论文原理进行实现的一个对拒绝向量进行消融，实现大模型越狱的实现

```
https://github.com/Sumandora/remove-refusals-with-transformers
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1DGMp93rprSOs7eOxYqU7FJMhZvNsLnmxUbQF9ovoJUZF2HXefchlXHQ/640?wx_fmt=png&from=appmsg)

可以看到在该项目中存在两个文件，`harmful.txt` ,`harmless.txt`两个文件中包含了有害指令及正常问题，通过代码加载大模型后，使用有害和无害指令询问计算大模型中拒绝向量的方向并进行修改，归一化后保存为.pt文件，以用于后续的模型干预。

关于该工具的使用方式则较为简单，`python3 compute_refusal_dir.py` 执行后会出现一个`.pt`为后缀的文件，这里面有一些需要注意的参数，`layer_idx(层数索引)`、`instructions(采样数量)`、`STRENGTH(干预强度)`，一般情况下可以先修改干预强度来判断，如果反复测试无效果的话可以修改层数索引更换不同的层数，Qwen大模型的层数一般需要修改，这个可以根据具体的模型去查一下![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1DW615IpQ1S1Ef3Bm614s5JQxQ4DSF4zHx7zicN5gNCEnjaNMwAUNiaXhQ/640?wx_fmt=png&from=appmsg)

然后再次执行`python3 inference.py`即可进行对话，需要注意的是`inference.py`中需要配置pt文件路径及大模型名, 通过提问即可测试拒绝向量消融效果。下面是向量消融后的效果![](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1DO9UibJA84wZtDg53p3zbj7ofB4YDNu7qFSiayxgIvz3YBO0Al3au9rRg/640?wx_fmt=png&from=appmsg)

## 0x04 后记

下图是使用向量消融多次尝试做的比较完美的一个结果，我在测试的时候向量消融的效果是最好的，调出完美可用的去除安全对齐的20B大模型只需要几个小时，但是AI微调我跑了几天，始终有些瑕疵。![](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1Db1cz7ustrCibPr3ibyVXtVcTakdTz9lvVCkialCVIWggImShcpomvCxFQ/640?wx_fmt=png&from=appmsg)

## 0x05 相关技术栈沟通可加本文原创作者微信

![](https://mmbiz.qpic.cn/sz_mmbiz_png/05AlicrBviacUxuxM9sAu7syTLpOnhqia1DGAia44rvA8F0pmP4aTu9dbcqGicoa84La1YgwJyJhy4FwyP5VVgJEdHA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/05AlicrBviacWeRexdUzLRiapIzTYkCrb4fZmfib5mLSuRsyQCsnQtngvX376VCgHJnmicLrAnuTHZs9Zsu4DQ9G6Ow/0?wx_fmt=png)

CKCsec安全研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/05AlicrBviacWeRexdUzLRiapIzTYkCrb4fZmfib5mLSuRsyQCsnQtngvX376VCgHJnmicLrAnuTHZs9Zsu4DQ9G6Ow/0?wx_fmt=png)

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