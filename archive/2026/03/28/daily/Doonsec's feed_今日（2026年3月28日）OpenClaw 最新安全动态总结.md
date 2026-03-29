---
title: 今日（2026年3月28日）OpenClaw 最新安全动态总结
url: https://mp.weixin.qq.com/s/6a2IBsoFlw_D_BAMDaMI6A
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:34:43.950276
---

# 今日（2026年3月28日）OpenClaw 最新安全动态总结

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555t9XZQOsUiaibh2ZJH7LGOXmJSGXbFIDZpkOMU83JMUOI80icKq2yTLspg4ubN11d2ibHKWp1xSSsgm2B8x0WricQKo23sRPic33fUr0/0?wx_fmt=jpeg)

# 今日（2026年3月28日）OpenClaw 最新安全动态总结

奇安信 CERT

![]()

在小说阅读器中沉浸阅读

**3月28日资讯导视**

OpenClaw于3月26日集中发布12条GHSA安全公告，聚焦Gateway授权绕过、Webhook预认证解析及DM配对策略绕过等多项高/中危问题。

CVE-2026-27183（Shell Approval Gating Bypass）于3月23-27日披露，影响<2026.3.7版本，已在最新版修复；社区今日热议其对system.run执行链的影响。

山东大学研究团队3月27日发布OpenClaw安全分析报告，对47种攻击场景（融合MITRE ATLAS/ATT&CK）进行实测，AI代理默认高度易受攻击，HITL（人工介入）为关键防御；X平台今日广泛转发，强调“情绪操控”等新型绕过风险。

***PART 0****1***

**今日核心事件**

今天（2026-03-28）暂无全新零日漏洞或大规模安全事件爆发，但OpenClaw生态持续处于高活跃状态：

* GitHub官方安全公告页面显示，3月26日集中发布了多条GHSA（High/Critical），包括Gateway Plugin子代理权限提升、HTTP Session History路由绕过Operator Read Scope、Feishu/Telegram/Webhook预认证解析、Matrix/BlueBubbles DM策略绕过等。
* CVE-2026-27183（授权绕过）作为近期重点，已被SentinelOne、NVD等多方收录并分析，核心成因是exec-wrapper-resolution.ts中approval classifier与execution planner的深度边界检查不一致（off-by-one），允许攻击者用精确4层透明dispatch wrapper绕过shell allowlist审批，实现未授权命令执行。受影响版本为<2026.3.7，已通过commit 2fc95a7修复。
* 今日多条高热度帖讨论OpenClaw最新更新（多代理默认开启、Telegram流式传输、安全+稳定性修复100+项），同时转发山东大学报告，强调AI编码代理在实际对抗中的脆弱性。

***PART 0****2***

**今日热度最高新动态**

安全社区今日最热议的是：山东大学研究团队的47种攻击场景实测报告（3月27日发布）：

* 测试覆盖提示注入、权限提升、数据外泄、沙箱逃逸、DoS等多种类别，OpenClaw高度依赖底层LLM安全防护，默认成功防御率仅17%-83%（随模型而异）。
* 报告明确指出“情绪操控”（guilt induction等社会工程提示）可诱导AI主动泄露数据、关闭保护甚至自我干扰，成为新型高关注向量。结
* 论一致推荐Human-in-the-Loop（HITL）作为核心防御，并呼吁加强技能市场监控。社区“OpenClaw安全性被实测攻破”“情绪操控AI泄密”等话题迅速发酵。

此外，OpenClaw官方同步推送包含大量安全修复的版本更新，社区同步发布《OpenClaw Security Handbook》，提醒140,000+暴露实例仍在被扫描攻击。

###

***PART 0****3***

**近期核心漏洞回顾**

**OpenClaw 核心漏洞表**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **GHSA/CVE** | **严重性** | **类型** | **影响版本** | **修复版本** |
| GHSA-fqw4-mph7-2vr8 | **9.4** | 权限提升 | < 2026.3.25 | 2026.3.25 |
| GHSA-9hjh-fr4f-gxc4 | **9.3** | 权限提升 | < 2026.3.25 | 2026.3.25 |

###

***PART 0****4***

**今日技术分析要点（社区最关注）**

**社区与安全研究团队今日最关注的问题是以下四点：**

**执行链边界漂移：CVE-2026-27183的核心是isTransparentDispatchWrapper函数中depth >= vs > MAX\_DISPATCH\_WRAPPER\_DEPTH的不一致，导致4层嵌套wrapper可绕过审批分类器，直接进入执行规划器。**

**AI代理对抗脆弱性：47场景测试显示，OpenClaw默认将安全责任推给LLM，提示注入+情绪操控可实现数据外泄、保护关闭等；HITL是唯一有效提升防御率的手段。**

**Webhook与Gateway共享风险：多条3月26日GHSA指向“先解析后验证”模式，攻击者可利用未认证请求体或跨域重定向窃取operator.admin作用域，进而实现RCE或会话劫持。**

**技能市场持续威胁：ClawHavoc恶意技能（539+个）及41%技能含高危漏洞的问题仍在发酵，Watchtower式持续监控需求强烈。**

**社区共识：OpenClaw功能强大但“安全是后加的”，暴露实例+技能盲装是最大现实风险。**

### ***PART 0****5*** **立即行动建议**

**立即升级：**若仍在使用原版OpenClaw，升级至最新稳定版本（至少2026.3.7或更高），优先采用NemoClaw单命令部署（支持本地/云/RTX）。

**强制隔离：**Docker/container运行，禁用管理员权限，仅授权必要目录；管理端口（默认18789）绝不暴露公网，用VPN/反向代理访问。

**技能与提示安全：**仅用官方/验证skill，安装Skill Vetter扫描器；禁用自动技能更新；所有密钥用环境变量/密钥管理器，绝不明文存prompt。

**操作确认：**开启二次确认（删除、发邮件等不可逆操作）；设置Token/消费上限；开启debug日志实时监控。

**额外防护：**禁用自动网页浏览或严格沙箱；企业/政府用户参考CNCERT建议，避免办公电脑直接运行；测试环境与生产彻底隔离。

立即执行以上措施，可将风险降至可控水平。持续关注GitHub advisories与NVD，OpenClaw安全仍处于“快速迭代补丁”阶段。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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