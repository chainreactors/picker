---
title: 【已复现】Langflow ≤1.8.1 远程代码执行漏洞
url: https://mp.weixin.qq.com/s/NzrZtU3VMV3udIkbLr3_uw
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:03:39.588578
---

# 【已复现】Langflow ≤1.8.1 远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/P5dz00jGoyQ3icX7VMfq6PwXlD4yNIfV129v7ibzibNpLC9aMxza5KBoZw2XTepdh16bVTxxtV6liaciaW3Y7WjibVfvFz7nCwRNFB1SaONYYev4k/0?wx_fmt=jpeg)

# 【已复现】Langflow ≤1.8.1 远程代码执行漏洞

安恒信息CERT

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/JAzzLj4nXevmL5H6C1I6nWLYOHeic25ZZq3Sju5Xs1LnOckux8PBqG1qYrBly0Nicx4verjADnLorl5g1ImeuTeg/640?wx_fmt=jpeg&from=appmsg&wx_&wx_)

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | Langflow ≤1.8.1 远程代码执行漏洞 | | |
| **安恒CERT评级** | 1级 | **CVSS3.1评分** | 10.0 |
| **CVE编号** | CVE-2026-33017 | **CNVD编号** | 未分配 |
| **CNNVD编号** | 未分配 | **安恒CERT编号** | DM-202603-003611 |
| **POC情况** | 未发现 | **EXP情况** | 未发现 |
| **在野利用** | 未发现 | **研究情况** | 已复现 |
| **危害描述** | 该漏洞由于langflow uild\_public\_tmp接口本应为公共流程提供免认证构建服务，却错误地接受了外部传入的data参数，导致攻击者可通过构造恶意节点定义将任意 Python 代码注入 exec()执行，实现未授权远程代码执行。 | | |

该产品主要使用客户行业分布广泛，漏洞危害性高，建议客户尽快做好自查及防护。

**安恒研究院卫兵实验室已复现此漏洞。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P5dz00jGoySCvnlQZPkdr8lZ9dlEviaKCRRoAVmqK0nbu67yRialJXcQic5rhu6bHsJo7eET1aU93xKJZur4rmbFeoBpw73rbnGibticDQqTunic4/640?wx_fmt=png&from=appmsg)

**漏洞信息**

LangFlow是一款开源的低代码工具，通过拖放式可视化界面，可用于构建AI 智能体及其他人工智能应用程序。它允许用户将大语言模型(LLM)、API 接口、矢量数据库及自定义组件编排成智能体式工作流，无需具备高级编程技能。

**漏洞描述**

**漏洞危害等级：超危**

**漏洞类型：**远程代码执行

**影响范围**

**影响版本：**

Langflow ≤1.8.1

**安全版本：**

Langflow >1.9.0

**CVSS向量**

访问途径（AV）：网络

攻击复杂度（AC）：低

所需权限（PR）：无

用户交互（UI）：无

影响范围 （S）：改变

机密性影响 （C）：高

完整性影响 （l）：高

可用性影响 （A）：高

**修复方案**

**官方修复方案：**

官方已发布修复方案，升级至 Langflow 1.9.0 或更高版本。

**参考资料**

https://github.com/advisories/GHSA-rvqx-wpfh-mfx7

https://github.com/langflow-ai/langflow/commit/73b6612e3ef25fdae0a752d75b0fabd47328d4f0

https://github.com/langflow-ai/langflow/security/advisories/GHSA-vwmf-pq79-vjvx

**产品能力覆盖**

|  |  |
| --- | --- |
| **产品名称** | **覆盖补丁包** |
| AiLPHA大数据平台 | GoldenEyeIPv6\_XXXXX\_strategy2.0.XXXXX.260320.1及以上版本 |
| APT攻击预警平台 | GoldenEyeIPv6\_XXXXX\_strategy2.0.XXXXX.260320.1及以上版本 |
| 明鉴漏洞扫描系统 | V1.3.1947.1736及以上版本 |
| WAF | 已支持 |
| 玄武盾 | 已支持 |

**技术支持**

如有漏洞相关需求支持请联系400-6059-110获取相关能力支撑。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Qiao60gtLmwVcoDMnCe4IdPoVDPOdqoc7brmYf1OS0B11CjaFfmbP2PjSbSmyFJYvCqoVr9cNkDibZriaTicYCnRVQ/0?wx_fmt=png)

安恒信息CERT

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Qiao60gtLmwVcoDMnCe4IdPoVDPOdqoc7brmYf1OS0B11CjaFfmbP2PjSbSmyFJYvCqoVr9cNkDibZriaTicYCnRVQ/0?wx_fmt=png)

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