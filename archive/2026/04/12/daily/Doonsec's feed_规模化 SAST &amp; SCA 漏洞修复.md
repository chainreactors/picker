---
title: 规模化 SAST &amp; SCA 漏洞修复
url: https://mp.weixin.qq.com/s/7vwpX9F3fNcS8ux-JJ_cUA
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:53:24.912893
---

# 规模化 SAST &amp; SCA 漏洞修复

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iatDdM4vSwrtTDNxusGN6XEQQicW7ucnyuiaYMrvwYJaJzZFv8x9C1IotV8SdfVW5KV0xLH5ic34RGEq3nbpcOzjia4eCbAuGEE9m8F4WTia7s5a8/0?wx_fmt=jpeg)

# 规模化 SAST & SCA 漏洞修复

原创

tonghuaroot
tonghuaroot

RedTeam

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

原文：*Remediation at Scale: What High-Performing AppSec Teams Do Differently*，Semgrep，2026 年。数据来自 2025 年全年，覆盖 50k+ 活跃 SAST 仓库、25k+ 活跃 SCA 仓库，400+ 组织。

## 问题不在发现，在于修复

这份报告的起点很直接：现代工程团队已经普遍部署了扫描工具，发现漏洞不是难事。难的是修。修一个漏洞意味着开发者要停下手头的活，看懂问题，写代码，过 Review，可能花几小时也可能花几天，而这些时间直接从功能开发里扣。

Semgrep 把数据里的组织分成两组：修复率前 15% 叫 Leaders，其余 85% 叫 Field。

![image](https://mmbiz.qpic.cn/mmbiz_png/iatDdM4vSwrueIXprogfHvFM8HdjeX6H2TS8kIpgY0IPtuINsbDumRLpdSicFvG1mHPcsG1QFLR7XVGYjsb7Yy1QkVEFc9GgibUKm3kHcjRI0Q/640?wx_fmt=png&from=appmsg)

image

## 差距有多大

| 指标 | Leaders | Field | 差距 |
| --- | --- | --- | --- |
| SAST 漏洞修复率 | 74.4% | 22.3% | 3.3 倍 |
| SCA 漏洞修复率 | 39.6% | 16.8% | 2.4 倍 |
| SAST 平均修复时间 | 32.9 天 | 41.7 天 | 快 1.3 倍 |
| SCA 平均修复时间 | 28.8 天 | 65.8 天 | 快 2.4 倍 |

有一点反直觉：Leaders 修单个漏洞的速度其实跟 Field 差不多，差距在于他们修掉了更大比例的总量。不是更快，是更多。

![image](https://mmbiz.qpic.cn/mmbiz_png/iatDdM4vSwrt2EY30M1zPicJBy54nUDib8K5ricmHicicR5BozDyIWW8KTRCAwLTyZuZTn0VFIGOqo28Vsibicicf9F2dLQhuiaHsWtF7cLFu2KBVKF9s/640?wx_fmt=png&from=appmsg)

image

各严重等级上，差距同样一致，Leaders 不是只修 Critical，是每个等级都修得更多：

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/iatDdM4vSwrsZobBTZooibLQnzuFw2hZRfvqib706PovsH2rbyWiaMha9a4aklXYMdlFFAVRn4EYVmOpjO9HTfYCAjHKlMWicSwkDhEu5OxqSptY/640?wx_fmt=png&from=appmsg)

image

## SAST 和 SCA 是两个不同的事

|  | SAST（自研代码漏洞） | SCA（第三方依赖漏洞） |
| --- | --- | --- |
| 来源 | 开发者自己写的代码 | 引入的第三方包/库 |
| 修复方式 | 改代码 | 升级依赖版本 |
| 主要障碍 | 理解漏洞、修代码 | 有没有补丁、升级会不会 break |
| PR 扫描效果 | 显著（代码刚写下） | 有限（漏洞往往在加包之后才被披露） |

区别在于控制权：SAST 漏洞是你自己引入的，SCA 漏洞是上游某天突然披露的。

## 什么时候检测，决定了修不修

这是报告里最值得停下来看的一组数据：

| 检测时机 | Leaders MTTR | Field MTTR |
| --- | --- | --- |
| PR 扫描（SAST） | 4.8 天 | 18.2 天 |
| 全量扫描（SAST） | 43.0 天 | 54.3 天 |
| PR 扫描（SCA） | 1.2 天 | 4.8 天 |
| 全量扫描（SCA） | 76.1 天 | 36.4 天 |

同一类漏洞，PR 里检测到的比全量扫描检测到的快 9 倍修完。原因很现实：开发者正在看那段代码，上下文在脑子里，顺手两行就解决了，不需要开 Ticket、不需要重新捡起旧包袱。Leaders 里有 63% 的 PR 发现当天就修完了。

全量扫描的结果要进 Backlog、等分配、重建上下文、和业务需求抢优先级，平均拖 43 天。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/iatDdM4vSwrstxicaE5MSh0YHcUpEYUIL0ica2WMtmUMibsicla5qQLc9Zml8icRYkKLjwsmBZBbRGOGl6YFab76qTmlJr0E2ibbyOYLr7syQ30iaYI/640?wx_fmt=png&from=appmsg)

image

## 同样的工具，不同的收益

Leaders 和 Field 用的功能基本一样，但 Leaders 从每个功能里拿到的提升明显更大。

### Blocking Rules

PR 里检测到高风险漏洞就阻止合并。Leaders 采用率比 Field 高 14 个百分点（45% vs 32%）。

| 指标 | Leaders | Field |
| --- | --- | --- |
| 有 Blocking Rule 的组织 | 45% | 32% |
| 开启后修复率提升 | +12.3pp | +4.9pp |

为什么同一个功能 Leaders 拿到 2.5 倍的收益？因为他们只对高置信度漏洞启用阻断（硬编码密钥、SQL 注入这类），而且阻断发生时开发者知道怎么处理。工具没差，配套流程有差。

### 跨文件分析（Cross-File Analysis）

追踪数据从一个文件流到另一个文件再到危险调用的完整路径，确认漏洞是不是真的能被触达。

| 发现类型 | Leaders 修复率 | Field 修复率 |
| --- | --- | --- |
| 跨文件确认的漏洞 | 69.4% | 40.1% |
| 单文件漏洞 | 42.8% | 18.1% |

开发者更愿意修"确认是真的"的漏洞，跨文件分析提供的就是这种确定性。

### 可达性分析（Reachability，SCA）

检查依赖包里的漏洞代码路径有没有被你的应用真正调用。

| 可达性状态 | Leaders 修复率 | Field 修复率 |
| --- | --- | --- |
| 可达 | 92.3% | 30.5% |
| 不可达/未知 | 66.9% | 20.5% |

可达的漏洞，Leaders 修复率 92%，这个数字挺惊人的。这个信号能有效解决依赖告警太多看不过来的问题，可达的先修，不可达的批量处理。

### AI Memories

团队可以把安全判断记录下来，比如"所有路由都过了 AuthMiddleware，这类告警是误报"，让扫描引擎以后自动识别同类模式，不再重复弹。Leaders 平均创建 32 条这样的记忆，Field 平均 25 条。最常记录的是框架保护和非生产环境两类。道理是：这个判断人做一次，系统记住，不用每次都重来。

### 自定义规则

通用规则集不认识你自己的代码库，不知道你的 `sanitize_html()` 已经处理了 XSS、你的 `@auth_required` 装饰器会做鉴权检查。Leaders 采用率比 Field 高 9pp（59% vs 50%），平均写 8.3 条，Field 写 6.4 条。

同一个功能在不同成熟度的团队里效果差距有多大：

![image](https://mmbiz.qpic.cn/mmbiz_png/iatDdM4vSwrtSKH1N5O1v8QxXhns8Dy9SIDURRzW5vGf3ujvRqbgOicTiczEnJJDCVEneXozVx2iaBYB6h2owbOdHp2AUyUHwdmTE7icqumiaT0Ss/640?wx_fmt=png&from=appmsg)

image

## OWASP Top 10 各类别修复率

| OWASP 类别 | Leaders | Field | 差距 |
| --- | --- | --- | --- |
| A07 身份验证失败 | 59.0% | ~11% | +48pp |
| A02 加密失败 | 47.7% | ~9% | +38pp |
| A03 注入 | 37.3% | 14.5% | +23pp |
| A01 访问控制失效 | 43.6% | 24.2% | +19pp |
| A10 SSRF | 38.1% | 40.4% | Field 反而更高 |

身份验证和加密的差距最大，修这两类问题不是改一行代码的事，往往要动架构（Session 管理、加密算法迁移、跨服务协调），所以多数团队的应对是推进 Backlog。Leaders 会真的去做，Field 更多是拖着。

SSRF 的反例值得注意：Field 修复率反而比 Leaders 高，是因为 SSRF 的"修法"不确定，简单的 URL 白名单可以被 DNS Rebinding 绕过，很多"修了"只是制造了错误的安全感，所以高修复率不代表真的修好了。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/iatDdM4vSwrtP3xm3yxoJPo6wJLUog90DgFYm9AGmPKg85PyuAP0L2mxtBz2bg5OnnWFibjLz9jT10bJibPF7yNI0yjPL7Rvks5EudibsbAA77o/640?wx_fmt=jpeg&from=appmsg)

image

## 90 天是个拐点

漏洞放超过 90 天，被修的概率急剧下降。

| 指标 | Leaders | Field |
| --- | --- | --- |
| SAST 修复来自 90+ 天 backlog 的比例 | 9.4% | 16% |
| SCA 修复来自 90+ 天 backlog 的比例 | 12.1% | 19.9% |

最容易积压的漏洞（Field 数据）

SAST 里，注入类有 31.9% 的漏洞积压超 90 天，平均躺了 218 天；加密失败 23.3%，平均 240 天；身份验证失败平均积压 262 天，是最长的。

SCA 里，ReDoS（正则 DoS）13% 超 90 天，平均 238 天；资源耗尽 11.5%，平均 215 天。

报告说得很直接：积压漏洞到期必须做决定，要么修，要么正式书面接受风险，要么确认是误报就关掉。什么都不做不是在管理风险，只是在表演管理风险。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/iatDdM4vSwrvnnm9ibRCsRu60xbrv1KMwl1ZCrAUPuW7lTsPbzh9w98zq6DWkIuQQNfC8hica2qqRibjYqDicWCTmD2pJziblRHd0VSEMSp7VyBEU/640?wx_fmt=png&from=appmsg)

image

## SCA 各生态修复情况

| 生态系统 | 修复率 | MTTR |
| --- | --- | --- |
| Composer (PHP) | 47.3% | 101 天 |
| PyPI (Python) | 38.7% | 31 天 |
| Cargo (Rust) | 33.6% | 63 天 |
| GoMod (Go) | 31.4% | 62 天 |
| Maven (Java) | 27.0% | 30 天 |
| NPM (JavaScript) | 26.5% | 42 天 |
| NuGet (C#) | 22.8% | 33 天 |

Composer 排第一，部分原因是 drupal/core 这类高频包升级路径清晰。NPM 在各严重级别上修复率都差不多是 26%，说明问题不在优先级，是生态整体的难度。

最难搞定的几个包：node-forge、Auth0 旧版 SDK、urllib3、commons-compress。这些包深埋在基础设施里，升级往往连着改一串东西。报告建议：如果一个依赖躺了半年以上，不如直接问自己：我们真的打算修吗？如果不打算，就正式接受这个风险，别装作在排队等修。

![image](https://mmbiz.qpic.cn/mmbiz_png/iatDdM4vSwrvruSK0EXzrGSHPf6kpWlc9NibIdbF16PmCiapPxrpnyMRD4ic4B17Ytu48Fvs4SnoOFEuzT0DhSYCWv13X40FCTEnB9DPpWMdCcY/640?wx_fmt=png&from=appmsg)

image

## 几条可以实际用的建议

**这周能做的：**

先找出 5 条最高风险的 SAST 规则启用阻断。从硬编码密钥和 SQL 注入字符串拼接开始，确保修复路径明确，不要在修法不清楚的规则上阻断，那只会让开发者烦。

SCA Backlog 按可达性排序，可达的先处理，不可达的单独批量审。用可达性数据做过滤，而不是把所有告警当同等优先级，是目前最直接的降噪方法。

优先处理跨文件确认的漏洞。置信度高，修复率也高，拿来建立早期成果和开发者信任都合适。

**这个季度可以推进的：**

建立 90 天 Escalation 机制：每条到期漏洞必须走三条路之一：修、书面接受风险、确认误报关掉。不允许第四条路（继续躺着）。

审计最近 50 条误报决策，找出高频模式，把它们编码成 AI Memories 或自定义规则，不要重复做同样的判断。

检查告警到达开发者的传导链：告警有没有真的到开发者那里？描述里有没有足够上下文（是哪个文件的哪个输入流到了哪个危险函数）？每条漏洞有没有明确的 Owner？这三个问题如果有一个答案是"不确定"，修复率上不去的原因就在这里。

**半年内的战略级决策：**

身份验证和加密这两类问题，要么划专项时间修（这是项目，不是 Ticket），要么书面接受风险，不能继续在 Backlog 里挂着不管不问。字段平均积压 262 天，说明这种漠视已经是常态了。

不同包管理生态适用不同的 SLA，用自己的数据校准，而不是拍脑袋定个"所有高危 30 天内修复"。

为团队内部框架和 API 写自定义规则，通用规则集不知道你的 `sanitize_html()` 安不安全、你的 `@auth_required` 管不管用，不写自定义规则就是在接受误报率。

## 最后一个值得记住的数字

如果 Critical SAST 修复率低于 50%，问题几乎不在扫描质量，而是告警到修复之间的流程断了。从这里查起。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

RedTeam

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6USuqjXjYk7KoXCtYjrNnB2XprMPwXgFMP2CGxa880Qdfw9zo3A3rl7TTUJF0iaI90KwgZMTem4JVjDSS3XrClw/0?wx_fmt=png)

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