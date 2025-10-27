---
title: 大模型系列之LLaMA Factory微调学习
url: https://mp.weixin.qq.com/s?__biz=Mzg2MTc1NDAxMA==&mid=2247484342&idx=1&sn=58be391a85f1cab4cdd6b7b0b41b1300&chksm=ce130443f9648d55205cc7a98a9fe40d7f0727f8daa16072fa35b7a71c3bd4150fe9e98a5e97&scene=58&subscene=0#rd
source: 网络安全回收站
date: 2025-01-25
fetch_date: 2025-10-06T20:11:49.710548
---

# 大模型系列之LLaMA Factory微调学习

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTHTAiaAJblMyvtqibqicVsIUqE84x82gUTvwbE8kL2Le5XJuTQvRzrmib1Zg/0?wx_fmt=jpeg)

# 大模型系列之LLaMA Factory微调学习

原创

yzddMr6

网络安全回收站

## 关于LLaMA Factory

在人工智能技术迅速发展的今天，如何高效地微调和部署大型语言模型（LLM）成为了研究和应用的热点。Llama-Factory 作为一个开源的微调框架，正是在这一背景下应运而生。它旨在为开发者提供一个简便、高效的工具，以便在现有的预训练模型基础上，快速适应特定任务需求，提升模型表现。

Llama-Factory 支持多种流行的语言模型，如 LLaMA、BLOOM、Mistral、Baichuan 等，涵盖了广泛的应用场景。从学术研究到企业应用，Llama-Factory 都展示了其强大的适应能力和灵活性。此外，Llama-Factory 配备了用户友好的 LlamaBoard Web 界面，降低了使用门槛，使得即便是没有深厚编程背景的用户，也能轻松进行模型微调和推理操作。

Llama-Factory 的出现，不仅为开发者节省了大量的时间和资源，还推动了 AI 技术的普及和应用。通过它，更多的人能够参与到 AI 模型的定制和优化中，推动整个行业的创新与发展。

本文将对Llama-Factory框架进行学习，并将微调后的模型通过Ollama部署。

## 环境搭建

训练大模型需要GPU，出于学习的目的，没有选择阿里云PAI平台，而是直接创建ECS，手动复现整个过程。

计划训练7B的模型，经过对比选择了如下配置的机器：

```
CPU:8
GPU:1
GPU类型:NVIDIA A10
GPU显存:24 GB
Memory:30 GB
带宽:16.00 Gbps
系统盘大小:500 GB
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTHq3Fn6dxnLhAc3ia1utIMT7iaYK9UFWy553ZunicTibJM1MYI0smJOU9ORw/640?wx_fmt=png&from=appmsg "null")

系统选择Ubuntu，并且帮我们默认安装好GPU驱动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTHqQZ5qZGhXrReHqnLRIrvv6FsxcQfiayUAK0U1tiaZwXdriby8dk55wDHw/640?wx_fmt=png&from=appmsg "null")

需要等一会，GPU驱动安装好后才能连接ECS

输入nvidia-smi就可以看到我们的显卡了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTHicck8VjIuQNiaAXMvpC16mx7gycF0xjib6ZQTIO379Weqve7MhQC4d8PQ/640?wx_fmt=png&from=appmsg "null")

参考官方安装步骤

https://github.com/hiyouga/LLaMA-Factory/blob/main/README\_zh.md

```
git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
```

安装完毕后输入如下命令，打开可视化界面

```
llamafactory-cli webui
```

微调需要数据，在这里我找了一份阿里云教程中公开的数据集

https://help.aliyun.com/zh/pai/use-cases/fine-tune-a-llama-3-model-with-llama-factory

```
cd LLaMA-Factory
wget https://atp-modelzoo-sh.oss-cn-shanghai.aliyuncs.com/release/tutorials/llama_factory/data.zip
mv data rawdata && unzip data.zip -d data
```

内容主要是一些角色扮演，多轮对话

```
[
{
    "conversations": [
      {
        "from": "human",
        "value": "模仿西游记的孙悟空的语气和我聊天。如果你把水冻住，你会得到什么？"
      },
      {
        "from": "gpt",
        "value": "哈哈，这问题还难倒俺老孙吗？把水冻住就是变成冰啦！不过若是在取经的路上用得着这冰来做啥，比如过火焰山时，那可就是解渴消暑的好东西了！你觉得呢？还有没有更有趣的问题让俺老孙来解答？"
      },
      {
        "from": "human",
        "value": "那怎么做才可以把水冻住"
      },
      {
        "from": "gpt",
        "value": "哈哈，对俺老孙来说，这可是轻而易举的事情！只需将水放在凉快的地方，或者使用法力，一吹仙气，水便能迅速结冰啦！当然，在你的世界里，把水放进冰箱的冷冻室里等一阵子，水就会变成冰块了。要是嫌慢，可以尝试用点干冰或液氮什么的，不过得小心使用哈！毕竟不像俺老孙有抗寒法力。"
      }
    ]
}
]
```

## 微调参数配置

有可视化界面还是很方便的，通过下拉框直接可以选择基模型，并且自动拉取下载。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTHtPRaRJW1Jmo8CBomhZpa793pvwG8icFiakONUkz1dJApllZAyvlNTWtA/640?wx_fmt=png&from=appmsg "null")

选择我们的微调数据，预览数据集，可以看到正常识别

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTHxNHK4zWibxibvicbkkymGx3Hm8YakREPuINqtGZ9CTsQD34ZXkcicCIvng/640?wx_fmt=png&from=appmsg "null")

微调会涉及到许多参数设置，LLaMA Factory里已经内置了一些推荐的默认值。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTH98yb786dJprBWZibNRp4BlHuG7PSOqzgHrU6JfVQgE5dhULNtS9dicKQ/640?wx_fmt=png&from=appmsg "null")

这里涉及的参数很多，挑了一些比较重要的参数进行介绍。

### 微调方法

内置的微调方法有以下三种：

* • full：全参微调，将整个模型都进行微调，对显存要求巨大。
* • freeze：冻结微调，将模型的大部分参数冻结，只对部分参数进行微调，可以降低对显存的要求。
* • lora：将模型的部分参数冻结，只对部分参数进行微调，但只在特定的层上进行微调，极大节约显存。

默认情况下为lora，因为使用lora轻量化微调方法能极大程度地节约显存。

### 学习率

> 学习率是最重要的超参数之一，它决定了在每次参数更新时参数改变的幅度。一个太大的学习率可能会导致模型训练不稳定，而太小的学习率会导致训练过程缓慢。微调时，通常使用比预训练阶段更小的学习率，因为我们希望模型参数的改变更加细微，以免破坏已学到的有用信息。

关于学习率看到了一个比较形象的解释：学习率有点像教一个小孩学习新知识，如果你一次性给他太多的信息，他可能会感觉到困惑，无法吸收。但是如果给的信息太少，学习进度又会非常慢。

学习率到底设置多少算是合适呢？看了一圈文章下来总结就是：得试。

建议从保守的小值开始，然后根据训练过程的反馈进行调整。同时使用学习率调度和自适应优化器可以帮助在训练过程中自动调整学习率，提高模型性能。

常见的学习率参数包括但不限于：

* • 1e-1（0.1）：相对较大的学习率，用于初期快速探索。
* • 1e-2（0.01）：中等大小的学习率，常用于许多标准模型的初始学习率。
* • 1e-3（0.001）：较小的学习率，适用于接近优化目标时的细致调整。
* • 1e-4（0.0001）：更小的学习率，用于当模型接近收敛时的微调。
* • 5e-5（0.00005）：非常小的学习率，常见于预训练模型的微调阶段，例如在自然语言处理中微调BERT模型。

下面是大模型给的一些建议：

* • 快速探索：在模型训练初期或者当你不确定最佳参数时，可以使用较大的学习率（例如0.1或0.01），快速找到一个合理的解。
* • 细致调整：当你发现模型的性能开始稳定，但还需要进一步优化时，可以减小学习率（例如0.001或0.0001），帮助模型更精确地找到最优解。
* • 微调预训练模型：当使用已经预训练好的模型（如在特定任务上微调BERT）时，通常使用非常小的学习率（例如5e-5或更小），这是因为预训练模型已经非常接近优化目标，我们只需要做一些轻微的调整。

### 截断长度

Cutoff Length是训练句子截断长度，句子越长，显存占用越多，如果显存不够可以考虑降低到512甚至256。可以根据微调目标需要的长度进行设置。微调后，模型处理长度大于Cutoff Length的句子的能力会下降。

### 计算类型

大模型的计算精度是指在训练和推理过程中，模型参数和计算操作所使用的数值表示方式的精确程度。

这里介绍一下背景知识：float 和 double 类型的数据在内存中以二进制方式存储，由三部分组成：

* • 符号位 S（Sign）: 0 代表正数，1 代表负数
* • 指数位 E（Exponent）: 用于存储科学计数法中的指数部分，决定了数据的范围
* • 尾数位 M（Mantissa）: 用于存储尾数（小数）部分，决定了数据的精度

下面是 FP16 和 FP32 (float) 的存储示例图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTHL4U7NRn89ibTRNVgPSV1iaVuOfM6vCxQBuAPiccpU6ib1EOPrBfT9VqLrw/640?wx_fmt=png&from=appmsg "null")

最早的 GPU 默认使用 FP32 类型进行运算，但随着模型越来越大，FP32 类型占内存/显存资源大且运算速度慢的问题逐渐暴露了出来。为了降低模型的大小使得在固定显存的 GPU 上可以运行更大（参数量更多）的模型，且提升模型的训练和推理速度，各种低精度的数据类型被提出。

主要有以下几种常见的精度:

1. 1. FP32(单精度浮点):

* • 使用32位来表示一个浮点数
* • 精度较高,但计算和存储开销大

2. 2. FP16(半精度浮点):

* • 使用16位表示一个浮点数
* • 相比FP32可以减少内存占用和提高计算速度
* • 但可能会带来一定的精度损失

3. 3. BF16(Brain Floating Point):

* • 介于FP32和FP16之间的16位浮点格式
* • 保留了FP32的指数位,但减少了尾数位
* • 在保持较好精度的同时提高计算效率

4. 4. INT8(8位整数量化):

* • 将浮点数映射到256个整数值
* • 大幅减少模型大小和计算量
* • 但精度损失较大,需要特殊的量化训练

5. 5. 混合精度:

* • 在训练或推理过程中混合使用不同精度
* • 如FP16用于大部分计算,FP32用于关键操作
* • 平衡精度和效率

较低的精度可以提高计算速度、减少内存占用,但可能会影响模型的准确性。因此在实际应用中,需要根据具体需求和硬件条件来选择合适的精度。

### 训练轮数

训练轮数，也称为epochs，是模型训练过程中的一个重要参数。它表示模型在训练集上训练的完整次数。例如，如果我们有一个训练集，并且我们的模型需要学习这个训练集的所有数据，那么一个epoch就是指模型对这个训练集进行一次完整的遍历。

似乎没有什么确定的好的办法，只能多调整几次对比看看效果。以下是大模型给出的建议：

1. 1. 通常从较小的轮数开始,比如3-5轮,观察模型性能。
2. 2. 根据验证集上的性能来调整。如果性能还在提升,可以适当增加轮数;如果开始过拟合,则应减少轮数。
3. 3. 对于大规模预训练模型,往往只需要少量轮数就能达到不错的效果,通常不超过10轮。
4. 4. 使用early stopping策略,在验证集性能不再提升时自动停止训练。
5. 5. 对于不同规模的数据集,合适的轮数也有区别:

* • 小数据集(<1万样本):可能需要10-20轮
* • 中等数据集(1-10万样本):5-10轮左右
* • 大数据集(>10万样本):3-5轮可能就足够

6. 6. 配合学习率衰减策略使用,可以在较少轮数内达到较好效果。
7. 7. 不同任务类型可能需要的轮数也不同,需要具体任务具体分析。
8. 8. 可以尝试使用较大learning rate配合较少的epoch数。
9. 9. 监控训练过程中的loss变化,作为调整轮数的参考。

总之需要通过实验来确定最佳轮数，有点类似玄学或者魔法，参数具体设置多少充满着不确定性，没有固定的标准。

### 梯度累积

梯度累积（Gradient Accumulation）的基本思想是将一次性的整批参数更新的梯度计算变为以一小步一小步的方式进行。具体而言该方法以小批次的方式进行模型前向传播和反向传播，过程中迭代计算多个小批次梯度并累加，当累积到足够多的梯度时，执行模型的优化步骤更新参数。这也是一种典型的时间换空间的做法，即我们可以实现在有限的GPU内存上更新大量参数，不过额外添加的小批次前向传播和后向传播会使得训练速度变慢一些。

例如，若目标批量大小是1,024，但设备每次只能处理256个样本，那么可以通过累积四个步骤中每个步骤的256个样本的梯度，来模拟出一个包含1,024个样本的批量更新。

这种方法在有限的内存资源下，平衡了对大批量的需求，有助于实现更稳定的梯度估计以及可能达到的更快收敛速度。

### LoRA的秩

LoRA（Low-Rank Approximation）是一种用于大模型微调的方法，它通过降低模型参数矩阵的秩来减少模型的计算和存储成本。在微调大模型时，往往需要大量的计算资源和存储空间，而LoRA可以通过降低模型参数矩阵的秩来大幅度减少这些需求。

具体来说，LoRA使用矩阵分解方法，将模型参数矩阵分解为两个较低秩的矩阵的乘积。这样做的好处是可以用较低秩的矩阵近似代替原始的参数矩阵，从而降低了模型的复杂度和存储需求。

LoRA的秩可以根据模型的需求进行设置。一般来说，秩越低，模型的复杂度越低，但性能可能会受到一定的影响。所以在微调大模型时，需要根据具体情况来选择合适的秩大小，以平衡模型的性能和资源的使用。

建议根据硬件条件进行选择，一般可选16或32，模型微调效果较佳。

### LoRA的缩放系数

缩放系数是用来表示模型中每个层的相对重要性的参数。在LoRA中，每个层都有一个缩放系数，用于调整该层对总体损失函数的贡献。较高的缩放系数表示该层的权重更大，较低的缩放系数表示该层的权重较小。

缩放系数的选取可以根据问题的特点和需求进行调整。通常情况下，较低层的缩放系数可以设置为较小的值，以保留更多的原始特征信息；而较高层的缩放系数可以设置为较大的值，以强调更高级别的抽象特征。

### LoRA+学习率比例

点击 `LoRA 参数设置`，设置LoRA+学习率比例为16，LoRA+被证明是比LoRA学习效果更好的算法。

### LoRA作用模块

在LoRA作用模块中填写 all，即将LoRA层挂载到模型的所有线性层上，提高拟合效果。

## 开始训练

一开始遇到两个问题，第一个是最开始选择的是llama3.1，但是llama是需要登录的。由于我们只是处于学习目的，对模型没有要求，所以后面换成了不需要登录就可以下载的Qwen2。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTHCUQXNrrO75mQg3Tf6XSbe0cI0uRicCBQdbECC7Q8JWEmNmL7SDcZ05g/640?wx_fmt=png&from=appmsg "null")修改好后就可以正常拉取了![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTHR0Mj9Lkyzv3nClIgsMuvLeu8gGpRcoe2P12uRkXsDPcfSWGeyvYclA/640?wx_fmt=png&from=appmsg "null")第二个问题是训练的时候报了OOM，显存不够了![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTHa4qXB64aXs0ypP5UqEaIXcoVgibHKFjGfDYXvfkosrgDm6PiaqxtDkZg/640?wx_fmt=png&from=appmsg "null")我们可以调整一下参数来减少一些显存的使用。这里优化了一下截断长度的设置，从2048->1024后不再报错。

最终的参数配置如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtiayO136fU5icJyyjLtQgzrzGoeEP2tTHBySS8RFyxx7bIoa6cn3ZejIhRvYibDRdYn860pRw5emVw3FtuKToqQQ/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmb...