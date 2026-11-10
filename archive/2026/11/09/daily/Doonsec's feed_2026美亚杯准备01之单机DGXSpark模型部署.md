---
title: 2026美亚杯准备01之单机DGXSpark模型部署
url: https://mp.weixin.qq.com/s/Z0o9EYYbtm-wPILj9t8CgQ
source: Doonsec's feed
date: 2026-11-09
fetch_date: 2026-11-10T09:01:13.832742
---

# 2026美亚杯准备01之单机DGXSpark模型部署

# 2026美亚杯准备01之单机DGXSpark模型部署

原创

ljnljn
ljnljn

ljnljn学习之路

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

因为要打美亚杯，听说其他学校师傅们都打算带上很多的Spark打比赛，所以撺掇着也弄了台 今天也是对师傅们推荐的Strata和TensorFold架构都进行了测试 模型感觉也只推荐qwen3.8 flash next了，其他在单机上表现都不太好 dgx给我最惊艳的是这么小的一个东西，也不太发热，能跑这么强劲的模型，果然时代发展的好快呀

# 速度对比

| 指标 | Strata IQ3\_S | TensorFold MLX 4-bit |
| --- | --- | --- |
| 单流解码·代码 | 42–55 tok/s | 50–76 tok/s |
| 单流解码·散文 | 42–50 | 27–31 |
| 单流解码·高可预测（JSON） | ~50 | **113** |
| 预填充 | 700–1,700 tok/s（3K/63K prompt） | ~2,100 tok/s（30K prompt 14 s） |
| 并发聚合 | 4 槽 32 客户端约 47 tok/s | **16 流 160–215 tok/s** |
| 长上下文 | 128K 实测可用（63K 召回通过） | 256K 实测可用（30K 召回通过），文档支持 1M（YaRN） |
| 内存占用 | 128K 时 100 G 用 / 21 G 余 | 128K+5 流时 76 G 用 / 28 G 余 |
| TensorFold 快的核心原因是 **MTP 草稿接受率高**（0.5→58 t/s，1.0→113 t/s），高并发还能叠加上去；Strata 是纯目标模型解码，速度稳定但不随并发增长。 |  |  |

# 比较

## Strata

**优点**

* 完整的“产品”体验：`strata launch` 引导式装模型、自动选量化、`strata connect` 一键生成 Claude Code / Codex / OpenCode 配置、预设、开机级 API key 管理。
* 有 Web 聊天页、TUI 监控（`strata monitor`）、桌面快捷方式、模型目录与显存适配计算。
* OpenAI + Anthropic 双协议、局域网/tailscale/cloudflare 访问模式。
* 签名更新源、断点续传、模型校验；文档极其完整（含 DGX Spark 专页）。
* 模型选择多（Qwen 各量化、DeepSeek V4.1、Qwen3.6 等），NVFP4/GGUF 等格式支持成熟。

**缺点**

* 慢：解码 42–55 tok/s，差不多是 TensorFold 的 60–70%。
* 128K 就顶到实测上限，再大没验证；并发只有 4–8 槽，聚合吞吐低。
* ARM/Spark 上只能用 Terminal，没有桌面 App；模型准备阶段还依赖 GitHub（被墙时要手动预置 llama.cpp）。
* 内存更吃紧（128K 只剩 21 G）。
* 模型是 IQ3\_S（约 3-bit）或 NVFP4，格式由它决定。

## TensorFold

**优点**

* 快：单流最高 113 tok/s，16 并发 215 tok/s，是这台机器上目前最快的方案。
* 内存效率高：128K + 5 流还能剩 28 G；32K 能开 16 流。
* 内置实时监控面板（`--dashboard`，解码/预填充/内存/草稿接受率，5 分钟曲线）。
* 单二进制 48 MB，无 Python 依赖；`pull` 断点续传 + SHA 校验，复用 HF 缓存；Prometheus `/metrics`。
* 模型家族覆盖广（qwen4、GLM、Nemotron、Gemma、LFM 等），支持多卡 TP、结构化输出、工具调用。
* 原生支持 256K，文档给出 1M 的 YaRN 路径。

**缺点**

* 开发者工具：没有 `connect`、没有模型目录/适配建议、没有预设和服务管理，装模型要自己选仓库和参数。
* **没有聊天网页**，`/dashboard` 只是监控页，还要过 API key（为此写了 8090 反代）。
* CUDA 上的 Flash Next 路径较新：只认 MLX 4-bit g32 检查点、不支持 fp8 KV、对模型结构校验很严（不匹配直接拒绝加载）。
* 模型 113 GB，比 Strata 的 84 GB 大；依赖 HuggingFace（国内要镜像，且镜像不稳定）。
* 文档偏“研发/复现”风格，普通用户上手成本高。

简单来说做美亚杯的话TensorFold更好，速度快一些，5并发基本没什么压力

上下文有个参考，目前来看128K是最好的

| 档位 | 上下文 | 并发 | 典型单流 | 典型聚合 |
| --- | --- | --- | --- | --- |
| 长上下文（当前） | 256K | 1 | 56–113 | — |
| 平衡 | 128K | 5 | 50–75 | 75–95 |
| 吞吐 | 32K | 16 | 68–113 | 160–215 |

# 安装

许愿式即可 ![](https://mmbiz.qpic.cn/mmbiz_png/3Bkxl9ud7XN1hKFg3mvqs9zJOUoBtdUIyMVsoHSficzdZFd2DftiaQ7x7ibSAjoribljs7VeBQ7Bpq8AB7ZxRjGTmicianvdx7se8LvQUKk0WFKHU/640?wx_fmt=png)

# 应用

dsh上就不说了，非常丝滑 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XMo9hAZZoiaXAicRmApbtmjMtECmppKNKpsibZeyM2XXE6YVbS2L89ics4vMujAVNGrdcBZNumbHgzmwHe41OslMxnlqT60UBjGk3c/640?wx_fmt=png) 接下来打算用苍穹测试一下（2025美亚杯个人赛），刚刚3分钟完成了题目分组 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XPKeUowib8ezwcOXgBA4SyIV6aMdbpLvPeXIesuNfGD1owAEiaQdhQ56BCiczL6GdGYTU0IH9QgDQmeq3icUibtrmjTa9jQxYzSGWSc/640?wx_fmt=png) 开了5并发（其实还是有点大了，导致大多数时间一直在prefill）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3Bkxl9ud7XNJqibn2mLhiaibl3NFqiatjz4h3xKp4arXUBD9gGenB8za7gGlTLvibpUQhZH2kPia08U3uFG2YqRcApCO66BrUOc45eceQk4LKj5PU/640?wx_fmt=png)

所以全分析就比较吃力了，先让他跑一晚上，明天看看效果 （这是做了一个半小时的） ![](https://mmbiz.qpic.cn/mmbiz_png/3Bkxl9ud7XOOf9g618qyIZqNhUQSAxCMmgL7kOfUy83JiaQg9ZDdQaxf51pPUAkHhjZXeXFrPmC7S6EPKOxqQF1XFXuRIQFAGMpQzSbcOiclc/640?wx_fmt=png)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/cA3l1kw40MLW9NibYDfx2QOcWfH3OzoO2IS6A6SbVLtfs4lmobf7giaUOuAlpFlkNNiaRia6vvnW9WIo3X7dIskQhA/0?wx_fmt=png)

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