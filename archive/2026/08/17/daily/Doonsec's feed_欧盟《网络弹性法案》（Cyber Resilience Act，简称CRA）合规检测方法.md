---
title: 欧盟《网络弹性法案》（Cyber Resilience Act，简称CRA）合规检测方法
url: https://mp.weixin.qq.com/s/1Jkx6ASOowHfES76rmvDKg
source: Doonsec's feed
date: 2026-08-17
fetch_date: 2026-08-18T02:51:22.242668
---

# 欧盟《网络弹性法案》（Cyber Resilience Act，简称CRA）合规检测方法

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/mddylWtMic28lncnzdtAHDEDwnLh84bYS6J2oxOZiamQfg9JibK26UkRdsReg4aIczyMMiaia9ibpxUicEiaJYOItgHJLCeO855XUOfiae7DviamVduwk/0?wx_fmt=jpeg)

# 欧盟《网络弹性法案》（Cyber Resilience Act，简称CRA）合规检测方法

苏州华克斯
苏州华克斯

华克斯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

欧盟《网络弹性法案》（Cyber Resilience Act，简称CRA），它并不像传统产品那样有一个单一的“检测方法”，而是建立了一套基于产品分类、风险评估和符合性评估的综合合规验证体系。

      结合欧盟委员会标准化请求M/606框架，CRA的检测与合规评估主要围绕“水平通用标准（Type A/B）”与“垂直产品标准（Type C）”的协同展开。

一、 核心检测与评估框架（Type A/B/C 协同机制）

      CRA的检测并非仅依赖最终测试，而是要求将Annex I（基本网络安全要求）作为法律红线，通过以下三层标准体系进行“三层叠加评估”：

Ø Type A（水平框架标准）： 提供通用的风险评估方法论、安全设计（Security by Design）原则和威胁建模基础。

Ø Type B（水平技术措施标准）： 将抽象要求转化为可验证的过程和控制清单，如漏洞处理流程（prEN 40000-1-3）、软件物料清单（SBOM）管理、通用安全控制目录等。

Ø Type C（垂直/产品特定标准）： 针对具体产品类别（如工业OT、消费物联网等）提供细化的技术要求和评估准则。

> 注：由于目前许多协调标准（如prEN 40000系列）仍处于草案阶段，检测认证机构在现阶段通常采用“Annex I基本要求 + 现有最佳实践（State-of-the-art）”进行差距分析（Gap Analysis）和预评估。

二、 具体检测与验证执行步骤

在实际操作中，制造商或检测认证机构通常通过以下步骤完成技术验证：

**1.****网络安全风险评估与威胁建模**

方法： 定义资产，使用STRIDE模型（欺骗、篡改、抵赖、信息泄露、拒绝服务、权限提升）等识别威胁。

验证： 评估风险发生的可能性与影响（Likelihood x Impact），并记录风险接受标准及缓解措施。

**2.****安全设计与架构验证**

方法： 审查产品是否遵循安全默认配置（Secure by Default）和安全设计原则。

验证： 检查11个生命周期活动（规划、需求、架构、实现、验证与确认V&V等）的输入与输出，验证安全架构与控制的有效性。

**3.****安全测试与渗透测试**

方法： 结合Type B和Type C标准，对产品的安全控制进行有效性验证。

验证： 执行漏洞扫描、渗透测试和源代码审计，以验证安全架构的防御能力。

**4.****漏洞处理流程审核**

方法： 依据EN 40000-1-3等标准，审查漏洞处理机制。

验证： 检查是否具备协调漏洞披露（CVD）政策、SBOM文档生成能力，以及是否能在法定时间内（24小时早期预警、72小时补充报告）向ENISA和CSIRT上报严重事件。

三、 基于产品分类的合规评估路径

CRA根据产品的风险等级，规定了不同的检测与评估路径：

Ø默认类别产品（Default）： 适用模块A（Module A），即制造商内部控制与自我声明。制造商自行执行风险评估、编制技术文档并签署符合性声明（DoC）。

Ø重要 I 类产品（Annex III Class I）： 如操作系统、路由器、智能家居、密码管理器等。若完整应用了协调标准或网络安全认证方案，可自评估；否则必须引入第三方公告机构（Notified Body）进行欧盟型式检查+生产内部控制（Module B+C）或全面质量保证（Module H）。

Ø重要 II类产品（Annex III Class II）： 如防火墙、入侵检测系统、防篡改微处理器等。通常必须通过第三方公告机构（Module B+C 或 Module H）进行评估。

Ø关键类产品（Annex IV Critical）： 必须通过欧盟通用准则网络安全认证（EUCC）等至少达到“实质级”保证水平的认证方案来证明合规。

四、 最终交付物与合规证明

完成上述检测与评估后，需输出以下法定文件以证明合规：

Ø技术文档（Technical Documentation）： 包含设计细节、威胁模型、SBOM、测试报告、漏洞处理流程及持续监控计划等。

Ø欧盟符合性声明（EU Declaration of Conformity, DoC）： 由制造商签署，声明产品符合Annex I要求。

ØCE标志： 在产品上可见地加贴CE标志，表明其符合CRA要求。

> 由于CRA的漏洞报告义务已于2026年9月11日生效，全面产品义务将于2027年12月11日生效。

**CRA****（欧盟网络弹性法案）合规差距分析自查清单**

![](https://mmecoa.qpic.cn/mmecoa_png/mddylWtMic29vczhJCTlT6IfSr6lkYicsWuBjJcOxV5UfLCAFicrOcBial395uZQYxqiaoT6OicicOa3icgSZVMeHsZQ4Dnq7eVQED4oI8khSnNhYc0/640?wx_fmt=png&from=appmsg)

**下载表格：CRA****（欧盟网络弹性法案）合规差距分析自查清单，点击“阅读原文”**

**文件包含3个工作表：**

**1.****差距分析总表**（100条检查项，覆盖 Annex I 全部要求）按三大模块逐条展开：

|  |  |  |
| --- | --- | --- |
| **模块** | **覆盖内容** | **检查项数** |
| **Part I —****交付时要求** | (1) 交付安全、(2) 风险评估 | 8项 |
| **Part I — 11****项功能要求** | (a)安全默认配置 → (k)安全更新机制 | 52项 |
| **Part II —****漏洞处理** | (1)~(8) 漏洞识别、修复、测试、披露、CVD、信息共享等 | 27项 |
| **Part III —****事件报告** | R1主动利用漏洞报告、R2严重事件报告、R3重大未修补漏洞报告 | 9项 |

每条检查项均包含：条款编号、要求类别、CRA原文描述、具体检查项、**符合状态**（留空供填写）、**差距说明/整改措施**（留空）、**证据/文档**（留空）。

**2.****产品分类评估** — 帮助企业确认产品所属CRA类别（默认类/重要I类/重要II类/关键类）及适用合规路径。

**3.****使用说明** — 包含使用方法、符合状态填写标准、时间规划建议、关键交付物清单和参考标准。

**使用建议：** 建议先填写"产品分类评估"表确定产品类别，再在"差距分析总表"中逐条对照。符合状态可标记为"已满足/部分满足/未满足/不适用"，对未满足项填写整改计划和所需证据文档。

---

相关内容：

[中国、美国、欧盟，医疗器械软件及网络安全检测法规对比分析](https://mp.weixin.qq.com/s?__biz=MzI3NzUyNjU5Mg==&mid=2247486215&idx=2&sn=65889d730d276a6396d07fe19a43f989&scene=21#wechat_redirect)

[物联网固件安全缺陷检测研究](https://mp.weixin.qq.com/s?__biz=MzI3NzUyNjU5Mg==&mid=2247485940&idx=1&sn=56d519bf046f5732cd5a08c3b0d77e0f&scene=21#wechat_redirect)

![](https://mmecoa.qpic.cn/mmecoa_png/mddylWtMic2icofR9R7VzKtiaIRjWYMo6AzicBXk2pQwdzAOpJIWj0H3wAw7ibWKa4Hb0l1MUhWoMqJtYWZJhqh7SjibuUa8t6N8YUOO0bOxjrnibI/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Napicagb93BKfegKR4EsIAvicPkYZwSMBD3LBscvxkCID4VYjkVmANGt15ic8Mj9vevPaaTBXjhpcMOWkMgY3Yibpw/0?wx_fmt=png)

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