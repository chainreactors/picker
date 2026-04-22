---
title: Anthropic MCP 设计漏洞可导致 RCE，威胁 AI 供应链安全
url: https://mp.weixin.qq.com/s/ZrAjye39hq8Olut8hrh5rw
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:41:51.382618
---

# Anthropic MCP 设计漏洞可导致 RCE，威胁 AI 供应链安全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQuoJibNce8dlpAMTvqm21iaKUXsfFGTCs9y03jFZZUgVLrh0SDAU6C0fGKxrxZAHqh8SPia88JeHUDg/0?wx_fmt=jpeg)

# Anthropic MCP 设计漏洞可导致 RCE，威胁 AI 供应链安全

综合编译
综合编译

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)

编译：代码卫士

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRSylJK2k7H6mNqiaS2G6WRaeeK34cLHE6pe9VeOIHYiboAnKB0TMoayZCxFpHMLljzTnz9DnNuFiaqQ/640?wx_fmt=png)

专栏·供应链安全

数字化时代，软件无处不在。软件如同社会中的“虚拟人”，已经成为支撑社会正常运转的最基本元素之一，软件的安全性问题也正在成为当今社会的根本性、基础性问题。

随着软件产业的快速发展，软件供应链也越发复杂多元，复杂的软件供应链会引入一系列的安全问题，导致信息系统的整体安全防护难度越来越大。近年来，针对软件供应链的安全攻击事件一直呈快速增长态势，造成的危害也越来越严重。

为此，我们推出“供应链安全”栏目。本栏目汇聚供应链安全资讯，分析供应链安全风险，提供缓解建议，为供应链安全保驾护航。

*注：以往发布的部分供应链安全相关内容，请见文末“推荐阅读”部分。*

**OX Security****公司发现 Flowise 及多个 AI 框架存在一个严重漏洞，导致数百万用户面临远程代码执行（RCE）风险。该漏洞源于由 Anthropic 开发、广泛用于 AI 代理的通信标准模型上下文协议MCP。与常见的软件缺陷不同，该漏洞源于 Anthropic 官方 MCP SDK（涉及 Python、TypeScript、Java 和 Rust 版本）中嵌入的一项架构设计决策。任何基于 MCP 进行开发的开发者都会在不知情的情况下继承这一风险暴露面，这意味着攻击面并不仅限于单一平台，而是会波及整个 AI 供应链。**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUqyJyfJNfO3mNQXwfE3USBUk7EPh8bJJEEH896ARMvwOxjBOooe0MPrOtnyJgQ8aK1bGE3xmwIvzzlP6o4ZOf02pl5sYlAfkY/640?wx_fmt=gif&from=appmsg)

**MCP 核心架构漏洞**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUAZwPL2eZE9JkuNraZurtfc8dc7SLdyrgvee6nKFsOPHJWkxL55Wxr6iboKiaEvrlJ9cATHqQuDICqlK7KciaaIkl2Mujs7njibOI/640?wx_fmt=gif&from=appmsg)

该漏洞使攻击者能够在受影响系统上执行任意命令，从而直接获取敏感的用户数据、内部数据库、API 密钥以及聊天记录。

研究人员在研究过程中成功在六个生产平台上实时执行了命令。Flowise（广泛使用的开源 AI 工作流构建工具）是受影响最严重的平台之一。研究人员发现了一种针对 Flowise 的“加固绕过”攻击向量，并证明即使配置了额外保护措施的环境，仍然可以通过 MCP 适配器接口被利用。

更广泛的危害范围令人震惊：超过 1.5 亿次下载、7000 多个公网可访问的服务器，以及整个生态系统中估计有 20 万个存在漏洞的实例。截至目前，已发布至少十个 CVE 编号，覆盖以下平台的关键漏洞：LiteLLM、LangChain、GPT Researcher、Windsurf、DocsGPT 以及 IBM 公司的 LangFlow。这些漏洞如下：

* CVE-2025-65720 (GPT Researcher)
* CVE-2026-30623 (LiteLLM) – 已修复
* CVE-2026-30624 (Agent Zero)
* CVE-2026-30618 (Fay 框架)
* CVE-2026-33224 (Bisheng) – 已修复
* CVE-2026-30617 (Langchain-Chatchat)
* CVE-2026-33224 (Jaaz)
* CVE-2026-30625 (Upsonic)
* CVE-2026-30615 (Windsurf)
* CVE-2026-26015 (DocsGPT) – 已修复
* CVE-2026-40933 (Flowise)

如下是已确认四类不同的利用方式：

* 未授权 UI 注入：影响多个流行 AI 框架。
* 加固绕过：针对 Flowise 等“受保护”环境。
* 零点击提示词注入：针对 Windsurf、Cursor 等 AI IDE。
* 恶意 MCP 服务器投毒：测试中成功污染了9 个 MCP 注册中心（共11个）。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUdYPMaavzaxrUgV4tl9LibWcJzRhXvUAaU2ib8zwVa9G7FjM23ZjygsrZWNfuibsFQvXN44FbvqlPF4XMG4WdnIvatYVYo6nGUZw/640?wx_fmt=gif&from=appmsg)

**Anthropic 拒绝协议层面的修复**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWLlMPyqKSCbG9pItOPeWaf7Mz9LT1VXwkvicRoBfXX3QAib6OyChcCrGmepj8HsX63EkCOTPc9Xflv5yNrGsicTVSO9fiaNwgQhR0/640?wx_fmt=gif&from=appmsg)

OX Security的研究人员多次向 Anthropic 建议进行根因层面的补丁修复，本可以保护数百万下游用户的安全。然而，Anthropic 公司拒绝了该建议，并将此行为定性为“符合预期”。当研究者告知其计划公开发布研究结果时，Anthropic 未表示异议。

安全团队应立即采取以下措施：

* 阻止 AI 服务（尤其是连接了敏感 API 或数据库的服务）暴露在公网。
* 将所有外部 MCP 配置输入视为不可信，并限制用户输入传递到 StdioServerParameters。
* 仅从经过验证的来源（例如官方 GitHub MCP Registry）安装 MCP 服务器。
* 在最小权限的沙箱环境中运行启用了 MCP 的服务。
* 监控 AI 代理的工具调用行为，发现异常的出站活动。
* 立即将所有受影响服务更新到最新的已修复版本。

开源卫士试用地址：https://sast.qianxin.com/#/login

代码卫士试用地址：https://codesafe.qianxin.com

---

**推荐阅读**

[在线阅读版：《2025中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523516&idx=1&sn=0b6fc53ba92e7b5135395b67fff6a822&scene=21#wechat_redirect)

[Axios 严重漏洞可导致 RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525768&idx=2&sn=b8967ced3022f4f88a311a652e635650&scene=21#wechat_redirect)

[Trivy供应链攻击触发CanisterWorm 在47个 npm 包中自传播](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525520&idx=2&sn=b3d4dddc586c4b0aa8cefb09c0344cb8&scene=21#wechat_redirect)

[热门包管理器中存在多个漏洞，JavaScript 生态系统易受供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524984&idx=1&sn=19aef4ce8e288278782458e430a710d8&scene=21#wechat_redirect)

[开源自托管平台 Coolify 修复11个严重漏洞，可导致服务器遭完全攻陷](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524828&idx=2&sn=21af241f60f1452013815133745e9a72&scene=21#wechat_redirect)

[得不到就毁掉：第二轮Sha1-Hulud供应链攻击已发起，影响2.5万+仓库](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524487&idx=1&sn=f170d3131122071dec6e419c6cff562c&scene=21#wechat_redirect)

[vLLM 高危漏洞可导致RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524481&idx=3&sn=6d0b161f8add2f6c1ee65e60ef6955d8&scene=21#wechat_redirect)

[开源AI框架 Ray 的0day已用于攻陷服务器和劫持资源](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519162&idx=1&sn=3872fcc82018e2c561d9e4e7574f0c8e&scene=21#wechat_redirect)

[热门 React Native NPM 包中存在严重漏洞，开发人员易受攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524330&idx=2&sn=bc54e02a8f815ed78b67d3135a9f9607&scene=21#wechat_redirect)

[10个npm包被指窃取 Windows、macOS 和 Linux 系统上的开发者凭据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524314&idx=2&sn=81cae6998a39f2153ed18d7cc065303b&scene=21#wechat_redirect)

[热门 React Native NPM 包中存在严重漏洞，开发人员易受攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524330&idx=2&sn=bc54e02a8f815ed78b67d3135a9f9607&scene=21#wechat_redirect)

[热门NPM库 “coa” 和“rc” 接连遭劫持，影响全球的 React 管道](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247508946&idx=1&sn=273c58d08a4225306a567cf6a150f40c&scene=21#wechat_redirect)

[开发人员注意：VSCode 应用市场易被滥用于托管恶意扩展](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515219&idx=1&sn=faa32338df1d68e7cd738a80222f3a44&scene=21#wechat_redirect)

[GitHub Copilot 严重漏洞可导致私有仓库源代码被盗](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524163&idx=1&sn=d70a7c55e27a3e179522330a9ce62b0b&scene=21#wechat_redirect)

[受 Salesforce 供应链攻击影响，全球汽车巨头 Stellantis 数据遭泄露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524053&idx=1&sn=2b843932ebd4eeeb17b6935b08be82f8&scene=21#wechat_redirect)

[捷豹路虎数据遭泄露生产仍未恢复，幕后黑手或与 Salesforce-Salesloft 供应链攻击有关](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523990&idx=1&sn=ad9957a5c3d054d4a0bf32250bceb556&scene=21#wechat_redirect)

[十几家安全大厂信息遭泄露，谁是 Salesforce-Salesloft 供应链攻击的下一个受害者？](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523972&idx=1&sn=7b06c31940ea7576d0236d9310886b39&scene=21#wechat_redirect)

[第三方集成应用 Drift OAuth 令牌被用于攻陷 Salesforce 实例，全球700+家企业受影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523952&idx=1&sn=2bc84253019e6c2525bcf928eaed696c&scene=21#wechat_redirect)

[黑客发动史上规模最大的 NPM 供应链攻击，影响全球10%的云环境](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523990&idx=2&sn=6e38e1ee8cd69f1375a5be218c02ff97&scene=21#wechat_redirect)

[十几家安全大厂信息遭泄露，谁是 Salesforce-Salesloft 供应链攻击的下一个受害者？](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523972&idx=1&sn=7b06c31940ea7576d0236d9310886b39&scene=21#wechat_redirect)

[第三方集成应用 Drift OAuth 令牌被用于攻陷 Salesforce 实例，全球700+家企业受影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523952&idx=1&sn=2bc84253019e6c2525bcf928eaed696c&scene=21#wechat_redirect)

[AI供应链易遭“模型命名空间复用”攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523962&idx=1&sn=2d9b8ca044c242a6ae1f72df93d7acb0&scene=21#wechat_redirect)

[Frostbyte10：威胁全球供应链的10个严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523957&idx=2&sn=288b0d14a657b13c7f1a6b14705a44e8&scene=21#wechat_redirect)

[PyPI拦截1800个过期域名邮件，防御供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523850&idx=2&sn=72dc01d9984a720959b312dd0e7cf05e&scene=21#wechat_redirect)

[PyPI恶意包利用依赖引入恶意行为，发动软件供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523844&idx=2&sn=08c8962eead61fe76467a9196b3da3e5&scene=21#wechat_redirect)

[黑客利用虚假 PyPI 站点钓鱼攻击Python 开发人员](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523700&idx=2&sn=463d300bdfd3de129cd5d258ceb67cf4&scene=21#wechat_redirect)

[700多个恶意误植域名库盯上RubyGems 仓库](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247492823&idx=2&sn=9c226ff328303e78331451ac5219df07&scene=21#wechat_redirect)

[NPM “意外” 删除 Stylus 合法包 全球流水线和构建被迫中断](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523648&idx=1&sn=d9237c45bf78637d1cdd3bedd1d873e6&scene=...