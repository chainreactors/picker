---
title: 使用ASC + 自建 MCP 做APK漏洞面定位流水线
url: https://mp.weixin.qq.com/s/rGr1WhpTcPK2WoFngUcVHw
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:04:15.271488
---

# 使用ASC + 自建 MCP 做APK漏洞面定位流水线

# 使用ASC + 自建 MCP 做APK漏洞面定位流水线

原创

安研新工
安研新工

赛博57库

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

|  |
| --- |
| MOBILE BUG BOUNTY · APK AUDIT PIPELINE APK 赏金：ASC + 自建 MCP 的漏洞面定位流水线 毫秒级定位危险 API 调用点，把「先反编译全包」倒转成「按危险面反查引用点」——附实测命令、输出与合规红线（成稿 2026-09-14） |

|  |
| --- |
| 📌 本文怎么读  本文先看两条流水线的时间损耗展示，方便读者建立「查询式审计」的直觉；再照表 A 把危险面换成可直接复制的查询命令，用本文实测的公开练习包走一遍「命中 → 收敛 → 精读」；随后自建一层 MCP 让 Agent 批量扫面，最后照 SOP 与红线收尾。第 08 节明确写了 ASC 现在做不到什么，动手前务必先读。 |

|  |
| --- |
| ⚠ 边界与合规  ①「跳过完整解压」是作者自述的实验特性、未合入主线，不要当成成熟能力依赖；②官方目前没有 MCP，第 06 节的 server 是自建的，文中已显式标注；③所有测试只在授权的目标上进行（赏金项目以项目范围为准）。本文不提供任何未授权目标的漏洞细节或利用代码。 |

|  |
| --- |
| 移动App赏金真正的瓶颈不是「看不看得懂代码」，而是时间和效率的最大化。本文给一条可复现的流水线：先用 ASC 把 300MB 混淆包当只读数据库来查询，再自建一层 MCP 把它的两个原语交给 Agent 批量跑面，人只负责验证与串链。全文命令与数据均来自GitHub项目文档里的实测引用，争议处已显式标注。 |

## 01 · 先算一笔账：赏金审计的时间烧在哪

一个 300MB 级别的商业 APK，用传统姿势（jadx 全量反编译 → 建全局索引 → 人眼加 grep）意味着什么？作者拿四个真实商业包做过对比，352MB 那个包的全局字符串交叉引用直接把 jadx 跑到 OOM；同一张图上 jadx GUI 的内存峰值标注是 **223GB+**。

这就是赏金猎人的现实约束：你在一个「可能没有漏洞」的目标上，先付掉 8 分钟索引、13GB 内存和一次 OOM 崩溃，才有资格开始看代码。而移动赏金的命中率又天然偏低——大多数包里没有能提交的问题，真正值钱的是那几个类。换句话说，**赏金审计的核心成本是「筛选」，不是「阅读」**。

所以工具选型的第一性问题应该是：能不能不做全量反编译，直接回答「危险 API 在哪里被调用」。ASC 就是冲着这个问题来的。

## 02 · 赏金视角：APK 里到底在找什么

移动端可提交的问题，绝大多数落在有限几类「危险面」上。把危险面翻译成**可查询的引用点**，是整条流水线最关键的一步——因为反编译器只能告诉你「谁引用了什么」，判断价值仍然是人。

表 A：危险面 → 查询 → 可提交漏洞类型（`findrefs` 查询维度为 string/type/method/field 四种）

|  |  |  |
| --- | --- | --- |
| 危险面 | 典型查询目标 | 常见可提交问题 |
| WebView 桥 | `addJavascriptInterface` / `javascript:` | JS 桥反射调用可达 RCE（低版本）、任意方法暴露 |
| WebView 配置 | `setAllowFileAccessFromFileURLs` | `file://` 跨源读取、本地文件窃取、任意页面加载 |
| 动态加载 | `Ldalvik/system/DexClassLoader;` | 加载可写目录代码 → 提权/RCE 链 |
| 导出组件 | manifest 中 `exported=true` 的 Activity/Service/Receiver/Provider | 越权调用、敏感功能暴露、Provider 数据越权 |
| 意图重定向 | Intent 透传 / `startActivity` 携带外部参数 | Trampoline 绕过权限、跳进非导出组件 |
| 明文凭据 | `field apiKey` / `secret` / 字符串 `Bearer` | 硬编码密钥、内网 endpoint 泄露 |
| 命令执行 | `Runtime.exec` / `ProcessBuilder` | 拼接可控入参 → 命令注入 |
| 传输校验 | `TrustManager` / `checkServerTrusted` | 证书校验空实现 → MITM |

|  |
| --- |
| 用法要点：这张表要**从右往左用**。先想清楚自己的赏金项目里哪类问题最可能被接受（有些项目不收 MITM、不收自测的低危），再倒推该查哪些引用点，最后才决定跑什么命令。反过来从工具能力出发，会得到一堆没人付钱的发现。 |

## 03 · 为什么快：把 R8 的优化反过来当反编译原语

ASC 全名是「Droid ASC: R8 Compiler Optimization as a DeCompiler Primitive」，Black Hat Europe Arsenal 议题（Apache-2.0，依赖只有 `androguard==4.1.3`）。它不封装 jadx，而是重新设计了三个环节：

01  **不建重型映射表，用 O(1) 指令定位原语**：把原始字节码 offset 常数时间映射回方法，跳过全量索引构建。

02  **按需在内存重建最小 DEX**：命中目标类后，只抽它的字节码与依赖，在内存里现场拼出一个自洽的小 DEX，再交给反编译；不落磁盘、无缓存目录。

03  **武器化 R8 的编译行为**：确定性常量重定位加指令去重，让相关代码在物理布局上高度聚集，这让跨 DEX 的引用搜索变成顺序扫描而不是随机寻址。

04  **无状态零预处理**：每次调用都是独立查询，没有「先建库」这一步——这一点对 Agent 化尤其重要，后面细说。

实测数据（作者基准图，ASC vs jadx，10 线程）：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 目标 APK | 全局 search | 单类反编译 | CLI 内存 | 磁盘缓存 |
| TelegramX 59MB | 493ms vs 20s（41x） | 168ms vs 6s（36x） | 36MB vs 1.0GB（28x） | 0 / 119MB |
| WhatsApp 130MB | 620ms vs 32s（52x） | 160ms vs 15s（94x） | 36MB vs 2.1GB（61x） | 0 / 30MB |
| Grab 228MB | 1.011s vs 2m14s（133x） | 177ms vs 37s（206x） | 58MB vs 7.1GB（125x） | 0 / 127MB |
| WPS 352MB | 1.79s vs 8m2s（269x） | 415ms vs 1m32s（222x） | 141MB vs 13.2GB（96x） | 0 / 322MB |

（左列为 ASC，右列为 jadx；括号内为倍数）

![img1](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XFXUibSGA3gaXwlNBAfemlMgneDLoTAUbejorsAzD2pGyAm3jgLW0kgWiblKF9nv9fJfwI1xXIAgSpF4dCJoM6EZiaY5VpibK9oz7rXUCZTwh18/640?from=appmsg)![img3](https://mmbiz.qpic.cn/mmbiz_jpg/XFXUibSGA3gazQnljWZwKxoXia3LLcUZjdyDmnZpHFdt821EoF0nyYE76dgVVeXSz5qSicHDs11bbrjnnibiaaToiaPodaly5icAtP2TehEcDfZ67s/640?from=appmsg)

对赏金工作的实际意义有三个：第一，查询一次的代价低于「打开 IDE 搜索框」的心理成本，于是你会愿意多试几组假设；第二，零磁盘缓存意味着你可以在同一台机器上并行审计多个目标而不炸硬盘；第三，也是最重要的——**毫秒级、无状态的单次调用，正好是 Agent 需要的那种工具接口**。

## 04 · 装上，先跑通几条命令

环境只有一个依赖，装完即可用：

|  |
| --- |
| `git clone https://github.com/MG1937/ASC.git`  `cd ASC`  `pip install androguard==4.1.3`  `python main.py --help`  `python main.py app.apk --gui` |

四条查询命令覆盖绝大多数场景（`--threads` 控制并行度）：

|  |
| --- |
| `# 定位单个类并反编译（支持 Lcom/poc/Main; 或点号写法）`  `python main.py getclass app.apk com.poc.Main --threads 16 -o Main.java`    `# 字符串引用（查 deeplink scheme、密钥前缀、内网域名）`  `python main.py findrefs app.apk string "javascript:" -o refs.txt`    `# 类型引用（查谁用了 WebView / DexClassLoader）`  `python main.py findrefs app.apk type Lcom/poc/Target;`    `# 方法引用（查谁调了敏感 API；配合类名收敛命中面）`  `python main.py findrefs app.apk method onCreate --class com.poc.Main`  `python main.py findrefs app.apk method notify --class MainActivity --fuzzy-class`  `python main.py findrefs app.apk field apiKey -o field_refs.txt` |

按表 A 落地的第一批命令（可以直接复制，把包名换掉）：

|  |
| --- |
| `# 危险面扫描：一个危险面对应一条查询`  `python main.py findrefs app.apk method addJavascriptInterface`  `python main.py findrefs app.apk method setAllowFileAccessFromFileURLs`  `python main.py findrefs app.apk type Ldalvik/system/DexClassLoader;`  `python main.py findrefs app.apk method checkServerTrusted`  `python main.py findrefs app.apk type Ljava/lang/ProcessBuilder;`    `# 凭据与配置面（field 查询按字段名模糊匹配）`  `python main.py findrefs app.apk field apiKey`  `python main.py findrefs app.apk field secret`  `python main.py findrefs app.apk string "Bearer "`    `# deeplink 与跳转面`  `python main.py findrefs app.apk string "://"`  `python main.py findrefs app.apk method startActivity` |

两个容易忽略的细节：**所有查询参数都是模糊（子串）匹配**——不需要写全字符串，`string flag` 会命中一切包含 `flag` 的字面量，这既省事也意味着你必须自己控制命中面；`--threads` 默认是 8，大包可以往上调。

实测手感（本文所有输出来自真实执行：InjuredAndroid 1.0.12，23.6MB，单个 classes.dex）：

|  |
| --- |
| `$ python main.py findrefs InjuredAndroid.apk string flag`  `classes.dex | Lb3nac/injuredandroid/FlagOneLoginActivity;->submitFlag`  `| matched=(flagOneButtonColor)`  `classes.dex | Lb3nac/injuredandroid/FlagSevenSqliteActivity;->submitFlag`  `| matched=(flagSevenButtonColor; flagSevenEncrypted)`  `classes.dex | Lb3nac/injuredandroid/DeepLinkActivity;->onCreate`  `| matched=(flag11)`  `...（实际 30 行命中）`  `TIME elapsed=0.18s rss=42332KB` |

实战建议：先 `string` 扫面（命中少、信息密度高、最适合开荒），再用 `method` / `type` 收敛到具体类，最后 `getclass` 把候选类拉成 Java 源码读。类型查询要注意**命中洪泛**——像 `Landroid/content/Intent;` 这种到处都在用的类型会刷屏，必须配合 `--class` 或先按包名过滤，别让它淹没真正有价值的几条。

**一条必须提前知道的校准项**：`--class` / `--fuzzy-class` 的类名过滤，我在这次实测里没跑出命中——精确 Dalvik 名、点号写法、README 里的 `--class MainActivity --fuzzy-class`、以及不带 `--class` 只给方法名四种写法，对 `method` 查询分别返回 0 行、0 行、0 行与数十行；同一包里 `type` 查询正常返回调用者。也就是说**这个类名过滤在你手上的版本与目标上是否生效，必须先自己验一次**，别把 0 命中读成「没有该调用」。稳妥做法：用 `string` 与 `type` 两个面交叉定位，`method` 只在不带类名时做粗筛再人读收敛。

## 05 · 从命中到漏洞：把查询结果读成线索

工具只能给出「谁引用了什么」，漏洞是人读出来的。下面是我在一线审计里最常用的几组查询，以及每条线索该怎么往下走：

|  |
| --- |
| `# 1. JS 桥：谁暴露了原生对象`  `python main.py findrefs app.apk method addJavascriptInterface`    `# 2. 本地文件跨源：WebView 的经典错配`  `python main.py findrefs app.apk method setAllowFileAccessFromFileURLs`    `# 3. 动态加载：注意排除热修框架，见下方过滤规则`  `python main.py findrefs app.apk type Ldalvik/system/DexClassLoader;`    `# 4. 明文凭据：先扫字段名，再扫前缀`  `python main.py findrefs app.apk field apiKey`  `python main.py findrefs app.apk string "Bearer "`    `# 5. 命令执行与拼接`  `python main.py findrefs app.apk method exec --class java.lang.Runtime` |

**先看一个真实闭环（原始输出）。** 同一个练习包上，`string flag` 圈出 30 个候选类，挑一个拉源码：

|  |
| --- |
| `$ python main.py getclass InjuredAndroid.apk Lb3nac/injuredandroid/FlagOneLoginActivity;`  `public final void submitFlag(android.view.View p4)`  `{`  `android.widget.EditText v4_5 =`  `(android.widget.EditText) this.findViewById(2131230887);`  `if (d.s.d.g.a(v4_5.getText().toString(), "F1ag_0n3")) {`  `...`  `}`  `}` |

硬编码口令 `F1ag_0n3` 就躺在反编译结果里——从查询到读出版本凭据，两三秒。这才是这条流水线真正的手感：**反编译不再是「打开工程」，而是小查询的副产品。**

然后是反面教材，也是本节最该记住的部分：**同一个包，三条命令的结果天差地别。**

•  `findrefs method addJavascriptInterface` → **0 命中**；但 `findrefs type Landroid/webkit/WebView;` 给出 3 处 WebView 使用点（DisplayPostXSS、FlagTwelveProtectedActivity、TestBroadcastReceiver）。**单条查询 0 命中不等于「没有」**，换查询维度才能下结论——这也正是自动化流水线必须多维度扫面的原因。

•  `findrefs method onCreate`（不加 `--class`）→ 刷出 80 多行，绝大多数是 androidx、Google Play Services、Flutter 的框架方法。**方法查询必须配 `--class` 收敛**，否则洪泛会淹没业务代码。

•  `findrefs string "http://"` → 全包只有 4 条，且全是库样板（`schemas.android.com` 的 XML 命名空间、`localhost`）。字面量查询抓不到被拼接、编码或走 HTTPS 的域名，得多组关键词分轮扫。

**误报过滤是这一节的...