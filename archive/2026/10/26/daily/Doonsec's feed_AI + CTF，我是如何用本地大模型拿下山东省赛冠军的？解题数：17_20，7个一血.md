---
title: AI + CTF，我是如何用本地大模型拿下山东省赛冠军的？解题数：17/20，7个一血
url: https://mp.weixin.qq.com/s/w72Ay689OZ0ls6Mbu5HPBw
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T06:59:28.754394
---

# AI + CTF，我是如何用本地大模型拿下山东省赛冠军的？解题数：17/20，7个一血

# AI + CTF，我是如何用本地大模型拿下山东省赛冠军的？解题数：17/20，7个一血

原创

Real返璞归真
Real返璞归真

Real返璞归真

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 前言

### 公众号

关注公众号【Real返璞归真】回复【山东省赛2026】获取全部题目附件下载地址：

![](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibgcGSTFgb196IfPB7HiahBNyNJJgam5LWmMJhod5RNUIvD0Mo15BauhhTPHFBtHD9wiaTSflcGaqWnlJ9E6237Q7oYibcSkv5oErg/640?wx_fmt=png&from=appmsg)

### 解题情况

比赛结束前10分钟各赛题解题情况：

![](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibgAIEomevZibTodm2ib2OEdC3425x98JWCEYWibFcq8O1Y2x4s8GPWvVeNegRVCqWptFP1wQy2XUF6u0f9jR243KkbMrYnrVMpQuA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2Wibg4tKLBwy3c6obQu0VVmeBIDAWNVCTjDEIe2texWvhdz9IA23uFeZEBRH3jGvex4W5o2LIUnN8wMCp6lZriagcP4Rv3Q3KyEsaI/640?wx_fmt=png&from=appmsg)

### 赛况简介

第十三届山东省网络安全技能大赛（瀚高数据库杯）于10月25日在枣庄学院举办。

鉴于往年的比赛情况，今年组委会在反作弊方面下了很大功夫：

* 每台电脑使用USB锁封锁多余的接口
* 每个已使用的USB接口使用一次性封条贴住
* 厕所由组委会工作人员严格控制出入
* 每个桌子有一名志愿者负责监考

为了防止黑幕，比赛前我开启了录屏+录像。虽然今年解题很快，但是没有和去年（）一样的志愿者全程盯着我的电脑、搜查物品和汇报我的解题进度。

本次比赛中，我使用AI辅助解题，最终解题数：17/20（包含7个1血、1个2血、2个3血）。

备赛阶段，学习到了很多关于LLM的知识，也深入了解一些LLM的薄弱点与能力边界。

LLM辅助安全，提高效率，但安全研判的主体依旧是人。

对于在CTF中使用Agent辅助解题，并不是简单的有合适的硬件、装上模型就可以，还需要对LLM和Agent的工作原理充分了解、选取合适的模型框架与参数、大量的赛前准备以及赛中的人机协同。

本篇文章主要分享一下个人关于 AI辅助CTF 的一些经验摸索，供各位师傅参考。

## AI辅助解题

### 简介

今年的比赛相比于往年发生了一个很大的变化：在AI Agent时代，很多选手开始使用**AI辅助解题**。

通过今年的排行榜，可以发现几个明显的特征：

* Crypto方向（AI最擅长的数学推理领域）解题数增多，有6名师傅AK。
* 理论题（AI知识丰富）均分增高，且有数名师傅满分。
* 选手们普遍解题速度更快，解题数量更多。

赛前，我也准备了很久本地AI环境，并探索各种场景下的最优解。

先揭晓一下答案，经过长时间的摸索和反复的bench测试，最终我采用的解决方案（Mac Silicon架构）：oMLX + Qwen3.8-Flash-Next + Pi Agent + 提示词 + 外部工具

最初的模型速度很慢、解题能力也比较弱，但是经过一些优化可以明显提高能力。

最终在4并发下，总体吞吐量达到 120 token / s，模型占用内存80G。在262k上下文限制下，每个会话占用约5-10G KV Cache。总占用105G左右。

（Tips：我的电脑配置是MacBook M5 Max 128G，融合内存带宽614GB / s，师傅们可以参照文章并结合自己的机器去配置调试，据说Strata已经能在32G显存下跑Qwen3.8-Flash-Next了）

### 需要关注的问题

大概需要关注几个问题：

* 内存：决定本机能运行什么参数量的模型
* 带宽：决定模型的速度（token/s），很容易被忽视的地方
* Agent：选取合适的Agent搭配模型实现自动化解题
* LLM：选取什么模型？考虑参数量与量化程度。
* 推理框架：选取什么推理框架运行模型？不同推理框架可能导致速度产生很大的差异。
* 提示词 / Skills / 知识库：是否需要为Agent增加提示词 / Skills /知识库？

下面，我们将从 **模型选取、推理框架选取、模型量化、提示词 / Skills、并发、外部工具框架**等方面，分享我是如何用AI解题的。

### 1.模型选取

目前，比较优秀的模型：

* Qwen3.8-27B（https://huggingface.co/Qwen/Qwen3.8-27B）

  ![](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibgLUXzq78kujdqk0fFPeHntouMyOib2ORARuJTG2OiavKmGaozrEtjhJujbI6qibm2DSaNQAfcJfEESkBuNSUD0OhbIbPJgM2BgBg/640?wx_fmt=png&from=appmsg)
* Qwen3.8-Flash-Next（https://huggingface.co/Qwen/Qwen3.8-Flash-Next）

  ![](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibgLORqWDRJbbMic9VzqL6wzWSKfw9iaPL5DUoXicSKbxmfKKsiaM2Y4Ks6BZsMWOiaBibWVdJ0jpvMREVftuB56IukKo3mZA1utNxA9w/640?wx_fmt=png&from=appmsg)

其中：

* `Qwen3.8-27B`是一个参数量为27b（270亿）参数的**稠密（Dense）模型**
* `Qwen3.8-Flash-Next`是**Moe（混合专家）模型**，包含125B参数和51B的N-gram，并且它是`Qwen4`新架构的预览版。

通俗易懂的来说，**稠密模型**每个 `token` 都会激活全部的27b参数，**Moe模型**每个`token`实际参与计算的只有6b参数。

也就是说，`Qwen3.8-27B`更擅长强推理的场景，而`Qwen3.8-Flash-Next`有更多的知识、更快的速度。

对于CTF解题赛来说，显然`Qwen3.8-Flash-Next`是更好的选择，它有更丰富的安全知识，并且可以快速交互。

快速交互非常关键，对于除Crypto方向外的其它赛题，AI并不需要太强的推理（思考）能力，而是需要大量的工具交互信息。

顺带提一下：这两个模型都支持Thinking能力，也都具备视觉能力。

如果电脑GPU的显存比较小，可参考 **8.拓展阅读** 部分对模型分层加载，目前比较成熟的方案：

* Strata （Windows和Mac通用，显存、内存和SSD分层加载）
* oMLX（Mac专用，专家分层加载）

并且，他们都会将51B的N-gram表放到磁盘。

### 2.推理框架

推理框架用于：加载模型、调度计算资源、管理显存，并高效地生成回答。

对于开源模型，官方默认发布 **F16 safetensors** 格式的模型参数文件，主要面向 `vLLM` 和 `SGLang` 推理框架，这两个框架主要用于生产级的高并发服务引擎，需要搭配专业的服务器GPU。

而消费级产品（游戏本、MacBook）CPU通常使用 `llama.cpp` 和 `MLX` 框架部署模型。

模型参数文件开源后，陆续会有社区版模型出现，它们会将官方格式转换为适用于消费级框架部署的格式。如：适用于 `llama.cpp` 的 **GGUF** 格式文件 和 适用于 **MLX** 的文件。

如何安装推理框架呢？有几个可供选择的方式（我逐个尝试了）：

* `llama.cpp`：直接安装`llama.cpp`框架，纯命令操作，但是可以配置很多自定义参数，如：后面要提到的**MTP加速**。
* `ollama`：基于`llama.cpp`的可视化界面客户端，操作简单，但是很多设置不能自定义（不知道能不能通过命令行定义）。
* `oMLX`：针对Mac的**Silicon**架构设计，在MacBook上可以获得更高的tps(token/s)速度。
* `LM Studio`：避雷，适合傻瓜式安装操作，启动简单。但很多设置不能自定义。

总的来说，如果你是Windows建议安装`llama.cpp`，如果你是Mac建议按照`oMLX`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2WibhkNxltiacDQCtn3BYNWE4usE9JPShtj2xDR56hUAgZNoqub44EQOLpwF91TgJVVgjXEgI8dVQfuETrJCh6HmibwAppCgxX5zDZo/640?wx_fmt=png&from=appmsg)

除了格式转换适配，社区版模型也会去做**量化**，这也是我们接下来要说的。

### 3.模型量化

官方开源的模型是满精度模型，常以 **BF16（Brain Floating Point 16）** 格式发布。

通俗易懂的来说，也就是每个参数占16bit（2字节）。

`量化`就是将参数的浮点数精度压缩，常见的量化：8bit、6bit、4bit、甚至2bit。

例如：4-bit量化就是以4bit浮点数存储原来16bit浮点数。

`Qwen3.8-27B`在 BF16 下大概需要56G显存，而4bit量化只需要16G显存。

通过模型量化（参数精度压缩），可以让低显存的设备跑更高参数的模型、得到更快的速度，但随之而来的是模型能力下降。

通过我的实测，发现4-bit和8-bit在做CTF题目的质量差距不大，但是4-bit的速度远快于8bit的速度（2倍）。

因此，我本地选取了4-bit量化版本。

### 4.模型调优

安装完推理框架、下载完量化版的模型权重文件后，就可以运行模型了。

`oMLX`自带bench功能，可以测试模型输出速度，起初我只有30 token/s。

对于简单的模型调优来说，主要是两点：

1. 按照官方文档配置 `temperature`、`top_p`、`top_k`、`min_p`等参数：

   ![](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibgPpn3t8sibY6mtemOtRibGtSsgb82I3EIeWHnGiaVISZWsBtTpIGeck8aEM5UsK3c46uAyBIG05ssRUh1oezBZTe2umUIokq96uY/640?wx_fmt=png&from=appmsg)

   这一步很重要，最初我没有按照官方文档去配置参数，发现理论题和CTF题输出质量下降很严重。
2. 打开MTP加速：

   ![](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2Wibia1ibNbziapia6ibTqus5wOhN5mP4sTOWPdvhRrdb7icaAIIsgQibic9dLAiahqbNTVnmbV3sic74RxVZHk3knJUFAY9eMhjLviarNK0jdCM/640?wx_fmt=png&from=appmsg)

   `Qwen`的两个模型都内置了MTP头，用于MTP加速。MTP加速的大概原理是批量猜测后续token，然后进行验证，如果猜测成功，就可以节省后续前向传播的次数。

   这里我也尝试了其它各种加速方式，包括 外部MTP模型、DFlash 等，发现内置MTP加速的效果最好。

   开启MTP加速后bench可以到达60 token/s（速度翻倍）。

### 5.模型并发

bench实测：

![](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibjdeFV9qRG24l2s0hsa1xRUUxUlW1P4tnxvnqSWPwRpKzMQJbbqgWh5afnwAOp3COd30S5BvxjWtd1N6s67qGZN6DbKQt6GV5o/640?wx_fmt=png&from=appmsg)

通俗易懂的说，并发调用LLM比单独调用LLM的利用率更高。

单并发下，经过优化达到 55 token / s。四并发下，108.9 token / s。

虽然每个会话只有26 token / s，但是每秒的token量增加，对于总体来说是收益。

也就是说，整体单位时间处理的请求数（QPS/吞吐量）会提升。

这些是一些简单的优化，关于kv cache缓存等，或许也有一些优化方案，师傅们也可以自行去探索。

### 6.提示词 / skills

比较热门的CTF Skills：https://github.com/ljagiello/ctf-skills

但是经过尝试，我发现对于本地小模型。skills会降低首字的速度，并误导模型严格按照skills的方式去执行。

因此，在比赛中，我没有使用这个庞大的skills，而是写了一个简短的提示词：

![](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2Wibj9ibLt8Baqf3d4sFcjIrmNzcSSsjlmbXefCQlownsb45Br9syzhYnZ7eXjIU9sYHg41I0Hb7beYmL6ccBP0FuYtYfvKs8EKwSQ/640?wx_fmt=png&from=appmsg)

告诉它我的基础环境信息、工作目录（防止乱放文件）、工具信息（MCP、Ubuntu虚拟机）等。

并让他进行三次实验循环，**如果没有进展，立刻停机（很重要）**然后输出**状态卡（卡壳点、已解决、下一步）**。

如果没有这段提示词，模型会无穷无尽的解下去，甚至走向错误的方向。而**停机+状态卡**可以更好的人机协同。

经过多次bench解题实测，发现这个是对模型解题能力最大的提升。本次比赛中的2道Web题目，我使用多并发去对黑盒题目进行信息收集，然后人工研判并将各自对话的有用信息汇总，交给一个新的对话重新探索。通过人机协同大幅度提高AI解题能力。

（Skills虽然冗余，但是这次比赛的密码题目：CRT泄露，纯LLM无法解决，我将Skills文件手动加到对话中，刚好弥补了模型的知识缺陷成功解出题目）

### 7.解题框架

理论题部分，我开发了一个**AI并行解题框架**：

![](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2Wibj8UXpULWShHZU6hGPW07ibtiaEq3tInzTu0ASYLsoXGxqmFickLQpjj78q5w9V2tTCWrqNLtUdWKGBu2V7ricxn5HxBiaom45WNYicc/640?wx_fmt=png&from=appmsg)

将选择题库**切片后建立 FTS5 全文索引**，检索时用 SQLite FTS5/BM25 做关键词匹配，再交给模型生成带引用的回答。

这个也是实测优化后的方法，RAG的向量检索会导致相似语义内容检索不准确。因此，我选择了关键词匹配方案。

当用户复制粘贴问答题时，系统会：

1. 调用小模型（无思考）将输入格式化，输出格式化后的 题目内容 与 选项。
2. 三路并行解题：

* 知识库检索 + LLM API
* Agent搜索知识库
* 纯LLM API

通过三个结果交叉检验，得到最终答案。在本次比赛中，发现有1道题目是**纯LLM无法解决**的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2WibianhxVhGIicJdp9iceGaZKKlD7c67EiaS5GTxUuEYa5JyNeocMRiaEDVNvnsIyGquAEJAtWpwIZT1ic7w5enINLXVZc3HnyR6rHkNJA/640?wx_fmt=png&from=appmsg)

这道题目模型出现知识缺失的问题，但知识库检索后丢给模型分析得到的答案是正确的。

使用`Pi Agent`作为解题的主力工具：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2Wibjd3UHs65Y5OOY4oK8NAXs1gnHujr8XADmrQh1q57KWt0PB5AWdhLJFTwkYT8KCJGm5gX6TtIx5oqyTqQyckozUqk67odTOdmo/640?wx_fmt=png&from=appmsg)

接入各种工具的MCP以及Ubuntu解题环境。

除此之外，我还用了`Cairn`框架（https://github.com/oritera/Cairn）解Web题目。

之所以使用这个框架，是因为对于附件题目来说，本地的信息是足够的，主要考察模型的工具交互与推理能力。

![](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibgEibgPwzJE1NWV1RyGV0JHod4jl6htWJ7f1gSyRtFVq4XNj6nJJj43hDFDOq1xCMfLMLDoMoic9Mibuu7FMqmcKAx3Eic701aIgy4/640?wx_fmt=png&from=appmsg)

而Web题目是黑盒，需要多Agent并发去收集足够的信息，并整合信息后解题。

最后，还开发了一个`CTF-Tiller`作为并发解题的补充：

![](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2Wibhxg22b8iaf9BryScQdhUgKnicwZcTwcTzRlUpawicGNTwn6xibGyCL21B0RPNZ8zS8d1HG8cnkpoIzzPlpHbibeGsYH8MjmOHFAl4c/640?wx_fmt=png&from=appmsg)

可以更直观的看到每个题目的结题进度，并回退到某一步的对话，修改`状态卡`重新解题。

并且便捷的接入了各种`mcp`和`skills`的开关选项，相比于`pi Agent`更方便的操作和处理并发。

相关工具后续会陆续开源（开发时间仓促，很多配置与本机绑定，需要逐步优化）。

### 8.拓展阅读

Strata（https://github.com/Niko1221/Strata）：Moe模型优化，可以让小显存跑大模型。原理大概为**显存放常...