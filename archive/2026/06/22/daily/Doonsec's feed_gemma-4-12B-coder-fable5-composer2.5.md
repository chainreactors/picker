---
title: gemma-4-12B-coder-fable5-composer2.5
url: https://mp.weixin.qq.com/s/hqWFHsALrcYtxvpMdXVxfQ
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:03:30.845572
---

# gemma-4-12B-coder-fable5-composer2.5

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FT3A8r9icDymQBiaBbfjINeaUeQkGRyHpMKfzYX6hRsX0HdsOq12Z99as1ZbdVIwQxEteCMajDj8LDlaYRxzn1oY4zZiaKE6d6NyBULlw9vhr0/0?wx_fmt=jpeg)

# gemma-4-12B-coder-fable5-composer2.5

凉城
凉城

ListSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# Gemma4-12B-Coder (GGUF)

## 模型基本信息

* • 仓库：`https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF`
* • 基础模型：`google/gemma-4-12B-it`
* • 格式：GGUF
* • 任务类型：text-generation

## 量化规格

仓库提供了多个量化版本。

| 量化版本 | 体积 | 大概适合什么场景 |
| --- | --- | --- |
| Q2\_K | 4.5 GB | 最小，能在很低端的机器上跑 |
| Q3\_K\_M | 5.7 GB | 8GB 显存能比较舒服地用 |
| Q4\_K\_M | 6.87 GB | README 推荐这个，体积和质量的平衡点 |
| Q6\_K | 9.11 GB | 接近无损 |
| Q8\_0 | 11.8 GB | 基本是全质量 |

**Q4\_K\_M** 是最现实的默认起点。Q2 太小，聊胜于无；Q6 和 Q8 对硬件要求一下子高很多，一般人未必用得上。

## 优势

* • 门槛低：大约 4.5 GB 可用显存或统一内存，就能跑最小的版本
* • 上下文长：现在是 256K
* • 偏编码：训练数据强调可验证的 Python 编码，模型会先展开推理，再给代码

## 怎么跑

**llama.cpp**

从hf下载后，直接llama-server启动

```
@echo off
cd /d C:\llama.cpp
llama-server.exe ^
  -m C:\models\gemma4-coding-Q4_K_M.gguf ^
  --ctx-size 16384 ^
  --n-gpu-layers 99 ^
  --no-mmap ^
  -fa on ^
  --cache-type-k q8_0 --cache-type-v q8_0 ^
  --temp 1.0 --top-p 0.95 --top-k 64 ^
  --host 0.0.0.0 --port 18080
pause
```

打开 http://localhost:18080 进行聊天吧。上下文`--ctx-size`根据需要调整

## 怎么用这类模型

建议先用一个 Q4 量化版本试出大致感受，再决定要不要换更高质量的版本。本地跑 12B 级别模型本来就不是为了追求极致效果，更多是为了方便、可控、能离线用。

## 参考

* • https://huggingface.co/yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

ListSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

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