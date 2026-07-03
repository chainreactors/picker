---
title: 【论文分享】你的\"空间\"成了攻击者的\"地盘\"：预训练模型平台上 AI 应用的安全风险研究
url: https://mp.weixin.qq.com/s/NHog1bNpBxUUoMqOGrdd3w
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:45:45.966512
---

# 【论文分享】你的\"空间\"成了攻击者的\"地盘\"：预训练模型平台上 AI 应用的安全风险研究

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QSjGzxHEMdtkrXsoWwnK9ZuSDXKxLTuhdU9VWWL0XH0QLOyYzgy3RrbrqPS1ibdTiclPt8U7rw4icO5iaHd6B8KGJv7MbtWJukYDTB8TLkGFA34/0?wx_fmt=jpeg)

# 【论文分享】你的"空间"成了攻击者的"地盘"：预训练模型平台上 AI 应用的安全风险研究

星图实验室
星图实验室

奇安信技术研究院

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/QSjGzxHEMduA7VZwzWBJRMb5tT3dwonCEojwHkAlj3Z6ibQw5Gly833B1wDhDNqtic4mhiajLMDVyOena50lQlCAx5Y2ib9o72onBqg1Nr8NPLI/640?wx_fmt=gif&from=appmsg)

**引言**

在 Hugging Face、Replicate、ModelScope 这些主流预训练模型平台上，把模型封装成"开箱即用"的在线 **AI****应用（AI-App****，在 Hugging Face****上被称为 Space****）** 已经很常见。用户无需本地显卡、无需配置环境，打开浏览器或调用 API 就能做推理和微调。截至 2025 年 12 月，仅 Hugging Face 一家就托管了超过 **93****万** 个公开 AI 应用。

这类应用降低了使用门槛，但也带来一个容易被忽视的问题：它们大多由**第三方开发者**编写，运行在共享环境中，平台对它们的隔离和配置约束相对薄弱。近年已有相关安全事件——Hugging Face 官方的一个模型转换应用存在漏洞，攻击者可借此冒充转换机器人、操纵任意应用；Replicate 曾因给多个应用错配共享网络，使攻击者可通过恶意应用操纵推理或窃取私有模型；2024 年 Hugging Face 也检测到未授权访问，导致多名用户的密钥被泄露。

本论文由清华大学与奇安信星图实验室联合完成，被网络安全国际四大顶会之一的 **ACM CCS 2026** 录用，题目为《**Your Space is My Zone: Demystifying the Security Risks of AI-Powered Applications on Pre-Trained Model Hubs**》。我们围绕 AI 应用这一新场景做了一次较为系统的安全分析，并实现了分析框架 **INSIGHTOR**，对三个平台共计 **972,546** 个公开 AI 应用做了实测。

论文链接：https://arxiv.org/abs/2606.30373

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QSjGzxHEMdsF3ITfNrMlLznTQYUeKjkuia9nnJWMND8bra8HNGfC4Jyotl2gc8uLsVIYAFWdmgPibT6HK7GSEuRRSnQRJy2NGzrp9PwIWRnqw/640?wx_fmt=jpeg&from=appmsg)

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/QSjGzxHEMdvcIOfyCjjre1YXREQT2jQGANrb6sd1ddUqBLr5GNsfFhfBnyH39S3ycjy8oEk57VRsWHHIGgPCffXCnro3TXy74S3TGxP4D3I/640?wx_fmt=jpeg&from=appmsg)

**PART.01**

![](https://mmbiz.qpic.cn/mmbiz_gif/QSjGzxHEMdt8C1UicXACpx362etv6OpiaqUBmvicaRgJPKBX9rbFMsmqxTI0DMOVMKFxBcnibZeicS2iaUFGA5tWBlGewdke6jYtHjb525ZqWrdA0/640?wx_fmt=gif&from=appmsg)

**AI应用是什么，问题出在哪？**

不同于需要本地部署的模型，AI 应用把**预训练模型、运行环境、推理****API****和 Web****界面**打包成一个云端服务。其典型生命周期是：开发者在平台上创建一个带全局唯一标识符（如 username/spacename）的应用，可以从零写代码、套用官方模板，也可以像 GitHub 上 fork 那样直接复制（Duplicate）他人的应用；平台随后自动构建容器镜像、分配资源并上线；用户通过浏览器或 API 访问。

由于平台文档普遍不够完整，我们用三种互补的方法弄清实现细节：**审阅平台文档、分析开源组件（如****Hugging Face****的 AutoTrain****、Replicate****的 Cog****），以及黑盒测试**——部署一个会把用户输入当 shell 命令执行的测试应用，抓包观察运行环境、环境变量、网络隔离和密钥处理。

我们发现，AI 应用与普通 Web 应用最关键的区别在于：**AI****应用本质上是开发者自建的 Web****服务器，再通过 iframe****嵌入到平台主站页面中。**

正是这种"平台页面嵌第三方 iframe"的架构，加上跨用户共享运行环境、无状态令牌认证、世界可读日志、代码自由复制等机制，构成了新的攻击面。需要说明的是，我们关注的是**承载模型的共享基础设施和集成逻辑**，而非模型本身的数学性质，因此提示词注入等模型层攻击不在讨论范围内。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QSjGzxHEMdvyFDXhXLKVdJ2YZIetmoupUgK5p3BW1wmkcnQj8MiaMPZ7zmQkiaPW66VdUT4psAWicOC5METOicw1K8iaDdFozeyrzBpIaDxClGww/640?wx_fmt=jpeg&from=appmsg)

图 1 AI应用架构

---

**PART.0****2**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/QSjGzxHEMdsFWPyf1ibXxAQg0MYFD6IrbLGZlEtzib0yeN9MCymcLSFqKoCb6wMEHDicDkIW406xqwdgLxeEQR6w7cpS25iaQNLlibVyDBOJu9PQ/640?wx_fmt=gif&from=appmsg)

**研究方法：对照成熟风险框架梳理威胁**

为了尽量不遗漏地找出风险，我们按以下步骤梳理：先**枚举安全关键接口**（密钥处理、令牌传递、iframe 嵌入、日志、存储等），再**优先看高影响、可实战利用的向量**（如数据窃取、远程代码执行），最后**对照标准框架**——把每个攻击向量映射到 **OWASP Web Top 10****、OWASP LLM Top 10** 和**软件供应链攻击分类法**，对应 AI 应用"既是 Web 应用、又是带复杂依赖的组合系统"这一双重属性。

最终我们归纳出 **5****类威胁、10****种攻击向量**。其中 3 种此前未被报告、由平台架构设计直接导致——**幽灵令牌（****Ghost Token****）**、**认证绕过（****Authentication Bypass****）** 和 **标识符复用（Identifier Reuse****）**；其余几种是传统 Web 漏洞在 AI 应用场景下被放大的形式。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QSjGzxHEMdvvZbQld0sHBKRChWFAtUriaW1qGGal8UTHlfe4u4qOegiaTDTm8ZWtdbu3WvAjKT8bLfypuF6fEbicT0jFKrQVsloUH3rsRYw6sU/640?wx_fmt=jpeg&from=appmsg)

图 2 五类威胁 × 10 向量 × 三平台对照表

---

**PART.03**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/QSjGzxHEMds3D6MPbxDf2MicEGhUC7yrZqJiaW8YNibjBggoEEDVRZ9JrDt4rHU3JDEtc0hEAic6eib6lfa5gkbJWjZJNBIA2xpulrUtBRBcE9UU/640?wx_fmt=gif&from=appmsg)

**主要攻击向量分析**

### 3.1 访问控制失效

**▶****幽灵令牌（Ghost Token****，A2****）**

Hugging Face 用**无状态的****JWT****令牌**为私有应用做认证，签发令牌的 APIjwt 接口对所有人开放。问题在于：当应用归属发生变化（被删除、用户名被重新注册）时，平台**不会让此前签发的令牌失效**。于是攻击者可以预测某组织未来会用的应用标识符（例如盯上在 GitHub 活跃、但尚未入驻 Hugging Face 的组织），抢先注册用户名、创建私有应用、生成有效期 24 小时的 JWT，再删除账号和应用、靠免费账号反复"创建—删除"维持令牌有效；当该组织日后注册同名账号并创建同名应用时，攻击者此前持有的令牌**仍能访问其私有应用**。

可行性方面我们给出了数据：在 49 万有应用的 Hugging Face 用户中，8,462 个是组织账号，其中 **51.16%** 与现存 GitHub 组织同名；重叠账号下 **4.88%** 的应用名与对应 GitHub 仓库名完全一致——说明标识符在一定程度上可预测。

![](https://mmbiz.qpic.cn/mmbiz_jpg/QSjGzxHEMdvRsHXmibR1JJ6iclJ58sckbD9gR6KGSPibPVm39OnY1JvMicwR9LTp542j3GfaVID8ZD2bNXdchwI1jgCHiciadicyXFs0QiaLhWUfShs/640?wx_fmt=jpeg&from=appmsg)

图 3 AI应用的认证流程

**▶****日志渗漏（Log Exfiltration****，A1****）**

运行时日志常会无意记录敏感数据。我们发现，Hugging Face 和 Replicate 虽在界面上隐藏了日志查看按钮，却把公开应用的运行日志配置成了**世界可读**。Hugging Face 那个公开的日志 API 还能为任意公开应用签发可读取完整日志的 JWT，结果是**任何****Hugging Face****用户都能读取任意公开应用的运行日志**。Replicate 也有类似问题，但因任务标识符是 26 位随机串、无法枚举，实际可利用范围有限；ModelScope 只允许管理员访问日志，不受此影响。

**▶****认证绕过（Authentication Bypass****，A3****）**

部分开发者把**口令直接写死在源码里**做访问校验（如 Replicate 上的 ardianfe/stable-audio-prod，直接比对用户传入的 key 与硬编码字符串）。但密码就在容器镜像的源码里，攻击者拉下镜像即可读到，这种"锁"起不到保护作用。

**▶****过度授权 iframe****（A4****）**

Hugging Face 默认给每个应用的 iframe 授予多达 27 项权限，包括摄像头和麦克风。当用户给一个可信应用授权后，**同一会话中后续加载的应用会继承这些权限**，不再重新询问。也就是说，用户先给一个正常应用授权了摄像头，之后加载的另一个应用就可能在不弹窗的情况下访问摄像头。实测中，21,444 个（2.28%）应用至少请求了一项浏览器权限。

### 3.2 资源复用缺陷

**▶****标识符复用（Identifier Reuse****，R1****）**

Hugging Face 给应用生成子域名时，会把标识符里的斜杠 / 换成连字符 -（如 user/space-name → user-space-name.hf.space）。但**用户名本身也允许带连字符**，于是 user/space-name 和 user-space/name 会**映射到同一个子域名**。据此可发动一种域名接管：攻击者预先注册 user-space 这类账号并蹲守目标应用被删除。一旦原应用被删，那些已嵌入第三方网站的 iframe 就成了指向无主子域名的悬空链接；攻击者随即创建 user-space/name 占用该子域名（此时平台不再追加随机后缀），于是原本正常的 iframe 开始从 Hugging Face 官方域名加载攻击者的内容。这种情况下网站方无需改动代码、也很难察觉，可被长期用于钓鱼和凭据窃取。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QSjGzxHEMdsboFCyzjSuUxjAibdgmUdWeRSiaa2vKTeXiaib9dJx3bmT1FeY1YZyh6s4GDKpct34GhTGQoJu9QQ3QOBcicuIT9Sb1053gFjNRrW0/640?wx_fmt=jpeg&from=appmsg)

图 4 标识符复用攻击原理

数据上：93.8 万个 Hugging Face 应用中，**47.03%** 标识符含连字符，其中 **99.79%** 至少存在一个可被抢注的冲突用户名；30 天监测期内观察到 **5,069** 次应用删除；我们还确认了 **9****个**正在嵌入"已删除且可被劫持"应用的真实网站（论文指出这是测量下界）。

**▶****代码投毒（Code Poisoning****，R2****）**

AI 应用的代码可通过两种方式传播：一是用户**显式复制**；二是更隐蔽的**隐式复制**——Replicate 上用户一旦使用某应用的训练功能，平台会自动在其账号下生成一个继承原始源码的新应用，且不通知开发者。这意味着一个带后门的应用，可以等待他人复制、或在不知情中触发复制，从而扩散。

### 3.3 输入校验不足（V1）

作为 Web 应用，AI 应用同样面临输入注入，风险来自两方面：一是开发者**未对用户输入做净化**（如把用户传入的文件路径直接拼进 os.system() 调用的 ffmpeg 命令）；二是依赖了**存在已知漏洞的第三方****SDK**——以广泛使用的前端库 Gradio 为例，它曾出现多个代码注入 CVE，会波及依赖它的应用。

### 3.4 敏感数据泄露（L1 / L2）

* **运行时日志泄露（L1****）**：在多用户共享的日志里，我们识别出三类被泄数据——无意打印的**密钥**、Hugging Face 用于认证的 **JWT****令牌**、以及包含 **LLM****提示词**在内的用户输入/输出，对应 OWASP LLM02（敏感信息泄露）与 LLM07（系统提示词泄露）。
* **容器文件泄露（L2****）**：源码里的硬编码凭据，以及自定义基础镜像中夹带的私有密钥，都会随镜像分发而泄露。

### 3.5 算力劫持（Cryptojacking，P1）

AI 应用依赖高性能 GPU，在"用户付费"计费模式下、或用户把应用拉到本地运行时，攻击者可把挖矿程序藏进看似正常的应用里——应用照常输出结果，同时占用受害者的 GPU 挖矿。

---

**PART.04**

![](https://mmbiz.qpic.cn/mmbiz_gif/QSjGzxHEMdseQAm2Y6SVwFVtOVXucibDnzFgSWk5586kuqOjATlyyC5RkiaTNWKcKbticXxHobpXtd66kxpcb4OIWnrQcqVIoZiaXOD4zPvsAFM/640?wx_fmt=gif&from=appmsg)

**INSIGHTOR：大规模测量框架**

发现攻击向量之后，还要回答影响范围有多大，为此我们实现了分析框架 **INSIGHTOR**。

**数据采集**：针对三个平台各自的接口差异定制采集策略，最终收集到 Hugging Face **938,602** 个、Replicate **25,340** 个、ModelScope **8,604** 个应用，以及它们的源码仓库、容器镜像和元数据，时间跨度为 2024 年 9 月至 2025 年 12 月。

**检测方法**：INSIGHTOR 采用混合策略——对幽灵令牌、标识符复用、过度授权 iframe 等**架构****/****配置类**问题，用预定义规则结合元数据扫描；对**输入注入**和**敏感数据泄露**这类需深入分析的问题，基于 **CodeQL** 做**数据流（污点）分析**，把 predict()、Gradio Textbox()、Streamlit 输入等作为"源"，把 os.system、eval、print、logger.\* 等作为"汇"，追踪从用户输入/密钥到危险函数或日志的可达路径；对供应链风险和硬编码密钥，复用成熟开源扫描器 GuardDog 与 KeySentinel。

INSIGHTOR 的作用是一个**筛选器**，把人工核查的搜索空间从 97 万个应用缩小到可复核的候选集。它属于静态分析，存在精度与召回的取舍，结果以人工抽样验证，不保证逐例精确。

---

**PART.05**

![](https://mmbiz.qpic.cn/mmbiz_gif/QSjGzxHEMdtr3MOpYmte9JMn5E0h2vHefeUNU5icWmaDlRiavgVsgIQhllDghXmS8XibD74hOzDT1NF37KyTfHz8aCzrQb53RJhcCMpDOMRaEA/640?wx_fmt=gif&from=appmsg)

**测量结果**

* **输入注入**：识别出 **1,442** 个潜在注入点，抽样 300 例人工确认 83 例为真实漏洞（精度约 27.67%），最常见的是把用户输入直接拼进 os.system()、eval()（CWE-78）。
* **过时 SDK**：**139,475**（14.34%）个应用使用了含已知 RCE 漏洞的过时 Gradio；这是基于版本的暴露面统计，反映补丁滞后程度，并不等于每个都可被利用。
* **密钥泄露进日志**：在遵循官方密钥管理规范的前提下，仍有 **936** 个应用因日志配置把密钥写进了世界可读日志（抽样 500 例确认 94 例）。用户输入方面，**9,372** 个应用记录了用户输入，其中 61.41% 涉及提交给 LLM 的提示词，少数还涉及医疗等敏感数据。
* **硬编码令牌**：在 4,846 个...