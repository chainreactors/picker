---
title: 10月Next.js未授权远程代码执行漏洞链分析
url: https://mp.weixin.qq.com/s/dvMj_VJ8zeaCmCWtjJqJPw
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:25:09.544441
---

# 10月Next.js未授权远程代码执行漏洞链分析

# 10月Next.js未授权远程代码执行漏洞链分析

原创

Thanatos
Thanatos

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 免责声明：本文复现步骤仅限作者自建隔离实验环境，请勿在未获授权的系统上验证。

---

## 摘要

2026-10-14，Vercel以带外方式发布Next.js 16.4.1（Active LTS）与15.5.28（Maintenance LTS），修复三枚上游依赖引发的漏洞：两枚Critical级可致未授权远程代码执行（RCE），一枚High级为Server Actions拒绝服务[1]。

本次更新的三个特殊之处：两枚修复原定9月发布，因上游依赖交付延迟而推迟[1]；三枚公告中有两枚**没有CVE编号**，且截至本文撰写时尚未进入OSV/npm advisory数据源，主流依赖扫描器存在结构性漏报[2][4]；两枚RCE的根因分别落在React Server Components序列化通道（`react-server-dom-*`）与原生SVG渲染栈（librsvg/libxml2经sharp引入）两个完全不同的层次，却共用同一App Router攻击面。

**关键词**：Next.js；React Server Components；`use cache`；Cache Components；Image Optimization；librsvg；use-after-free；sharp；未授权RCE；供应链安全

![Next.js未认证请求的四条入口与缺陷落点](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4OZrYGPs9JveYGdGt6icibTyCcFUaU0H3Eq2Hp0HscQZpMricc9UicYC1Cxc06QVr4bib3esmQ2jE5a7sOUX7ZAlKJZndRKJplPDCFPMVNNtwFuNg/640?wx_fmt=svg&from=appmsg)

Next.js未认证请求的四条入口与缺陷落点

**图1** 未认证请求的四条入口、缺陷落点与后果分级。虚线框表示9月已修复的Satori注入原语，它与10月的原生内存缺陷位于同一图像渲染链上。

---

## 1 漏洞概述

### 1.1 披露时间线

![2026年8—10月Next.js漏洞披露时间线](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6TPcaQQL1aIgRMMCibqrs8hrOKiawd4el3QqkVbXZowZO9gPG3LzkIgCp0eRCcrr3N6ibpialWaiaWDRXpj2PVicWPOApZ9DibXiaJBk4rcOPxDg0u7A/640?wx_fmt=svg&from=appmsg)

2026年8—10月Next.js漏洞披露时间线

**图2** 8—10月披露节奏。红色节点为Critical级RCE修复，橙色弧线表示两项修复因上游依赖延迟从9月例行发布推至10-14的带外发布[1][6]。

| 日期 | 事件 |
| --- | --- |
| 2026-07-13 | Next.js确立月度安全发布流程 |
| 2026-08-25 | 提前一天发布16.3.3 / 15.5.24：修复Windows路径穿越RCE（CVE-2026-75604）与AVIF优化RCE（GHSA-2xp9-vwfh-vxw4）[6] |
| 2026-09-22 | 带外发布16.3.6 / 15.5.26：修复`next/og``ImageResponse` RCE（CVE-2026-94545，上游Satori转义缺陷）[6] |
| 2026-09-23 | librsvg use-after-free（CVE-2026-96889）细节公开，代号**VectorFreed**[7] |
| 2026-09-27 | sharp发布修复版本，捆绑的librsvg完成升级[7] |
| 2026-09-30 | 9月例行发布16.3.7 / 15.5.27（9项漏洞），其中两项因上游未就绪被推迟 |
| 2026-10-08 | 官方预告带外更新：处理"两枚Critical + 一枚High"[1] |
| 2026-10-14 | 发布16.4.1 / 15.5.28，同时公开三枚Next.js公告与两枚React上游公告[1][2][3][4][5] |

### 1.2 评分与影响面

| # | 编号 | 位置 | Severity | CVSS 4.0 | 受影响版本 | 修复版本 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | GHSA-673q-mjm6-r5xr 上游GHSA-xqc2-xf4c-x3h3 | `use cache` 函数返回多个typed array | Critical | 9.5 AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:N | 16.0.0–16.4.0 | **16.4.1**  react-server-dom-\*需19.0.9/19.1.10/19.2.9/19.3.1 |
| 2 | CVE-2026-96889 GHSA-2464-fhr4-w9xw | Image Optimization处理SVG | Critical | 9.5 AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H | 10.0.0–15.5.27；16.0.0–16.4.0 | **15.5.28 / 16.4.1**  缓解：sharp≥0.35.5 |
| 3 | GHSA-p3m5-59mp-jv5r 上游GHSA-h3gv-c5rc-p453 | Server Actions拒绝服务 | High | 8.2 AV:N/AC:L/AT:P/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:N | 13.0.0–15.5.27；16.0.0–16.4.0 | **15.5.28 / 16.4.1** |

两点需在工程上强调：

* **漏洞一仅影响16.x。** Cache Components是16.x特性，15.5分支不在区间内，`v15.5.28`的release notes也只列后两项[1]。但官方原话是"**即使你的应用没有类似函数也应当立即升级**"[2]，不能据此跳过。
* **CVSS分歧反映的是攻击面差异。** 同一枚CVE-2026-96889，Red Hat给CVSS v3 7.8（`AV:L`+需用户交互，上游修复版记为2.63.1），Vercel在Next.js语境下给CVSS 4.0 9.5（`AV:N`+无需交互）[3][8]。差异来自"由谁触发解析"：桌面场景需用户打开恶意图片，而Next.js只需一个未认证的`GET /_next/image?url=...`。定级应以自身业务是否允许未认证请求直达图像处理组件为准。

---

## 2 漏洞详情

### 2.1 漏洞一：`use cache`返回多个typed array的未授权RCE

官方表述（逐字）[2]：

> "A vulnerability in applications using App router with Cache Component can lead to remote code execution. The application needs to have a `use cache` function that returns multiple typed arrays."
>
> "There is no known workaround for affected applications with such `use cache` functions. You should upgrade immediately even if your application does not have similar functions."

根因在React而非Next.js。上游公告限定条件为："Crafted payloads targeting frameworks supporting React Server Components can lead to remote code execution. This only affects extremely rare cases where responses transport multiple typed arrays and an attacker-controlled value."[5]受影响的是三个RSC序列化绑定包`react-server-dom-webpack`/`-parcel`/`-turbopack`，区间19.0.0–19.0.8、19.1.0–19.1.9、19.2.0–19.2.8、19.3.0。

攻击链三个必要前提，缺一即不成立：

1. 使用**App Router**并启用**Cache Components**；
2. 存在返回**多个**typed array（`Uint8Array`/`ArrayBuffer`等）的`use cache`函数，典型如返回字节与签名二元组、protobuf/msgpack序列化载荷；
3. 这些数组中包含**攻击者可控值**（请求体、query、header、上传字节、外部API响应）。

满足前提时，恶意输入进入RSC（"Flight"）协议的反序列化流程。typed array在Flight载荷中以分块引用表达，**多个**typed array的偏移与引用解析存在缺陷路径，可被引导至异常对象并影响后续调用目标绑定，最终在服务端进程上下文执行代码。需明确：**Vercel与React均未公布该缺陷的调用链级细节**，本文不对未公开的gadget链作臆测。

历史坐标：这与2025-12的React2Shell（CVE-2025-55182 / CVE-2025-66478，RSC Flight协议原型链污染，CVSS 10.0）落在同一组`react-server-dom-*`包上，但本次范围窄得多——React自己用"extremely rare cases"作了限定[5]。此外Vercel在2026-05的变更日志中已承认，RSC类攻击载荷"表现为正常的HTTP请求结构，WAF层无法可靠拦截"，该结论对本次同样适用。

### 2.2 漏洞二：Image Optimization处理SVG的未授权RCE（CVE-2026-96889 / VectorFreed）

官方表述（逐字）[3]：

> "A memory-related vulnerability has been discovered in an upstream library used for Image Optimization can lead to possible remote code execution (RCE) when Next.js runs on glibc-based Linux."
>
> "Ensure the version of `sharp` used by Next.js is greater than or equal to `0.35.5`."

这不是Next.js的代码缺陷，而是原生栈内存破坏的穿透——公告给出的缓解与修复动作都落在sharp版本上，而非Next.js自身的优化器代码。数据路径：

```
攻击者 → GET /_next/image?url=<attacker-hosted>&w=...&q=...
      → Next.js Image Optimization
      → sharp → libvips (VipsForeignLoadSvg) → librsvg + libxml2   ← CVE-2026-96889
      → 原生进程内存破坏 → glibc Linux上可稳定化为代码执行
```

发现者@rafabd1（Rafael B. Dias）将该链命名为VectorFreed，机制如下[7]：SVG可通过`xi:include`引入另一个SVG文档；脆弱路径中，**libxml2在外层文档展开实体时，librsvg已开始解析被包含文档**；若被包含SVG声明**同名实体**，librsvg会替换并**释放**第一个实体对象，而libxml2仍持有其指针；被包含文档解析结束后，libxml2继续用这一**悬垂指针**写入，此时该内存可能已归属其他对象。结果是崩溃，而"**in other cases this also led to command execution**"。这是两个解析器对同一文档树并发持有可变状态导致的生命周期不一致（owner-confusion UAF），不是简单越界写。

关键约束：

| 条件 | 说明 |
| --- | --- |
| 平台 | 公告仅指**glibc-based Linux**；musl/Alpine与macOS不在官方风险描述内，能否稳定利用还取决于Node.js构建是否加固（PIE/RELRO）[3] |
| 运行时 | Node.js运行时。Edge运行时用沙箱化`resvg-wasm`，不进入该路径 |
| SVG入口A | `images.dangerouslyAllowSVG: true` +攻击者可控`url`。**默认关闭**，官方文档的理由正是"SVG具备与HTML/CSS同类特性，缺乏CSP时会导致漏洞"[9] |
| SVG入口B | `next/og` 的`ImageResponse`在Node运行时下使用**同一套**渲染栈，与CVE-2026-94545共享底层缺陷面[1][6] |
| 依赖形态 | 使用sharp预构建二进制时，真正的librsvg藏在\*\*`@img/sharp-libvips-*`**包内，**只升级系统librsvg无效\*\*[7] |

**修复实质**：该条公告的缓解与修复都表现为"把sharp提升到0.35.5"，其内含修复后的librsvg[3][7]。这解释了该条公告为何横跨Next.js 10.0.0至16.4.0——漏洞一直存在于依赖树中。上游librsvg修复版被记为2.63.1（Red Hat）/2.63.2（VectorFreed与sharp捆绑）[7][8]。

![sharp与librsvg的版本传导链](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM426UaMwxXQzwLQXp9uujibNx4cPibXszSA6ibYTKTbjeP4icrAqCodQ6P6nDGsOiaDEnpy5yAkAobl0ZDu1hpd8Ja1vE2pHubibQTsD2diaO4kKPicag/640?wx_fmt=svg&from=appmsg)

sharp与librsvg的版本传导链

**图3** 修复的版本传导链与两个最常见的处置失效点。缺陷实际落点在librsvg，而它由sharp的预构建捆绑包带入应用，因此"升级了next"与"库已修复"之间还差一次依赖树核验。

### 2.3 漏洞三：App Router Server Actions拒绝服务

官方表述（逐字）[4]：

> "Crafted requests targeting Next.js applications using App Router with at least one Server Action can lead to excessive CPU usage blocking processing of further requests in the same process."
>
> "Applications using Pages Router or not using Server Actions are not vulnerable."

上游React公告表述更宽："...this could lead to out-of-memory exceptions or excessive CPU usage."[5]两点不一致：React侧同时提到**OOM与CPU耗尽**，Next.js侧只强调CPU；且React公告正文段落把受影响版本写作19.0.0–19.0.7/19.1.0–19.1.8/19.2.0–19.2.7，而页面表格列出19.0.0–19.0.8/19.1.0–19.1.9/19.2.0–19.2.8/19.3.0，**同一公告内部自相矛盾**——做资产判断时按更宽的表格取保守值[5]。

利用门槛极低：只需应用中存在至少一个Server Action，无需其被业务调用、无需认证。Next.js默认以有限进程数处理请求，CPU打满后同进程全部请求排队，等效全站不可用。除升级外无workaround。

### 2.4 同系列前奏

单独讨论10-14的三枚会低估风险，它们与8—9月三枚属于同一攻击面的连续发现：

* **CVE-2026-94545**（9-22修复于16.3.6 / Satori 0.33.5）：根因是Satori把攻击者可控值写入SVG元素、XML名称与内部style字段时**转义不足**，使其被当作SVG标记解释[6]。即\*\*Satori的CWE-116编码缺陷负责"把文本变成SVG标记"，VectorFreed一类内存缺陷负责"把标记变成代码执行"\*\*——注入原语与内存破坏原语的组合才是本轮图像类RCE的完整形状。
* **GHSA-2xp9-vwfh-vxw4**（AVIF，CVSS 4.0 9.5）：根因在sharp依赖的**libheif**堆溢出；官方缓解是"在完成上游修复传导之前**直接禁用AVIF优化**"[6]。这是Next.js首次以"关掉功能"而非"等补丁"应对原生栈RCE。
* **CVE-2026-75604**（Windows路径穿越，CVSS 9.0）：ISR/增量缓存键的转义正则只覆盖`/`、`#`、`?`，**漏掉反斜杠**，Windows上`..%5C`可越出缓存目录[6]。第三方分析认为后续可读取`server-reference-manifest.json`中的Server Action `encryptionKey`进而伪造`Next-Action`绑定参数，**该升级路径官方公告文本未记载，应作假设而非结论**。

---

## 3 复现与验证

> 步骤3.2的资产自查为...