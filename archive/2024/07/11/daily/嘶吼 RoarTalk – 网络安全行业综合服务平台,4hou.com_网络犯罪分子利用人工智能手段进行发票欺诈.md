---
title: 网络犯罪分子利用人工智能手段进行发票欺诈
url: https://www.4hou.com/posts/wyM1
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-11
fetch_date: 2025-10-06T17:38:51.199661
---

# 网络犯罪分子利用人工智能手段进行发票欺诈

网络犯罪分子利用人工智能手段进行发票欺诈 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 网络犯罪分子利用人工智能手段进行发票欺诈

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-07-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)108957

收藏

导语：恶意分子创建了一种新工具，该工具使用AI来创建用于电信欺诈和BEC的虚假发票。

有安全研究机构发现了一个名为“GXC Team”的网络犯罪团伙，该团伙专门制作用于网上银行盗窃、电子商务欺诈和网络诈骗的工具。2023 年 11 月，该团伙的头目以“googleXcoder”的别名在暗网上发布了多条公告，宣布在暗网上出售的产品最高可享受 20% 的折扣。

这些帖子中向大家介绍了一种新工具，该工具结合了人工智能 (AI)，可用于创建用于电信欺诈和商业电子邮件欺诈 (BEC) 的虚假发票。

据报告，成功的商业电子邮件欺诈 (BEC) 诈骗（例如发票欺诈）平均每起事件可造成超过 12 万美元的损失，给企业造成了超过 24 亿美元的惊人财务损失。

毫无疑问，网络犯罪分子已经认识到人工智能在增强和扩展其业务方面的巨大潜力。但人工智能为他们提供了哪些具体优势？

利用大型语言模型 (LLM) 的人工智能驱动平台（如 FraudGPT 和 WormGPT）的出现改变了游戏规则。这些框架可以创建复杂而精密的商业电子邮件入侵 (BEC) 活动，生成用于洗钱计划的垃圾邮件内容，并提供预制的恶意策略和工具。

就在 2024 年开始之前，即 12 月 30 日，他们推出了其 AI 工具的更新版本，名为“Business Invoice Swapper”。

![image-9.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240619/1718768043205981.png "1718767834872391.png")

此次更新已通过“GXC 团队”的官方 Telegram 频道发布。该工具以租赁方式提供，订阅计划起价为每周 2,000 美元，或者一次性支付 15,000 美元即可无限制使用。

要使该工具发挥作用，操作员必须输入要扫描的受感染电子邮件帐户列表。这涉及在文档中指定凭证以及用于“交换”或欺骗过程的 IBAN 和 BIC 代码。值得注意的是，大多数已识别的受害者帐户主要来自英国和各个欧盟国家，包括但不限于西班牙、法国、波兰、意大利、德国、瑞士等。

该工具采用专有检测算法，通过 POP3/IMAP4 协议仔细检查受感染的电子邮件，识别提及发票或包含付款详细信息附件的邮件。检测到后，它会将预期收件人（如受害者的供应商）的银行信息更改为犯罪者指定的详细信息。然后，更改后的发票要么替换原始邮件，要么发送给预定的联系人列表。这些方法通常用于电信欺诈和众所周知的虚假发票诈骗。

通常，受害公司的会计和员工不会彻底检查看似熟悉或几乎真实的发票，从而导致有未经核实的付款出现。该工具的多语言功能允许自动扫描消息而无需任何人工干预，提供了显著的优势和规模。在这种情况下，该工具的创建者有效地利用人工智能来完成一项专门的任务——识别包含付款详细信息的发票。此外，该工具还配备了多语言支持，使其能够处理和理解各种语言的数据，这是处理以不同语言编写的发票的关键功能。

此前，“GXC 团队”因创建各种在线欺诈工具而声名狼藉，这些工具包括从受感染的支付数据检查器到复杂的网络钓鱼和短信钓鱼工具包。他们被认为是这一非法领域的主谋，为网络犯罪分子提供一套现成的工具，旨在欺骗全球消费者。此外，他们还提供持续的更新和技术支持以进行欺诈。

目前，“GXC 团队”开发的工具能够针对 300 多个实体，包括顶级金融机构、政府服务、邮政服务、加密货币平台、支付网络和主要国际在线市场，包括 AMEX、亚马逊、币安、Coinbase、Office 365（微软）、PayPal、ING、德意志银行、邮政银行、DKB AG（Das kann Bank）、BBBank eG（前身为 Badische Beamtenbank）和多家西班牙银行，具体包括 ABANCA、Banca March、Banco de Sabadell、Grupo Caja Rural、Unicaja Banco SA、Caixa Enginyers、Banco Mediolanum、Laboral Kutxa、Eurocaja Dynamic、BBVA 和 Santander。

除了利用人工智能来扩大运营范围外，犯罪者还采取了一种新方法——绕过双因素身份验证 (2FA)，即制作模仿官方手机银行应用程序的恶意 Android 代码。受害者被诱骗安装这个假应用程序，并被要求确认他们的 OTP（一次性密码），然后该密码会被拦截并传输到攻击者管理的命令与控制 (C2C) 服务器。

网上银行系统所需的登录凭据之前是通过网络钓鱼工具包获取的。一旦 OTP 被拦截，恶意分子就可以访问受害者的银行账户，利用地理相关的住宅代理来促进未经授权的访问。

“GXC 团队”还创建了多个工具包，旨在通过虚假的政府网站窃取澳大利亚和西班牙公民的身份信息。在澳大利亚，攻击者冒充“my.gov.au”门户网站，诱骗受害者提供个人信息，然后恶意收集这些信息。他们通过欺骗性在线手段窃取身份信息和并利用人们毫无戒心这一条件进行欺诈。

在西班牙的案例中，“GXC 团队”创建了一个冒充 GOB.ES 网站的伪造登陆页面。这个虚假页面声称支持通过多家银行付款，其目的是通过呈现看似来自政府官方网站的内容来赢得受害者的信任。这种方法被用来欺骗个人与恶意行为者分享敏感信息。

人工智能在网络犯罪中的应用并不是一个全新的概念。已被用于各种恶意目的，例如垃圾邮件，其中神经网络被用来逃避反垃圾邮件过滤器，通常通过马尔可夫链等方法。此外，人工智能还被用于黑市 SEO 等领域，高级参与者使用神经网络来创建欺骗性网络内容。

根据评估，人工智能在网络犯罪活动中市场前景较大的应用领域包括：

**·**为恶意和欺诈目的而生成内容，目的是优化人力资源和扩大运营规模。

**·**通过文本处理和文档分析识别特定对象和目标。

**·**网络犯罪行动的决策和自动化。

**·**利用人工智能驱动的机器人进行先进的社会工程技术。

**·**分析和评分潜在受害者，研究他们的行为，并发现更有效的定位和利用模式。

**·**绕过反欺诈过滤器和网络安全控制（例如使用 Deep Fakes 和 AI 生成的工件）。

**·**影响和干扰活动，其中 AI 将用于情感分析、定位活动和与受众的实际互动（例如在社交媒体网络和替代数字渠道中）。

这些观察突出了 AI 在网络犯罪中不断发展和扩大的作用，对网络安全工作构成了重大挑战。

文章翻译自：https://securityaffairs.com/156863/cyber-crime/artificial-intelligence-tool-for-invoice-fraud.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?KgaEo1j2)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)