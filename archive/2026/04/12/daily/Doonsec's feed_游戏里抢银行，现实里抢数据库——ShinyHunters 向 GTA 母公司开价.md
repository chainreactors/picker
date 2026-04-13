---
title: 游戏里抢银行，现实里抢数据库——ShinyHunters 向 GTA 母公司开价
url: https://mp.weixin.qq.com/s/IENnSvKzMvatv4bFxu-Pdg
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:56:49.860445
---

# 游戏里抢银行，现实里抢数据库——ShinyHunters 向 GTA 母公司开价

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAheNbxZThAOOSAniaicpmqSCia3VibkicVMicvFVgza53WBiaaLfGHiax0AhZRViciajJMomL49wqqWovXBd3ro0t0HSaL5UWNDptOgvsBZw/0?wx_fmt=jpeg)

# 游戏里抢银行，现实里抢数据库——ShinyHunters 向 GTA 母公司开价

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAian2PzlmlPZbpAic613S74HuQ59GQ2KmCyHzlM3dXOUiaoLjX7JnjSRH0DHfwdDnW1Ooteqk817nBBgFJEHiabeUY0Grw3SnYtmlg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAhNP8icrria3vwjLAhZIoRMmWp7jLjNhBo4WuFLl6CIhaz8H6b0DeQh0r5WiaTUIQ05csQOVZQeGr0KTicAb5AjYCsoGTpXF4p7C5g/640?wx_fmt=png&from=appmsg)

## 长话短说

2026 年 4 月 11 日，勒索黑客组织 ShinyHunters 在其暗网泄露站点发布公告，声称已通过以色列 AI 分析公司 Anodot 的安全漏洞，获取了游戏巨头 Rockstar Games 的 Snowflake 数据库访问权限，并给出 4 月 14 日的付款截止期限。

这不是孤立事件。BleepingComputer 的交叉核实显示，此次行动波及超过十数家企业，核心攻击路径是从 Anodot 的系统中窃取用于连接客户云环境的身份验证令牌，再以这些令牌作为「合法通行证」进入各受害方的 Snowflake 实例，完成数据外泄而无需攻破 Snowflake 平台本身。

**核心判断**：这次攻击代表 ShinyHunters 对 Snowflake 生态的第二轮系统性打击，其战术相比 2024 年有明显升级——从直接盗取终端用户凭证，转向劫持上游 SaaS 集成商的 API 令牌，用受信任的服务身份完成横向渗透。Rockstar Games 是否真正受损，截至本文成稿仍属**待证实**状态，但 Anodot 事件本身已获 Snowflake 官方承认。

## 一、事件时间线

| 时间（UTC 近似） | 事件节点 |
| --- | --- |
| 2025 年 11 月 | 数据分析公司 Glassbox 完成对 Anodot 的收购 |
| 2026 年 4 月 4 日（周五） | ShinyHunters 实施数据外泄，时逢多国银行假日（复活节/逾越节前夕） |
| 2026 年 4 月 7 日 | 开源社区首次出现涉及 Snowflake 异常活动的报告 |
| 2026 年 4 月 8 日 | 媒体发布调查报告，Snowflake 官方向其确认「少量客户账户出现异常活动」并启动锁定措施；Anodot 状态页面显示所有连接器（Snowflake、S3、Amazon Kinesis）全区中断 |
| 2026 年 4 月 9 日 | Snowflake 正式向 BleepingComputer 确认 Anodot 是涉事第三方集成平台 |
| 2026 年 4 月 11 日（UK 时间） | ShinyHunters 在其暗网泄露站点（`.onion`）发布针对 Rockstar Games 的公告，要求付款，截止日期 4 月 14 日 |
| 2026 年 4 月 12 日 | Rockstar Games 未发表任何公开声明；Anodot/Glassbox 未回应媒体问询 |

值得单独标注：ShinyHunters 在接受 BleepingComputer 核实时，措辞使用了「已在 Anodot 基础设施中驻留一段时间」，这意味着实际入侵时间点可能远早于公开数据外泄日期。

## 二、攻击路径还原

### 2.1 Anodot 是什么

Anodot 是一家以色列 AI 驱动的云分析平台，核心功能是对企业的业务和运营数据进行实时异常检测——自动发现收入下跌、成本突增、系统性能异常等信号。为了实现这一功能，Anodot 需要对接客户的核心数据环境，包括 Snowflake 数仓、S3 对象存储、Amazon Kinesis 数据流等。2025 年 11 月，数据分析公司 Glassbox 完成对 Anodot 的收购。

正是这种深度集成特性，使 Anodot 成为攻击者的理想跳板——劫持一个集成平台，等于同时拿到了所有接入该平台的下游客户的入口。

### 2.2 令牌劫持的攻击链

根据的多源报道，攻击链如下：

```
入侵 Anodot 内部系统
       ↓
提取 Anodot 持有的客户侧身份验证令牌
（这些令牌是 Anodot 与客户云服务之间的「受信任凭证」）
       ↓
使用令牌以合法身份进入各受害方的 Snowflake 实例
（无需攻破 Snowflake 平台本身的任何漏洞）
       ↓
通过标准数据库操作（SQL 查询）完成数据外泄
（访问行为与正常 Anodot 集成操作在日志层面高度相似）
       ↓
对受害方发起勒索
```

这条攻击链的核心技术价值在于：**令牌冒用与正常业务流量混同，使基于行为基线的检测机制面临较高的误判风险**。受害方看到的日志，可能与 Anodot 例行数据同步操作在形态上难以区分。

Snowflake 官方的表态也印证了这一点——其声明强调「异常活动与 Snowflake 平台自身的漏洞或错误配置无关」，隐含的逻辑是：攻击者持有的是合法令牌，平台层面无从直接拦截。

### 2.3 Salesforce 方向的尝试：被 AI 检测拦截

ShinyHunters 同时确认，攻击者曾尝试用相同的令牌访问 Salesforce 客户数据，但在尝试过程中被 AI 检测系统识别并阻断。这一细节耐人寻味：一方面说明攻击者掌握的令牌确实覆盖了多个平台；另一方面，Salesforce 的 AI 异常检测有效拦截了此轮攻击，而 Snowflake 的默认防护则未能做到同等效果。

### 2.4 时机选择：节假日窗口期

攻击主体行动集中在 2026 年 4 月 4 日（周五），该日期恰逢复活节前夕，多个欧洲国家和北美地区进入银行假日。这与 ShinyHunters 在过往行动中展现出的节假日窗口期策略高度吻合——安全运营中心（SOC）值班人员减少，事件响应速度滞后，为攻击者提供了更长的无干扰驻留时间。

## 三、Rockstar Games 的具体处境

Rockstar Games 在本次事件中的特殊性在于：它既是 ShinyHunters 的声称目标，也是历史上的数次攻击受害方。

**L1 已验证**：2022 年，Scattered Spider（Lapsus$ 关联组织）通过社会工程学手段入侵 Rockstar Games 内部 Slack，泄露了大量《GTA 6》早期开发素材，造成重大商业损失。这使 Rockstar 成为黑客社区中高知名度的目标标签。

**L3 待证实**：ShinyHunters 本次在暗网泄露站点发布的声明称「Rockstar Games，你的 Snowflake 实例已通过 Anodot.com 被攻破。付款或泄露。这是 4 月 14 日前联系我们的最后警告……」。截至本文成稿，Rockstar Games 官方未发表任何声明，Hackread.com 的采访请求亦未得到回应。由于勒索方在达成付款之前存在夸大受损范围的明显动机，**该具体声明的真实性无法在当前时点确认**。

**研判**：Rockstar Games 是否真正受损，初步判断需要等待以下任一证据出现：（1）Rockstar 官方就此事发表声明；（2）ShinyHunters 在截止日期后实际公开可验证的数据样本；（3）第三方安全研究人员对样本的独立核实。目前仅凭勒索帖本身，置信度维持在低水平。

## 四、ShinyHunters：一个拒绝瓦解的组织

理解这次事件，需要理解 ShinyHunters 这个组织的结构性特征。

### 4.1 从 2024 年到 2026 年：Snowflake 轨道上的两次打击

**2024 年中期**，ShinyHunters 对 Snowflake 客户发动了历史上规模最大的云数据盗取行动之一。根据 Mandiant 的调查，至少 160 家组织的 Snowflake 实例遭到入侵，攻击向量是通过 infostealer 恶意软件窃取的终端用户凭证（且目标账户普遍未启用 MFA）。受害方涵盖 AT&T、Ticketmaster/Live Nation、Santander、Neiman Marcus、Advance Auto Parts 等企业，涉及数亿条用户记录。AT&T 据报为此支付了约 37 万美元赎金。

事后，执法机构取得突破：Connor Riley Moucka（网络 ID：Waifu/Judische）于 2024 年 10 月 30 日在加拿大被捕；John Erin Binns（ID：IRDev）于 2024 年 5 月在土耳其被捕。2025 年 6 月，法国当局进一步逮捕了另外四名涉嫌成员（绰号 ShinyHunters、Hollow、Noct、Depressed）。

然而，逮捕并未终止组织运作。**2026 年初，该组织的行动节奏反而有所加快**。

**2026 年 3 月**，ShinyHunters 声称掌握来自 400 余家企业的 Salesforce 关联数据，并已实际公开其中 26 家的数据（Google 威胁情报团队将此活动追踪为 UNC6040）。

**2026 年 4 月**，通过 Anodot 的供应链入口，再次对 Snowflake 生态发起新一轮打击。

### 4.2 战术升级：从凭证盗用到令牌劫持

| 维度 | 2024 年模式 | 2026 年模式 |
| --- | --- | --- |
| **初始入口** | infostealer 恶意软件窃取终端用户账号密码 | 入侵 SaaS 集成平台（Anodot）窃取 API 令牌 |
| **认证绕过** | 利用无 MFA 保护的账户直接登录 | 令牌冒用，绕过密码认证环节 |
| **横向覆盖** | 逐一攻破各受害方账户 | 一点突破，通过集成平台辐射所有接入客户 |
| **伪装能力** | 登录行为可被 IP/设备异常检测识别 | 与正常集成服务流量混同，检测难度更高 |
| **Salesforce** | 未明确涉及 | 尝试横向扩展，被 AI 检测拦截 |

这一战术转变的本质是**把攻击目标从企业个体转向企业共同依赖的基础设施节点**。SaaS 集成商掌握着大量客户的「委托凭证」，而这些凭证的安全性往往不在最终用户的安全审计视野内。

### 4.3 组织韧性：品牌大于个体

ShinyHunters 更像一个「特许经营品牌」而非传统的层级制犯罪组织。个体成员被逮捕，不影响品牌延续，也不影响其他成员继续以该名义运作。历史上，多次声称为 ShinyHunters 的行动，执法机构事后无法确认是否为同一核心成员。这种结构性特征使法律手段的威慑效果大打折扣。

## 五、供应链攻击面的系统性分析

Anodot 事件的深层意义，超出了单一公司的安全失误范畴，它是过去两年 SaaS 集成攻击面系统性扩大的缩影。

### 5.1 「受信任集成者」问题

Snowflake 的商业价值建立在生态兼容性上——它天然设计为可与大量第三方分析、监控、ETL 工具无缝对接。这些第三方工具为了正常运行，需要持有客户云环境的访问凭证，通常以 API 令牌或 OAuth 授权的形式储存在集成平台自己的基础设施中。

问题的结构性困境在于：

* **客户将安全信任委托给了集成商**，但集成商的安全水平往往不在客户的安全评估流程之内；
* **集成商持有的令牌通常具有较高权限**（需要足够权限才能读取业务数据并进行分析）；
* **令牌泄露后的检测窗口极短**——使用令牌的异常访问与正常集成调用在日志层面高度相似。

Anodot 在 2025 年 11 月被 Glassbox 收购，这一企业并购事件本身也值得关注：并购整合期间，安全策略的衔接是否出现空窗，目前无法判断，但并购后数月内发生安全事件的时间关联值得记录在案（**研判**：置信度低，仅作观察存档，无直接证据支持因果关系）。

### 5.2 Payoneer 的正面案例

在已披露的受害方中，Payoneer 是唯一正式回应媒体查询的企业：「我们知悉涉及第三方服务提供商 Anodot 的安全事件。根据我们的审查，Payoneer 未受影响。」这一表态的意义在于两点：（1）证明部分企业确实通过隔离措施或限制权限范围规避了损失；（2）为其他未回应的企业提供了对照参照——沉默不等于安全，也不等于受损。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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