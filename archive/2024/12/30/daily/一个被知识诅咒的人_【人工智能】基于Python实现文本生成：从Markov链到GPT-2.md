---
title: 【人工智能】基于Python实现文本生成：从Markov链到GPT-2
url: https://blog.csdn.net/nokiaguy/article/details/144800462
source: 一个被知识诅咒的人
date: 2024-12-30
fetch_date: 2025-10-06T19:34:56.554608
---

# 【人工智能】基于Python实现文本生成：从Markov链到GPT-2

# 【人工智能】基于Python实现文本生成：从Markov链到GPT-2

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)Python实现Markov链与GPT-2文本生成对比

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2025-01-09 16:48:31 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.1k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

16

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
23

CC 4.0 BY-SA版权

分类专栏：
[Python杂谈](https://blog.csdn.net/nokiaguy/category_12800257.html)
[人工智能](https://blog.csdn.net/nokiaguy/category_1260139.html)
文章标签：
[人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[gpt](https://so.csdn.net/so/search/s.do?q=gpt&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-12-29 10:06:00 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/144800462>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
同时被 2 个专栏收录![](https://csdnimg.cn/release/blogv2/dist/pc/img/newArrowDown1White.png)](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756780.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

人工智能](https://blog.csdn.net/nokiaguy/category_1260139.html "人工智能")

195 篇文章

订阅专栏

文本生成是自然语言处理（NLP）中的一个重要研究方向，随着技术的发展，文本生成的质量也在不断提高。本文将介绍如何基于Python实现文本生成，首先通过经典的Markov链生成文本，并分析其原理和实现。然后，文章将深入探讨现代自然语言生成模型——GPT-2，并展示如何通过Python使用GPT-2生成高质量文本。文章将通过大量的代码示例进行说明，并提供中文注释，帮助读者理解从Markov链到GPT-2的文本生成过程，适合有一定Python和机器学习基础的读者。

---

#### 1. **引言**

文本生成是自然语言处理（NLP）中的一个关键任务，广泛应用于自动写作、对话系统、机器翻译等领域。在文本生成任务中，生成模型的目标是根据一定的输入（通常是一个种子文本）生成连贯、符合语法且有意义的文本。

传统的文本生成方法，如基于Markov链的方法，虽然简单且计算开销小，但生成的文本质量较低，通常只适合短文本生成。而近年来，基于深度学习的模型，如GPT-2（Generative Pretrained Transformer 2），已经取得了显著进展，可以生成长篇、语法通顺且具有一定上下文理解的文本。本文将逐步介绍如何通过Python实现文本生成，并比较Markov链和GPT-2的生成效果。

#### 2. **Markov链简介**

Markov链是一种数学模型，用于描述一个系统在不同状态之间的转移过程。在文本生成中，Markov链的思想是通过当前状态（当前词语或字符）来预测下一个状态（下一个词语或字符）。具体来说，Markov链假设文本的生成过程只依赖于当前状态，未来状态的概率仅与当前状态有关，而与过去的历史状态无关。

##### 2.1 Markov链的实现

我们将通过一个简单的Python实现来展示如何使用Markov链生成文本。首先，我们需要对一段文本进行处理，提取词语之间的转移概率。

```
import random

# 读取文本数据
def read_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

# 构建Markov链模型
def build_markov_chain(text, n=2):
    markov_chain = {}
    words = text.split()

    for i in range(len(words) - n):
        key = tuple(words[i:i+n-1])
        value = words[i+n-1]

        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(value)

    return markov_chain

# 使用Markov链生成文本
def generate_text(markov_chain, length=50):
    # 从Markov链的任意起始状态开始
    start_key = random.choice(list(markov_chain.keys()))
    generated_words = list(start_key)

    for i in range(length - len(start_key)):
        current_key = tuple(generated_words[-(len(start_key)):])
        if current_key in markov_chain:
            next_word = random.choice(markov_chain[current_key])
            generated_words.append(next_word)
        else:
            break  # 如果找不到下一个词，生成结束

    return ' '.join(generated_words)

# 读取文本数据
text = read_text('sample.txt')  # 请将此路径替换为实际的文本文件路径
# 构建Markov链
markov_chain = build_markov_chain(text, n=2)
# 生成文本
generated_text = generate_text(markov_chain, length=50)
print(generated_text)
```

##### 2.2 代码解析

* **read\_text**：从文件中读取文本数据。
* **build\_markov\_chain**：根据文本数据生成Markov链。在此例中，`n=2`表示我们使用二元模型（bigram），即通过前一个词预测下一个词。
* **generate\_text**：根据生成的Markov链生成指定长度的文本，随机从Markov链的起始状态开始，并根据当前状态选择下一个词。

生成的文本通常会包含很多不连贯的部分，这是由于Markov链只是基于词与词之间的概率关系进行生成的，缺乏对上下文的深层理解。

#### 3. **GPT-2简介**

GPT-2（Generative Pretrained Transformer 2）是一个基于Transformer架构的预训练生成模型，由OpenAI提出。它的强大之处在于通过大量的语料库进行预训练，然后通过微调来生成高质量的文本。与Markov链不同，GPT-2能够捕捉到长距离的依赖关系，并生成连贯且有语法意义的长篇文本。

##### 3.1 GPT-2模型实现

为了使用GPT-2进行文本生成，我们可以通过Hugging Face的`transformers`库进行实现。以下是如何通过Python使用GPT-2生成文本的示例代码：

```
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# 加载预训练的GPT-2模型和Tokenizer
model_name = "gpt2"  # 可以选择gpt2-medium, gpt2-large等更大的版本
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# 编码输入文本
input_text = "Python is a powerful"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# 生成文本
output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.95, top_k=60)

# 解码并输出生成的文本
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
```

##### 3.2 代码解析

* **model\_name**：加载GPT-2的预训练模型，可以选择不同大小的模型（如`gpt2-medium`、`gpt2-large`等）。
* **input\_text**：输入的种子文本。GPT-2将根据这个文本生成后续的内容。
* **model.generate**：调用GPT-2模型的`generate`方法来生成文本。`max_length`指定生成文本的最大长度，`num_return_sequences`指定返回生成的文本数量，`no_repeat_ngram_size`限制重复的n-grams，`top_p`和`top_k`用于控制生成文本的多样性和随机性。

#### 4. **Markov链与GPT-2的比较**

Markov链和GPT-2的生成方式存在显著差异。Markov链是基于前一个状态的转移概率来生成文本的，而GPT-2则是通过深度学习模型从大量数据中学习语言的语法和语义规则，能够生成更长、更连贯的文本。

| 特性 | Markov链 | GPT-2 |
| --- | --- | --- |
| **模型复杂度** | 简单、基于概率的模型 | 复杂、基于Transformer架构 |
| **上下文理解** | 仅依赖于前一个词或字符 | 理解长距离依赖关系，生成长文本 |
| **生成质量** | 文本通常较为简单和无意义 | 生成连贯、语法正确的文本 |
| **计算资源** | 低 | 高，需要大量计算资源 |

#### 5. **总结与展望**

本文介绍了两种基于Python的文本生成方法：经典的Markov链和现代的GPT-2模型。Markov链虽然简单易懂，但由于其局限性，生成的文本通常缺乏上下文连贯性和语法正确性。而GPT-2则通过强大的预训练和生成能力，能够生成高质量的文本，适用于各种复杂的应用场景。

随着自然语言生成技术的不断发展，未来将有更多基于深度学习的模型出现，例如GPT-3等，这些模型将能够生成更自然、更人性化的文本，广泛应用于写作助手、自动对话系统等领域。

---

#### 6. **附录：数学公式**

在介绍文本生成的过程中，我们提到了一些基本的数学概念，尤其是在Markov链模型中。为了更好地理解这些概念，接下来我们将详细阐述相关的数学公式。

##### 6.1 Markov链的转移矩阵

在Markov链模型中，状态转移是通过一个转移概率矩阵来描述的。设有一组状态 {S1,S2,…,Sn}\{S\_1, S\_2, \dots, S\_n\}{S1​,S2​,…,Sn​}，从状态 SiS\_iSi​ 到状态 SjS\_jSj​ 的转移概率为 P(Sj∣Si)P(S\_j | S\_i)P(Sj​∣Si​)。在文本生成的场景中，每个状态可以看作是一个词，而转移矩阵描述了词与词之间的转移概率。

我们可以通过转移概率矩阵 P\mathbf{P}P 来表示：

P=[P(S1∣S1)P(S2∣S1)…P(Sn∣S1)P(S1∣S2)P(S2∣S2)…P(Sn∣S2)⋮⋮⋱⋮P(S1∣Sn)P(S2∣Sn)…P(Sn∣Sn)]
\mathbf{P} = \begin{bmatrix}
P(S\_1|S\_1) & P(S\_2|S\_1) & \dots & P(S\_n|S\_1) \\
P(S\_1|S\_2) & P(S\_2|S\_2) & \dots & P(S\_n|S\_2) \\
\vdots & \vdots & \ddots & \vdots \\
P(S\_1|S\_n) & P(S\_2|S\_n) & \dots & P(S\_n|S\_n)
\end{bmatrix}
P=​P(S1​∣S1​)P(S1​∣S2​)⋮P(S1​∣Sn​)​P(S2​∣S1​)P(S2​∣S2​)⋮P(S2​∣Sn​)​……⋱…​P(Sn​∣S1​)P(Sn​∣S2​)⋮P(Sn​∣Sn​)​​

这个矩阵中的每一行表示从某个状态出发，到其他状态的概率。为了生成文本，我们可以通过计算从某个词开始，基于已知的词序列（上下文）来预测下一个词的概率。

##### 6.2 生成文本的概率模型

在生成文本时，我们需要通过计算当前词和下一个词的条件概率，来选择最可能的下一个词。对于给定的状态（例如当前词 wtw\_twt​），下一个词 wt+1w\_{t+1}wt+1​ 的概率可以表示为：

P(wt+1∣wt)=C(wt,wt+1)C(wt)
P(w\_{t+1} | w\_t) = \frac{C(w\_t, w\_{t+1})}{C(w\_t)}
P(wt+1​∣wt​)=C(wt​)C(wt​,wt+1​)​

其中 C(wt,wt+1)C(w\_t, w\_{t+1})C(wt​,wt+1​) 表示词 wtw\_twt​ 后面紧跟着词 wt+1w\_{t+1}wt+1​ 的次数，而 C(wt)C(w\_t)C(wt​) 是词 wtw\_twt​ 出现的总次数。这个概率可以用来构建Markov链的状态转移，从而生成一个新的文本序列。

##### 6.3 GPT-2模型：自回归生成

GPT-2（Generative Pretrained Transformer 2）是一种基于Transformer架构的自回归生成模型。自回归生成模型的核心思想是利用已有的文本序列（上下文）来预测下一个单词（或字符）。在GPT-2中，输入的文本序列 X=[x1,x2,…,xt]X = [x\_1, x\_2, \dots, x\_t]X=[x1​,x2​,…,xt​] 被用来预测下一个单词 xt+1x\_{t+1}xt+1​，并且通过条件概率分布进行生成：

P(xt+1∣x1,x2,…,xt)=softmax(Wht+b)
P(x\_{t+1} | x\_1, x\_2, \dots, x\_t) = \text{softmax}(W h\_t + b)
P(xt+1​∣x1​,x2​,…,xt​)=softmax(Wht​+b)

其中 hth\_tht​ 是通过Transformer网络计算得到的隐藏状态，WWW 是权重矩阵，bbb 是偏置项，softmax\text{softmax}softmax 是将输出转换为概率分布的激活函数。GPT-2通过自回归的方式不断生成新词，直到达到预设的文本长度或生成结束符号。

##### 6.4 语言模型的损失函数

GPT-2模型的训练过程中，我们使用最大化条件概率的方式来训练模型，这就需要用到交叉熵损失函数...