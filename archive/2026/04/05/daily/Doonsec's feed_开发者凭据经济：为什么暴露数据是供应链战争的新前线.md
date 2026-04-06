---
title: 开发者凭据经济：为什么暴露数据是供应链战争的新前线
url: https://mp.weixin.qq.com/s/rPu64YyYJRwyxzq9RTG2Qg
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:40:29.566226
---

# 开发者凭据经济：为什么暴露数据是供应链战争的新前线

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/PO9bjOzlHYB1wcgg08Ghz4JlxyVVlI6AtIr4Luj1rw6eI3Irbds08tdh7UtGMvbD8MJgUb2udwZDRrMNREiacF5iaxXGW9Bme921icvibNZibx7c/0?wx_fmt=jpeg)

# 开发者凭据经济：为什么暴露数据是供应链战争的新前线

bitbot
bitbot

Desync InfoSec

![]()

在小说阅读器中沉浸阅读

近期一系列供应链攻击事件揭示了一个令人不安的新趋势：**开发者凭据经济**正在成为网络犯罪的新兴蓝海市场。攻击者不再仅仅入侵软件供应链，而是系统性地利用供应链攻击来收割安全团队最信任的工具中的"王国钥匙"——API 密钥、Cloud Access Token 和长期有效的凭据。

────────────────

关键要点

攻击者正越来越多地利用供应链攻击来收割高权限的开发者凭据，催生了一个利润丰厚的"开发者凭据经济"——一个专门交易 API 密钥、Secrets 和云访问令牌的地下市场。

依赖执行层检测（如 EDR）来应对供应链威胁远远不够，因为这些工具对凭据实际被盗取的临时性 CI/CD 环境缺乏可见性。

要消除开发者凭据经济带来的系统性基础设施风险，需要采用**持续威胁暴露管理（CTEM）**方法，在攻击者利用之前主动识别并消除暴露条件（如长期有效的访问令牌）。

────────────────

背景：当 AI 源码泄露遇上供应链攻击

2026 年 3 月，两起标志性事件几乎同时发生：

• **Anthropic Claude Code** 源代码泄露，涉及 512,000 行代码
• **Sapphire Sleet（UNC1069）** 对 Axios npm 包的供应链攻击，该包周下载量高达 1 亿次

这两起事件的交汇，模糊了传统恶意软件与系统性基础设施风险之间的界限。Tenable 对暴露情报数据的分析显示，2026 年 3 月观察到的一系列供应链攻击不应被视为孤立事件——它们标志着高效率**"开发者凭据经济"**的全新运营现实。

EDR 奇点的迷思

微软和 Google 均独立将近期的 Axios 攻击事件归因于朝鲜国家级威胁行为者。业界叙事将这次入侵——在一个拥有**每周 1 亿次下载量**的 npm JavaScript 库中植入后门——描绘为 EDR（端点检测与响应）的胜利。逻辑看似简单：EDR 在执行阶段捕获并阻止了 Payload，因此 EDR 就是解决方案。

**⚠ 这是一个危险的误判。**"EDR 奇点"——即 EDR 解决方案变得如此全面、智能和自主，以至于无需任何其他安全工具——是一个主导当前安全格局的强大却危险的神话。

依靠 EDR 来阻止供应链攻击，**就像在厨房里放着打开的汽油罐，却指望烟雾报警器来救你**。分析表明，当 EDR 代理触发对 **WAVESHAPER.V2 RAT** 的告警时，真正的损害——凭据暴露——早已发生。

EDR 为何不够用？

• **EDR 是反应式的：**它监控执行过程，而非允许攻击发生的条件。它看不到被错误配置的 GitHub Action 或权限过大的 npm Token。

• **覆盖盲区：**EDR 对临时性的 CI/CD Runner 和构建环境完全缺乏可见性，而凭据盗窃恰恰发生在没有 EDR Agent 的地方。

• **致命速度差：**在 Axios 攻击活动中，恶意软件被设计为在数秒内外泄 Secret 并自毁——通常比安全分析师响应 EDR 告警的速度更快。

• **EDR 绕过并非理论：**EDR 绕过是一种成熟的工业化能力。威胁行为者通过 BYOVD（自带易受攻击驱动程序）攻击常规性地禁用 EDR Agent——加载合法签名但存在漏洞的内核驱动程序。

────────────────

目标分析：映射凭据生成层

攻击者越来越多地入侵和武器化开发者与安全团队使用的关键瓶颈工具——如 Axios npm 包和 KICS IaC 扫描器。这一向开发生命周期上游移动的趋势，揭示了新兴威胁经济中明确的劳动分工。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PO9bjOzlHYDUwRxia7HL50nK1JdElibbktIFuSicnwjyjTAAsBicxLbRpCcENtbxol2b0s0aQE7P4cwFXAmBaW24ZLrJGZFianHt2HZ11CRd9Gns/640?wx_fmt=png)

|  |  |  |
| --- | --- | --- |
| 威胁行为者 | 运营焦点 | 主要目标 |
| TeamPCP | 生成层：通过工具漏洞批量收割凭据 | Trivy, LiteLLM, KICS |
| Sapphire Sleet | 武器化层：国家级数据外泄与收入生成 | Axios, npm 生态 |
| GlassWorm | 机会主义层：高量自动化盗窃 | VSCode 插件, OpenVSX |

────────────────

暴露情报：转向 CTEM

要摆脱这种被动模式，防御者必须从仅仅对恶意软件做出反应，转向采用**持续威胁暴露管理（CTEM）**作为先发制人的策略。虽然 AI 公司将前沿模型宣传为安全工具，但最近泄露的 512,000 行 Claude 源代码表明，AI 本身就带有巨大的暴露面。

一个成熟的 CTEM 程序，由**暴露情报**驱动，专注于真正降低风险的先发行动：

**阶段一：加固（Kill Switch）**
立即审计 Lockfile 并禁用生命周期钩子（`--ignore-scripts`）。这消除了 Sapphire Sleet 用于部署 WAVESHAPER.V2 的 postinstall 攻击向量。

**阶段二：人/身份防御**
必须淘汰长期有效的 Token。Axios 攻击之所以成功，是因为一个被盗的 Token 绕过了所有安全控制。转向基于 OIDC 的短期自动化不是"锦上添花"，而是暴露管理的基本要求。

**阶段三：反侦察**
映射完整攻击面，包括 EDR 无法覆盖的 CI/CD 流水线和云原生构建阶段。

![](https://mmbiz.qpic.cn/mmbiz_png/PO9bjOzlHYDYGmckXaSTnGTuywdx4CznWbicYq8FwhjGkRRmFEuKoS6j0kRSw0qjiayfz0yRHJOy6spcsX04X4fqUgfkGqM5XYULIEFAtVybU/640?wx_fmt=png)

────────────────

总结

Axios 和 Anthropic 事件是对 C-suite 管理层的一次警醒。理论上的严重性评估和反应式检测（EDR）不足以应对已经将开发者身份盗窃工业化的攻击者。

**暴露管理**应该成为你的第一道也是主要防线。通过识别和修复供应链攻击所依赖的暴露条件，我们可以在 Payload 到达端点之前就阻止它。

────────────────

来源：Tenable Research Special Operations (RSO) 团队
原文：The developer credential economy: Why exposure data is the new front line in the supply chain war
发布日期：2026年4月3日

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

Desync InfoSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

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