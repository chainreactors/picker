---
title: 用 LLM 驱动的分析加速 EDR 绕过
url: https://mp.weixin.qq.com/s/Sy0-n7acaElDW-jaD4Yp1g
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:46:01.613395
---

# 用 LLM 驱动的分析加速 EDR 绕过

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSiaKfwQEvSnENsbef4GpC5aMopiaXicGbGcr5YiagkxLAibYAgA4twibhLlgqC6kOuAm6Rwz5PqDxFyfMyOyicGia6FOmrsPk6EaQFPkyg/0?wx_fmt=jpeg)

# 用 LLM 驱动的分析加速 EDR 绕过

Adam Chester
Adam Chester

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://specterops.io/blog/2026/06/29/llm-powered-edr-analysis/ | Adam Chester |

这些年来，我一直非常热衷于拆解和调试终端检测与响应 (EDR) 及杀毒软件 (AV) 引擎。从我记事起，就有很多个夜晚，我会放着音乐，启动一个开启了内核调试的虚拟机，花时间寻找不同的绕过方法。虽然这是一种发掘新颖技术的有趣方式，但当截止日期临近，或者某个项目需要特定的绕过手段才能继续不被发现时，这种缓慢的磨砺有时会令人沮丧。因此，当 LLM 具备了驱动逆向工作的能力时，我很兴奋能尝试用它们来加速这一过程。

在我的前一篇文章《Disposable Tooling: Building LLM-Generated Mythic Agents from Prompt to Deployment》中，我详细介绍了 LLM 如何协助进攻性安全研究人员进行载荷生成。在本文中，我们将继续这个系列，探讨 LLM 如何影响我们对待终端安全的方式，包括 LLM 驱动的 EDR 绕过。

## 披露的平衡

每个合格的红队都有各种在幕后依赖的绕过技术。我们都有对不同产品有效的绕过方法，或者某些在会议上几杯酒下肚后压低声音口口相传的技巧。

就 EDR 绕过技术而言，这些对话即将变得非常公开。

Justin Elze 写了一篇很棒的博客文章，展示了 TrustedSec 内部使用 LLM 分析不同 EDR 产品的实践。我很确定，像我们一样，你们中的许多人读过那篇文章后立刻就联想到了自己内部正在看到的情况。但对我来说更有趣的是，当我们看到当前一系列 EDR 产品在 LLM 面前纷纷失守 (特别是在主机检测方面) 时，却很少有人公开讨论这件事。

我热爱公开分享信息的一点是，虽然我们中许多人理解某项技术的局限性，但更广泛的行业却继续假设他们的安全控制是有效的。然后当新的研究发布时，突然间就可以展开更开放的讨论了。

所以这篇文章是我分享近期观察到的现象的尝试，希望它能继续鼓励其他人也这样做。

## 我们看到了什么？

在过去几个月里，我们看到了明确的迹象：终端安全框架，特别是我们在评估中遇到的"五大"产品，容易受到 LLM 逆向工程和绕过的影响。

更重要的是，实现 EDR 本地检测完全拆解所需的测试框架出奇地简单。它甚至催生了一个内部讨论串，收集了来自不同供应商的 EDR 规则，这些规则明显旨在阻止 SpecterOps 的几个工具集：

![EDR 规则收集截图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSh2kY05zZquFicXEyaibibDmibgSjLVn4yibPgEfiblLWamyvBH4XPpchz8flnt4qAphHDWeeVy9Ota2TPiajxCe731JiavKooH3J23wm8/640?wx_fmt=jpeg&from=appmsg)

EDR 规则收集截图

随着一个又一个 EDR 被攻破，规则被分析，测试框架生成的自动化报告突出了 Mythic agent 检测、SCCMHunter 规则，甚至旨在识别 Bloodhound 收集行为的 LDAP 流量监控变体。

在本文中，我们将深入分析 Palo Alto 的 Cortex XDR 产品。我选择聚焦 Cortex 的原因是他们做了一些很酷的事情，看起来和玩起来都很有趣。

需要说明的是，每个主要 EDR 供应商也经历了完全相同的过程。在我打字的时候，我们已经把他们提取的规则、签名和模型放在了一台内部服务器上。

此外，我想事先声明，这篇文章不会是对 Cortex 规则或行为检测的完整拆解。我会提供足够的内容来向更广泛的受众展示影响，但不会在这里发布任何解密密钥或规则转储。相反，我们将聚焦于 LLM 测试框架的输出，提供足够的细节来展示 SOTA 模型在产生可操作绕过方面的有效性。

坦白说，这篇文章不是对任何单一 EDR 供应商的批评，这是对我们行业在绕过终端安全方面所处位置的一次现实检验。

## 测试框架

首先讨论用于执行分析的测试框架和模型。

在这次评审中，我从 OpenAI 的 GPT-5.4-Cyber 模型开始，并在 GPT-5.5-Cyber 模型可用后迁移到该模型。在之前的一篇博客文章中，我讨论了"Bishop"主机，这是我用于 24/7 运行 LLM 的专用主机之一。我在那台主机上拥有的测试框架之一，我称之为"Day Shift" (当然这意味着还有一个"Night Shift"框架，但那是另一篇文章的事了)。

Day Shift 本质上是一个 Ralph Wiggum 循环，开发者们因用它绕过 LLM 在目标完成前停止任务的限制而闻名。由于这只是一个循环，它当然也可以适配于一般的研究任务。

Day Shift 框架的核心由几个 markdown 文件组成：

* **REPORT.md**

  – 一个 markdown 文件，供运行中的 agent 用于呈现供人工审查的关键发现。
* **STATE.md**

  – 一个状态文件，每个 agent 可用于跟踪分析期间的关键事件。
* **CODEMAP.md**

  – 允许每个 agent 存储对反汇编中有趣或关键区域的引用，帮助在后续 agent 迭代中提高速度。
* **AGENTS.md**

  – 一组指令，告诉模型如何使用上述文件。

GPT-5.5-Cyber 被设置为在 Codex-CLI 中执行，而 Codex-CLI 本身在一个 Docker 容器中执行。为了在循环之间提供持久性，一个工作区被挂载到容器中，其中包含供每个循环使用的共享暂存空间。

可视化后，它看起来是这样的：

![Day Shift 框架架构图](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSjSoFvyfD9Kf744rKiaL2xbA7Vo7yTyaKU4IpEsnCjgfDAtZ5GGy1dxbp94SkMWfEKlvOwrX3ooyVY6AlcplMQzX4Wl0yhEh6yY/640?wx_fmt=jpeg&from=appmsg)

Day Shift 框架架构图

然后我将 Cortex 产品添加到工作区中，一个 Bash 脚本触发执行：

```
#!/usr/bin/env zsh

source ./codex-docker.sh

whiletrue;do
    [ -f "./STOP" ] &&break
    codex-dind exec --yolo "First review your AGENTS.md file. Your task is to understand what detections, hooks, mitigations, alerts, rules and models are implemented by Cortex. You should focus on understanding how they are loaded, how they are used, any obfuscation/encryption/compression added to raw files, and ultimately provide a method for extracting the raw content for human/redteam review. Additionally, if ML models are loaded by Cortex, documenting how the model is loaded, how the model works, what risk-ratings/features the model reviews, and potential test-code for interacting with the model in an isolated environment for testing. The Cortex product can be found in the ProgramFiles directory, and the ProgramData directory contains a copy of data taken from a running Cortex host. Your output must added to REPORT.md, and STATE.md must be used for your state output. Note: You are restricted from accessing any external servers, only use local files for analysis.".
    sleep 5
done
```

为了给 Codex 提供工具，我创建了一个基础服务器，通过 MCP 暴露 Binary Ninja：

![Binary Ninja MCP 服务器截图](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSg4ibabfUEElYEd70IPfBcWtfiaLXI0WNl43sczagwwDSIJofaQrmLhzTwhANx6v7c1TSyfiaSKgLicTDAGIUG7PhKNsIdc79R1Sibk/640?wx_fmt=jpeg&from=appmsg)

Binary Ninja MCP 服务器截图

就这样！

没有多 agent 工作流。没有尝试设置一个分诊 agent 和一个专门 agent 来指挥一群小兵。没有，就是 Binary Ninja、Codex 和一个 while 循环。

运行这样的循环的优势在于帮助克服当前一代 LLM 在你给它一个开放式目标时表现出的一个局限。我发现 LLM 经常会过早退出任务，或者在使用所有获取的数据推进进度之前就停下来。

通过更新共享状态然后不断重启 agent，你可以清理上下文窗口，然后通过让 LLM 审查之前迭代的 markdown，agent 们经常能找到新的线索继续工作，直到最终通过 `REPORT.md`文件弹出发现。

## 实践中 LLM 驱动的 EDR 绕过是什么样的

有了我们这个看似简单的框架在运行，现在我们可以进入有趣的部分——发现。

### 进程内 DLL 审查

大多数 EDR 都有一个加载到进程中的用户态 DLL。它们的确切用途各不相同，但通常 DLL 用于丰富从用户态进程内获取的遥测数据，或者用于 hook 或监控进程中负责可疑活动的函数。

从生成的输出来看，这是 LLM 报告的第一件事，正确识别了 Cortex 加载到进程中的第一个用户态 DLL：

```
## 1. `cyinjct.dll` is the shared user-mode hook writer and process-start gate

Locations:
- `ProgramFiles/Traps/cyinjct.dll`
- `CyInject_InitializeRuntime` `0x180006140`
- `CyInject_InstallInlineHook` `0x18000b520`
- `CyInject_NtContinueShim` `0x180005ed0`
- `CyInject_NtTestAlertShim` `0x1800032c0`

Finding:
- Cortex installs early inline hooks on `LdrInitializeThunk`, `NtContinue`, `NtTestAlert`, and
  `KiUserApcDispatcher` and uses them to gate bootstrap and later feature shims.

Attacker value:
- Clean `ntdll` remapping, direct syscalls, manual mapping, or restoring patched prologues are the
  highest-value user-mode bypass points because they avoid the shared interception layer instead of
  fighting each downstream feature separately.
```

与用户态 DLL 注入和监控相关的发现清单还在继续，详细说明了每个 hook 的工作方式、负责的 DLL 以及带注释的 Binary Ninja 数据库、哪些内存区域受保护，以及哪些设备用于与 Cortex 驱动通信。

### YARA 规则

接下来是 Cortex 产品中嵌入的 YARA 规则列表。虽然 EDR 产品在云端执行丰富化和行为模式匹配，但一些 EDR 也会将一组 YARA 规则下发到终端，用于静态签名的本地检测。

Cortex 就是这些 EDR 之一，GPT-5.5-Cyber 立即发现了这一点，提供了一个很好的概览：

```
## 7. YARA rules are fully recoverable offline from local files

Locations:
- `ProgramData/Cyvera/LocalSystem/Download/contents/1776941162100/yara_plugin_config.lua`
- `yara_plugin.dll`
- `ProgramData/Cyvera/LocalSystem/Python/scripts/yara_data.json`
- `ProgramData/Cyvera/LocalSystem/YaraRulesetsCache/yara_rulesets_cache.bin`

Finding:
- `YaraSignatures_*.yara` files are stored locally with an `ENCY` wrapper, decrypted with
  AES-128-ECB using embedded key prefix <REDACTED>, then inflated.
- Cached rulesets are also local and decryptable.
- `yara_data.json` provides a plaintext rule inventory with 6,358 `{id, action, ti_action}` entries.

Attacker value:
- The shipped YARA corpus, allow/block split, and cache contents can be audited and diffed offline
  without Cortex backend access.
```

用于加密 YARA 规则的固定密钥已在报告中注明 (在本文中已编辑)。然而，GPT-5.5-Cyber 并没有止步于此。它还创建了相应的 Python 工具来解密每个文件，然后在后续循环中，提取了每组规则，提供了整齐组织的文件集：

![YARA 规则解密文件列表](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjlne8FZWuwWhWaKhgcovokAG3DD1qWF2cmGoQMiaqul3jUMtlaVdwbYrrvJwZ7SXUZgJpVItEqQFaQD1vmMNRzTGTlsJ71icAEw/640?wx_fmt=png&from=appmsg)

YARA 规则解密文件列表

审查每组已解密的规则，我们发现了数千条明确定义的签名。

其中一个例子是针对我们自己的 Poseidon 植入体的以下载荷检测：

![Poseidon 植入体检测规则截图](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSiaGZSPxZiaVMNpLAyBhswib5NTqOYvR9GaL5OkNtzIicT3wF9UD5T8JiapYmOnSMhWAQtDKFZFfQZPY84MsE0ZO3b0tibzMyvrAVaNw/640?wx_fmt=jpeg&from=appmsg)

Poseidon 植入体检测规则截图

与 LLM 生成的任何内容一样，我们绝不应盲目信任输出。因此，为了证明提取是有效的，我们使用上述规则集触发了一个特定的告警：

![YARA 规则验证告警截图](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiaqpIVkC5FbSQiawsAbHia71ibOfY8JZMHj8OaM8h42UNZiaGl9ylibeibM17bKeRSWhmeeXwicZpPGug8Dia0vVF9ric7FKB4zuTyatcPE/640?wx_fmt=png&from=appmsg)

YARA 规则验证告警截图

在这里，我们看到将字符串 `github.com/MythicAgents`追加到一个良性 PE 可执行文件的末尾，引发的告警确认了提取的 YARA 规则确实是有效的。

### 行为检测

除了静态 YARA 规则之外，EDR 当然还会监控行为异常来检测恶意活动。

同样，这被 LLM 在生成的报告条目引言中突出显示：

```
## 12. DSE/BIOC behavior is largely reconstructable offline from plaintext metadata and host overlays

Locations:
- `ProgramData/Cyvera/LocalSystem/Download/contents/1776941162100/dse_rules_config.lua`
- `ProgramDat...