---
title: 网络安全渗透测试 Agent 推荐
url: https://mp.weixin.qq.com/s/3hYS5KfAEl5bt8yi5YVB6g
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:05:37.984302
---

# 网络安全渗透测试 Agent 推荐

# 网络安全渗透测试 Agent 推荐

原创

智能化态势感知
智能化态势感知

智能化态势感知

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

PENTEST AGENT2026.10

AI 渗透就是跑一遍 nmap？

一个 Agent 打穿 Web 到 APP

的全链路渗透

全链哨兵实测 · 6 个开源方案横评 · 附上手命令

网络安全渗透测试 Agent 推荐

授权合规附命令

如果只是把 nmap 和 sqlmap 包一层大模型

那不叫渗透测试 Agent，那叫扫描器加了个聊天框

2026 年，开源 AI 渗透测试早就不是新鲜事了。从PentestGPT 那篇 USENIX Security 论文算起，这个方向走了两年多，GitHub 上能自托管的方案少说七十个。真正的问题不是“有没有”，而是能不能用在真实交付上。

有个数据值得记住：2025 年 12 月 ARTEMIS 那场实测里，最强的自主 Agent 在8000 台主机的真实网络上赢了 10 个测试者中的 9 个，却输给了最好的那个人类——9 个发现对 13 个。差在哪？不是工具调用能力，是创造性链条串联和业务逻辑理解。

所以这篇不堆 star 数。我把最近在看的六个开源方案摆在一起，重点拆一个把Web、小程序、安卓、iOS 全打通的国产项目——全链哨兵（Full-Chain Sentinel System，下文简称 PCSS）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wAz56BweAib7J0qDklF4JlLEnv1tJdl2QhaRjZy65iaf5J0yexeCjJoLWwwHtlSg93DUgz5otWVqdvHQlEDscV637SUXM5TyDoBetj35u5QOQ/640?wx_fmt=png&from=appmsg)

⚠️ 合规前置：本文涉及的所有工具均为攻击性安全工具，仅限在你已获得书面授权的目标上使用。未经授权对他人系统做渗透测试属于违法行为。PCSS 首次进入控制台必须勾选授权承诺，这不是形式主义。

01

PART

先说结论：六款方案怎么选

VERDICT · 选型速览

先把牌摊开。下面这张表按“你是谁、要干什么”来选，不是按 star 数排名——star 数只说明热度，不说明你能不能交付。

| 项目 | 一句话定位 | 最适合谁 |
| --- | --- | --- |
| 全链哨兵 PCSS | Web+小程序+安卓+iOS 全打通，中文控制台 | 做安全服务的交付团队 |
| Strix | 发现即修复，自动生成补丁开 PR | 把测试嵌进 CI/CD 的研发团队 |
| PentestGPT | 学术血统，公开基准成绩最好的一批 | 学习与二次开发、靶场验证 |
| HexStrike AI | MCP 形态，150+ 工具挂给任意 AI | 已有编码 Agent，想加装工具库 |
| CAI | 框架型，93 位贡献者，研究生态最厚 | Bug Bounty 工业化、论文研究 |
| PentAGI | 四子 Agent 分工，Docker 内自闭环 | 要开箱即用的自主多智能体 |

如果你的工作是“给客户出报告”，只有 PCSS 把证据链做成了产品

其余五个各有胜场，但它们的共同短板是只覆盖 Web 与代码侧。而国内甲乙方的真实工单里，小程序和 APP 占了大头——这正是 PCSS 的切口。

02

PART

全链哨兵到底是什么

WHAT IS IT · 定位与出身

它是知攻善防实验室基于 pi 这个 agent harness 改造出来的授权渗透测试 Agent，带中英文 Web 控制台（默认中文）和容器化作业环境。说白了，底层是一个成熟的编码 Agent 运行时，上层套了一整套渗透测试的方法论、工具链和审计机制。

“渗透测试场景在安全服务工作中，通常分为三种：1.Web 渗透 2.小程序渗透 3.APP 渗透。至此，我们全链路打通，一个平台畅游所有任务……本质上 Web、小程序、APP 都是一样的——前端载体不同，后端测试相同。”

这段话是理解它的钥匙。别人的思路是“做一个更强的 Web 黑客”，它的思路是把前端载体的差异抽象掉，让 Agent 只面对统一的后端攻击面。所以同一个会话里，Web 打完切小程序，小程序打完切 APP，中间不用换工具、不用换上下文。

项目采用以项目为隔离单位的设计，一个项目一个 Kali 容器。作者明确建议开 host 网络模式——否则公网环境没法做监听操作，反弹 shell 之类的动作会全部落空。

✦ 关于出身

它是 pi 的衍生作品（fork），不是上游官方项目，与上游团队无关。上游包名仍保留 @earendil-works/\*，改名单独进行。这意味着上游的安全更新要自己跟。

03

PART

它凭什么不一样：六个硬设计

HARD DESIGN · 能力拆解

下面这六条是我认为真正拉开差距的地方，不是 README 的功能罗列，而是决定“能不能交付”的那部分设计。

TOOL 01

#### 全链路：四种目标一个平台

Web 直接输目标开打；小程序选预设 Agent，用 Tscan 反编译后把源码当附件上传；APP 侧在左侧配好 root 过的安卓真机，对话框点“安卓”按钮才会插入对应的工具与 prompt。iOS 走 SentinelBridge deb 包反连，支持 rootless 与 rootful 越狱，能砸壳和拉 IPA，目前标注测试中。

TOOL 02

#### 三档执行模式：把“要不要放行”做成旋钮

这是我最欣赏的一处设计。默认是审批模式，每条 bash 命令你能先编辑再放行或拒绝；想放手就切自动执行；中间档是 AI 审批——由一个守门小模型逐条判 ALLOW 还是 BLOCK。作者的实操建议是配个 qwen-flash 这类小模型去 Hook 全部 Bash 调用，用小模型监管大模型，成本和可控性兼顾。

⚠️ AI 审批是 fail-open：守门模型判定失败或超时时一律放行。它不是沙箱，也不做数据防泄漏，只能拦六类破坏性操作。别把它当安全边界。

TOOL 03

#### 漏洞中枢：CVSS 必填 + 原始数据包留证

Agent 用 vuln\_submit 提交已验证的漏洞，CVSS 分数是必填项，触发漏洞的原始数据包逐字保存，操作员的复核动作会留下时间线，最后按项目导出 Markdown 报告。这一条直击行业痛点——绝大多数开源方案的产出是“一段聊天记录”，而客户要的是能进合同附件的证据。

TOOL 04

#### 发包重放与界面截图：replayd

一个 Go 写的单二进制服务，控制台会话默认挂载、没有开关。它同时是 MITM 代理、本地 CA、goja 脚本钩子、CDP 无头渲染器和 HTTP 型 MCP 服务器。对应两个工具：replay\_capture 负责改包重放并截图留证，replay\_flows 回查历史流量。写报告时最耗时间的“复现截图”这一步，它自动化了。

TOOL 05

#### 资产测绘与情报：国内三件套 + Tavily

接了 FOFA、360 Quake、奇安信 Hunter，对应 fofa\_search / quake\_search / hunter\_search 三个工具，原始响应落 evidence/asset/。只有“已启用 + 已配密钥 + 验证通过”才挂载。国外方案普遍只认 Shodan，这套组合对国内资产明显更准。情报侧接 Tavily，多 Key 池轮换。

TOOL 06

#### 业务建模 + 插件体系 + 会话即审计

能把目标站点还原成 OpenAPI 3.0 文档，让 Agent 对业务接口有结构化认知，而不是靠猜；Nuclei POC 支持订阅、检索与引用，打 nday 不用现找。插件以 Docker 镜像交付，每个插件就是一个 MCP server，支持 http/sse/stdio 三种传输。所有命令、输出与模型决策都落进 JSONL 会话树，可回溯、可分支、可标注。

04

PART

三十分钟把它跑起来

QUICK START · 安装与启动

前置条件只有一个：装好 Docker。推荐直接下 Releases 里的二进制，不用碰 Node 工具链。Linux 上是这样的：

...bash

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh --mirror Aliyun

tar -xzvf sentinel-web-linux-x64.tar.gz

cd sentinel-web/ && chmod +x sentinel-web && ./sentinel-web

首次访问要设账号密码并勾选授权承诺。启动后日志会打印一个带随机串的入口地址，形如 https://地址:端口/随机串——这串随机路径是用来挡扫描器的，别嫌麻烦把它去掉。默认监听 0.0.0.0，放公网务必配合 TLS 和 gate token。

！踩坑提示 🕳

Windows 用户建议直接放弃本机部署。作者明确说不建议在 Windows 上跑，还得额外装 Win32OpenSSL、把 C:\Program Files\Git\usr\bin\ 加进系统环境变量，否则 HTTPS 访问都不正常。真要用就丢台 Linux 服务器上。另外 zip 包比裸 exe 好——裸 exe 找不到 replayd 会丢掉发包功能，用 SENTINEL\_REPLAYD\_DIR 指过去也行。

想改代码就从源码跑，Node 要求 >= 22.19.0：

bash

npm install --ignore-scripts

npm run build:offline　　# 模型目录已入库，不联网

npm run build:web　　　　# 构建 Web 控制台

npm run start:web

作业容器镜像自己构建：docker build -t sentinel:latest docker/。镜像里内置了 Chromium 和中文字体，就是为了发包截图不出现方块。长期挂着跑用 screen -R sentinel 然后 ctrl+a , d 摘出去。

05

PART

三种目标各自的打法

WORKFLOW · Web / 小程序 / APP

Web

输入框直接开打

→

小程序

Tscan 反编译上传

→

APP

真机反连 + Frida

同一套方法论：侦察 → 枚举 → 漏洞映射 → 验证 → 利用 → 后渗透 → 报告

1

Web：最省事，对话框里输目标就开始。Agent 按方法论推进，需要跑命令时走审批链等你放行。

2

小程序：先选预设的小程序 Agent，本地用 Tscan 反编译拿到源码包，在对话框作为附件上传。Agent 基于源码做白盒分析，比纯黑盒盲打命中率高得多。

3

APP：左侧配好 root 测试机，装自研 DroidBridge APK 主动反连，提供 shell、文件上下行、截屏、logcat、tcpdump 抓包、Frida 动态调试和 APK 静态分析。

✦ 一个容易忽略的细节

不开“安卓”按钮，就不会插入安卓相关的工具与 prompt。这是刻意设计的——工具集越小，模型的注意力越集中，乱调用的概率越低。想批量测的话还有工程模式（指挥官架构），但作者标注测试阶段，别上生产。

06

PART

横向对比

COMPARISON · 诚实的一面

| 项目 | 隔离 | 模型 | 公开验证 |
| --- | --- | --- | --- |
| 全链哨兵 PCSS | Kali 容器，按项目隔离 | 任意 OpenAI 兼容端点 | 暂无公开基准成绩 |
| Strix | 有沙箱 | 可配，本地 Ollama 也行 | PoC 级验证 + 自动修复 |
| PentestGPT | Docker 可选 | 多后端，含本地 | USENIX'24 + XBOW 86.5% |
| HexStrike AI | 可选 Docker | 依赖宿主 MCP 客户端 | 无自身验证门控 |
| CAI | 视配置而定 | 300+ 后端 | 多篇 arXiv 论文 |
| PentAGI | Docker 全隔离 | 多 provider | 活跃迭代 |

07

PART

别踩的坑：四条安全边界真相

BOUNDARY · 用之前必须知道

这四条全部来自项目自己的说明，不是我推测。它们决定了你能把这套东西用到什么程度，跳过这节直接上生产出事的概率不小。

审批链只覆盖三条路径

只有 bash、安卓 shell（droid\_shell）和 iOS shell（ios\_shell）过门。read/edit/write、文件面板、MCP 工具、codemode，以及 Frida、抓包、APK 分析这些直连容器的工具都不经过审批。

stdio 型 MCP 在宿主机直接执行

接第三方 MCP 时看清传输方式。stdio 类型不过 bash 审批，等于在你本机以启动者身份跑代码。社区插件若申请 host 网络或 privileged，要单独确认。

容器不是整体沙箱

控制台与 Agent 进程本身以启动者的用户身份跑在宿主机上，只有命令进容器。容器约束的是命令，不是整体环境。且自动执行模式下没有危险命令黑名单。

AI 审批会 fail-open

守门模型判不动或超时，结果是放行而不是拦截。把它当“减少误操作”的手段，别当“阻止攻击”的闸门。

一句话：把它当成“带审计的强力助手”，不是“可以撒手不管的自动化平台”。生产环境务必配 scope 白名单 + 人工复核高危项。

///

LAST

写在最后：给不同人的一句话建议

SUMMARY · 该不该上车

做安全服务交付、工单里既有 Web 又有小程序和 APP 的团队，现在就值得装一套试。它把“证据留痕 + CVSS 定级 + 报告导出”这条链路做成了产品功能，这是其他几个开源方案普遍缺失的一段——它们停在“发现了什么”，它往前走到了“怎么证明、怎么交付”。

最后提醒一句：这些工具的“自主攻击”能力和失控风险是同一件事的两面。书面授权、scope 白名单、沙箱隔离、人工审批这四样，少一样都别开跑。技术本身不危险，把技术用在不该用的地方才危险。

开源渗透 Agent 的护城河不是模型，是围绕模型建的那一层 harness

项目地址：github.com/zgsfsec/Full-Chain-Sentinel-System。作者知善攻防。文中各方案的 star 数与基准成绩截至 2026 年 10 月，变化很快，装之前自己去仓库看一眼最新状态。

既然看到这里了，如果觉得有用，随手点个赞、在看、转发三连吧。

点赞

喜欢

转发

THANKS FOR READING

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wAz56BweAib6pja6TlWh8CL72mheGVw2a8iarW891tdOcXZzHJ1CgtJcnkom7NfYJzaj7MDUkBHeOEWz4kiaLOjL2jOf0PiccEU3wNoxEvqZ0u0/0?wx_fmt=png)

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