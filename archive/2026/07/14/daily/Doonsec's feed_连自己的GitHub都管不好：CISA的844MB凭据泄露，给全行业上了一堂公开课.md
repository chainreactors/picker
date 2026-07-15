---
title: 连自己的GitHub都管不好：CISA的844MB凭据泄露，给全行业上了一堂公开课
url: https://mp.weixin.qq.com/s/nqg1NXriBJakmyMu6nfuZA
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:47:11.314158
---

# 连自己的GitHub都管不好：CISA的844MB凭据泄露，给全行业上了一堂公开课

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/odcL3w4qOq9Ryrd61liaXV06p31BLptTyQ4DLWVozKHCqhLWuuC8z2Rc8iaM7ZSx4YhQmjJURPlAJZ4xOLKNs0ET4iaGS0PibN8zD2iadmyIMOwU/0?wx_fmt=jpeg)

# 连自己的GitHub都管不好：CISA的844MB凭据泄露，给全行业上了一堂公开课

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一个负责保护全美关键基础设施的顶级网络安全机构，自己的承包商把844MB的内部凭据扔到了公共GitHub仓库上，公开放了将近六个月，期间自动告警发了9次无人处理，最后还是靠外部记者才捅到CISA面前。

这不是段子。这是2026年5月CISA事后报告还原出的真实事件。

作为长期关注凭据泄露和供应链安全的研究者，看完这份报告后的第一反应是：这事本身的技术门槛极低，低到任何一个初级开发者都可能犯。但它的后续反应链暴露出的问题，才是所有安全团队需要警惕的。

---

仓库是怎么暴露的

事故源头很朴素：CISA的一个承包商在操作过程中，把内部数据发布到了GitHub上一个名为 **"Private CISA"** 的公共仓库。名字里虽然带个"Private"，但仓库可见性是公开的（public），任何人都能直接克隆。

仓库总大小 **844MB**，暴露内容包含两个关键文件：

* **importantAWStokens**：3台 Amazon AWS GovCloud 服务器的管理员凭据。GovCloud是AWS面向美国政府的隔离云区域，承载的是联邦机构的敏感工作负载，能拿到管理员权限意味着对这三台服务器拥有完全控制权。
* **AWS-Workspace-Firefox-Passwords.csv**：CISA内部数十个系统的明文用户名和密码，以CSV表格形式存储。这不是哈希后的密码，不是密钥管理的vault导出，就是浏览器导出的明文密码文件，文件名里的"Firefox"直接暴露了来源——大概率是承包商从Firefox密码管理器里导出后随手提交上去的。

从凭据安全的角度看，这两个文件组合在一起几乎是一份"CISA内部系统访问手册"：有云平台管理员密钥，有内网系统的明文凭据，攻击者拿到后可以直接横向移动。

## 六个月的沉默：9封被忽略的告警

2026年5月15日，法国安全公司 **GitGuardian** 的研究员 **Guillaume Valadon** 在例行扫描中发现这个仓库，试图联系CISA但碰壁——下文会详述这个"碰壁"过程——最终他绕了一圈联系到独立安全记者 **Brian Krebs（KrebsOnSecurity）**，由KrebsOnSecurity直接向CISA通报，CISA才正式进入响应流程。

更值得反思的是Valadon后续披露的细节：在5月15日CISA正式收到通报**之前**，GitGuardian的自动化扫描系统已经针对该仓库的暴露凭据向CISA相关账户发送了**9次自动告警邮件**。全部未获响应。

GitGuardian的商业模式就是在GitHub等公共代码仓库上做持续扫描，检测泄漏的API密钥、令牌、密码等，发现后自动通知账户持有人。这相当于CISA免费获得了一套外部监控服务，但9次告警石沉大海。

用一个简单的等式：**9次未读告警 + 无人值守的公共仓库 = 一次本应1天内处理的事故演变为持续6个月的数据暴露。**

## CISA的响应：48小时才完成密钥轮换

CISA在收到KrebsOnSecurity的通报后，第一时间的确认是快的。但从确认到完成实际的密钥轮换（key rotation），花了**超过48小时**。

CISA的事后报告给出的理由是"系统复杂性以及与联邦机构和行业合作伙伴的互联性导致轮换时间超出预期"。这个解释说得通但并不让人满意——AWS GovCloud的管理员密钥不是联邦机构之间互联的组件，轮换一个IAM密钥在技术上通常只需要几分钟。48小时以上的延迟说明CISA可能并没有一个经过充分测试的、可以在紧急情况下快速执行的密钥轮换预案。

CISA代理首席信息官 **Preston Werntz** 和代理首席信息安全官 **Brad Libbey** 在报告中最终给出的建议是："建议其他组织维持成熟且经过充分测试的密钥管理能力。"翻译成大白话：我们的密钥管理流程在紧急情况下不够用，大家别学我们。

## 通报渠道的混乱：研究者被当皮球踢了

GitGuardian的Valadon在5月15日发现仓库后，尝试了以下渠道联系CISA：

1. **直接给承包商发邮件**——承包商可能没有安全响应职责，或者邮件根本没被看到。
2. **通过CISA的漏洞披露平台（Vulnerability Disclosure Platform）提交**——这个平台的设计初衷是接收影响更广泛网络安全社区的漏洞报告，而不是处理涉及CISA自身的凭据泄露事件。报告被淹没在常规漏洞队列里。
3. **最终联系记者Brian Krebs**——通过媒体施压才触发了CISA的正式响应。

CISA在事后报告中也承认了这个问题：组织自身相关的安全事件报告渠道，与产品/客户相关的事件报告渠道没有明确区分。结果是外部研究者像打乒乓球一样在不同入口之间弹来弹去，浪费了关键的时间窗口。

Valadon在分析中一针见血："泄露数据来报告的人不是威胁。发布security.txt是好的，但不能止步于此。报告流程应该在多个显眼位置公开，确保涉及自身基础设施的报告不会被埋进产品bug的工单队列里。"

## 报告中最让我不安的一个细节：IR剧本里没有"GitHub"这个词

CISA事后报告自曝了一个严重问题：CISA有网络事件响应剧本（incident response playbook），但**这些剧本里没有覆盖GitHub或其他云代码仓库相关场景的内容**。

这意味着CISA在制定事件响应流程时，根本没有把"凭据可能被提交到公共代码仓库"这个场景纳入预案。对于一个以网络安全为核心使命的联邦机构来说，这是一个系统性的盲区。

Valadon的评论很直接：这份报告恰恰说明了为什么不能靠季度扫描，必须对公开GitHub做持续监控。"Private-CISA仓库在公开状态下挂了整整6个月。是公开GitHub的持续监控最终发现了它。如果CISA内部有全面的扫描机制，那些明文密码和被提交的备份早在泄露到外部之前就应该被发现。"

## CISA做对了什么

公平地说，CISA的事后报告也有几个亮点：

* **1. 详细日志起到了决定性作用。** CISA承认正是增强后的日志能力让调查团队能够确认：暴露的凭据未被在CISA环境外使用，客户的敏感数据和任务关键数据未受影响。在凭据泄露场景中，能否证明"凭据是否被滥用"是评估影响的核心问题，而日志就是回答这个问题的唯一可靠依据。
* **2. 零信任架构降低了实际损害。** CISA声称在生产环境和开发环境都采用了零信任原则。即便承包商的凭据被泄露，零信任的微分段、最小权限和持续验证机制可能阻止了攻击者利用这些凭据进行深度横向移动。
* **3. 责任追溯到人。** 泄露凭据的承包商被直接撤销了系统访问权限。
* **4. 公开事后报告本身。** Valadon认为这是最大的亮点：这是他记忆中第一个公开倡导凭据扫描重要性、并主动简化与安全研究者关系的国家级网络安全机构。

## 给安全社区的教训清单

基于这份报告，以下几个教训值得每个安全团队刻在墙上：

* **第一，仓库名不是安全机制。** "Private CISA"这个名字给人虚假的安全感。GitHub仓库的可见性只有public和private两个硬性状态，命名约定不提供任何保护。开发流程中应该加入预提交钩子（pre-commit hook）和CI/CD检查，主动扫描凭据。
* **第二，自动化告警必须有响应SLA。** 9次未读告警不是技术问题，是流程问题。自动告警的接收方必须有明确的值班制度、升级路径和SLA承诺。无人值守的告警比没有告警更危险，因为它制造了一种"我们已经在监控"的安全错觉。
* **第三，IR剧本必须覆盖SaaS和云代码仓库场景。** 如果你的事件响应计划里没有"凭据泄漏到GitHub/GitLab""API密钥在公共仓库被发现""第三方SaaS配置错误"这几个场景，你的剧本就不完整。
* **第四，外部研究者的通报体验需要被设计。** 安全.txt（security.txt）文件是起点而非终点。组织应该建立专门的、与产品漏洞分离的"组织自身安全事件"报告渠道，并在多个显眼位置公开。
* **第五，凭据管理的基本功不能省。** 不要在CSV里存明文密码，不要把AWS管理员密钥提交到任何代码仓库。密码管理器和密钥管理vault是基础设施，不是可选项。

## 最后的思考

CISA这起事件没有黑客组织，没有零日漏洞，没有高级持续性威胁（APT）。就是一个承包商在GitHub上点错了按钮，而CISA的防御纵深在"发现"和"响应"两个环节同时失灵。

这恰恰是最值得警惕的地方：对于绝大多数组织而言，日常运营中的配置错误和流程漏洞，远比国家级攻击者的复杂工具更容易造成实际损害。一个把自身定位为"国家网络安全防御核心"的机构，在最基本的代码仓库卫生和事件响应流程上栽了跟头，这个信号比任何CVE都响亮。

## 技术附录

### 失陷指标（IOC）

| 类型 | 指标 | 说明 |
| --- | --- | --- |
| 暴露资产 | GitHub公共仓库 "Private CISA" | 可见性为public，暴露约6个月 |
| 暴露文件 | `importantAWStokens` | 含3台AWS GovCloud服务器管理员凭据 |
| 暴露文件 | `AWS-Workspace-Firefox-Passwords.csv` | 含CISA内部数十个系统的明文用户名/密码 |
| 暴露数据量 | 844MB | 仓库总大小 |

> 注：本次事件为凭据/数据意外暴露，无传统恶意软件IOC（无C2 IP、无文件哈希、无域名）。上表所列为暴露的资产与文件标识。

###

### 关键威胁实体

| 实体 | 角色 |
| --- | --- |
| **CISA** (Cybersecurity and Infrastructure Security Agency) | 受害机构；美国网络安全和基础设施安全局 |
| **GitGuardian** | 发现暴露的安全公司；持续扫描公共代码仓库 |
| **Guillaume Valadon** | GitGuardian研究员；首个发现并尝试通报的研究者 |
| **KrebsOnSecurity (Brian Krebs)** | 独立安全记者；最终触发CISA响应的通报渠道 |
| **AWS GovCloud** | 受影响云平台；Amazon面向美国政府的隔离云区域 |
| **Preston Werntz** | CISA代理首席信息官（Acting CIO）；事后报告作者之一 |
| **Brad Libbey** | CISA代理首席信息安全官（Acting CISO）；事后报告作者之一 |
| **泄露承包商** | 误将凭据发布至公共GitHub的第三方承包商（身份未公开）；已被撤销系统访问权限 |

###

### 关联MITRE ATT&CK技术（潜在利用路径）

虽然本事件为意外暴露而非主动攻击，但暴露的凭据一旦被恶意行为体获取，潜在利用路径涉及以下技术：

* **T1552.001 - Unsecured Credentials: Credentials In Files**：明文密码以CSV文件形式存储在公开仓库
* **T1078.004 - Valid Accounts: Cloud Accounts**：AWS GovCloud管理员密钥可直接用于云环境访问
* **T1530 - Data from Cloud Storage Object**：获取云凭据后可能直接访问S3等存储对象
* **T1021 - Remote Services**：利用获取的内部系统凭据进行远程访问
* **T1078 - Valid Accounts**：明文凭据可用于多种内部系统的合法登录尝试

###

### 关键时间线

| 日期 | 事件 |
| --- | --- |
| 约2025年11月 | 承包商将数据发布至公共GitHub仓库（"Private CISA"） |
| 2025年11月–2026年5月 | 仓库公开暴露约6个月；GitGuardian发送9次自动告警，均未获响应 |
| 2026年5月15日 | GitGuardian研究员Guillaume Valadon发现仓库；尝试通过承包商邮件、CISA漏洞披露平台通报未果；联系KrebsOnSecurity |
| 2026年5月15日 | KrebsOnSecurity直接通报CISA；CISA确认收到 |
| 2026年5月15–17日 | CISA完成AWS密钥及暴露凭据的轮换（耗时>48小时） |
| 2026年7月 | CISA发布事后报告 |

##

## 参考来源

* 从CISA最近的GitHub泄露事件中吸取的教训: https://blackhatnews.tokyo/archives/121769
* CISA 近期 GitHub 数据泄露事件的经验教训 – Krebs on Security - Cybernoz: https://cybernoz.com/lessons-learned-from-cisas-recent-github-leak-krebs-on-security/
* Lessons Learned from CISA's Latest GitHub Leak - Krebs on Security - TECH SPARKING: https://techsparking.com/lessons-learned-from-cisas-latest-github-leak-krebs-on-security/
* CISA近期GitHub泄露事件的经验教训: https://poseidon-us.com/2026/07/13/lessons-learned-from-cisas-recent-github-leak/
* 高危：从CISA近期GitHub泄露事件中汲取的教训: https://securityintelhub.com/article/lessons-learned-from-cisa-8217-s-recent-github-leak

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2AqAgxkehic9reynyobeEoOxwxOBrYrdjpuwE9eRaLTgBEVEuichLmtKsGusaxticjIQZGPZhCtODWekJxj0Zqscw/0?wx_fmt=png)

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