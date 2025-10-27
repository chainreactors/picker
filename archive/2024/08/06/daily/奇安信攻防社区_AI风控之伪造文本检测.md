---
title: AI风控之伪造文本检测
url: https://forum.butian.net/share/3635
source: 奇安信攻防社区
date: 2024-08-06
fetch_date: 2025-10-06T18:01:38.521646
---

# AI风控之伪造文本检测

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### AI风控之伪造文本检测

* [安全工具](https://forum.butian.net/topic/53)

AIGC技术可能导致大量低质量、重复性和垃圾内容的产生，这些内容可能会淹没真正有价值的信息，影响用户的体验，并可能导致互联网整体的信任度下降。例如，一些AIGC平台可以根据用户输入的关键词或简介，自动生成小说、诗歌、歌词等文学作品，而这些作品很可能是对已有作品的抄袭或改编。
为此，在风控场景下也很多必要检测AI伪造文本。在本文中将分享一种有效的技术，用魔法打败魔法，我们用AI来检测AI。

前言
==
AIGC（Artificial Intelligence Generated Content，人工智能生成内容）技术通过机器学习和自然语言处理等手段，能够自动生成文本、图像、音频和视频等多种形式的内容。
![image-20240621105946733.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-0a04b46663457a26ffb93e449abc75efbbca89be.png)
虽然这项技术在提高内容创作效率和降低成本方面具有巨大潜力，但它也带来了一些关于信息质量下降的问题。
AIGC技术可能导致大量低质量、重复性和垃圾内容的产生，这些内容可能会淹没真正有价值的信息，影响用户的体验，并可能导致互联网整体的信任度下降。例如，一些AIGC平台可以根据用户输入的关键词或简介，自动生成小说、诗歌、歌词等文学作品，而这些作品很可能是对已有作品的抄袭或改编。
为此，在风控场景下也很多必要检测AI伪造文本。在本文中将分享一种有效的技术，用魔法打败魔法，我们用AI来检测AI。
在此之前，我们也可以试试已有的方法
比如我先用chatgpt生成一段文本
![image-20240621110437141.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-d891f6b0465068f6504e7a72dae009c7b9e0df98.png)
然后交给GPTZero检测
![image-20240621110454863.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-ed716e5a69229482463bc234d20db14e278fd8d0.png)
可以看到它也能较好检测出来，现在我们的目标就是自己实现类似的功能，方便针对所需的业务场景进行本地、高效、可靠部署。
背景知识
====
为了便于后续代码、实战的完整性，我们把所需的背景知识全部几种到这一部分
文本生成原理
------
AIGC（人工智能生成内容）技术的核心在于其背后的神经网络模型，这些网络模型通过大量的训练数据学习语言结构、文本风格和内容特征。最常见的神经网络架构包括循环神经网络（RNN）、长短时记忆网络（LSTM）、以及近年来备受瞩目的转换器模型。这些模型能够通过学习大量的文本数据，掌握语言的语法、语义和上下文理解，从而生成与训练数据相似的内容。
更进一步地，输入文本经过分词器处理，生成 token\\_id 输出，其中每个 token\\_id 被分配为唯一的数值表示。 分词后的输入文本被传递给预训练模型的编码器部分。编码器处理输入并生成一个特征表示，该表示编码了输入的含义和上下文。编码器是在大量数据上进行训练的。 解码器获取编码器生成的特征表示，并根据这个上下文逐个 token 地生成新文本。它利用先前生成的 token 来创建新的 token。
![image-20240621110701899.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-889da3f794383a52b6f7d791a8d433b5c71fcd7e.png)
现在深入一点。假设我们想生成继续短语“Paris is the city ...”。编码器发送所有我们拥有的 token 的 logit 值），这些 logit 值可以通过 softmax 函数转换为选择该 token 用于生成的概率。 如果看一下前5个输出的 token，它们都是有意义的。我们可以生成以下听起来合理的短语： Paris is the city of love. Paris is the city that never sleeps. Paris is the city where art and culture flourish. Paris is the city with iconic landmarks. Paris is the city in which history has a unique charm. 现在的挑战是选择适当的 token。有几种策略可以使用
![image-20240621110831931.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-4703807dbe00aecd004e4ff369cd7e47ab00d62b.png)
比如使用贪婪采样
![image-20240621110946476.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-e446d3e3109542e32fd4c7c0bd0583f4004dfdd8.png)
在贪婪策略中，模型在每一步总是选择它认为最有可能的 token —— 它不考虑其他可能性或者探索不同的选项。模型选择具有最高概率的 token，并基于所选的选择继续生成文本。使用贪婪策略在计算上是高效且直接的，但有时会导致重复或过于确定性的输出。因为模型在每一步只考虑最有可能的 token，它可能无法捕捉上下文和语言的全部多样性，或产生最具创造性的回应。模型的短视特性仅关注每一步中最可能的 token，而忽略整个序列的整体影响。 生成的输出：Paris is the city of the future.
再比如束搜索Beam search
![image-20240621111035846.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-4de4635d5f1099d35898156fc9e39f78a4bb964b.png)
这是文本生成中使用的另一种策略。在beam search中，模型不仅仅考虑每一步最可能的 token，而是考虑一组前 "k" 个最有可能的 token。这组 k 个 token 被称为一个 "beam"。模型为每个 token 生成可能的序列，并通过扩展每个 beam 来跟踪它们在每一步文本生成中的概率。
这个过程会持续进行，直到达到所需长度的生成文本，或者在每个 beam 中遇到一个 "end" token。模型从所有 beam 中选择具有最高整体概率的序列作为最终输出。
从算法的角度来看，创建 beams 就像是展开一个 k 叉树。创建 beams 后，你选择具有最高整体概率的分支作为最终输出。
生成的输出：Paris is the city of history and culture.
DeBERTa
-------
DeBERTaV3是一种先进的自然语言处理（NLP）预训练模型，它是DeBERTa系列模型的第三个版本。DeBERTaV3在模型架构上并没有进行重大修改，而是在预训练任务上进行了创新。它采用了类似于ELECTRA的预训练任务，称为Replaced Token Detection（RTD），取代了传统的掩码语言模型（MLM）。RTD任务通过生成器和判别器的对抗训练来提高模型的性能，其中生成器负责生成不确定的结果以替换输入序列中的掩码标记，而判别器则需要判断对应的token是原始token还是被生成器替换的token。
![image-20240621111402060.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-a82a99d291c3e12340d2d29d00746eb8ac4f0b5f.png)
此外，DeBERTaV3还提出了词向量梯度分散共享的方法，优化了生成器和判别器词向量共享，避免了在共享过程中产生激烈竞争。这种方法有助于模型更有效地捕捉单词的语义信息，从而在下游NLP任务中取得更好的表现。
DeBERTaV3在多个NLP任务上展现出了优异的性能，例如在SQuAD 2.0和MNLI任务上的表现均优于先前的DeBERTa版本. 这使得DeBERTaV3成为了NLP领域中一个重要的模型，广泛应用于各种自然语言理解任务中。
实战
==
依赖
--
首先导入必要的依赖库文件
```php
import os
os.environ["KERAS\_BACKEND"] = "jax"
import keras\_nlp
import keras\_core as keras
import keras\_core.backend as K
import torch
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
cmap = mpl.cm.get\_cmap('coolwarm')
```
1. \*\*设置环境变量\*\*：
- 代码通过设置 `os.environ["KERAS\_BACKEND"] = "jax"` 将环境变量 `KERAS\_BACKEND` 设为 `"jax"`。这表明代码打算使用 JAX 作为 Keras 的后端。JAX 是一个由Google开发的数值计算库，特别适合在具有加速器（如GPU）的设备上进行高性能的机器学习操作。
2. \*\*导入Keras相关库\*\*：
- `keras\_nlp` 库暗示代码可能涉及使用 Keras 进行自然语言处理任务。
- `keras\_core` 作为 `keras` 别名导入，可能是Keras功能的核心模块。
- `keras\_core.backend` 导入为 `K`，可能提供了对Keras后端功能的访问。
3. \*\*导入PyTorch库\*\*：
- `import torch` 导入了 PyTorch 库。PyTorch 是另一个流行的深度学习框架，以其灵活性和效率而闻名，特别适用于神经网络。
4. \*\*其他导入\*\*：
- `import tensorflow as tf`：导入 TensorFlow 库，是一个广泛用于机器学习和深度学习的框架。
- `import numpy as np` 和 `import pandas as pd`：导入 NumPy 和 Pandas 库，分别用于数值计算和数据操作。
- `import matplotlib.pyplot as plt` 和 `import matplotlib as mpl`：导入 Matplotlib 库，用于数据可视化。
5. \*\*颜色映射设置\*\*：
- `cmap = mpl.cm.get\_cmap('coolwarm')`：设置颜色映射为 'coolwarm'，这是 Matplotlib 中的一种颜色映射方式，通常用于绘制热图等可视化任务。
将相关的配置设置好
```php
class CFG:
verbose = 0
wandb = True
\_wandb\_kernel = 'awsaf49'
comment = 'DebertaV3-MaxSeq\_200-ext\_s-torch'
preset = "deberta\_v3\_base\_en"
sequence\_length = 200
device = 'TPU'
seed = 42
num\_folds = 5
selected\_folds = [0, 1]
epochs = 3
batch\_size = 3
drop\_remainder = True
cache = True
scheduler = 'cosine'
class\_names = ["real", "fake"]
num\_classes = len(class\_names)
class\_labels = list(range(num\_classes))
label2name = dict(zip(class\_labels, class\_names))
name2label = {v: k for k, v in label2name.items()}
```
这段代码定义了一个名为 `CFG` 的类，该类包含了一些配置参数和常量：
1. \*\*verbose\*\*:
- 设置为 `0`，通常用于控制输出信息的详细程度，这里设为静默模式。
2. \*\*wandb\*\*:
- 设置为 `True`，表示是否启用了 WandB（Weights &amp; Biases）的功能，用于跟踪和可视化训练过程中的指标和结果。
3. \*\*\\_wandb\\_kernel\*\*:
- 一个字符串 `\_wandb\_kernel = 'awsaf49'`，可能是用于连接到特定的 WandB 服务或项目。
4. \*\*comment\*\*:
- 设置为 `'DebertaV3-MaxSeq\_200-ext\_s-torch'`，可能是用来描述或标识当前配置的一个注释或标记。
5. \*\*preset\*\*:
- 设置为 `"deberta\_v3\_base\_en"`，可能是指定了某种预设的模型或配置，这里可能是 DeBERTa V3 的一个基础配置。
6. \*\*sequence\\_length\*\*:
- 设置为 `200`，指定了序列的长度，这在处理序列数据（如文本）时很常见。
7. \*\*device\*\*:
- 设置为 `'TPU'`，指明了训练时使用的设备，即谷歌的 TPU（Tensor Processing Unit），用于加速深度学习模型的训练。
8. \*\*seed\*\*:
- 设置为 `42`，用作随机数种子，可以确保随机数生成的可重复性。
9. \*\*num\\_folds\*\* 和 \*\*selected\\_folds\*\*:
- `num\_folds` 设置为 `5`，表示交叉验证时的折数。
- `selected\_folds` 设置为 `[0, 1]`，表示选择参与训练的交叉验证折数索引。
10. \*\*epochs\*\* 和 \*\*batch\\_size\*\*:
- `epochs` 设置为 `3`，表示训练的轮数。
- `batch\_size` 设置为 `3`，表示每个批次的样本数。
- `drop\_remainder` 设置为 `True`，表示在最后一个批次不足 `batch\_size` 时是否丢弃剩余的样本。
- `cache` 设置为 `True`，用于在每次迭代后缓存数据，通常在使用 TPU 时避免 Out Of Memory（内存不足）错误。
11. \*\*scheduler\*\*:
- 设置为 `'cosine'`，可能指定了学习率调度器的类型，这里是余弦退火调度器。
12. \*\*class\\_names\*\*, \*\*num\\_classes\*\*, \*\*class\\_labels\*\*, \*\*label2name\*\*, \*\*name2label\*\*:
- `class\_names` 设置为 `["real", "fake"]`，是类别的名称列表。
- `num\_classes` 根据 `class\_names` 的长度确定，表示类别的数量。
- `class\_labels` 是从 `0` 到 `num\_classes-1` 的类别标签列表。
- `label2name` 是一个字典，将类别标签映射到类别名称。
- `name2label` 是一个字典，将类别名称映射到类别标签。
接下来设置加速器
```php
def get\_device():
"Detect and intializes GPU/TPU automatically"
try:
tpu = tf.distribute.cluster\_resolver.TPUClusterResolver()
tf.tpu.experimental.initialize\_tpu\_system(tpu)
strategy = tf.distribute.TPUStrategy(tpu)
print(f'> Running on TPU', tpu.master(), end=' | ')
print('Num of TPUs: ', strateg...