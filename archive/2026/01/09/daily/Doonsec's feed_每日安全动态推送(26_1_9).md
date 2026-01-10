---
title: 每日安全动态推送(26/1/9)
url: https://mp.weixin.qq.com/s/rqaI77U4qAM6y8QGa2k3hg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:28:27.333171
---

# 每日安全动态推送(26/1/9)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dWDic6IAXZsfiaZW0JQviacCLMqWhF3SNibuLiadsQ0NIQTtMib9dtRNwicMAnvZMsHoH8R05VSkImpkiavrZ7h5ia6ZMew/0?wx_fmt=jpeg)

# 每日安全动态推送(26/1/9)

原创

admin

腾讯玄武实验室

![]()

在小说阅读器中沉浸阅读

•  利用内核补丁保护机制在Windows中隐藏进程以逃避任务管理器检测
<https://cybersecuritynews.com/hackers-can-leverage-kernel-patch-protection/>

本文揭示了一种利用Windows内核数据结构隐藏恶意进程的新技术，即使在PatchGuard等现代安全机制的保护下仍能有效运行。其核心亮点在于通过精确时序和对进程终止流程的深度理解，实现了从运行到终止全程的隐蔽性，这对系统安全防护提出了新的挑战。

•  n8n 未认证远程代码执行漏洞（CVE-2026-21858）
<https://sectoday.tencent.com/event/JeKLnZsBQreNZx83uo-I>

流行的工作流自动化平台 n8n 被发现存在一个高危的未认证远程代码执行漏洞（CVE-2026-21858），攻击者可利用 Form Webhook 节点中的 Content-Type 解析问题，在无需认证的情况下实现对服务器的完全控制，包括任意文件读取、凭证窃取和系统命令执行。目前全球已有约 100,000 台服务器受到影响，其中 26,512 个实例已暴露在互联网上。n8n 已发布修复版本 1.121.0，强烈建议用户立即升级以防止基础设施被入侵。

•  PR-Attack：基于双层优化的协同Prompt-RAG攻击方法研究
<https://dl.acm.org/doi/10.1145/3726302.3730058>

该文章提出了PR-Attack，一种针对检索增强生成（RAG）框架下大型语言模型（LLM）的新型优化驱动攻击方法。其最大亮点在于通过双层优化框架生成毒化文本和触发器，即使在少量毒化文本注入的情况下也能实现高攻击成功率和隐蔽性。

•  关键 jsPDF 漏洞通过生成 PDF 泄露敏感数据
<https://www.bleepingcomputer.com/news/security/critical-jspdf-flaw-lets-hackers-steal-secrets-via-generated-pdfs/>

本文详细揭示了广泛使用的jsPDF库中存在的严重本地文件包含漏洞（CVE-2025-68428），该漏洞可能被攻击者利用窃取本地文件数据，是当前前端安全领域亟需关注的重要议题。

•  利用 CVE-2025-38352：Linux 内核 POSIX CPU 定时器中的 Use-After-Free 漏洞
<https://cyberpress.org/poc-exploit-released-for-android-and-linux-kernel-vulnerability-cve-2025-38352/>

本文详细披露了Linux内核中一个高危的UAF漏洞（CVE-2025-38352）及其完整利用链Chronomaly，成功实现Android设备上的提权攻击，为内核安全研究提供了重要参考。

•  Chrome WebView 严重漏洞（CVE-2026-0628）允许绕过安全限制
<https://cybersecuritynews.com/chrome-webview-vulnerability/>

本文重点揭示了Google Chrome浏览器WebView标签组件中的高危漏洞CVE-2026-0628，该漏洞可能导致攻击者绕过安全限制，具有严重的安全威胁。文章详细介绍了漏洞的影响、修复措施及更新建议，对广大用户和安全研究人员具有重要参考价值。

•  CVE-2025-66848：京东云路由器曝严重漏洞 黑客可直接获取 root 权限-安全KER - 安全资讯平台
<https://www.anquanke.com/post/id/314126>

本文详细披露了京东云多款 NAS 路由器中一个高危漏洞（CVE-2025-66848），攻击者可借此绕过身份验证并获取系统 root 权限，CVSS 评分为 9.8，凸显其极高的安全风险。该漏洞的利用链清晰展示了从信息泄露到系统完全沦陷的全过程，对网络安全实践具有重要警示意义。

•  CVE-2025-14174分析：ANGLE Metal暂存缓冲区越界写入漏洞
<https://github.com/zeroxjf/CVE-2025-14174-analysis>

本文深入分析并提供了针对CVE-2025-14174的漏洞利用与概念验证代码，揭示了ANGLE在使用Metal后端上传深度纹理时的越界写入问题。该漏洞被用于针对iOS用户的定向攻击，技术细节详实，具有极高的参考价值。

\* 查看或搜索历史推送内容请访问：
<https://sectoday.tencent.com/>
\* 新浪微博账号： 腾讯玄武实验室
<https://weibo.com/xuanwulab>
\* 微信公众号： 腾讯玄武实验室
![微信公众号： 腾讯玄武实验室](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dWDic6IAXZsdry4Sjk6aDIVyY6an3SWfiaxjjYAFgRDjkU7TwPk5ia7VybJzeGOT0IHibic8s3upgwYXjiax8fIiag4hg/640?wx_fmt=jpeg&from=appmsg)

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