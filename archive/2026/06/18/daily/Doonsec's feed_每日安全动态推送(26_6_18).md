---
title: 每日安全动态推送(26/6/18)
url: https://mp.weixin.qq.com/s/Rpbj8e3xIXoODoF9mVGnaA
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:04:27.009475
---

# 每日安全动态推送(26/6/18)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dWDic6IAXZsfiaZW0JQviacCLMqWhF3SNibuLiadsQ0NIQTtMib9dtRNwicMAnvZMsHoH8R05VSkImpkiavrZ7h5ia6ZMew/0?wx_fmt=jpeg)

# 每日安全动态推送(26/6/18)

原创

admin
admin

腾讯玄武实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

•  ITScape KVM 逃逸漏洞：公开 PoC 利用代码威胁云主机安全 | CN-SEC 中文网
<https://cn-sec.com/archives/5278449.html>

本文揭示了针对 KVM/arm64 的严重逃逸漏洞 ITScape（CVE-2026-46316），其核心亮点在于利用 VGIC-ITS 模拟中的竞争条件，使攻击者能绕过用户空间防护直接以内核权限接管宿主机。鉴于公开的概念验证代码（PoC）已使多租户云环境面临迫在眉睫的威胁，该文章为云服务商提供了至关重要的技术分析与即时缓解指南。

•  Windows Defender 关键竞态条件漏洞：导致 SYSTEM 权限提升与 Use-After-Free 崩溃
<https://cxsecurity.com/issue/WLB-2026060013>

本文揭示了 Windows Defender 中一个利用竞争条件导致本地提权至 SYSTEM 并触发用后释放（UAF）崩溃的严重零日漏洞。该研究不仅展示了如何绕过实时防护机制，还证实了攻击者可在系统失去防病毒保护的状态下获取最高权限，对当前企业安全架构构成直接威胁。

•  Zombie COTables：利用 VirtualBox SVGA 中的 Use-After-Free 漏洞实现虚拟机逃逸
<https://blog.exodusintel.com/2026/06/15/zombie-cotables-resurrecting-freed-memory-to-escape-virtualbox/>

本文深入剖析了2025年在VirtualBox SVGA设备中发现的关键Use-After-Free漏洞，详细披露了从SVGA-II架构机制到Linux环境下完整利用链的技术细节。作为即将在2026年修复的严重漏洞，该文章为虚拟化安全研究提供了极具价值的实战参考。

•  CVE-2026-21241：AFD.sys 中 Socket 通知处理 Race Condition 引发的 Use-After-Free LPE 漏洞
<https://hackyboiz.github.io/2026/06/15/Libera/CVE-2026-21241/>

本文深入剖析了 Windows AFD.sys 中因 I/O 迷你完成包在队列化与销毁间存在竞争窗口而导致的严重 Use-After-Free 漏洞（CVE-2026-21241），并详细揭示了微软通过重构内存释放逻辑来彻底根除该竞态条件的修复方案。

•  CVE-2026-40519：Nginx Proxy Manager 命令注入漏洞复现 | CN-SEC 中文网
<https://cn-sec.com/archives/5271770.html>

本文深入剖析了Nginx Proxy Manager中因双重转义顺序错误导致的高危命令注入漏洞（CVE-2026-40519），揭示了攻击者如何利用该缺陷在容器内以root权限执行任意命令。文章不仅提供了从根因分析到完整攻击链复现的详细技术路径，还探讨了绕过API校验与事务回滚的实战技巧，对运维安全与代码审计具有极高的参考价值。

•  图片越糊越危险？西湖大学发现多模态大模型“攻击舒适区” - 安全内参 | 决策者的网络安全知识库
<https://www.secrss.com/articles/91278>

本文揭示了多模态大模型在特定视觉退化区间（ACZ）下，因视觉认知过载导致安全对齐机制失效的反直觉现象，并提出了有效的结构化认知卸载防御策略。该研究不仅填补了视觉文本压缩场景下的安全评估空白，更为即将普及的长上下文视觉应用提供了关键的风险预警与工程解决方案。

•  Apache CXF 系列严重安全漏洞爆发
<https://sectoday.tencent.com/event/_aTEuJ4B0VHppVqoW3aG>

Apache CXF 框架近期曝出包含 JNDI 注入、OAuth2 认证绕过、XXE 注入及逻辑错误在内的多项严重安全漏洞，影响 4.2.2 及 4.1.7 之前的多个版本。攻击者可利用这些缺陷执行远程代码、绕过身份验证、窃取敏感数据或导致服务拒绝。具体风险包括 JMSConfigFactory 与 DispatchMDBMessageListenerImpl 中的 JNDI 注入漏洞、OAuth2 模块中缺失的 JWT 声明验证及反向 IP 绑定逻辑错误、W3CMultiSchemaFactory 中的 XML 外部实体注入、以及 JwsJsonContainerRequestFilter 中的元数据信任绕过。此外，还发现了附件头无限制导致的拒绝服务、日志注入及 HTTP 响应拆分等辅助性漏洞。官方强烈建议所有受影响用户立即升级至 4.2.2 或 4.1.7 修复版本以阻断攻击路径。

•  IronWorm：利用 Linux 凭证与 eBPF 技术自动化供应链攻击
<https://linuxsecurity.com/news/security-vulnerabilities/ironworm-linux-credentials-supply-chain-attack>

本文揭示了 IronWorm 如何利用 eBPF 技术实现深度隐蔽，并将开发者工作站的凭证窃取升级为自动化的软件供应链攻击，彻底改变了我们对 Linux 开发环境安全边界的认知。这一发现警示业界，单一的终端感染已不再是孤立事件，而是能够利用开发者声誉大规模污染开源生态的致命跳板。

\* 查看或搜索历史推送内容请访问：
<https://sectoday.tencent.com/>
\* 新浪微博账号： 腾讯玄武实验室
<https://weibo.com/xuanwulab>
\* 微信公众号： 腾讯玄武实验室
![微信公众号： 腾讯玄武实验室](https://mmbiz.qpic.cn/mmbiz_jpg/HhcytTU2b7ea6bC9zT3rPlGtgiceQ5zL7tiarksKXI6Tv56HIW2n72sH1Tn8sVyHObX7ZRlgaXsFVkr1qjeQahvEJWA9NnZJuNdWcSRxvDlibQ/640?wx_fmt=jpeg&from=appmsg)

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