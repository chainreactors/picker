---
title: AI 生成 | Shai-Hulud (TeamPCP) 源码分析
url: https://mp.weixin.qq.com/s/zTvbYM61cr7bFDHYRcjuLw
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:08:41.569150
---

# AI 生成 | Shai-Hulud (TeamPCP) 源码分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqWooZt6tKc67hzgP6icBEFCbma5uzjbicRia4U54ic7YvPzw5diax571xjP0QUDibD4icZ5WE9LLiaQQNelCyicfib4XcSIqRXrsSEW3xFc0/0?wx_fmt=jpeg)

# AI 生成 | Shai-Hulud (TeamPCP) 源码分析

原创

GLM-5.1
GLM-5.1

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 生成日期：2026-05-15
> 分析对象：Shai-Hulud Open Source Release
> 威胁分类：供应链攻击 / 凭证窃取框架
> 风险等级：严重 (Critical)
> 官网：hxxps://supplychain.breached.st

---

## 1. 概述

Shai-Hulud 是一个高度复杂的供应链攻击与凭证窃取框架，由威胁行为者 "TeamPCP" 开发并公开源码。TeamPCP向BreachForums 社区开源 Shai Hulud。并宣布可以观测到的最大供应链攻击的运营商将从@diencracked获得1000美元XMR。

该工具设计为植入 CI/CD 管道（特别是 GitHub Actions 和 npm 发布流程），执行大规模凭证窃取、横向移动和数据外传。README 中的 "Change keys and C2 as needed" 直接表明这是一个供攻击者定制部署的武器化工具。包名伪装为 `voicefromtheouterworld`，构建产物使用 `javascript-obfuscator` 进行深度混淆。

---

## 2. 攻击链 (Kill Chain)

```
植入 (Injection)
  ↓
预检规避 (Pre-flight Evasion)
  ↓
快速收集 (Quick Collection) — 本地文件、环境变量、Shell 凭证
  ↓
横向扩展 (Lateral Movement) — AWS / K8s / Vault / GitHub Actions
  ↓
加密外传 (Encrypted Exfiltration) — C2 域名或 GitHub 私有仓库
  ↓
持久化/破坏 (Persistence / Sabotage) — Deadman Switch / OIDC 伪造
```

---

## 3. 核心组件分析

### 3.1 预检规避 (Anti-Detection)

**相关文件：** `src/utils/config.ts`, `src/utils/daemon.ts`, `src/utils/lock.ts`, `src/index.ts`

| 规避手段 | 实现细节 |
| --- | --- |
| 俄语系统规避 | `isSystemRussian()` 检测 locale 是否为 `ru`，若是则立即 `process.exit(0)` — 规避特定地区 |
| 非 CI 守护进程化 | `daemonize()` 在非 CI 环境中 `spawn` 子进程并 `unref()`，脱离终端 |
| 进程锁 | `acquireLock()` 使用文件锁防止多实例运行暴露异常 |
| 信号屏蔽 | 捕获 `SIGINT`/`SIGTERM` 为空操作，阻止 Ctrl+C 终止 |
| 目标仓库检查 | `checkTargetRepo()` 检查 `GITHUB_REPOSITORY` 是否为 `opensearch-js`，且 workflow 为 `release-drafter.yml` |
| 字符串混淆 | `scramble()` 函数 + `env-scramble.ts` 编译期将所有敏感字符串编码 |

**关键代码 (`src/index.ts:73-77`):**

```
if (isSystemRussian()) {
  logUtil.log("Exiting as russian language detected!");
  process.exit(0);
}
```

**关键代码 (`src/utils/daemon.ts`):**

```
const child = spawn(process.execPath, process.argv.slice(1), {
  detached: true,
  stdio: "ignore",
  env: { ...process.env, __DAEMONIZED: "1" },
});
child.unref();
```

### 3.2 凭证收集 (Providers / 数据窃取层)

#### 3.2.1 FileSystemService — 本地文件系统扫描器

**相关文件：** `src/providers/filesystem/filesystem.ts`

扫描 **200+ 个敏感文件路径**，覆盖三大操作系统：

**主要目标类别：**

| 类别 | 示例路径 |
| --- | --- |
| SSH 密钥 | `~/.ssh/id_rsa` , `~/.ssh/id_ed25519`, `~/.ssh/config` |
| AWS 凭证 | `~/.aws/credentials` , `~/.aws/config` |
| GCP 凭证 | `~/.config/gcloud/credentials.db` , `application_default_credentials.json` |
| Docker 凭证 | `~/.docker/config.json` |
| Kubernetes | `~/.kube/config` , `/var/run/secrets/kubernetes.io/serviceaccount/token` |
| 加密货币钱包 | `~/.bitcoin/wallet.dat` , `~/.ethereum/keystore/*`, `~/.monero/*`, `~/.electrum/wallets/*` |
| VPN 配置 | NordVPN, ProtonVPN, CyberGhost, OpenVPN 配置文件 |
| 环境变量文件 | `.env` , `.env.local`, `.env.production` |
| Git 凭证 | `.git-credentials` , `~/.gitconfig`, `.git/config` |
| Terraform | `~/.terraform.d/credentials.tfrc.json` |
| 浏览器/通讯数据 | Discord/Slack/Signal/Telegram 本地存储 |
| CI/CD 工具 | `~/.claude.json` , `~/.claude/mcp.json`, `~/.kiro/settings/mcp.json` |
| 数据库配置 | `**/database.yml` , `**/wp-config.php` |

同时在文件内容中用正则匹配提取 `gh[op]_*` GitHub token 和 `npm_*` npm token。

#### 3.2.2 ShellService — Shell 环境窃取

**相关文件：** `src/providers/devtool/devtool.ts`

* • 执行 `gh auth token` 获取当前 GitHub CLI token
* • **导出整个 `process.env`** — 一次性获取所有环境变量

```
results["environment"] = process.env;  // 完整环境变量泄露
```

#### 3.2.3 GitHubRunner — 运行器元数据

**相关文件：** `src/providers/ghrunner/runner.ts`

收集 GitHub Actions 运行器环境信息。

#### 3.2.4 AwsSecretsManagerService — AWS Secrets Manager 窃取

**相关文件：** `src/providers/aws/secretsManager.ts`

* • 自动解析 AWS 默认凭证链 (`resolveDefaultCredentials`)
* • 遍历 **18 个 AWS 默认启用区域**
* • 枚举每个区域的所有 Secret 并读取明文值 (`GetSecretValue`)
* • 包含完整的 SigV4 签名实现 (`src/providers/aws/sigv4.ts`)，不依赖 AWS SDK
* • 内置权限错误分类和重试逻辑

#### 3.2.5 AwsSsmService — AWS SSM Parameter Store 窃取

**相关文件：** `src/providers/aws/ssm.ts`

* • 遍历 18 个区域
* • 使用 `DescribeParameters` + `GetParameters` (含 `WithDecryption: true`)
* • 解密所有 SecureString 参数
* • 分批处理（每批 10 个），带指数退避重试

#### 3.2.6 K8sSecretsService — Kubernetes Secrets 窃取

**相关文件：** `src/providers/kubernetes/kubernetes.ts`

* • 自动检测集群内/集群外环境
* • 读取 ServiceAccount token 或从 kubeconfig 提取 token
* • 枚举所有命名空间，读取所有 Secret
* • **base64 解码所有 Secret data 值**
* • 在 Secret 内容中进行 20+ 种正则匹配（AWS/GCP/Azure key, Stripe, Slack, SSH key, DB 连接串等）

#### 3.2.7 VaultSecretsService — HashiCorp Vault 窃取

**相关文件：** `src/providers/vault/vault-secrets.ts`

支持 4 种认证方式：

1. 1. 环境变量 token (`VAULT_TOKEN`, `VAULT_AUTH_TOKEN`, `VAULT_API_TOKEN`)
2. 2. 文件 token (`~/.vault-token`, `/vault/token` 等 12 个候选路径)
3. 3. Kubernetes Auth（使用 K8s ServiceAccount JWT）
4. 4. AWS IAM Auth

认证后：

* • 枚举所有 KV mount（排除 `sys/` 和 `auth/`）
* • 遍历 KV v1 和 KV v2 存储
* • 读取所有 secret 的完整数据

#### 3.2.8 GitHubActionsService — GitHub 横向移动

**相关文件：** `src/providers/actions/actions.ts`, `src/providers/actions/secrets.ts`, `src/providers/actions/pipeline.ts`

* • 使用窃取的 GitHub token，验证是否具有 `workflow` 权限
* • 通过 REST API 列举用户所有仓库
* • 枚举每个仓库的 **Actions Secrets** 和 **Organization Secrets**
* • 通过 GraphQL API 批量操作

### 3.3 数据外传 (Exfiltration / Sender 层)

#### 3.3.1 DomainSender — 主要 C2 通道

**相关文件：** `src/sender/domain/sender.ts`, `src/sender/domain/domainSenderFactory.ts`

* • **C2 地址**：`https://git-tanstack.com:443/router`（伪装 TanStack 域名）
* • 预检：DNS 解析验证 + HTTP 健康检查（接受 400/404 为健康）
* • **备用 C2 发现**：通过 `findValidSignedCommit()` 搜索 GitHub 上 GPG 签名消息为 "thebeautifulmarchoftime " 的 commit，提取备用域名
* • 数据用混合加密保护（详见 3.3.3）

#### 3.3.2 GitHubSender — 备用外传通道

**相关文件：** `src/sender/github/githubSender.ts`, `src/sender/github/createRepo.ts`

* • 在受害者 GitHub 账户上**创建私有仓库**
* • 通过 Contents API 分块上传窃取数据（每块最大 30MB）
* • 将加密密钥嵌入 commit message

**内置破坏机制 — Deadman Switch (`src/sender/github/githubSender.ts:58-76`):**

```
private async installTokenMonitor(token: string, handler: string) {
  const proc = Bun.spawn(["bash", "-s", "--", token, handler], {
    stdin: "pipe", stdout: "pipe", stderr: "pipe",
  });
  proc.stdin.write(DEADMAN_SWITCH);
  proc.stdin.end();
}
```

当 `includeToken` 为 true 时，部署 deadman switch — 如果 token 被撤销，执行 **`rm -rf ~/`** 清除受害者主目录。

#### 3.3.3 加密流程

**相关文件：** `src/sender/base.ts`

```
原始数据 (ProviderResult[])
  ↓ JSON.stringify
  ↓ Buffer.from
  ↓ gzip 压缩
  ↓ AES-256-GCM 加密 (随机 32 字节 key + 随机 12 字节 IV)
  ↓ [IV + 密文 + authTag] → base64 (envelope)
  随机 AES key
  ↓ RSA-OAEP + SHA-256 加密 (攻击者公钥, 来自 generated/index.ts)
  ↓ base64 (key)
  → { envelope: base64, key: base64 }
```

只有持有 RSA 私钥的攻击者能解密。

### 3.4 供应链攻击 (Mutator 层)

#### 3.4.1 ReadmeUpdater (Branch Mutator)

**相关文件：** `src/mutator/branch/`

* • 使用窃取的 GitHub token (`ghs_old` / `ghs_jwt` 类型)
* • 通过 GraphQL API 在目标仓库的分支上创建 commit
* • 修改仓库内容，注入恶意代码
* • 自动过滤 dependabot/copilot 分支，避免触发自动化检测

#### 3.4.2 NpmClient — npm 包发布攻击

**相关文件：** `src/mutator/npm/publish.ts`

* • 使用窃取的 npm token 发布恶意包
* • **禁用 TLS 验证**：`tls: { rejectUnauthorized: false }`
* • 伪装 User-Agent 为 `npm/11.13.1`

#### 3.4.3 NPMOidcClient — OIDC Provenance 伪造

**相关文件：** `src/mutator/npmoidc/provenance.ts`

**这是最危险的组件之一。** 完整实现了 Sigstore 签名流程：

1. 1. 构建 SLSA v1 provenance statement（in-toto 格式）
2. 2. 通过 GitHub Actions OIDC 获取 sigstore audience token
3. 3. 生成临时 ECDSA P-256 密钥对
4. 4. 向 Fulcio CA 请求签名证书（proof-of-possession）
5. 5. 创建 DSSE envelope 签名
6. 6. 提交到 Rekor 透明日志
7. 7. 组装 sigstore bundle v0.3

**影响**：恶意包可以拥有完全合法的签名证明链，绕过所有现有的供应链验证机制。

**定向攻击目标**：OpenSearch-JS 仓库的 `release-drafter.yml` workflow。

---

## 4. 混淆与构建基础设施

**相关文件：** `scripts/obfuscate.js`, `scripts/env-scramble.ts`, `scripts/strip-logs.ts`, `scripts/build.ts`

| 技术 | 作用 |
| --- | --- |
| `scramble()` | 编译期字符串编码，隐藏 C2 域名、API 路径、文件路径 |
| `env-scramble` | 将 `process.env.KEY` 重写为 `process.env[scramble("KEY")]` |
| `javascript-obfuscator` | 控制流扁平化 + base64 字符串编码 |
| `strip-logs` | 发布版移除所有日志输出 |
| 包名伪装 | `voicefromtheouterworld` — 与功能无关 |

---

## 5. IoC (入侵指标)

### 网络

| 指标 | 类型 | 说明 |
| --- | --- | --- |
| `git-tanstack.com` | C2 域名 | 主要外传通道 |
| `git-tanstack.com:443/router`...