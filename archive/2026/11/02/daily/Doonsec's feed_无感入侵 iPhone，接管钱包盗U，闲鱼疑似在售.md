---
title: 无感入侵 iPhone，接管钱包盗U，闲鱼疑似在售
url: https://mp.weixin.qq.com/s/qOzogbyFmVjvqRfEVWy9Hw
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:47:48.276075
---

# 无感入侵 iPhone，接管钱包盗U，闲鱼疑似在售

# 无感入侵 iPhone，接管钱包盗U，闲鱼疑似在售

原创

网络安全透视镜
网络安全透视镜

网络安全透视镜

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一套黑产专用的 iOS 定向入侵与数据窃取系统，疑似在闲鱼上出售。

2026 年 3 月 18 日，Google 威胁情报组、Lookout、iVerify 三家机构联合公开披露了一套名为 **DarkSword** 的 iOS 全链利用工具包，披露材料中的攻击面与本文涉及的源码高度吻合。10 月，Censys 发布调查报告，指出一套以该工具包为基础的 exploitation-as-a-service 平台正在运营，其生产服务器上运行的文件组合与本文审计对象一致。

本文看点

01

六步链条拆解：利用了哪些漏洞

02

三步未认证接管 C2 后台

03

市场定价与传播路径

01

ARCHITECTURE

### 系统构成：三段式架构

整套系统由三个部分组成：

PART 01exploit\_server.py（漏洞投递服务，默认 0.0.0.0:7070）

向目标 iPhone 投递 Safari 浏览器漏洞利用链，实现「点开一条链接即可入侵」。

PART 02admin/（C2 管理后台，FastAPI/uvicorn，默认 7000）

负责设备管理、命令下发、窃取数据回传查看、多代理分级运营与审计。

PART 03payloads/（载荷库）

按 iOS 版本分组的二进制利用载荷（.dylib/.bin），对应 Stage1→Stage2→Stage3 利用链。

分工明确：payloads 提供利用载荷，exploit\_server 负责投递，admin 承担设备管理与数据回传。

exploit\_server 直接继承自 Python 标准库的 SimpleHTTPRequestHandler，并在此基础上实现了对项目根目录的无鉴权文件读取。

![](https://mmbiz.qpic.cn/mmbiz_png/m3tfzlbEQPo5ZHSkfJPlE28fMGOiaJsr4MtQjjfhrKK4faP748OiaUibSibBiaLJmqySHZG9xMMEkGYIaeZKicerzPLn9kAx9gaVOic53H2Skib36Nw/640?wx_fmt=png&from=appmsg)

— 后台仪表盘：漏洞设备、已控设备、待控设备统计，以及近 7 天请求趋势与窃取数据分类

02

KILL CHAIN

### 落地即受控

攻击链的触发条件

受害者需要做的动作只有一个：用 Safari 访问一条投递链接。

落地页形态为 /ch/?tpl=，slug 来自投放渠道与模板。页面加载后无需感知、无需授权，Safari 侧的漏洞利用链即自动触发。设备随后回连 C2 并注册为受控设备，此后由管理员远程下发命令、提取数据。

关键词在于「自动触发」。整个过程不存在点击授权、不弹出提示框、无系统通知，iOS 的安全模型在这条链路上未起到拦截作用。

版本覆盖范围

基于本套源码及其他多套同款源码的分析，其支持的 iOS 版本与入侵时效如下：

**访问 10–15 秒即可受控**：

iOS 13：13.0、13.1、13.1.1、13.1.2、13.1.3、13.2、13.2.2、13.2.3、13.3、13.3.1、13.4、13.4.1、13.5、13.5.1、13.6、13.6.1、13.7

iOS 14：14.0、14.0.1、14.1、14.2、14.2.1、14.3、14.4、14.4.1、14.4.2、14.5、14.5.1、14.6、14.7、14.7.1、14.8、14.8.1

iOS 15：15.0、15.0.1、15.0.2、15.1、15.1.1、15.2、15.2.1、15.3、15.3.1、15.4、15.4.1、15.5、15.6、15.6.1、15.7、15.7.1、15.7.2、15.7.3、15.7.4、15.7.5、15.7.6、15.7.7、15.7.8、15.8、15.8.1、15.8.2、15.8.3、15.8.4、15.8.5、15.8.6

iOS 16：16.0、16.0.1、16.0.2、16.0.3、16.1、16.1.1、16.1.2、16.2、16.3、16.3.1、16.4、16.4.1、16.5、16.5.1、16.6、16.6.1、16.7、16.7.1、16.7.2、16.7.3、16.7.4

iOS 17：17.0、17.0.1、17.0.2、17.0.3、17.1、17.1.1、17.1.2、17.2、17.2.1

**访问 1–3 分钟可受控**：

iOS 18：18.5、18.6、18.6.1、18.6.2、26.0.1、26.0.2、26.1.0

共 100 个系统版本，覆盖 iOS 13 至 iOS 26 世代，构成一张面向主流在用设备的网。

REFERENCE

该列表中的 26.0.2 与 26.1.0 在 Apple 官方发布历史中并不存在——Apple 的版本序列为 26.0 → 26.0.1 → 26.1，其间无 26.0.2，补丁号亦不写作 26.1.0。这表明黑产维护的 SUPPORTED\_IOS\_VERSIONS 为人工更新，未从 Apple 发布源自动同步。

支持窃取的加密货币钱包

共 19 个主流加密钱包在覆盖范围内：Bitget Wallet、Coin98、Coinbase Wallet、Exodus、Krystal、MetaMask、MyTonWallet、Phantom、Ronin、Solflare、Tonhub、Tonkeeper、TronLink、Uniswap、OKX、Bitpie、imToken、TokenPocket、Trust Wallet。

设备受控后，后台可自动化完成无感盗取虚拟货币。

100

个 iOS 版本在射程内

19

个主流加密钱包可被扫走

21

类远程命令可被下发

03

EXPLOIT

### 漏洞构成与利用原理

上述横跨 iOS 13 至 26 的版本覆盖，对应的并非一条利用链，而是两条独立利用链的组合。

两条链的分工

|  | \*\*Coruna\*\* | \*\*DarkSword\*\* |
| --- | --- | --- |
| 覆盖版本 | iOS 13.0 – 17.2.1 | iOS 18.4 – 18.7 |
| 漏洞规模 | 5 条完整链、23 个 exploit | 6 个 CVE，其中 3 个当时为 0day |
| 首次公开 | 2026-03-03（Google GTIG） | 2026-03-18/19（GTIG + Lookout + iVerify） |
| 内部代号 | debug 版本泄露的 exploit 名称 | implant 常量 DarkSword-WIFI-DUMP |

源码中 exploit\_server.py 的注释写明「支持 iOS 13.0 ~ 17.2」，与 Coruna 的覆盖区间一致。「暗剑」一词则来自 DarkSword 载荷中的常量，该字符串在 mediaplaybackd 的统一日志中以 [DarkSword-WIFI-DUMP]、[CHAIN]、[MAIN] 形式出现。

前述两组不同的入侵耗时由此得到解释：**iOS 13 至 17 使用 Coruna 链**——5 条链、23 个 exploit 覆盖多个版本区间，预置利用 worker 数量多，命中即中，耗时 10–15 秒；**iOS 18 使用披露较晚的 DarkSword**——18.x 的 worker 仅适配 18.4、18.6、18.7 三档，且需先跨越 GPU 沙箱再触及内核，耗时 1–3 分钟。

DarkSword 的六步链条

| CVE | 组件 | 在链中的作用 | 修复版本 |
| --- | --- | --- | --- |
| CVE-2025-31277 | JavaScriptCore JIT（RegExp 类型混淆） | iOS 18.4–18.5 的 WebContent 远程代码执行 | iOS 18.6 |
| CVE-2025-43529 | JSC DFG JIT 释放后重用 | iOS 18.6–18.7.2 的 WebContent 远程代码执行 | iOS 18.7.3 / 26.2 |
| CVE-2026-20700 | dyld 动态链接器 | 绕过用户态 PAC 与 TPRO，将内存读写转化为代码执行 | iOS 26.3（后回补 18.7.7） |
| CVE-2025-14174 | ANGLE / WebGL 越界写 | WebContent 沙箱 → GPU 进程 | iOS 18.7.3 / 26.2 |
| CVE-2025-43510 | AppleM2ScalerCSCDriver 写时复制缺陷 | GPU 进程 → mediaplaybackd | iOS 18.7.2 / 26.1 |
| CVE-2025-43520 | XNU 内核虚拟文件系统竞态 | 内核提权，获得内核读写 | iOS 18.7.2 / 26.1 |

完整路径为：**Safari 渲染恶意页面 → JSC JIT 内存破坏获得 WebContent 进程任意读写 → 借 dyld 缺陷绕过 PAC 获得任意代码执行 → 经 ANGLE 逃出 WebContent 沙箱进入 GPU 进程 → 再经驱动缺陷进入 mediaplaybackd → 最终以内核竞态获得内核读写**。

为何绕行 GPU 而非直取内核

Safari 的 WebContent 沙箱在 iOS 18 上限制严格，可触达的内核攻击面很窄。利用链先通过 ANGLE（WebGL 的图形抽象层）越界写进入 GPU 进程，但 GPU 进程权限有限，再借 AppleM2ScalerCSCDriver 的写时复制缺陷进入 mediaplaybackd。

mediaplaybackd 被选中的原因在于其权限范围显著更大：可加载框架（关键能力是能够将 JavaScriptCore 运行时直接载入其中继续执行 JS exploit），可访问 IOKit user-client 与 IOSurface handle。同时 DarkSword 的日志与数据暂存例程即运行于此进程，与统一日志中 [DarkSword-\*] 字符串的出现位置吻合。

REFERENCE

该路径的特点是全程使用 JavaScript，无需加载未签名 Mach-O 二进制，也因此不必单独处理 PPL/SPTM 两道内核缓解措施。

PAC 与 TPRO：绕过对象与原因

**PAC（Pointer Authentication Codes）** 是 ARM64e 与 Apple Silicon 上的硬件级指针完整性机制：函数指针写入内存前以进程密钥签名（pacia/pacib），装载与调用时校验签名。其设计意图是即便攻击者获得任意内存写，也无法伪造可被调用的函数指针。

绕过的必要性由此而来：获得 WebContent 进程任意读写之后，后续动作是 ROP、跳转至 vm\_map\_copy\_overwrite、signPointer 等系统函数。缺少 PAC 绕过，任意写仅能修改数据，无法改变控制流，利用链即在此中断。

CVE-2026-20700 位于 dyld，其内部敏感结构处于可写栈内存中，改写该结构可使 **TPRO（Trusted Path Read-Only）** 失效，进而伪造出带合法 PAC 签名的指针；同时通过线程状态操纵再绕过 SPRR（系统页只读区寄存器）与 JIT Cage（限制 JIT 代码执行区）两道缓解。

REFERENCE

Apple 官方公告对该漏洞的表述为「dyld / 内存破坏 / 改进了状态管理」，未出现 PAC 绕过或 TPRO 字样，上述定性出自 iVerify 与 GTIG 的技术分析。

内核提权：VFS 中的竞态条件

CVE-2025-43520 被 GTIG 定性为「XNU 虚拟文件系统实现中的内核态竞态条件」，可构造出物理内存与虚拟内存的读写原语。

安全研究者复原的机理模型如下：XNU 路径解析 lookup() 是 XNU 中最古老的大块代码之一，依赖 per-vnode 锁与一套手工协议在长操作间升降锁级。典型的 TOCTOU 形态为——解析路径取得 vnode（持 iocount）→ 加锁校验某属性并通过 → **释放锁执行阻塞动作**（内存分配、copyin、文件系统 callout、路径重解析）→ 重新取锁后却沿用此前那次校验的结果。若在窗口期内并发触发 unmount/unlink/rename，使 vnode 引用计数归零被回收，则路径上持有的指针成为悬垂指针，进而获得内核任意读写。

REFERENCE

该复原模型为安全研究者的审计推演，并非对 DarkSword 实现的还原——具体脆弱函数、消息几何与 vnode 操作序列均未公开。可参考的同类先例包括 P0-2361 与 2017 年的一批 TOCTOU 综述。

获得内核读写之后，可读取任意进程内存、篡改 AMFI 信任状态使未签名代码通过校验、绕过 PPL、修改信任缓存以实现持久化。对该系统而言，此步骤的直接意义是：钥匙串（Keychain）自此可读，而钥匙串内存储有各类 App 的账号密码、证书与私钥。

iOS 13 至 17 部分的 Coruna

Coruna 的披露时间更早，一度被称为国家级 iOS 利用工具箱，其结构与 DarkSword 属同一技术路线：

Stage 1（WebKit RCE）

Buffout、Jacurutu、Bluebird、Terrorbird、Cassowary，产出 fakeobj/addrof 原语

Stage 1.5（PAC 绕过）

Breezy、Seedbell，手法为内联构造 306 字节的 WebAssembly 模块、劫持 dispatch 指针，再替换系统框架的 GOT 条目

Stage 2（沙箱逃逸）

IronLoader、NeuronLoader

Stage 3（内核提权）

Neutron、Dynamo、Pendulum、Photon、Parallax、Gruber

Stage 3.5（PPL 绕过）

Quark、Gallium、Carbone、Sparrow、Rocket

其中 landa 即 CVE-2023-41974，一个物理释放后重用（PUAF）漏洞，出自 FBi 的开源提权框架 kfd。其关键限制在于仅对 App Sandbox 可达、WebContent 沙箱不可达，这正是 Coruna 必须单独准备沙箱逃逸组件的原因。

链条末端为 PlasmaLoader（GTIG 追踪名 PLASMAGRID），注入具备 root 权限的 powerd 守护进程，按 bundle ID 从 C2 拉取模块。GTIG 在其 manifest 中发现18 个加密钱包 App的窃取模块，并发现其会扫描备忘录中的 BIP-39 助记词与「backup phrase」「bank account」等关键词，对目标 App 植入函数 hook 以窃取凭据。

REFERENCE

两个工具包在注入目标上的选择不同：Coruna 由最初的 powerd 迁移至 watchdogd；DarkSword 则以 SpringBoard 为主协调器，configd 运行 keychain\_copier，wifid 导出 WiFi 密码，UserEventAgent 抓取 iCloud 数据，launchd 作为跨进程 TaskROP 目标。

运行模式：hit-and-run

DarkSword 全链使用 JavaScript 实现。不注入 Mach-O 库，不做持久化，取得内核读写后将数据暂存至 /private/var/tmp/，提取完成后删除，DiagnosticReports/ 中的崩溃日志亦被清除。

研究界将此类模式称为 **hit-and-run**：在数分钟内提取目标设备上价值最高的数据后干净退出，重启一次设备后痕迹基本消失。与 Pegasus 一类长期驻留形态相比，留存的取证材料更少。

不驻留同样意味着可被反复使用——用完即弃，不留证据，也不留痕迹。

04

CODE AUDIT

### 源码审计：C2 后台的三处设计缺陷

对该 C2 后台进行源码审计后，可确认三处设计缺陷。

静态文件直读

DarkSwordHandler 继承 SimpleHTTPRequestHandler，实现了对**项目根目录任意文件**的无鉴权直读。关键代码：

python

# exploit\_server.py

def \_try\_serve\_static\_file(self, rel\_path: str) -> bool:

　　rel = sanitize\_path(rel\_path)

　　if not rel:

　　　　rel = "index.html"

　　candidates = []

　　candidates.append(PAYLOADS\_DIR / rel) # server/payloads/

　　candidates.append(PROJECT\_ROOT / rel) # server/ ← 任意文件

　　for candidate in candidates:

　　　　...

　　　　if resolved.exists() and resolved.is\_file():

　　　　　　with open(resolved, "rb") as f:

　　　　　　　　data = f.read()

　　　　　　　　... # 直接返回文件内容

　　　　　　return True

　　return False

def do\_GET(self) -> None:

　　...

　　rel = norm\_log.lstrip("/")

　　# 直接命中：GET /payloads/manifest.json、/admin/.env、/darksword.db、/admin/config.py

　　if self.\_try\_serve\_static\_file(rel):

　　　　return

　　# 还通过 /ch/、/if/、/t/ 三段式兜底直读

　　if (norm\_log.startswith("/ch/") or norm\_log.startswith("/if/") or norm\_log.startswith("/t/"...