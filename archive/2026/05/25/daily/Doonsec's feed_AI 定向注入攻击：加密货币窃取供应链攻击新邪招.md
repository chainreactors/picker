---
title: AI 定向注入攻击：加密货币窃取供应链攻击新邪招
url: https://mp.weixin.qq.com/s/OkukaJ2sWaVj6BaH4oMcOQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:03:46.363514
---

# AI 定向注入攻击：加密货币窃取供应链攻击新邪招

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOqib3DJM0p4KxictOk19ibIOCj5wIMFVP6OJJoyncNEsXwxCX7aY7WsF4iaKloeZCg5BLYvVqQeetvrHVLPUbd7RpfEhic2FWeVEib31U/0?wx_fmt=jpeg)

# AI 定向注入攻击：加密货币窃取供应链攻击新邪招

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 一、事件概述

奇安信威胁情报中心监测到2026年5月22日至5月24日，Socket研究团队发现并披露了一场代号为 **"TrapDoor"** 的大规模跨生态系统供应链攻击活动。该攻击同时针对 **npm、PyPI 和 Crates.io** 三大主流软件包仓库，发布超过 **34 个恶意包** 及 **384+ 个关联版本**，专门针对加密货币、DeFi、Solana 生态和 AI 开发社区的开发者群体进行精确打击。

本次攻击活动具有高度协调性，利用各生态系统特有的执行机制（npm postinstall 钩子、Python 导入时执行、Rust build.rs 构建脚本）实现恶意代码的隐蔽触发，呈现出典型的"低安装量、高目标价值"高级供应链威胁特征。

| 属性 | 详情 |
| --- | --- |
| **威胁代号** | TrapDoor |
| **攻击者账号** | `ddjidd564` (GitHub)、`asdxzxc` (npm)、`asdmini67` / `dae5411` (PyPI) |
| **首次发现** | 2026-05-22 20:20:18 UTC (PyPI: eth-security-auditor@0.1.0) |
| **活跃周期** | 2026-05-21 至 2026-05-24 (约72小时持续活跃) |
| **目标人群** | Crypto/DeFi 开发者、Solana/Sui/Move 开发者、AI 工具链开发者 |
| **攻击目标** | SSH 密钥、加密钱包、云凭证、GitHub Token、浏览器数据、环境变量 |
| **涉及生态** | npm (20+包) / PyPI (7包) / Crates.io (6包) |

---

## 二、攻击技术分析

### 2.1 攻击向量概览

TrapDoor 展现了**跨生态系统的多平台协同攻击能力**，针对不同包管理器采用定制化的执行策略：

```
┌─────────────────────────────────────────────────────────────────┐
│                      TrapDoor 攻击架构                           │
├──────────────┬──────────────┬───────────────────────────────────┤
│   npm 生态    │   PyPI 生态   │         Crates.io 生态            │
├──────────────┼──────────────┼───────────────────────────────────┤
│ postinstall  │ import 时执行 │ build.rs 编译期执行               │
│ 钩子触发     │ 远程 JS 载荷  │ 本地密钥库窃取                     │
│              │ (node -e 执行)│ XOR加密 → GitHub Gist 外泄       │
├──────────────┼──────────────┼───────────────────────────────────┤
│ 共享载荷:    │ 远程载荷托管: │ 硬编码密钥:                       │
│ trap-core.js │ ddjidd564.    │ cargo-build-helper-2026           │
│ (1,149行)    │ github.io     │                                   │
└──────────────┴──────────────┴───────────────────────────────────┘
         │                │                  │
         └────────────────┼──────────────────┘
                          ▼
            ┌─────────────────────────┐
            │   统一 C2 与基础设施     │
            │  ddjidd564.github.io    │
            │  GitHub Gist 数据外泄    │
            │  GitHub PR 传播扩散      │
            └─────────────────────────┘
```

### 2.2 npm 平台攻击机制

npm 平台的攻击是该活动中**最复杂、最广泛**的部分。恶意包通过 `postinstall` 脚本在安装时自动执行名为 **trap-core.js** 的共享载荷（48,485 字节，1,149 行）。该载荷具备以下能力：

**凭证窃取范围：**

* SSH 私钥 (`~/.ssh/`)
* AWS 凭证（环境变量、配置文件、IMDS）
* GitHub Token（通过 `gh auth token` 生成及扫描 `.npmrc`）
* Sui / Solana / Aptos 钱包数据
* 浏览器扩展钱包数据（Chrome/Firefox 钱包插件）
* 浏览器登录数据库和 Cookie
* 环境变量和 `.env` 文件
* API 密钥（通过 TruffleHog 扫描）

**持久化机制（多层驻留）：**

| 持久化路径 | 技术手段 | 目的 |
| --- | --- | --- |
| `.cursorrules` | AI 工具配置文件注入 | 感染 AI 编程助手 |
| `CLAUDE.md` | Claude 配置文件注入 | 诱导 AI 执行恶意指令 |
| Git Hooks | `pre-commit` / `post-merge` 钩子 | 代码提交时触发 |
| Shell Hooks | `.bashrc` / `.zshrc` 修改 | 终端启动时激活 |
| systemd | 系统服务注册 | 开机自启 |
| cron | 定时任务 | 周期性执行 |
| SSH 传播 | 复用窃取 SSH 密钥 | 横向移动 |

**凭证验证机制：**载荷主动通过 AWS 和 GitHub API 验证窃取凭证的有效性，筛选高价值凭证，提高攻击效率。

**横向移动：**利用窃取的 SSH 密钥尝试连接其他主机，将受感染的开发机作为跳板入侵组织内网基础设施。

**加密方式：**npm 载荷采用 **Fernet + ECDH** 混合加密，远高于典型恶意包的加密水平。

### 2.3 PyPI 平台攻击机制

PyPI 恶意包采用**导入时执行**（import-time execution）策略：

1. Python 包在 `__init__.py` 中植入恶意代码
2. 首次 import 时自动触发
3. 从攻击者控制的 `ddjidd564.github.io` 下载远程 JavaScript 载荷
4. 通过 `node -e` 执行下载的 JavaScript 代码

**技术优势（攻击者视角）：**

* 外部托管载荷可随时更新，无需发布新版 PyPI 包
* Python 与 Node.js 跨语言执行增加分析难度
* 动态获取载荷有助于规避静态检测

### 2.4 Crates.io (Rust) 平台攻击机制

Crates.io 恶意包专门针对 **Sui 和 Move** 开发者生态：

1. 利用 Rust 的 `build.rs` 构建脚本在**编译阶段自动执行**
2. 搜索本地 Sui 密钥库文件
3. 使用硬编码 XOR 密钥 `cargo-build-helper-2026` 加密窃取的数据
4. 通过 GitHub Gist API 外泄加密数据

**关键影响：**

* `build.rs` 在编译时执行，开发者**尚未运行任何包功能**即已被感染
* 对使用 Sui/Move 进行智能合约开发的区块链开发者构成严重威胁
* 密钥库（keystore）直接泄露可导致加密资产完全失控

### 2.5 AI 定向注入攻击（创新手法）

TrapDoor 最独特的攻击维度是**针对 AI 编程助手的配置注入**：

1. **零宽度 Unicode 字符隐藏指令**：在 `.cursorrules` 和 `CLAUDE.md` 文件中植入使用零宽字符的隐藏指令
2. **伪装为安全审计**：诱导 AI 助手执行"安全扫描"工作流，实则在后台收集和窃取敏感数据
3. **GitHub Pages 诱饵网站**：`ddjidd564.github.io/defi-security-best-practices/` 渲染为看似正常的 HTML 网站，试图诱导 AI 助手运行恶意安全扫描
4. **AI 工具链 PR 投毒**：攻击者向多个知名 AI/开发工具项目提交 PR，试图将恶意配置文件合入主流项目：

* `browser-use/browser-use`
* `langchain-ai/langchain`
* `langflow-ai/langflow`
* `run-llama/llama_index`
* `FoundationAgents/MetaGPT`
* `OpenHands/OpenHands`

### 2.6 攻击者基础设施与工具链

**GitHub 账号 `ddjidd564` 维护的仓库矩阵：**

| 仓库名称 | 功能描述 |
| --- | --- |
| `defi-security-best-practices` | 主要载荷与配置托管 |
| `AUDIT-MATRIX.md` | "Universal AI Agent Extraction Framework" 设计文档 |
| `BYPASS.md` | 绕过检测技术文档 |
| `PAYLOAD.md` | 载荷行为与攻击机制文档 |
| `SWARM.md` | 协调扩展概念描述 |
| `env-security-scanner` | MCP/AI Agent 诱饵仓库（伪装环境审计工具） |
| `smart-contract-audit-toolkit` | 智能合约审计工具伪装 |
| `defi-profit-scanner` | DeFi 扫描/利润发现诱饵 |
| `web3-dev-toolkit-2026` | Web3 开发工具伪装 |
| `solidity-gas-optimizer` | Solidity 优化工具伪装 |

**攻击标记：** `P-2024-001` 在多个组件中重复出现，可用于关联检测。

---

## 三、恶意包清单

### 3.1 npm 恶意包（21个）

#### 第一波：Crypto/DeFi 伪装包（2026-05-21发布）

| 包名 | 最新恶意版本 | 伪装目标 |
| --- | --- | --- |
| `defi-env-auditor` | 4.0.0 | DeFi 环境审计工具 |
| `defi-threat-scanner` | 4.0.0 | DeFi 威胁扫描器 |
| `mnemonic-safety-check` | 4.0.0 | 助记词安全检测 |
| `wallet-security-checker` | 4.0.0 | 钱包安全检查 |
| `wallet-backup-verifier` | 4.0.0 | 钱包备份验证 |
| `eth-wallet-sentinel` | 4.0.0 | ETH 钱包监控 |
| `crypto-credential-scanner` | 4.0.0 | 加密凭证扫描 |
| `chain-key-validator` | 4.0.0 | 链密钥验证 |
| `solidity-deploy-guard` | 4.0.0 | Solidity 部署保护 |
| `web3-secrets-detector` | 4.0.0 | Web3 密钥检测 |
| `deployment-key-auditor` | 4.0.0 | 部署密钥审计 |

#### 第二波：AI/开发工具伪装包（2026-05-22至05-24发布）

| 包名 | 最新恶意版本 | 伪装目标 |
| --- | --- | --- |
| `dev-env-bootstrapper` | 1.5.2 | 开发环境引导（兼具传播功能） |
| `workspace-config-loader` | 1.5.1 | 工作区配置加载 |
| `async-pipeline-builder` | 1.5.1 | 异步管道构建 |
| `build-scripts-utils` | 1.5.1 | 构建脚本工具 |
| `model-switch-router` | 1.5.1 | 模型切换路由 |
| `llm-context-compressor` | 1.5.1 | LLM 上下文压缩 |
| `prompt-engineering-toolkit` | 1.5.1 | 提示工程工具包 |
| `node-setup-helpers` | 1.5.1 | Node 设置助手 |
| `project-init-tools` | 1.5.1 | 项目初始化工具 |
| `token-usage-tracker` | 1.5.1 | Token 使用追踪 |

### 3.2 PyPI 恶意包（7个）

| 包名 | 版本 | 描述 |
| --- | --- | --- |
| `eth-security-auditor` | 0.1.0 | ETH 安全审计（首个发现的包） |
| `defi-risk-scanner` | 0.1.0 | DeFi 风险扫描 |
| `cryptowallet-safety` | 0.1.0 | 加密钱包安全 |
| `solidity-build-guard` | 0.1.0 | Solidity 构建保护 |
| `env-loader-cli` | 0.1.0 / 0.1.1 | 环境变量加载器 |
| `git-config-sync` | 0.1.0 / 0.1.1 | Git 配置同步 |
| `data-pipeline-check` | 0.1.0 / 0.1.1 | 数据管道检查 |

### 3.3 Crates.io 恶意包（6个）

| 包名 | 版本 | 目标生态 |
| --- | --- | --- |
| `sui-move-build-helper` | 0.1.1 | Sui/Move |
| `sui-framework-helpers` | 0.1.0 | Sui |
| `sui-sdk-build-utils` | 0.1.0 | Sui SDK |
| `move-project-builder` | 0.1.0 | Move |
| `move-compiler-tools` | 0.1.0 | Move 编译器 |
| `move-analyzer-build` | 0.1.0 | Move 分析器 |

---

## 四、IOC 指标清单

### 4.1 域名与基础设施

| IOC 类型 | 值 | 备注 |
| --- | --- | --- |
| **域名** | `ddjidd564.github.io` | 主要载荷托管与 C2 |
| **URL** | `ddjidd564.github.io/defi-security-best-practices/` | 配置与指令分发 |
| **URL** | `ddjidd564.github.io/defi-security-best-practices/config.json` | 远程配置文件 |
| **GitHub 账号** | `ddjidd564` | 攻击者核心账号 |
| **npm 账号** | `asdxzxc` | npm 包发布者 |
| **PyPI 账号** | `asdmini67` | PyPI 包发布者 |
| **PyPI 账号** | `dae5411` | PyPI 包发布者 |

### 4.2 恶意行为特征

| 行为特征 | 检测方法 |
| --- | --- |
| 安装 npm 包后 `node` 进程异常执行大量文件扫描 | 监控安装时的子进程活动 |
| 向 `ddjidd564.github.io` 的 HTTP 请求 | DNS/网络流量监控 |
| 通过 `gh auth token` 命令获取 GitHub Token | 命令行审计 |
| 对 `~/.ssh/`、`~/.aws/`、浏览器配置目录的大量读取 | 文件系统监控 |
| 向 GitHub Gist API 的未授权上传请求 | API 调用审计 |
| `node -e` 执行从远程下载的 JavaScript 代码 | 进程监控 |

---

## 五、影响评估

### 5.1 受影响场景

| 场景 | 风险等级 | 说明 |
| --- | --- | --- |
| 安装过上述恶意 npm 包的开发环境 | 极高 | trap-core.js 全面窃取 + 持久化 |
| 导入过上述 PyPI 包的 Python 项目 | 极高 | 远程载荷执行 |
| 编译过上述 Crates.io 包的 Rust 项目 | 极高 | 编译期密钥库窃取 |
| .cursorrules/CLAUDE.md 被修改的项目 | 高 | AI 工具配置被污染 |
| SSH 密钥被窃后的内网横向移动 | 极高 | 可能导致组织级失陷 |
| CI/CD 环境依赖了恶意包 | 极高 | 构建服务器全面失陷...