---
title: DifyTap 暴露 AI 聊天和文档：多租户 AI 平台，不能只看模型能力
url: https://mp.weixin.qq.com/s/Mur29N7HoPgnDnK07vOwtg
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:05:00.782969
---

# DifyTap 暴露 AI 聊天和文档：多租户 AI 平台，不能只看模型能力

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nOo5YmK1PHz69qNNK4B4kK46iafCTUuA2FMKTLplBFy0SKqzqtteg7x4wJ2d2gnkZsGO1QgH3OeMsQxDmwKwg22pbeFOJHSxRQS6PpxNCtVc/0?wx_fmt=jpeg)

# DifyTap 暴露 AI 聊天和文档：多租户 AI 平台，不能只看模型能力

原创

tcode
tcode

字节脉搏实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

摘要：Zafran 披露 Dify 平台的四个漏洞，称其中两个为严重级别、两个无需认证，且多个问题具有跨租户影响。SecurityWeek 6 月 23 日报道，这些缺陷可能让攻击者读取私有 AI 对话、预览其他租户文档并触达内部 API。对企业来说，AI 平台进入生产后，租户隔离、文件预览、插件守护进程和日志追踪都必须纳入安全基线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nOo5YmK1PHzPvBnCBJYXa5ZXjpNy4s8xGT5RrE5El8PHmg0ogiaYrxDGiceFH4HIicdNPLRVqAibsKh70C3YJ12RkqbOIia3hgFwqQpOfBR4waQs/640?wx_fmt=png&from=appmsg)

事件概述
    AI 应用平台 Dify 被披露存在一组被命名为 DifyTap 的安全缺陷。Zafran 于 2026 年 6 月 22 日发布研究称，其发现四个漏洞，其中两个为严重级别，两个无需认证，三个在 Dify 多租户云服务中具有跨租户影响。
    SecurityWeek 在 6 月 23 日报道，这些缺陷可能允许攻击者读取其他客户应用的私有聊天、触发跨租户内部 API 调用、预览其他租户上传的文档，以及泄露同一租户内其他用户的文件。Dify 是一个用于创建、部署、维护和监控 AI 应用的开源 LLMOps 平台，公开报道称其支撑超过 100 万个应用。
    本文不提供漏洞复现路径、接口细节或可操作利用步骤。更值得关注的是：AI 应用平台不只是“套模型”，它包含租户、插件、文件、日志、追踪和内部服务调用。任何一个边界没守住，都可能让 AI 对话和企业文档暴露。

![](https://mmbiz.qpic.cn/mmbiz_png/nOo5YmK1PHy6DYXCic210neIgPQbBsf1yBx1xVVEm9qQZ3UichTsO0lfCU7tDcKQrBPesibX3FubiaHe6edQLaFPkWGvNJ1RmXDbWG6KNfLoFtU/640?wx_fmt=png&from=appmsg)

核心事实
    第一，Zafran 披露 DifyTap 共涉及四个漏洞，并称其中多个影响 Dify 的多租户云服务，可能导致跨租户数据暴露。
    第二，公开描述涉及私有聊天记录、上传文档预览、内部 API 访问和同租户文件访问边界。SecurityWeek 报道了 CVE-2026-41947、CVE-2026-41948、CVE-2026-41949 和 CVE-2026-41950。
    第三，Zafran 称 CVE-2026-41947、CVE-2026-41949、CVE-2026-41950 已在 Dify 1.14.2 修复；CVE-2026-41948 的修复已合并并将随后续版本提供，同时给出了缓解建议。
    第四，这类风险的影响不仅取决于漏洞本身，也取决于企业把什么数据交给 AI 平台：客户对话、内部知识库、合同、工单、源代码片段、会议摘要和运维文档，都会提高后果严重性。
影响分析
    对业务团队来说，AI 平台经常被快速接入知识库、客服、销售助手、内部问答和文档检索。如果这些系统出现跨租户或文件访问边界问题，泄露的可能不是单一账号数据，而是一段段原本只给内部员工或客户可见的业务语境。
    对安全团队来说，AI 平台的攻击面比传统 Web 应用更复杂。除了登录、权限和 API，还要关注插件系统、文件解析、向量库、会话记录、追踪日志、外部工具调用、内部服务代理和模型上下文。
    对管理层来说，这类事件说明 AI 采购和自建平台不能只问“能不能接入模型”“能不能上线 Agent”，还要问“租户隔离怎么做”“文件预览是否隔离”“插件权限如何收敛”“聊天记录是否可审计和可删除”。
应对建议
     立即确认 Dify 部署方式和版本。区分云服务、自托管、测试环境和生产环境，并核对是否已升级到官方修复版本或应用临时缓解。
    排查外网暴露实例。对互联网可访问的 Dify 控制台、API、插件服务和文件预览入口做资产确认，关闭不必要的公开访问。
    审计 AI 会话和文档访问。检查是否存在异常访问、批量预览、跨应用读取、陌生用户会话和异常内部 API 调用迹象。
    限制敏感数据进入 AI 平台。客户隐私、密钥、合同、源代码、财务信息和内部安全文档进入 RAG 或知识库前，应先做数据分级和脱敏策略。
    收紧插件和工具调用权限。插件守护进程、内部 API 代理和外部工具连接应采用最小权限，不应默认继承平台高权限。
    分离测试和生产。不要让测试应用、演示应用和生产知识库共享同一套高权限 token、文件存储或内部服务访问路径。
    建立 AI 平台安全基线。至少包括身份认证、租户隔离、日志审计、文件访问控制、依赖更新、插件准入和数据保留策略。
事实、推测与观点区分
    事实：Zafran 披露 DifyTap 四个漏洞，SecurityWeek 于 2026 年 6 月 23 日报道这些漏洞可能暴露私有聊天、其他租户文档和内部 API；Dify 1.14.2 已修复其中三项，另一项按 Zafran 说明已有合并修复并需关注后续版本与缓解措施。
    合理推测：已经把客户对话、内部知识库或文档上传到 Dify 的企业，其潜在影响会高于只做本地测试或空应用验证的环境。
    本文观点：AI 平台安全的核心不是“模型安全”四个字，而是应用平台的每一层边界是否真的隔离。
结语
    AI 应用上线越快，越不能把平台安全留到最后。多租户、插件、文件预览和追踪日志，这些看似工程细节的组件，决定了 AI 对话和企业文档是否真的只属于它们该属于的人。
关键来源
• Zafran, “DifyTap: Zafran discovers how attackers can silently wiretap AI data across tenants on a platform powering 1M+ apps”, 2026-06-22: https://www.zafran.io/resources/difytap-zafran-discovers-how-attackers-can-silently-wiretap-ai-data-across-tenants-on-a-platform-powering-1m-apps
• SecurityWeek, “Data Exposure Flaws Threaten Dify AI Platform Used by 1 Million Apps”, 2026-06-23 11:36 AM ET: https://www.securityweek.com/data-exposure-flaws-threaten-dify-ai-platform-powering-over-1-million-apps/
• The Hacker News, “Researchers Detail DifyTap Flaws in Dify That Could Expose AI Chats Across Tenants”, 2026-06-23: https://thehackernews.com/2026/06/researchers-detail-difytap-flaws-in.html

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ia3Is12pQKnIPvX43Bm5RTfn38gGrVIvGtiaMrLfFqknYBzOd4wmQb1Ra7InwkMM5Ru09FTZ6ibhcLiagpiannxZdlA/0?wx_fmt=png)

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