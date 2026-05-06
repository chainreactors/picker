---
title: DeepZero: 睡梦中自动化挖掘 Windows 内核驱动的 0day
url: https://mp.weixin.qq.com/s/i6IBsXxA5qwbgdX6I7TkSA
source: Doonsec's feed
date: 2026-05-05
fetch_date: 2026-05-06T05:07:32.592077
---

# DeepZero: 睡梦中自动化挖掘 Windows 内核驱动的 0day

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSia76rrJE81icJQXKnkWbxHibh1P9icCj66FzJqSD7julcJNFiaRSGdFj50sqz3SpHaJLDBUjZpr6Sibmlj5lr811TkOiaJ8Hd95XRLoc/0?wx_fmt=jpeg)

# DeepZero: 睡梦中自动化挖掘 Windows 内核驱动的 0day

Cyber News
Cyber News

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://cyberwarrior76.substack.com/p/deepzero-automating-zero-day-discovery | Cyber News Network |

在自带漏洞驱动 (Bring Your Own Vulnerable Driver, BYOVD) 攻击已成为勒索软件运营者与民族国家级 APT 惯用利器的当下,开发者 **416rehman**推出的一个新开源项目正在彻底改写内核漏洞研究的经济格局。**DeepZero**是一款面向 Python 3.11+ 的自动化漏洞研究框架,它借助 AI agent 对数以千计的 Windows 内核驱动进行原生级别的解析、反编译与分析,从中挖掘可被利用的 IOCTL。它的宣传语 *"Find zero-days while you sleep" (睡梦中也能挖到 0day)*并非营销噱头:该框架被明确设计为一个可断点续跑、并行化的流水线引擎,能够在无人值守的情况下持续吞吐海量驱动样本。

本文将拆解 DeepZero 究竟做了什么、为何对威胁情报与 DFIR 社区意义重大,以及它在架构层面是如何运作的。

## DeepZero 是什么

DeepZero 是一个面向漏洞研究的 **"流水线即 YAML" 编排引擎 (pipeline-as-YAML orchestration engine)**。研究人员不必再用脆弱的 bash 胶水脚本把反编译器、静态分析器和 LLM 硬拼在一起,而是以一份 YAML 文件声明分析流水线,由 DeepZero 负责编排、并行、容错与状态持久化。

该项目采用 MIT 许可证,以 Python 为主 (98.9% Python, 1.1% Jinja),可同时在 Windows 与 Linux 上运行,目前共有 124 stars 和 15 forks — 这一数字看似不起眼,却低估了代码库背后的野心。其核心能力包括:

* 流水线即 YAML — 以声明式方式串联 ingest、filter、transform 与 LLM 评估等阶段
* 通过 ThreadPoolExecutor 实现并行执行,且每个阶段的并发度都可单独配置
* 可断点续跑 — 每个样本的状态以原子方式落盘,因此按下 `Ctrl+C`后重新运行会自动从上次中断处接续
* 通过 Jinja2 提示词模板与 LiteLLM 集成 LLM (兼容任意供应商)
* 处理器可扩展,以 Python 类形式编写,并在 YAML 中按路径引用
* 一个 (开发中 / 实验性) 用于查询运行状态的 REST API

## DeepZero 所瞄准的 BYOVD 难题

仓库中随附的旗舰用例是 **LOLDrivers pipeline**,专门用于在 Windows 内核驱动中搜寻 BYOVD 攻击面。所谓 BYOVD — 攻击者加载一份合法签名却存在漏洞的驱动以获得内核级代码执行权限 — 已被从 Scattered Spider 到朝鲜 Lazarus 关联团伙在内的多个组织武器化。研究界最主要的防御数据库是 loldrivers.io,而 DeepZero 明确将其作为 *阻断名单 (blocklist)*来使用,以便研究者把精力集中在 **尚未被收录的驱动**上 — 也就是新鲜 0day 的候选目标。

## 架构:四种处理器类型

每条 DeepZero 流水线都以一个 **Ingest**处理器作为起点,后续可任意组合 **Map**、**BulkMap**与 **Reduce**处理器,而每种处理器都具有不同的输入/输出语义。

![DeepZero 处理器流水线示意图](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjVRx4D0v2tSDUjQDcYPxG7mia9dmqyHsbTjUjCojSQGsaf62eE5Z7hCjBc16bKCRhujhk9LyCHb41icR2ePEeHDtOR0Ioqlnyts/640?wx_fmt=png&from=appmsg)

每个 Map 处理器都会返回一个 `ProcessorResult`,其结果有三种可能:`ok`(样本继续向下传递)、`filter`(主动剔除) 或 `fail`(处理出错) — 这让引擎在整次运行过程中都能清晰地保留三态判定追踪。

## LOLDrivers Pipeline 详解

仓库自带的 `pipelines/loldrivers/`流水线是一条由七个阶段组成的漏洞研究流水线:

1. `discover`

   (`pe_ingest`) — 借助 LIEF 进行 PE 头部解析的 ingest 阶段;提取驱动元数据与攻击面相关信号
2. `kernel_filter`

   (`metadata_filter`) — 仅保留具有 IOCTL 接口的内核态驱动,并按 SHA256 去重
3. `loldrivers_filter`

   — 排除已在 loldrivers.io 上被收录的驱动 (已知不良跳过列表)
4. `decompile`

   (`ghidra_decompile`) — 使用 Ghidra 无头模式进行反编译,并提取 IOCTL 分发逻辑
5. `semgrep_scanner`

   — 使用自定义规则对反编译后的 C 源码批量执行 semgrep 扫描
6. `pick_top_10`

   (`top_k`) — 按 semgrep 命中数量排序,留下前 10 个候选目标
7. `assess`

   (`generic_llm`) — 由 LLM 对每个剩余候选样本做深度分析

随附的 semgrep 规则覆盖了经典的内核驱动漏洞类别:`arbitrary_rw`、`buffer_overflow`、`method_neither`与 `msr_access`。LLM 评估阶段使用 Jinja2 提示词模板,支持高达 900,000 tokens 的上下文窗口,并能通过正则表达式将输出分类为 `[VULNERABLE]`/ `[SAFE]`标签。

## 状态持久化与容错

DeepZero 在状态模型上的设计是其最贴近威胁研究人员需求的亮点之一。所有运行状态都存放在 `work/<pipeline>/`目录下,每个样本拥有独立的子目录,其中包含 `state.json`、一个供 LLM 阅读的自动生成 `context.md`,以及处理器产生的工件 (反编译源码、漏洞发现等)。写入操作均为 **原子化**(先写入临时文件,再 `os.replace`),并且针对 Windows 上短暂出现的反病毒文件锁问题做了重试处理 — 这在扫描内核驱动时是相当贴心的考量,因为扫描内核驱动几乎一定会触发 AV。再次执行完全相同的命令会立刻从磁盘状态恢复;`--clean`则会清除此前所有状态。

## CLI 命令面

`deepzero`CLI 暴露了完整的工作流:

* `deepzero run <target> -p <pipeline>`

  — 执行或自动恢复一条流水线
* `deepzero status -p <name>`

  — 查看运行状态
* `deepzero validate`

  — 在不执行的情况下检查流水线定义
* `deepzero list-processors`

  — 枚举所有内置处理器
* `deepzero init <name>`

  — 生成新流水线骨架
* `deepzero interactive -m openai/gpt-4o`

  — 基于 LLM 的 REPL,可直接对运行数据进行问答
* `deepzero serve`

  — 启动 (实验性的) REST API,运行于 Starlette + Uvicorn 之上

REST API 暴露了一组只读端点,包括 `/api/runs`、`/api/samples`(可按 verdict/stage/status 过滤) 和 `/api/samples/{id}/artifacts/{name}`— 不过维护者已醒目地标注其仍在开发中且部分功能存在故障。

## 内置处理器

DeepZero 开箱即用,自带七种内置处理器,覆盖了常见的流水线原语:

* `file_discovery`

  — 带 SHA256 哈希的 ingest
* `metadata_filter`

  — 字段相等性、最小/最大阈值、去重
* `hash_exclude`

  — 内联或文件形式的哈希排除
* `generic_llm`

  — Jinja2 → LiteLLM → 输出文件,可选地配合正则进行结果分类
* `generic_command`

  — 把任意 shell 命令封装为一个阶段,并支持模板变量替换
* `top_k`

  — 按数值指标保留前 N 个
* `sort`

  — 仅按指标重新排序,但不做过滤

作为示例随附的外部处理器包括 `ghidra_decompile`、`loldrivers_filter`、`pe_ingest`与 `semgrep_scanner`。

## 它对威胁情报为何重要

DeepZero 是 **AI 辅助进攻性安全工具链 (AI-assisted offensive security tooling)**这一日益壮大类别中的一员;在这类工具中,LLM 不再只是代码评审者,而是已经成为漏洞发现流水线中的活跃环节。Ghidra 无头反编译、semgrep 静态规则,加上对排序后的候选样本做 900k token 级别的 LLM 评估,这一组合代表了一种务实且具成本意识的流水线思路:让廉价的过滤器先把样本库筛一遍,再让昂贵的 AI 阶段登场。对于红队而言,这极大地降低了 BYOVD 狩猎的成本;对于蓝队和 CTI 分析师而言,这则意味着随着此类框架的扩散,防御方应当预期到将有一批 \_新近披露的\_、签名合法但存在漏洞的驱动出现在勒索软件作业中。

## 快速上手

安装方式是标准的 Python 流程:对仓库执行 `git clone`,运行 `pip install -e .`,通过 `cp .env.example .env`配置 LLM API 密钥,然后将 CLI 指向某个驱动样本库,例如开源的 Snappy Driver Installer 驱动包。快速启动命令为:

`deepzero run C:\drivers -p .\pipelines\loldrivers\pipeline.yaml`

DeepZero 会并行执行任务、缓存中间产物、通过 Rich 渲染实时终端仪表盘,并在再次运行时自动恢复进度。

## 结语

DeepZero 架构精良、维护活跃 (撰文时已积累 71 次提交,绝大部分集中于最近一周内),是一款专为 BYOVD 0day 狩猎打造的自动化漏洞研究框架,其简洁的可扩展原语完全可以推广到 Windows 内核驱动以外的领域。它真正的贡献并不在于某个巧妙的小技巧 — 而在于一种坚持:漏洞研究流水线理应享有与数据工程流水线同等的工程严谨度,即声明式配置、原子化状态、可断点续跑以及可插拔阶段。对于希望以 LLM 增强方式狩猎漏洞、又不想亲手把十种工具粘合在一起的威胁研究者而言,这是今年最值得关注的开源发布之一。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgKPGhr5FRnEaV7qQickzpWlN4Q0lzzklBGhHficUE3MqciazBfDMVGYba7uYNdAObOiaKvnNjvhKhYWfibVORfrFVklnyHGdWgiarMo/640?wx_fmt=png&from=appmsg)

---

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

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