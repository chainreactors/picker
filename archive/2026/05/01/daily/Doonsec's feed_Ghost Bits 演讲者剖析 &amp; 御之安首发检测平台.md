---
title: Ghost Bits 演讲者剖析 &amp; 御之安首发检测平台
url: https://mp.weixin.qq.com/s/644j8bwWbF8Ud0aZe2ftXQ
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:54:54.607153
---

# Ghost Bits 演讲者剖析 &amp; 御之安首发检测平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/txKdUNHV69NPMzv9vSgyPCKzRbrXHNR7y5bQQVGWKyW30e0w6WqXZibtica87EAQ6CBCn2l7ve77DeL54s3DGBtROe844iauD6rrZK7jREs0Ac/0?wx_fmt=jpeg)

# Ghost Bits 演讲者剖析 & 御之安首发检测平台

米斯特安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于御之安先驱实验室
，作者始终在线的

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4QxFczKO6AHzTttdibEwLMtYpodSfLz4GSicsv7faqesUw/0)

**御之安先驱实验室**
.

御之安先驱实验室是御之安科技旗下一支国际一流的信息安全团队。以守护无声，保障万象为使命。目标是为全球用户提供最先进、最安全的解决方案，从而保护他们免受网络和信息安全威胁。

## 写在前面

2026 年 4 月，Black Hat Asia 2026 上一个名为 Ghost Bits（幽灵比特位）的新型攻击面被正式披露。和以往的漏洞披露不太一样：Ghost Bits 没有指向某一个具体应用组件或程序，它影响的是一整类 Java 生态的系统性缺陷 —— Tomcat、Jetty、Spring、Jackson、Fastjson、Apache HttpClient 等十多个主流组件都在影响范围里，WAF、IDS 这些老防线在它面前集体失明。

该议题在 Black Hat Asia 2026 现场公开发表，原题《Cast Attack: A New Threat Posed by Ghost Bits in Java》。发现者：

* **浅蓝（Xinyu Bai）—— 御之安科技 先驱实验室研究员。**
* **1ue（Zhihui Chen）—— 阿里云 研究员。**

下面是来自御之安先驱实验室的深度解读、CVE 实战分析、修复建议，以及社区版专项扫描工具的简介。

## 一、Ghost Bits 漏洞原理

Ghost Bits（幽灵比特位）的本质，是 Java 在处理 Unicode 字符到 byte 的转换过程中，**静默丢弃了高 8 位、只保留低 8 位**。

具体场景包括 `String.getBytes()`、`ByteArrayOutputStream.write(ch)`、`DataOutputStream.writeBytes()`、`(byte)ch`、`ch & 0xFF`等几乎所有 Java 代码里常见的"字符 → 字节"操作。它们本质上都执行了同一件事：

```
截断结果 = unicodeChar & 0xFF
```

只要构造一个 Unicode 字符，让它的低 8 位等于目标 ASCII 字符，就能在服务端伪装成那个 ASCII 字符。看几个直观的例子：

```
阮 = U+962E → 0x962E & 0xFF = 0x2E → '.'
```

```
严 = U+4E25 → 0x4E25 & 0xFF = 0x25 → '%'
```

```
灵 = U+7075 → 0x7075 & 0xFF = 0x75 → 'u'
```

攻击者只需把 Payload 中的关键 ASCII 字符（如 `../`、`union select`）替换成精心选取的 Unicode 字符。WAF 看到的是无意义的中文字符序列，规则不命中；后端 Java 在解码时高位被截断，原始攻击载荷被忠实还原 —— 绕过完成。

研究中在 GitHub 上检索 Java 代码中典型的 Ghost Bits 写法（`(byte)ch`、`ch & 0xff`、`baos.write(ch)`、`writeBytes(...)`等），命中 **超过 8,100 条**。这种缺陷在 Java 生态里分布之广，已经远远超出"某个框架疏忽"的范畴 —— 它是整个 Java 生态共存多年的"集体盲点"。

## 二、攻击链实例：CVE-2025-41242

讲再多原理，不如看一条完整的攻击链。以 Spring Framework 路径穿越漏洞 **CVE-2025-41242**为例，整个利用过程分为四步：

| 步骤 | 攻击者动作 / 防御侧反应 |
| --- | --- |
| **1. WAF 放行** | WAF 看到请求中 `阮严灵丰丰甲来`等 Unicode 字符，没有敏感关键词，**放行** |
| **2. Spring 字面量校验放行** | `ResourceHttpRequestHandler#getResource` 调用 `isInvalidPath(path)`检查字面量 `../`，路径中没有 `../`，**判定安全** |
| **3. 截断发生** | `StringUtils.uriDecode()` 内部的 `baos.write(ch)`丢弃高 8 位，`阮`（U+962E）→ `.`（0x2E） |
| **4. 路径折叠** | Jetty / Servlet 容器将 `%u002e`解码为 `.`，最终 `.%u002e`→ `..`，**目录穿越成功** |

每一层防御都"看到了自己以为安全的输入"，但每两层之间的语义解读不一致 —— 这就是 Ghost Bits 的核心威胁：**编码层与解析层的语义差异**。

这种攻击模式可以平移到 SQL 注入、反序列化 RCE、文件上传 Webshell、SMTP 注入、HTTP 请求走私等几乎所有"WAF 看字符 / 后端处字节"的场景。

## 三、为什么传统 WAF 救不了你

这事真没法怪 WAF 厂商 —— Ghost Bits **根本就发生在 WAF 看不到的层面**：

* WAF 工作在 HTTP 字符串语义层，看见的是 Unicode 原文；
* 漏洞发生在 JVM 内存中的字符 → 字节转换层，是 WAF 触不到的下游。

这是一道架构性鸿沟，单靠规则补丁追不上 —— 攻击者拥有 0xFFFF 量级的 Unicode 字符空间可以排列组合。

> 想从根本上止血，得回到代码层，网络边界已经管不到了。

## 四、影响有多大

### 已确认受影响的组件

| 组件 | 漏洞类型 |
| --- | --- |
| Apache Commons BCEL | WAF 绕过 / 反序列化 RCE |
| Jackson Databind | WAF 绕过 / SQL 注入 |
| Fastjson | WAF 绕过 / 反序列化 RCE |
| Apache Tomcat | 文件上传绕过（Webshell） |
| Spring Framework | URL 解码绕过 / 路径穿越 |
| Jetty | URL 解码绕过 / CRLF 注入 |
| Undertow | URL 解码绕过 |
| Vert.x | URL 解码绕过 |
| Angus Mail | SMTP 注入 |
| Apache HttpClient（≤ 4.5.9） | HTTP 请求走私 |
| ActiveJ | HTTP CRLF 注入 |
| Lettuce（Redis 客户端） | Redis 命令注入 |
| Jodd | 路径穿越 |
| XMLWriter | XML 标签注入 |

### 借 Ghost Bits 二次绕过的真实 CVE

* **GeoServer CVE-2024-36401**

  （CVSS 9.8）—— Ghost Bits 变体 Payload 直接 RCE
* **Spring4Shell（CVE-2022-22965）**
* **Openfire CVE-2023-32315**
* **Spring Framework CVE-2025-41242**

  （上文实战示例）

利用门槛低，POC / EXP 已公开，建议尽快完成自查修复。

## 五、修复与缓解

### 升级修复方案

请关注上述各受影响组件的官方 Security Advisory，升级至已修复版本。重点关注：

* **Apache Commons BCEL：升级至 6.12.0 及以上版本**
* **Fastjson：升级至 2.x 系列最新版本**
* **Apache HttpClient：升级至 4.5.10 及以上版本，或迁移至 HttpClient 5.x**
* **GeoServer：升级至 2.28.3 及以上版本**
* **Openfire：升级至 5.0.4 及以上版本**

### 临时缓解方案

* **WAF 规则**

  基于字符串特征的 WAF 规则对 Ghost Bits 变形 Payload 防护效果有限，建议在解码层面进行语义检测，或引入 Unicode 规范化（NFC / NFKC）预处理后再执行规则匹配。
* **代码层面**

  排查自研代码中 `(byte)ch`、`ch & 0xFF`、`baos.write(ch)`、`DataOutputStream#writeBytes()`等写法。
* **输入验证**

  对关键字段（文件名、邮件地址、URL 参数、JSON 键名等）严格过滤非 ASCII 字符或进行 Unicode 归一化处理。
* **网络层面**

  暴露在公网的 Java 应用服务，在完成代码修复前限制访问来源，降低攻击面。

## 六、Secrux-GhostBits-Scanner · 社区版专项扫描工具（开源 · 免费）

议题正式发布前，由于 Secrux 平台的高度可拓展性，一句话就能定制对 Ghost Bits 的定制化专项检测，我们率先使用 Secrux 平台对多个开源项目进行了扫描，并发现了大量由人工检查时遗漏的攻击点。相关能力早已在本次 Black Hat 议题研究中完整落地体现，实现技术研究与产品能力同步赋能。

与此同时，**御之安**先驱实验室同步开源了 **Secrux-GhostBits-Scanner**—— Ghost Bits 社区版专项扫描工具，由 **御之安先驱实验室的 SpringKill（Zongzheng Zheng）、浅蓝（Xinyu Bai）**共同研发。

工具能力一览：

* **代码层扫描**

  扫描自研 Java 代码中所有典型的 Ghost Bits 模式（`(byte)ch`、`ch & 0xff`、`baos.write(ch)`、`DataOutputStream#writeBytes()`等），定位高危转换点；
* **依赖层扫描**

  扫描自研 Java 项目中包含的第三方依赖，内置 CVE-2025-41242、Jackson、Fastjson 等常见场景预设；
* **结果输出**

  风险文件清单 + 高危转换点行号 + 上下文片段 + 目标资产命中报告；
* **本地运行**

  无需上传源码到云端，离线可用，附带使用文档与修复参考。
* Web & CLI 双模

  支持使用 Web 或 CLI 的形式对项目开展扫描。

**工具 Web 界面：**

![](https://mmbiz.qpic.cn/mmbiz_png/txKdUNHV69OhR1u0JdxD9XPgFyeDwR7FQ864sxJxFnPXYqNZ36sqC0KLicribkgEE2HR39gwbiccJK3rjsHiaIygv58uIOsSoBSOX1kDYaPO4nk/640?wx_fmt=png&from=appmsg)

Secrux-GhostBits-Scanner Web 界面

**命令行界面：**

![](https://mmbiz.qpic.cn/mmbiz_png/txKdUNHV69O85vFTeficvvzp5RicrP8KHKeDnCK4xujqrNoORmBNyUNSJS1R3LiarUtT9L0zc71sZ1RDZnQwKicSnY537dGXz5BnBG4f37k22N4/640?wx_fmt=png&from=appmsg)

Secrux-GhostBits-Scanner 命令行界面

它的能力没法和 Secrux 平台的全栈数据流追踪相比，但应付那个最急的问题 —— **你代码里到底有没有 Ghost Bits 模式？目标资产到底有没有受影响？**—— 绰绰有余。

**社区版专项工具与 Secrux 平台能力对比：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/txKdUNHV69Og4kI4UrVRL8SjleZYdrxzCCYfOM8eh5iakxh3nLME2hP3H7hre3llXdKNjProxyG1ejRrsfmzSThF7C7BMgQsq1ic9NrwAtyZI/640?wx_fmt=png&from=appmsg)

Secrux-GhostBits-Scanner 与 Secrux 平台能力对比

获取方式：

* **GitHub**

  https://github.com/GeetoRinku/Ghost-Bits-Scanner

## 七、Secrux 人工智能代码审计平台

对于希望进行体系化、跨函数 / 跨文件数据流追踪的代码审计场景，**Secrux 人工智能代码审计平台**已第一时间内置 Ghost Bits 检测策略包。

Secrux 是御之安自研的 AI 驱动代码审计平台，已经在金融、央国企、大型互联网客户的代码安全审计场景中长期商业化交付。它真正想解的是更大一档的问题：把代码里所有需要"读懂语义才能识别"的安全缺陷，让平台自动看见。Ghost Bits 在 Secrux 眼里只是一个具体例子。

我们在议题公开的 **第一时间**把 Ghost Bits 检测能力内置到 Secrux，原因很朴素 —— **议题演讲者浅蓝（Xinyu Bai）就是御之安先驱实验室研究员，与 Secrux 平台核心开发者 SpringKill（Zongzheng Zheng）同属一支团队**。从研究阶段开始，模式特征、误报点位、未在议题展开的边界 case，就在实验室内部完成同步。这种"研究方和产品方是同一支团队"的协同节奏，是其他厂商等议题公开后再回去补检测规则、追不上的。

具体到 Ghost Bits 这类问题，Secrux 的能力优势：

* **跨函数 / 跨文件的数据流追踪**

  单点扫描看不出问题，Secrux 会把数据从入口（Controller、反序列化、文件读入）一路追到 `byte[]`转换点，识别"未做高位校验的污染数据流"；
* **语义级模式识别**

  模型理解"为什么 `(byte)ch`在某些上下文里安全、在另一些里致命"，避免传统 SAST 的高误报；
* **批量复盘 + 持续监测**

  可对接 CI / CD，每次提交即审，新代码引入 Ghost Bits 模式立刻预警；
* **第三方组件扫描覆盖**

  上述 14 个受影响组件 + 自研代码做体系化检测。

**Secrux 平台已完成 Ghost Bits 漏洞检测能力升级：**

**主仪表盘：**

![Secrux 平台主仪表盘](https://mmbiz.qpic.cn/sz_mmbiz_png/txKdUNHV69PhJJkFUfp8DHNGmpTIWD0NZeIrkeibX6esEMGSQz6PnwQnld0H3iaesfayu1rRcYF5QS07x2hqYibGRElZUhwQ8ejvg00A6XowjE/640?wx_fmt=png&from=appmsg)

Secrux 平台主仪表盘

**漏洞管理：**

![Secrux 平台漏洞管理 · Ghost Bits 风险闭环](https://mmbiz.qpic.cn/mmbiz_png/txKdUNHV69NNz5ALwaUKfTFWeQwDkhEbkFFK9nudyoK5QnnZ2etiaYrVnqR4yZX5GFU9QkwafgG9w2DpPfyRSUAtB0U9AqBon6GVXqwmicJwc/640?wx_fmt=png&from=appmsg)

Secrux 平台漏洞管理 · Ghost Bits 风险闭环

**代码审计发现真实 Ghost Bits：**

![](https://mmbiz.qpic.cn/mmbiz_png/txKdUNHV69OiaFuoogicCiaeJCUgAVEMs9S0W4KYEhNe9tD06xdicjdWnM16LKib4uH1gBSXrpr4iatkNgoOfaOIGNQh79JM09HQxWsd28YgDJIYM/640?wx_fmt=png&from=appmsg)

Secrux 平台代码审计 · Ghost Bits 检测

> 我们对 Secrux 的定位很朴素：把那些"以前只有专家凭经验才能看出来"的语义级代码缺陷，沉淀成平台能自动跑出来的东西。"找了多少 CVE"从来不是它的 KPI。

**预约试用 / 商务咨询 / 应急对接：**

* 公众号后台回复 **「Secrux」**，1 个工作日内由商务同学对接；
* 直接联系：cl4y@yuzhian.com.cn。

## 写在最后

Ghost Bits 短期内不会被"修完" —— 根治需要 Java 生态上下游对字符编码安全的集体重新校准，那是个慢工。在那一天到来之前，**早一天看见，早一天止血**。

御之安先驱实验室会持续披露此类系统性攻击面，也会持续把研究成果沉淀进 Secrux 的产品能力里。

## 关于御之安先驱实验室

御之安先驱实验室，是御之安科技旗下国际一流的 **AI 安全专业团队**。秉持「守护无声，保障万象」核心使命，深耕 **AI 安全全栈一体化解决方案**领域，致力于为政企及全球用户提供前沿、完备、可靠的 AI 安全体系服务，全方位抵御人工智能领域网络与信息安全风险，筑牢智能时代安全屏障。

> **关于成都御之安科技有限公司**
>
> 聚焦人工智能安全核心赛道，打造**"AI 安全 + 数据安全"**双核心政企安全防护体系。
>
> 核心团队来自腾讯科恩实验室、字节无恒实验室等顶尖安全机构，深耕网络安全领域十余年，曾登上 BlackHat 等国际顶级安全峰会，主导开源项目斩获 GitHub 万星认证，TC260 WG9（网络安全标准化技术委员会 第九工作组）成员单位。
>
> 旗下产品矩阵：CyberEdge、SoulBind、虚影、Secrux。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mm...