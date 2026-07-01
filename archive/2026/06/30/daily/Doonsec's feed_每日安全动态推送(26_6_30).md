---
title: 每日安全动态推送(26/6/30)
url: https://mp.weixin.qq.com/s/8zWXIW7DzEjVpStA8d1B9w
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:21:23.832841
---

# 每日安全动态推送(26/6/30)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dWDic6IAXZsfiaZW0JQviacCLMqWhF3SNibuLiadsQ0NIQTtMib9dtRNwicMAnvZMsHoH8R05VSkImpkiavrZ7h5ia6ZMew/0?wx_fmt=jpeg)

# 每日安全动态推送(26/6/30)

原创

admin
admin

腾讯玄武实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

•  Bucket Hijacking：利用全局名称唯一性劫持云数据流
<https://cybersecuritynews.com/bucket-hijacking-attack/>

本文揭示了名为“存储桶劫持”的致命云攻击技术，攻击者利用云存储桶名称全局唯一的架构缺陷，在删除并重建同名存储桶后，能悄无声息地将组织的审计日志和遥测数据重定向至其控制端。该研究不仅证实了攻击在 AWS、GCP 和 Azure 三大平台上的可行性，更强调了其“自我维持”且难以被原生监控发现的隐蔽特性，为云安全防御提供了关键的预警与缓解方案。

•  DirtyClone：利用克隆数据包和文件映射内存的 Linux 内核提权新漏洞
<https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html>

本文揭示了 DirtyClone 漏洞如何通过 IPsec 隧道在内存中静默篡改二进制文件，其最大亮点在于展示了攻击者无需修改磁盘即可绕过文件完整性检测获取 root 权限。作为 DirtyFrag 系列的最新变种，该文章不仅提供了首个公开利用演示，更深刻剖析了 Linux 内核在零拷贝网络优化中因标志位丢失而引发的系统性设计缺陷，对多租户环境和容器安全具有极高的警示价值。

•  从 context\_handle 到类型混淆：利用 Windows RPC 服务器中的 FC\_BINDING\_CONTEXT 漏洞
<https://whereisk0shl.top/post/From%20context_handle%20to%20type%20confusion/>

本文揭示了 Windows RPC 服务中因 IDL 定义中 `BIND\_CONTEXT` 类型缺乏跨类型验证而导致的新型类型混淆攻击模式。作者通过深入逆向分析 RPC 运行时机制，不仅成功复现了 CVE-2025-48815 等高危漏洞，还提出了一套可自动识别此类攻击面的通用方法论。

•  Cisco SD-WAN 零日漏洞致通信服务商 Root 权限失陷事件
<https://sectoday.tencent.com/event/Ql3b_Z4BVJfJhgnJq_lj>

威胁行为者在 Cisco 披露前两个月利用 Cisco Catalyst SD-WAN Manager 中的零日漏洞 CVE-2026-20245，针对某通信服务提供商发动了高级持续性攻击。攻击者首先通过非法对等连接（Rogue Peering）和认证绕过漏洞获取初始访问权限，随后上传恶意 CSV 载荷触发命令注入，成功将权限提升至 Root 级别。攻击者创建了隐藏的 'troot' 账户以维持持久访问，并篡改 /etc/passwd 和 /etc/shadow 等系统文件，同时采用复杂的反取证技术抹除入侵痕迹以规避检测。此次事件凸显了攻击者利用边缘网络设备绕过传统安全边界以获取内部网络流量监控能力的战术，被定性为与国家级网络间谍活动一致的严重安全事件。

•  CVE-2026-41613：VS Code MCP 安装流程漏洞导致远程代码执行与会话劫持
<https://www.cybersecurity-insiders.com/what-the-visual-studio-code-vulnerability-reveals-about-ai-tooling-risk/>

本文揭示了VS Code中MCP安装流程的严重漏洞（CVE-2026-41613），攻击者利用界面未显示的隐藏字段即可实现远程代码执行或静默劫持开发者会话。这一发现不仅暴露了AI工具在快速集成中忽视的“信任边界”风险，更警示安全团队必须立即升级并建立针对非人类AI代理的严格治理框架。

•  驯服 AI 工具泛滥：利用 PowerShell 与 Microsoft Graph 审计未授权 AI 应用
<https://adamtheautomator.com/taming-ai-tool-sprawl-powershell-guide-auditing/>

本文的核心亮点在于提供了一套基于 PowerShell 和 Microsoft Graph API 的实战方案，能够精准审计并量化组织内未经授权的 AI 应用风险，将模糊的“影子 IT"问题转化为可执行的治理报告。在 AI 工具泛滥导致数据泄露风险激增的当下，这篇教程为安全团队提供了立即落地的身份侧防御手段，填补了从发现到管控的关键技术空白。"

•  绕过 AI Agent Skill 扫描器：一个虚假 Skill 如何通过外部链接触达 26,000 个 Agent
<https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html>

本文通过精心设计的实验，揭示了当前AI代理技能扫描器存在致命的“外部链接盲区”，即攻击者可利用审查后篡改的远程指令绕过所有静态检测。这一发现警示安全社区必须将技能视为动态软件而非静态文本，立即重构信任模型以应对外部依赖带来的供应链风险。

\* 查看或搜索历史推送内容请访问：
<https://sectoday.tencent.com/>
\* 新浪微博账号： 腾讯玄武实验室
<https://weibo.com/xuanwulab>
\* 微信公众号： 腾讯玄武实验室
![微信公众号： 腾讯玄武实验室](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HhcytTU2b7ddotodRYdvA2niaEXowlo6ibMNT1qU5yrRGcYToKXwgDibak1v0YNrO4aMuEYUiabt8xu4xVh6V8FCt5LWyMEzsbun5T2Um03xgsc/640?wx_fmt=jpeg&from=appmsg)

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