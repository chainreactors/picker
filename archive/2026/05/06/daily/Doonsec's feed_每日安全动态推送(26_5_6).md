---
title: 每日安全动态推送(26/5/6)
url: https://mp.weixin.qq.com/s/hZe3Rg6jXoAfow0rMBKZ7w
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:25:33.461777
---

# 每日安全动态推送(26/5/6)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dWDic6IAXZsfiaZW0JQviacCLMqWhF3SNibuLiadsQ0NIQTtMib9dtRNwicMAnvZMsHoH8R05VSkImpkiavrZ7h5ia6ZMew/0?wx_fmt=jpeg)

# 每日安全动态推送(26/5/6)

原创

admin
admin

腾讯玄武实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

•  Bleeding Llama：Ollama 严重未认证堆溢出漏洞致 30 万部署面临数据窃取风险
<https://www.securityweek.com/critical-bug-could-expose-300000-ollama-deployments-to-information-theft/>

本文揭示了影响全球约 30 万台 Ollama 部署的严重未认证漏洞（Bleeding Llama），攻击者仅需三次 API 调用即可窃取包含 API 密钥和敏感提示词的堆内存数据。鉴于该漏洞默认暴露于公网且无需凭证即可利用，其紧迫性要求所有组织立即升级补丁并实施网络隔离。

•  cPanel CVE-2026-41940 认证绕过漏洞导致全球大规模入侵与勒索软件爆发
<https://sectoday.tencent.com/event/3Ufp5p0BVJfJhgnJmJZi>

2026 年，cPanel、WHM 及 WP Squared 产品中爆发了严重的认证绕过漏洞（CVE-2026-41940），该漏洞源于 Session.pm 模块中的 CRLF 注入缺陷，允许未认证攻击者通过伪造 Authorization 头直接获取 root 权限。漏洞披露后迅速被武器化，公开的概念验证（PoC）工具 cPanelSniper 和 authbypass-RCE.py 被广泛传播，导致全球超过 44,000 台服务器沦陷，影响数百万域名。攻击活动呈现出高度组织化特征，未知威胁组织针对东南亚政府机构、军事部门及 MSP 网络发起定向攻击，利用 SQL 注入与 AdaptixC2 框架窃取敏感铁路文档；同时，大规模自动化攻击部署了 Mirai 僵尸网络变种及名为'Sorry'的勒索软件，后者采用 ChaCha20 和 RSA-2048 加密算法锁定文件。鉴于其 CVSS 评分高达 9.8 且修复截止日期已过，美国网络安全和基础设施安全局（CISA）已将该漏洞列入已知被利用漏洞（KEV）目录，强制要求联邦机构立即修补或停用受影响产品，全球安全社区正紧急呼吁应用补丁或封锁 2083、2087、2095 及 2096 端口以遏制威胁蔓延。

•  MOVEit Automation 关键认证绕过与权限提升漏洞
<https://sectoday.tencent.com/event/CPJd9p0B5M25NX6PkiL4>

Progress Software 发布了紧急补丁，修复了由其合作伙伴 Airbus SecLab 研究人员发现的 MOVEit Automation 中的两项严重漏洞。其中，CVE-2026-4670 是一个关键级别的身份验证绕过漏洞（CVSS 9.8），允许攻击者通过后端命令端口绕过认证；CVE-2026-5174 是一个输入验证缺陷（CVSS 7.7），可导致权限提升。利用这些漏洞，攻击者能够获取系统的完全控制权、访问敏感数据并危及企业网络。受影响的版本包括 2025.1.4、2025.0.8 及 2024.1.7 等早期版本，且目前无临时缓解措施，用户必须通过完整安装程序升级至最新补丁版本。此次事件引发了全球对 MOVEit 系列工具安全性的关注，特别是考虑到该系列软件曾在 2023 年被勒索软件组织利用，目前全球已有超过 1,440 台联网设备（含政府机构）运行易受攻击的版本。

•  间接提示注入：恶意脚本如何利用注释噪声和大文件绕过 AI 代码审查
<https://securitybrief.asia/story/cloudflare-warns-of-ai-code-review-prompt-injection>

本文揭示了攻击者如何利用代码注释中的间接提示注入和“上下文淹没”技术，将AI代码审查的误报率从67%骤降至12%，暴露了当前自动化安全流程在对抗大规模良性代码伪装时的致命结构性弱点。这项研究不仅量化了不同模型在语言偏见和文件大小上的脆弱性，更为企业部署AI安全工具提供了关键的防御策略参考。

•  CVE-2026-26268：通过恶意 Git Hooks 在 Cursor AI 中实现任意代码执行
<https://gbhackers.com/cursor-ai-coding-agent-vulnerability/>

本文揭示了 CVE-2026-26268 这一关键漏洞，证明攻击者如何利用 AI 代理的自主性与 Git 钩子结合，在无需用户交互的情况下通过看似合法的操作实现静默代码执行。该研究不仅暴露了开发者环境这一被忽视的攻击面，更标志着安全威胁建模必须从单一漏洞转向复杂交互模式的重大范式转变。

•  沉默的观察者：AI 会议助手如何引发关键内部威胁与 OAuth 攻击向量
<https://www.cybersecurity-insiders.com/the-most-dangerous-enterprise-insider-threat-comes-with-a-free-trial/>

本文深刻揭示了企业广泛采用的AI会议助手如何因过度权限（OAuth）和未经审查的数据外流，演变为比传统网络攻击更隐蔽的内部威胁。文章不仅剖析了从数据主权到法律合规（如GDPR及多方录音同意法）的致命风险，更警示了AI工具在缺乏上下文感知的情况下对商业机密和信任体系的系统性破坏。

•  AI 辅助'Vibecoding'失误致 Jerry's Store 服务器泄露 34.5 万张被盗信用卡
<https://hackread.com/misconfigured-server-hackers-leak-stolen-credit-cards/>

本文揭示了黑客因过度依赖 AI 代码助手 Cursor 进行“氛围编程”，意外构建出无认证目录并导致 14.5 万张有效信用卡数据泄露的重大安全事故。这一案例极具警示意义，它生动地证明了在缺乏人工审查和安全护栏的情况下，AI 辅助开发可能成为攻击者自身防御体系的致命漏洞。

\* 查看或搜索历史推送内容请访问：
<https://sectoday.tencent.com/>
\* 新浪微博账号： 腾讯玄武实验室
<https://weibo.com/xuanwulab>
\* 微信公众号： 腾讯玄武实验室
![微信公众号： 腾讯玄武实验室](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HhcytTU2b7fSw1WPP1oTUaT0CiaZ6f8hCSiaAibKAzCpneuFeETYFUnXIaC1jaNJ6DQZkRPmuVTBy1Kku0AKgN9RY5LSibUfTJ6IOodPSFHbBG4/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

腾讯玄武实验室

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