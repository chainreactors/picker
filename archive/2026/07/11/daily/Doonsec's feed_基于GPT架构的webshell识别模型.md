---
title: 基于GPT架构的webshell识别模型
url: https://mp.weixin.qq.com/s/lfz-YKOoI8UQ-lnTZjRnBw
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:06:28.701730
---

# 基于GPT架构的webshell识别模型

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jQwkzezUrMibAUGl0AERxTsVPaKXBOEcLMRg0rvwXm2rf5kG4cBvDpzMzibmEe38PwBu8Xg2CVTrLNwInwWTqlOX5Ov8HLwtC6WHG3e1kXP1Y/0?wx_fmt=jpeg)

# 基于GPT架构的webshell识别模型

原创

k
k

漏洞推送

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 模型架构

基于gpt3 only decode架构

完成从头开始训练，模型总参数量: 9.98 百万,在mac m1上使用mps进行训练

模型代码

```
import torchimport torch.nn as nnfrom tokenizers import Tokenizerimport configimport os
class GPTBlock(nn.Module):    def __init__(self, embed_size, num_heads):        super().__init__()        self.ln1 = nn.LayerNorm(embed_size)        self.attention = nn.MultiheadAttention(            embed_dim=embed_size, num_heads=num_heads, batch_first=True        )        self.ln2 = nn.LayerNorm(embed_size)        self.ffn = nn.Sequential(            nn.Linear(embed_size, embed_size * config.FFN_SIZE),  # 升维            nn.GELU(),  # 非线性激活 (比 ReLU 更平滑)            nn.Linear(embed_size * config.FFN_SIZE, embed_size),  # 降维        )
    def forward(self, x, mask=None):        # 1. 注意力机制与残差连接        # PyTorch 的 MultiheadAttention 会返回 (输出, 注意力权重)，我们目前只需要输出        # is_causal=True 搭配 mask 会自动处理防止“看未来”的逻辑        attn_output, _ = self.attention(            x,            x,            x,            attn_mask=mask,            is_causal=True,            need_weights=False,        )        x = self.ln1(x + attn_output)
        # 2. FFN 与残差连接        ffn_output = self.ffn(x)        x = self.ln2(x + ffn_output)
        return x

class SimpleGPT(nn.Module):    def __init__(self, vocab_size, embed_size, max_seq_length, num_heads, num_layers):        super().__init__()        # 1. 词嵌入与位置嵌入 (PyTorch 的 nn.Embedding 自带可学习权重)        self.token_embedding = nn.Embedding(vocab_size, embed_size)        self.position_embedding = nn.Embedding(max_seq_length, embed_size)
        # 2. 堆叠多个 Transformer Block (盖楼)        # 用 nn.ModuleList 包装起来，确保 PyTorch 能够追踪里面的参数        self.blocks = nn.ModuleList(            [GPTBlock(embed_size, num_heads) for _ in range(num_layers)]        )
        # 3. 语言模型头 (LM Head)        self.ln_final = nn.LayerNorm(embed_size)        # 投射回词表大小，bias=False 是行业惯例，节约参数        self.lm_head = nn.Linear(embed_size, vocab_size, bias=False)
    def forward(self, input_ids):        batch_size, seq_length = input_ids.size()        device = input_ids.device
        # 生成位置索引 [0, 1, ..., seq_length - 1]        positions = torch.arange(            0, seq_length, dtype=torch.long, device=device        ).unsqueeze(0)
        # 特征融合：词意 + 位置        x = self.token_embedding(input_ids) + self.position_embedding(positions)
        # 生成因果掩码 (Causal Mask)        mask = nn.Transformer.generate_square_subsequent_mask(seq_length, device=device)
        # 让数据一层一层穿过所有的 Transformer Block        for block in self.blocks:            x = block(x, mask=mask)
        # 最后一层归一化        x = self.ln_final(x)
        # 通过 LM Head 转化为词表打分 (Logits)        # 形状变为: (Batch_Size, Seq_Len, Vocab_Size)        logits = self.lm_head(x)
        return logits
```

关键参数如下:

```
EMBED_SIZE = 256  # 256维特征MAX_LEN = 1024 * 4  # 4k上下文VOCAB_SIZE = 1024 * 8NUM_HEADS = 8  # 8个注意力头 (256/8 = 每个头32维)NUM_LAYERS = 6  # 堆叠6层 Transformer BlockFFN_SIZE = 4
```

## 生成词表

```
trainer = BpeTrainer(    vocab_size=config.VOCAB_SIZE,    special_tokens=["[UNK]", "[PAD]", "[BOS]", "[EOS]", "[black]", "[white]"],)
```

## 预训练

使用数据 WordPress + dede + webshell

![image-20260622173837148](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jQwkzezUrM82ftThuD26uDXp27yGycJ2s4jibictrbPIrmeT7etDqyBWquTI9TNKDBBgUpbMhfQ8T7H9AaRwXxl0ktia0RAzSDicZibSCM7ECsibM/640?wx_fmt=other&from=appmsg "null")

```
PHP 文件数量: 2445原始 token 总量: 16,139,532当前训练实际 token 总量: 4,480,725被 MAX_LEN 截断的文件数量: 593平均原始 token/文件: 6,601.04平均训练 token/文件: 1,832.61
```

## 预训练能力测试

`prompt = """<?php eval($_POST['"""`

学到了一堆没屌用的

![image-20260622175801764](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrM9P3KGHAtohLibwudAROvzeCO5DEpiaJjWMT7j8YJ2mrK1WbJKoiaSuh3pogc5bw5qjclWPLBQNMRKKrLicibl8CDicl3TfYiaDVEts5U/640?wx_fmt=other&from=appmsg "null")

## SFT

[bos\_id] + code\_ids + [eos\_id]

在[eos\_id]后增加[black]或者[white] 特殊token来标识样本

sft白数据:

![image-20260622173905510](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrMibfUN3BEqVmTdlnHdEvoCUzkudYfWkNztI5BhotdickWclc7BXJwzPfOHeB9Xl9XuRnbuDicWFPM3Alznjb3220d8pZmcUgqibyac/640?wx_fmt=other&from=appmsg "null")

sft黑数据:

•https://github.com/tennc/webshell•https://github.com/xl7dev/WebShell•https://github.com/JohnTroony/php-webshells

第一轮训练完以后出现了很严重的误报问题，会把`<?php echo $admin; ?>`也判断为webshell

大概原因是因为在sft数据中，黑样本的数据长度总是比较短，模型学歪了把长度作为特征了。

后续做了注入增强，1.随机抽取白样本中的片段，作为短白样本 2. 将黑样本去掉`<?php ?>`标签复制到白样本的`;`后做黑样本,并且将比例对齐

```
🔍 SFT 数据集加载完毕：原始 Webshell 780 个，注入增强 Webshell 780 个，正常样本 780 个，短正常样本 780 个 (原始正常 2098，原始 Webshell 780)
```

## Eval

![image-20260622190733431](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrMicCjdjNU6OFfZOfncmiboYI6DuptheJEQUly6BBTEAYeoHzYQcytp9WVju7nQoPXvNEFmougI0I0Uq46tNLDicJtm0nrSPZgQj68/640?wx_fmt=other&from=appmsg "null")

## 扩大预训练规模

接下来我想探索一个我一直很好奇的问题，在sft完全不变的情况下，增加预训练的规模对模型的最终效果是否有改善。

根据经验，模型的最近预训练token数量是模型的参数\*20

这是1千万的模型，所以最佳的训练token是 2e

我在compose上收集了大概1.8e的php token，单论实际训了的token大概是1e左右。训练2论，大概在2e左右。

![image-20260623163507052](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrMibbYibcT60lfqWcjdU8ibibibReRj1Jia5SrCDUibzVEfnysQl9l6Ftv3en1By4LjHe5kPy9mRa5fbEiaichmJUoU3kiatdOq6gGqCQq1qE/640?wx_fmt=other&from=appmsg "null")

首先在我的mac上训练，大概训练了5-8小时，才训了是1/20。完整训练完大概要几天到一周。

不得已，租了一个5090的服务器，大概训练2个多小时即可

![image-20260623163918173](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jQwkzezUrMibyVP2E4pcAtu6R9mAKzqPrWrgYYepRPW4XV58kV3BLTPjSEKEZpevs6F9NCSIFe4F8ibU4jduzkbxpJeNiamj7E23BAwod1dpicw/640?wx_fmt=other&from=appmsg "null")

![image-20260623163834511](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrMibAkxOGusuF08MVUFIGGibIdzgKSRdsxCWiaspYF8VicCiaf5of0PZ5dOv9e2ID1AF96Mncf76nctNU92lKYG016xNDIHicUT0NqnRA/640?wx_fmt=other&from=appmsg "null")

预训练完第一个batch，看看效果

![PixPin_2026-06-23_19-26-50](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrM8tXMUlnkwCkjIdYx3eQGUG8day9ygIuaGUHXhxviazrAicI5pWiaDqwhjzArciaX0ZK5G9mmIVAx2Gm37SJmknNA610FmjRRJFEBQ/640?wx_fmt=other&from=appmsg "null")

第二个batch的效果

![PixPin_2026-06-23_20-31-34](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrMibE4GFdgJlNXFTGG3yYX3HRkQMUzs2ZFia7X9rOcxsglBtGEowNsHWauzwmPMct0ISMJuUF6tgon9SWEnHIJzOF0zZXArNg4oicY/640?wx_fmt=other&from=appmsg "null")

有比较严重的重复的问题。

sft以后的误报率也大幅升高。

![PixPin_2026-06-23_20-37-11](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrM8IEJOCmicMlr8gMhJlOXvfFwZRCUyQgk6g3zvXicjPwrzWCvWHpwAB4HHjZiaPSYJ42ib8wsg7EdMQATrxUic38NMHR5ibqXgKS3DSk/640?wx_fmt=other&from=appmsg "null")

推测可能是因为我在预训练数据中放了webshell的代码，webshell代码中有大量的重复，删除掉webshell代码以后再训练

Batch1

![PixPin_2026-06-23_22-02-32](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jQwkzezUrMib8kVdfzexW1eictDYnrnMmPFYGLIVY02VjkZU9rfJajqVHv9sjoElMdL7l0nVbUWTzav4IKfiaEo0bVjUsl9CicXVS3sTeUVsgeA/640?wx_fmt=other&from=appmsg "null")

batch2

![PixPin_2026-06-23_23-22-23](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrMicxyITYD2obgk6Y1qbgSdzrq7icmiaW43t4wiarhNe911REuuPkpiabalJFLsat1SL7DsCKC10ofmISXskk9HC45mBCnaib024j7xdA/640?wx_fmt=other&from=appmsg "null")

基于batch1 sft结果

![PixPin_2026-06-23_23-34-27](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrMibiaGiaadOPtlSDDCbicpTXiadCmHYSicX9988HJBvr2NGst1GKWzRRanQjIaLNxToIkgdKAjIkKfoiaPL5kdYdqBus1ib3SibNWtvmO3I/640?wx_fmt=other&from=appmsg "null")

基于batch2 sft结果

![PixPin_2026-06-23_23-27-09](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrM8JFicYwSE1g60fwwzBg5iaJhE7qHOOoxCLhcXkYTJxT4U1gPhHHnnsbMguzLdN6jX6CsZ5UslplCj8lTS2H7982tG0MQSnk3qiaI/640?wx_fmt=other&from=appmsg "null")

如果完全不做预训练的情况下进行SFT对齐

sft batch1

![image-20260624100357301](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jQwkzezUrMibQiaQOzcnyZA0IlcAiac9SDgrfZOKUsNpZaIsibibcfDELEUJEicgjSgqNz3rhgbpibK9iaQPqsBrw7lEskwnAdZu2uVPLFicicQaEXxlM/640?wx_fmt=other&from=appmsg "null")

sft batch2

![image-20260624100459787](https://mmbiz.qpic.cn/mmbiz_jpg/jQwkzezUrMibBZqaHeQ4YFImAUfeQcs1gQsl6lnapMqWAYp2NvMWTLsUyefeCpHz0GbfIjZsJE32rA2HTCMYQDRQftia9EGJxwTCuDqxgpb2s/640?wx_fmt=other&from=appmsg "null")

sft batch3

![im...