---
title: 8月17日高危CVE漏洞速报
url: https://mp.weixin.qq.com/s/KK4w6QmEfOkB6trnt4kdqA
source: Doonsec's feed
date: 2026-08-17
fetch_date: 2026-08-18T02:51:30.431349
---

# 8月17日高危CVE漏洞速报

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nZrMrH4FF0LaMSa17exIy36nEE7eK5qtSvTxLC15eBfcaNTpzIQRItm1kwKchMwNGgfiabV5dt9qZdWMrO0mxnMuzIzUpQ8qlOkrtC1xN0E8/0?wx_fmt=jpeg)

# 8月17日高危CVE漏洞速报

探知安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

安全速报

# 【安全速报】8月17日高危漏洞紧急预警

2026年08月17日  |  探知安全

今日焦点：SAP Commerce Cloud CVSS 10.0 满分漏洞确认在野利用，补丁发布数日内即遭攻击；Adobe 紧急修复 ColdFusion 未认证命令注入（Priority 1）；AI 提示词文件 Prompty 曝模板渲染 RCE；Dell VSI 虚拟化插件与 Gitea 代码托管平台亦需立即升级，请优先排查公网暴露资产。

## 漏洞详情

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-58231 | CVSS 10.0 |

### SAP Commerce Cloud 默认认证客户端滥用致 RCE（CVSS 10.0·满分·在野利用）

SAP Commerce Cloud 存在授权校验与输入验证不足缺陷（CWE-862/CWE-20），未经身份验证的远程攻击者可滥用默认认证客户端（default authentication client），向缺乏充分校验的功能提交特制输入，实现任意代码执行并破坏内部组件，对机密性、完整性与可用性造成高危影响。该漏洞 CVSS 满分 10.0，SAP 发布补丁后仅数日即被证实遭在野利用（Security Affairs 8月15日报道），电商平台通常直接暴露公网，是攻击者重点扫描目标。

影响范围

SAP Commerce Cloud 受影响版本（公网部署的电商/交易平台）

修复建议：立即应用 SAP 官方补丁；审查默认认证客户端配置与异常认证行为，限制平台仅受信网络访问

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-48362 | CVSS 10.0 |

### Adobe ColdFusion OS 命令注入（CVSS 10.0·Priority 1·未认证 RCE）

Adobe ColdFusion 存在 OS 命令注入漏洞（CWE-78），未经身份验证的远程攻击者无需用户交互，即可通过网络向受影响服务器注入系统命令，在服务账户上下文下执行任意代码，导致主机完全失陷。Adobe 在安全公告 APSB26-90 中将其评级为 Priority 1 紧急修复。ColdFusion 常作为遗留业务系统底层，且常被直接暴露公网，一旦被攻破即可作为内网渗透跳板，部署 webshell、窃取配置凭据、横向移动。

影响范围

Adobe ColdFusion 2025.0.11 及更早、2023.0.22 及更早

修复建议：立即升级至 ColdFusion 2025.0.12 / 2023.0.23；限制管理界面公网暴露，排查异常子进程与陌生外联

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-73299 | CVSS 10.0 |

### Prompty（TypeScript Nunjucks）模板渲染致任意代码执行（CVSS 10.0·AI 提示词供应链）

AI 提示词文件格式 Prompty 的 TypeScript Nunjucks 渲染器存在任意代码执行漏洞，攻击者构造恶意 .prompty 文件，一旦被渲染即可执行任意代码。对允许用户上传提示词文件的 LLM 应用/平台威胁尤其严重，恶意提示词文件可在服务端触发 RCE。随着 AI 应用与 Agent 编排平台快速普及，提示词文件正成为新的供应链攻击载体，需像对待代码一样对待提示词输入。

影响范围

Prompty TypeScript Nunjucks 渲染器 0.1.5 之前、2.0.0-beta.5 之前

修复建议：立即升级至 0.1.5 / 2.0.0-beta.5 及以上；不处理不受信任的 .prompty 文件

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-67261 | CVSS 9.8 |

### Dell VSI for VMware vSphere OS 命令注入（CVSS 9.8·root 权限 RCE）

Dell Virtual Storage Integrator (VSI) for VMware vSphere Client 的 IAPI 组件存在操作系统命令注入漏洞，未经身份验证的远程攻击者即可通过网络利用，在目标主机上以 root 权限执行任意系统命令，完全接管系统。VSI 作为 vSphere Client 的集成插件，直接嵌入虚拟化控制平面，被攻破意味着攻击者可威胁整个虚拟化环境，导致敏感数据泄露与基础设施瘫痪。配套漏洞 CVE-2026-54489（信息泄露 CVSS 9.1）可窃取活动会话凭据并冒充管理员，两者可组合利用。戴尔官方公告 DSA-2026-335，无临时缓解措施，升级是唯一修复途径。

影响范围

Dell VSI for VMware vSphere Client 10.11.1.0 之前所有版本

修复建议：立即升级至 10.11.1.0 及以上版本；检查 vSphere 插件暴露面并限制访问

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-60004 | CVSS 9.8 |

### Gitea diffpatch API 远程代码执行（CVSS 9.8·恶意 patch 触发 git hooks）

开源自托管 Git 平台 Gitea 的 diffpatch API 存在远程代码执行漏洞，攻击者提交恶意格式的 patch 文件至临时裸仓库，当系统使用 Git 2.32 以上版本时，恶意 patch 可触发 add/add 冲突，诱使 Git 三方合并机制将可执行文件写入仓库的 git hooks 目录，随后 Git 更新索引时自动执行 post-index-change Hook，以 Gitea 服务账户身份执行任意命令。虽然利用需仓库写权限，但 Gitea 默认开放注册，未授权攻击者可轻易注册账号获取写权限。Gitea 广泛用于企业内部代码托管与 CI/CD 流水线，一旦失陷可导致源码泄露、供应链攻击与内网横向移动。

影响范围

Gitea 1.17.0 – 1.27.0

修复建议：立即升级至 1.27.1 及以上；关闭开放注册或限制仓库写权限，审查仓库 git hooks 目录

紧急提醒

本期最高优先级：SAP Commerce Cloud CVE-2026-58231 CVSS 10.0 满分漏洞已确认在野利用（补丁发布数日内即遭攻击）；Adobe ColdFusion CVE-2026-48362 未认证 OS 命令注入被评级 Priority 1 紧急修复。建议安全团队优先排查公网暴露的 ERP、应用服务器、虚拟化插件与代码托管平台，先升级再谈其他。

处置建议

① SAP Commerce Cloud 用户立即应用官方补丁，审查默认认证客户端配置与异常认证行为

② Adobe ColdFusion 立即升级至 2025.0.12 / 2023.0.23，限制管理界面公网暴露并排查异常进程

③ Prompty 用户升级至 0.1.5 / 2.0.0-beta.5 及以上，不处理不受信任的 .prompty 文件

④ Dell VSI for VMware vSphere 立即升级至 10.11.1.0 及以上（DSA-2026-335），检查插件暴露面

⑤ Gitea 自托管用户立即升级至 1.27.1，关闭开放注册或收紧仓库写权限

觉得有用？点击右下角**在看**，让更多人看到

探知安全 · 每日推送最新漏洞资讯

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ayPnpNqYCJKbeG52l1HMrttVrHhaGYKtDOWalO9FcwwVTzzCKhpg0BEKR4eZdo8JXdrv6n8RZAOgtnmcEPgvHg/0?wx_fmt=png)

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