---
title: 从0实现网络安全“小”模型.md
url: https://buaq.net/go-171521.html
source: unSafe.sh - 不安全
date: 2023-07-09
fetch_date: 2025-10-04T11:51:19.911032
---

# 从0实现网络安全“小”模型.md

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/370220a4809918310b22dbb269b087f9.jpg)

从0实现网络安全“小”模型.md

自从chatgpt发布后一直关注如何和网络安全融合，最近一直在学习GPT相关内容，传统的用文本向量相似度索引的方式局限太大。所以想到自己训练或微调，受限于算力，很多地方都不好验证，于是想做一个本
*2023-7-8 14:41:8
Author: [x.hacking8.com(查看原文)](/jump-171521.htm)
阅读量:71
收藏*

---

自从chatgpt发布后一直关注如何和网络安全融合，最近一直在学习GPT相关内容，传统的用文本向量相似度索引的方式局限太大。

所以想到自己训练或微调，受限于算力，很多地方都不好验证，于是想做一个本地能跑起来的GPT学习研究。

## GPT的发展史

* 2018年 GPT1发布，作者用5G的书籍文本做无监督学习预训练，架构为12层transformer，每层12个注意头，模型参数约1.17亿，使用生成的预训练模型再到微调运用到各类nlp任务。
* 2019年GPT2发布，对gpt1架构改动了一下，使用40GB文本，包含web爬虫数据，redit等数据，模型参数达到15亿。
  + 提出了不修改预训练模型的情况下，使用0样本或少样本学习，完成任务

![](https://images.hacking8.com/2023/07/08/ayhAF_image_lqxaxPUkhg.png)

* 2020年GPT3发布
  + 和GPT2的区别就是将数据和模型都扩大了100倍，暴力出奇迹。使用45T文本，参数量达到1750亿，效果炸裂。
  + in-context learning
* GPT3.5
  + GPT3很强大，但机器只是试图完成文章，并不是“助手”
  + SFT supervised fine-tuning
    - 使用监督微调的方式，提供大量人类对话的例子，让机器模仿人类
  + RLHF align human
    - 训练奖励模型，让模型更偏向人类的思考方式
* GPT4
  + 多模态混合模型
  + GPT-4每个head都有2200亿参数，是一个8路的混合模型，总参数达到1.6万亿
  + 在GPT4论文有一个有意思的点，因为每次训练都相当于黑盒，训练的代价又过于昂贵，担心loss不下降，所以GPT4先训练了一个参数低100倍的小模型，基于这个模型用机器学习预测了GPT4模型量的loss值。

GPT是为了解决广泛的nlp的任务所以才会在数据集和模型参数上不断加倍，如果只是对一个垂直领域数据做问答和推理，是否可以用一个小模型达到效果。

## 数据收集

小模型整个训练都是在Google colab上完成，免费提供的显存大小只有16G，实际可用在13～15之间，后面很多地方受限于显存大小，所以有些地方实现会非常简单，后面会说到。

在数据的收集上，先进行一遍无监督学习，选取了seebug paper和一个poc仓库

* <https://github.com/Threekiii/Awesome-POC>
* <https://paper.seebug.org/>

这只是一个简单的测试，跑通后后面自然可以增大数据集

每个文章按1024大小进行分割，保存到json文件中，最后数据大小有31M。

![](https://images.hacking8.com/2023/07/08/98yqk_image_RF72EdbsVA.png)

Ps：按块分割会造成很多信息不完整，数据收集这块还是需要清洗后效果会更好。

## 数据处理

模型只是对数字进行计算，所以需要将文本转换为文本向量，这里简单的做法是将训练集中每个字提取出来生成一个字表，字表的索引号就是该文本的向量。

![](https://images.hacking8.com/2023/07/08/ylQ2W_image_b7CbI0wo09.png)

最后生成的大小有4214。

Ps：这是简单的做法，GPT的做法是使用 BPE（Byte Pair Encoding）算法处理，最后词表有5w大小，词表和显存占用是线性关系所以用这个简单的方法跑了。

### 数据集加载类

对每篇文章mask最后一个字用作预测，计算loss用mask第一个字的文本，gpt架构的神奇之处在于此，它只是预测最后一个字，而预测的这个字是根据学习文本的概率计算的。

```
# 定义数据集
class MyDataSet(Data.Dataset):
    def __init__(self, datas):
        self.datas = datas

    def __getitem__(self, item):
        data_item = self.datas[item]
        decoder_input = data_item[:-1]
        decoder_output = data_item[1:]
        return {"decoder_input": decoder_input,
                "decoder_output": decoder_output}

    def padding_batch(self, batch):  #
        for d in batch:  # 对当前batch的每一个decoder_input和decoder_output数据填充"<pad>"，填充到和batch里面的有的最大长度为止
            input_len = len(d["decoder_input"])
            output_len = len(d["decoder_output"])
            d["decoder_input"].extend([special_char_pad] * (max_pos - input_len))
            d["decoder_output"].extend([special_char_pad] * (max_pos - output_len))
        decoder_inputs = torch.tensor([d["decoder_input"] for d in batch], dtype=torch.long)  # 转type
        decoder_outputs = torch.tensor([d["decoder_output"] for d in batch], dtype=torch.long)

        return decoder_inputs, decoder_outputs  # 形状[b,decoder_input_maxlen], [b,decoder_output_maxlen]  type为torch.long

    def __len__(self):
        return len(self.datas)
```

## 训练超参数

这里简单训练一个6层 8个注意头的模型。

```
max_pos = 1024  # 一段话最多字
d_model = 768  # Embedding Size
d_ff = 2048  # FeedForward dimension
d_k = d_v = 64  # dimension of K(=Q), V
n_layers = 6  # number of Encoder of Decoder Layer
n_heads = 8  # number of heads in Multi-Head Attention
```

参数量在36M，及3600万的小模型，显存占用在11G左右，再大显存就不够了

## 模型层

模型使用是GPT2的结构

```
GPT(
  (decoder): Decoder(
    (tgt_emb): Embedding(6110, 768)
    (pos_emb): Embedding(1024, 768)
    (layers): ModuleList(
      (0-5): 6 x DecoderLayer(
        (dec_self_attn): MultiHeadAttention(
          (W_Q): Linear(in_features=768, out_features=512, bias=False)
          (W_K): Linear(in_features=768, out_features=512, bias=False)
          (W_V): Linear(in_features=768, out_features=512, bias=False)
          (fc): Linear(in_features=512, out_features=768, bias=False)
          (layernorm): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
        )
        (pos_ffn): PoswiseFeedForwardNet(
          (fc): Sequential(
            (0): Linear(in_features=768, out_features=2048, bias=False)
            (1): ReLU()
            (2): Linear(in_features=2048, out_features=768, bias=False)
          )
          (layernorm): LayerNorm((768,), eps=1e-05, elementwise_affine=True)
        )
      )
    )
  )
  (projection): Linear(in_features=768, out_features=6110, bias=True)
)
```

模型代码

```
# 把数据里面<pad>对应的字符给mask掉，让后面Q和K相似度矩阵的softmax中这些pad都为0，就不会被后续的V考虑
def get_attn_pad_mask(seq_q, seq_k):  # 形状都是[b, tgt_len <300]

    batch_size, len_q = seq_q.size()  # len_q = len_k = tgt_len
    batch_size, len_k = seq_k.size()
    # eq(zero) is PAD token.就是把数据里面<pad>对应的字符给mask掉，让后面Q和K的softmax不考虑这些<pad>
    pad_attn_mask = seq_k.data.eq(0).unsqueeze(
        1)  # [b, 1, tgt_len], id为0(也就是<pad>的id)的位置为True，其他位置为False。后面会把Ture位置的mask掉
    return pad_attn_mask.expand(batch_size, len_q, len_k)  # [b, tgt_len, tgt_len]

def get_attn_subsequence_mask(seq):  # seq: [b, tgt_len]

    attn_shape = [seq.size(0), seq.size(1), seq.size(1)]  # [b, tgt_len, tgt_len]
    subsequence_mask = np.triu(np.ones(attn_shape), k=1)  # Upper triangular matrix(上三角矩阵)
    subsequence_mask = torch.from_numpy(subsequence_mask).byte()
    subsequence_mask = subsequence_mask.to(device)
    return subsequence_mask  # [b, tgt_len, tgt_len] 上三角矩阵,下0上1,dtype=torch.uint8

class ScaledDotProductAttention(nn.Module):  # 计算Q和K的相似度矩阵，然后乘V。对应笔记里的图
    def __init__(self):
        super(ScaledDotProductAttention, self).__init__()

    def forward(self, Q, K, V,
                attn_mask):  # 前三者形状相同[b, n_heads, tgt_len, d_k=64]，attn_mask:[b, n_heads, tgt_len, tgt_len]

        scores = torch.matmul(Q, K.transpose(-1, -2)) / np.sqrt(d_k)  # Q和K的相似度矩阵scores : [b, n_heads, tgt_len, tgt_len]
        scores.masked_fill_(attn_mask, -1e9)  # Fills elements of self tensor with value where mask is True.
        # 就是scores矩阵里面和attn_mask=1对应位置的元素全部替换成-1e9，使其在下一步的softmax中变为0

        attn = nn.Softmax(dim=-1)(scores)  # [b, n_heads, tgt_len, tgt_len]
        context = torch.matmul(attn, V)  # [b, n_heads, tgt_len, d_v]
        return context, attn

class MultiHeadAttention(nn.Module):  # 多头注意力机制
    def __init__(self):
        super(MultiHeadAttention, self).__init__()
        self.W_Q = nn.Linear(d_model, d_k * n_heads, bias=False)  # d_model=768 ,  d_v = d_k = 64 ,  n_heads=8
        self.W_K = nn.Linear(d_model, d_k * n_heads, bias=False)
        self.W_V = nn.Linear(d_model, d_v * n_heads, bias=False)
        self.fc = nn.Linear(n_heads * d_v, d_model, bias=False)
        self.layernorm = nn.LayerNorm(d_model)

    def forward(self, input_Q, input_K, input_V,
                attn_mask):  # 前三者形状相同，都是[b, tgt_len, d_model]  , attn_mask: [b, tgt_len, tgt_len]

        residual, batch_size = input_Q, input_Q.size(0)  #
        # [b, tgt_len, d_model] --> [b, tgt_len, d_k * n_heads] -split-> (b, tgt_len, n_heads, d_k) -trans-> (b, n_heads, tgt_len, d_k)
        Q = self.W_Q(input_Q).view(batch_size, -1, n_heads, d_k).transpose(1, 2)  # Q: [b, n_heads, tgt_len, d_k=64]
        K = self.W_K(input_K).view(batch_size, -1, n_heads, d_k).transpose(1, 2)  # K: [b, n_heads, tgt_len, d_k=64]
        V = self.W_V(input_V).view(batch_size, -1, n_heads, d_v).transpose(1, 2)  # V: [b, n_heads, tgt_len, d_v=64]

        attn_mask = attn_mask.unsqueeze(1).repeat(1, n_heads, 1,
                                                  1)  # 添加n_heads维度并复制。attn_mask : [b, n_heads, tgt_len, tgt_len]

        context, attn = ScaledDotProductAttention()(Q, K, V, attn_mask)  # 参考图解，context形状[b, n_heads, tgt_len, d_v]
        context = context.transpose(1, 2...