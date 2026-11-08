---
title: 给大模型装上固件审计员的骨架：一个 IoT 固件漏洞挖掘 Skill 的设计与实现
url: https://mp.weixin.qq.com/s/RFPFZVHPqTWC9vA_1QG4ww
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:09:31.023724
---

# 给大模型装上固件审计员的骨架：一个 IoT 固件漏洞挖掘 Skill 的设计与实现

# 给大模型装上固件审计员的骨架：一个 IoT 固件漏洞挖掘 Skill 的设计与实现

记忆里的纯真
记忆里的纯真

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 固件漏洞挖掘的瓶颈不在于「模型看不懂汇编」，而在于没有一套可执行、可复核的工作流。

#

# 本文介绍一个开源的 IoT 固件审计 Skill：它把资深审计员的工作骨架——流水线、资源分配、证据标准、质量门禁——编码成协议，再用纯标准库脚本把关键判据做成机器可判的形式。文章重点讲三件事：怎么让「审过了」变成可验证的结论；怎么检测跨请求的高阶污点漏洞（并给出对 IEEE S&P'26 论文 Bridge 的实测复现与一处判据修正）；以及怎么用测试守住文档本身。文末附完整实现与自检数据。

#

**先说清楚这是什么**

它不是又一个「一键挖洞工具」。市面上已经有 FAT、Firmadyne、EMBA、FACT 这类整链工具，它们的价值是**交叉验证基线**；但它们也把分析路径固定死了——遇到非常规固件（UBIFS 而不是 squashfs、MIPS16e、自研 Web 框架）就在某一环卡住，而卡住之前的结论往往看起来依然完整。

这个 Skill 固化的是**三层能力**：

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0ck0l7QfTjv4OxFO4mk2VlP7xcVIRgegWCgD8gFrPXHZqXOL5WRK5Yr9WiaRoYwcAibRjGoK3xcPNYoVTVZ4cX5tpR2q1fh6azw/640?wx_fmt=png&from=appmsg)

工作流是「侦察 → 按判据选路 → 调用能力 → 观察反馈 → 按反馈调整」，而不是「按顺序试工具」。这一点决定了它在异常固件上的表现：**失败时先读反馈定位原因，换实现是最后手段。**

仓库地址：https://github.com/DroidKali/iot-firmware-vuln-hunting（Apache-2.0）

##

**1、裸跑大模型做固件审计，会稳定复现哪些失败**

把固件丢给任意一个强模型，说「帮我找漏洞」，你会看到这几类问题反复出现：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2LaJ454PS6wpbNFKa9lgRIMnslXfaIXgMRh9L8onu4UD4Nw9avKRqh4mxrWOLrPDhtv607CSRfJTX1s69NbLUczwpOJ57bUqQ/640?wx_fmt=png&from=appmsg)

这九条里，真正致命的只有两条：**假装覆盖**和**CVE 当漏洞**。前者让报告失去可信度，后者让厂商直接忽略你的提交。所以 Skill 的设计重心不是「帮模型想得更多」，而是**给结论加约束**。

##

**2、流水线：Phase 0–5，每阶段必须落盘**

```
Phase0  度量与定界   → 00-metrics.json / 00-scope.md
Phase1  提取与侦察   → 01-extract/ / 01-manifest.json
Phase2  分层与分配   → 02-tiering.json / 03-audit-plan.md
Phase2.5 覆盖矩阵   → 25-review-list.md（声明 + 逐项打勾）
Phase3  三层审计     → 10-layer1-sinks.json / 20-candidates.jsonl / 30-findings-verified.md
Phase4  动态验证     → 每条候选的可利用性判定
Phase5  门禁与报告   → 40-coverage.md / report.md
```

关键设计：**中间状态全部写文件，不信任模型记忆**。任何时刻中断都能从产物恢复；多个 Agent 分工时，交接靠文件而不是靠「我上一轮说过」。

Phase 3 的三层结构值得展开，因为它决定了「广度」和「深度」怎么分工：

* **Layer 1（不用 LLM）**

  正则 + 结构级二次过滤（ast-grep）扫全域，输出候选清单。它的产物是**辅助参考，不是唯一入口**——Agent 必须逐文件阅读分配到的代码，否则会系统性漏掉「工具认不出来」的逻辑漏洞。
* **Layer 2（模型主场）**

  每个文件跑三条并行轨道——

+ **Track A · Sink 驱动**

  从危险调用往上追数据来源；
+ **Track B · Control 驱动**

  从入口往下查「该有的安全控制有没有」。认证绕过、OTA 无验签、越权改配置**只能用 Track B 找到**，因为它们不是「某行代码有问题」，而是「某个入口缺了检查」；
+ **Track C · 跨请求驱动**

  见第 5 节，专攻「请求 1 写、请求 2 读」的高阶污点。

* **Layer 3（语义验证）**

  用 LSP / 反编译交叉验证 Source→Sink 可达性；LSP 不可用时退化为 grep + 人工追踪，但**必须在报告里写明降级**。

##

**3、资源分配：给固件估「工作量」，而不是估字节**

固件没有「代码行数」直觉——一个 40 MB 的镜像里可能有 30 MB 是证书、字体和 locale。所以用 **ELF `.text` 段大小**（而不是文件大小）乘 Tier 权重来估算认知负荷：

```
text_units(f) =  ELF ?      section('.text').size / 1024
脚本/文本 ? line_count / 40          # 40 行 ≈ 1KB 代码的认知量
其他 ?      0

weight  = {T1:1.0, T2:0.5, T3:0.1, SKIP:0}
EALB    = Σ weight[tier(f)] * text_units(f)
agents  = max(1, ceil(EALB / budget))                 # budget 默认 800
```

Tier 由 R0–R7 规则引擎判定（先后顺序即优先级）：`doc/`、字体、静态资源 → SKIP；Layer 1 命中 P0/P1 → 动态提升 T1；监听服务、`cgi-bin/*`、协议解析器 → T1；`etc/init.d/*`、`*.sh`、`nvram` 默认值 → T1；`.so`、`.ko`、非监听守护进程 → T2；**未匹配任何规则 → T2（保守兜底，不降级）**。

命令层面就是一行：

```
uv run scripts/fw_triage.py \    --rootfs fw-audit/$TARGET/01-extract \    --tier --budget 800 \    --out  fw-audit/$TARGET/02-tiering.json \    --plan fw-audit/$TARGET/03-audit-plan.md
```

这里有个诚实标注：**EALB 目前是 heuristic**。仓库里带了校准脚本（`ealb_calib.py`：predict / evaluate / fit / check），但状态机是明确的——真实工时样本 ≥20 才进 `experimental`，≥60 且 MAPE ≤0.30 才进 `calibrated`。在此之前，EALB 只用于**排序和切分 Agent**，不能当工期承诺。写这句话比喊「智能估算」有用。

**4、让「审过了」可验证：门禁与三类假阳性**

自动化审计最常见的三类假阳性，都不是模型算错，而是**流程给了错误信号**：

**① 空集通过**
「漏洞详情」整节缺失时，字段校验器遍历 0 个条目，返回「全部完整」——0 条当然都完整。修复方式很土：先判**区块是否存在**，缺整节直接失败。

**② 未执行算通过**
高级检查（入口级覆盖、绕过矩阵、跨请求溯源）只在启用时才进判据表。于是 `exit 0` 变成「所有检查都过了」，而实际上其中几项根本没跑。

修复是把判据改成四态：

```
PASS / FAIL / WARN / SKIPPED
```

`SKIPPED` 的含义是「本次没有执行」，strict 档位下**必需项 SKIPPED 直接判失败**。同时落一份 `gate-config.json`：档位、门禁版本、各项阈值、每项检查状态、**全部输入的 sha256**——换台机器可以复算同一次判定。

**③ 版本命中当漏洞**
`busybox 1.31` 命中几十条 CVE，但这个镜像可能裁掉了相关 applet、可能已 backport 修复、可能漏洞需要编译期未开启的选项。所以 CVE 只能走三态：`cve-hit`（仅版本落在区间）/ `cve-reachable`（定位到受影响函数且可达）/ `cve-exploitable`（动态复现）。门禁会检查：版本命中被写成漏洞断言 → V1 违规；未验证的组件 CVE 被塞进「漏洞统计」表 → V2；同一 CVE 同时出现在「组件风险」和「漏洞详情」→ V4（应移动而非复制）。

七道门禁一览：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K36LUXq2XHxXBqAAP8bB9hQPs52TcjOAaZ2tROtZk24dLicIPUHxW8icv9yicf4sckMnVLPTZlEZBBFFL5ZKABN7P5BFogDC45iaqU/640?wx_fmt=png&from=appmsg)

从 Phase 0 到 Phase 5 的产物都是**纯文本 + JSON**，门禁只读文件不读模型的自述。这是整个设计里我最坚持的一点：**报告的措辞不能成为证据。**

##

**5、深水区：跨请求（高阶）污点**

### 5.1 为什么单请求视角必然漏

以 D-Link DIR882 为例，它的 Web 请求处理是两段式的：边界二进制 `prog.cgi` 收请求、按动作关键字（`SetNetwork`、`SetVLAN`）分发；需要改系统状态时，通过 IPC 控制消息（`notify_rc`）交给 `rc` 进程继续处理。

于是漏洞可以是这样的：

```
请求 1  SetNetwork  → nvram_safe_set("lan0_management_link", <用户可控>)
请求 2  SetVLAN     → notify_rc("start_vlanall") → rc 进程
                    → nvram_safe_get("lan0_management_link") → system(buf)
```

只审请求 2 的人会看到「`lan0_management_link` 来自 nvram，是设备自己的配置，不可控」；只审请求 1 的人会看到「写进去了，但没人拿它执行命令」。**两边都看不出问题，而链是通的。**

这类漏洞的定义可以做到完全可判定——**写它的请求 ≠ 触发读的请求**：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K05NjgqNDGDHg4pryKSic3vAvpyd1cLYIVQshlgDDNYia7olnT6I3ibWa941iah9VCPoBe9haGk0yVMgwf4ianexmicBTQmGg0sy7Wic8/640?wx_fmt=png&from=appmsg)

### 5.2 论文怎么做：三阶段

IEEE S&P 2026 的 Bridge 把这个问题拆成三步（我按其开源 artifact 逐行读过实现）：

* **入口点提取**

  识别 AEH（动作入口处理器）与 IPF（用户输入解析函数）。AEH 有三种落地形态，识别阈值来自代码而非文字——注册回调（同调「常量串 + 函数指针」，与前端动作名匹配 ≥10）、函数指针表（≥20）、嵌套 `strcmp` 链（某基本块**入度 ≥10** 是汇聚点，同一函数某 `strcmp`**调用 ≥10 次**；每个 action 的 handler 边界用 `descendants(分支) ∩ descendants(reverse(汇聚点))` 求可达交集）。IPF 则用三道闸：被调用 ≥100 次、常量实参占比 ≥2/3、返回值反向 DDG ≤100 节点。
* **BDG（二进制依赖图）**

  两段污点分析，跑同一个引擎、只是 source/sink 对调——第一段以 IPF 为源、IPC 写为汇；第二段以 IPC 读为源、危险函数为汇；最后**按 sink 地址反查存储键**，把两段 join 起来。
* **ADG（动作依赖图）**

  跨二进制、跨库追踪 action handler 之间的控制流，把「哪个前端请求触发了 rc 里的读」补上。控制消息的判定用两个约束：生产端**集中性**（多个 handler 写同一接口，阈值 10 加相对阈值）与消费端**控制流**（消息是否影响分支条件）。控制值恢复不了的，扔给欠约束符号执行（单次 600 s 超时，超时即丢弃，不拿部分结果充数）。

统计口径上，Bridge 在 44 个固件上报告 1168 个真阳性，其中 566 个高阶。

### 5.3 我的工程化：把结论做成图

论文的实现依赖 IDA Pro + angr + 40 核，普通审计机跑不动。所以 Skill 里做的是**判据落地**，不是复刻工具链：

* `assets/ipc-functions.json`

  10 类 IPC 机制的读写原语、键参数位置、集中性阈值、sink 分类、AEH 识别模式——把论文的概念变成可查的表；
* `scripts/taint_graph.py`

  两条子命令：

+ `recover`

  从反编译伪代码恢复常量键，只做四条确定性规则（字面量 / 局部常量 / 缓冲区填充 / 拼不出来记 `unknown`），不做概率猜测；
+ `build`

  把写点、读点、触发 action、控制值、sink 组成图，按 C1–C5 校验，产出 `taint-graph.json`；

* 门禁 `--taint-graph`（G7）消费这张图，任一判据不满足即阻断；strict 下报告声称了高阶漏洞却没给图，直接失败（`required SKIPPED`）。

### 5.4 实测复现：数字与一处判据修正

我在一台 4 核 / 15 GB 的 Ubuntu 上把论文 artifact 的镜像真跑了一遍（DIR878\_0day，MIPS32）：

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1Mqkz2lTvIhd437mZzYAicbzembPZyOn3YLzJAJNekj6dzq8tpTNM2hz6GkeAWUOtaFodhEjyfNBVxF0Lib5DSuuoKyslArohsE/640?wx_fmt=png&from=appmsg)

入口点识别结果是 `callback_key` 形态，前端动作名匹配 **128/152**；最终 `vuln_result.txt` 有 **1188 个键**，其中带 `other_get`（读发生在另一个二进制）的 **35 个**。

动机样例的输出与论文给定样例**逐字一致**：

```
'lan0_management_link': {'other_get': {'prog.cgi': {
'SetRouterLanSettings': {'restart_lan': {('rc','430d1c'): {'command_exec':['4312cc']}}},
'SetVLANSettings': {'start_vlanwanall': {('rc','430d1c'): {'command_exec':['4312cc']}}}}},
'set': {'prog.cgi': {'SetNetworkSettings': {'43b57c': None}}}},
```

但跑完我改了自己文档里的一条判据。**`other_get` 不等于高阶。** 同一个结果文件里还有：

```
'SysLogRemote_IPAddress': {'other_get': {'prog.cgi': {
'SetSysLogSettings': {'restart_SystemLog': {('rc','451f00'): {'buffer_overflow':['451fa4'],
'command_exec':['451fc8']}}}}},
'set': {'prog.cgi': {'SetSysLogSettings': {'436450': None}}}},
```

读点同样在 `rc`，同样带 `other_get`，但**写它和触发读的都是 `SetSysLogSettings`**——一个请求既写完又触发读，这是**一阶**。

原因很直接：读点几乎总在 `rc` / `librcm.so`，从来不在边界二进制里。所以「读在别的进程」根本不能当高阶证据。我在原文档里把「读点宿主」当成了 `read.action`，这会**把所有一阶都算成高阶**——一个典型的、靠读论文发现不了、只能靠跑数据发现的错。

修正后的链是五元组：

```
write.action--key--> 存储 --key--> read.trigger_action
                                    └─ via(控制值) → read.binary:addr → sink
```

`read.trigger_action` 来自 ADG（前端），`read.binary:addr` 来自 BDG（进程）。两者都写清楚，一阶和高阶才不会混。

**6、用测试守住文档（而不是靠人复读）**

这一节是我认为最值得在同类项目里抄的做法。

**起因**：文档 Phase 2 的示例命令曾把布尔开关 `--tier` 当成路径参数（`--tier fw-audit/.../01-extract`），而 `--rootfs` 才是路径参数。命令照抄必然报错，但所有单元测试是绿的——因为测试根本不读文档。

**做法**：把文档当成被测对象。自检脚本第 14 组会：

* 抽 `README.md` / `SKILL.md` / `references/` / `assets/` 里所有 ```bash 块中调用 `...