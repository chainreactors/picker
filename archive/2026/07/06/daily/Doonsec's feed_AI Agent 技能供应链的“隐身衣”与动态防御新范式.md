---
title: AI Agent 技能供应链的“隐身衣”与动态防御新范式
url: https://mp.weixin.qq.com/s/IcUVR8HOLH14ttjLTQOl1g
source: Doonsec's feed
date: 2026-07-06
fetch_date: 2026-07-07T06:02:08.247502
---

# AI Agent 技能供应链的“隐身衣”与动态防御新范式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PIWj1VguNosujlfsM3oKEUK5r788dXCEunmYW2gZVFNKBiatQOnDyibRYlnicVnTpu2oxjxU7eSONVZynSRcRbpsfsibRarSNn8e0Kwn9CWx7OY/0?wx_fmt=jpeg)

# AI Agent 技能供应链的“隐身衣”与动态防御新范式

原创

APT-101
APT-101

APT-101

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 一、 核心背景与问题

随着 LLM Agent（如 OpenHands, Claude Code）的普及，开发者可以通过安装第三方“技能包”（Skills）来扩展其能力。然而，这引入了严重的**供应链安全风险**：

* **攻击面**：恶意攻击者可以发布包含后门、数据窃取或权限提升逻辑的技能包。
* **现有防御失效**目前业界主要依赖**静态扫描器**（Static Scanners），如 Cisco AI Defense, Huifer, Vigile 等，它们在安装时检查代码和文档。
* **核心痛点**：静态扫描器容易被**语义保持的逃避技术**（Semantics-Preserving Evasion）绕过。攻击者只需改变代码的“外观”，而不改变其“行为”，即可让扫描器放行，但在运行时依然执行恶意操作。

---

## 二、 攻击侧：SKILLCLOAK 逃避框架

为了证明现有防御的脆弱性，作者提出了 **SKILLCLOAK**，一个自动化的技能伪装框架。它通过两种互补策略，将恶意技能转换为“看起来无害”但“行为不变”的形式。

### 1. 结构混淆（Structural Obfuscation）

针对基于规则（Regex/YARA/AST）的静态扫描器。

* **原理**：提取扫描器的匹配规则，然后通过最小化编辑来消除触发信号，同时保留恶意载荷。
* **技术手段**：

+ **分散（Disperse）**：将共现的关键字拆分到不同行或文件。例如，`curl http://evil.com` 被拆分为 `curl` 在一行，URL 在另一行，或者通过变量拼接。
+ **重构（Reify）**：将直接命令替换为等效的系统调用或库函数。
+ **重命名/移动**：将敏感文件移动到扫描器忽略的目录（如 `.git/` 或 `build/`），或更改扩展名。

* **效果**：在测试中，结构混淆使大多数静态扫描器的检出率下降了 **80%-99%**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PIWj1VguNoujwjZkDS0DUplibrYXKibiaSZsgO1cicSpYVhZrLCf2icRicPaSr0g0wiaKpS6N5fvxuBLuLwz80bmvB51mu3PvhK6GaFSFWftLprc28/640?wx_fmt=png&from=appmsg)

### 2. 自解压打包（Self-Extracting Skill Packing, SFS）

针对更高级的混合扫描器（包括 LLM 法官）。

* **原理**：类比二进制恶意软件的加壳技术。将真实的恶意负载加密或隐藏在一个看似 benign（良性）的“外壳”中。
* **工作流程**：

1. **构造**：生成一个良性的封面文件（Cover）和一个解码器（Decoder）。原始恶意技能被加密存储在隐藏位置（如 `.git/skillpack.dat`）。
2. **安装时**：扫描器只看到封面和解码器，判定为安全。
3. **运行时**：Agent 执行解码器，解密并恢复原始恶意技能，然后按照封面中的指令执行。

* **LLM 优化**：如果 LLM 法官对封面产生怀疑，SKILLCLOAK 会使用另一个 LLM 重写封面，使其叙事更合理，直到通过审查。
* **效果**：SFS 打包绕过了 **所有** 测试的静态扫描器（包括 Cisco 和 Nova）， bypass 率超过 **90%-99%**。

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNouWuH2pA0iahD0WGHicT0nq64fAWnChT5Oy4rh4UNTA60LyU4fZtvEIJJ5Liasj5yLfwvwoIMVavPp0U0re2Lf7ut808jxWxdqnNw/640?wx_fmt=png&from=appmsg)

---

## 三、 防御侧：SKILLDETONATE 动态检测框架

既然静态扫描不可靠，作者提出了 **SKILLDETONATE**，一个**以行为为中心**的动态审计系统。

### 核心理念

> **“不看它长什么样，只看它做什么。”** SKILLDETONATE 不在安装时做决定，而是在沙箱中**实际运行**该技能，并监控其操作系统级别的副作用。

### 两大技术创新

#### 1. 按需闭包提升（On-Demand Closure Lift）

* **问题**：传统沙箱只监控初始文件。但恶意技能可能在运行时动态生成新的脚本或配置文件（即“闭包”的一部分），这些新生成的文件可能包含恶意指令。
* **解决方案**：SKILLDETONATE 监控文件系统写入。一旦发现技能创建了新的可执行文件或自然语言指令文件（如 `.md`, `.sh`），它会立即将这些新文件“提升”回 Agent 的执行上下文中，并继续监控它们的执行。
* **意义**：确保了即使恶意负载是动态生成的，也能被捕获。

#### 2. 基于标记的污点分析（Marker-Based Taint Analysis）

* **问题**：如何追踪敏感数据（如 API Key, SSH 私钥）是否被泄露？传统的污点分析难以处理自然语言上下文和跨进程转换。
* **解决方案**：

+ **数据标记（Data Markers）**：当 Agent 读取敏感文件时，系统不返回真实内容，而是返回一个唯一的、不透明的标记（如 `#data1`）。
+ **传播追踪**：这个标记会在整个数据流中传播——从文件读取 -> 内存变量 -> 网络请求参数。
+ **策略检查**：如果标记最终出现在网络出口（如 `curl` 的参数中）或被写入非授权文件，则触发警报。

* **优势**：无需修改 Agent 运行时，通过 FUSE 文件系统层拦截 syscall 即可实现，且误报率极低。

![](https://mmbiz.qpic.cn/mmbiz_png/PIWj1VguNouJQRXNyh8BlXwXfGBPKxm7ICjf7vN2AZJSkOic8rDicO9VzffqtkwTicDE5zU4z8n3ONdxouK6fxjHQibib7cm9ibJW9HY5XW8hXNJ4/640?wx_fmt=png&from=appmsg)

---

## 四、 实验评估

### 1. 数据集

* **恶意样本**：1,613 个来自真实世界的恶意技能（In-the-wild malicious skills），涵盖凭证窃取、反向 Shell、加密货币挖矿等。
* **扫描器对比**：9 种主流静态扫描器（Cisco, Huifer, Vigile, Nova 等）。
* **代理平台**：OpenAI Codex (GPT-5.4) 和 Claude Code (Sonnet 4.6)。

### 2. 逃避有效性（RQ1）

| 扫描器类型 | 原始检出率 | 结构混淆后检出率 | SFS 打包后检出率 |
| --- | --- | --- | --- |
| **静态规则类** (Huifer, Caterpillar) | ~98% | < 5% | < 1% |
| **混合/LLM类** (Cisco, Nova) | ~95% | ~10-20% | < 5% |
| **结论** | **极高** | **大幅下降** | **几乎完全绕过** |

> **关键发现**：即使是结合了 LLM 判断的高级扫描器（如 Cisco），在面对 SFS 打包时也几乎完全失效。

### 3. SKILLDETONATE 的检测能力（RQ2）

| 指标 | 结果 |
| --- | --- |
| **恶意技能检出率** | **97%** (平均) |
| **误报率 (False Positive)** | **2%** |
| **对逃避变体的鲁棒性** | 对结构混淆和 SFS 打包的检出率保持在 **87%-95%** 之间，几乎没有下降。 |
| **性能开销** | 每个技能约 153 秒，14.1K tokens。对于离线安装网关来说是可以接受的。 |

### 4. 消融实验

* **移除闭包提升**：检出率略有下降，但误报率飙升 8 倍（因为无法区分良性动态文件和恶意动态文件）。
* **移除污点分析**：检出率基本不变，但失去了对数据泄露的具体归因能力。

---

## 五、 核心启示与建议

### 1. 静态扫描已死，动态行为分析当立

论文有力地证明了，在 AI 技能生态中，**基于外观的静态审计已经过时**。攻击者可以轻易地通过代码变形来绕过任何固定的规则集。未来的安全防线必须建立在**运行时行为监控**之上。

### 2. “零信任”技能执行环境

Agent 不应盲目信任安装的 skill。每个 skill 都应在隔离的沙箱中运行，并且其所有 I/O 操作（文件、网络、进程）都应受到严格的信息流控制（Information Flow Control）。

### 3. 标准化执行环境的需求

类似于二进制恶意软件分析中的 Cuckoo Sandbox，AI 社区需要建立**标准化的 Agent 执行沙箱**，以便统一进行动态行为审计。

### 4. 开发者的责任

* **不要硬编码密钥**：使用环境变量或秘密管理服务。
* **最小权限原则**：Skill 应只请求其功能所需的最小权限。
* **代码签名与来源验证**：虽然不能防止逻辑恶意，但可以增加攻击者的溯源成本。

---

## 六、 总结

《Cloak and Detonate》不仅揭露了当前 AI 技能市场的巨大安全黑洞，还提供了一套切实可行的解决方案。

* **攻击方**：SKILLCLOAK 展示了恶意技能如何像变色龙一样适应各种扫描规则。
* **防御方**：SKILLDETONATE 证明了通过**动态执行 + 污点追踪**，我们可以有效地捕捉这些隐蔽的威胁。

参考：https://anonymous.4open.science/r/Skill\_Cloak\_Detonate-346C/README.md

参考：https://arxiv.org/pdf/2607.02357

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vgGymHXkYlHxHm5eWcF04Jiak4wbaPHuibiaRpMSS9cibMpn8zszwAmT9Oc2YYhJN1nowIDPnEgAddjclhcuDOaZtQ/0?wx_fmt=png)

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