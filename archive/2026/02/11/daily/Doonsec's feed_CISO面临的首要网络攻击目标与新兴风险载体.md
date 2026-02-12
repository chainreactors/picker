---
title: CISO面临的首要网络攻击目标与新兴风险载体
url: https://mp.weixin.qq.com/s/e8m6m6elWU8S8vcRtN3Teg
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:20:33.165407
---

# CISO面临的首要网络攻击目标与新兴风险载体

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2ytPC2n6wkDk6qGV58Q6wWnIb4SBbjSWTpVLGpib7fRfU7FA5xXX6bDnibZScFSAwh0ZaGzRs9LKXeck9fXY1Gk8x1u0SXicr7G0/0?wx_fmt=jpeg)

# CISO面临的首要网络攻击目标与新兴风险载体

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

从技术入侵到AI驱动攻击，网络犯罪分子日益将软件开发者视为主要目标，这给CISO们带来了必须应对的系统性风险。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1OfhVTjdkrbGwwsgXKSWCB3pviatwRicvId8ysQfzSWS1UxNcOibHGnFNHRnwNWXdnY04D4vbVZ6xJORu9SsAvzA6DZWBAtypW60/640?wx_fmt=png&from=appmsg)

针对企业软件开发者的威胁正呈现多样化增长态势，迫使安全领导者必须针对这一不断扩大的攻击面制定更灵活的防御策略。

攻击者不再局限于利用应用程序漏洞，而是越来越多地瞄准软件开发者使用的工具、访问权限和可信渠道。这些威胁融合了技术入侵手段（如恶意软件包、开发流水线滥用等）与社会工程学和AI驱动攻击。

"攻击者不再只是试图入侵网络，他们正在试图入侵工作流程，"网络安全公司Immersive的首席应用安全专家Chris Wood表示，"通过入侵开发者绝对信任的工具（如扩展插件和软件包注册表），他们可以在代码编写之前就污染整个开发环境。"

软件开发者持有的令牌、API密钥、云凭证和CI/CD机密比普通办公用户账户拥有更广泛的访问权限，这使他们成为网络犯罪分子的主要目标。

"开发者掌握着王国的钥匙——对源代码和云基础设施的特权访问，这使他们成为高价值目标，"Wood补充道。

CSO采访的安全专家表示，针对软件开发者的威胁可分为几大类：恶意扩展、IDE插件和工具；供应链和依赖项攻击；凭证窃取和环境入侵；社会工程学；以及软件开发工作流中的AI风险。

**Part01**

## ****恶意工具污染开发生态****

应用安全公司Checkmarx的安全研究倡导者Darren Meyer认为，大多数针对开发者的攻击属于"低投入"的非定向攻击。

例如，攻击者会在域名拼写错误的网站上植入被污染的开源软件包，诱骗开发者安装流行工具的恶意版本。

但这类广撒网式攻击只是冰山一角。Meyer警告称，更精准的定向攻击也在活跃，如针对GitHub等软件开发平台的Shai-Hulud蠕虫攻击、近期对npm软件包Chalk的攻击，以及试图入侵Visual Studio Code插件生态系统的尝试。

DevSecOps公司Sonatype的最新研究证实了Meyer关于被污染开源软件包的警告，该研究识别出123.3万个恶意软件包。

已知漏洞组件也构成重大风险。根据Sonatype最新的《软件供应链状况报告》，在漏洞修复四年后，去年仍有4200万次下载了存在Log4Shell漏洞的Log4j版本。

**Part02**

## ****凭证窃取与环境入侵****

攻击者不仅寻找代码中的缺陷——他们还寻求入侵软件开发环境的途径。

过度授权的服务账户、长期有效的令牌和配置错误的流水线等常见安全缺陷，为非法进入敏感软件开发环境提供了便利途径。

"即使是技术最业余的威胁行为者，也能轻易获取存储不当的访问凭证，"云原生安全与可观测性供应商Sysdig的高级网络安全策略师Crystal Morin表示。

**Part03**

## ****恶意内部威胁****

攻击者还试图通过伪装成软件开发承包商或远程雇佣人员来渗透目标企业。

由朝鲜威胁行为者主导的虚假员工计划，依赖使用伪造身份的技术人员，通过社会工程学手段诱骗受害者雇佣他们。一旦进入企业，这些内鬼就会窃取数据和敏感机密，作为勒索诈骗的筹码。

"我们还发现威胁行为者伪装成维护者，向开源项目提交恶意代码，目的是感染流行软件包的用户，XZ Utils后门事件（CVE-2024-3094）就是典型案例，"Sysdig的Morin表示。

**Part04**

## ****软件供应链风险****

一个被入侵的共享软件库等依赖项可能污染所有依赖它的开发者代码，导致软件供应链风险不断扩大。

暴露管理公司Tenable的情报副总裁Gavin Millard表示，来自软件供应链的威胁已超越漏洞利用，成为最大的系统性网络安全风险。

软件供应链风险意味着攻击面已从传统漏洞和被盗凭证扩展到npm或PyPI等平台上的维护者账户劫持。

"最近的S1ngularity和npm维护者劫持事件证明，在常见库中植入一个被污染的更新，几分钟内就能取得比发送一年定向钓鱼邮件或扫描互联网暴露系统更大的成果，"Millard告诉CSO。

他补充说，滥用供应链能为任何对手提供"力量倍增器"。

"对主流用户而言，数据泄露意味着信息泄漏；但对开发者来说，这就像一口被污染的井，可能感染他们开发的每个应用程序和下游的每个产品用户，"Millard解释道。

对供应链抵御网络攻击能力的担忧与日俱增。世界经济论坛最新的《全球网络安全展望》报告显示，65%的大型企业认为第三方和供应链漏洞是他们面临的最大挑战，这一比例较2025年的54%有所上升。

"开发者经常从公共注册表拉取代码、安装第三方依赖项、授予自动化广泛权限，并发布下游系统绝对信任的构件，"应用安全公司Black Duck的高级研发经理Christopher Jess表示。

"攻击者正通过左移到开发者工具链来利用这一现实——污染开源软件包、注册拼写错误的流行库、向IDE市场发布恶意扩展，以及瞄准构建系统，在那里一个被入侵的流水线可能影响每个环境，"他补充道。

**Part05**

## ****混合威胁模式****

Jess指出，攻击者还开始将技术入侵与社会工程学相结合，以提高攻击效力。

"恶意软件包可能被植入隐蔽后门，然后通过伪造维护者消息、紧急安全修复拉取请求或冒充可信协作者等令人信服的方式加速传播，"Jess解释道。

"AI正在提升这些攻击的规模和精准度：钓鱼和借口制造可以更具上下文相关性——匹配仓库名称、提交历史和团队角色——对手可以生成看似合理的代码变更或文档，降低审查时的怀疑，"他表示。

**Part06**

## ****AI辅助开发增加风险暴露****

AI辅助开发和"氛围编程"正在增加风险暴露，特别是因为这类代码通常生成迅速，缺乏充分测试、文档或可追溯性。

网络安全公司APIContext的首席产品官Jamie Beckland警告称，随着软件开发团队采用AI Agent和模型上下文协议（MCP）服务器，工具泛滥与权限不透明构成了新的增长风险。

"MCP服务器可以通过添加设计用于从内部API、数据存储或SaaS系统窃取数据的工具进行修改，"Beckland表示，"风险不仅来自LLM模型，还来自工具接触面及其可触及范围。"

"监控MCP服务器工具基础设施的变化和服务器数据访问权限，对于验证工具和请求变更至关重要。"

网络安全教育公司Secure Code Warrior的CEO兼联合创始人Pieter Danhieux补充说，MCP和AI Agent是攻击者的沃土，因为很容易"故意引入不安全的提示或插入AI增强的恶意代码"。

"此外，我们发现威胁行为者以新方式利用用户身份，即利用混淆代理漏洞欺骗AI Agent代表用户执行未授权操作，"Danhieux表示。

Sonatype对37,000条建议的分析显示，GPT-5虚构了27.8%的组件版本，在某些情况下甚至推荐了实际恶意软件包，这一统计数据强调了人工代码审查的必要性。

根据BaxBench的数据，即使是最好的大语言模型（LLM）生成的解决方案中，62%要么不正确，要么包含安全漏洞，凸显LLM尚无法生成可直接部署的代码。

Tenable的Millard表示，CISO需要"停止执着于单个漏洞，开始掌控整体风险暴露，包括通过AI代码助手自动引入的共享库来源"。

**Part07**

## ****应对措施****

对CISO而言，强化软件开发环境需要技术控制、安全教育和创建安全意识文化的结合。

更严格的身份验证检查、凭证卫生和对数据的最小权限访问，是提升软件开发实践安全成熟度的步骤。

"这些问题的知名解决方案包括在容器中隔离工作空间、集中管理镜像和机密、强制执行定期审计和程序日志记录，所有这些都能有效降低风险，"软件开发平台提供商Coder的EMEA地区CTO Eric Paulsen表示。

数字化转型咨询公司Axiologik的工程主管David Sugden指出，最佳实践始终是将工作流操作与存储在防篡改硬件模块中的不可变SHA哈希值绑定。

"同样，允许列表、机密扫描和软件成分分析继续构成提升保护的DevSecOps基线，"Sugden表示，"控制对外部依赖的直接访问可防范恶意软件包和版本，同时防止下载老旧的不安全软件包。"

网络安全培训公司Security Journey的应用安全倡导者Michael Burch强调了为软件开发者提供持续实践培训的重要性。

"开发者需要能展示影响的实战演练。让他们看到系统如何失效，并赋予他们自行解决问题的能力，"Burch建议道。

**参考来源：**

Software developers: Prime cyber targets and a rising risk vector for CISOs

https://www.csoonline.com/article/4127693/software-developers-prime-cyber-targets-and-a-rising-risk-vector-for-cisos.html

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1QWGTwJ4jnO2icEhSqbRNdWd3iaVBKjlfTsWSdDBiayVW1jWahKjlggw6mzYnEo5D6PMvFzRX6fEpVEic5NqQoVDFCWvHlh48OxrA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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