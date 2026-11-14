---
title: 可以在笔记本电脑上本地运行专为自主网络安全任务设计的 7B-Cyber Agent 模型
url: https://mp.weixin.qq.com/s/d6uEijB9rlBJJlRcK27iLQ
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:18:46.387044
---

# 可以在笔记本电脑上本地运行专为自主网络安全任务设计的 7B-Cyber Agent 模型

# 可以在笔记本电脑上本地运行专为自主网络安全任务设计的 7B-Cyber Agent 模型

华盟信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于黑白之道
，作者杜芳

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM74633fuicFWYWOan94rMVOvWWNGza1w5PTNfoC0NoAHsw/0)

**黑白之道**
.

我们是网络世界的启明星，安全之路的垫脚石。

> **导语**：安全研究员在 X 上甩出一句话：现在能在笔记本上本地跑一个专为自主网络安全任务设计的 7B Agent 模型了。这个模型叫 Bimo-7B-CyberAgent，32K 上下文、原生工具调用、量化后最小 3GB。我们把量化文件头几百兆拉下来扒了一遍：训练分四段，跑分涨得凶也塌得狠，工具调用靠不靠谱，答案就写在作者自己承认的局限性里。

---

## 一、这条推文说了什么

发帖的是安全研究员穆罕默德·伊斯梅尔·索亚尔（Md Ismail Šojal，账号 @0x0SojalSec），11 月 10 日晚在 X 上推荐了一个 HuggingFace 模型，目前 143 个赞、12 次转发、3 条回复。回复区最实用的一条来自 @752963e64："正在用 ollama 在 CPU 上试。"

先划清界限，避免和昨天那篇重复：这条推文是**引用转发**他自己昨天发的数据集推荐贴——那套 95GB、30+ 领域覆盖的网络安全训练集。昨天我们拆了它的三处雷，今天讲**基于它训练出来的模型**。

模型在 HuggingFace 上是两个仓库。作者萨伊姆·阿扎姆（Saim Azam，账号 iBimo-o）发布原始权重，通义千问 2.5 编码器 7B 指令版（Qwen2.5-Coder-7B-Instruct）打底，Apache-2.0 许可，11 月 4 日上线；量化版由 mradermacher 转制，11 月 5 日上线。

![HuggingFace 上的 Bimo-7B-CyberAgent 量化仓库](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6P8Ficeict2hlbftynicAqPPnZwkrbR7PwNeBIRkBef591Dn4ByLjHicQZYvnkUqIpzCa1xuZICpeoj3MuUzZ2nsYTXLv6Q80yLDsY/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1 "HuggingFace 上的 Bimo-7B-CyberAgent 量化仓库")

## 二、模型本体：7.62B 参数，32K 上下文

我们没只看模型卡，而是把 Q4\_K\_M 量化文件头几百兆拉下来，直接读 GGUF 文件头里的元数据，结果和模型卡对得上：

* 架构 Qwen2 系列，28 层，隐藏维度 3584，注意力头 28 个、KV 头 4 个
* 参数总量 76.15 亿，词表 152064
* 上下文 32768，YaRN 扩展，缩放系数 4.0
* 默认采样：温度 0.7，top\_p 0.8，top\_k 20

原始权重是 BF16，四个分片共 14.2 GiB，16G 显存的机器装得下但会溢出，这是量化版存在的意义。聊天模板同样藏在 GGUF 里，llama.cpp 能直接读走——它会在首轮自动注入系统提示词，大意是"你是 Bimo，一个由萨伊姆·阿扎姆创建的自主网络安全与系统智能体"，并被要求被问及身份时始终自称 Bimo。

## 三、四段式训练：从安全语料到会调工具

训练分四步，每步 LoRA 微调后合并回主模型，NF4 量化、秩 16、alpha 32，硬件是一张 A100 80G。

![Bimo 的四段式训练流程与关键指标](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NJd6QSHGG9eQVFT5TA8WB3yRm3ibKn0lWh7nLpKqP6ej9jibP8mvRDwlHn5zg7I7qZZBibXicxAiaxwt3QIOEwLLYOb4cdJBdxHpJY/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2 "Bimo 的四段式训练流程与关键指标")

**第一步，安全知识 SFT**。用 Vyber07/cyber-security 的 53,201 条样本做监督微调，把攻防知识灌进底座。这是模型"懂安全"的来源。

**第二步，Agent 轨迹**。用 cx-cmu/agent\_trajectories 的 SWE-bench 轨迹，训练它多步操作、观察反馈、再决定下一步——这决定它能不能连续干活，而不是一问一答。

**第三步，工具调用格式**。用 hermes-function-calling-v1 的 1,893 次调用样本把输出规范成 JSON，学会用 `<tool_call>` 包住函数调用，结果用 `<tool_response>` 回填。

**第四步，上下文扩展**。用 YaRN 把 RoPE 缩放从 8192 推到 32768，让它能吞下整个代码仓库或长日志。

## 四、跑分：涨得凶，塌得也狠

作者自测的对比数据（基座 vs Bimo）：

| 基准 | 基座 | Bimo | 变化 |
| --- | --- | --- | --- |
| MMLU 计算机安全 | 64.00% | 73.00% | +9.00 |
| MMLU 综合 | 67.60% | 63.87% | −3.73 |
| GSM8K 数学推理 | 83.90% | 56.80% | **−27.10** |
| ARC-Challenge | 60.90% | 48.80% | **−12.10** |
| 自主动作/工具调用 | ~12.50% | 89.50% | **+77.00** |

最后一行才是重点：**自主动作与工具调用从 12.5% 干到 89.5%**，涨了 77 个点。作者称多轮工具调用准确率 94.2%，漏洞推理 Pass@1 88.6%。

代价同样明显。GSM8K 掉 27 个点，ARC 掉 12 个点。翻译成人话：为了把模型掰成"会自己动手"的形态，通用推理能力被牺牲了——你不会指望安全审计 Agent 去算小学应用题，但这意味着**别拿它当通用大脑用**。

还有两点必须说清楚：这些数字全部来自作者自测，模型卡里没有第三方复现记录；HuggingFace 官方推理组件在这个仓库上**被刻意关闭**，作者的解释是想把算力留给本地部署。

## 五、怎么下载、怎么跑

```
# 量化版（推荐 Q4_K_M，约 4.7 GB）
hf download mradermacher/Bimo-7B-CyberAgent-GGUF \
  Bimo-7B-CyberAgent.Q4_K_M.gguf --local-dir ./bimo

# 原始 BF16 权重（4 分片，14.2 GiB，要 transformers 环境）
hf download iBimo-o/Bimo-7B-CyberAgent --local-dir ./bimo-bf16
```

量化包一共 12 种，实测体积：Q2\_K 3.02 GB（极限压缩，质量损失明显）、Q4\_K\_S 4.46 GB、**Q4\_K\_M 4.68 GB（官方标注"快，推荐"）**、Q6\_K 6.25 GB（标注"质量很好"）、Q8\_0 8.10 GB（标注"最快，质量最好"）、f16 15.24 GB。

跑起来首选 llama.cpp，聊天模板和采样参数会自动从 GGUF 元数据里读：

```
./llama-cli -m Bimo-7B-CyberAgent.Q4_K_M.gguf -c 32768 --jinja
```

`-c 32768` 必须给足，不然 YaRN 扩展的上下文直接废掉。`--jinja` 用 GGUF 自带的模板，这是新版 llama.cpp 的默认行为，显式写上更保险。

用 Ollama 的话，官方库里目前**没有** bimo（`ollama pull bimo` 直接 404），得自己导入 GGUF：

```
FROM ./Bimo-7B-CyberAgent.Q4_K_M.gguf
PARAMETER num_ctx 32768
PARAMETER temperature 0.7
PARAMETER top_p 0.8
```

```
ollama create bimo -f Modelfile
ollama run bimo
```

采样参数那几个值不是我编的，是从 GGUF 元数据读出来的原始默认值。

## 六、动手之前，这几条必须知道

**它会编 CVE。** 作者在局限性一节里白纸黑字写了：模型会虚构 CVE 编号、版本号和配置项；输出的 JSON 语法完全合法，但里面的命令是错的；超过 8192 的上下文质量不均匀。**参数格式挑不出毛病，但别当成验证过的结论直接执行**——生产环境得加一层人工确认或沙箱拦截。

**训练语料带着未决争议。** 第一步 SFT 用的正是昨天拆过的 Vyber07/cyber-security：未处理的版权投诉、互相打架的许可条款、作者承认夹带的真实恶意样本。这不代表模型有毒，但"用有争议语料训出来的安全 Agent"，写进方案前该跟法务说清楚。

**它只认英文，也不联网。** GGUF 元数据里 `general.languages` 只写了 `en`，且没有检索、没有实时漏洞库。中文提问可以，但中文安全术语准头打折；想查当天新披露的漏洞，得自己喂数据。

伦理边界作者也划了：定位是"合规安全审计"，许可没给武器化用途背书——授权评估、代码审计、靶场演练没问题，未授权攻击是你自己的责任。

## 七、总结

7.62B 参数、32K 上下文、原生工具调用、3GB 起的量化包——摆在一起，本地跑一个安全 Agent 的门槛确实降到一台笔记本了，比任何跑分都实在。

但别被 89.5% 的工具调用率带跑偏。要盯的是作者自己承认的三条：会编 CVE、JSON 合法但命令错、超 8K 上下文质量不稳。加上 GSM8K 掉 27 个点，正确用法是把它当一个**需要复核的助手**，不是能替你按回车的人。

条条大路通 shell——但这次 shell 得你自己盯着。

**下载入口**

* 模型主页：https://huggingface.co/iBimo-o/Bimo-7B-CyberAgent
* 量化仓库：https://huggingface.co/mradermacher/Bimo-7B-CyberAgent-GGUF
* 原始推文：https://x.com/0x0SojalSec/status/2120280234851488145

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kZ8oAGNeUuj6mOI5YlyeqpmfFDmlWrhDUPtdowLH0Fe1bbFYw5foqQqLA333icDSHCp2490tNgrcOArofX5wjWw/0?wx_fmt=png)

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