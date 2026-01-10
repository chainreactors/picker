---
title: 国家数据局领导班子调整，明确2026年“数据要素价值释放”重点任务；国安部警示：违规部署开源大模型导致敏感数据跨境传输| 牛览
url: https://mp.weixin.qq.com/s/ZE0ssPhpCWYHkrduANqmUg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:29:05.128954
---

# 国家数据局领导班子调整，明确2026年“数据要素价值释放”重点任务；国安部警示：违规部署开源大模型导致敏感数据跨境传输| 牛览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkCLjuXaE0XiaWEqCuDicuowIA2qHwdhdI91IYCcuAUpQnFC5eibOy7RibqZ16qUF0INXptOdZIfaCzrYQ/0?wx_fmt=jpeg)

# 国家数据局领导班子调整，明确2026年“数据要素价值释放”重点任务；国安部警示：违规部署开源大模型导致敏感数据跨境传输| 牛览

安全牛

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkCLjuXaE0XiaWEqCuDicuowIASyOjwPSrGXS3XzT0cKK1whuWNmMjSYYMR9R6ADEqIxGhr37fFeiccxg/640?wx_fmt=png&from=appmsg)

**新闻速览**

* 国家数据局领导班子调整，明确2026年“数据要素价值释放”重点任务
* 国安部警示：违规部署开源大模型导致敏感数据跨境传输
* 美国暂停支持GFCE和Hybrid CoE，国际网络安全合作格局生变
* 阿里云2026云上安全健康体检正式开启
* 从AI factories到RAG，生成式AI安全的现实挑战
* VPN不等于隐身：FBI如何用1100个IP击穿cyberstalking
* ChatGPT新漏洞"ZombieAgent"可持续窃取用户敏感数据
* Microsoft 365遭大规模钓鱼攻击，MX记录配置错误成突破口
* 百万Chrome用户中招，恶意AI插件窃取ChatGPT对话记录
* PCI DSS 4.0合规困境:密码管理器从便利工具转变为合规基础设施
* Gmail AI全面升级：三大智能功能助力邮件管理效率提升

**特别关注**

**国家数据局领导班子调整，明确2026年“数据要素价值释放”重点任务**

1月7日，国务院任命张建民为国家数据局副局长。张建民曾任国家发改委投资司司长等职，上任后该局领导架构恢复为“一正四副”。国家数据局负责协调数据基础制度建设、统筹数字中国建设等。近日召开的全国数据工作会议将2026年定为“数据要素价值释放年”，部署了推进数据科技与产业融合、强化数据赋能人工智能发展等八大重点任务，旨在推动数据“供得出、流得动、用得好、保安全”，促进数据要素融入经济价值创造。

原文链接：

https://mp.weixin.qq.com/s/7A7xQAdaE-9hTV2Pi4-R9Q

**热点观察**

**从AI factories到RAG，生成式AI安全的现实挑战**

随着企业加速部署生成式和智能体AI系统，网络安全成为制约其安全扩展的关键因素。Gartner数据显示，近三分之一组织遭遇过提示词操纵攻击，约30%面临生成式AI基础设施直接攻击，但Lakera研究表明仅不到五分之一组织认为自身GenAI安全成熟度高。为应对威胁，Check Point推出AI Cloud Protect，集成于NVIDIA Enterprise AI Factory参考架构。该方案通过NVIDIA BlueField平台实现实时监控与隔离，在不消耗GPU资源的前提下保护AI运行时环境，解决工作负载隔离、数据可见性及运行时操控风险。AI安全需覆盖基础设施、模型、数据管道及用户交互，从边界防御转向核心架构层嵌入，确保AI规模化部署的安全性与性能。

原文链接：

https://www.expresscomputer.in/news/securing-ai-factories-why-enterprise-grade-cybersecurity-is-becoming-foundational-to-ai-adoption/131546/

**ChatGPT新漏洞"ZombieAgent"可持续窃取用户敏感数据**

OpenAI近期为ChatGPT增加了Connectors连接器等代理功能，可快速对接Gmail、Outlook、Google Drive等外部系统，但这也带来严重安全风险。Radware研究员Bado发现名为"ZombieAgent"的新型攻击技术，可完全绕过OpenAI的URL修改防护机制。

该攻击利用预构建的静态URL实施数据窃取。攻击者通过恶意邮件植入预设URL列表，每个URL对应特定字符。当用户正常使用ChatGPT处理Gmail任务时，ChatGPT会按攻击者指令逐字符提取敏感数据并"打开"相应URL完成外泄。由于ChatGPT仅访问预设链接而非动态生成URL，成功规避了OpenAI的安全过滤器。

此前Radware曾发现ShadowLeak漏洞，可通过间接提示注入技术窃取Gmail数据。虽然OpenAI随后禁止ChatGPT动态修改URL，但ZombieAgent证明该防护已被攻破。更严重的是，该技术可实现持久化攻击，持续窃取用户与ChatGPT的所有对话内容，并具备传播能力定向攻击特定目标。攻击过程无需用户额外操作，数据直接从OpenAI云基础设施泄露，本地防御系统无法检测。

原文链接：

https://www.infosecurity-magazine.com/news/new-zeroclick-attack-chatgpt/

**Microsoft 365遭大规模钓鱼攻击，MX记录配置错误成突破口**

Microsoft威胁情报团队警告，自2025年5月以来，针对Microsoft 365账户的钓鱼攻击显著增加，攻击者利用邮件路由设置和域名欺骗防护配置错误，使恶意邮件看似来自企业内部。这些攻击常与Typhoon2FA等钓鱼即服务工具包结合使用，以HR部门和IT安全团队名义发送虚假通知窃取登录凭证。

攻击的关键在于企业错误配置MX记录，未将其直接指向Office 365服务器。这导致Microsoft的欺骗检测和邮件过滤工具默认未启用，攻击者可利用宽松的邮件服务器设置，在"收件人"和"发件人"字段使用企业域名，使恶意邮件伪装成内部通信。MX记录直接指向Office 365的租户不受此攻击影响。

典型的钓鱼场景包括伪造文档签署请求、密码更新通知(引导至虚假登录门户)以及冒充CEO的虚假发票，要求支付数千美元。由于邮件看似来自同事，目标更易上当。成功的凭证窃取可能导致数据泄露、商业邮件诈骗(BEC)攻击甚至资金损失。

Microsoft建议企业将MX服务器正确配置为直接指向Office 365，实施严格的DMARC规则防止域名欺骗，确保第三方服务正确配置，并为Microsoft Entra ID特权角色强制执行抗钓鱼多因素认证(MFA)。

原文链接：

https://www.infosecurity-magazine.com/news/phishing-exploits-misconfigured/

**安全事件**

**VPN不等于隐身：FBI如何用1100个IP击穿cyberstalking**

美国Bigfork市25岁男子Jeremiah Daniel Starr因持续近三年的cyberstalking被判联邦监禁46个月。其以“好友”身份接近受害者Jane Doe，暗中使用50余个电话号码及NordVPN实施威胁与恐吓。FBI通过溯源分析1100余个IP地址，最终锁定嫌疑人。

案件升级至现实暴力：2025年2月9日，Starr向受害者公寓开枪，并伪造“回击袭击者”的情节制造恐慌。调查证实并无他人涉案。受害者长期承受巨大心理压力。Starr于2025年8月认罪，除刑期外还将接受三年监管。该案凸显匿名工具并非“免罪牌”，高强度取证与关联分析可还原复杂数字轨迹。

原文链接：

https://hackread.com/us-man-jailed-fbi-ip-addresses-cyberstalking-case/

**国安部警示：违规部署开源大模型导致敏感数据跨境传输**

国家安全部近日披露，某单位因违规使用开源AI工具，且系统默认开启公网访问未设密码，导致敏感资料被境外IP非法访问和下载。专家指出，开源大模型虽将模型架构、参数及训练数据公开以供免费使用，但其工作原理要求必须存储投喂数据以进行分析，这构成了核心安全隐患。泄露风险主要来自两方面：一是开发者拥有权限可直接查看数据；二是黑客可能利用后台漏洞入侵获取数据。针对此风险，专家建议个人不应上传隐私信息，企业在利用大模型训练数据时，应采用私有化部署，将数据保留在本地并配备专业运维团队，以阻断数据外传路径，确保内部信息安全。

原文链接：

https://mp.weixin.qq.com/s/XcOPnf8gimd7zJbYIdM7WQ

**百万Chrome用户中招，恶意AI插件窃取ChatGPT对话记录**

2025年12月29日，OX Security披露两款Chrome扩展程序正在窃取用户与AI的私密对话，合计影响近百万用户。这两款插件分别为"Chat GPT for Chrome with GPT-5， Claude Sonnet & DeepSeek AI"(60万安装量)和"AI Sidebar with Deepseek， ChatGPT， Claude and more"(30万安装量)，伪装成合法工具AITOPIA，其中一款甚至获得Google的Featured认证标识。

攻击者采用Secure Annex命名的"Prompt Poaching"技术，专门针对用户输入AI工具的敏感问题和专有数据。这些扩展程序通过DOM scraping技术直接读取屏幕文本内容，当用户访问chatgpt.com或deepseek.com时，系统会分配唯一追踪ID"gptChatId"并开始数据采集。

窃取的信息包括用户提示词、AI回复、会话令牌及认证数据，每30分钟打包发送至deepaichats.com或chatsaigpt.com等服务器。更危险的是，卸载其中一个插件后浏览器会自动重定向到另一个，攻击者利用Lovable.dev平台托管虚假隐私政策维持运营。

截至2026年1月7日，尽管已向Google报告，这两款扩展仍可下载。建议立即检查chrome://extensions并删除ID为fnmihdojmnkclgjpcoonokmkhjpjechg或inhcgfpbfdjbjogdfjbclgolkmhnooop的扩展程序。

原文链接：

https://hackread.com/fake-chatgpt-deepseek-extensions-spy-chrome-users/

**产业动态**

**阿里云2026云上安全健康体检正式开启**

2026年1月8日，阿里云「2026云上安全健康体检」正式上线，所有阿里云用户均可参与。今年，阿里云首次将系统稳定性评估与AI安全专项检测纳入体检项，共计覆盖安全、稳定、AI三大维度在内的110余项关键风险，助力用户筑牢2026年云上风险防控的第一道防线。

原文链接：https://mp.weixin.qq.com/s/z-mTaqlrbhW9U0ERRt5Ubw

**PCI DSS 4.0合规困境:密码管理器从便利工具转变为合规基础设施**

PCI DSS 4.0将合规重点从技术控制转向员工行为，密码复用、凭证存储在电子表格、共享登录等日常习惯成为合规失败的主要原因。新标准要求12.6强调基于角色的持续培训和安全意识活动，要求组织证明员工理解其行为对持卡人数据安全的影响。

传统密码规则如长度、复杂度和轮换策略虽满足技术要求，但实际增加了员工负担，导致更多密码重置、可预测模式和重复使用变体，并未改善安全结果。密码管理器可作为合规基础设施，同时满足PCI DSS多项要求:生成唯一凭证减少复用，消除电子表格等不安全存储方式，集中访问审查，配合基于角色的权限支持最小权限原则。

Passwork CEO Alex Muntyan指出，当安全工具与员工工作方式对抗时合规就会崩溃，密码管理器改变了这一动态。Passwork作为本地部署解决方案，帮助组织在自有基础设施内集中管理凭证，提供基于角色的访问控制和审计日志，满足PCI问责期望。

有效的PCI DSS合规项目通过设计减少违规，使安全路径比不安全路径更容易。将密码管理器整合到培训和日常操作中，将合规从项目转变为日常运营的一部分，这正是PCI DSS 4.x衡量员工行为的核心要求。

原文链接：

https://www.helpnetsecurity.com/2026/01/08/passwords-pci-dds-compliance/

**美国暂停支持GFCE和Hybrid CoE，国际网络安全合作格局生变**

2026年1月7日，特朗普总统签署行政令宣布美国退出66个国际组织，其中31个为联合国实体，涉及两个关键网络安全组织:全球网络专业知识论坛(GFCE)和欧洲应对混合威胁卓越中心(Hybrid CoE)。特朗普政府表示继续参与这些组织"有悖美国利益"。

GFCE成立于2015年，由荷兰政府联合41位部长及高层代表共同发起，是致力于全球网络安全能力建设的多方利益相关者平台。该论坛汇聚超过100个国家和组织，包括各国政府、国际机构、私营企业和学术机构，围绕网络安全政策与战略、网络事件管理、网络犯罪、网络安全文化与技能以及关键基础设施保护五大主题开展工作。

Hybrid CoE于2017年在赫尔辛基成立，由欧盟和北约联合领导，专注于增强对混合威胁的抵御能力。该组织将混合威胁定义为融合常规、非常规和网络战术的恶意活动，旨在破坏民主机构、安全和社会稳定。Hybrid CoE为36个成员国和伙伴国提供分析、培训和政策制定支持，帮助各国应对虚假信息、网络攻击、经济胁迫和外国干预等威胁。

此次退出还包括政府间气候变化专门委员会(IPCC)、自由在线联盟(FOC)和全球反恐论坛(GCTF)等组织。

原文链接：

https://www.infosecurity-magazine.com/news/us-leave-global-forum-on-cyber/

**新品发布**

**Gmail AI全面升级：三大智能功能助力邮件管理效率提升**

Google为Gmail推出全新AI Inbox功能，旨在通过智能化手段提升用户邮件管理效率。新功能包含"建议待办事项"和"主题汇总"两大板块，前者自动提取需要行动的优先邮件（如账单提醒、预约确认），后者则按"财务"、"购物"等类别整合相关更新。用户可随时在传统收件箱和AI视图间切换。

Gmail同时推出自然语言搜索功能AI Overviews，允许用户通过提问方式快速获取信息，例如询问"去年给我报价的水管工是谁"即可获得AI整合的答案摘要，该功能目前面向Google AI Pro和Ultra订阅用户开放。

此外，Gmail引入类似Grammarly的Proofread校对工具，可一键优化用词、句式和语法错误，帮助用户润色邮件内容。Google强调所有AI功能均为可选项，且不使用个人内容训练基础模型，数据处理在隔离环境中进行。

值得注意的是，此前仅对付费用户开放的"Help Me Write"撰写助手、邮件线程AI摘要及智能回复建议功能，现已向所有Gmail用户免费开放，大幅降低AI邮件工具的使用门槛。

原文链接：

https://techcrunch.com/2026/01/08/gmail-debuts-a-personalized-ai-inbox-ai-overviews-in-search-and-more/

**联系我们**

合作电话：18311333376

合作微信：aqniu001

联系邮箱：bd@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkCLjuXaE0XiaWEqCuDicuowIACbhEfaIZCk8fPCKKKurDoRceJNGJkeEmesI16Y4QicoYQpib7ibnfwzXw/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

安全牛

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBZmyIrtuKu5NvaM1vicN8Y6b8TFgIImLsIf7G7sbQcuymdibuezvQtS7YgVtEibUWQlqXsxiaviagrB9A/0?wx_fmt=png)

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