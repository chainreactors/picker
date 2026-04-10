---
title: 【安全圈】AI 数据独角兽遭黑客攻击，一周内吃了 5 场官司，Meta 紧急暂停合作
url: https://mp.weixin.qq.com/s/stjWO0x8awF11M7IhU428w
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:42:42.490382
---

# 【安全圈】AI 数据独角兽遭黑客攻击，一周内吃了 5 场官司，Meta 紧急暂停合作

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHibMiabGYgOP8hoeXLCSlxQ428H4Mc2nhlSZof4arPviakLkJz7ic1QMfpPemVeUlXYra4picBibS9pdKTBsia4YVHLs30Noa1ESibrkg/0?wx_fmt=jpeg)

# 【安全圈】AI 数据独角兽遭黑客攻击，一周内吃了 5 场官司，Meta 紧急暂停合作

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

据外媒 Business Insider 昨日报道，美国 AI 训练数据平台 Mercor 遭黑客攻击，超过 4 万人的个人信息因此泄露，一周内被多名承包商在美国多地提起至少五起诉讼，指控其未能妥善保护个人敏感信息。

Meta 已于 4 月 4 日暂停与该公司的全部合作，恢复时间未定；OpenAI 同日称其正在调查专有训练数据是否受到波及。

这起事件起源于 3 月 27 日一场针对开源工具 LiteLLM 的供应链攻击，黑客组织 TeamPCP 通过植入恶意代码，在线上存续约 40 分钟内窃取受感染企业的云账号密钥、数据库密码及服务器访问凭证。

在 Mercor3 月 31 日确认泄露同日，另一个黑客组织 Lapsus$ 宣称掌握 4TB 的 Mercor 数据，包括源代码、数据库记录和视频资料，并在暗网上公开叫卖。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFxyHW5vIHFibibuU5zAo1ia5XKZrIyF2IDQt8DywWfzbhibT2BLugjSsUBg0kjf6TQ6rfiaFAPhl4e8NRYvPRbDKRU9WBljFVRCbG0/640?wx_fmt=jpeg&from=appmsg)

在 Telegram 上挂牌出售的 Mercor 数据截图

Mercor 成立于 2023 年，其客户涵盖 Anthropic、OpenAI 及 Meta，主要招募医学、法律、文学等领域的专家，为 AI 公司的模型训练提供数据。该公司估值达 100 亿美元（约合人民币 686.8 亿元）。

此次泄露之所以令各家 AI 大厂紧张，不只是因为个人数据外泄，更是因为 Mercor 同时身处多家竞争对手的数据流水线之中，一旦数据选择标准、标注规范、训练策略等核心方法论细节被竞争对手获取，各家公司耗费数年、数十亿美元构筑的技术护城河将面临威胁。

事件发酵至今不足两周，Mercor 已在美国多地收到五起诉讼。诉状指控该公司网络安全防护措施严重不达标。

**一、三位 22 岁创始人的百亿帝国，在 AI 供应链安全的薄弱处被击中**

Mercor 由布伦丹 · 福迪（Brendan Foody）、阿达什 · 海尔马斯（Adarsh Hiremath）和苏利亚 · 米达（Surya Midha）三人于 2023 年创立，三人均毕业于旧金山湾区贝拉明预科学院，曾是同一支辩论队的队友。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGmYN0NrTVRRYqHJmDYDa8ia4GCXG2lhic0rltkGasR52qh8na1nicoVK1UA1npDe99KV7oKc0vic9pLTJb2fqvLdLmDntwbJyp8o0/640?wx_fmt=jpeg&from=appmsg)

Mercor 三位创始人阿达什 · 海尔马斯（Adarsh Hiremath，左）、布伦丹 · 福迪（Brendan Foody，中）和苏利亚 · 米达（Surya Midha，右）（图源：Global Indian Times）

2025 年 10 月，Mercor 完成由风险投资机构 Felicis Ventures 领投的 3.5 亿美元（约合人民币 24.038 亿元）C 轮融资，估值达 100 亿美元（约合人民币 686.8 亿元）。该公司三位创始人以 22 岁之龄同时跻身福布斯认定的全球最年轻的白手起家十亿美元富翁行列。

Mercor 的商业模式是做 AI 大厂与领域专家之间的桥梁，负责招募医生、律师、科学家、记者等各类专业人士，为 AI 公司生产高度定制化的训练数据，每日结算额规模超百万美元。

Wired4 月 4 日报道揭示了一个内部代号为 "Chordus" 的 Meta 项目，目标是训练 AI 模型利用多个网络来源核实信息，而这个项目目前已因攻击事件被迫暂停。

正是因为处于这一节点，Mercor 的数据泄露后果格外棘手。多家机构共用同一家数据供应商，意味着一次攻击就能同时触及多家竞争企业的机密。

The Next Web 指出，训练数据集或许可以复制，但训练方法论几乎不可能，而后者正是这次泄露最令人担忧的部分。

**二、40 分钟的窗口期，一个开源工具撬动整个 AI 供应链**

这起攻击的技术核心是 LiteLLM，一款用于将各类应用程序接入 AI 服务的开源 Python 库，每月下载量约 9700 万次，广泛存在于全球约 36% 的云环境中。安全公司 Snyk 的数据显示，LiteLLM 每天被下载数百万次。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFUW2ibJxezt2ugo5ldLDcTatJbskQNC6TBXxreMkOx0qibg4ia3jq0CRn4hYWEicTR3icnqfhvlOvzZXCHUe7BxicxZKdjV3slJxT4g/640?wx_fmt=jpeg&from=appmsg)

LiteLLM 供应链攻击技术流程图（图源：GitGuardian）

3 月 27 日，攻击者 TeamPCP 使用被盗的开发者凭证，向 Python 包索引（PyPI）发布了 LiteLLM 的两个恶意版本（1.82.7 和 1.82.8），这两个版本在被检测发现、下架之前，在线上存续了约 40 分钟。

针对开源工具 LiteLLM 的供应链攻击示意图（图源：Medium）

然而这短短 40 分钟足以让大量企业下载并部署受感染的版本。安全研究人员将此次攻击的源头追溯至更早期针对安全工具 Trivy 的入侵，攻击者 TeamPCP 通过攻破 Trivy，获取了 LiteLLM 维护者的开发账号凭证，再凭借这些凭证直接登录 PyPI 发布了恶意版本。

Mercor 在 3 月 31 日向内部员工发送的邮件中承认：" 近期发生了一起影响我们系统和全球数千家机构的安全事件。"

该公司发言人海蒂 · 哈格伯格（Heidi Hagberg）告诉 TechCrunch，安全团队已迅速采取措施遏制和修复事件，并引入第三方法证专家展开调查，但她拒绝就 Lapsus$ 的声索或是否有客户数据被实际窃取等具体问题作答。

以社会工程和凭证盗窃著称的老牌勒索黑客组织 Lapsus$，随后在其泄露站点上公开声称已入侵 Mercor，并在暗网上挂出拍卖帖，声称持有 4TB 的 Mercor 数据，包括逾 200GB 的数据库、约 939GB 的源代码、3TB 的视频和验证数据，以及该公司 TailScale VPN 账户的全部数据。

TechCrunch 发现 Lapsus$ 发布的部分样本，其中包含疑似来自 Mercor 内部 Slack 的数据、工单记录，以及两段据称展示 Mercor AI 系统与承包商对话的视频。

**三、Meta 无限期暂停合作，承包商突然失去收入来源**

据 Wired 援引两名知情人士，Meta 已暂停与 Mercor 的全部合作，且暂停期限不定。Meta 对此未有任何公开声明。

OpenAI 发言人告诉 Wired，OpenAI 正就其专有训练数据在此次事件中可能遭泄露的情况展开调查，并强调此次事件不影响任何用户数据，OpenAI 目前也没有暂停与 Mercor 合作的计划。

Anthropic 没有就外界的采访请求作出回应。谷歌同样在评估此次泄露的波及范围。

这场合作暂停对 Mercor 旗下承包商造成了直接冲击。据 Wired 发现的内部通讯，参与 Meta 相关项目的承包商在暂停期间无法记录工时，实际上已处于失业状态。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFs3QGEkz20uqcMRRic1O3bWvJ7IXVlWic0P4ia8EdDMqyI8n6r9NGxSDj5AvXjmXq8VJZ0N5AIKaq7jEYJOMVm70E5iaic4Xp8k8us/640?wx_fmt=jpeg&from=appmsg)

AI 训练数据标注工作场景（图源：Getty Images）

Mercor 试图将受影响的承包商调配至其他项目，但据知情人士透露，这些承包商起初甚至不知道合作被叫停的原因。

法律层面的事态发展迅速。4 月 1 日，夏威夷瓦希阿瓦居民丽莎 · 吉尔（Lisa Gill）向美国加利福尼亚州北区联邦地区法院提起集体诉讼，称自己为处理此次泄露事件的后续问题耗费了大量时间，且面临更高的身份盗窃风险。

另一名承包商纳蒂维亚 · 埃森（NaTivia Esson）也递交了诉状，她自称于 2025 年 3 月至 2026 年 3 月间为 Mercor 工作，每次接单都需填写含个人信息的 W-9 税表，并 " 相信公司会采取合理措施保护这些信息 "。

一周内，Mercor 共收到五起诉讼。其中一起还将 Berrie AI 和合规机构 Delve Technologies 一并列为被告，LiteLLM 由 AI 开发工具公司 Berrie AI 开发，此前持有由自动化合规认证机构 Delve Technologies 出具的 SOC2 和 ISO 27001 安全认证，诉状指控前者提供了存在安全漏洞的工具，后者出具了不实的安全认证背书。

上个月，Delve 曾公开否认一篇匿名 Substack 文章中关于其协助伪造合规、安排虚假安全审计的指控。

根据法律研究机构 Cornerstone Research 对 2018 年至 2021 年间数据泄露和解案例的统计，此类案件赔偿金额通常在每位集体成员 1 至 5 美元（约合人民币 6.87 至 34.3 元）之间，有记录经济损失的受害者有时可获更多赔偿。

**结语：AI 数据外包暗藏结构性风险，一次攻击影响多家顶级实验室的护城河**

目前，案件调查仍在进行，诉讼尚处早期阶段。这场针对 Mercor 的攻击暴露出 AI 产业一个结构性盲点。当多家顶级 AI 实验室将敏感的训练工作外包给同一家供应商时，这家供应商自身的安全漏洞就成了整个行业的共同风险暴露点。

安全公司 Recorded Future 的勒索软件分析师艾伦 · 利斯卡（Allan Liska）说，攻击者 TeamPCP 的动机明确是金钱驱动，并已公开表示将与勒索软件和勒索团伙合作，针对受影响企业发起规模化攻击。相比 2023 年 Cl0p 组织利用 MOVEit 漏洞一次性影响近 1 亿人的案例，AI 训练数据领域的供应链攻击在商业损害维度上各有不同。

***END***

阅读推荐

[【安全圈】Claude Code 源码泄露遭利用，攻击者借 GitHub 散播窃密木马](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075434&idx=1&sn=38835976425f7fc5a2f505d16e2e7c05&scene=21#wechat_redirect)

[【安全圈】GrafanaGhost：攻击者可利用 Grafana 泄露企业数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075434&idx=2&sn=0c081efedc82241e98bf1346f1884ad6&scene=21#wechat_redirect)

[【安全圈】SaaS 集成商遭入侵，Snowflake 客户数据被盗](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075434&idx=3&sn=29e56481c53f45c906a0a82e40418478&scene=21#wechat_redirect)

[【安全圈】朝鲜关联黑客利用 GitHub 作为 C2 基础设施攻击韩国](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075407&idx=1&sn=09f221b7c8c762cb312a7520dbc12557&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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