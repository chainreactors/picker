---
title: 大模型（LLM）安全测试工具汇总
url: https://mp.weixin.qq.com/s/FvoZImHGTIMrgDZZhEscow
source: Doonsec's feed
date: 2026-09-13
fetch_date: 2026-09-14T07:18:28.982168
---

# 大模型（LLM）安全测试工具汇总

# 大模型（LLM）安全测试工具汇总

bafangwy
bafangwy

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 总体概览

| 工具 | 维护方 | 语言 | 核心定位 | 活跃度 |
| --- | --- | --- | --- | --- |
| Promptfoo | OpenAI（已收购） | TypeScript/Node.js | LLM评估 + 红队测试 | 极高 |
| PyRIT | Microsoft | Python | AI风险识别框架 | 高 |
| Garak | NVIDIA | Python | LLM漏洞扫描器 | 高 |
| FuzzyAI | CyberArk | Python | LLM模糊测试/越狱 | 中 |
| BenchLLM | V7 Labs | Python | LLM应用CI测试 | 低（2023年停更） |
| [Giskard | Giskard-AI | Python | Agent系统测试评估 | 高（v3重写中） |
| PurpleLlama | Meta | Python/C++ | 紫队安全框架 | 高 |
| Agentic Security | 社区 | Python | Agent/LLM漏洞扫描 | 高 |

---

## 工具详情

### 2.1 Promptfoo

| 属性 | 内容 |
| --- | --- |
| **GitHub** | promptfoo/promptfoo |
| **官网** | https://www.promptfoo.dev |
| **协议** | MIT |
| **安装** | `npm install -g promptfoo` / `pip install promptfoo` |

#### 功能特点

* • 同时支持 **LLM效果评估（Evals）** 和 **红队测试（Red Teaming）**
* • 支持 100+ 种模型提供商（OpenAI、Anthropic、Azure、Bedrock、Ollama 等）
* • 提供 CLI、Node.js 库、Web UI 三种使用方式
* • 内置丰富的安全漏洞扫描插件（提示注入、越狱、数据泄露、幻觉等）
* • 支持 CI/CD 集成，可自动生成安全报告
* • 支持代码扫描（Code Scanning），检测 PR 中的 LLM 安全问题
* • **2025年已被 OpenAI 收购**，仍保持 MIT 开源

#### 使用场景

* • 企业 LLM 应用上线前的安全评估
* • 持续集成中的自动化红队测试
* • 模型选型时的横向对比测试
* • 提示词工程的效果验证

#### 快速开始

```
npm install -g promptfoo
promptfoo init --example getting-started
cd getting-started
promptfoo eval
promptfoo view
```

---

### 2.2 PyRIT

| 属性 | 内容 |
| --- | --- |
| **全称** | Python Risk Identification Tool for generative AI |
| **GitHub** | microsoft/PyRIT |
| **官网** | https://microsoft.github.io/PyRIT |
| **协议** | MIT |
| **安装** | `pip install pyrit` |

#### 功能特点

* • 微软官方出品，专为生成式 AI 系统安全设计
* • 模块化架构：攻击者（Attacker）、目标（Target）、评分器（Scorer）分离
* • 支持自动化攻击编排和多轮对话攻击
* • 内置多种攻击技术（Crescendo、Violent Durien 等）
* • 支持数据集加载器（如 0DIN 威胁情报 Feed）
* • 提供 GUI 界面和 Azure 部署模板
* • 支持 Azure Key Vault 集成管理密钥

#### 使用场景

* • 企业级 AI 系统的红队演练
* • 与 Azure 生态深度集成的安全测试
* • 多轮对话场景的安全评估
* • 学术研究中的 AI 攻击方法验证

---

### 2.3 Garak

| 属性 | 内容 |
| --- | --- |
| **全称** | Generative AI Red-teaming & Assessment Kit |
| **GitHub** | NVIDIA/garak |
| **官网** | https://garak.ai |
| **文档** | https://docs.garak.ai |
| **协议** | Apache-2.0 |
| **安装** | `pip install -U garak` |

#### 功能特点

* • NVIDIA 官方出品，定位为"LLM 版的 nmap/metasploit"
* • 探测类型最全面：幻觉、数据泄露、提示注入、毒性生成、越狱、XSS 等
* • 支持静态探测（Static）、动态探测（Dynamic）和自适应探测（Adaptive）
* • 支持几乎所有主流模型接口（HuggingFace、OpenAI、Bedrock、NIM、REST 等）
* • 插件化架构：Probe（探测）、Detector（检测）、Evaluator（评估）分离
* • 生成详细的 JSONL 报告和命中日志

#### 内置探测类型

| 探测类型 | 说明 |
| --- | --- |
| `dan` | DAN 及类似越狱攻击 |
| `encoding` | 编码型提示注入 |
| `promptinject` | PromptInject 框架攻击 |
| `leakreplay` | 训练数据泄露检测 |
| `malwaregen` | 恶意代码生成检测 |
| `xss` | XSS 和数据外泄检测 |
| `snowball` | 雪球式幻觉探测 |
| `gcg` | 对抗性后缀攻击 |

#### 使用场景

* • 对自研或私有化部署 LLM 的全面安全扫描
* • 代码解释器类应用的安全评估
* • 需要高度定制化探测策略的测试
* • 红队测试中的自动化漏洞发现

#### 快速开始

```
python -m garak --target_type openai --target_name gpt-5-nano --probes encoding
```

---

### 2.4 FuzzyAI

| 属性 | 内容 |
| --- | --- |
| **GitHub** | cyberark/FuzzyAI |
| **协议** | Apache-2.0 |
| **安装** | `pip install git+https://github.com/cyberark/FuzzyAI.git` |

#### 功能特点

* • CyberArk 出品，专注于 **LLM 模糊测试（Fuzzing）**
* • 内置 15+ 种越狱攻击方法
* • 支持变异型、生成型和智能型模糊测试
* • 提供 Web UI（实验性）和 Jupyter Notebook 示例
* • 支持自定义 REST API 作为测试目标
* • 支持分类器模型对输出进行自动评估

#### 内置攻击方法

| 攻击类型 | 说明 |
| --- | --- |
| ArtPrompt | ASCII Art 越狱攻击 |
| PAIR | 自动迭代对抗提示生成 |
| Many-shot | 多示例对话越狱 |
| Crescendo | 渐进式对话诱导 |
| ASCII Smuggling | Unicode Tag 字符隐藏指令 |
| Genetic | 遗传算法优化对抗提示 |
| ActorAttack | 基于行动者网络理论的语义攻击 |
| SI-Attack | 乱序不一致性攻击 |

#### 使用场景

* • 专门用于发现 LLM 的越狱漏洞
* • 对 API 接口的模糊测试
* • 需要快速验证多种攻击方法的场景
* • 安全研究中的对抗性提示生成

#### 快速开始

```
fuzzyai fuzz -m ollama/llama3.1 -a def -t "Harmful_Prompt"
```

---

### 2.5 BenchLLM

| 属性 | 内容 |
| --- | --- |
| **GitHub** | v7labs/benchllm |
| **官网** | https://benchllm.com |
| **协议** | MIT |
| **安装** | `pip install benchllm` |

#### 功能特点

* • V7 Labs 出品，定位为"LLM 应用的 CI 测试框架"
* • 测试与评估分离的两步方法论
* • 支持语义相似度评估（GPT-3/4）、Embedding 相似度、字符串匹配、人工评估
* • 支持函数 Mock，便于测试需要外部调用的 Agent
* • 通过 `@benchllm.test` 装饰器标记测试函数
* • 支持缓存加速和并行评估

#### 使用场景

* • LLM 应用的功能正确性测试
* • LangChain/Agent 链路的回归测试
* • 需要与现有 Python 测试框架集成的场景

> **注意**：该项目自 2023 年 7 月后更新较少，活跃度较低，建议谨慎采用。

---

### 2.6 Giskard

| 属性 | 内容 |
| --- | --- |
| **GitHub** | Giskard-AI/giskard-oss |
| **官网** | https://www.giskard.ai |
| **文档** | https://docs.giskard.ai |
| **协议** | Apache-2.0 |
| **安装** | `pip install giskard` |

#### 功能特点

* • 欧洲 AI 安全公司 Giskard-AI 出品
* • **v3 版本全新重写**，专为动态多轮 Agent 测试设计
* • 模块化包架构：

+ • `giskard-checks`：测试评估（场景 API、内置检查、LLM-as-judge）
+ • `giskard-scan`：Agent 漏洞扫描（红队、提示注入、数据泄露）
+ • `giskard-rag`：RAG 评估与合成数据生成

* • 支持 LLM-as-Judge 评估模式
* • v2 版本仍可用，包含 Scan（自动漏洞检测）和 RAGET（RAG 测试集生成）

#### 使用场景

* • RAG 系统的质量和安全评估
* • Agent 多轮对话测试
* • 模型偏见和公平性检测
* • 需要生成合成测试数据的场景

#### 快速开始（v3）

```
from giskard.checks import Scenario, Groundedness

scenario = (
    Scenario("test_dynamic_output")
    .interact(inputs="What is the capital of France?", outputs=get_answer)
    .check(Groundedness(name="answer is grounded", ...))
)
result = await scenario.run()
```

---

### 2.7 PurpleLlama

| 属性 | 内容 |
| --- | --- |
| **GitHub** | meta-llama/PurpleLlama |
| **协议** | MIT / Llama Community License |

#### 功能特点

* • Meta 官方出品，\*\*紫队（Purple Teaming）\*\*理念
* • 包含多个子项目：

| 子项目 | 说明 |
| --- | --- |
| **CyberSecEval** | 网络安全评估基准（v3 支持视觉提示注入、钓鱼、自主网络攻击） |
| **Llama Guard** | 输入/输出内容审核模型（已发布到 v4） |
| **Prompt Guard** | 提示注入和越狱检测模型 |
| **CodeShield** | 不安全代码过滤工具 |
| **LlamaFirewall** | 多层安全防火墙 |

#### 使用场景

* • 需要标准化安全评估基准的场景
* • 部署输入/输出安全护栏
* • 代码生成类应用的安全过滤
* • 与 Llama 模型生态配合使用

---

### 2.8 Agentic Security

| 属性 | 内容 |
| --- | --- |
| **GitHub** | msoedov/agentic\_security |
| **文档** | https://agentic-security.vercel.app |
| **协议** | Apache-2.0 |
| **安装** | `pip install agentic_security` |

#### 功能特点

* • 专为 **Agent 工作流和 LLM** 设计的开源漏洞扫描器
* • 支持多模态攻击（文本、图像、音频）
* • 支持多步越狱攻击模拟
* • 集成 Garak、InspectAI、llm-adaptive-attacks 等工具
* • 支持动态数据集变异（ROT13、Base64、乱序等）
* • 提供 Web UI 和 CI/CD 集成
* • 支持成本控制和预算限制

#### 使用场景

* • Agent 系统的持续安全扫描
* • 多模态 LLM 的安全测试
* • CI 流水线中的自动化安全检查
* • 需要控制测试成本的场景

#### 快速开始

```
agentic_security
# 启动后访问 http://0.0.0.0:8718
```

---

## 选型建议

| 你的需求 | 推荐工具 | 理由 |
| --- | --- | --- |
| 最全面的 LLM 安全测试（红队+评估） | **Promptfoo** | 功能最全、生态最大、已被 OpenAI 认可 |
| 微软/Azure 生态深度集成 | **PyRIT** | 微软官方出品，Azure 部署模板齐全 |
| 类似 nmap 的 LLM 漏洞扫描 | **Garak** | NVIDIA 出品，探测类型最丰富 |
| 专门做越狱/模糊测试 | **FuzzyAI** | 攻击方法最多，模糊测试专业 |
| RAG/Agent 系统测试 | **Giskard** | v3 专为 Agent 设计，RAG 评估能力强 |
| 部署内容安全护栏 | **PurpleLlama** | Meta 出品，包含 LlamaGuard、PromptGuard 等成熟护栏 |
| Agent 工作流持续扫描 | **Agentic Security** | 支持多模态、多步攻击，CI 集成友好 |
| LLM 应用功能回归测试 | **BenchLLM** | 注意：活跃度较低，建议谨慎采用 |

---

## 运行示例

以下示例演示各工具如何对**OpenAI GPT模型**或**自定义HTTP接口**进行安全测试。

### 3.1 Promptfoo - 测试HTTP接口

#### 场景：测试一个REST API对话接口

**Step 1: 创建配置文件 `promptfooconfig.yaml`**

```
targets:
  - id: my-api
    config:
      url: 'https://api.example.com/v1/chat'
      method: POST
      headers:
        Content-Type: application/json
        Authorization: Bearer ${API_KEY}
      body:
        messages:
          - role: user
            content: '{{prompt}}'
      responseParser: 'json.choices[0].message.content'

redteam:
  plugins:
    - id: harmful
    - id: pii
    - id: prompt-injection
    - id: jailbreak
  strategies:
    - id: jailbreak
    - id: prompt-injection
```

**Step 2: 运行红队测试**

```
export API_KEY=sk-your-key
export OPENAI_API_KEY=sk-your-key

# 初始化红队配置
promptfoo redteam init

# 运行测试
promptfoo redteam run

# 查看Web报告
promptfoo view
```

**Step 3: 测试结果示例**

```
╔══════════════════════════════════════════════════════════════╗
║ Promptfoo Red Team Report                                    ║
╠══════════════════════════════════════════════════════════════╣
║ Plugin          │ Pass │ Fail │ Pass Rate                   ║
╠═════════════════╪══════╪══════╪═════════════════════════════╣
║ harmful         │ 78   │ 22   │ 78.0%                       ║
║ pii             │ 95   │ 5    │ 95.0%                       ║
║ prompt-i...