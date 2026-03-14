---
title: 网络安全一周大事记（20260313期）
url: https://mp.weixin.qq.com/s/mjl_KqJh35gzGEtq3Yetig
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:04:55.875695
---

# 网络安全一周大事记（20260313期）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HmaGibWBicEEmSTGnuMywWmEkCsJ7up2CokyGDViamlia0d6YbfR7wJxMemWOFrUzgE7yBTvypRq6qSZFbDo3oDHUCyMe9ibVyiah5ZFeVlY83Hac/0?wx_fmt=jpeg)

# 网络安全一周大事记（20260313期）

网络安全研究站

![]()

在小说阅读器中沉浸阅读

为了让大家在繁杂的信息流中快速抓住重点，我们从全球安全情报精选了本周（3月6日-3月13日）最具影响力的10条新闻。无论是企业决策者、技术从业者还是普通用户，这份清单都将为你提供不可或缺的安全视野。#新闻 #资讯 #信息安全

**本周大事**

1. 【高危】n8n平台再曝多个高危漏洞，攻击者可远程执行代码并窃取所有存储凭证
2. 【地缘】伊朗关联黑客组织Handala宣称入侵Stryker与Verifone
3. 【恶意软件】BeatBanker恶意软件通过银行木马与加密货币挖矿程序攻击安卓用户
4. 【研究】Anthropic成立研究院专注应对AI风险
5. 【AI】OpenAI称Codex Security一个月内发现1.1万个高危漏洞
6. 【窃密】MaaS VIP键盘记录器攻击活动利用隐写术与内存驻留技术大规模窃取凭证
7. 【供应链】GhostClaw伪装成OpenClaw工具链，定向攻击开发者窃取系统密码、云凭证与加密钱包
8. 【恶意软件】大规模GitHub恶意软件活动传播BoryptGrab窃密程序
9. 【APT】AI生成“劣质海量”恶意软件：巴基斯坦APT36利用Vibeware战术淹没印度政府网络
10. 【行动】微软主导跨国行动，一举摧毁大型网络钓鱼服务平台Tycoon2FA

**1**

**n8n平台再曝多个高危漏洞，攻击者可远程执行代码并窃取所有存储凭证**

**新闻概览**

工作流自动化平台n8n近日被披露存在多个高危安全漏洞，其中四个被评为“严重”级别，可能导致远程代码执行、凭证泄露及系统完全沦陷。关键漏洞包括：CVE-2026-27577，一个表达式沙箱逃逸漏洞，允许认证用户通过精心构造的工作流参数在n8n主机上执行任意系统命令；CVE-2026-27493，一个存在于Form节点中的“双重评估”缺陷，由于表单端点默认公开且无需认证，攻击者可利用公开表单的输入字段注入恶意表达式，当与其他漏洞（如CVE-2026-27577）链式利用时，可直接升级为远程代码执行。更严重的是，成功利用这些漏洞的攻击者能够读取环境变量 N8N\_ENCRYPTION\_KEY，并用其解密存储在n8n数据库中的所有凭证，包括AWS密钥、数据库密码、OAuth令牌和API密钥。此外，新修复的还包括JavaScript任务运行器中的代码注入漏洞（CVE-2026-27495）和Merge节点的SQL注入漏洞（CVE-2026-27497）。受影响版本包括1.123.22之前、2.0.0至2.9.3以及2.10.0至2.10.1之间的所有版本，已在2.10.1、2.9.3和1.123.22中修复。n8n强烈建议用户立即更新，并在无法立即修补时严格限制工作流权限、禁用风险节点并采用外部运行器模式。

原文链接

https://thehackernews.com/2026/03/critical-n8n-flaws-allow-remote-code.html

**2**

**伊朗关联黑客组织Handala宣称入侵Stryker与Verifone**

**新闻概览**

与伊朗有关联的黑客组织Handala声称对两家大型企业发动了网络攻击。医疗技术制造商Stryker已证实其部分网络基础设施遭遇安全事件，导致系统中断，但未发现勒索软件部署迹象，也暂未确认黑客关于“清除超过20万台设备并窃取50TB数据”的夸张声明。另一方面，支付技术公司Verifone则完全否认其系统被入侵，表示未发现任何证据支持相关指控。Handala为证明攻击，发布了据称是Verifone内部管理界面的截图，但这尚不足以确认其来源或时效性。该组织常以地缘政治紧张为名发起攻击，其行动往往混合了网络破坏与信息宣传。目前，两起事件均处于不同阶段的调查中，真实影响有待进一步核实。

**原文链接：**

https://hackread.com/iran-handala-hackers-verifone-stryker-hacks/

**3**

**BeatBanker恶意软件通过银行木马与加密货币挖矿程序攻击安卓用户**

**新闻概览**

卡巴斯基研究人员发现了一款名为 BeatBanker 的新型Android恶意软件，其通过仿冒Google Play商店的钓鱼网站传播，主要针对巴西用户。该恶意软件最初伪装成政府服务应用“INSS Reembolso”，最新变种则假冒Starlink应用。BeatBanker采用高度复杂的多层攻击策略：它利用原生库在内存中解密加载恶意载荷以逃避检测，并通过Firebase Cloud Messaging作为命令与控制信道。一旦安装，它会部署基于XMRig的门罗币挖矿机，同时滥用无障碍服务权限安装银行木马，窃取登录凭证、监控浏览器活动，并针对币安、Trust Wallet等加密应用进行攻击。在用户进行USDT转账时，恶意软件会覆盖虚假界面并悄无声息地将收款地址替换为攻击者控制的地址。最新样本显示，其银行木马模块已被替换为功能更强大的远程访问木马 BTMOB RAT（作为恶意软件即服务出售），可提供设备完全控制权、键盘记录、GPS追踪及摄像头访问等能力。该恶意软件通过运行播放无声音频的前台服务维持持久化。

**原文链接：**

https://securityaffairs.com/189288/malware/beatbanker-malware-targets-android-users-with-banking-trojan-and-crypto-miner.html

**4**

**Anthropic成立研究院专注应对AI风险**

**新闻概览**

人工智能公司Anthropic宣布成立名为 “Anthropic Institute” 的新业务部门，旨在系统性地研究人工智能带来的多重风险。该机构由公司联合创始人Jack Clark领导，整合了原有的三大核心团队：负责AI网络安全风险研究的 “前沿红队”（曾利用Claude扫描Firefox代码库并测试自主漏洞利用能力）、收集用户与Claude交互数据的 “社会影响团队”，以及发布经济指数报告、研究AI对经济活动影响的 “经济研究团队”。为加强研究力量，公司还从Google DeepMind和OpenAI招募了多位顶尖人才，包括前DeepMind高级研究总监Matt Botvinick和前OpenAI研究员Zoë Hitzig。此外，Anthropic同步扩充了其 “公共政策团队”，任命前Stripe高管Sarah Heck为负责人，并计划春季在华盛顿特区开设办公室，以加强与立法者的沟通并推动AI政策建议，未来还将扩展至国际市场。此举标志着Anthropic在AI安全与治理领域的投入进入体系化、建制化的新阶段。

**原文链接：**

https://siliconangle.com/2026/03/11/anthropic-launches-anthropic-institute-tackle-ai-risks/

**5**

**OpenAI称Codex Security一个月内发现1.1万个高危漏洞**

**新闻概览**

OpenAI宣布其新型AI驱动应用安全代理 Codex Security 在为期30天的研究测试中，于超过120万个代码提交中自主识别出 792个严重漏洞和10561个高危漏洞。该工具并非传统静态扫描器，而是模拟人类安全研究员的工作方式：通过分析整个代码库的上下文，构建威胁模型，探索可能的攻击路径，并在沙盒环境中验证漏洞的可利用性，最终生成易于集成的补丁建议。测试范围涵盖私有代码库及开源项目，已在OpenSSH、GnuTLS、Chromium等广泛使用的项目中发现了漏洞，并获得 14个CVE编号。Netgear产品安全负责人表示，该工具无缝融入其安全开发环境，显著提升了审查效率。Codex Security是此前内部项目“Aardvark”的演进成果，能够从开发者反馈中学习以持续提高精准度。即日起，该工具以研究预览形式面向ChatGPT Pro、企业版及教育版用户开放，并提供30天免费试用。

**原文链接：**

https://www.csoonline.com/article/4142354/openai-says-codex-security-found-11000-high-impact-bugs-in-a-month.html

**6**

**MaaS VIP键盘记录器攻击活动利用隐写术与内存驻留技术大规模窃取凭证**

**新闻概览**

一场依托于名为 VIP Keylogger 的工具开展的规模化凭据窃取活动正构成严重威胁。该恶意软件的最大特点在于其 无文件内存执行 技术，通过将最终载荷隐藏在PNG图片等载体中，利用隐写术和进程挖空等手段，直接在内存中运行，从而有效规避传统基于文件扫描的安全检测。攻击链始于包含伪装成采购订单的RAR附件的鱼叉式钓鱼邮件。恶意执行文件运行后，会依次提取隐藏的DLL，最终从图片中解密并加载VIP Keylogger载荷。一旦激活，该键盘记录器会针对数十种基于Chromium和Firefox的浏览器，窃取保存的登录凭据、信用卡信息及浏览历史，同时也能从Outlook等邮件客户端以及Discord、FileZilla等应用中盗取账户令牌。分析表明，该活动很可能以 恶意软件即服务 模式运营，其核心功能模块（如AntiVM）可配置，允许不同技术水平的攻击者按需购买使用。所有窃取的数据通过SMTP、Telegram等五种渠道外传。

**原文链接：**

https://cybersecuritynews.com/maas-vip-keylogger-campaign-uses-steganography/

**7**

**GhostClaw伪装成OpenClaw工具链，定向攻击开发者窃取系统密码、云凭证与加密钱包**

**新闻概览**

JFrog安全研究人员在npm注册表中发现一个名为 @openclaw-ai/openclawai 的恶意包，其伪装成合法的“OpenClaw Installer”命令行工具，发动了一场针对软件开发者的供应链攻击。该恶意软件（内部代号GhostLoader）利用npm的postinstall钩子全球安装自身，并呈现一个高度仿真的伪造CLI安装界面。当进度条完成后，它会弹出一个酷似macOS Keychain授权的原生对话框，诱骗开发者输入管理员密码，且每次输入均会与系统真实认证机制验证，使错误密码返回真实的失败信息。在用户交互的同时，脚本从命令与控制服务器（trackpipe[.]dev）获取并解密第二阶段的完整恶意框架。该框架具备跨平台能力（影响macOS、Linux、Windows），可窃取系统密码、macOS钥匙串、AWS/GCP/Azure云凭证、BIP-39加密货币种子短语、所有浏览器保存的密码和信用卡信息，以及iMessage历史记录。研究人员强烈建议受影响开发者立即卸载该包、清除隐藏目录、检查shell配置文件，并完全重装系统以确保清除。

**原文链接：**

https://cybersecuritynews.com/ghostclaw-mimic-as-openclaw/

**8**

****大规模 GitHub 恶意软件活动传播 BoryptGrab 窃密程序****

**新闻概览**

趋势科技研究人员发现一场大规模恶意软件分发活动，攻击者利用超过100个GitHub公共仓库传播名为 BoryptGrab 的信息窃密软件。这些仓库伪装成免费软件工具、游戏外挂或实用程序，通过SEO关键词填充提高搜索引擎排名，诱骗用户下载包含恶意软件的ZIP压缩包。下载的文件通过DLL侧加载、VBS下载器或.NET加载器等多条路径启动感染链，最终部署BoryptGrab。该窃密软件以C/C++编写，具备反虚拟机检测和权限提升能力，可针对数十种浏览器（包括Chrome、Edge、Firefox等）窃取保存的凭据，同时瞄准Exodus、Electrum等主流桌面加密货币钱包，并设有“文件抓取器”模块收集特定后缀文件。窃取的数据压缩后上传至攻击者服务器。部分变种还会额外部署名为 TunnesshClient 的PyInstaller后门，建立反向SSH隧道以实现持久远程控制。基础设施中的俄语注释表明攻击者可能具有俄罗斯背景。

**原文链接：**

https://securityaffairs.com/189110/malware/massive-github-malware-operation-spreads-boryptgrab-stealer.html

**9**

**AI生成“劣质海量”恶意软件：巴基斯坦APT36利用Vibeware战术淹没印度政府网络**

**新闻概览**

网络安全公司Bitdefender披露，巴基斯坦背景的APT36组织（亦称Transparent Tribe）正针对印度政府及外交机构发起一场战术诡异的网络攻击活动。该组织不再追求开发精密复杂的单一工具，转而利用人工智能快速生成大量使用Nim、Zig、Crystal等冷门编程语言编写的恶意软件——被研究者称为 “Vibeware”。这些代码质量普遍低下，甚至出现忘记写入C2地址的严重错误，但其核心目的并非技术突破，而是通过 “分布式拒绝检测” 战术，用数量庞大的新变种持续冲击防御体系，耗尽安全分析师精力。攻击链常以携带诱饵PDF的鱼叉式钓鱼邮件开始，一旦受害者点击，恶意软件便会通过多种方式活动：例如 LuminousCookies 工具通过注入浏览器内存绕过Chrome和Edge的App-Bound加密窃取凭据；部分变种会劫持Google Chrome和Edge的桌面快捷方式，在用户启动浏览器时静默加载间谍模块；攻击者还利用Google Sheets下发指令，并通过Slack、Discord等合法云服务外泄窃取的文件，使其活动融入正常办公流量。此外，研究人员发现攻击者在代码路径中植入常见印度教名字“Kumar”，试图误导调查方向。此案例标志着APT攻击正从“技术奇袭”转向“心理与资源消耗战”。

**原文链接：**

https://hackread.com/pakistan-apt36-indian-govt-networks-ai-vibeware/

**10**

**微软主导跨国行动，一举摧毁大型网络钓鱼服务平台Tycoon2FA**

**新闻概览**

由微软牵头，联合欧洲刑警组织及多国执法机构，成功对美国、拉脱维亚、立陶宛等国境内支撑Tycoon2FA网络钓鱼服务的核心基础设施实施了技术取缔。此次行动通过美国法院授权，扣押了运营其控制面板和欺诈登录页面的330个活跃域名。Tycoon2FA是一种高度商业化的“网络钓鱼即服务”平台，通过提供易于使用的逆向代理工具包，使低技能犯罪者也能大规模发起绕过双因素认证的攻击。该服务通过Telegram等渠道向网络犯罪分子销售，允许攻击者配置仿冒页面、实时截获用户凭证和会话Cookie，甚至在密码重置后仍能通过窃取的会话令牌维持访问权限。据微软统计，Tycoon2FA2025年中期一度占其拦截的所有网络钓鱼尝试的62%，单月拦截邮件量超过3000万封，自2023年以来已关联全球约9.6万名受害者。Cloudflare、Coinbase、Proofpoint等多家科技公司参与了此次协同打击。专家指出，尽管此次行动暂缓了威胁，但企业必须转向部署如FIDO2硬件密钥等抗钓鱼的多因素认证，才能有效应对此类利用逆向代理的攻击技术。

**原文链接：**

https://www.csoonline.com/article/4140890/microsoft-leads-takedown-of-tycoon2fa-phishing-service-infrastructure.html

---

如果您觉得本文有价值，欢迎点击关注。本站将持续追踪全球安全态势，每周五更新重要安全情报，为您带来第一手的深度解读与前沿干货**。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/15HGVMWyloZOSdbGl9MB8Ef3JM0WKdpiazPppKm6z0UMEQO2de0DIa0BkfoTp2HeyVjPuMxN5MXXW5tmzvEu1jQ/0?wx_fmt=png)

网络安全研究站

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/15HGVMWyloZOSdbGl9MB8Ef3JM0WKdpiazPppKm6z0UMEQO2de0DIa0BkfoTp2HeyVjPuMxN5MXXW5tmzvEu1jQ/0?wx_fmt=png)

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