---
title: 今日（2026年4月5日）OpenClaw 最新安全动态总结
url: https://mp.weixin.qq.com/s/qP8fGtRNXHfK7AnDFPnpmQ
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:40:42.835332
---

# 今日（2026年4月5日）OpenClaw 最新安全动态总结

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RwAbCjh555uyttwa8BS6BawFJoME9LyZiaGrphup4YfIUpftCA2iaMDqQVjr5AicSFVxH20McXvR1Z0XumiaAOOc4AGzuzBJYUcLQaQ9FNqPAQg/0?wx_fmt=jpeg)

# 今日（2026年4月5日）OpenClaw 最新安全动态总结

奇安信 CERT

![]()

在小说阅读器中沉浸阅读

**4月5日资讯导视**

OpenClaw CVE/GHSA自动追踪器于今日完成最新同步，纳入截至4月4日的全部安全公告，继续监控授权绕过与沙箱逃逸类高危问题。

CVE-2026-33579（权限提升漏洞，CVSS 8.1-9.8）近期补丁（2026.3.28版）引发社区热议，Ars Technica等媒体提醒用户“假设已遭入侵”，低权限设备即可静默提权至admin。

OpenClaw安全公告已累计137条（2026年2-4月），授权绕过（CWE-863）占比近半，社区持续呼吁立即升级并审查配对日志。

***PART 0****1***

**今日核心事件**

今日（4月5日）暂无OpenClaw官方或主流媒体披露全新零日漏洞或重大安全事件。核心动态为GitHub自动化仓库[jgamblin/OpenClawCVEs](https://github.com/jgamblin/OpenClawCVEs/)于00:47 UTC完成小时级更新，同步了GitHub Advisory Database、cvelistV5及项目自身安全公告的最新状态。这是该追踪器日常维护的一部分，但反映出OpenClaw安全问题仍处于持续高频披露与修复周期中。

与此同时，4月3日Ars Technica发布的分析文章（4月5日仍在被广泛转发）将焦点放在“较早本周”发布的三个高危补丁上，尤其是CVE-2026-33579，强调即使本地运行的AI代理也可能被低权限设备静默接管。安全社区今日讨论多为用户使用心得，少数提及“privilege escalation vulnerability”并链接HN讨论，热度延续自4月4日。

***PART 0****2***

**今日热度最高新动态**

安全社区当前最热话题仍是CVE-2026-33579权限提升漏洞的落地影响。该漏洞允许持有最低`operator.pairing`权限的调用方，在`/pair approve`路径中绕过作用域检查，直接批准要求`operator.admin`权限的设备配对请求，从而实现完整实例接管。

* 技术根因：`extensions/device-pair/index.ts`未将调用者作用域转发至`src/infra/device-pairing.ts`的核心审批函数。
* 影响：攻击者可读取所有连接数据源、窃取凭证、执行任意工具调用并横向渗透。
* 补丁版本：2026.3.28（约3月29日发布），NVD于3月31日正式收录，Ars Technica称补丁周日发布但CVE周二才上线，留出短暂利用窗口。

今日安全社区上多条转发均强调“63%的暴露实例未启用认证，进一步放大风险”。

###

***PART 0****3***

**近期核心漏洞回顾**

**OpenClaw 核心漏洞表**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **GHSA/CVE** | **严重性** | **类型** | **影响版本** | **修复版本** |
| GHSA-9jpj-g8vv-j5mf | **7.0** | 安全特性绕过 | <= 2026.4.1 | 2026.4.2 |

***PART 0****4***

**今日技术分析要点（社区最关注）**

**社区与安全研究团队今日最关注的问题是权限模型设计缺陷：**

* **OpenClaw采用“operator.pairing → operator.admin”分层模型，但`/pair approve`路径未严格校验调用者作用域，导致低权限实体可自提升为admin。**
* **结合63%实例未开启认证的事实，一旦配对令牌泄露或通过钓鱼获取低权限访问，即可实现“零交互”完整接管。**
* **更深层问题是OpenClaw架构本身：本地AI代理需高系统权限执行工具调用、技能安装与文件操作，任何授权绕过都直接映射到宿主机RCE或数据外泄。**

**技术社区强调：即使升级到最新版，也应结合`openclaw security audit`命令、严格网络隔离（不暴露公网）、技能沙箱与日志审计（重点检查/pair事件）。Ars Technica直言“效率收益已被安全风险抵消，建议重新评估是否继续使用”。**

### ***PART 0****5*** **立即行动建议**

**立即升级：**若仍在使用原版OpenClaw，升级至最新稳定版本（2026.3.28或更高），优先采用NemoClaw单命令部署（支持本地/云/RTX）。

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