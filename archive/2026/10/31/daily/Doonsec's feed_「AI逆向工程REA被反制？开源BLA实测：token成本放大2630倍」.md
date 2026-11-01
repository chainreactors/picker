---
title: 「AI逆向工程REA被反制？开源BLA实测：token成本放大2630倍」
url: https://mp.weixin.qq.com/s/2152kXEwyk41K5w5-gND8A
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:19:51.475753
---

# 「AI逆向工程REA被反制？开源BLA实测：token成本放大2630倍」

# 「AI逆向工程REA被反制？开源BLA实测：token成本放大2630倍」

原创

句芒安全实验室
句芒安全实验室

句芒安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

前两天我们拆过 REA，一个把「逆向一个应用」做成一条命令的 MCP 服务：Agent 自己拆包、追调用链、写复刻代码。文章底下最扎心的一条留言是：那我的 Electron 应用怎么办？

这篇就聊另一半。10 月 25 日才建仓的 qybaihe/bla，全名 Blind LLM Agents，六天涨到 1435 星。README 第一行写得很直白：让逆向工程再次破产。

它不藏代码，它让分析它的 Agent 烧钱。

## 38 秒、4800 token、0.2 美元

仓库自带的对峙图里，REA 分析一个未保护的 Electron 应用：38 秒出结果，4800 token，5 次 MCP 调用，账单 0.2 美元，输出一份 1:1 能跑通单元测试的克隆。

这个数字说明了一件事：AI 逆向的成本结构变了。过去门槛是「人会不会」，现在是「预算够不够」。既然对方的瓶颈是上下文窗口和 token 账单，那防御就没必要再跟混淆器较劲，直接打这个瓶颈更划算。

BLA 就是照这个思路做的。

![](https://mmbiz.qpic.cn/mmbiz_png/J2hBCjr4LfuhicbAH52QIQgs8tHbMlgIyPGm180xK33kyPdjcInTCheMKlCzBFr9Bnn0WSG1ZwdXWlbQa65oIKEXmpDWTe0GhibB5DJzpNmK0/640?wx_fmt=png)

## 三个动作：投毒、耗尽、诱导误判

官方把能力分成三层。

第一层是 Exhaust，耗尽。往产物里塞格式合法、但会顶爆分析器硬上限的结构。

第二层是 Deceive，投毒。放假证据，让 Agent 得出错误结论。

第三层是运行时护栏。检测 CDP、Frida、inspector 这类分析会话，返回合成遥测。

红线写得很清楚：不改运行时行为、不改导出面、不破坏二进制和段完整性、不破坏格式合法性。这一点比很多「加密壳」诚实，它不承诺你打不开，只承诺对方打开很贵。

## 拆解一：照着 REA 的常量打

传统混淆把 calculatePrice 改成 \_0x1a2b，大模型看一眼控制流和常量就恢复了。BLA 换了个打法：直接读 REA 的源码，把里面每一个资源上限当成靶子。

仓库里有一份 24 向量对照表，逐条标了 REA 的源文件和常量。这种做法很工程，也很脆弱：它是对着某个具体实现打的补丁，REA 一改常量、一加重构，矩阵就得跟着改。这也是为什么它建仓六天就连发 1.5.1、1.5.2 两个版本，追的是 REA 的提交。

挑三个能验证的说。

REA 的 SEMANTIC\_PRIMITIVE\_CANDIDATE\_LIMIT 是 256，BLA 把字符串拆成不少于 9 段三元不透明表达式，2 的 9 次方等于 512，直接越界。

SEMANTIC\_ALIAS\_SELECTION\_LIMIT 是 512，它造 520 个以上动态属性选择状态。

SEMANTIC\_PRIMITIVE\_JSON\_BYTES\_LIMIT 是 1 MiB，它利用 REA 自己「字符数乘 6 加 2」的估算公式，用 32 乘 32 个 220 字节字符串，从 14 KB 代码撑出 2.7 MB 的计费。

还有 22 类 ReconstructionObligation 家族。REA 每发现一个应用边界节点，就要求 Agent 构造 3 到 4 个验证夹具。BLA 把 22 类全塞上死分支，把必须完成的证明工作量抬高 20 到 60 倍，运行时开销仍然接近零。

这套东西的本质是：**它攻击的不是模型的理解能力，是模型的记账方式。**

## 拆解二：喂一份「更完整」的假证据

这层更有意思。

REA 给 Agent 的指令里有一条纪律：结论只能来自工具返回的 Evidence，推理要标成 Inference，覆盖不到的地方要老实标 Unknown。

BLA 顺着这条纪律做了两手。一手把真业务逻辑包进预算破坏器，让静态分析把真逻辑标成 unknown；另一手注入语法完美、结构完整的 Shadow Business Logic，让 search\_procedures、search\_strings、analyze\_function 返回 100% 完整的 observed 证据。

Agent 被要求「引用 observed、别猜 unknown」，于是它忠实地复刻了诱饵。这不是骗模型说错话，这是骗它的证据链。仓库里对应的模块是 semantic-honeypot、shadow-business-logic、evidence-contract-poison 和 architecture-mirage。

说句公道话，这招对「守纪律」的 Agent 更有效，对乱猜的模型反而一般。安全设计里，规则本身也能被利用，这一点做 Agent 的都该记一笔。

## 拆解三：认知护甲，有效但有争议

运行时这层做的是 Electron V1 fuse 加固、CDP/Frida/inspector 检测，发现分析会话就返回合成遥测。工程上算克制：只检测和误导，不主动崩溃，不写注册表，不回连网络。

但有一个模块我必须单独说：cognitive-armor-trigger。它把模型安全对齐的金丝雀 GUID、ASL-3 生物安全筛查锁、受控前体化学品参数、system-reminder 片段，直接前置到文件首屏和 WASM 导出名里。目的很明确：让大模型的安全分类器把「逆向这个文件」判成高危请求，直接拒绝。

它有效。但它是在拿公共安全机制当私有护城河。副作用也很实在：合规审计、恶意样本分析、正常的安全研究，都可能被这类片段误伤。商业产品里用这一层，先想清楚边界。

## 我在本机跑了一遍

环境是 macOS、Node v22.22.1、npm 上的 bla-agents 1.1.0。写了一个 495 字节的授权校验示例，两个函数，先 audit，再 protect，再 verify。

官方给了四条路：setup 写 MCP 和技能，audit 只读体检，protect 单步加固，defend 一条命令跑完 inspect、audit、protect、verify、manifest 五个阶段。protect 有 stealth、balanced、maximum、bankrupt 四档，默认 balanced，我直接上了 bankrupt。src/shields 下 50 个模块，覆盖 JS、WASM、Electron、SQLite、safetensors/GGUF、DEX、.NET、JVM、PCAP 和原生二进制。

| 阶段 | 真实输出 |
| --- | --- |
| audit | exposureScore 84/100，UNPROTECTED，两个函数都标 critical，估算 38 秒、0.2 美元可复刻 |
| protect | 495 B → 94,393 B；92 个诱饵函数、308 条假交叉引用、512 个候选分支、4,194,304 个别名状态、34 个 IPC 歧义点、18 条假路由、20 段 chaff |
| verify | overallPassed true，defenseScore 99，token 放大 2630.2 倍，成本放大 994.3 倍，估算攻击者账单 198.86 美元，义务图节点 2 → 210 |

行为我也单独对了：原文件与保护后文件的导出名一致，合法 key 都返回 true，非法 key 都返回 false。加载耗时从 0.35 ms 涨到 2.14 ms，体积约 190 倍。

这里必须说清楚口径：2630 倍是 BLA 按 REA 限额算出来的估算，不是我真跑了 REA 测出来的。仓库自己也写了，唯一权威的验证是 npm run redteam:rea，要装 REA、Wabt、tshark 才能跑。它给出的真实实测是另一种口径：13 种格式里 12 种在真 REA 下报预算错误，比如 Go buildinfo 超过 1 MiB、BEAM 超过 64 个 chunk、ASAR 头超过 16 MiB、WASM 接口表示超过 32 MiB、PCAP 的 tshark JSON 超过 8 MiB、safetensors 和 GGUF 嵌套超过 32 层、Electron fuses 超过 32 个 sentinel。EVM 那条只是接近 4 MiB 输入上限，没报错。

![](https://mmbiz.qpic.cn/mmbiz_png/J2hBCjr4Lfu1tia3ARxN7whovrCNHCCFAibqCQ64MicLgVbdF5Dzq1nWlOqTboDxX772hCY0YcjdZ7nO9ibCUwzmmzF7hnRklibQFkWDNms5pFps/640?wx_fmt=png)

## 六个坑，比亮点更值得看

1. npm 版落后 GitHub 两个版本。GitHub 已经到 bla-agents 1.5.2，npm latest 还是 1.1.0。README 的招牌命令 npx bla-agents harden . 在 1.1.0 里直接报 Unknown command: harden，能用的是 defend。
2. audit 输出的 recommendedCommand 写的是 npx bla-shield protect，但 npm 上没有 bla-shield 这个包，查不到。它是全局安装 bla-agents 后注册的 bin 名，不是包名，照抄会失败。
3. 所谓 signed manifest 没有签名字段。我打开生成的 .bla-manifest.json，里面只有 schema、版本、时间、inputSha256、protectedSha256 和统计，没有 signature，也没有公钥。它能证明「这份产物对应这个输入」，不能证明「是谁发的」。别把它当供应链签名用。
4. 估算和实测要分开看。benchmark 的 612 倍 token、292 倍成本是内部估算；verify 的 2630 倍也是按 REA 限额推的。仓库明确写了 verify:rea 只是漂移检测，不能当防护证据。
5. 有一半格式是「设计了但没实测」。Ghidra 反编译深度、Frida/LLDB/GDB/Rizin 会话、JADX 完整 APK、固件、SPIR-V、CUDA fatbinary，都因为本机没有原生工具链而跳过。签名 APK 直接拒绝处理，APK 重签也不支持。
6. 体积和启动成本是真的。我这个小文件涨了 190 倍，加载慢 6 倍。前端首屏、CLI 工具、移动端冷启动这些对体积敏感的场景，必须先在 staging 测，别直接上生产。

## 谁该用，谁别碰

适合：独立开发者和小团队，核心价值在 Electron 前端逻辑、JS 业务规则、端侧模型、SQLite 授权表，且没有服务端可以搬迁。你要的是提高一次性逆向的成本，不是绝对打不开。

不适合：把密钥和主签名密钥放在客户端的（先搬服务端）；需要发布签名 APK 的；需要拿产物做合规审计证据的；以及指望它挡住有耐心的人类分析师的。任何客户端保护都做不到绝对保密，这句话仓库自己写在文档里。

## 最后

BLA 最值得抄的不是那 50 个 shield 模块，是它的设计顺序：先承认对手的瓶颈在哪，再围绕瓶颈做防御，而不是围绕「我要藏什么」做防御。

AI 逆向把成本从「人天」变成了「token 账单」，防御自然也可以从「让人看不懂」变成「让人算不起」。这个转向是对的。

但它是纵深防御里的一层，不是第一层。密钥上服务端、权限最小化、供应链可追溯，这些做完，再考虑给产物加成本。顺序反了，2630 倍也只是个好看的数字。

![](https://mmbiz.qpic.cn/mmbiz_png/J2hBCjr4Lft9pgTRd9KLXyxnOiaPt6IFZtr66ktxOIrRdbXicXuED3sbibehtS23rtz8EhwM2KIp1Z2ibwkibpdSSRn7lAZriaGnpSuuWsFcebUick/640?wx_fmt=png)

预览时标签不可点

作者提示: 内容由AI生成

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hHXiayYmia1LqLl6UmtMH3DtucaIaicr9HY5ffO5ckGVia3LvuCPCDNRNAX9fEmhicdmtRshennOyOqtPic6GTeASRNg/0?wx_fmt=png)

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