---
title: 从攻击者视角思考 Detection Engineering
url: https://mp.weixin.qq.com/s/RGEBwAP5D9N9NRv0jWV0HQ
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:44:11.222383
---

# 从攻击者视角思考 Detection Engineering

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSiaGrzoNQvVIPqbo0X2L5vzMibNaMJcjSiabwXE2QWWAXm7mbnicGKb88Xnd4IGwbz2voKPONNMkl2vw6Pok7j5tVrYlGrico0Tq4ibo/0?wx_fmt=jpeg)

# 从攻击者视角思考 Detection Engineering

Ruslan Sayfiev
Ruslan Sayfiev

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://files.speakerdeck.com/presentations/6746bca2d3b74466af4ac884206b9ba7/AttackerView\_Detection\_Engineering.pdf | Ruslan Sayfiev |

从攻击者视角思考 Detection Engineering 演讲

2026/06/11

Ruslan Sayfiev

Interop Tokyo 2026

## Slide 2 — 自我介绍

Ruslan Sayfiev / 赛菲耶夫·鲁斯兰

Principal Consultant / Red Team Architect — Fujitsu Uvance Wayfinders

OSEE OSCE3 OSCP GXPN

**履历**

* 以"Red Team 测试 = 重新设计防御态势的起点"为核心理念，推动守护重要资产的防御变革
* 在进攻性安全 (Offensive Security) 领域从业 15 年以上，拥有 300+ 实战项目经验，主导了日本国内相关服务的搭建与运营
* 不将 Red Team 局限于入侵验证，而是基于攻击者视角与业务风险，支持重新设计防御态势、检测设计与响应能力
* 2026 年起加入富士通 Uvance Wayfinders，推动实战化网络抵抗力的构建与新实践型安全服务的创造

**专业领域**

* Red Teaming / adversary simulation（对手模拟）
* 渗透测试
* Exploit 开发 / 逆向工程
* 漏洞研究（有发现 CVE 的实绩）
* Offensive R&D / 工具开发
* 与 Detection Engineering 的协同设计
* OffSec 官方讲师（CODE BLUE）

LinkedIn: https://www.linkedin.com/in/ruslan-sayfiev/

X: @cryptopeg

## Slide 3 — 术语定义与概念梳理：相似但角色不同

**Red Team**

从攻击者视角，实证通向最大业务风险的攻击路径

攻击路径 / 防御缺口 / 业务影响

**Threat Hunting（威胁狩猎）**

基于假设，搜寻尚未告警化的威胁痕迹

假设验证 / 痕迹探索 / 新的检测候选

**Detection Engineering（检测工程）**

基于攻击场景，设计"下次同样攻击再来时能察觉"的机制

日志设计 / 检测逻辑 / 告警质量 / 响应设计

**Purple Team（紫队）**

在同一场景下验证攻击与防御，改善检测、响应与防御

检测验证 / 调优 / Playbook 改善

> 虽然各自角色不同，但在提升"攻击者视角的防御力"上，每一项都至关重要。

## Slide 4 — 关键不在"有无对策"，而在"是否看得见攻击的流向"

* **有 EDR ≠ 看得见整个攻击**

EDR 擅长终端可视化。但认证、SaaS、VPN、权限滥用往往在其范围之外。

* **Red Team 演习 ≠ 下次就能察觉**

演习只是快照。若不改变设计、检测、运营，同样的缺口会残留。

* **符合 CSF ≠ 能阻止攻击路径**

框架只是基线。企业自身特有的攻击路径需要另行设计。

常见的误解

## Slide 5 — 框架只是基线，企业自身的攻击路径需要另行设计

**CSF 提供的东西**

* 一般性管理措施的指针
* 风险分类的框架
* 安全成熟度的评估轴
* 合规应对的基础

**仅靠 CSF 无法具体化的内容**

* 企业自身特有的攻击路径
* 所需日志源的优先级
* 应在何处阻止攻击者
* 检测规则的具体设计

**为何仅靠符合 CSF 仍不够**

需要在 CSF 基础上，将企业自身的重要资产、攻击路径、检测需求具体化。

## Slide 6 — 演习只是当时点的快照，攻击面每天都在变化

Red Team 演习并不能持续保证安全：

* 业务风险高度依赖范围 (scope)
* 若止步于报告书，效果无法留存
* 即便修复了个别漏洞，攻击路径或设计层面的问题仍可能残留
* 即便无法修复的问题，也可以通过监控/检测来设计应对
* 新的 SaaS 或例外设置会持续改变攻击面
* 攻击者的手法也在变，因此检测也需持续更新

**为何仅靠 Red Team 演习仍不够**

重要的是将演习结果转化为环境设计、运营与检测设计。

## Slide 7 — 攻击不只在终端完成，需要认证/SaaS/VPN-ZTNA/权限的可视化

**EDR 的主要可视范围**

* 终端
* 认证 IdP / AD
* 数据访问 SaaS / DB / 文件服务器
* 连接 VPN / ZTNA / SASE
* 横向移动 网络 / 终端 / 服务器
* 权限滥用 IdP / AD / PAM

**为何部署 EDR 仍会被入侵**

需要建立一套机制：将 EDR（即使被绕过也）看不见的攻击路径，与其他日志源做关联分析。

## Slide 8 — 收集日志与能检测攻击是两回事

* Level 1: 产品导入
* Level 2: 日志整合
* Level 3: Detection Engineering（检测工程）

## Slide 9 — 统一攻击者模型

**Initial Access Broker（初始访问代理）**

泄露/弱认证信息、远程访问 (VPN)、钓鱼、外部公开服务

**Ransomware Operator（勒索软件运营者）**

短期（最大影响）：数据窃取、加密、业务停止

**APT（高级持续性威胁）**

定向型、长期入侵：零日攻击、隐蔽/OPSEC、多次尝试

**内部犯罪**

正规访问，极难检测

Detection Engineering 视角：

* 明确"假设的是谁"
* 不同攻击者模型所需的日志源与检测粒度不同
* 应对内部犯罪需要正规操作的基线化

> 因攻击者不同，目标手法与所需检测也不同。

## Slide 10 — 从外部看公司是什么样

攻击者寻找"入口"，仅凭外部可见信息就能制定攻击计划。

**公开信息**

* 域名 / 子域名
* IdP / SSO
* VPN / ZTNA / SASE
* SaaS / 外部服务
* 招聘信息（产品、技能栈等）
* 导入案例（产品信息）/ 技术文章（流程等）
* 集团 / 子公司（同网络）
* 供应链 / 合作企业
* 员工信息 / 邮箱地址

Detection Engineering 视角：

* 持续盘点外部公开资产
* 优先确认 IdP / VPN / SaaS 等"入口"的日志
* 将外部可见的攻击路径转化为检测场景

## Slide 11 — 攻击场景：当多个防御缺口相连会发生什么

此场景基于多个实战经验与一般防御缺口构建。

## Slide 12 — 微小的例外、过度共享的信息、看不见的日志相连，就构成攻击路径

**攻击场景 · 整体概要**

OSINT → 认证信息泄露（信息收集、外部监控）→ [2][3] IdP/SSO 配置缺陷（IdP 日志）→ M365 资源内部信息收集（M365 审计日志）→ [5] 远程访问配置缺陷（VPN/SASE 日志）→ [7] 特权账户（AD / 特权操作日志）→ 通向业务影响的道路

**前提：假设的防御状况**

* EDR：已部署
* IdP：已部署 MFA / 条件访问策略
* 远程访问：ID/PW + MFA（形式上的 MFA）

[1][2][3][4][5]

## Slide 13 — 攻击场景①：认证信息泄露成为攻击起点

从泄露信息与可推测的密码模式，识别出有效的认证信息。

**OSINT / 攻击者行为**

* 从泄露数据库中获取认证信息（类似默认密码的、复用的）
* 构建用于密码喷射 (password spray) 攻击的列表
* 发现有效账户

**常见的防御缺口**

* 未持续监控泄露信息
* 使用默认或可推测的密码
* 未设置密码喷射攻击的检测阈值
* 未监控失败登录
* 大量失败 → 1 次成功
* 来自陌生上下文的首次登录

**Detection Engineering 视角**

* 定期监控泄露信息，并快速重置相关账户
* 从 IdP 日志设计规则：检测短时间内的多次认证失败
* 关联检测：同一 IP 对多个账户的登录尝试

## Slide 14 — 攻击场景②：被信任的条件成为漏洞

利用例外规则规避条件访问策略，非法访问 M365 资源。

**IdP / SSO / 攻击者行为**

* 分析条件访问策略的判定条件
* 通过伪造特定设备来规避条件访问策略
* 在绕过 MFA 的情况下成功访问 M365 资源

**常见的防御缺口**

* 条件访问策略依赖 User-Agent 等易于伪造的条件
* 缺乏对设备合规状态或自定义参数的验证
* 未将策略规避的尝试作为日志记录与监控

**Detection Engineering 视角**

* 从 IdP 日志设计规则：检测非预期的 IP 地址、User-Agent 或 OS 信息
* 检测不熟悉的 Client ID / App ID，或无需 MFA 的许可登录模式
* 定期审查条件访问策略的判定结果（许可/拒绝），发现例外模式
* 关联检测：同一用户来自不同设备配置文件的访问

## Slide 15 — 攻击场景③：M365 成为攻击者的地图

从过度共享的文档中，泄露内部系统配置与认证信息。

**M365 资源 / 攻击者行为**

* 发现外部服务相关信息
* 发现以明文记载的认证信息
* 发现与远程访问或内部环境相关的信息

**常见的防御缺口**

* 含机密信息的文档向全公司员工公开
* 认证信息以明文写在文档内
* 未监控 SharePoint 或 OneDrive 上的大量文件访问

**Detection Engineering 视角**

* 从 M365 审计日志检测短时间内的海量文件访问
* 用 DLP（数据防泄漏）检测含密码/证书的文档
* 定期盘点 SharePoint 与 OneDrive 的共享范围，发现过度共享

## Slide 16 — 攻击场景④：正规连接不等于正规用户

利用获取的证书与认证信息建立 VPN 连接，入侵内部网络。

**远程访问 / 攻击者行为**

* 基于获取的信息建立远程访问
* 缺乏设备合规或自定义参数验证，连接成功
* 可从攻击者终端直接访问内部网络

**常见的防御缺口**

* 无设备态势 (device posture) 检查
* 证书+密码的"形式上 MFA"实质上不起作用
* 未监控/告警来自新设备的 VPN 或 SASE 连接

**Detection Engineering 视角**

* 从 VPN/SASE 日志检测未登记设备/新设备的连接
* 比对证书序列号与签发者，检测非预期证书
* 比较 VPN/SASE 连接源的 IP/地理信息与用户通常模式
* 证书不只验证 CA，也验证 CN（Common Name），检测非预期值

## Slide 17 — 攻击场景⑤：通向业务影响的最短路径

利用特权账户，获得对所有系统的访问权。

**特权账户 / 攻击者行为**

* 用特权账户向 AD 认证成功
* 掌握对所有域资源的访问权限

**常见的防御缺口**

* 特权账户相关信息被过度共享
* 特权账户认证成功未触发告警
* 特权账户未执行密码轮换

**Detection Engineering 视角**

* 将特权账户的所有认证设计为告警对象
* 从 AD 日志即时检测来自新设备/IP 的特权登录
* 通过"远程访问 → 特权认证"的时间相关性，可视化攻击链

## Slide 18 — 再次思考：为何部署 EDR 仍会被入侵

EDR 很重要。但要看清整个攻击路径，需要与其他日志源关联。

| 攻击步骤 | 日志源 | EDR 单独不足的理由 |
| --- | --- | --- |
| 密码喷射攻击 | IdP 日志 | 云认证事件发生在终端之外 |
| 条件访问策略规避 | IdP 日志 | 云认证事件发生在终端之外 |
| M365 资源探索 | M365 审计日志 | 云上的操作事件仅靠终端日志无法追踪 |
| 远程访问 | VPN / SASE 日志 | 攻击者终端上没有 EDR |
| 域管理员权限滥用 | AD / 特权操作日志 | 仅靠认证成功难以触发告警 |

> 根据攻击步骤的不同，需要确认的日志源也不同。

## Slide 19 — 再次思考：为何仅靠 Red Team 演习仍不够

若不将演习结果转化为持续的检测与运营，缺口会残留。

Red Team 展示"能否入侵"。Detection Engineering 构建"下次能否察觉"。

```
Red Team                          Detection Engineering
测试实施 → 报告书受领 → 应对指摘事项
                          ↓
              攻击场景的评审
                          ↓
          所需日志 / 遥测的再定义
                          ↓
            检测逻辑的制作
                          ↓
              测试 / 调优
```

## Slide 20 — 总结

CSF、EDR、Red Team 演习各自都很重要。

但单独任何一个都无法看清整个攻击路径。

**今日要点**

* CSF 展示基线，但无法具体化企业自身特有的攻击路径
* EDR 可视化终端，但看不清认证/SaaS/VPN/权限滥用
* Red Team 揭示攻击路径，但若不将结果落地到运营，就无法形成持续的防御力
* 攻击者将微小的例外、过度共享、看不见的日志串联起来，制造攻击路径

**重要的思维方式**

需要的不仅仅是增加个别对策，而是基于攻击场景，设计所需的日志、检测、关联与运营。

---

*原文：攻撃者視点で考える Detection Engineering — Ruslan Sayfiev (Interop Tokyo 2026)*

*PDF 下载：https://files.speakerdeck.com/presentations/6746bca2d3b74466af4ac884206b9ba7/AttackerView\_Detection\_Engineering.pdf*

---

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

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