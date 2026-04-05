---
title: 今日（2026年4月4日）OpenClaw 最新安全动态总结
url: https://mp.weixin.qq.com/s/HqUz4pyzDErPAW7IEB2qjA
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:33:21.990407
---

# 今日（2026年4月4日）OpenClaw 最新安全动态总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555sIvW74lQSZdkw9TheJn2MVZEZEh2zJD9Nhhkdxm39eVcjeA1ZF9u1fR7COicnkJ2mobJHBmtQZNmUIgrFQ7C6hjQqYaIyEfibLQ/0?wx_fmt=jpeg)

# 今日（2026年4月4日）OpenClaw 最新安全动态总结

奇安信 CERT

![]()

在小说阅读器中沉浸阅读

**4月4日资讯导视**

Anthropic今日起正式切断Claude订阅对OpenClaw等第三方工具的支持，用户需转向按量付费或API密钥。

OpenClaw曝出高危权限提升漏洞CVE-2026-33579，开发者紧急发布三高危漏洞补丁，安全专家警告用户“假设已遭入侵”。

OpenClaw生态安全风险持续发酵，社区高度关注权限继承与供应链投毒问题，呼吁立即升级与审计。

***PART 0****1***

**今日核心事件**

Anthropic官方切断Claude订阅支持：4月4日12:00 PT（北京时间4月5日03:00）起，Claude Pro/Max/Team订阅不再覆盖OpenClaw等第三方Harness的使用。用户收到邮件通知，现有订阅额度无法继续用于OpenClaw，必须购买额外Usage Bundle或切换API密钥。此举直接影响依赖Claude驱动OpenClaw的自动化工作流（如邮件管理、浏览器控制、企业工具集成）。

CVE-2026-33579高危权限提升漏洞披露与紧急修复：OpenClaw 2026.3.28之前版本存在/pair approve命令路径的调用者作用域（caller scopes）验证缺失，低权限用户（pairing privileges）可直接升级为管理员权限，继承实例所有访问权（Telegram、共享网盘、浏览器会话、Slack/Discord等）。开发者已发布补丁，覆盖三个高危漏洞。

***PART 0****2***

**今日热度最高新动态**

Anthropic的订阅政策变动在Reddit、Hacker News等平台迅速刷屏，成为今日OpenClaw相关最高热度话题。用户反馈集中于“突然断供”“成本暴增”“被迫迁移”。同时，CVE-2026-33579的NVD条目与“Assume Compromise”警告文章同步传播，社区讨论焦点从“使用成本”快速转向“安全假设已入侵”。ClawHavoc恶意Skill存量风险（此前审计显示539个热门Skill受感染）也被再次提及，形成“政策+漏洞+供应链”的三重热点叠加。

###

***PART 0****3***

**近期核心漏洞回顾**

**OpenClaw 核心漏洞表**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **GHSA/CVE** | **严重性** | **类型** | **影响版本** | **修复版本** |
| CVE-2026-33579 | **8.6** | 权限提升 | < 2026.3.28 | 2026.3.28 |
| CVE-2026-34511 | **6.0** | 安全特性绕过 | < 2026.4.2 | 2026.4.2 |

***PART 0****4***

**今日技术分析要点（社区最关注）**

**社区与安全研究团队今日最关注的仍是CVE-2026-33579的权限继承机制：低权限用户通过构造/pair approve请求，可绕过作用域验证，直接获得实例完整管理员权限。OpenClaw的Agentic设计本意是让AI拥有“系统级访问”（浏览器、Telegram、Slack、企业Drive），一旦权限升级，攻击者即获得“全盘接管”能力。**

**技术根源在于：**

**1) 配对流程未严格校验调用者上下文；**

**2) 权限继承模型过于宽松，未实施最小权限原则；**

**3) 高权限Skill普遍缺少config.json权限清单（99.3% Skill无manifest）。**

**叠加ClawHavoc供应链投毒（npm依赖未锁定、凭证泄露、未授权网络调用），形成“初始入侵→权限提升→持久化控制”的完整攻击链。**

**社区共识：OpenClaw当前架构在零信任缺失的情况下，任何单点逻辑缺陷都可能导致毁灭性后果。**

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