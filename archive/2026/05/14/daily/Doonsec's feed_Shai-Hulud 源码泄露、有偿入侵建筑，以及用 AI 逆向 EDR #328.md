---
title: Shai-Hulud 源码泄露、有偿入侵建筑，以及用 AI 逆向 EDR #328
url: https://mp.weixin.qq.com/s/bJtQNXCA7eG6Jxe5NAAWnA
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:46:45.589657
---

# Shai-Hulud 源码泄露、有偿入侵建筑，以及用 AI 逆向 EDR #328

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSjXPQrNsEoMKId6zic0G5N1Jtfjact27CibnfPL4AIXicvXDaukH7J2mIOQC2YzSibLcIvlHDhEfoFENSAFkFtaPrGd9qUB6AhIqFQ/0?wx_fmt=jpeg)

# Shai-Hulud 源码泄露、有偿入侵建筑，以及用 AI 逆向 EDR #328

Clint Gibler
Clint Gibler

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## TeamPCP 攻击框架拆解；物理渗透测试职业问答；AI 终结"不透明防御"假设

2026 年 5 月 14 日

---

## My Least Favorite Type of Tan(Stack)

先向所有正在疲于应对又一波供应链攻击的朋友送上 #HugOps，希望你们能得到足够的支撑。

---

## AppSec

V4bel/dirtyfrag

通用 Linux LPE 漏洞类，由 Hyunwoo Kim 发现。串联 xfrm-ESP 和 RxRPC 两个页缓存写入 bug，无竞争条件即可确定性拿到 root，覆盖 Ubuntu、RHEL、Fedora 和 openSUSE。

Copy Fail 漏洞：五条 YARA 检测规则

CVE-2026-31431，Linux 内核 LPE。非特权用户可向任意可读文件内存副本写入 4 字节（比如 `/usr/bin/su`），足以干掉密码校验直接拿 root shell，磁盘文件纹丝不动，文件完整性工具完全看不见。2017 年后所有主流发行版中招，多租户服务器、CI/CD 和容器集群风险最高。一天内野外已冒出十几种变体。ReversingLabs 围绕漏洞核心加密字符串构建了五级 YARA 规则集。技术细节见 copy.fail 和原始 PoC，另有 Microsoft 补充分析。

microsoft/AntiSSRF

Microsoft 开源的默认安全库，防护云应用中的 SSRF（服务端请求伪造），覆盖 HTTP 重定向和 DNS 重绑定绕过，支持 .NET 和 NodeJS。配套发布动态验证工具 Dusseldorf。

要我在"吃最爱的甜点"和"获得一个消灭整类漏洞的默认安全库"之间选——我选后者。刚出炉的苹果酥饼再香也就那一口，而从根上斩断一类漏洞，那满足感是永久的。多来点这样的东西。

---

## Cloud Security

BigQuery 威胁模型报告

Google Cloud 发布 BigQuery 威胁模型，14 种攻击向量映射至 STRIDE 和 MITRE ATT&CK，涵盖 schema 篡改、服务账号伪冒、导出任务数据外传、隐蔽 IAM 绑定持久化和成本型 DoS。缓解措施：最小权限 IAM、VPC Service Controls、Cloud Audit Log 监控（`SetIamPolicy`、`datasets.patch`）、Workload Identity Federation。

多 SSO AWS Cognito 用户池的安全隐患

Doyensec 分析了单个 Cognito 用户池挂多个外部 IdP（OIDC/SAML）时的攻击面，找到四条路径：JIT 幽灵身份创建、Unicode 同形字提供方碰撞、用户名解析攻击、IdP 标识符劫持。根因都一样——tenantID、role 等安全敏感属性直接从攻击者可控的联合令牌里读。配套发布武器化测试工具 maSSO 及 Terraform 实验环境。另见工具集 doyensec/cloudsec-tidbits。

---

## Supply Chain

Mini Shai-Hulud 再度来袭：TanStack 等 npm 包遭入侵

Wiz 拆解 TeamPCP 最新攻击链，受害者包括 TanStack、UiPath 和 Mistral AI。攻击者 fork 仓库并重命名规避检测，通过 `pull_request_target`触发工作流并投毒 pnpm store 缓存；合法维护者 PR 合并后发布工作流恢复了被污染的缓存，攻击者直接从 runner 进程内存提取 OIDC 令牌发布恶意包——全程无需偷 npm 凭据。文章附 IoC、检测和修复步骤。社区检测工具：Tanstack-Worm-Detector、mini-shai-hulud-ioc-scanner。

Shai-Hulud 开源了

Datadog 对 TeamPCP 短暂公开于 GitHub 的 Shai-Hulud 完整源码做了静态分析。这套 TypeScript/Bun 模块化工具包能力覆盖：从 100+ 文件路径收割凭据；通过 `/proc/<pid>/mem`提取 GitHub Actions Runner 进程内存；跨 17 个区域枚举 AWS Secrets Manager/SSM；混合加密外传至 `git-tanstack[.]com`或 GitHub dead-drop 仓库；伪造完整 Sigstore 来源证明（Fulcio + Rekor）；通过 VSCode tasks 和 Claude Code `SessionStart`hook 持久化；令牌一旦被吊销就触发自毁开关（`rm -rf ~/`）。可识别出 TeamPCP 22 个 TTP 中的 19 个。

说实话，工程质量相当用心。

---

## Blue Team

ridgelinecyberdefence/vanguard

单一 Go 二进制打包完整 IR 工具链，集成 Velociraptor、Volatility、KAPE，附 28 个 MITRE 映射的 IR 用例。支持 Windows/Linux，内置案件管理、防篡改证据处理，支持气隙环境。

gadievron/honeyslop

代码金丝雀集合，通过植入唯一 UUID、伪造函数名（如 `zqx_tarnish_v3`）和虚构的 CVE-2025-99919，识别 AI 幻觉生成的漏洞报告。

"随手搞的快速 PoC，vibe-coded 当玩笑，非生产级"——但这思路我很喜欢。

referefref/OpenAIPot

OpenAI 兼容 API 蜜罐：有效密钥透传，诱饵密钥触发提示词替换并注入欺骗内容，重复尝试触发 IP 封锁并返回逼真的 token 耗尽报错。日志接入 SIEM 和 Slack，映射至 MITRE Engage。

---

## Red Team

我们靠有偿入侵建筑为生。随便问！

TrustedSec 的 Paul Koblitz、Costa Petros 和 David Boyd 在 Reddit 做的物理渗透测试职业 AMA。

重新定义 Agentic 时代的 AI 红队测试

Dreadnode 发布 Agentic AI 红队系统，基于开源 SDK（45+ 攻击策略、450+ prompt 变换、130+ 评分器）。操作者用自然语言描述目标，Agent 自动选攻击手法、跑工作流、输出结构化报告——这些就是你现在用 PyRIT/Garak/Promptfoo 手动编排的那些活。针对 Meta Llama Scout 案例：3 小时、674 次攻击、零代码、85% 成功率、232 个严重发现。不用任何 jailbreak 直接问，有害内容产出率仍达 80%。完整方法论见 arXiv 论文。

防御栈已暴露：LLM、逆向工程与"不透明防御"的终结

TrustedSec 的 Justin Elze 把 LLM 怼向五款商业 EDR，发现搞清楚 EDR 内部逻辑这件事已经从"熟练逆向工程师花数周"变成"配合正确工作流花数天"。五款产品都一样好使，因为构建方式趋同：YARA 规则、行为逻辑、允许列表、脚本引擎（有些一把解密就是可读 Lua）、本地 ML 分类器——全部驻留在宿主机上。规则和阈值可直接提取，排除列表暴露监控盲区，更新差异暴露厂商悄悄修的东西。参见 EDR 逆向 Skill 及完整工作流。

防御建议：攻击者研究不到的层才靠谱——主机加固（WDAC、ASR、LSA Protection）、基于原始遥测而非 EDR 裁决构建 SIEM 检测、Entra ID 身份层检测。

> "大量防御工具的构建前提是其内部逻辑对攻击者保持不透明。防御栈正在成为攻击面的一部分。"
>
> — Justin Elze

好文章。对正在改变的安全假设点得很准，防御方行动建议那段尤其扎实。

---

## AI + Security

distil-labs/distil-ai-slop-detector

Chrome 扩展，用 242MB 精调模型（Gemma 3 270M）在浏览器本地检测 AI 生成文本，附 Claude Desktop Skill 和 CLI 支持训练自定义分类器。

Daybreak：面向网络防御者的前沿 AI

OpenAI 发布 Daybreak，定位类似 Project Glasswing，强调将安全代码审查、威胁建模、补丁验证、依赖风险分析融入开发循环。合作伙伴包括 Cloudflare、Cisco、CrowdStrike、Palo Alto Networks 等。

Agentic AI 跑起来可能搞出一堆乱子这事，现在关注动态强制最小权限的安全态势策略确实挺重要的。

Mythos 发现了一个 curl 漏洞

Daniel Stenberg 拆了 Mythos 扫描 curl 17.8 万行 C 代码的结果：五个"已确认漏洞"，人工过完——三个是文档里写明的 API 行为，一个"只是个 bug"，就一个最后成了低危 CVE。跟之前 AISLE、Zeropath、OpenAI Codex Security 的结论一致：AI 工具擅长抓已知类型错误，新型 bug 还不行。

> "这个模型迄今的巨大炒作，主要是营销。"

幕后：用 Claude Mythos Preview 加固 Firefox

Mozilla 在现有 fuzzing 基础设施上搭了套 Agentic 框架——自动写可复现测试用例、跨临时虚拟机集群扩展、集成安全生命周期。跑 Claude Mythos Preview 在 Firefox 150 里找到 271 个 bug，含 fuzzer 覆盖不到的沙箱逃逸、竞争条件和 use-after-free。审计日志同时验证了现有防御——模型反复尝试 prototype pollution 沙箱逃逸，都被原型冻结架构挡回去了。后续计划接入 CI 实时扫描落地补丁。

目标特化（target-specific）框架叠加强大底层模型能带来多大额外价值——这是个很好的示范。架构层面消灭整类漏洞那段也很值得学。

---

## Misc

* ScreenX，270 度视野的未来电影院
* 如何创立一个狂热社群 | Lulu Cheng Meservey
* facebookincubator/below — 现代 Linux 时间旅行式资源监控工具
* GitLab Act 2 — GitLab 宣布重组，大概率裁员
* Cloudflare 裁掉约 1100 人（20%），备战 "Agentic AI 时代"
* Claude 用于创意工作 — Anthropic 发布 MCP 连接器，集成 Blender、Adobe Creative Cloud、Ableton 等
* 面向金融服务的 Agent 模板 — 十个金融工作流 Agent 模板，代码库：anthropics/financial-services

---

## 总结建议

* Shai-Hulud 以 MIT 许可开源，仿冒变体已在扩散，发动同等能力供应链攻击的门槛降至"克隆、改、部署"；应立即轮换所有开发者凭据，审计 GitHub Actions 的 `pull_request_target`触发器和缓存投毒风险。
* CVE-2026-31431（Copy Fail）无竞争条件、绕过文件完整性检测、野外变体已逾十种；应立即在多租户服务器、容器集群和 CI/CD 节点打补丁，将五级 YARA 规则集导入检测管道。
* LLM 辅助逆向已将商业 EDR 的内部逻辑从"不透明资产"变为可分析攻击面；应将检测逻辑迁移至原始遥测层，优先加固 WDAC/ASR 主机层与身份层，减少对 EDR 裁决的单点依赖。
* AI 漏洞扫描的实际价值取决于目标特化程度——通用扫描信噪比低，Mozilla 式针对性框架产出显著更高；引入此类工具前应建立人工复核机制，防止原始 AI 输出直接灌入漏洞管理流程。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

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