---
title: 命令与控制（C2）的演进：从中心化到链上（On-Chain）
url: https://mp.weixin.qq.com/s/zon5sH5_uERDq6TRSvJm_w
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:28:15.003743
---

# 命令与控制（C2）的演进：从中心化到链上（On-Chain）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3iaS2QChpZWGq6DDucmyHibp1nu4YLD8LPkkmavrpnJgRKh3CcfLCwJEQ/0?wx_fmt=jpeg)

# 命令与控制（C2）的演进：从中心化到链上（On-Chain）

Sukant Kumar

securitainment

![]()

在小说阅读器中沉浸阅读

> C2 如何从中心化服务器迁移到区块链合约：韧性、权衡、真实案例，以及通过 RPC 过滤与链上分析开展实用检测。

## 引言: C2 的必要性

命令与控制 (C2) 基础设施是攻击者的“神经中枢”，让其能够与被入侵主机通信，并对感染资产进行编排与指挥。广义上，C2 指威胁行为者用于与恶意软件保持隐蔽连接的手段：一条用于下发指令、接收回传数据的通道。在实践中，C2 通道会使用多种协议 (IRC、HTTP、DNS 等)，以便与正常流量混杂。C2 的历史本质上是一场持续的军备竞赛：防守方不断发展“接管”与检测能力，进攻方随之持续创新以规避之。

### 定义命令与控制基础设施

Command and control (C2) 指让攻击者能够向恶意软件下发命令并从中接收数据的软件与网络组件。它可以跨越多个阶段 (beacon、loader、payload 等)，并运行在多种通道之上 (中心化服务器、P2P 网络，甚至合法平台)。例如，在传统僵尸网络中，受感染主机会轮询一个已知服务器 (例如某个 IRC 频道或 HTTP 端点) 来获取任务。近年来，C2 已扩展到一些“非常规”通道，例如社交媒体帖子、云 API，以及最新的 **blockchain transactions（链上交易）**。

![C2 架构](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt306eGt70zGfuY3hXSTUqQcyqic1dSnpGXwDtJhvj9ibBlib856xfef3KZQ/640?wx_fmt=png&from=appmsg)

C2 架构

**C2 架构: 关键阶段与操作**

**阶段 1: 初始入侵与植入物部署**

* 攻击者通过钓鱼、漏洞利用或供应链获得访问权限。
* 在受害者系统上部署恶意软件植入物。
* 植入物通过常见通道 (HTTP/S、DNS、TCP/UDP) 与 C2 服务器建立周期性、加密通信。

**阶段 2: 命令获取与执行**

* 受感染系统周期性轮询 C2 获取指令。
* C2 返回加密/编码后的命令。
* 恶意软件在本地解密并执行命令。

**阶段 3: 数据外传与回传**

* 恶意软件按命令收集数据。收集到的数据通常先在本地暂存后再外传。
* 结果加密后通过加密通道传回 C2。
* 攻击者在其控制端接收外传数据。

**阶段 4: 持久化与横向移动**

* 部署持久化机制以维持长期访问。
* 攻击者使用植入物向内部服务器横向移动。

### 演化驱动力: 检测 vs 规避

C2 设计的演化由“检测-规避”的动态对抗所驱动。随着防守方提升发现与破坏 C2 的能力 (例如 sinkhole、防火墙阻断、特征检测等)，攻击者就会通过隐藏或去中心化 C2 通道来对抗。防守方中和一种方法，攻击者便在其基础上迭代出新的规避策略。从可被夺取的 IRC 僵尸网络向 HTTP/HTTPS 通信的迁移、Conficker 通过大规模 Domain Generation Algorithms (DGA) “淹没”黑名单体系、以及 Gameover Zeus 向去中心化 P2P 网络的关键跃迁，都是这种拉锯的典型案例。

到了 2010 年代，进攻方开始将 C2 基础设施迁移到更“抗拆除”的通道上。越来越多恶意软件家族采用 Tor hidden services，以隐藏 C2 服务器真实位置并显著提高破坏难度。与此同时，威胁行为者也把 C2 通信嵌入高信誉云与协作平台之中，例如 Google Drive、Dropbox、GitHub 等，而企业往往不愿轻易整体封禁这些平台。基于区块链的 C2 是这一策略最新、也最具韧性的演进。自 2023 年末以来，威胁行为者开始将恶意代码直接嵌入公共区块链 (如 Ethereum 与 BNB Smart Chain (BSC)) 的 smart contracts 中，实际上把区块链本身改造为一种“防弹”的 C2 服务器。

关于 Smart Contracts

Smart contracts 是存储在区块链上的自执行程序；一旦部署，其代码与状态通常不可变。它们无需中心服务器或第三方权威，即可按既定规则自动执行，从而在去中心化网络中强制执行规则、保存数据并触发预定义动作。

## C2 基础设施的历史演进

### 中心化时代: 基于 IRC 的 C2 (1990s)

![基于 IRC 的 C2](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3yLy6bYWIRqFibcamNVEicytLd6MnIrCnKAqZwIhFyw6E3oxHxpdvkNkA/640?wx_fmt=png&from=appmsg)

基于 IRC 的 C2

第一代僵尸网络主要依赖中心化的广播式架构，Internet Relay Chat (IRC) 是典型通道。诸如 GTBot 与 Sdbot 等恶意软件会指示受感染主机加入指定 IRC 频道，并在其中潜伏等待实时命令。该模型能够把恶意指令隐藏在看似正常的聊天流量中，但存在致命单点故障：一旦识别并接管中心 IRC 服务器，就能立即切断对整个僵尸网络的控制，从而快速实现“整体瘫痪”。

### HTTP/HTTPS 转型 (2000s 初-中期)

![Web C2](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3FZzcVsbx4IWxLVqicz09MRcGAoyH00At6JibRLGIgJZC02kRgXe1QV5g/640?wx_fmt=png&from=appmsg)

Web C2

到 2000 年代中期，进攻方转向 HTTP/HTTPS 协议以提升操作隐蔽性。借助标准端口 (80/443) 与 SSL/TLS 加密，C2 通信可以与正常 Web 流量无缝融合，绕过基础防火墙过滤。Zeus 等恶意软件将该模型规模化落地：通过周期性 HTTP GET/POST 请求访问被入侵的 Web 服务器以获取命令。尽管伪装性更强，但该架构依旧是中心化的；一旦发现并拉黑 C2 域名或 IP 地址，便足以使其失效。

### 混合模型与早期去中心化 (2000s 后期)

2000 年代后期出现了旨在消除中心故障点的架构。Domain Generation Algorithms (DGA) (如 Conficker 蠕虫所使用) 使恶意软件能够以程序化方式每天生成成千上万个域名，从而压垮黑名单机制。

与此同时，诸如 GameOver Zeus 的 P2P 僵尸网络也开始出现：受感染节点彼此转发命令，从而移除任何中心服务器。这迫使防守方必须拆解整个 P2P 网络，而这比简单“下线一台服务器”要复杂得多。

### 现代动态规避技术 (2010s - 2020s 初)

在 2010 年代，C2 基础设施演进到高度动态化。Fast-flux 网络成为主流规避技术：在单一域名背后快速轮换成千上万个不同 IP 地址，以对抗基于 IP 的阻断。随后又发展为 “double-flux” 设计，同时轮换 A 记录与权威 DNS 服务器。与此同时，DGA 变得更复杂、更难预测；再叠加 “bulletproof hosting” 与快速端点轮换，使得进攻方迁移基础设施的速度往往快于防守方更新黑名单的速度。

### 云平台与合法服务滥用 (2015-2023)

进攻方开始从自建基础设施战略性转向滥用 trusted cloud and collaboration services 来承载 C2。这种方式让恶意软件可以“明目张胆地隐身”: 将其流量与对 Discord、Dropbox、Google Drive、Telegram 等平台的合法、被白名单放行的通信混合在一起。

![云端 C2](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt35Y1Ao0qtE2Is78d8d4NRLulrEibiam7Iuoacd8Kjwdbv6zpElnEZvWzw/640?wx_fmt=png&from=appmsg)

云端 C2

威胁行为者偏好这些平台，因为它们提供免费、稳健且易于搭建的基础设施；同时其流量受 TLS 加密保护，难以与合法使用区分；并且网络防守方通常不愿轻易将其整体封禁。

## 区块链革命: 去中心化 C2 基础设施

### 为什么区块链代表 C2 的范式转移

区块链 C2 不再依赖中心化服务器，而是以公共账本上的不可变 smart contract 取而代之。这使基础设施天然具备抗拆除能力，因为不存在可被扣押的单点服务器。该方法利用公共区块链上的交易与合约状态来存储并检索恶意 payload，从而让传统阻断方式更难奏效。

在操作隐蔽性方面，区块链的“假名性”与“只读取数”机制进一步抬高了归因与检测门槛。攻击者可使用匿名钱包降低可追溯性。命令则通过只读的 `eth_call`函数获取：该过程不会在链上留下请求交易记录，也无需费用，更容易与合法查询流量混淆。去中心化、持久化与隐蔽性叠加，构成了对手基础设施的根本性转变。

### 架构与工作流: 将 Smart Contract 作为“防弹” C2 服务器

![区块链 C2 架构](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3jib6XHyBiaSffJt8Zj5XSWk2qScg6naBrOLWajWE93Y1euxulR9JPHSg/640?wx_fmt=png&from=appmsg)

区块链 C2 架构

区块链 C2 的战略优势显而易见，而其真正的力量来自支撑其落地的技术架构。该系统以三类组件的动态组合取代中心服务器：承载命令的恶意 smart contract、由攻击者控制并用于管理合约的钱包、以及提供访问通道的公共 RPC 节点。下表拆解了这套核心基础设施：

| **架构组件** | **角色与对手优势** |
| --- | --- |
| 恶意 Smart Contract | “服务器”逻辑。攻击者在公共链 (Ethereum、BNB Smart Chain) 部署合约，将 payload、配置数据或路由逻辑编码在合约状态中。 |
| 攻击者控制的钱包 (EOA) | “管理控制台”。攻击者使用 Externally Owned Account (EOA) 签名交易以更新 C2 指令。这些钱包用于更新指针或轮换 payload 解密密钥，基础设施管理只需支付极少 gas。 |
| 公共 RPC 节点 | 恶意软件通过标准 JSON-RPC 端点 (由区块链网络或公共服务商托管) 查询合约。例如，在 Infura 或 BSC dataseed 节点上调用 `eth_call`，让恶意软件在不发送任何交易的情况下执行合约的 view 函数。 |

关于 JSON-RPC 端点

JSON-RPC 是进行区块链查询的标准接口。为避免运行全节点的开销，恶意软件会通过公共 RPC Provider (例如 Infura、Alchemy) 的 HTTPS 端点发起调用，从而发送诸如 `eth_call`的请求读取 smart contract。这样既无需同步全链，又能把其流量伪装成普通 Web 请求。

**作战杀伤链 (Operational Kill Chain)**

这些组件与受感染主机之间的交互遵循一条精确的四阶段 kill chain，从而实现持久化并规避传统防御。

![区块链感染链](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3JUz3RKibf1jENgu9Z0BAKGwvzIP4WIibb1ibaQDIZpPExia9enGbA7x0ibg/640?wx_fmt=png&from=appmsg)

区块链感染链

**1. Initial Compromise:**攻击者通过社会工程 (例如 UNC5342 的虚假求职面试) 或入侵合法资产 (例如 UNC5142 的 WordPress 脚本注入) 建立立足点。

**2. Loader Script Execution:**轻量级 JavaScript loader 在受害者机器上执行。其逻辑极少，往往只包含一个 Web3 库与硬编码的 smart contract 地址；唯一目的就是发起到公共区块链 RPC 节点的连接。

**3. On-Chain Payload Retrieval:**loader 对攻击者 smart contract 执行只读 JSON-RPC 查询 (例如 `eth_call`)。该动作直接从区块链状态中取回 payload，不会生成链上交易记录，也无需 gas。诸如 UNC5142 等高级行动还使用了多合约路由系统，以动态解析 payload 位置。

**4. Payload Execution:**取回的数据 (通常是加密的 shellcode 或脚本) 会在内存中解密并执行。最终 payload 建立完整 C2 能力 (例如后门、信息窃取器)，在整个感染过程中从未直接联系中心化命令服务器。

### 近期已披露的区块链 C2 实现

**拆解 UNC5142 的 ClearFake 行动**

UNC5142 行动提供了一个“教科书级”的区块链 C2 工作流示例。UNC5142 是以经济利益为动机的威胁行为者，自 2023 年末以来在相当规模上运用区块链 C2。到 2025 年 6 月，UNC5142 使用 EtherHiding 技术在全球约 14,000 个被入侵的 WordPress 网站上开展投放。

我们对其 smart contract (`0x53fd54f55C93f9BCCA471cD0CcbaBC3Acbd3E4AA`) 的分析勾勒出了这条攻击链。

**1. Initial Compromise & 2. Loader Script Execution**UNC5142 入侵约 14,000 个 WordPress 站点并注入 JavaScript loader。该 loader 在访问者浏览器中执行时，包含第一级 smart contract 的硬编码地址，从而启动链上检索流程。

**3. On-Chain Payload Retrieval**

我们使用 BscScan 导航到 smart contract `0x53fd54f55C93f9BCCA471cD0CcbaBC3Acbd3E4AA`。C2 机制的核心被嵌在合约交易数据中。我们分析了若干笔交易以挖掘恶意 payload:

**Transaction Hash:**`0x47aa558f5710aee657ecdc726c77be1b9492f646dba9773a5fae0ec9d727e8d9`

![BC Transaction](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3jfSYH4AJnvDibsyvmEDfXr7UPibCgQ4atxzJ24XQevEzOWyOV8B2EYmQ/640?wx_fmt=png&from=appmsg)

BC Transaction

这笔交易的 “Input Data” 在以 UTF-8 解码后呈现为混淆的 Base64 字符串。我们使用 CyberChef 对其进行解码。该字符串触发了多阶段 shell 命令，最终输出为托管在如下位置的恶意 shell 脚本: `https[:]//salorttactical[.]top/2/verify[.]sh`

![Cyber Chef Decoder](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3GOV56nBUCq3amgfZvzcwQfbJVeccUpFt6fzDhNNqw6ib2Fq28NozNHw/640?wx_fmt=png&from=appmsg)

Cyber Chef Decoder

对交易 `0xee45352945b58acecfd50b7d802a40eb9c843f30b2b7ce7c627918d959809c6c`的类似分析得到另一个恶意端点: `https[:]//kimbeech[.]cfd/cap/verify[.]sh`

![BC Transaction 2](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3afLMInwE4LubE1IzKVCT6L068as7rib61lO7ia3VAA9dMJrB4Iz2lZHg/640?wx_fmt=png&from=appmsg)

BC Transaction 2

![Cyber Chef Decoder 2](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCN09WX7WNAbTjjHxDSlOlt3AjrVkGykDoeicOJeWYbnRDFqxJWIKJAklyXkHtWgKmHbCu5OPaDxEaw/640?wx_fmt=png&from=appmsg)

Cyber Chef Decoder 2

**关键观察:**URL 只存在于链上，而不在任何被入侵网站中出现。因此，当防守方封禁 salorttactical.top 后，UNC5142 只需发布一笔新的区块链交易替换 URL，即可让所有被入侵站点瞬间自动生效。

**4. 基础设施扩展与 payload 执行**

攻击者在 Cloudflare (AS13335) 上持续使用文件名 `verify[.]sh`，形成了一个可用于威胁狩猎的独特“指纹”。为评估该基础设施规模，我们构造了如下 URLScan.io 查询: `page.asn:AS13335 AND filename:verify.sh`

![URLScan Search Query](h...