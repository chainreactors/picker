---
title: Gemini CLI 严重漏洞可触发 RCE 攻击和软件供应链风险
url: https://mp.weixin.qq.com/s/X4L3vZe6Vk4qdMV15DT3zg
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:09:25.230406
---

# Gemini CLI 严重漏洞可触发 RCE 攻击和软件供应链风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQuoJibNce8dlpAMTvqm21iaKUXsfFGTCs9y03jFZZUgVLrh0SDAU6C0fGKxrxZAHqh8SPia88JeHUDg/0?wx_fmt=jpeg)

# Gemini CLI 严重漏洞可触发 RCE 攻击和软件供应链风险

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

**谷歌已修复 Gemini CLI 中的一个严重的安全漏洞，它可导致攻击者在某些自动化工作流中执行远程代码。该漏洞影响 npm 包 @google/gemini-cli 以及 GitHub Action google-github-actions/run-gemini-cli，尤其是当它们在 CI/CD 流水线等无头环境中使用时，从而可能导致供应链风险。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/t5z0xV2OYfVaymqZxrsOywlymiaZvnra1vmPGEIG101pBDOvjzric0w0kRG6H6PtSt9v233x77b71c75ZTtaO737wH9ydbwKN9JTNZVZ8GvuQ/640?wx_fmt=png&from=appmsg)

安全公告提到，该漏洞源于两个相关的弱点：不安全的工作区信任处理和在 --yolo 模式下对工具允许列表的绕过机制。这两个漏洞可导致处理不可信内容的系统（例如来自外部用户的拉取请求或问题提交）遭暴露。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXxfwh6ZruqXqcniaz8qicS6HE4kEG7J8JufzdW13ytxib302V8qeCORniafzVOnpic2C1NqdVkAic5pHUOTkE7Hrx0LhaA9JU1kfjibQ/640?wx_fmt=gif&from=appmsg)

**Gemini CLI 远程代码执行漏洞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXH3BFRXsR0M5fYIaJ85SUiaqHhAvicHE9ABIv0VkiaHvAJia6mywc3pPgyqibAP055v2MW6MCleRslZTzxhzjTxEMPLmHGPr8cibtpg/640?wx_fmt=gif&from=appmsg)

第一个漏洞涉及无头模式下的文件夹信任机制。Gemini CLI 更早版本在非交互式环境中运行时会自动信任当前工作区。这意味着在无需明确批准的情况下，该工具会从 .gemini/ 目录加载本地配置文件和环境变量。如果攻击者在该目录中放置恶意内容，CLI 可能会处理这些内容，并可能执行有害命令。在实际场景中，这为处理不可信仓库的 CI 工作流带来了远程代码执行的可能。

第二个漏洞影响 --yolo 模式下的工具允许列表。在之前版本中，当启用 --yolo 模式时，系统并未正确执行 ~/.gemini/settings.json 中定义的细粒度工具限制。例如，如果某个工作流允许 run\_shell\_command，相关策略可能过于宽泛，从而允许危险的命令，而不仅仅是允许经过批准的指令。在处理不可信提示词或用户控制文本的环境中，该弱点可能通过提示词注入被滥用，进而触发命令执行。

安全公告指出，该漏洞的影响范围仅限于以无头模式部署的 Gemini CLI，但仍涵盖了大量 GitHub Actions 工作流。谷歌警告称，所有用户应重新审视 Gemini CLI 在自动化流水线中的配置方式，特别是在外部贡献者可能影响文件、提示词或环境设置的情况下。

该漏洞影响 @google/gemini-cli 9.39.1和0.40.0-preview.2之前的版本，以及 google-github-actions/run-gemini-cli 0.1.22之前版本。修复版本为@google/gemini-cli 0.39.1、0.40.0-preview.3以及run-gemini-cli 0.1.22。建议所有固定使用旧版 Gemini CLI 的工作流立即进行更新。谷歌同时引入了一项破坏性安全变更：无头模式将不再自动信任工作区文件夹。使用可信输入的组织机构，必须将GEMINI\_TRUST\_WORKSPACE 设置为true。对于处理不可信内容的工作流，谷歌建议遵循其加固指南，并仔细审查所允许的工具及命令执行设置。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfV9FKhccibAMnvqywWNUv5icO0ojglPU2FMjjfEticuMlPAK5T6LNgDia62DpFIZCuyF1RWcayTS2JgdZdeOIhgmuLKribOX8jhm7Qo/640?wx_fmt=gif&from=appmsg)

**软件供应链风险**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfV4pwW87g8bibiaqz0yUXibjPrTFtx5gomeU05MtDjjHEZx1OsQYc943NsOU7OAxgmIpkEvftZ6kWfQkjyZSaXr1tWFrk57AFPnF4/640?wx_fmt=gif&from=appmsg)

该漏洞对软件供应链构成了重大威胁。许多 CI/CD 流水线会自动处理外部输入，例如拉取请求或公开的 GitHub 议题。

如果某条流水线在不可信输入上运行了存在漏洞的 Gemini CLI 版本，则可能在不知情的情况下执行恶意配置。这种自动信任行为为攻击者打开了以下攻击途径：

* 在构建服务器上执行任意代码
* 窃取代码仓库中的敏感密钥和凭证
* 在流水线内部修改源代码
* 横向移动到内部其它系统

由于该漏洞可远程触发且无需任何身份验证，因此被利用的风险显著增加。该漏洞由研究员 Elad Meged（Novee Security公司）和 Dan Lisichkin（Pillar Security公司）通过谷歌的漏洞奖励计划提交。此事件凸显了 AI 驱动开发工具所面临的风险不断增长：当自动化、提示词处理、Shell 访问与不可信输入交织在一起时，细微的策略缺口可能迅速演变为严重的攻击路径；同时也强调了保障CI/CD流水线安全、实施严格验证控制对于保护现代软件供应链免受威胁的重要性。

开源卫士试用地址：https://sast.qianxin.com/#/login

代码卫士试用地址：https://codesafe.qianxin.com

---

**推荐阅读**

[在线阅读版：《2025中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523516&idx=1&sn=0b6fc53ba92e7b5135395b67fff6a822&scene=21#wechat_redirect)

[自传播供应链蠕虫劫持 npm 包，窃取开发人员令牌](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525844&idx=2&sn=3f396c2336c086719e62350cd61cd2bb&scene=21#wechat_redirect)

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

[黑客利用虚假 PyPI 站点钓鱼攻击Python 开发人员](https://mp.we...