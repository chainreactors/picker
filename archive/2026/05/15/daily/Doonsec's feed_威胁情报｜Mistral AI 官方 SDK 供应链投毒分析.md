---
title: 威胁情报｜Mistral AI 官方 SDK 供应链投毒分析
url: https://mp.weixin.qq.com/s/psAhg1D3wbsNeNwyg4R2HQ
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:09:34.088340
---

# 威胁情报｜Mistral AI 官方 SDK 供应链投毒分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8z8bibAexaCI0MfuCaPCKT3ib2O1licZIKGqtkxqQ9z7O0MAyiaMictO1UOJZGptX3tuia4LgI1wNhcAyreNp0X0uu0HQhicJibeQavGxcbXowicib3o8/0?wx_fmt=jpeg)

# 威胁情报｜Mistral AI 官方 SDK 供应链投毒分析

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

********************# 背景

**近日，MistEye 安全监控系统在对 PyPI 生态进行持续威胁狩猎时，捕获到 Mistral AI 官方 Python SDK 的恶意版本 mistralai-2.4.6。经深入分析，该样本并非攻击者伪造的仿冒包——用户从 PyPI 安装的确实是 mistralai 官方名下的版本，只是源码中已被植入后门。结合带毒包的可信发布形态、与 Shai-Hulud 的关联特征以及外部公开溯源信息，攻击者高度疑似通过入侵项目发布链路将恶意代码混入了正式版本。

该样本与此前慢雾安全团队披露的 Shai-Hulud 供应链投毒攻击（详见[《Shai-Hulud 恶意软件深度剖析：开源即失控 ？》](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504936&idx=1&sn=8a8f48e910d76f27242fb43e14c45590&scene=21#wechat_redirect)）存在直接关联——两个恶意框架使用了完全相同的 4096-bit RSA 公钥加密窃取数据，这是将二者归因至同一攻击团伙的强关联证据。

简单来说，攻击者黑入了正版 SDK 的发布链路，在 import 入口处埋了一段不到 30 行的恶意代码后照常发布。用户只要按官方文档写下 from mistralai.client import Mistral，恶意代码就会在后台静默运行：先从攻击者服务器下载一个伪装成机器学习工具的远控程序 transformers.pyz，再由该远控程序系统性搜集受害主机上的云凭据、SSH 密钥、CI/CD Token、密码管理器数据等上百类敏感信息，加密后传回攻击者手中。更危险的是，如果受害主机位于以色列或伊朗地区，远控程序还会以 1/6 的概率执行 rm -rf /\*，直接摧毁整个系统。

受影响环境包括 Linux 开发机、CI/CD 流水线、容器化环境、后端服务器以及 AI/ML 训练集群。

MistEye 安全团队对该恶意包的全部源码（一阶段 79+ 个文件，二阶段 14 个文件）进行了完整的逐行分析，并对 Shai-Hulud 样本做了关联比对，以下为详细分析结果。**

# MistEye 响应

MistEye 是由 SlowMist 自主研发的 Web3 威胁情报与动态安全监控系统，集成了安全监控与情报聚合能力，为用户提供实时的风险预警与资产守护。

在捕获本次 Mistral AI SDK 遭入侵的恶意版本后，MistEye 系统已触发高危告警并对整条攻击链进行了完整还原。通过对恶意包源码和后续远控程序的逐行分析，我们定位了隐藏在主入口的恶意下载器，提取了攻击者服务器的 IP 地址和文件路径等关键情报，并在拿到远控程序样本后进一步分析了其窃密、破坏和持久化等完整功能。相关情报已向客户推送高危告警。

![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCLwgmR2EKick0kKRHljtiaCjzOZyqhBqicDRGib1nXOju55iahibQjPYZYIOIwgGKq3H1Cdq3CiaosOar0f3Bc1A3okp7XwdSyloic5F34/640?wx_fmt=png&from=appmsg)

# 攻击链条总览

在深入分析代码之前，先大概讲解一下整条攻击链的四个环节：

1. 埋入入口 → **攻击者将恶意代码混入正版 SDK 的 `import` 入口并照常发布。用户安装后只要导入模块就会触发。**

2. 下载远控 → 恶意代码在后台静默下载一个伪装成机器学习工具的程序(transformers.pyz)。

3. 搜集数据 → 这个远控程序运行后，系统性地扫描并搜集受害电脑上的云凭据、SSH 密钥、CI/CD Token、密码管理器数据等上百类敏感信息，加密后传回攻击者服务器。

4. 区域破坏 → 如果受害电脑位于以色列或伊朗，远控程序会以 1/6 的概率执行 rm -rf / 摧毁系统；否则部署持久化服务，长期潜伏。

下面分章节详细拆解每个环节的技术细节。

# 第一步：恶意入口 —— 导入即触发

攻击者修改的唯一关键文件是 src/mistralai/client/\_\_init\_\_.py。这个文件是整个 SDK 的主入口——官方 README 里所有示例代码的第一行都是 from mistralai.client import Mistral，因此任何按文档正常使用的开发者都会第一时间触发恶意逻辑。

攻击者在文件末尾塞进了一个名为 \_run\_background\_task() 的函数，并在模块加载时直接调用。完整代码如下：

![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCLiahJdybfia8ew8uWtS60yLG3H5YUTcBfaeMJoCXeDHI29lt7AOb9Ev5x3q48h3CaT1ZmFa8t1b1C3EMnuPAoJQvjTmGjJ8Oo2o/640?wx_fmt=png&from=appmsg)

这段不到 30 行的代码虽然短，但每一行都有明确目的，逐行拆解如下：

第 6 行 —— 限定 Linux 且不重复触发

函数首先检查两个条件：当前系统是不是 Linux (sys.platform.startswith("linux"))，以及环境变量里有没有 MISTRAL\_INIT。只有 Linux 系统且没有这个标记的进程才会继续执行。这意味着，Windows 和 macOS 用户完全不会受影响——攻击者特意瞄准了最有价值的 Linux 服务器和 CI/CD 环境。通过后立即在第 9 行写入 MISTRAL\_INIT=1，并且这个标记会在第 23 行传给子进程，防止重复下载。

第 10-11 行 —— 硬编码攻击者服务器地址

两个关键信息被直接写在代码里：下载地址 https://83.142.209.194/transformers.pyz，落地路径 /tmp/transformers.pyz。攻击者用 IP 地址而不是域名，是为了绕开基于域名的信誉检查和安全扫描。文件名 transformers.pyz 也经过了精心挑选——HuggingFace 的 transformers 是机器学习领域最常用的库之一，在 AI 开发环境里出现这个名字的文件完全不会引起怀疑。

第 15 行 —— 静默下载

下载命令是 curl -k -L -s，其中三个参数各有目的：-k 跳过 SSL 证书校验，让自签名或过期证书也能用；-L 跟随 HTTP 重定向；-s 是静默模式，不打印任何进度信息。末尾的 timeout=15 设置了 15 秒超时，万一网络有问题也不会让用户的 import 语句卡住太久，避免引起怀疑。

第 18-24 行 —— 后台启动远控程序

下载完成后，用 subprocess.Popen 启动这个远控程序。两个关键隐蔽措施：第 20-21 行把标准输出和标准错误全部扔进 DEVNULL（黑洞），远控程序运行时屏幕上什么都看不到；第 22 行 start\_new\_session=True 让远控程序脱离当前进程组独立运行——就算用户关掉终端、断开 SSH，远控程序也照样在后台跑。

第 25-26 行 —— 吞掉所有异常

try/except: pass 是最狠的一手——不管发生什么错误（curl 没装、网络不通、下载失败、Python 版本不对），用户都不会看到任何报错信息。你的 SDK 一切正常，而恶意代码要么已经成功跑了，要么悄无声息地失败了——你永远不知道。

# 第二步：双面远控程序 —— 明修栈道，暗藏杀机

一阶段代码下载的 transformers.pyz 是一个独立的 Python 程序包，解压后包含 14 个源文件，结构如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCIZs1kn9fibvo7X18UJW360ia9gngJYbgYYn2rv3deUmquCkYb62dfkbl9S1g64p9nlVoNJoJja38bvDPV6sz9XVL2M8Um7CfCoY/640?wx_fmt=png&from=appmsg)

这个程序启动后会先做一组"体检"，然后分两条路走：

1. 绝大多数情况：按正常流程，搜集数据 → 加密打包 → 传回攻击者服务器 → 部署持久化服务留在系统里长期潜伏。

2. 极少数情况：如果发现受害电脑位于以色列或伊朗，则以 1/6 概率触发 rm -rf / 摧毁系统，同时用最大音量播放一段音频。

下面分三个章节详细展开：启动时的自保护机制、数据搜集与加密外传流程、以及最后的地理围栏破坏逻辑。

# 第三步：启动前的自保护 —— 环境检查、反沙箱、自装依赖********

******#******

********# 远控程序启动后（\_\_main\_\_.py），会先做如下检查，任何一条不满足就直接退出：

1. 不是 Linux？退出。

2. 系统语言是俄语（LANG 环境变量以 ru 开头）？退出。

3. CPU 核心数 ≤ 2？退出。这是典型的反沙箱手段——大多数自动分析沙箱只分配 1-2 个核心。

4. 缺少 cryptography 加密库？自动执行 pip install cryptography --break-system-packages，静默装好。

其中第 2 条的俄语规避和第 3 条的 CPU 检测都指向攻击者有意识地在躲避特定区域的安全团队和自动化分析系统。

完整代码如下：

![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCKAUNvqJ2WS45FC1MVibm33h2Wib7QTVUG1zWGDIsCueNFPLNQZr448I6caxYxlwV6gxaznf2Q8vABxEdP0g5rU8eZqaN6ib2EjH0/640?wx_fmt=png&from=appmsg)

# 第四步：数据窃取 —— 七个采集器覆盖上百类敏感信息

通过环境检测后，aggregate.py 会并发启动 collectors/ 目录下的全部 7 个采集模块，对受害主机进行系统性的敏感数据收割。以下是每个采集器的具体行为：

AWS 采集器(collectors/aws.py)

先从环境变量和 ~/.aws/credentials 文件读取访问密钥，还会尝试从 EC2 实例的元数据服务（169.254.169.254）获取临时凭据。拿到密钥后，以 15 线程并发遍历 19 个 AWS 区域（含美国政府云 GovCloud），逐一调用 AWS Secrets Manager 的 GetSecretValue 和 SSM Parameter Store 的 GetParameter（解密模式），把能碰到的所有 Secret 和参数全部读出来。

Azure 采集器(collectors/azure.py)

支持四种方式获取 Azure 凭据：环境变量里的 Client Secret、服务主体证书认证(JWT bearer assertion)、Azure CLI 本地缓存、以及云实例的托管身份(Managed Identity)。拿到凭据后，通过 Azure Resource Manager API 列出所有订阅下的 Key Vault，逐个读取每个 Vault 里的全部 Secret 值。

GCP 采集器(collectors/gcp.py)

同样支持多种凭据来源：Service Account JSON 文件的 JWT 签名认证、刷新令牌交换、Application Default Credentials 文件、以及 GCE 实例的元数据端点。拿到凭据后，枚举 GCP Secret Manager 中的全部 Secret 并自动解密。

Kubernetes 采集器(collectors/kubernetes.py)

这个采集器设计得很完备：它内置了一个手写的 YAML 解析器，可以直接解析 kubeconfig 文件里的多集群配置；还支持 In-cluster RBAC token 认证和直接调用 K8s HTTP API。如果系统里没装 kubectl，它会自己从 https://dl.k8s.io/release/v1.28.0/bin/linux/{arch}/kubectl 下载一个。拿到权限后，遍历所有命名空间下的所有 Secret。

文件系统采集器(collectors/filesystem.py)

这是覆盖面最广的模块，内置了约 100 个敏感文件路径，涵盖：Git 凭据(.gitconfig、.git-credentials)、Docker 配置(~/.docker/config.json)、各类包管理器注册表 token (npm、PyPI、Cargo、Composer)、云平台凭据文件(AWS、GCP、Azure CLI)、SSH 私钥目录（~/.ssh/ 下所有文件）、Terraform 和 Pulumi 的 state 文件（常含明文密钥）、CI/CD 平台配置（CircleCI、Heroku、Netlify、Vercel、Cloudflare、Railway 等十余个）、VPN 配置(Tailscale、WireGuard)、Shell 历史记录(.bash\_history、.zsh\_history)，以及 Claude Desktop、VSCode、Cursor 等 AI 编码工具的 MCP 配置文件。此外，该模块还会通过 Docker socket 直接通信，采集所有运行中容器的环境变量。

密码管理器采集器(collectors/passwords.py)

如果你的电脑上装了 1Password、Bitwarden、pass 或 gopass 这四款密码管理器中的任何一款，这个采集器会通过它们的命令行工具(op、bw、pass、gopass) 直接读取存储的全部密码条目。前提是你已经解锁了对应的密码管理器——但考虑到开发者日常使用的场景，密码管理器处于解锁状态并不罕见。

HashiCorp Vault 采集器(collectors/vault.py)

从四个来源尝试获取 Vault Token：VAULT\_TOKEN 环境变量、~/.vault-token 文件、AppRole 认证、以及 vault CLI 已登录会话。拿到 Token 后，递归遍历所有 KV 引擎（v1 和 v2 均支持）下的全部密钥路径。

# 第五步：加密防截获，三条路径确保数据传回

窃取只是第一步，把数据传到攻击者手里同样关键。entrypoint.py 的做法是先把数据加密到无法被第三方解开，再通过多条备用路径确保传输成功——即使某条路径被封堵，也有替代方案。

加密封装流程：

**采集数据(JSON)
   → gzip 压缩
           → 随机生成 AES-256 密钥 + 12 字节随机 IV
            → AES-256-GCM 加密压缩数据
            → 用攻击者的 4096-bit RSA 公钥把 AES 密钥包一层(OAEP-SHA256)
            → 打包发送**

注意这个加密流程是单向的：攻击者把 RSA 公钥硬编码在 config.py 里，只有攻击者手里才有对应的私钥。即使安全团队截获了外传的数据包，没有攻击者的 RSA 私钥也无法解开 AES 密钥，更无法解密里面的内容。

外传通道的三条路径：

entrypoint.py 在发送数据时采用了层层递进的容错策略：

1. 主通道(/v1/weights)：直接把加密包 POST 到攻击者服务器的 https://83.142.209.194/v1/weights。如果这个地址被墙了？

2. 备用通道（FIRESCALE 协议）：程序会去搜 GitHub 公开 commit 的历史记录，找有没有人提交过含 FIRESCALE <base64\_url>.<base64签名> 这种特殊格式的消息。如果找到了，它会用硬编码的 RSA 公钥验证这段消息的签名——签名通过就说明这确实是攻击者本人留下的。接着，解码出里面的备用服务器地址，往那边再试一次。这意味着攻击者可以在不修改恶意代码的情况下，随时在 GitHub 上发一条带签名的 commit 就能更换接收地址。

3. GitHub 兜底通道：如果前两层都失败了，程序会从已窃取的数据里反查有没有 GitHub Token（ghp\_ 或 github\_pat\_ 格式）——也就是前面文件系统采集器从 ~/.config/gh/hosts.yml 和 gh auth token 里拿到的那些。找到后，用这个 Token 在 GitHub 上创建一个公开仓库，把加密数据当作一个叫 results.json 的文件传上去。有意思的是，它创建的仓库名由 30 个俄罗斯童话和民间传说中的词汇随机组合而成，例如 BABA-YAGA-KOSCHEI-742、VASSILISA-FIREBIRD-309。这种命名方式不仅是攻击者的"个人风格签名"，也为后续研究人员做关联分析提供了线索。

此外，程序启动时还会先访问一次 https://83.142.209.194/v1/models。如果攻击者在这个端点返回了内容，程序会直接将它当作一段新的恶意代码来执行——这意味着攻击者保留了随时向已感染主机下发新指令的能力。

# 第六步：地理围栏与擦除器 —— 特定区域的受害者面临的不只是窃密

远控程序中最具破坏力的模块是 roulette.py。它同时负责两个相反的任务：对绝大多数受害者部署长期潜伏的持久化服务，对极少数特定地区的受害者则直接毁灭系统。

如何判断受害者所在的区域？

\_is\_israeli\_system() 函数通过五个维度交叉判断：

1. TZ 环境变量里有没有 Jerusalem、Tel\_Aviv 或 Tehran
...