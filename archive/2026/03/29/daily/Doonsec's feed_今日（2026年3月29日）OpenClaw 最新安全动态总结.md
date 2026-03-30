---
title: 今日（2026年3月29日）OpenClaw 最新安全动态总结
url: https://mp.weixin.qq.com/s/F1swy13ZrX_xEB-PTWIVXw
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:41:41.416742
---

# 今日（2026年3月29日）OpenClaw 最新安全动态总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555uY3JaLf3D42OPmicicKx3E1PPkNLZicjA4uZKJgGzgNicoL9ZQdc8fJQndDozx0CD8VWO39OF7ickncku8NBuKhPdp7rtlSCMGOfOU/0?wx_fmt=jpeg)

# 今日（2026年3月29日）OpenClaw 最新安全动态总结

奇安信 CERT

![]()

在小说阅读器中沉浸阅读

**3月29日资讯导视**

OpenClaw v2026.3.28 版本今日发布，移除弃用 Qwen OAuth 集成并强化多平台凭证审计，安全防护进一步升级。

CVE-2026-32895（Slack 系统事件处理器授权绕过，中危）持续引发社区讨论，旧版本仍存在 allowlist 绕过风险。

OpenClaw 暴露实例与供应链安全担忧未消，社区重点关注 webhook 授权、沙箱逃逸及插件恶意代码问题，呼吁立即更新并收紧权限。

***PART 0****1***

**今日核心事件**

OpenClaw 官方于今日推送 v2026.3.28 重大更新。该版本核心安全改进包括：彻底移除弃用的 Qwen OAuth 集成（旧配置不再自动迁移，老 key 将校验失败）；扩展 web search key 审计范围，新增对 Gemini、Grok/xAI、Kimi、Moonshot、OpenRouter 等凭证的边界安全检查；同时优化 OpenAI/Codex apply\_patch 默认启用并对齐 sandbox 写权限策略。这是近期针对凭证泄露和第三方集成风险的针对性加固。

***PART 0****2***

**今日热度最高新动态**

今日安全社区对 v2026.3.28 版本讨论最热，多位开发者实时分享更新内容，并提及“安全升级更彻底”。另有帖子指出 OpenClaw 在个人生产力场景仍有优势，但企业部署仍谨慎，强调需人类在环与 guardrail。无新零日攻击或大规模利用报告，但旧漏洞讨论与新版本安全特性形成鲜明对比，成为今日热度焦点。

###

***PART 0****3***

**近期核心漏洞回顾**

**OpenClaw 核心漏洞表**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **GHSA/CVE** | **严重性** | **类型** | **影响版本** | **修复版本** |
| CVE-2026-32895 | **5.4** | 授权不当 | < 2026.2.26 | 2026.2.26 |

***PART 0****4***

**今日技术分析要点（社区最关注）**

**社区与安全研究团队今日最关注点集中在“授权与边界控制”：**

* **Slack/Feishu/Telegram 等聊天平台 webhook 与 system event handler 的 sender authorization bypass 机制（以 CVE-2026-32895 为代表），攻击者可伪造非 allowlist 发送者事件，实现会话状态突变或绕过 DM 配对。**
* **新版本安全审计扩展（web search key + SecretRef 强化）被视为对早期凭证泄露（如 CVE-2026-25253 token theft RCE）的后续补强，但社区提醒：仍需手动验证所有第三方技能（ClawHub 历史曾出现 15%+ 恶意 prompt）。**
* **暴露实例与供应链风险：虽无今日新扫描数据，但历史 17k-135k 暴露实例 + 恶意技能持续被提及，技术讨论聚焦“localhost-bound 实例仍可被浏览器恶意页面劫持”及 sandbox writeFile race/path traversal 类问题。GitHub 追踪器与 VulnCheck 等平台分析显示，49% 漏洞与 allowlist 相关，是当前 OpenClaw 架构最大痛点。**

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