---
title: 每日安全动态推送(26/7/10)
url: https://mp.weixin.qq.com/s/PuTwL_SgUVWTtBHddegFkw
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:58:17.985093
---

# 每日安全动态推送(26/7/10)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dWDic6IAXZsfiaZW0JQviacCLMqWhF3SNibuLiadsQ0NIQTtMib9dtRNwicMAnvZMsHoH8R05VSkImpkiavrZ7h5ia6ZMew/0?wx_fmt=jpeg)

# 每日安全动态推送(26/7/10)

原创

admin
admin

腾讯玄武实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

•  GitLost：GitHub Agentic Workflows 间接提示注入漏洞
<https://sectoday.tencent.com/event/DNxxPp8B5M25NX6P7EYK>

Noma Security 研究人员披露了名为 GitLost 的严重安全漏洞，该漏洞利用 GitHub Agentic Workflows 中的间接提示注入技术。攻击者无需任何凭证，仅需在公共仓库中构造恶意的 GitHub Issue，即可嵌入隐藏指令，诱骗拥有广泛读取权限的 AI Agent 绕过内置安全护栏。该攻击利用了 Agent 将不可信的用户输入与特权系统指令混合处理的架构缺陷，导致私有仓库中的敏感代码和数据被泄露至公开评论中。此事件揭示了在自主 AI 驱动的 DevOps 流水线中，委托信任机制失效带来的重大风险，缓解措施需依赖严格的 Token 范围限制、输出约束及人工审核。

•  CVE-2026-49145：App::Ack 通过未受信任的 .ackrc 和 --files-from 导致的任意文件读取漏洞
<https://seclists.org/oss-sec/2026/q3/99>

本文揭示了 Perl 工具 App::Ack 中一个关键的任意文件读取漏洞（CVE-2026-49145），攻击者可通过恶意 .ackrc 配置文件利用未被加入黑名单的 --files-from 参数窃取敏感数据。该发现对于依赖 Perl 生态的开发者和安全团队至关重要，提醒其立即升级或采取临时缓解措施以防止供应链攻击。

•  SharePoint 远程代码执行 CVE-2025-53770 PoC 发布：利用 XSD 导入绕过 XmlValidator
<https://cybersecuritynews.com/poc-sharepoint-rce-vulnerability/>

本文独家披露了针对微软SharePoint Server关键RCE漏洞（CVE-2025-53770）的完整利用代码，详细解析了攻击者如何通过XML架构导入机制绕过官方补丁验证，利用ExcelDataSet组件实现无认证远程代码执行。鉴于该漏洞已在野外被大规模武器化利用，这篇文章为安全团队提供了紧急防御和威胁狩猎的关键技术细节。

•  签名可塑性：在不破坏签名的情况下重写 GitHub 已验证 Commit
<https://thehackernews.com/2026/07/github-verified-commits-can-be.html>

本文揭示了 Git 签名提交中一个长期被忽视的严重缺陷：攻击者无需私钥即可通过签名编码变异生成具有相同内容但不同哈希值的“已验证”提交，从而绕过基于哈希的黑名单和溯源机制。该研究不仅提供了可复现的攻击工具，更明确指出修复责任在于代码托管平台需实施签名标准化，而非开发者，对重塑软件供应链信任模型具有紧迫的现实意义。

•  利用 Realtek SD 读卡器 DMA 漏洞实现物理内存访问
<https://zwclose.github.io/2026/07/08/rtsper2.html>

本文揭示了Realtek SD卡读卡器驱动中一个被修复遗漏的关键漏洞，展示了攻击者如何通过用户态直接操控DMA控制器以读写物理内存。其最大亮点在于详细复现了从寄存器暴露到利用SCSI命令触发DMA攻击的完整技术路径，为理解硬件级内存窃取提供了极具价值的实战案例。

•  Rogue Agent：Google Dialogflow CX 关键漏洞利用共享运行时实现跨 Agent 劫持
<https://thehackernews.com/2026/07/rogue-agent-flaw-could-have-let.html>

本文揭示了Google Dialogflow CX中一个名为'Rogue Agent'的严重漏洞，攻击者仅需单一代码块编辑权限即可通过覆盖共享运行时文件，劫持同一项目下所有智能体并窃取敏感数据。该案例极具警示意义，它打破了AI安全仅关注提示注入的固有认知，深刻暴露了云原生AI开发环境中因沙箱隔离失效和权限模型设计缺陷而引发的底层代码执行风险。

•  ObfusGit：一款防止 AI 抓取公共仓库的 Python 加密工具
<https://trustedsec.com/blog/welcoming-obfusgit>

本文亮点在于介绍了一个由本地 LLM 快速生成的实用工具 ObfusGit，它通过自动加密机制让开发者在公开代码库时能有效抵御 AI 模型的自动爬取与训练。这一创新尝试为开源社区在生成式 AI 时代保护代码知识产权提供了低成本且即插即用的新思路。

•  当AI Coding编出不存在的包：53个可注册幻觉依赖如何变成供应链入口 - 安全内参 | 决策者的网络安全知识库
<https://www.secrss.com/articles/91900>

本文揭示了前沿代码模型中一种隐蔽的供应链攻击新范式——slopsquatting，即攻击者利用模型稳定生成的“共同幻觉”包名进行恶意注册。研究证实，尽管各模型幻觉率已收敛，但跨模型共同编造的127个高风险包名构成了可复用的攻击面，警示企业必须将AI生成的依赖视为不可信输入并实施严格的供应链门禁。

\* 查看或搜索历史推送内容请访问：
<https://sectoday.tencent.com/>
\* 新浪微博账号： 腾讯玄武实验室
<https://weibo.com/xuanwulab>
\* 微信公众号： 腾讯玄武实验室
![微信公众号： 腾讯玄武实验室](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HhcytTU2b7f8rnRPukk7nvILVtpLKXqtwJjSn3BaOEuWyfbDVqBB4Ex00ySOEz0A53o7YlzOvIWg1OukSR7w8ekicJcQpOBhDjUCibSlLuID8/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

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