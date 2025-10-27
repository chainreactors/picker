---
title: 尝试学习训练一个GPT-2对话模型 - 郑瀚Andrew
url: https://buaq.net/go-158815.html
source: unSafe.sh - 不安全
date: 2023-04-16
fetch_date: 2025-10-04T11:31:31.296166
---

# 尝试学习训练一个GPT-2对话模型 - 郑瀚Andrew

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

![]()

尝试学习训练一个GPT-2对话模型 - 郑瀚Andrew

# 训练shakespeare python3 train.py config/train\_shakespeare\_char.py# 实测V100 GPU，训练100分钟后，train los
*2023-4-15 20:14:0
Author: [www.cnblogs.com(查看原文)](/jump-158815.htm)
阅读量:44
收藏*

---

```
# 训练shakespeare
python3 train.py config/train_shakespeare_char.py

# 实测V100 GPU，训练100分钟后，train loss可以降到0.15左右，valid loss可以降到3.72
Overriding config with config/train_shakespeare_char.py:
# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

out_dir = 'out-shakespeare-char'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 200
log_interval = 10 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'shakespeare-char'
wandb_run_name = 'mini-gpt'

dataset = 'shakespeare_char'
batch_size = 64
block_size = 256 # context of up to 256 previous characters
dtype = 'bfloat16'

# baby GPT model :)
n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 5000
lr_decay_iters = 5000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

# on macbook also add
# device = 'cpu'  # run on cpu only
compile = False # do not torch compile the model

# on GPU server
device = 'cuda'

total number of tokens per iteration: 655360
Traceback (most recent call last):
  File "train.py", line 106, in <module>
    ctx = nullcontext() if device_type == 'cpu' else torch.amp.autocast(device_type=device_type, dtype=ptdtype)
  File "/usr/local/lib/python3.8/dist-packages/torch/amp/autocast_mode.py", line 234, in __init__
    raise RuntimeError('Current CUDA Device does not support bfloat16. Please switch dtype to float16.')
RuntimeError: Current CUDA Device does not support bfloat16. Please switch dtype to float16.
[email protected]:~/nanoGPT# python3 train.py config/train_shakespeare_char.py
Overriding config with config/train_shakespeare_char.py:
# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

out_dir = 'out-shakespeare-char'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 200
log_interval = 10 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'shakespeare-char'
wandb_run_name = 'mini-gpt'

dataset = 'shakespeare_char'
batch_size = 64
block_size = 256 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 5000
lr_decay_iters = 5000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

# on macbook also add
# device = 'cpu'  # run on cpu only
# compile = False # do not torch compile the model

# on GPU server
device = 'cuda'

total number of tokens per iteration: 655360
Traceback (most recent call last):
  File "train.py", line 106, in <module>
    ptdtype = {'float32': torch.float32, 'float16': torch.float16}[dtype]
KeyError: 'bfloat16'
[email protected]:~/nanoGPT# python3 train.py config/train_shakespeare_char.py
[email protected]:~/nanoGPT# python3 train.py config/train_shakespeare_char.py
Overriding config with config/train_shakespeare_char.py:
# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

out_dir = 'out-shakespeare-char'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 200
log_interval = 10 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'shakespeare-char'
wandb_run_name = 'mini-gpt'

dataset = 'shakespeare_char'
batch_size = 64
block_size = 256 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 5000
lr_decay_iters = 5000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

# on macbook also add
# device = 'cpu'  # run on cpu only
# compile = False # do not torch compile the model

# on GPU server
device = 'cuda'

total number of tokens per iteration: 655360
found vocab_size = 65 (inside data/shakespeare_char/meta.pkl)
Initializing a new model from scratch
number of parameters: 10.65M
using fused AdamW: True
compiling the model... (takes a ~minute)
step 0: train loss 4.2874, val loss 4.2823
[2023-04-14 09:55:30,333] torch._inductor.utils: [WARNING] using triton random, expect difference from eager
iter 0: loss 4.2586, time 35048.17ms, mfu -100.00%
iter 10: loss 3.2202, time 1389.25ms, mfu 10.73%
iter 20: loss 2.7714, time 1392.25ms, mfu 10.73%
iter 30: loss 2.6154, time 1392.92ms, mfu 10.72%
iter 40: loss 2.5368, time 1394.59ms, mfu 10.72%
iter 50: loss 2.5093, time 1394.69ms, mfu 10.72%
iter 60: loss 2.4757, time 1394.85ms, mfu 10.71%
iter 70: loss 2.5073, time 1394.47ms, mfu 10.71%
iter 80: loss 2.4474, time 1394.96ms, mfu 10.71%
iter 90: loss 2.4334, time 1395.45ms, mfu 10.71%
iter 100: loss 2.4050, time 1395.06ms, mfu 10.70%
iter 110: loss 2.3856, time 1396.25ms, mfu 10.70%
iter 120: loss 2.3631, time 1394.67ms, mfu 10.70%
iter 130: loss 2.3024, time 1394.34ms, mfu 10.70%
iter 140: loss 2.2330, time 1394.40ms, mfu 10.70%
iter 150: loss 2.1229, time 1396.18ms, mfu 10.70%
iter 160: loss 2.0596, time 1396.76ms, mfu 10.69%
iter 170: loss 2.0247, time 1396.03ms, mfu 10.69%
iter 180: loss 1.9253, time 1394.91ms, mfu 10.69%
iter 190: loss 1.8770, time 1395.84ms, mfu 10.69%
iter 200: loss 1.8505, time 1396.60ms, mfu 10.69%
iter 210: loss 1.8220, time 1396.59ms, mfu 10.69%
iter 220: loss 1.7351, time 1397.92ms, mfu 10.68%
iter 230: loss 1.7186, time 1396.52ms, mfu 10.68%
iter 240: loss 1.6742, time 1395.36ms, mfu 10.68%
step 250: train loss 1.5482, val loss 1.7322
saving checkpoint to out-shakespeare-char
iter 250: loss 1.6170, time 6002.98ms, mfu 9.86%
iter 260: loss 1.6227, time 1396.29ms, mfu 9.94%
iter 270: loss 1.6086, time 1395.38ms, mfu 10.02%
iter 280: loss 1.5508, time 1396.46ms, mfu 10.08%
iter 290: loss 1.5237, time 1395.96ms, mfu 10.14%
iter 300: loss 1.5497, time 1395.28ms, mfu 10.20%
iter 310: loss 1.5187, time 1397.89ms, mfu 10.24%
iter 320: loss 1.5137, time 1396.06ms, mfu 10.29%
iter 330: loss 1.5041, time 1395.99ms, mfu 10.33%
iter 340: loss 1.4562, time 1394.80ms, mfu 10.36%
iter 350: loss 1.4466, time 1396.15ms, mfu 10.39%
iter 360: loss 1.3967, time 1399.17ms, mfu 10.42%
iter 370: loss 1.3867, time 1396.58ms, mfu 10.44%
iter 380: loss 1.3648, time 1395.66ms, mfu 10.47%
iter 390: loss 1.3446, time 1395.32ms, mfu 10.49%
iter 400: loss 1.3223, time 1396.27ms, mfu 10.51%
iter 410: loss 1.3614, time 1395.41ms, mfu 10.53%
iter 420: loss 1.3121, time 1396.52ms, mfu 10.54%
iter 430: loss 1.2831, time 1396.91ms, mfu 10.55%
iter 440: loss 1.3500, time 1395.62ms, mfu 10.57%
ite...