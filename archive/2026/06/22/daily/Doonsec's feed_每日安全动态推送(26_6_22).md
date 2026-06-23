---
title: 每日安全动态推送(26/6/22)
url: https://mp.weixin.qq.com/s/bUNm24ozzLshczhYKBHYvQ
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:05:40.533826
---

# 每日安全动态推送(26/6/22)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dWDic6IAXZsfiaZW0JQviacCLMqWhF3SNibuLiadsQ0NIQTtMib9dtRNwicMAnvZMsHoH8R05VSkImpkiavrZ7h5ia6ZMew/0?wx_fmt=jpeg)

# 每日安全动态推送(26/6/22)

原创

admin
admin

腾讯玄武实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

•  usbliter8：利用DWC2下溢漏洞破坏苹果A12-A13芯片BootROM信任链
<https://cybersecuritynews.com/iphone-bootrom-vulnerability/>

本文揭示了影响苹果A12/A13芯片的usbliter8 BootROM漏洞，其核心亮点在于利用Synopsys USB控制器的硬件指针算术缺陷，实现了无法通过软件修复的不可变引导链完全攻破。该研究不仅详细解析了绕过A13指针认证（PAC）的复杂利用链，更证明了苹果安全启动机制在特定硬件代际上的根本性失效。

•  CVE-2026-43495：MediaTek t7xx WWAN 驱动因缺少长度校验导致的 Slab 越界读取漏洞
<https://seclists.org/oss-sec/2026/q2/962>

本文深入剖析了 MediaTek t7xx WWAN 驱动中一个 CVSS 评分高达 8.8 的严重漏洞，揭示了攻击者如何通过伪造基带消息绕过完整性校验，利用未经验证的端口计数引发 slab 越界读取。该研究不仅展示了在 Intel 5G 模组中实现跨边界攻击链的具体技术路径，还详细阐述了利用任意内存内容操控驱动控制流的核心机制，对移动设备内核安全具有极高的警示价值。

•  SoK：Android 设计层漏洞在 OpenHarmony 中重演：一项系统性研究
[https://yancomm.net/papers/2026%20-%20USENIX%20Security%20-%20SoK:%20History%20Doesn't%20Repeat%20Itself,%20but%20Android%20Design-Level%20Vulnerabilities%20Rhyme%20in%20OpenHarmony.pdf](https://yancomm.net/papers/2026%20-%20USENIX%20Security%20-%20SoK%3A%20History%20Doesn%27t%20Repeat%20Itself%2C%20but%20Android%20Design-Level%20Vulnerabilities%20Rhyme%20in%20OpenHarmony.pdf)

本文首次系统性地梳理了 Android 历史上的 56 种设计级漏洞，并开创性地将其应用于对拥有十亿用户规模的 OpenHarmony 进行安全审计。研究惊人地发现，尽管 OpenHarmony 已移除 Android 代码，但其核心设计仍继承了 24 种已被 Android 修复的严重漏洞，揭示了新兴操作系统在“设计同源性”下潜藏的巨大安全风险。

•  量子网络安全：MCP 部署亟需升级以应对 Shadow AI 威胁
<https://securityboulevard.com/2026/06/quantum-cyber-security-why-your-mcp-deployment-needs-an-upgrade-now/>

本文深刻揭示了模型上下文协议（MCP）在构建多跳代理工作流时引发的“影子AI”盲区，并警示传统加密在“现在窃取、日后解密”量子威胁下的脆弱性。文章极具前瞻性地提出了融合零信任架构与后量子密码学（PQC）的防御策略，为即将全面普及的AI代理生态提供了至关重要的安全升级蓝图。

•  Steam Workshop 会话劫持：Wallpaper Engine 恶意壁纸利用技术分析
<https://cybersecuritynews.com/steam-workshop-abused/>

本文揭示了攻击者如何利用Steam Workshop的零信任机制，通过伪装成热门壁纸应用“Wallpaper Engine”的恶意可执行文件，大规模窃取Steam会话并植入后门。该研究不仅详细剖析了针对中国用户（占受害者89%）的精准攻击链，更警示了用户生成内容平台在缺乏代码审查下的巨大安全盲区。

•  Mythos：当攻防进入火器时代，防御策略和人的技能栈，都要重写 - atum@Tencent
<https://atum.li/cn/blog/mythos-era-attack-defense-evolution/>

本文深刻揭示了 AI Agent 将网络攻防推向“火器时代”的范式转移，提出防御重心必须从单纯追求响应速度（MTTR）转向控制攻击可达性（P\_reach）与爆炸半径（B）的结构性治理。文章不仅构建了全新的“防御者方程”，更给出了从资产图谱、自动化红队验证到工程化安全运营的可落地实施路径，是指导企业应对 AI 时代安全挑战的必读指南。

•  OpenBSD 零长度 bcmp 导致的 PAP 认证绕过与内核堆越界读取漏洞
<https://seclists.org/oss-sec/2026/q2/947>

本文揭示了一个在 OpenBSD 中潜伏长达 27 年的严重 PAP 认证绕过漏洞，攻击者仅需发送零长度凭据即可在无需任何密码的情况下建立完整的网络链路。该文章不仅详细剖析了从 1999 年代码引入至今的边界检查逻辑缺陷，还展示了其如何导致认证失效及内核堆越界读取，为理解长期遗留代码中的隐蔽风险提供了极具价值的技术案例。

\* 查看或搜索历史推送内容请访问：
<https://sectoday.tencent.com/>
\* 新浪微博账号： 腾讯玄武实验室
<https://weibo.com/xuanwulab>
\* 微信公众号： 腾讯玄武实验室
![微信公众号： 腾讯玄武实验室](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HhcytTU2b7ckJdlaFpTibOaAOgaYO2I7DhBzt1EuBlEKFica0ySWzwrX38pnW6PAVRCzUF0ZC2ohL55h3sauU13oD1Z8EpHAeN04WWpfU4jAE/640?wx_fmt=jpeg&from=appmsg)

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