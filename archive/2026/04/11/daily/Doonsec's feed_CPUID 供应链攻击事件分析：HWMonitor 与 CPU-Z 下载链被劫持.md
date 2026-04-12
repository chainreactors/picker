---
title: CPUID 供应链攻击事件分析：HWMonitor 与 CPU-Z 下载链被劫持
url: https://mp.weixin.qq.com/s/MaZOzlh3zVVQEXJiwcouXQ
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:45:33.993330
---

# CPUID 供应链攻击事件分析：HWMonitor 与 CPU-Z 下载链被劫持

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAgL2mALwcK6BuG8j3icibVficUibonyZZ0UJzCw5Q26lXzCFLhY9KoqTiatpqA1MrBvfwvSqJtBEn9Qw5REEicViadRRwhgVIrUNRIBXQ/0?wx_fmt=jpeg)

# CPUID 供应链攻击事件分析：HWMonitor 与 CPU-Z 下载链被劫持

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAia2pLtVh0AllXM38ibbf1DEgop9YwlxHkl9alXiatDRLfoKZutgj2vkc6zAMuNTeoy8P3J5Myn9o7bQKuFKAb45oCkFUVN3agnIU/640?wx_fmt=png&from=appmsg)

## 长话短说

2026 年 4 月 9 日至 10 日，法国软件公司 CPUID 的官方网站 cpuid.com 遭到供应链攻击。攻击者通过入侵 CPUID 后端的一个侧向 API，将 HWMonitor 1.63、CPU-Z 2.19 和 PerfMonitor 2 的官方下载链接重定向到托管在 Cloudflare R2 存储桶上的恶意安装包，持续时间约为 6 小时。

**核心判断**：本次攻击的最终载荷是 STX RAT——一个具备隐藏远程桌面和凭据窃取能力的远程访问木马。攻击者在基础设施层面犯下了严重的操作安全失误：直接复用了 2026 年 3 月针对 FileZilla 用户的同一套 C2 域名和 IP 地址，这一疏漏成为快速溯源的关键突破口。

CPUID 官方签名文件本身未被篡改，但使用 HWMonitor 或 CPU-Z 内置更新功能、或在攻击时间窗口内从官网下载安装包的用户，存在高度感染风险。现有证据充分支持认定这是一次真实的供应链入侵，而非单纯的域名仿冒或广告投毒。

## 背景：CPUID 是谁，为什么值得关注

CPUID 是总部位于法国的软件公司，创始人 Franck Delattre，主要产品线包括 CPU-Z（处理器信息工具）、HWMonitor（硬件温度/电压监控）、HWMonitor PRO 和 PerfMonitor 2。CPU-Z 和 HWMonitor 是 PC 硬件爱好者、超频玩家、系统管理员群体中极为普及的免费工具，累计下载量估算以数千万计。

这一用户画像恰好构成了攻击者的理想目标群体：他们通常对系统有较高权限、习惯于信任「官方网站直链下载」，且因工具本身涉及硬件底层访问，杀软规则对此类程序的行为往往更宽松。

## 事件时间线

| 时间（UTC） | 事件节点 |
| --- | --- |
| 2026-03-xx | 攻击者使用同一套 C2 基础设施（supp0v3.com）发起针对 FileZilla 用户的木马化安装包分发活动（单一信源，待证实具体日期） |
| 2026-04-03 | CPUID 官网更新 HWMonitor 至 1.63 版本（正常发布） |
| 2026-04-09 约 15:00 UTC | 攻击者入侵 CPUID 后端侧向 API，下载链接开始随机指向 Cloudflare R2 上的恶意文件 |
| 2026-04-10 约 10:00 UTC | CPUID 发现并修复入侵，恢复正常下载链接，受影响窗口约 6 小时 |
| 2026-04-10 | Reddit 社区（r/pcmasterrace）出现大量用户报告，描述下载到名为 `HWiNFO_Monitor_Setup.exe` 的异常文件，Windows Defender 立即报警 |
| 2026-04-10 | vx-underground、igor's LAB、Kaspersky Securelist 相继发布技术分析；eSentire TRU 将载荷认定为 STX RAT |
| 2026-04-10 | CPUID 开发者 Samuel Demeulemeester 通过 X（推特）公开承认入侵，发表情况说明 |
| 2026-04-11 | BleepingComputer、The Register、Tom's Hardware 等主流媒体跟进报道 |

## 入侵向量：「侧向 API」是什么

CPUID 官方声明指出，被入侵的是一个「辅助功能组件」，而非主代码库或签名构建系统。目前公开信息不足以精确判断该 API 的具体功能和认证机制。

可以确认的是：CPUID 的下载架构存在一个值得注意的技术分叉——HWMonitor 的安装包（EXE 格式）经由 `download.cpuid.com` 子域名分发，而 ZIP 压缩包则直链至 Cloudflare R2 存储桶。

**研判**：这种双路径分发架构在权限隔离设计上可能存在薄弱点，攻击者利用该 API 将安装包链接重定向至攻击者自控的 Cloudflare R2 存储桶（三个不同的 Bucket ID 被轮换使用，推测是为规避拦截），而直链方式下载 `hwmonitor_1.63.exe` 的用户获取的仍是正常文件。

这一行为特征说明，攻击者并未取得 CPUID 整体服务器的 root 权限，而是对下载链接的生成或重定向逻辑实施了有限度的精确篡改。**待证实**：目前尚不清楚该侧向 API 的具体实现方式、认证方式以及攻击者如何取得访问凭据，CPUID 官方表示调查仍在进行中。

## 恶意载荷技术解剖

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAia9AIOe38vYRraKOQzEMphw8LuW9S6xlUU6FYLnZAWcJ9mbJzVsRibYrSVMXNKQpZ4Rt7eX0X9Fp5HKxxamoJibAgQVFnoXNGpfU/640?wx_fmt=png&from=appmsg)

### 第一阶段：伪装的安装包

用户在攻击时间窗口内从官网下载到的文件名为 `HWiNFO_Monitor_Setup.exe`，而非预期的 `hwmonitor_1.63.exe`。这个命名经过刻意设计：将 CPUID 和 HWiNFO 两个品牌词拼合，利用用户对熟悉名称的认知惯性降低警觉。安装界面为俄语 UI、使用 Inno Setup 封装，与正规 CPUID 安装包有明显差异。

安装包内包含合法的、经正规数字签名的 CPUID 可执行文件，同时捆绑了一个名为 `CRYPTBASE.dll` 的恶意 DLL——这个名字不是随意取的，CRYPTBASE.dll 是 Windows 系统中一个合法的加密支撑库，此命名意在与系统组件混淆。

### 第二阶段：DLL 侧加载与内存驻留

攻击采用 DLL 侧加载（T1574.002）技术：当用户运行签名正常的 HWMonitor 或 CPU-Z 主程序时，恶意 `CRYPTBASE.dll` 被优先加载执行。恶意 DLL 本身使用 Zig 语言编译，这一选择并不常见，推测是为了增加逆向工程难度。

加载器随后通过 PowerShell 从攻击者控制的 C2 服务器拉取后续载荷，执行链几乎完全在内存中进行，最大限度减少磁盘落地痕迹。vx-underground 的分析指出，恶意代码还通过 .NET 程序集代理调用 NTDLL 函数，以规避部分 EDR（端点检测与响应）的系统调用监控。此外，Kaspersky Securelist 披露了一个有趣的技术细节：加载器内嵌了一个巨型 MAC 地址字符串数组，通过将十六进制 MAC 地址字符转换为字节值的方式，隐写（steganography-like）拼装出下一阶段载荷——这是相对少见的混淆手法。

### 第三阶段：STX RAT

最终落地的是 STX RAT（远程访问木马），由 eSentire TRU 于 2026 年 2 月底首次记录，此前曾通过木马化 FileZilla 安装包投递。在 CPUID 事件中，攻击者复用了完全相同的 C2 配置，包括：

* **C2 服务器**：`welcome.supp0v3.com`（回调路径 `/d/callback`）
* **C2 IP**：`95.216.51.236`（归属 Hetzner，位于芬兰赫尔辛基）
* **配置字段**：嵌入 DLL 的 `referrer` 字段值为 `cpz`（CPU-Z 的缩写），说明攻击者针对不同目标维护了不同的配置标识

STX RAT 的通信协议采用自定义 TCP 协议，通过 X25519 椭圆曲线 Diffie-Hellman 协商会话密钥，使用内嵌的 Ed25519 公钥验证 C2 身份，消息体经 ChaCha20-Poly1305 加密——密码学栈设计相对成熟。RAT 同时支持通过 Tor 洋葱网络进行备用 C2 通信，内嵌了自定义 Tor 客户端实现。

**核心能力**如下：

| 能力模块 | 描述 |
| --- | --- |
| HVNC（隐藏虚拟网络计算） | 在受害者屏幕不可见的独立桌面会话中，攻击者可完整交互操控受害机器 |
| 凭据窃取 | 针对 Chrome、Firefox、SeaMonkey 及 Chromium 系浏览器存储的密码和 Cookie；Windows Vault；FileZilla、WinSCP、Cyberduck 的 FTP 凭据；Litecoin-Qt、Electrum 等桌面加密货币钱包 |
| 延迟激活 | 窃取功能不会自动触发，需 C2 明确下达 `getcreds` 命令后才开始窃取，这意味着离线沙箱分析无法观察到完整行为 |
| 内存执行 | 支持 EXE/BIN、反射式 DLL、原始 shellcode 及 PowerShell 脚本的内存执行，通过劫持 PowerShell STDIN 管道实现完全无文件执行 |
| 持久化 | HKCU Run 注册表键（启动混淆的 PowerShell 加载器）；MSBuild 项目滥用（T1127.001）；COM 对象劫持 |
| 截图 | 在凭据外传前先使用 GDI BitBlt 截取桌面 JPEG 图像，为攻击者提供受害环境视觉上下文 |
| 反沙箱 | 对 VirtualBox、VMware、QEMU 等虚拟化环境进行检测，发现后中止执行 |

## 关键情报：攻击者的操作安全失误

这是本次事件中分析价值最高的部分。Kaspersky Securelist 将本次攻击定性为「照搬式攻击（copy-pasted attack）」，并指出攻击者犯下了严重的操作安全错误：

**复用 C2 基础设施**。FileZilla 木马活动（2026 年 3 月）和 CPUID 事件（2026 年 4 月）使用了完全相同的 C2 IP（`95.216.51.236`）和域名（`supp0v3.com`）。这意味着，当社区研究人员分析 CPUID 样本时，通过 C2 IP 的历史记录可以立即将其与 FileZilla 活动关联，直接暴露了攻击者的跨活动身份。Kaspersky 原文评价：「攻击者最严重的错误是复用了相同的感染链……这反而使得水坑攻击一启动就能被快速发现。」

**安装包包含俄语 UI**。恶意安装包的安装界面为俄语，这是一个显著的指纹特征，也是最初引发用户警觉的早期信号之一。

**研判**：这可能说明攻击者的开发环境或工具链的系统区域设置为俄语，而非攻击者有意植入的混淆信号；但这一线索不足以独立支持归因到任何具体个人、组织或国家，需结合更多 TTPs 证据综合判断。

**GitHub 上的公开技术分析**显示，攻击者在 FileZilla 活动中使用了 `version.dll` 实施 DLL 侧加载，而在 CPUID 活动中换用了 `CRYPTBASE.dll`——这是唯一一处可见的变化，C2 地址和载荷本身几乎未做更改。这种程度的 OPSEC 疏漏，与 STX RAT 成熟的密码学设计形成了强烈反差，指向开发能力与部署纪律之间的明显割裂。

## 受影响范围评估

**研判**：受感染用户的规模难以精确估计，但有几个因素可以框定量级：

* 攻击时间窗口约 6 小时，但 CPU-Z 和 HWMonitor 的日下载量是一个未知数。考虑到此类工具在 PC 硬件爱好者、测评媒体、IT 运营人员中的普及程度，6 小时内的累计下载量有可能达到数万级别
* 攻击影响的是经由 CPUID 官网「点击更新按钮」的用户，以及直接从主站下载 EXE 安装包的用户；使用直链下载 ZIP 版的用户未受影响（原始二进制文件完好）
* HWMonitor、CPU-Z 2.19 和 PerfMonitor 2 均被确认受到波及
* ScoopInstaller/Extras 的 GitHub Issue 中记录，此前曾出现过针对 CPU-Z 2.19 的哈希校验失败报告，经复盘可能与本次事件存在时间重叠关系

**待证实**：目前没有公开数据能够支撑对实际感染用户数量的精确判断。

## 横向关联：一个正在扩张的分发模式

从已确认的信息来看，运营 STX RAT 的攻击者在 2026 年初已展示出明确的运营模式——以广泛使用的合法实用工具安装包为载体，通过供应链入侵或仿冒分发网站进行投递：

* **2025 年 11 月**：`helloworld.supp0v3.com` 首次被观测到，推测为 C2 测试阶段
* **2025 年 12 月**：`welcome.supp0v3.com` 首次出现
* **2026 年 2 月下旬**：eSentire TRU 在金融服务客户处首次捕获 STX RAT，初始投递向量为 VBScript 文件
* **2026 年 3 月**：Malwarebytes 报告通过木马化 FileZilla 安装包分发 STX RAT 的活动
* **2026 年 4 月 9–10 日**：CPUID 供应链入侵

**研判**：该攻击者目前表现出「工具链劫持」的系统性偏好，不同于针对企业内网的 APT（高级持续性威胁）组织，这种模式更接近以大规模撒网为目标的机会性攻击者。然而，STX RAT 对 HVNC、延迟凭据激活和 Tor 支持的精心设计，又暗示攻击者对某些高价值目标有二次开发和深度驻留的意图。这两个特征并不矛盾：广泛投递 + 精准筛选激活，是凭据盗取活动中常见的漏斗式运营策略。

## 防御建议

以下建议针对两类受众，请按实际情况评估执行：

**对于 IT 运维和安全团队**

* **立即排查**：检查 2026 年 4 月 9 日 15:00 UTC 至 2026 年 4 月 10 日 10:00 UTC 期间，企业内网中是否有主机发起过对 `download.cpuid.com` 的连接，并检查下载文件的 SHA-256 哈希值是否与 CPUID 官方公布的正版哈希一致（CPUID 已恢复提供正常文件，建议重新下载并比对）
* **网络层封堵**：在防火墙和 DNS 过滤层封锁以下 IOC：

+ IP：`95.216.51.236`（Hetzner，芬兰）
+ 域名：`supp0v3.com` 及其所有子域名（`welcome.supp0v3.com`、`helloworld.supp0v3.com` 等）
+ 历史 C2 IP：`104.21.63.112`、`172.67.145.101`（FileZilla 活动关联 IP）

* **EDR 检测规则**：重点关注 CRYPTBASE.dll 被非系统进程加载的行为；从临时目录启动的 WScript 执行 JScript 文件；PowerShell STDIN 劫持；MSBuild 被用于非构建场景的进程派生
* **凭据轮换**：如判断有主机在时间窗口内下载了受感染安装包且已运行，**建议将该主机视为完全失陷（full compromise）**，立即轮换该机器上存储的所有浏览器密码、FTP 客户端（FileZilla、WinSCP）凭据、加密货币钱包助记词，并审查企业账号的 MFA 启用状态

**对于个人用户**

* 如在 2026 年 4 月 9 日至 10 日期间通过 CPUID 官网更新或下载过 HWMonitor 1.63 或 CPU-Z 2.19，且下载的文件名不是 `hwmonitor_1.63.exe`，应立即停止使用并进行系统全面扫描
* VirusTotal 确认，恶意安装包被至少 32 个安全厂商标记为木马，主流杀软已有对应规则，但考虑到 STX RAT 的反沙箱和延迟激活特性，建议结合内存扫描工具进行排查
* 若已运行过可疑安装包，最稳妥的处置方式是重装系统；STX RAT 具备 4 条独立持久化路径，手动清除风险较高

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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