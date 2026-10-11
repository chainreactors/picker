---
title: AI取证实战第24期：本地大模型取证实战
url: https://mp.weixin.qq.com/s/Csk6YXfi1nvNQ7Eh4GkrBg
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:59:13.430060
---

# AI取证实战第24期：本地大模型取证实战

# AI取证实战第24期：本地大模型取证实战

原创

小谢
小谢

小谢取证

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 本地部署大模型取证实战：从模型权重到会话日志的全证据面剖析

当大模型从"云端 API"走进"本地硬盘"，它留下的痕迹比传统应用更丰富、也更隐蔽：模型权重躺在另一个盘、会话存在 SQLite 里、日志里明晃晃写着你的每一句提问，甚至整套系统提示词都被完整记录。

本文基于一台真实 Windows 工作站的活取证过程，把五层证据面逐层拆开。文中包含两个实战案例：**模型客户端**（LM Studio）与**自带本地模型的 AI 应用**（WorkBuddy 调用 Qwen3.6-35B-A3B），后者完整还原出了 9 次本地模型会话的全部内容。

## 一、为什么要给本地大模型做取证

"本地部署大模型"的典型案件场景有三类：

* **涉案内容生成**

  ——嫌疑人用本地模型生成诈骗话术、钓鱼文案、违规内容，数据不出本机，云端取证无从下手；
* **涉密数据外流**

  ——把案件材料、内部文档丢给本地模型做 RAG 检索，向量库与解析缓存里全是原件内容；
* **违规工具开发**

  ——用本地模型辅助分析目标系统源码、生成攻击脚本，会话记录直接构成主观明知的证据。

与传统应用取证相比，本地大模型的特殊性在于：**证据分散在五个层次，且易失性差异极大**。缓存和内存几秒钟就可能消失，而模型权重文件几个 GB 躺上几个月不动。抓取顺序错了，关键证据就没了。

## 二、证据面分层：该抓什么

先把"该抓的东西"一次性圈全。下图是我在实际检材中总结的五层证据面，从最稳定的模型层到最易失的系统网络层，逐层递进。

![本地大模型取证证据面分层](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcH21Gxuds7icIe0WlKg8ABicIHqLPImyMGqLMialibGp6bN1qtPm9CiaWjNxTEX3HJhCmv3IZS16nYmXt9Zyk3db0MgibwOzMnibfI9qw/640?wx_fmt=png&from=appmsg)

图1　本地大模型取证的证据面分层

每一层的取证价值和时效性完全不同，实际工作中建议按**"先易失、后稳定"**的顺序固定：

| 层次 | 典型对象 | 易失性 | 取证价值 |
| --- | --- | --- | --- |
| 模型层 | GGUF / safetensors 权重、config、LoRA 适配器 | 低 | 来源溯源、是否被篡改、是否存在违规微调 |
| 缓存层 | HF hub 缓存、Ollama blobs、KV / prompt 缓存 | 中 | 下载历史、真实使用过的模型、推理残留 |
| 会话层 | 对话数据库、向量库、导出记录 | 中 | 提问内容、时间线、主观明知 |
| 日志层 | 应用日志、API 网关日志、系统事件日志 | 中 | 完整 prompt、客户端 IP、调用频次 |
| 系统网络层 | 进程内存、页面文件、浏览器痕迹、出站流量 | 高 | 运行证据、是否外联回传 |

## 三、各平台证据落盘速查

不同部署方式的证据位置差异很大，抓错目录等于白干。下表是 Windows 环境下主流方案的默认落盘位置（本文检材实测确认）。

| 平台 | 模型权重 | 会话 / 历史 | 日志 |
| --- | --- | --- | --- |
| Ollama | %USERPROFILE%\.ollama\models\blobs | 依赖前端（Open WebUI 等） | 系统日志 / 服务输出 |
| LM Studio | %USERPROFILE%\.lmstudio\models（可被改为任意盘） | conversations\\*.conversation.json | server-logs\YYYY-MM\\*.log |
| HF transformers | %USERPROFILE%\.cache\huggingface\hub | 由调用方决定 | 无内置 |
| AnythingLLM | storage\models | storage\anythingllm.db（SQLite） | storage\logs\ |
| llama.cpp | 自选目录 | 无 | stdout |
| vLLM | HF 缓存或自选 | 无 | 服务 stdout |

新手要点：**先把目录找全，再谈分析**。本机检材就踩了经典陷阱——LM Studio 的 `models` 目录是空的，真正的权重全在 `D:\models`。只按默认路径找，会得出"没下载过模型"的错误结论。

## 四、实战：本机检材逐层剖析

### 4.1　模型层：最大的陷阱是"目录是空的"

检材是一台 Windows 工作站。按默认路径查看 LM Studio 的模型目录：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGtlALZhodzwZ9picX7C7rWCsvzl3Vmg8Sjibn171UasZoVV7osHiaL8CdrI4rlykK61lUSPCQeH5cyugO1j5ica7IY3oojwPH0y2o/640?wx_fmt=png&from=appmsg)

但应用自身的配置和下载记录出卖了真实位置。读取 `.lmstudio/.internal/single-downloads-info.json`：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGS1fBFdyO9oDQDoyKMhSzcae8vNrX4tU12th48rRjbBbZ9TAOg1Bj3NWsGsSM2RHUZBYz8VYkhicgZAu4G4Zvibiaicup1IaVYibDs/640?wx_fmt=png&from=appmsg)

这一条记录就交代了四件事：**模型真实存放路径、官方期望哈希、下载中断的进度、以及重试了 8 次**。顺藤摸瓜，D 盘里确实躺着 6 个权重文件：

| 文件 | 大小（字节） | SHA256（前 16 位） |
| --- | --- | --- |
| unsloth\Qwen3.5-0.8B-GGUF\Qwen3.5-0.8B-Q8\_0.gguf | 811,843,840 | 0ad885ffd4bb022f |
| unsloth\Qwen3.5-0.8B-GGUF\mmproj-F32.gguf | 402,381,664 | 2b167b9d9a96bf18 |
| unsloth\Qwen3.5-9B-GGUF\Qwen3.5-9B-Q3\_K\_S.gguf | 4,316,865,760 | 162050d39ebae6b8 |
| unsloth\Qwen3.5-9B-GGUF\mmproj-F32.gguf | 1,824,062,016 | a1cd5c1625b44dd0 |
| lmstudio-community\...\downloading\_Qwen3.5-9B-Q8\_0.gguf.part | 1,133,581,802 | 1fe6028610b33512 |
| lmstudio-community\...\mmproj-Qwen3.5-9B-BF16.gguf | 921,704,480 | 330d17547bfdbcd0 |

取证价值：**比对本地权重哈希与官方发布哈希**，可以判断模型是否被替换或二次打包。本案中 `.part` 文件只有 1.13 GB，而官方 `totalSizeBytes` 是 9.53 GB —— 这个"未完成"状态本身也是证据：说明使用者在下载大模型时网络受限（镜像代理超时），转而使用了更小的量化版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGvt0VicembdE17ibqIdukuOsxwJKk4XVNv3wEru8ic1NLBGAJ8ZW07YTqdSnuUHjX8gVaAxV6GVMgwVFtLCbMYOmpYmQrONJmSZY/640?wx_fmt=png&from=appmsg)

### 4.2　会话层：LM Studio 的 JSON 与 AnythingLLM 的 SQLite

LM Studio 把每段对话存成独立 JSON，文件名就是**创建时间的毫秒时间戳**——这是天然的溯源线索。本机共发现 4 个文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcFf9fDnMTdvLKybkgzFRJic2nnc04bVwHMluxr3AzK5tmCkArN3QOJV6r2YeyZxLVb7vAXZoAumKibUTuQvuvhBgnfeK4Plazyyc/640?wx_fmt=png&from=appmsg)

解析 JSON 后，对话内容直接暴露了使用者的工作性质：

| 文件 | 会话标题 | 创建时间 | Token 数 |
| --- | --- | --- | --- |
| 1787729118199 | Nginx SSL Config Analysis | 2026-08-26 15:25:18 | 5,175 |
| 1787729252675 | Nginx Exchange Configuration | 2026-08-26 15:27:32 | 10,036,646 |
| 1787732785512 | Activity Controller MD5 Encryption | 2026-08-26 16:26:25 | 12,573 |

其中"Activity Controller MD5 Encryption"会话的第一条消息，是一整段 Java 源码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGicCTthPKur2S2X4rGa9DMuEASlNykiaA0XKaqyqNibuInWTphcZIxmbiagk2V5t0MfJT9I1bxpZFJBFIEjxePZEbRcS08brs5Qtg/640?wx_fmt=png&from=appmsg)

这段包名指向一套虚拟币交易平台后台系统。会话标题"MD5 加密"进一步说明，使用者当时正在分析该系统的口令加密逻辑——这类记录在案件中是**主观明知的直接证据**。

AnythingLLM 走的是另一条路：一个 Prisma 管理的 SQLite 数据库。

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcETPuOCwN6kNtgWR3ZEAxVXeCw6EaQen2qyShtYVupfIsCHLcKLZFCXTRpHmibofJogic6tDAdotll8ztUYz7QNfW0A1WYFCB13g/640?wx_fmt=png&from=appmsg)

三个工作区的名字本身就很有信息量：**「我的工作区」「比武竞赛解题」「小谢取证」**。而 `workspace_chats` 表里存着完整提问：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEaNBDBGKXLyLdFZBDhicBK0r5bwcKANJQKUATWySabWPsBQOHXOAnPlaW5ChZmTVl9DyLvVsK9yxeDnlHlgTSBfSsZw7507Vp8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcFnEp0JfVq9dyk8YDXMhelQljicaAvl3tRib6DV6Xy0Mkic7iaZe3qibgohauOIJK1Dt20Rla3fia3rJ4miaTNKDa241hiaunWyN1F1zOQ/640?wx_fmt=png&from=appmsg)

注意最后一条的 `response` 字段：里面不仅有模型回答，还有 `sources` 数组，把命中的**原始文档片段**整段回填进数据库。本案中回填的是一份名为「0414-V7 详细版.pdf」的取证竞赛答案解析，包含标准答案与解题步骤。也就是说——**RAG 向量库和响应缓存会把"参考资料"原件内容二次落盘，即使原文件已删除，内容仍在数据库里。**

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcE200P21fXXGr4tGvcBUjqekaibMMwZbBQMiaPzel5IWIWk2peJeTmHKwuCVTT6I8PNxQZhZ1tTIB1aWlG2LzB9VBxYrJeGQDAJg/640?wx_fmt=png&from=appmsg)

### 4.3　损坏会话文件：100% NUL 字节的启示

检材里最值得玩味的是一个被标记为损坏的文件：`1782888525218.conversation.json.corrupt`，3,255,120 字节。尝试解析直接失败，十六进制检查给出答案：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEq996rl0ezZ5SE0YZwRDJEjKEhUx1dHkI12ibgwtwiaRBdzLYYThZibQv8rdcounWFvcSfut8NWha9rqaHicNkz8l2I3lPiavOZVicg/640?wx_fmt=png&from=appmsg)

结论明确：**文件内容被整体清零，不是删除、不是截断，而是被零字节覆盖**。这排除了"文件系统残留可雕刻恢复"的可能——雕刻的前提是数据区还有原始字节，而这里已经被 0x00 填满。

但证据并没有消失，只是换了形态：

* **文件名保留了创建时间戳**

  ——`1782888525218` 换算为 2026-07-01 14:48:45，这是文件真实创建时刻；
* **配置文件的引用记录仍在**

  ——`conversation-config.json` 的 `selectedConversationHistory` 数组里，这个文件名出现了整整一次，证明它曾是被正常打开过的会话；
* **修改时间戳仍在**

  ——文件 mtime 为 2026-08-26 14:58:19，说明清零动作发生在 8 月 26 日，比创建时间晚了近两个月。

这是取证里一条通用规律：**元数据往往比内容更长寿**。文件名、时间戳、配置引用、目录项残留，构成了"内容已灭失但事实仍可证明"的证据链。遇到清零文件不要直接判"无价值"，先把元数据全部固定下来。

### 4.4　日志层：明文 prompt 与系统提示词泄露

LM Studio 的服务日志是最富矿的一层。本机共 34 个日志文件，按月份归档：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGiafXKibnH8biaaJdqjaZeibHmkdcJlDJKqaJMWKus2btpGCic7s9iaIUNLZyylRgic27mu3Gbv0Ec7UM0ibqO18971hnf1l6xIJxbN9A/640?wx_fmt=png&from=appmsg)

统计所有日志中的推理请求与来源 IP：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEeZqvaFicVzYkGsk9TWUy1ib0aibwOKCRkdTLOmeOU5jicZKm0VXBrxibLRIxDVrRwXzZwExgIsjefhkdYnvicTtXn5NKx8rvoYC3a8/640?wx_fmt=png&from=appmsg)

![推理请求来源 IP 统计](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHibXiaSk1ZBn7JAMjW9eriacv85zDLX4iaCjUib2jlKluictp6b3r3Frh2rQdPibzQ8QicgYggelxheyMEeibUhBtIYzBo3h0pwKgEmmAQ/640?wx_fmt=png&from=appmsg)

图3　推理请求来源 IP 统计（共 521 次）

这组 IP 很有讲头：`192.168.246.1` 与 `172.26.208.1` 是典型的 **WSL2 虚拟网段网关**，`169.254.91.196` 是 APIPA 链路本地地址。结合 `http-server-config.json` 里的配置：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGW9bgEP0EYKmkdA41HdRjnicGkB1W61JLsdxUO8g1m3EnRnNuwe0A3sPVE7SCm4TDs9Z3ndveE8K69SdGt2ibxiaBAKnXuOoOc7U/640?wx_fmt=png&from=appmsg)

两个高危配置一目了然：**服务绑定在 0.0.0.0:1234**，局域网内任何主机都能调用；**logSensitiveData 打开**，所有请求体被完整写入日志。这既是取证的福音（证据完整），也是安全的灾难（提问内容全量落盘、明文可读）。

日志里能还原出什么？把一段请求体从日志中提取出来：

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcE1xSmeB3UnGwgAwfZNVMmwQEmmOFegyJKu1gPVwCPVhYrqkictpsskW43THya4bBf5H4d23m4lAyLsMKwDlib1mv6SRtaSUMk58/640?wx_fmt=png&from=appmsg)

最后一段是本轮取证最意外的收获：日志里不只有用户的提问，还有**完整的 Agent 工具定义与系统提示词**——工具名、参数结构、参数说明全部明文。任何接入本地模型的智能体框架，只要开启详细日志，其内部提示词都会随之泄露。

### 4.5　缓存层：HF hub 的三层结构

HuggingFace 缓存目录的结构经常让新手困惑，它其实分三层：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcFs1iaVLYLxUC1ootS9ctGtdU1WbzBHfHib7BtHyh3wqteuiaMLRuzIDdHdo1zicWmJlk7Jj8jqZC0sicdFe9oLTzOiczbfB5M3lc81A/640?wx_fmt=png&from=appmsg)

关键点：**snaps...