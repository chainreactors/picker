---
title: 已复现！Windows 音频服务本地提权漏洞利用链
url: https://mp.weixin.qq.com/s/huytmSXl4j4nb18NEtlfUA
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:13:46.763299
---

# 已复现！Windows 音频服务本地提权漏洞利用链

# 已复现！Windows 音频服务本地提权漏洞利用链

微步情报局
微步情报局

微步在线研究响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

漏洞概况

近日，微步情报局监测到研究人员公开披露了一条涉及 Windows 音频服务的本地提权利用链，关联 CVE-2026-116714 和 CVE-2026-97799，微软已分别在 11 月 10 日和 10 月 13 日的安全更新中修复。微步情报局已成功复现完整利用链。经分析，攻击者可利用两处缺陷登记未签名媒体编解码器并触发音频引擎加载，再通过后续利用步骤实现从普通用户提权至`SYSTEM`，建议受影响用户尽快修复。

两处漏洞分别涉及利用链中的不同环节：

1. CVE-2026-116714 涉及 AppX 部署服务对未签名媒体编解码器包的校验缺陷，为利用链提供恶意编解码器登记入口。微软于 11 月 10 日发布修复，官方列出的受影响系统包括 Windows 10 21H2、Windows 10 22H2（ESU）、Windows 11 23H2 及 Windows Server 2022。

2. CVE-2026-97799 涉及音频服务加载编解码器动态库时签名校验不当，可使已登记的恶意编解码器以 LOCAL SERVICE 身份执行代码，为后续提权提供条件。微软于 10 月 13 日发布修复，官方列出的受影响系统包括 Windows 11 24H2、25H2、26H2 及 26H1。

（完整漏洞情报请查阅https://x.threatbook.com/v5/vul/XVE-2026-94643 与 https://x.threatbook.com/v5/vul/XVE-2026-78811）

漏洞处置优先级(VPT)

**综合处置优先级：**中风险

|  |  |  |
| --- | --- | --- |
| 基本信息 | 微步编号 | XVE-2026-94643、XVE-2026-78811 |
| CVE编号 | CVE-2026-116714、CVE-2026-97799 |
| 漏洞类型 | 本地权限提升 |
| 利用条件评估 | 利用漏洞的网络条件 | 本地 |
| 是否需要绕过安全机制 | 否 |
| 对被攻击系统的要求 | 完整利用链需当前用户已安装或启动过依赖系统框架的应用（如 Microsoft Store 应用、winget 等），且本机存在播放设备 |
| 利用漏洞的权限要求 | 需要普通用户权限 |
| 是否需要受害者配合 | 否 |
| 利用情报 | 是否有POC | 是 |
| 已知利用行为 | 暂无 |

漏洞影响范围

CVE-2026-116714：

* Windows 10 21H2：version<10.0.19044.7846
* Windows 10 22H2：version<10.0.19045.7846
* Windows 11 23H2：version<10.0.22631.7711
* Windows Server 2022（含Server Core）：version<10.0.20348.5870

CVE-2026-97799：

* Windows 11 24H2：version<10.0.26100.9711
* Windows 11 25H2：version<10.0.26200.9711
* Windows 11 26H2：version<10.0.26300.9711
* Windows 11 26H1：version<10.0.28000.3231

漏洞复现

在Windows 11 26H2（10.0.26300.9457）环境中，以本机标准用户运行 PoC（完整利用链），实现从普通用户提权至SYSTEM。

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdENs9Wh2CNAg3Ilfsng55IHYnjiaDApgp8k7lVsPvLSO6DXROmtf2Uuo6ibI0wUJ0R8z6ZGY0Y3jg2FWmP3XlLr27aYBU8CtxGHQU/640?wx_fmt=png&from=appmsg)

修复方案

### 官方修复方案

官方已发布修复方案，请访问链接下载：
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-116714
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-97799

微步产品支撑

微步漏洞情报于2026年10月13日（CVE-2026-97799）、2026年11月11日（CVE-2026-116714）收录上述漏洞。

微步下一代威胁情报平台NGTIP及X情报中心已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。

当前OneSEC已支持相关提权漏洞检测, 可关注告警规则ID：1714

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEPSWtd0ia3q1jPegXxVtSQuM4jArgeypUUt2QEWicj2BrzTqceIwO8KicEqQQqMtKicD08h8NtI27FDE9GDbHDqtXTzoapJAhZtMp8/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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