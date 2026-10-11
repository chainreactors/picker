---
title: IRify 架构升级：分段报告与 C# .NET 支持
url: https://mp.weixin.qq.com/s/6ueit-MVOVV2Z_-zC0i-nA
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:01:50.148739
---

# IRify 架构升级：分段报告与 C# .NET 支持

# IRify 架构升级：分段报告与 C# .NET 支持

原创

Yak
Yak

Yak Project

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuud9I0gL4U9bSUD2lUpicibTtwAKcSPvkh1Wlibj7Mmo7BOWN5myLMiaeQQ9w/640?wx_fmt=webp&from=appmsg)

最近 SyntaxFlow 做了一次比较大的升级。扫描方式、阶段信息、规则覆盖、大项目表现都有明显变化。这篇文章把这些变化讲清楚，并在中间穿插真实项目的扫描片段作为例子。

一、一次扫描，三种互补的检测模式

过去提到 SyntaxFlow，默认的理解是：编译 SSA，然后做数据流分析。现在引擎里跑的是三种互补的检测模式。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FoEsd3lNLWx5fWXLXQbBFSIxUEuHH73E3u39CvVCXibakVVePia8ga4fzRQuuWica8GnNnk7uTj8YyL19DAlTUPSofiavbveGhjog/640?wx_fmt=png&from=appmsg)

**source 模式（源码检测）**：直接在源码文本上匹配，不需要编译。适合"看代码形态就能判断"的问题——硬编码密钥、危险配置、不安全的写法。因为不依赖编译，收集完代码立刻就能出结果。

**struct 模式（结构检测）**：在每个编译单元编译骨架之后执行。每个包的骨架编译出来，先把包内的语义结构检查掉，再继续下一个单元，不用等整个项目编译完。适合"包内就能定性"的问题——危险 API 调用、不安全的语言结构。

**ssa 模式（语义检测）**：全项目 SSA 编译完成后执行，做跨函数、跨包的数据流和污点分析。适合必须追踪数据来源的问题——SQL 注入、SSRF、完整的 XSS 污点链。

三种模式不是三选一，而是互补。`yak code-scan` 默认把三种都跑一遍，也可以用 `--mode` 指定只跑其中一种或两种。

用一个真实的小项目看效果会很直观。下面是对一个 PHP 靶场项目（169 个 PHP 文件、9 个 JS 文件，约 6.3 MB）只跑源码检测的输出：

```
$ yak code-scan -t ./target --mode source
[INFO] [code-scan] 代码检测 (inspect) stage=100% overall=30%[INFO] [Task e63d106d-309d-461c-a413-ddfccd41c8b1][INFO]   status=done progress=30.00%[INFO]   Failed=0 Skipped=0 Success=595 Finished=595 Total=595 Risk=125
=============================================== Scan Summary===============================================| Failed Rules         |                    0 || Risk Count           |                  125 || Success Rules        |                  595 || Total Rules          |                  595 || Total Scan Time      |           1.1037101s |===============================================
```

595 条规则、1.1 秒、125 条风险。这就是"不编译也能出结果"的实际体感。

源码检测这一轮还有几处能力增强，可以理解为原有文本匹配能力的增强版本——以前也能匹配，现在匹配得更准、表达力更强：

**·上下文感知的正则:**

支持"只有出现在某个代码块内部的匹配才算命中"、"出现在这段配置里的不算"、"多个正则同时命中才算"这类组合条件。规则语法上新增了 `inside` / `not_inside` 两个操作符，`&` 和 `-` 在源码命中值上改为区间重叠语义。

**·在文件中继续搜索:**

支持 `$hit.pattern_regex(...)` 这类链式写法——拿到一个命中之后，在它所在的文件里继续搜索下一个模式（默认 `scope=file`，也可切到 `scope=region`），用来表达"先定位到某个块，再看块里有没有危险写法"。

**·命中位置带完整上下文:**

以前告警只有一段匹配片段，没有文件路径和行号，遇到多字节字符（比如中文注释）时行列还会错位。现在每个命中都锚定到完整文件，位置计算统一为字节语义，告警带上真实文件路径、行号和代码片段；每条风险还新增了 `scan_mode` 字段，标记它来自源码检测还是语义分析。

**·与编译解耦:**

对本地目录、Git 仓库、zip/jar 包这些输入，源码检测先收集源码直接扫描，不再为了拿到源码目录而先编译一遍 SSA；如果这次扫描同时包含语义分析，收集好的源码目录会被复用。

二、扫描过程会输出四个阶段的信息

SyntaxFlow 现在会在扫描过程中汇报四个产品阶段：**收集代码 → 代码检测 → 语义检测 → 深度分析。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72F1UlP7tul2x2vbUCt4Dr0s7KTeUgy9evYfsNIdq2ZDh3KlObdnFicGYzmLpzqrEQsNjcueDEAUd7TphMDYDWqJehAhetQyicsvM/640?wx_fmt=png&from=appmsg)

每个阶段独立汇报自己的执行信息：跑了多少条规则、命中多少条风险、实际消耗的规则耗时。这些信息跟随扫描结果一起返回并持久化，所以即使扫描进程的事件流已经过期，事后仍然能查到本次扫描在收集阶段处理了多少文件、多少代码行、多少体积，以及每个阶段的规则执行情况。

对只请求了部分阶段的扫描（比如只跑代码检测），没有执行的阶段会被明确标记为跳过，而不是留下含义不明的空状态。

上面那个小项目跑完整三模式时，四个阶段的日志是这样的：

```
[INFO] [code-scan] 收集代码 (collect) stage=0%   overall=0%[INFO] [code-scan] 收集代码 (collect) stage=100% overall=10%[INFO] [code-scan] 代码检测 (inspect) stage=0%   overall=10%[INFO] [manager:403] rulecount 595 ; total query: 595[INFO] [code-scan] 语义检测 (review) stage=0%    overall=30%[INFO] [code-scan] 深度分析 (analyze) stage=100% overall=100%
[INFO] [code-scan] stage 收集代码 (collect) status=succeeded duration_ms=0    rules=0   risks=0[INFO] [code-scan] stage 代码检测 (inspect) status=succeeded duration_ms=1118 rules=595 risks=125[INFO] [code-scan] stage 语义检测 (review)  status=succeeded duration_ms=9568 rules=151 risks=1510[INFO] [code-scan] stage 深度分析 (analyze) status=succeeded duration_ms=342  rules=348 risks=0 duration_ms=342  rules=348 risks=0
```

深度分析阶段有个细节值得说明：348 条规则里有 347 条因为语言不匹配被跳过。内置 SSA 规则覆盖 Java、C#、Go 等多种语言，而这个小项目是 PHP/JS，引擎会自动跳过不适用的规则，不在无关语言上浪费分析开销。日志里逐条标注了原因：

```
 [DONE] [100.00%]: 检测 Java 路径遍历漏洞        status=skipped: language mismatch [DONE] [100.00%]: 检测 Java EE 的 XSS 漏洞      status=skipped: language mismatch [DONE] [100.00%]: 检测 C 语言缓冲区溢出漏洞      status=skipped: language mismatch
```

另外，每个阶段的 `risks` 是该阶段**流式上报的计数**。同一个问题如果同时被前一阶段和后一阶段命中，最终报告只保留后一阶段（更精确）的那条。所以阶段计数相加不等于最终报告条数——上面这次扫描最终报告是 150 条（125 条源码检测 + 25 条结构检测）。

这些阶段信息同时暴露给 CLI 和平台侧使用，客户端界面会逐步呈现。

三、规则库：规模、速度与精度分级

目前内置规则文件近 1200 个。其中显式声明了扫描模式的有 759 条：source 584 条、struct 151 条、ssa 24 条；其余是不带模式声明的历史规则。

三种模式的预期速度和理解能力，本质上是分析深度不同：source 只看文本，所以快；struct 在一个包的结构内做判断，所以中等；ssa 要追踪数据在整个代码仓库里的流动，所以慢。三种模式可以按需组合——想快速摸底只跑 source，想做完整检测三种全开。

***YAK***

**3.1 规则分布**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72H4FMl06O2ogoZYUgaSm2f5icz8ssnL5HShOI7L8vMJDwf9XiazyIuu0pibjCTsRWiaHbDibiakwqgEV8LoyI8n2a93M0xnz0BvYYkEQ/640?wx_fmt=png&from=appmsg)

（图：三条横向长条对应三种扫描模式，**条的长度代表该模式的规则数量**；条内色块代表语言构成，颜色与底部图例一一对应。source 规则最多（584 条），struct 151 条，ssa 规则最少（24 条）。数据截至 2026-10-10。）

从语言构成看，source 规则中语言无关的通用规则（general）有 345 条，其余以 Java（56）、Python（45）、PHP（41）、C#（39）为主；struct 规则集中在 Java（44）、Python（28）、C#（25）、PHP（24）；ssa 规则最少（24 条），覆盖 Java（6）、C#（5）、Python（4）、PHP（4）等语言。

***YAK***

**3.2 组织方式与质量**

**按 CWE 和代码模式组织，而不是按 CVE 指纹。** 以 Java Spring 系列为例，新增的 41 条规则是按通用漏洞类型写的——SQL 注入、命令注入、路径穿越、XSS、CSRF、开放重定向、SSRF、XXE、反序列化、弱加密等——而不是针对某个 CVE 的特定代码形状。同一个漏洞类型出现在其他项目、其他框架里同样能命中。

**按扫描模式拆分规则。** 同一条检测目标会按"用什么方式判定最合适"落到不同模式：字面量和配置类问题放 source，能靠调用本身定性的放 struct，需要追踪数据流的放 ssa。

**每条规则都有可读的说明和修复建议。** 全部 source 规则都带完整描述，写清楚漏洞原理、触发场景、影响分析和修复方式。

**误报经过专门治理。** 有一批改动专门针对高频误报，改完在真实项目上重扫对比。可量化的例子：某个 PHP 项目里反引号相关的误报从 11 条降到 0；70 个 shell 文件的变量展开误报从 611 条降到 147。

**规则自带正反例校验。** 内置规则内嵌正例和反例用例，规则改动后必须做到正例命中、反例保持干净，否则内置校验不通过。实际跑一次校验的输出：

```
$ yak verify-builtin-risk[INFO] inspected 1196 rules (102 libraries), 1317 alerts, 112 risk types
```

***YAK***

**3.3 规则命中的样子**

还是用那个 PHP 靶场项目做例子，源码检测命中的风险按规则聚合，前几名是这些：

| 规则 | 命中数 | 说明 |
| --- | --- | --- |
| `source-php-shell-exec` | 24 | PHP shell 命令执行 |
| `source-php-md5` | 21 | PHP `md5` 弱哈希 |
| `source-php-header-call` | 12 | 响应头写入外部数据 |
| `source-php-mt-rand` | 12 | `mt_rand` 弱随机数 |
| `source-php-backticks` | 10 | PHP 反引号执行命令 |
| `source-js-innerhtml` | 6 | JS `innerHTML` 赋值 |
| `source-php-xpath-query` | 6 | XPath 查询注入 |
| `source-php-allow-url-include` | 6 | 危险的 URL include |
| `source-js-eval` | 4 | JS `eval` |
| `source-secrets-username-password-uri` | 4 | 代码中硬编码的账号密码 |

报告里每条风险都带文件路径、行号、列号：

```
source-php-shell-exec              vulnerabilities/exec/source/low.php          line 10source-php-md5                     vulnerabilities/captcha/source/low.php       line 57source-php-backticks               vulnerabilities/captcha/source/low.php       line 60source-php-allow-url-include       includes/page.inc.php                        line 672source-php-header-location         vulnerabilities/fi/index.php                line 38source-js-eval                     vulnerabilities/javascript/source/high.js    line 83source-secret-password-assignment  vulnerabilities/sqli/test.php               line 4
```

四、C#/.NET：完整补上的新语言

C#/.NET 是这一轮重点补齐的方向。以前做 .NET 项目可用的安全规则有限，现在 C# 有了成体系的覆盖。

**规则规模与覆盖面。** C# 内置规则 90 条，分布在 29 个 CWE 类别中，另有 7 条 `lib` 规则用于描述 source/sink 等基础语义。

| 类别 | 覆盖内容 |
| --- | --- |
| 注入类 | SQL 注入（`SqlCommand`、`CommandText`、字符串拼接与插值）、命令注入（`Process.Start`）、LDAP 注入（`DirectorySearcher.Filter`）、XPath 注入、XML 注入 |
| 反序列化 | `BinaryFormatter` 、Newtonsoft `TypeNameHandling` 不安全配置、`SoapFormatter` / `LosFormatter` |
| 危险数据流 | 路径穿越、SSRF（`HttpClient`）、XXE（`LoadXml`）、XSS（`Response.Write`、`Html.Raw`）、开放重定向 |
| 加密与配置 | 弱加密算法（含 ECB 模式）、弱随机数（`System.Random`）、证书校验回调、明文传输、未签名 Token、Cookie 安全与 `SameSite` |
| 其他 | 代码注入、不安全反射、Mass Assignment、CORS 配置、堆栈信息泄露、正则 DoS、日志伪造、响应头注入 |

**C# 现在和其他语言一样得到完整支持。** 语言前端、SSA 构建、规则描述、正反例校验、三种扫描模式，C# 都齐了。按模式统计，C# 规则里 source 39 条、struct 25 条、ssa 5 条，分工是：

* 危险调用本身就能定性（`BinaryFormatter.Deserialize`、`System.Random`、`DirectorySearcher`）→ struct 模式，编译期查掉

* 需要追踪数据来源（SQL 注入、XSS、路径穿越）→ SSA 数据流

* 纯字面量和配置类判断 → source 规则

**规则描述完整可读。** 每条规则都带漏洞原理、触发场景、影响分析和修复建议。以 SQL 注入规则为例，描述里会给出有问题的 C# 代码，说明攻击者把输入改成 `name' OR 'a'='a` 之后 WHERE 条件为什么会恒为真、带分号时如何变成多条语句删除整表，最后给出参数化查询的修复方式。

**背后是独立...