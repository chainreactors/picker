---
title: 2025年全球威胁报告
url: https://mp.weixin.qq.com/s/VXLe45iuQ7TCPedFKGSNmQ
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:13:16.867438
---

# 2025年全球威胁报告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oCABd1XUc0jUqpExf9U93EOYKqgOAibogqgtiaQCl2LT6ia4qKe8dTnvW4TdADWdXU8f3LCQVcPeZ5ULj4uH2Vlx2ouicvY4lhgPw36X3H637pE/0?wx_fmt=jpeg)

# 2025年全球威胁报告

计算机与网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

报告指出，网络安全的核心冲突已从“预防”转向“上下文”，攻击者正利用AI实现高速、规模化攻击，将速度与效率置于隐蔽性之上。防御方必须超越简单阻断或存储历史数据，转而采用AI驱动的分析能力，在攻击发生时实时关联事件与历史模式，以实现快速、自信的决策。

一、关键趋势与发现

1. 攻击行为范式转变

战术优先级翻转：在Windows上，“执行”（Execution）已成为首要战术，占比32.05%，远超“防御规避”（Defense Evasion），标志着攻击者不再等待隐藏，而是追求“即入即执行”。

AI赋能犯罪：通用型威胁（Generic threats）激增15.5%，主要由攻击者利用大语言模型（LLMs）快速生成有效载荷所致，这要求防御体系从依赖静态签名转向行为分析与AI驱动检测。

浏览器成为主战场：超过1/8的恶意软件旨在窃取浏览器凭据，这些凭据是后续攻击链的“原材料”，传统身份控制已显不足。

源码泄露带来永久风险：一次意外的GitHub提交（如API密钥、护照照片）即可构成不可逆的分布式暴露。

2. 威胁分布与重点平台

操作系统：Windows仍是绝对主力，占所有签名相关检测的89.97%；Linux占比9%，但其高级攻击技术（如PUMAKIT）极具挑战性；macOS占比仅1.03%，但其高覆盖率使其成为发现先进攻击（如DPKR）的关键窗口。

云安全：攻击高度集中于三大目标——初始访问、持久化、凭证访问。Azure是最大攻击面，占异常信号的54.06%；AWS次之（36.83%）；GCP最少（9.11%）。

3. 主要威胁家族与技术

Windows：Trojan（64.49%）和Generic（23.53%）是两大主力。最常见的是GhostPulse（12.2%）、Lumma（6.67%）等。

Linux：威胁以“被 commoditized malware”为主，如Silver、Mythic、Metasploit。其攻击常通过Shell直接执行，强调“动手入侵”风格。

macOS：Metasploit（25.66%）为最大威胁，Cryptominers（17.70%）和Info stealers（13.27%）也占据重要位置。

核心技术：Command and Scripting Interpreter（21.62%）是最高频技术；Defense Evasion（32.05%）是最高频战术；Browser Credential Theft（19,000+样本）是关键风险点。

二、内部洞察与研究贡献

1. Elastic 内部防护能力

机器学习模型：Elastic Endpoint 的多层防护体系基于数百万恶意与良性样本训练，能高效识别新旧威胁。其模型在内部测试中表现卓越，TPR >98%，FPR <0.5%。

特权访问检测：预构建的“Privileged Access Detection”包包含21个跨平台ML作业，可高效识别管理员等高权限用户的可疑行为。

主机异常检测：Security: Host 预建作业可用于检测主机流量中的突发峰值或下降，从而识别系统被攻陷、DDoS或数据外泄等事件。

2. 客户零视角（Customer Zero）故事

“Commit”-ment 问题：内部团队曾因GitHub误操作导致用户护照照片被上传至公共分支，虽未合并，但已构成敏感数据泄露，凸显了代码版本控制的长期风险。

误认身份：一个非Elastic账户的开发者因本地Git配置错误，将真实Elastic账号作为作者推送了更改，揭示了自动化工具与人工操作结合时的潜在风险。

三、重点威胁案例

BANSHEE：一款针对macOS的新型信息窃取者，可从系统和浏览器中窃取大量数据，其简洁架构使其威胁性显著。

EDDIESTEALER：一款通过社会工程学（ClickFix）获取初始访问的Rust编译器，能窃取Chrome会话数据并将其通过HTTP POST发送至攻击者服务器。

PUMAKIT：一个高级Linux后门，采用模块化、多阶段架构，具备内核级隐蔽性和精准系统定位能力，已被Elastic成功检出。

FINALDRAFT：一个围绕南美外交部门展开的定向间谍活动，利用Microsoft Graph API进行双向通信，并通过定制化工具链（如PATHLOADER）实现远程命令控制。

ARECHCLIENT：一个利用“ClickFix”技术的多阶段攻击框架，通过GHOSTPULSE加载器部署最终恶意载荷（如ARECHCLIENT2），形成完整的攻击闭环。

四、核心建议

自动化与人机协同：采用AI辅助检测与响应，加速决策，但需保留人类分析师在关键节点上的判断权。

强化浏览器防御：浏览器凭据库是高价值目标，应加强插件、扩展及第三方集成的加固。

提升身份验证：持续投资强身份验证（KYC）实践，确保第一道防线的安全。

聚焦内存保护：攻击者持续利用内存技术，企业应重视对注入、混淆等行为的监控。

保障开发与供应链安全：加强对IDE、包管理器及第三方库的观察与检测，防范供应链攻击。

本文原文件及下列文件

[点这里自助下载](https://mp.weixin.qq.com/s?__biz=MjM5OTk4MDE2MA==&mid=2655293752&idx=4&sn=542faf284cbe4c38f4d8ca79773c5327&scene=21#wechat_redirect)

2025年全球威胁报告.pdf

网络安全运营体系建设方案.docx

GB∕T 37939-2026 网络安全技术 网络存储安全技术要求.pdf

GB∕T 47697-2026 网络安全技术 鉴别与授权 基于属性的访问控制模型与管理规范.pdf

GB∕T 20274.2-2026 网络安全技术 信息系统安全保障评估框架 第2部分：安全保障要求.pdf

网络取证隐私与安全.pdf

2026年网络安全人才研究报告.pdf

2026年全球威胁态势研究报告.pdf

2025年度软件供应链安全态势分析报告.pdf

零信任能力成熟度模型.pdf

2025年网络安全状况特点及2026年趋势研判.pdf

GB∕T 22081-2024 网络安全技术 信息安全控制.pdf

GB∕T 22080-2025 网络安全技术 信息安全管理体系 要求.pdf

GB∕T 31595-2025 安全与韧性 业务连续性管理体系 GB∕T 30146 使用指南.pdf

GBT 30146-2023 安全与韧性 业务连续性管理体系 要求.pdf

信息化项目绩效审计规范.pdf

信息通信行业网络安全保险服务实施指南.pdf

电信网和互联网勒索软件防范指南.pdf

人工智能在网络安全分析与网络威胁检测中的应.pdf

邮件系统安全防护要求营.pdf

电信和互联网软件供应链安全 技术能力建设指南.pdf

2026年度开源安全与风险分析报告.pdf

电信和互联网软件供应链安全 软件产品供应链安全要求.pdf

ENISA：网络安全市场分析框架 V3.0.pdf

通信行业信息安全托管运营服务实施指南.pdf

网络安全演练方法论.pdf

网络安全与取证技术的前沿进展及应用.pdf

网络安全风险管理实践.pdf

2025年度网络安全应急响应总结报告.pdf

网络安全运营.pdf

网络安全运营大模型参考架构.pdf

开源安全治理最佳实践（2026）.pdf

健康医疗信息零信任安全访问控制应用规范.pdf

网络安全威胁态势评估方法论.pdf

纵深防御：现代网络安全策略和不断演变的威胁.pdf

网络安全服务责任及损失评估标准.pdf

全球网络安全政策法律发展年度报告（2025）.pdf

2026网络供应链攻击的影响及缓解策略.pdf

安全运营中心：网络安全路线图.pdf

[加入网络安全社群](https://mp.weixin.qq.com/s?__biz=MjM5OTk4MDE2MA==&mid=2655303936&idx=2&sn=ae07eb64654d3e4471be32e7d2c52d13&scene=21#wechat_redirect)

-

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VcRPEU1K2ocHOjGZiciaQiaQiaib4dQ6cgtlqv30oqJVBYiaoB9PGibNlE3IibJblQWCH8E2PEj3YZKib7iaR2Bj3G8GJaGg/0?wx_fmt=png)

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