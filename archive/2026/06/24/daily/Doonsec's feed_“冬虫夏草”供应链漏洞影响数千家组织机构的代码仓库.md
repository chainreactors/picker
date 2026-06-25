---
title: “冬虫夏草”供应链漏洞影响数千家组织机构的代码仓库
url: https://mp.weixin.qq.com/s/PfoHqQUojOONl1M4FMe0zw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:00:20.382167
---

# “冬虫夏草”供应链漏洞影响数千家组织机构的代码仓库

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQuoJibNce8dlpAMTvqm21iaKUXsfFGTCs9y03jFZZUgVLrh0SDAU6C0fGKxrxZAHqh8SPia88JeHUDg/0?wx_fmt=jpeg)

# “冬虫夏草”供应链漏洞影响数千家组织机构的代码仓库

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

作者：Tushar Subhra Dutta

编译：代码卫士

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRSylJK2k7H6mNqiaS2G6WRaeeK34cLHE6pe9VeOIHYiboAnKB0TMoayZCxFpHMLljzTnz9DnNuFiaqQ/640?wx_fmt=png)

专栏·供应链安全

数字化时代，软件无处不在。软件如同社会中的“虚拟人”，已经成为支撑社会正常运转的最基本元素之一，软件的安全性问题也正在成为当今社会的根本性、基础性问题。

随着软件产业的快速发展，软件供应链也越发复杂多元，复杂的软件供应链会引入一系列的安全问题，导致信息系统的整体安全防护难度越来越大。近年来，针对软件供应链的安全攻击事件一直呈快速增长态势，造成的危害也越来越严重。

为此，我们推出“供应链安全”栏目。本栏目汇聚供应链安全资讯，分析供应链安全风险，提供缓解建议，为供应链安全保驾护航。

*注：以往发布的部分供应链安全相关内容，请见文末“推荐阅读”部分。*

**Novee****公司的研究人员发现了一个被称为 “冬虫夏草 (Cordyceps)”供应链漏洞，使成千上万的组织机构面临严重风险。该漏洞以寄生真菌“冬虫夏草”命名，它会悄无声息地钻入软件开发流水线，使攻击者能够完全控制全球一些最大公司的代码仓库。**

这些CI/CD工作流会运行shell命令、持有签名密钥、向云提供商进行身份验证并发布版本。然而，它们被广泛视为简单的配置文件，而非安全关键型代码。而这种认知上的差距正是“冬虫夏草”漏洞所利用的。

研究人员在开源供应链中识别出了这一系统性的可利用漏洞类别，发现了GitHub Actions工作流中的命令注入、认证逻辑缺陷、制品投毒链和权限提升等模式。研究团队扫描了约3万个高影响力仓库，并确认了数百个完全可利用的攻击链。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUdrpBVr6jsETdZiatEruCf3HwuHIa44rPgfribDibhoDndoDAUId7OQykqNtMOaPqdk0R7KkzYThZXQMIg61srPXV7tnXcEpTboo/640?wx_fmt=gif&from=appmsg)

**极易利用**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUSU3Rct7YKZHaZhaLejdsOkhvXVibooFDnPQOrtxnsDqNIE4VI1A50iazKKXMJd7CZ3tC5X7icxSeMtMeByzmuHway15MOuvpZpQ/640?wx_fmt=gif&from=appmsg)

这一发现令人担忧的不仅是漏洞的技术深度，还有其易用性。任何拥有免费GitHub账户的人都可以利用它，无需特殊权限或组织成员资格。

只需一个拉取请求，甚至一个评论，就足以触发攻击链，让外部人员完全控制项目的构建流水线。其下游影响范围巨大。当一个被入侵的仓库供应着数千个组织机构所依赖的软件时，一次攻击就可能波及银行、云环境、AI实验室和终端用户设备。包括微软、谷歌、Apache、Cloudflare和Python软件基金会在内的主要组织已确认修复了该漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUicbxHY4lSd0pZpn6eFJTXKkdFu22p7lrCvyVRBPP4rNEncDPvK1BEcTWuBSSZQ2MNVIuia2loH96Sc3TBDRolHrnH8gwkicM2o4/640?wx_fmt=gif&from=appmsg)

**“冬虫夏草”供应链漏洞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXLwaxyMqJkickF4Macy8gEibndZ8ZySPTEIeSSbLrvo8uGaChLHPzexibsbVOGn6fTf1iaicEQR19iaAdZlpANshjp5EBgbqZlGQxicI/640?wx_fmt=gif&from=appmsg)

“冬虫夏草”最危险的一面在于它如何隐藏于无形之中。攻击链是多步骤的，这意味着没有任何单一环节本身看起来是危险的。一个不受信任的拉取请求会触发一个低权限工作流，其输出流入一个高权限工作流，然后该工作流以最高权限向云环境进行身份验证。每一步看起来都很正常，但组合起来就形成了一条通往完全控制的清晰路径。这正是该漏洞难以被传统安全扫描器发现的原因。

标准工具会检查单个文件中的已知模式，但“冬虫夏草”的风险仅存在于多个工作流之间的交互方式中。扫描器看到的是有效的YAML配置，而攻击者看到的是一条通往永久凭证访问权限的四步攻击链。

研究人员确认有超过300个仓库完全可利用。在微软的Azure Sentinel中，对拉取请求的一条评论就足以让攻击者窃取一个永不过期的GitHub App密钥。对于谷歌的AI Agent开发套件，一个拉取请求就能让攻击者获得最高的Google Cloud角色。在Apache的Doris中，确认了两条零点击攻击路径，都导致凭证窃取和直接代码修改权限。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXqrVzsXzzllIsWia6Hv58PCzJMA3ibFQxjRs1UHS52wmMwNtIFkyZdib1sNB8hibMkdBjm1KfDpGP2qr9tuf5Vic0YEPolTCuAbv90/640?wx_fmt=gif&from=appmsg)

**AI正在大规模加剧问题的严重性**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWL6y4NBE1DU5kd9WIJQ807LwvGF9n6E6R5yR9MEY1bPvhkOIPGn9OAaxvzKIzibAhk3I2wD0OX7D85TwdetzF4Y69NJbicdTLlY/640?wx_fmt=gif&from=appmsg)

“冬虫夏草”漏洞研究中最令人不安的发现之一是AI编码助手在传播该漏洞中所扮演的角色。随着开发人员越来越依赖AI工具快速生成CI/CD配置文件，这些工具会反复生成相同的不安全模式。结果是同一类漏洞被悄悄植入可能数以百万计的仓库中。研究团队提取了npm、PyPI、crates和Go生态系统的数据，在一次扫描中就标记了654个仓库。已证实的影响覆盖了完整的构建和发布流水线，涉及从代码推送到受保护分支，再到AWS、GCP和Netlify上的凭证窃取等各个方面。

在GitHub上运行软件或依赖此类开源项目的组织被敦促评估其风险敞口。一旦识别出问题，修复方法其实很直接。安全团队应以与应用程序代码同等的严谨度对待工作流代码，进行跨工作流审计，并确保低权限与高权限工作流之间的信任边界不能被拉取请求标题、分支名称或评论内容等不受信任的输入所跨越。

开源卫士试用地址：https://sast.qianxin.com/#/login

代码卫士试用地址：https://codesafe.qianxin.com

---

**推荐阅读**

[在线阅读版：《2025中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523516&idx=1&sn=0b6fc53ba92e7b5135395b67fff6a822&scene=21#wechat_redirect)

[多家网络安全公司受 Klue 供应链攻击影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526334&idx=2&sn=d4abea93a1ec375ff30540cc905667d5&scene=21#wechat_redirect)

[GitHub 推出 npm 安全变更，对抗供应链攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526263&idx=2&sn=c680ad4854702c179a3070ca44d72c78&scene=21#wechat_redirect)

[最新软件供应链事件概览：Red Hat npm 包遭劫持；投毒 Claude Code；OpenAI Codex 认证令牌被盗](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526103&idx=1&sn=5bb0348b6f36ac8d144547cea211d8bd&scene=21#wechat_redirect)

[TrapDoor 供应链攻击通过 npm、PyPI 和 CratesIO 传播凭据窃取恶意软件](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526103&idx=1&sn=5bb0348b6f36ac8d144547cea211d8bd&scene=21#wechat_redirect)

[自动化供应链攻击6小时内攻陷5561个 GitHub 仓库](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526078&idx=2&sn=23c01cd3ffaa8a2a7421ffb9fe242d2a&scene=21#wechat_redirect)

[GitHub 被黑或因员工安装 Nx Console 恶意扩展引发，更多详情待调查](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526078&idx=2&sn=23c01cd3ffaa8a2a7421ffb9fe242d2a&scene=21#wechat_redirect)

[GitHub 内部仓库疑遭未授权访问，TeamPCP 据称正在出售 GitHub 内部源代码](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526060&idx=1&sn=63894334faf0814e075ab85697c75a66&scene=21#wechat_redirect)

[奇安信Qcode Agents重磅升级，正式解锁操作系统级漏洞挖掘能力](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526078&idx=2&sn=23c01cd3ffaa8a2a7421ffb9fe242d2a&scene=21#wechat_redirect)

[Grafana 令牌被盗，GitHub 环境可遭访问且代码库被下载](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526043&idx=2&sn=ef8599cf70e02716369d0205be9be468&scene=21#wechat_redirect)

[TeamPCP再发动供应链攻击；数百个恶意包被上传，RubyGems 暂停新账号注册](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525995&idx=3&sn=e59f7d088b3f4113b18c149ac6e505c3&scene=21#wechat_redirect)

[Checkmarx 再遭攻击，Jenkins AST 插件受陷](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525972&idx=1&sn=b93bcffc7c3ad4c106fbd39a4ee2218e&scene=21#wechat_redirect)

[Go 流行库 fsnotify 的维护人员访问权限变更，拉响供应链攻击警报](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525972&idx=2&sn=26ec27a2c831c25b913ce2dfb5658469&scene=21#wechat_redirect)

[Gemini CLI 严重漏洞可触发 RCE 攻击和软件供应链风险](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525887&idx=1&sn=294cc8c49080c6239db19c1f8525457e&scene=21#wechat_redirect)

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

[开发人员注意：VSCode 应用市场易被滥用于托管恶意扩展](https://mp.weixin.qq.com/s?__b...