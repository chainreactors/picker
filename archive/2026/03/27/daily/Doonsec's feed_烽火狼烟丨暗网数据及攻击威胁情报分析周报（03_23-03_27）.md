---
title: 烽火狼烟丨暗网数据及攻击威胁情报分析周报（03/23-03/27）
url: https://mp.weixin.qq.com/s/YUaLOYUaL5q4eaJcKaq-lQ
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:14:54.676837
---

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（03/23-03/27）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mxwq2AF6zpMbvp7zIgCFsDfV0G70vUPvPGwXXVqQGoJFNOfQCFV28zfq7TTtMXv8JI1QdJkkWDbYtqhiapXqlBAcrBHs6NKvT3xGSAEjkalE/0?wx_fmt=jpeg)

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（03/23-03/27）

盛邦安全应急响应中心

![]()

在小说阅读器中沉浸阅读

WebRAY安全服务团队定期针对敏感数据泄露、热点资讯、热点技术、热点漏洞、威胁攻击等情况进行跟踪整理与监测分析，本周总体情况如下：

本周内共发现暗网数据贩卖事件498起，同比上周减少38.05%。本周内贩卖数据总量共计111846.6万条；累计涉及8个主要地区及7种数据分类，数据泄露来源地区分布情况如图1所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpM7AEqiaNbBSDvKibh5uf5Vm2L4OqCCef8kGib61ETI2jKJbaZFK7uSMbA48sIcqXoibgP0iaDHKiaOem2tpTVhH91Svdj4rAYfVRiaJk/640?wx_fmt=png&from=appmsg)

图1 泄露数据来源地区分布情况

本周内泄露数据涉及金融、个人信息、服务等多种类型数据，具体占比如图2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpOJZCD2JicYOUYpjLlxicTTVd7avX06YMoCMgYsEDLgE40Ihu3PVC4LYVzTC1ueHI68GyEmtHwKKPmfcWQ7r0lM6xkVxVNEOAG4s/640?wx_fmt=png&from=appmsg)

图2 泄露信息数据类型占比

近期主要威胁来自恶意软件、钓鱼攻击及供应链攻击，需加强关注；本周内出现的安全漏洞以solidtime项目详情未授权访问漏洞危害程度较大；内部安全运营中心共发现恶意攻击来源IP8875条，主要涉及组件漏洞攻击、SQL注入攻击等类型。

**01.**

**重点数据泄露事件**

**AstraZeneca数据泄露**

泄露时间：2026-03-23

泄露内容：黑客声称已获取并出售约3GB的阿斯利康（AstraZeneca）公司内部数据。阿斯利康是一家全球知名的跨国制药企业，专注于肿瘤、心血管、呼吸系统等领域的创新药物研发与生产。据称泄露内容涉及Java、Angular、Python等源代码，AWS、Azure、Terraform配置等云基础设施相关信息，访问凭证及密钥，以及与员工和账户相关的数据。

泄露数据量：3GB

关联行业：医药

地区：英国

**Crunchyroll数据泄露**

泄露时间：2026-03-23

泄露内容：攻击者声称获取并出售大量来自Crunchyroll平台的数据，样本中包含经过掩码处理的邮箱地址、IP地址等信息。Crunchyroll是一家总部位于美国的知名流媒体服务平台，专注于提供日本动画、剧集及相关内容的在线观看服务。据称此次泄露的数据量约为100GB，包含用户个人信息等内容。

泄露数据量：100GB

关联行业：服务

地区：美国

**Ajax数据泄露**

泄露时间：2026-03-25

泄露内容：荷兰知名足球俱乐部阿贾克斯（AFC Ajax）近日发生一起数据泄露事件，超过30万名球迷的个人信息受到影响。攻击者非法访问了俱乐部的部分IT系统，涉及的数据包括球迷的个人身份信息。

泄露数据量：未涉及

关联行业：体育

地区：荷兰

**Ameriprise Financial数据泄漏**

泄露时间：2026-03-25

泄露内容：黑客宣称入侵了美国金融服务公司Ameriprise Financial，并窃取了约200GB的内部数据。黑客声称获取的数据包含客户的个人信息以及企业内部资料，其中部分数据可能来自公司的Salesforce记录系统。

泄露数据量：200GB

关联行业：金融

地区：美国

**QualDerm数据泄露**

泄露时间：2026-03-25

泄露内容：美国皮肤科服务管理公司QualDerm遭遇重大数据泄露事件，影响其在17个州运营的医疗网络中的310万名患者。泄露的数据类型较为敏感，包括姓名、出生日期、联系方式、医疗记录、诊断和治疗信息，以及健康保险信息，部分用户还涉及政府身份证件数据。

泄露数据量：未涉及

关联行业：医疗

地区：美国

**02.**

**热点资讯**

**WebRTC窃卡攻击绕过CSP防护**

研究人员发现一种新型网页支付窃取攻击，利用WebRTC数据通道绕过内容安全策略，窃取用户支付信息。与传统通过HTTP外传数据的方式不同，该攻击使用基于加密UDP的WebRTC通信加载恶意载荷并外泄数据，使依赖HTTP流量检测的安全工具难以发现。攻击主要利用Magento和Adobe Commerce的“PolyShell”漏洞上传恶意文件并执行代码，目前超过一半的易受攻击站点已被利用。专家指出，该攻击利用WebRTC这一“安全盲区”，即使配置严格CSP仍可能被绕过，建议网站及时修补漏洞、检查异常脚本并加强对非HTTP通信行为的监测。

消息来源：

https://thehackernews.com/2026/03/webrtc-skimmer-bypasses-csp-to-steal.html

**LiteLLM供应链攻击震动AI开发生态**

广泛使用的AI开发工具LiteLLM遭遇严重供应链攻击。攻击者入侵维护者账户，在PyPI上发布被植入恶意代码的版本（1.82.7和1.82.8），导致大量开发环境受到影响。恶意代码可窃取API密钥、云凭证、SSH密钥、数据库密码等敏感信息，并在系统中建立持久后门，甚至横向移动至Kubernetes集群。由于LiteLLM作为调用大模型服务的核心组件，每月下载量近亿次，此次攻击影响范围极广。目前受影响版本已被下架，安全专家建议所有使用过相关版本的用户立即更换凭证、审计系统访问记录并排查异常行为。

消息来源：

https://cybernews.com/security/critical-litellm-supply-chain-attack-sends-shockwaves/

**企业投保网络保险需披露AI使用情况**

随着人工智能在企业中的广泛应用，网络保险行业正发生显著变化。保险公司在承保时开始要求企业披露AI使用情况，尤其关注“影子AI”及AI系统可能带来的安全隐患，因为不透明的AI部署可能引入新漏洞，增加数据泄露或攻击风险。由于AI相关威胁难以预测，保险公司正加强审查力度，并可能据此调整保费或保障范围。专家指出，未来企业不仅需强化网络安全能力，还需对AI使用进行规范管理和审计，否则可能在投保或理赔时面临更严格限制。

消息来源：

https://cybernews.com/security/companies-reveal-ai-cyber-insurance/

**语音钓鱼攻击激增威胁企业网络**

最新研究显示，语音钓鱼正迅速成为企业网络入侵的重要手段，已上升为第二大攻击途径，约占所有入侵事件的11%。攻击者通常冒充IT人员或内部员工，通过电话诱导企业员工批准登录请求，从而绕过多重身份验证等安全措施。报告指出，随着企业对传统邮件钓鱼的防护能力提升，相关攻击占比已下降至约6%，而更具欺骗性的语音社工攻击正快速增长。专家提醒，企业需加强员工安全培训，并对异常身份验证请求保持警惕，以降低此类攻击风险。

消息来源：

https://cybernews.com/security/hackers-corporate-network-voice-phishing-surges/

**超50万Windows服务器暴露在公网**

安全研究人员发现，全球约有51万台服务器仍暴露在互联网上，运行着已停止支持的Windows IIS服务，存在严重安全隐患。由于相关软件版本已结束生命周期，不再接收任何安全补丁，这些服务器极易被攻击者利用，实施远程代码执行、数据窃取等攻击。受影响的服务器分布广泛，涉及美国及多个欧洲和亚洲国家。专家建议相关组织尽快更新或替换旧版本服务，并限制公网访问，以降低被攻击的风险。

消息来源：

https://cybernews.com/security/exposed-windows-servers-found-online/

**03.**

**热点技术**

**黑客攻击波及Checkmarx供应链**

近期黑客发起大规模供应链攻击，从早期针对Trivy扩展至Checkmarx的GitHub Actions工具。攻击者通过窃取CI/CD凭证，在多个受信任的开发工具中植入恶意代码，其中Checkmarx的ast-github-action和kics-github-action被植入凭证窃取程序，可从CI运行环境中收集GitHub及云服务等敏感信息并加密外传。此外，攻击还扩展至开发者工具生态，通过恶意OpenVSX插件检测系统内的云凭证并下载二阶段恶意载荷。此次事件已演变为跨平台、可持续扩散的供应链攻击，利用已窃取的凭证在不同项目间横向传播，可能影响上千个企业环境。专家建议开发团队审计GitHub Actions工作流、轮换所有相关密钥，并避免使用可变版本标签以降低风险。

消息来源：

https://socradar.io/blog/teampcp-checkmarx-github-actions-attack/

**无密码认证机制解析**

最新研究指出，无密码认证虽被视为替代传统密码的安全方案，但其背后机制复杂，并非绝对安全。该技术主要通过Passkey体系实现，基于公私钥加密：用户设备生成密钥对，公钥存储在服务端，私钥保存在本地或云端认证器中，登录时通过签名验证身份。以Google生态为例，系统通过云认证器同步Passkey，使用安全域密钥加密私钥，并借助OAuth令牌和加密通信协议完成跨设备登录。然而，该架构也引入新的风险，如云端组件成为攻击目标、设备同步机制可能被滥用，以及恢复流程中的PIN或凭证管理可能成为突破口。专家建议，部署时需结合设备安全、密钥管理和恢复机制设计，以提升整体安全性。

消息来源：

https://unit42.paloaltonetworks.com/passwordless-authentication/

**假应用商店骗局利用PWA传播**

一种名为“FriendlyDealer”的新型诈骗正通过“假应用商店”大规模传播。攻击者搭建伪装成Google Play或Apple App Store的网站，诱导用户安装实为渐进式网页应用的假应用。这类应用会在手机桌面生成图标且界面逼真，还能绕过系统安全限制，不触发任何安装警告。目前该诈骗已涉及1500多个恶意域名，通过广告将用户引流至假商店，最终导向不受监管的赌博网站以赚取佣金，并可能随时替换为其他诈骗内容。专家提醒，用户应避免通过不明链接安装应用，并定期检查浏览器数据和通知权限，及时删除可疑“应用”。

消息来源：

https://cybernews.com/security/fake-app-stores-deliver-scam-using-pwa/

**GlassWorm恶意软件利用区块链隐藏命令进行攻击**

研究人员发现名为GlassWorm的高级恶意软件利用Solana区块链交易的dead字段作为隐蔽的命令与控制信道，通过多阶段攻击实现入侵。该恶意软件首先借助被污染的npm、PyPI、GitHub等生态组件或项目维护者账户入侵，在系统中建立初始立足点，随后下载远程访问木马及伪装成“GoogleDocs离线版”的Chrome扩展，用于记录按键、劫持会话令牌、截取屏幕并窃取浏览器数据及加密钱包信息。在高级阶段，GlassWorm通过Solana交易中的memo字段获取C2地址，规避传统网络检测，并利用钓鱼窗口骗取硬件钱包的恢复密钥。该攻击结合区块链与供应链入侵手段，增加了防护难度。研究人员建议开发者审查依赖组件、定期更换凭据，并加强对链上恶意通信的监控。

消息来源：

https://thehackernews.com/2026/03/glassworm-malware-uses-solana-dead.html

**黑客用假简历邮件窃取企业凭据并部署加密挖矿程序**

研究人员发现名为“FAUX#ELEVATE”的网络钓鱼活动正瞄准企业用户，攻击者通过发送伪装成简历的恶意邮件，在设备上秘密安装恶意软件。邮件内嵌高度混淆的VBScript脚本，打开后迅速执行完整攻击链：获取管理员权限、禁用安全防护、窃取浏览器凭据和数据，并将敏感信息外传，同时部署门罗币挖矿程序以占用企业硬件资源获利。该攻击利用Dropbox、WordPress等合法服务托管载荷和通信，使检测更加困难，整个过程通常在几十秒内完成。由于攻击主要针对已加入域的企业机器并优先窃取企业凭据，此类钓鱼邮件对组织构成严重威胁。专家建议企业加强可疑附件防护、提升员工安全意识，并对异常登录行为进行监控。

消息来源：

https://thehackernews.com/2026/03/hackers-use-fake-resumes-to-steal.html

**04.**

**热点漏洞**

**NVIDIA NeMo Framework远程代码执行漏洞（CVE-2026-24159）**

NVIDIA NeMo Framework是一款用于构建和训练大型语言模型的AI框架，提供模型开发和部署功能。NVIDIA NeMo Framework存在远程代码执行漏洞。该漏洞产生的原因是系统未能对用户输入进行有效验证。攻击者可利用该漏洞通过本地低权限用户身份执行任意代码，导致权限提升、信息泄露和数据篡改。

影响版本：

NVIDIA NeMo Framework<2.6.2

**Vim glob函数命令注入漏洞（CVE-2026-33412）**

Vim是一款开源的命令行文本编辑器，提供glob函数用于文件名匹配和扩展功能。Vim存在glob函数命令注入漏洞。该漏洞产生的原因是程序在处理包含换行符的匹配模式时未能进行有效过滤。攻击者可利用该漏洞通过本地低权限用户身份在模式中注入换行符，在特定shell设置下执行任意shell命令，对系统造成破坏。

影响版本：

vim<9.2.0202

**oRPC OpenAPI文档存储型跨站脚本漏洞（CVE-2026-33331）**

oRPC是一款用于构建端到端类型安全且符合OpenAPI标准的API开发工具，提供OpenAPI文档生成功能。oRPC存在OpenAPI文档存储型跨站脚本漏洞。该漏洞产生的原因是程序在生成OpenAPI文档时未能对用户可控字段进行有效过滤。攻击者可利用该漏洞通过控制info.description等字段注入恶意脚本，在用户查看API文档时执行任意JavaScript代码，从而窃取敏感信息。

影响版本：

orpc<1.13.9

**HCL Traveler错误信息泄露漏洞（CVE-2026-21783）**

HCL Traveler是一款移动设备同步解决方案，提供邮件、日历和联系人同步功能。HCL Traveler存在错误信息泄露漏洞。该漏洞产生的原因是应用生成的错误消息中包含内部路径、文件名、敏感令牌、凭据、错误代码或堆栈跟踪等详细信息。攻击者可利用该漏洞通过已认证低权限用户身份获取系统架构信息，从而发动针对性攻击。

影响版本：

Traveler<14.5.1.0

**solidtime项目详情未授权访问漏洞（CVE-2026-33345）**

solidtime是一款开源时间跟踪应用，提供项目管理和权限控制功能。solidtime存在项目详情未授权访问漏洞。该漏洞产生的原因是GET /api/v1/organizations/{org}/projects/{project}端点未能应用可见性限制。攻击者可利用该漏洞通过已认证用户身份通过UUID访问组织内任意项目（包括其未加入的私有项目），导致敏感信息泄露。

影响版本：

solidtime<0.11.6

**05.**

**攻击情报**

本周部分重点攻击来源及攻击参数如下表所示，建议将以下IP加入安全设备进行持续跟踪监控。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpPoFy9DyVuticEjAk2crMNOiapjBDpKFjJK5ObcLvuSXTOhacxkeFugNPDufWLIB8eY1bZhicY4aC50qmUy1M9C1ZKb9rMz5Dgf68/640?wx_fmt=png&from=appmsg)

*请注意：以上均为监测到的情报数据，盛邦安全不做真实性判断与检测*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6oQwlp95XBm9ia9yroBLJd83wAseiabOAQoLDBAJrxjfU1KmTexS35sibxXQvt4ots9DicJoxXNiabToHw1T09Myv7Q/0?wx_fmt=png)

盛邦安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6oQwlp95XBm9ia9yroBLJd83wAseiabOAQoLDBAJrxjfU1KmTexS35sibxXQvt4ots9DicJoxXNiabToHw1T09Myv7Q/0?wx_fmt=png)

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