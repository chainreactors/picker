---
title: SaaS安全大考：黑客“全明星”盘点与2025年备战指南
url: https://www.freebuf.com/articles/419699.html
source: FreeBuf网络安全行业门户
date: 2025-01-14
fetch_date: 2025-10-06T20:10:37.771033
---

# SaaS安全大考：黑客“全明星”盘点与2025年备战指南

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

SaaS安全大考：黑客“全明星”盘点与2025年备战指南

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

SaaS安全大考：黑客“全明星”盘点与2025年备战指南

2025-01-13 10:32:07

所属地 上海

![](https://image.3001.net/images/20250113/1736745447_6784a1e71afb29d489123.png!small)

2024年，针对SaaS的网络威胁激增，仅在Entra ID中，每秒阻止的密码攻击频次就高达7000次，比前一年增加了75%，钓鱼攻击尝试增加了58%，造成了35亿美元的损失（来源：Microsoft Digital Defense Report 2024）。黑客通常通过合法使用模式来规避检测。

进入2025年，安全团队必须优先考虑SaaS安全风险评估以发现漏洞，并采用SSPM工具持续监控，主动进行系统防御。

以下是2025年需要重点关注的SaaS威胁行为者：

## 1. ShinyHunters

**攻击风格：精准射击（网络犯罪组织）**

**最大受害者：Snowflake 、Ticketmaster 和 Authy**

**“爆炸性”事件：利用一处配置错误，攻破了165多家组织。**

2024年ShinyHunters以无情的SaaS漏洞攻击席卷了整个网络世界，泄露了包括Authy和Ticketmaster在内的多个平台的敏感数据。他们的攻击并非利用供应商的漏洞，而是抓住了 Snowflake客户忽视的一处配置错误。这些用户并未启用多因素认证（MFA）或妥善保护其SaaS环境，因此，ShinyHunters能够轻松渗透、窃取数据并勒索这些Snowflake用户。

**SaaS安全启示：**Snowflake事件暴露了客户端的重大安全疏忽，而非供应商的失误。

企业未能强制执行MFA 、定期轮换凭证或实施允许列表，导致系统容易遭受未经授权的访问。

## 2. ALPHV（BlackCat）

**攻击风格：战略操控（勒索软件即服务，RaaS）**

**最大受害者：Change Healthcare 、Prudential（医疗保健与金融领域）**

**“爆炸性”事件： 与RansomHub的2200万美元退出骗局。**

ALPHV，又名BlackCat，在2024年上演了年度最大胆的操作之一。在通过窃取的凭证从 Change Healthcare勒索了2200万美元后，他们竟然伪造了FBI查封的页面，以误导执法机构和合作伙伴。更戏剧的是，作为合作伙伴的RansomHub公开指控ALPHV独吞赎金并让他们空手而归，甚至分享了一笔比特币交易作为证据。尽管遭到背叛，RansomHub仍公布了被盗数据，导致Change Healthcare既支付了赎金又失去了数据。

**SaaS安全启示：**通过暗网监控追踪凭证泄露，并强制执行单点登录（SSO）以简化身份验证流程，降低凭证风险。

跟踪身份验证活动，尽早检测到被泄露的凭证，并应用账户暂停策略以防止暴力破解攻击。

## 3. RansomHub

**攻击风格：机会主义攻击（勒索软件即服务，RaaS）**

**最大受害者： Frontier Communications （电信与基础设施领域）**

**“爆炸性”事件：卷入ALPHV 的2200万美元骗局风波。**

2024 年初，RansomHub从Knight Ransomware的废墟中崛起，成为最活跃的勒索软件团伙之一。他们以机会主义策略而闻名，因与 ALPHV（BlackCat）的合作登上头条。他们在Change Healthcare事件中的角色影响了超过1亿美国公民，突显了他们利用SaaS漏洞（包括配置错误、弱身份验证和第三方集成）的能力，并最大限度地扩大了自己的影响范围和影响力。

**SaaS安全启示：**警惕利用窃取的个人信息进行的钓鱼攻击，这些攻击更具欺骗性。

实施身份威胁检测工具，监控账户劫持迹象和用户活动异常，以便及时识别并响应潜在的数据泄露。

## 4. LockBit

**攻击风格：持续进攻（勒索软件即服务，RaaS）**

**最大受害者： Evolve Bank&Trust的供应链效应（金融科技领域）**

**“爆炸性”事件：FBI的“Cronos 行动”未能彻底将其消灭。**

尽管 FBI 和NCA（英国国家犯罪局）不断努力摧毁其基础设施，LockBit 在勒索软件的“赛场”上仍然占据主导地位。针对Evolve Bank&Trust等金融科技公司的高调行动，以及对Affirm和Wise等更多公司的供应链影响，巩固了LockBit作为SaaS攻击联盟中最稳定进攻者的地位。

**SaaS安全启示：**优先进行第三方供应商风险评估，并保持对 SaaS 应用连接的可视性，以便尽早发现潜在的利用路径。

使用具备威胁检测、 UEBA（用户和实体行为分析）以及异常检测功能的活动监控工具，实时发现可疑行为。

## 5.Midnight Blizzard（APT29）

**攻击风格：防御性渗透（高级持续性威胁，APT）**

**最大受害者： TeamViewer （远程访问工具）**

**“爆炸性”事件：突破防线，开展无声间谍活动。**

这个组织得到了俄罗斯国家资源的支持，专门攻击关键系统，2024年TeamViewer 成为其突出目标。这个组织并不张扬——不会留下勒索信或在暗网论坛上吹嘘。相反，他们悄无声息地窃取敏感数据，留下的数字足迹微乎其微，几乎无法追踪。与勒索软件团伙不同，像Midnight Blizzard这样的国家支持组织专注于网络间谍活动，低调地收集情报而不触发任何警报。

**SaaS 安全启示：**对关键 SaaS 应用的入侵保持警惕，这些应用往往是国家级行为者的目标。定期进行配置审计以降低风险，并确保实施多因素认证（MFA）等安全访问控制措施。

主动审计有助于最小化入侵影响并限制利用路径。

## 第六人：值得关注的其他团体

**Hellcat：**一个在2024年底崭露头角的勒索软件团伙，已确认对施耐德电气（Schneider Electric）发起攻击。他们的迅速崛起和初期成功预示着2025年可能会采取更激进的策略。

**Scattered Spider：**这个混合型社交工程团伙曾是网络犯罪领域的主要参与者，在遭到逮捕和法律打击后暂时沉寂。尽管他们的活动有所减少，但专家警告称，现在断言他们出局还为时过早。

这两个团体都值得关注——一个是因为其发展势头，另一个是因为其声誉和潜在东山再起的可能性。

## 2025年的关键要点

**错误配置仍是主要目标：**威胁行为者继续利用被忽视的SaaS错误配置，获取关键系统和敏感数据的访问权限。定期审计、强制MFA和凭证轮换是必不可少的防御措施。

**身份基础设施遭受攻击：**攻击者利用窃取的凭证、 API操作和隐蔽的数据外泄绕过防御。监控凭证泄露、实施强MFA 、异常检测和身份监控是防止入侵的关键。

**影子IT和供应链成为切入点：**未经授权的SaaS应用和应用间集成会产生隐藏的漏洞。持续监控、主动监督和自动化修复对于降低风险至关重要。

多层SaaS安全解决方案的基础始于自动化的持续风险评估，并将持续监控工具集成到安全管理中。

这并非他们的最后一舞，安全团队必须时刻保持高度警惕，为迎接新的一年做好准备，继续抵御全球最活跃的威胁行为者。

而不是等待下一次的入侵。

**参考链接：**

> [https://thehackernews.com/2025/01/from-22m-in-ransom-to-100m-stolen.html﻿](https://thehackernews.com/2025/01/from-22m-in-ransom-to-100m-stolen.html)

# 资讯 # 黑客 # 数据泄露

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

1. ShinyHunters

2. ALPHV（BlackCat）

3. RansomHub

4. LockBit

5.Midnight Blizzard（APT29）

第六人：值得关注的其他团体

2025年的关键要点

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)