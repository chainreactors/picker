---
title: 老把戏，新靶心：Bash 正威胁 AI 编程代理供应链安全
url: https://mp.weixin.qq.com/s/F1yK6vedUY2q7rX3HvFhEw
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:55:30.768339
---

# 老把戏，新靶心：Bash 正威胁 AI 编程代理供应链安全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQuoJibNce8dlpAMTvqm21iaKUXsfFGTCs9y03jFZZUgVLrh0SDAU6C0fGKxrxZAHqh8SPia88JeHUDg/0?wx_fmt=jpeg)

# 老把戏，新靶心：Bash 正威胁 AI 编程代理供应链安全

Omer Ben Simon
Omer Ben Simon

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

编译：代码卫士

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRSylJK2k7H6mNqiaS2G6WRaeeK34cLHE6pe9VeOIHYiboAnKB0TMoayZCxFpHMLljzTnz9DnNuFiaqQ/640?wx_fmt=png)

专栏·供应链安全

数字化时代，软件无处不在。软件如同社会中的“虚拟人”，已经成为支撑社会正常运转的最基本元素之一，软件的安全性问题也正在成为当今社会的根本性、基础性问题。

随着软件产业的快速发展，软件供应链也越发复杂多元，复杂的软件供应链会引入一系列的安全问题，导致信息系统的整体安全防护难度越来越大。近年来，针对软件供应链的安全攻击事件一直呈快速增长态势，造成的危害也越来越严重。

为此，我们推出“供应链安全”栏目。本栏目汇聚供应链安全资讯，分析供应链安全风险，提供缓解建议，为供应链安全保驾护航。

*注：以往发布的部分供应链安全相关内容，请见文末“推荐阅读”部分。*

**Adversa AI****公司在多个开源 AI 代理中发现了一个结构性的安全缺陷，并将其称之为“GuardFall”。该缺陷并非单一漏洞，而是一种危险的惯例和一类问题的总称。基于原始命令字符串匹配的过滤器无法建模 Bash 的展开机制，因此只能提供虚假的安全感而并无实际防护——这种虚假安全感恰恰会导致人工审批被关闭、自动模式被开启。**

研究人员测试了 11 个流行的开源代理（包括 Hermes、OpenCode、Roo-code 等）。实验结果表明，其中 10 个至少存在一类可被利用的防护绕过路径，仅 1 个代理（Continue）在全部测试类别中未发现绕过情况。研究将所用绕过手法分为五类（A 至 E），包括引号移除、$IFS、命令替换、base64 转 shell、破坏性 argv 标志等——这些均是有数十年历史的 shell 技巧，能够系统地击溃当今最流行开源 AI 代理的防护机制。其中 E 类成功率最高，它能绕过最多的防护，包括基于标记化的最强防护。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWsicq2Tl39NlzXd8uNNeicWPGD7V8m56SFfCPnUw7x93nJBPbh4iaR0c6ZGEEBv5PzlJa7vADYKLlnSmJEh2J2w955bcwdPRkM1w/640?wx_fmt=gif&from=appmsg)

**为什么会发生？**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfX0XAh1jbpUfiaYCqoxqia0jN6P5CyfjIlTEp0uFZTWEsgoFibfE0oofqLmuNky98RJ7avdaokKLqmPXuu3PweTSQINl8NItIBWco/640?wx_fmt=gif&from=appmsg)

根本原因在于防护机制与 Bash 实际执行之间的不匹配。代理通常使用基于模式匹配的 shell 防护，检查原始文本，但系统 shell（Bash）在执行命令前会对文本进行展开、移除引号和重写。因此，代理认为自己在运行的命令与 Bash 实际运行的命令存在差异，这一结构性缺口正是 GuardFall 得以成立的基础。

研究人员归纳出四种架构性失效模式：在所调查的代理中，有三个（Hermes、opencode、Goose）虽然内置了防护但均被绕过；其余代理的失效形式各不相同——有的采用基于标记化的防护，但在带引号替换和破坏性标志处存在泄漏；有的完全没有静态防护；有的依赖沙盒，但一旦切换至文档中允许的本地/自动模式便会失效。单纯“增加更多拒绝列表模式”无法解决其中任何一个问题。

此外，此类利用还依赖前置条件：虽然直接的恶意提示词往往会被模型拒绝，但代理在摄入操作上下文（如被投毒的 README 或 Makefile）时，很容易诱使前沿模型将注入的命令作为常规任务发出。这一攻击链依赖于模型和上下文框架——研究实际测试使用的是 Claude Sonnet 4.6。

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfWdw2VGARywRrfawvXycUHbwRTsZ5dnaAIc9mgIVfDbtN7Qfmvd8l4CibYaGwibOfykrcJLo5H03uRAOPvKINxNYN4vJHJhbT7gY/640?wx_fmt=gif&from=appmsg)

**造成的影响**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUBGL8DCmz7FiacIoOpicuY0zEl8tqast87D1kCm91r50KT4fjJFF226ftf7NvVAC4I8NqaQoWvjZKE5cicqp4D1v47aDo8BEdNjA/640?wx_fmt=gif&from=appmsg)

由于这些代理以开发者的完整账户权限运行，攻击者可利用 GuardFall 悄无声息地执行命令，例如窃取 AWS 凭证或清空整个开发环境，尤其在 CI 流水线中（“自动确认”模式常为默认），风险会放大，进而演变为重大的供应链风险。

在测试的 11 个代理中，仅有 1 个（Continue）未出现可被利用的绕过路径；其余代理均在不同类别上存在缺陷。研究人员将 Continue 视为在其默认 IDE 模式下能够在结构上封闭大部分绕过路径的参考设计，它是针对大多数开发者实际运行配置（代理在宿主机上运行、真实 $HOME、非一次性工作空间）的有效防御方案。另一种常见方案沙盒，仅在可以丢弃工作空间的配置下才有效。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfW6l28wz5xAhxiaWjT0zdFL7nibO0lUMbZrhIKmicpskXJ9k9iaWsfPx5COcVkGg9QE5b4k7L9vm07drCibnxBvZaQrjPQDamO5JZyg/640?wx_fmt=gif&from=appmsg)

**应对措施**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXh5y6sUibfGbgLk7bhCeELEX9hxLUvoicQDwL50HFn962WvZTRVXtSzzlKM86PmHmM5PTafQqWIwPUePDUKzCzRCQHmfL3dS8Po/640?wx_fmt=gif&from=appmsg)

针对该问题，研究人员提出了临时缓解措施（如限定 shell 作用域、重定向 $HOME、禁用自动确认等），但强调这些仅为权宜之计。长期解决方案需由代理维护者在其内部实现更严格的命令评估机制，以弥合模式匹配防护与 Bash 实际执行之间的结构性差距。

开源卫士试用地址：https://sast.qianxin.com/#/login

代码卫士试用地址：https://codesafe.qianxin.com

---

**推荐阅读**

[在线阅读版：《2025中国软件供应链安全分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523516&idx=1&sn=0b6fc53ba92e7b5135395b67fff6a822&scene=21#wechat_redirect)

[“冬虫夏草”供应链漏洞影响数千家组织机构的代码仓库](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526367&idx=2&sn=873a39cf55d45ffab906c2a6ab004056&scene=21#wechat_redirect)

[多家网络安全公司受 Klue 供应链攻击影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247526263&idx=2&sn=c680ad4854702c179a3070ca44d72c78&scene=21#wechat_redirect)

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

[热门NPM库 “coa” 和“rc” 接连遭劫持，影响全球的 React 管道](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247508946&idx=1&sn=...