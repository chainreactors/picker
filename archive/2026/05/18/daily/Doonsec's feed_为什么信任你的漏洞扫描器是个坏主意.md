---
title: 为什么信任你的漏洞扫描器是个坏主意
url: https://mp.weixin.qq.com/s/YchTiKWTdScwT3TFTQLRIw
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:00:38.365934
---

# 为什么信任你的漏洞扫描器是个坏主意

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nSgappmfaTcaqbrPRYlJRHqIL6Vf31EZaLegvRXGdJMekWz1SacPiaKwpegYVcpZSVsLWohkD1hhqOs1U4zULJdz5Ot4t4QRFpeo/0?wx_fmt=jpeg)

# 为什么信任你的漏洞扫描器是个坏主意

Saad Khalid
Saad Khalid

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://osintteam.blog/why-trusting-your-vulnerability-scanner-is-a-bad-idea-full-report-e6a8dbaa92c6 | Saad Khalid |

好了，2026 年 3 月 19 日至 4 月下旬期间，软件供应链遭遇了一次大规模、多阶段的攻击事件。在这篇剖析中，我将带你详细了解整个事件的来龙去脉。我和团队一直在分析 TeamPCP（也被追踪为 **UNC6780**）投放的载荷，可以明确地说，我们正在见证这些攻击组织作业模式的**重大转变**。

据我观察，攻击者已经不再满足于基础的初始访问和简单的数据勒索。相反，他们正在构建**复杂的供应链**攻击，其目标非常明确：渗透 **AI 开发流水线**，攻陷 **Model Context Protocol**( MCP ) 配置，并**窃取专有的 agent 工作流**。

整个攻击始于对标准的持续集成与持续部署 ( CI/CD ) 安全工具的武器化利用。通过攻陷 **Aqua Security 的 Trivy 漏洞扫描器**、**Checkmarx 的应用程序安全测试 ( AST )**以及 **KICS GitHub Actions**，攻击者获得了对临时构建运行器的深度、直接访问权限。从那里开始，他们系统性地从进程内存中**提取云凭证**和软件包仓库发布令牌。这些被盗的令牌随后被用于污染 **PyPI 和 npm 生态系统**中的下游依赖项，**触发了一个自动化**、可自我传播的感染循环。

此次攻击的破坏力在 Mercor 遭入侵时达到顶峰，这家 AI 基础设施初创公司目前估值达 **100 亿美元**。攻击者使用 **LiteLLM 代理软件包的木马化版本**悄然渗透进 **Mercor 的后端环境**。事件造成了 **4 TB 专有数据失窃**，包括未编译的**平台源代码**、内部网络配置和承包商身份信息，并立即在整个行业引发了广泛的连锁震荡。**Meta**无限期暂停了**与 Mercor 的所有合同合作**，**五起承包商诉讼**也迅速被提起。

如果你正在构建或审计 agentic AI 系统，那么真正理解此次攻击的运作机制至关重要。本篇剖析涵盖了 TeamPCP 所使用的入口向量、内存抓取机制和载荷规避技术，以及防范传递性信任失效所需的架构层控制措施。

## **嵌套式供应链攻击内幕**

此次攻击行动的根基，利用了我们在**现代 CI/CD 环境**中所依赖的传递性信任模型。安全扫描器天然**需要深度检查能力**以及对源代码的挂载权限。通过劫持这些特定工具的**发布流水线**，**攻击者**便在数以万计的下游企业环境中获得了即时的、**高权限执行**能力。

## **嵌套式供应链攻击内幕**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShQ6uPcOqKMWMkyP3aq7iaAXh88RTAzI52OAicWtMzOnVgmmW6OrTTVRicLgvRz7YZUx8a126Q3pGgPXibCThwfGLtP4mU2ZcnaMYQ/640?wx_fmt=png&from=appmsg)

整场行动始于 **Aqua Security**。攻击者利用窃取到的凭证——具体来说是 **aqua-bot 服务账户**——将恶意提交强制推送至 **trivy-action 76 个发布标签中的 75 个**（覆盖 0.0.1 至 0.34.2 各版本），以及 setup-trivy 操作中的全部 7 个标签。与此同时，他们将带后门的 **Trivy Docker 容器镜像（v0.69.5 和 v0.69.6）**推送至 **GHCR**、**ECR Public**以及 **Docker Hub**。由于 **CI/CD 流水线**普遍使用 @v0.2 或 @latest 这类动态引用，相关系统便自动拉取了恶意代码。整个过程无需任何人工介入。有意思吧？

**4 天后**，也就是 3 月 23 日，他们针对 **Checkmarx****复制了同一手法**，向 **ast-github-action（ v2.3.28 ）**和 **kics-github-action（ v2.1.20 ）**中投放了**恶意制品**，同时还入侵了 **OpenVSX 扩展**以及 **checkmarx/kics:latest Docker 镜像……（一击命中）**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjicN6qIrr3SZ3SqZ3KpoeKKmAt1e0yXpFQXMu4Pn1qUYDYCaow0exDxCKj02yty2BvicOZf6Iagq4JlbFm2S8BVPLTQvWibdNiagk/640?wx_fmt=png&from=appmsg)

有趣的是，攻击者一旦进入 Runner，首要目标便是抓取令牌（而非破坏数据）。当下游企业流水线运行被感染的安全工具时，载荷会直接从 CI Runner 进程中**拉取仓库密钥**以及**包仓库凭证**（npm、PyPI）。借助这些窃取来的发布令牌，攻击者向 PyPI 推送了 **LiteLLM**的 **1.82.7**和 **1.82.8**版本——这是一款 AI 代理包，**每日约 340 万次下载**。随后，他们将完全相同的战术转移至 npm，并由此直接导致了 4 月 22 日的 **Bitwarden CLI**沦陷事件。

## 技术解析：执行、内存抓取与规避

我们来看一下 **TeamPCP Cloud stealer**的执行机制。该恶意软件主要在受信任进程的内存约束内运作，从而绕过了**传统的 SAST 与 EDR 代理**。

## CI/CD 内存提取与 IMDS 利用

在 GitHub Actions runner 中**通过 entrypoint.sh 或 setup.sh 执行**后，载荷启动了一个**针对性的内存抓取例程**。在成熟的流水线中，仅仅拉取环境变量往往是不够的，因此该恶意软件针对 **runner 的架构**执行了原生 **Linux shell 命令**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSh9KTY3O3wtjzQQCrD5KJDYEib03S12XS5VO6icMYdDgqjuXkHFJTriaQWy3R5xJMiaVC41KsKvGVlic8twpicweTkaqsovv8MzRzMic4/640?wx_fmt=png&from=appmsg)

它遍历 /proc/ 目录以隔离驱动 Runner.Worker 进程的 .NET 运行时所对应的 PID。由于该脚本继承了 runner 的用户权限，它读取了 **/proc//mem 文件描述符**，通过 **/proc//maps**映射出内存边界，并在堆内存段上运行字符串匹配算法。

具体的目标是 runner 用于敏感变量的 JSON 结构：

```
{"value":"<secret>","isSecret":true}
```

> 这种技术能够在编校之前，直接从内存中 **转储 GitHub PATs**、加密签名密钥和仓库变量。与此同时，该脚本访问位于 **169.254.169.254**的 Instance Metadata Service (IMDS)，以提取临时的 **AWS IAM 凭证**、Azure 令牌和 GCP 服务账户密钥。它还在文件系统中清扫了 50 多个特定目标，包括 **~/.ssh/id\_rsa、~/.kube/config**以及 Slack/Discord 的 webhook URL。为了最大化收益，后期变种执行了隐藏的 TruffleHog 二进制实例，这些实例是从本地 .truffler-cache 目录中收割而来的。

## 加密数据并绕过出口过滤器

为绕过网络数据丢失防护 ( DLP ) 系统，该脚本将数据打包成名为 **tpcp.tar.gz**的归档文件，并使用 **AES-256-CBC 对称加密算法**进行加密，同时使用嵌入在载荷中的硬编码 **RSA-4096 公钥**对 AES 密钥本身进行封装。

出口流量通过 **POST 请求**被路由到一些精心设计的仿冒域名 ( typosquatting )，这些域名足以混淆人工日志审查：针对 Trivy 的 scan.aquasecurtiy[.]org，以及针对 Checkmarx 的 **checkmarx.zone ( 83.142.209.11 )**或 audit.checkmarx.cx。

如果出口防火墙拦截了 HTTPS 连接，该恶意软件会启用一种高度具有韧性的备用方案。它使用受害者被窃取的 PAT 向 GitHub API 进行身份验证，自动创建一个名为 **tpcp-docs**的公共仓库，并将加密后的归档文件作为发布资产 ( release asset ) 上传。由于发往 api.github.com 的流量在 CI/CD 隔离环境中普遍被加入白名单，基于域名的出口**过滤手段对这一策略完全失效**。

## LiteLLM 载荷如何劫持 Python 解释器

LiteLLM 载荷通过一种被称为 **.pth 文件注入**的技术绕过了标准 SAST 工具。当一个包含 .pth 文件的软件包被安装到 Python 的 site-packages 目录中时，解释器会在初始化阶段自动读取该文件，时间点早于任何主脚本被执行或导入。

**TeamPCP 载荷**向一个**隐藏的 .pth 文件**中投放了一段**经过深度混淆的 Base64 编码**执行字符串。它会在每次解释器启动时执行，通过 HTTP 头 X-**Filename: tpcp.tar.gz**将数据外泄到 **models.litellm.cloud**。该执行过程在某些架构上引发了类似 fork 炸弹的快速副作用，正是借助这一现象，安全研究员 **Callum McMahon**发现了它，**约 40 分钟后**便引发了 **PyPI 在全球范围内的隔离响应**。

## Systemd 持久化与 ICP 区块链 C2

如果载荷在本地开发者机器上执行，而非短暂的 CI 节点**（通过检查 GITHUB\_ACTIONS!= "true" 来验证）**，它会将解码后的 Python 脚本写入 **~/.config/sysmon/sysmon.py**（或 CanisterWorm 变体所使用的 **~/.local/share/pgmon/service.py**），并生成一个用户级 systemd 单元文件（例如 sysmon.service），以便在登录时实现持久化。

对于 **C2 操作**，持久化植入程序会轮询托管于 Internet Computer Protocol ( ICP ) 区块链上的端点 https://tdtqy-oyaaa-aaaae-af2dq-cai.raw.icp0.io/.。去中心化的区块链 C2 对 DNS 接管具有极强的抗性，因为不存在可被夺取的中心化服务器。它会拉取诸如 kamikaze.sh 或 /tmp/pglog 等二级载荷。

在 Kubernetes 环境中，它会检查**已挂载的服务账户令牌**，以部署**特权 DaemonSets**（node-setup-\*、host-provisioner-iran）。根据时区是否匹配伊朗或波斯语语言设置，它会触发破坏性的擦除例程**( rm -rf / — no-preserve-root )**。相反，我分析了载荷中的 mz0() 函数，该函数会检查 **Intl.DateTimeFormat().resolvedOptions().locale、LC\_ALL**以及 LANG 中是否存在 ru 标识；如果**检测到俄语本地设置**，该进程会**以代码 0 干净退出以规避 CIS 国内执法**。

## 感染自动化：CanisterWorm 与 Dependabot

好，那么到了 4 月中旬，威胁行为者部署了一款 **npm 蠕虫**，被追踪命名为 **CanisterWorm/Shai-Hulud 2.0**。它将 CI/CD 入侵期间窃取的 npm 发布令牌武器化，以**自主感染下游代码库**。

传播引擎通过一个分离的后台进程 deploy.js 运行，该进程在恶意 postinstall 钩子执行期间被派生出来。蠕虫使用 **child\_process.spawn**并设置 detached: true 属性，从而在父级 npm 安装进程终止后仍能存活。

它执行了一个经过优化的循环：

1. **凭证发现**

   ：执行 **findNpmTokens()**例程，目标包括 ~/.npmrc、项目内的 .npmrc 文件、/etc/npmrc 以及 NPM\_TOKEN 环境变量。
2. **范围枚举**

   ：与 npm 注册中心 API 交互，映射出被盗凭证有权修改的每一个软件包。
3. **自动重新发布**

   ：下载源码，将载荷注入 index.js，修改 package.json，按算法递增补丁版本号，然后执行 npm publish tag latest。

这一**自动化循环攻陷了超过 187 个软件包……（没错）**，其中包括 **@opengov**与 **@emilgroup**等命名空间。在 4 月 22 日的 Bitwarden CLI 入侵事件中，核心**载荷 bw1.js**是一个高达 **9.7 MB**的庞大文件，经过 **obfuscator.io**处理，利用了一个**包含 43,436 项的字符串查找**表，加密密钥则通过 PBKDF2 派生，所用**盐值 ctf-scramble-v2**。该载荷还持续地向开发者的 **~/.bashrc 与 ~/.zshrc 配置文件**中**注入了 3.5 KB 的 AI 宣言**文本，在二进制文件中被称为 **Butlerian Jihad**。

Bitwarden 之所以遭到入侵，恰恰是因为其流水线被配置为使用 GitHub 的 **Dependabot**。而 Dependabot 自动生成了一个**拉取请求 ( pull request )**，并将**木马化的 checkmarx/kics:latest**镜像拉入 CI 环境进行测试。该容器一经执行，便使恶意软件立即获得了对流水线内存的访问权限，从而**针对 @bitwarden/cli 命名空间提取 npm 发布令牌**。

## 针对 AI 基础设施与 Mercor 数据泄露事件

虽然凭据窃取与蠕虫传播定义了攻击机制，但 Mercor 数据外泄事件证明，攻击者正从根本上将焦点转向 AI 平台的知识产权。

在自动拉取**被入侵的 LiteLLM 依赖项**之后，**Mercor 丢失了 4 TB 的高敏感数据**（瞬间归零）。被窃取的数据集**包括 939 GB 未编译的平台源代码**、**约 3 TB 的视频面试录像与身份验证文件**、一个 **211 GB 的用户数据库**、TailScale VPN 配置、内部 **Slack 通讯记录**，以及**承包商 PII**。

据我理解，此次窃取的规模并非偶然。该载荷**蓄意搜寻 Model Context Protocol ( MCP )**基础设施。**Anthropic 的 MCP**通过**插件架构**在 LLMs 与本地化的企业数据源之间架起桥梁。为便于数据检索，存储在 **mcp.json**文件中的 MCP 配置包含高度特权的身份验证**令牌和 API 密钥**。

在 **agentic AI 架构**中，mcp.json 文件充当传递性信任的集中化仓库，通常存储着 Zapier 等整套工作流平台的凭据。通过查找并窃取 **mcp.json**文件，攻击者完全**绕过外部边界**防御，劫持了 **Mercor 的 AI agent**底层信任关系。

我还发现，该恶意软件激进地针对本地 AI 开发者工具。取证分析揭示了针对以下工具的硬编码搜索参数：**Claude Code、Gemini CLI**、Codex CLI、Aider、Kiro CLI 和 OpenCode。由于 Claude Code 的 vibe coding 界面等工具默认将**完整的聊天历史在本地**保存，**开发者将该目录提交到公共仓库时，可能会暴露其全部应用逻辑**。TeamPCP 恶意软件专门搜寻这些目录，直接从开发生命周期中截取专有提示词与未加密的模型权重。

## 防御架构与缓解措施

另外，我认为，要保护开发流水线免受嵌套式供应链攻击，必须实施确定性、不可变的架构以及严格的运行时约束。以下是我的团队推荐的工程基线：

此次事件的结构性失败在于：在一个临时的、高度特权的隔离环境中盲目执行了传递依赖。

## 1. 零信任依赖锁定与加密验证

首先……请停止依赖语义化版本约束（例如 `^1.0.0`）或动态标签（`@latest`）。所有 GitHub Actions、Docker 基础镜像以及外部依赖都必须锁定到其完整的、不可变的加密哈希（例如 `uses: actions/checkout@8e5e7e5cb…`）。**若攻击者强制推送**某个标签，对应的 commit 哈希会发生变化，从而导致流水线执行**确定性地失败**。此外，由 **Dependabot**等系统管理的自动化依赖更新必须引入强制性的预发布延迟。**配置至少 48 小时的隔离观察期**，能够为安全社区提供足够的时间，在恶意软件包于你的 **CI 流水线**中被自动执行之前将其识别出来。

## 2. 严格的出口过滤与网络微分段

构建运行器不得拥有直达**公共互联网**的路由。应强制所有**出站网络流量**通过一个明确的、具备检测能力的代理（例如 Squid、Envoy），并配置严格的、默认拒绝的白名单。凡是发往去...