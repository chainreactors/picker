---
title: 第163篇：借助AI + Claude + Skills 构建 APK 自动化安全分析工作流
url: https://mp.weixin.qq.com/s/LzfQOtNIxvh4-4WTxKCaHg
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:54:04.854529
---

# 第163篇：借助AI + Claude + Skills 构建 APK 自动化安全分析工作流

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2bRblN4F5FagiaHg1JXRdT1NafGIxRcnasOs5XoFugpiczHiaRKnq9V9FQyxAxHIA87wibLhFPJHJl7miaiccgwKRKNFn0NEib4jKOG0w/0?wx_fmt=jpeg)

# 第163篇：借助AI + Claude + Skills 构建 APK 自动化安全分析工作流

原创

abc123info
abc123info

希潭实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcCCMJ6Af2WYicgMPA32IwibF8mI2ibC9h8jaHkhxnZzZuqctMLRTxDudicA/640?wx_fmt=png)

Part1 前言

大家好，我是ABC\_123。做过Android APK的安全审计的同行们都有这样的体验：一个apk甩过来，我们得手工打开jadx分析、手工检查是否加壳、手动查找AndroidManifest关键字，手工逐个看代码分析是否存在硬编码密钥，手工调试分析SO文件......所以分析一个apk是特别耗费时间和精力的。问题不在于这个APK分析有多难，而在于步骤多，生成结果散落各处，从而造成人是流程中最慢的环节。今天我们尝试通过Claude Code Skills的方式，让 AI 按工程化流程自动执行apk检测任务，最后生成报告，全部SKILLS由（ID：M1k3）编写。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2aSrrFtI5259NPOqfK7yzKpB8TQVkJFclAY9Ulom70TA8cKybkkhHVh4DVjB7edf4vsMBwvMtSWTgS7lKtib6YvLKmBYzDlhV5g/640?wx_fmt=png&from=appmsg)

## Part2 技术研究过程

* ## SKILLS简单介绍与使用

Skill 就是把“怎么把一件事做好”打包成一个可以反复用的能力，而不只是临时写一段更长的 Prompt 让 AI 进行回答。 它更像一个随时能调用的小工具，而不是一次性的对话指令。 一个Skill大致包括以下结构，最主要的是SKILL.md文件，SKILL.md 就是全部文档，AI 读完就知道怎么执行apk分析任务。

```
.claude/skills/<skill-name>/├── SKILL.md          # 技能定义（入口）├── references/       # 参考知识库├── tools/            # 配套工具脚本└── rules/            # 规则集
```

接下来将我们做好的SKILLS文件夹放在我们要分析的apk文件所在目录的.claude\skills\目录中，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2YEYmMRLlO07ctXTbQ8q2nn0iatXFaKRwXl4RMZFHAdkkerVjlVh3CKibuD0PfZOdFDpTQocQqrBpdKQz1GZByjaH44M0xOdv1B8/640?wx_fmt=png&from=appmsg)

输入/skills命令查看我们自己写的skill是否被claude正确识别，如果不能被正常识别，可能是配置文件位置或者格式错误。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2bdJryUAuThNouicO8DQafWJHu0OodS3Y2zicRZUqSP6fCicHTVPkwEWcfJWhAMXAM6SENwPxxVjDx6XDvft46YP61USm37qiaBiaM8/640?wx_fmt=png&from=appmsg)

* ## 分析APK的5个SKILLS介绍

该SKILLS的技能全景图如下，是一个流水线架构：串行入口对APK进行初步分析，包括加固检查、加壳检测及反编译；后续再进行4个并行分析模块；最后统一输出报告。

```
阶段 1（串行）            阶段 2（并行分析）                  阶段 3（汇总）┌──────────────┐        ┌────────────────────────────┐        ┌──────────────────────────┐│ 加固检测      │        │        并行分析模块         │        │        综合安全报告        ││ + 反编译      │───────▶│                            │───────▶│  comprehensive_analysis.md ││              │        │  ┌──────────────────────┐  │        │                          ││              │        │  │  Semgrep 扫描        │  │        │                          │└──────────────┘        │  ├──────────────────────┤  │        └──────────────────────────┘                        │  │  H5 分析器           │  │                        │  ├──────────────────────┤  │                        │  │  Manifest 分析器     │  │                        │  ├──────────────────────┤  │                        │  │  SO 分析器           │  │                        │  └──────────────────────┘  │                        └──────────────┬─────────────┘                                       │                                       ▼
```

如下图所示，加固apk需要走不同的工作流程。串行入口：加固检测是所有后续分析的前提，必须先完成；并行分析：四个分析任务相互独立，并行执行可以节省 60% 以上时间；统一输出：所有报告汇聚到一个目录，便于归档和对比。

```
if (已加固) {    跳过 Semgrep 扫描;     // 源码被加密，扫描无意义    跳过 H5 分析;          // JSBridge 代码不可读    执行 Manifest 分析;    // XML 资源未被加密    执行 SO 分析;          // SO 文件通常不在加固范围} else {    执行全部四项分析;}
```

* 参考知识库 references 机制

每个SKILL技能都可以携带自己的参考知识库，如so-analyzer这个SKILL。SKILL.md 控制在 100 行以内，保持简洁，篇幅太长的话Claude不会严格按照其内容执行；详细知识通过 `@references/` 引用，按需加载。这避免了一个超长 Prompt 淹没上下文窗口的问题。

```
so-analyzer/├── SKILL.md                          # 精简的执行指令├── references/│   ├── sdk_functions.md              # SDK 函数映射表（AI 知识增强）│   ├── so_auto_analyzer.md           # SO 分析方法论│   └── example_targets.py            # 目标模式示例└── scripts/    └── so_auto_analyzer.py           # 核心分析脚本
```

##

## Part3 五个分析APK的SKILLS

* ## 技能一：加固检测与反编译（apk-decompile-check）

这是整个流水线的入口技能，它主要做两件事：1. 加固检测。调用 `ApkCheckPack` 识别 APK 是否被加固（360加固、腾讯乐固、梆梆安全等）；2. JADX 反编译。将 APK 反编译为 Java 源码和资源文件，并输出分析报告。apk加固与否会自动影响后续技能的选择，加固处理的APK源码是加密的，所以需要跳过代码级分析，只执行 Manifest 和 SO 文件分析，这是一个关键的条件分支设计。

```
加固状态: 已加固加固厂商: 360加固安全检测特征:- ROOT检测: 有- 模拟器检测: 有- 反调试检测: 有
```

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2aibye4kichQ0jOz0UCaWEg0f9nHEoZSJ9HknDhOxFB1eqDr4R90Kut97fb26myEWiaSQMiblzp1z1dSlicPsib9sQeVq1nw5DHZaPYE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2bCwJxxdUzibz1AickicTQcfXxJ0XnbvWS2gPxW9DfbPJNlk4Iib0yUYbohwiaGBrWviaSwkyrDTxMTKKAeUhiapSek0fTQChJsQsdTTU/640?wx_fmt=png&from=appmsg)

* ## 技能二：Semgrep 安全扫描（semgrep-scanner）

该技能用 16 条自定义规则扫描 Java 源码中的安全漏洞，它不依赖 AI 的主观判断，而是用 Semgrep 静态分析引擎 + 自定义规则集做确定性检测。扫描结果由 JSON 自动转换为 Markdown 报告（`semgrep_report_converter.py`），按高/中/低危分类，方便阅读。

```
rules/├── crypto/│   ├── keys/          # AES、DES、HMAC 等硬编码密钥检测│   ├── cloud/         # 阿里云/AWS/腾讯云 AK/SK 泄露检测│   ├── certificates/  # 硬编码证书检测│   ├── iv/            # 硬编码 IV 检测│   ├── salt/          # 硬编码盐值检测│   └── keystore/      # KeyStore 密码硬编码检测└── webview/    ├── webview_insecure_config.yaml   # WebView 不安全配置    ├── jsbridge_sensitive_data.yaml   # JSBridge 敏感数据传输    ├── ssl_pinning_bypass.yaml        # SSL Pinning 绕过    └── intent_url_injection.yaml      # Intent URL 注入
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2YFibVeyRqtcst9ZXKmicDC3gT2RCEdkySDT9XxJibtvQvhzdKaTpeDSEVBK9NslTUOd8gqQDJSRrUw74dsrpicj7TsXImlDr9FXHo/640?wx_fmt=png&from=appmsg)

* ## 技能三：AndroidManifest 安全分析（android-manifest-analyzer）

该技能从 Manifest 和网络安全配置中挖掘攻击面，主要检查APK的AndroidManifest.xml 文件。该技能不只是罗列问题，而是标注风险等级并给出修复建议。例如导出 Activity 无权限保护会标记为「高危」。

| 检查维度 | 具体内容 |
| --- | --- |
| 安全标志 | `debuggable`、`allowBackup`、`usesCleartextTraffic` |
| 网络安全 | `network_security_config.xml` 的明文策略、证书信任 |
| URL Scheme | 自定义协议、Deep Link、潜在的劫持风险 |
| 组件导出 | 四大组件的 `exported` 状态及权限保护 |
| 权限声明 | 危险权限、自定义权限保护级别 |

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2aicjUS6JdDve5UjLicCcw56mp2CGiaKbUPXBwz0Aj4S2qG4BrPf68J98I30WB0SiclVvdsxWmNYg0HWCG7VibqFQvAcYzNaXEM5dkk/640?wx_fmt=png&from=appmsg)

* ## 技能四：H5/JS 数据返回路径分析（android-app-h5-data-return-analyzer）

该技能追踪 Native 到 H5 的数据通道，发现跨边界安全风险。现代 Android App 大量使用混合开发（WebView + H5），数据在 Native 和 Web 之间流转。这个技能追踪所有数据通道如下所示：不仅找出数据通道，还分析可导**出 Activity 的 Intent Filter**，拼出完整的 URL Scheme 攻击路径（如 `myapp://h5/open`），直接可用于渗透测试。

```
检查清单:├── WebView + JSBridge（addJavascriptInterface / @JavascriptInterface）├── Cordova Plugin 回调├── evaluateJavascript / loadUrl("javascript:...")├── URL Scheme / shouldOverrideUrlLoading├── Unity 通信（UnitySendMessage）└── React Native Bridge（@ReactMethod）
```

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2YopxDv1KEIdhJbMTr6z9Xia1ITSU8QmDMOqCAywSomonO0XQoBrx7Y55apictSvUyI4g8eyp6mA0dH8m9cF8YsojDE8uPsYd2Ug/640?wx_fmt=png&from=appmsg)

* ## 技能五：SO 文件敏感信息提取（so-analyzer）

该技能用 CPU 仿真器执行 SO 库中的函数，捕获运行时产生的密钥和 Token。这是技术含量最高的技能。它不是简单的字符串搜索，而是模拟执行：置信度阈值（`--threshold`）可调，低阈值会分析更多函数，适合深度审计。这让技能可以在「快速扫描」和「深度分析」之间灵活切换。

```
执行流程:1. 解析 ELF 结构 → 提取导入/导出符号2. 生成 Stub → 为外部依赖创建仿真桩3. 签名解析 → 从 JNI 函数签名推断参数类型4. 仿真执行 → 用 Unicorn Engine 运行 ARM64 代码5. 生成报告 → 输出发现的密钥、Token、证书
```

它配备了专门的参考知识库：1.  sdk\_functions.md：常见 SDK 的敏感函数映射表；2. so\_auto\_analyzer.md：详细的 SO 文件逆向分析方法论； 3. example\_targets.py：典型敏感函数的目标模式。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2aicvS6kllENlHWulZ343mCDbHmnSWkJHI0QbF4L2aAvP1OLHIw9VAjtAs9MnXcrTKtvYvcriaeYxa07aapmBZliaQRuMTs0E9rmE/640?wx_fmt=png&from=appmsg)

* ## 技能六：最佳实践检查器（skill-best-practices-checker）

该技能可以去检查技能的执行是否符合预期，输出报告是否能达到质量。它从 Claude Code 官方文档拉取最佳实践标准，对任意技能做自动化审查：

```
检查项:├── Frontmatter 格式是否规范├── 参数是否使用 $ARGUMENTS 语法├── SKILL.md 是否控制在 100 行以内├── 执行步骤是否清晰可执行├── 是否有验证方式└── 有副作用的操作是否标记 disable-model-invocation
```

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2ajejicSAtkdCia1xfK1c29D3HKcW9S0jpDD1LcvG1na0tADlvxONu84NAmpvAMSlYZL8Fd4vbLsfoK9R0j8n3ia3WIwIFvoImLrY/640?wx_fmt=png&from=appmsg)

##

* ## 输出结果汇总报告

所有技能设计完成后，使用过程如下：

```
# 1. 反编译（自动检测加固）/skill: apk-decompile-check /path/to/target.apk
# 2. 并行安全分析（AI 自动根据加固状态选择）/skill: semgrep-scanner/skill: android-manifest-analyzer/skill: so-analyzer/skill: android-app-h5-data-return-analyzer
# 3. 综合报告（AI 自动汇总所有分析结果）
```

最终在 `reports/` 目录下获得一份完整的安全评估报告：

```
reports/2026-04-12-143000-target-ap...