---
title: 法国电信巨头遭黑客入侵，近2000万用户数据现身暗网；AI安全新挑战：研究揭示ChatGPT可被十六进制代码操纵 | 牛览
url: https://mp.weixin.qq.com/s?__biz=MjM5Njc3NjM4MA==&mid=2651133097&idx=2&sn=cca0451e844d60257068b7d3956ff4f5&chksm=bd15a47a8a622d6c19c3f268aa6cc085438c857abd3bf18d05bcabc818b8625bd891395b44ab&scene=58&subscene=0#rd
source: 安全牛
date: 2024-10-31
fetch_date: 2025-10-06T18:54:04.612088
---

# 法国电信巨头遭黑客入侵，近2000万用户数据现身暗网；AI安全新挑战：研究揭示ChatGPT可被十六进制代码操纵 | 牛览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kuIKKC9tNkBNcT49K4SwZbl3eqC5Fq88yKycIEL3FdeINeO7py04ANSThuEyS4nQPVQnGkIKZ75jA01H0IfLYg/0?wx_fmt=jpeg)

# 法国电信巨头遭黑客入侵，近2000万用户数据现身暗网；AI安全新挑战：研究揭示ChatGPT可被十六进制代码操纵 | 牛览

安全牛

点击蓝字·关注我们 / aqniu

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkBjwIRcuxcIx3fvDBydiaqkxw4o55dLPMJBKVsRbYl7ULkJDmFtatY9fWSIcZttiaeQm76cm0TXSBCA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**新闻速览**

•国际联合执法行动重大突破：Redline和Meta信息窃取工具被瓦解

•AI安全新挑战：研究揭示ChatGPT可被十六进制代码操纵

•雷军首次回应AI语音被恶搞：让自己很困扰！

•法国电信巨头遭黑客入侵，近2000万用户数据现身暗网

•RansomHub勒索软件盯上墨西哥航空业，OMA成为最新受害者

•警惕！Black  Basta勒索软件利用微软Teams平台发起新型钓鱼攻击

•Akira与Fog勒索软件团伙联手攻击SonicWall VPN，10小时内就可以完成入侵

•NVIDIA发布关键安全更新，修复GPU驱动程序中的多个高风险漏洞

•Realtek  SD卡读卡器驱动严重安全缺陷曝光，或威胁数百万笔记本电脑

**热点观察**

**国际联合执法行动重大突破：Redline和Meta信息窃取工具被瓦解**

近日，荷兰国家警察联合多国执法机构共同发起"马格努斯行动"，成功破坏了两款知名信息窃取工具Redline和Meta的运营，并获取了大量关键数据。

Redline和Meta是两款应用广泛的MaaS模式信息窃取工具，能够窃取包括操作系统信息、浏览器凭证、信用卡数据、加密货币钱包凭证，以及各类应用程序账户信息等敏感数据。Redline自2020年问世以来迅速成为最受欢迎的信息窃取工具之一，而Meta则于2022年进入暗网市场，主要针对macOS用户和企业。

执法部门表示已完全控制Redline和Meta的所有服务器，获取了包括源代码、许可证服务器、REST API服务器、控制面板、窃取工具和Telegram机器人在内的全部关键组件。更重要的是，他们还收集了两款工具用户（含VIP用户）的详细信息，包括用户名、密码、IP地址、时间戳和注册日期等。

虽然目前执法部门尚未公布与此次行动相关的逮捕信息或被识别的客户名单，但表示"相关方将被通知，法律行动正在展开"。这可能借鉴了此前由英国国家犯罪调查局（NCA）主导的Cronos行动的策略，采用了渐进式的信息公布方式。

原文链接：

https://www.helpnetsecurity.com/2024/10/28/police-hacks-disrupts-redline-meta-infostealer-operations/

**AI安全新挑战：研究揭示ChatGPT可被十六进制代码操纵**

近日，Mozilla的生成式人工智能（GenAI）漏洞奖励计划经理Marco Figueroa发现了一种新的提示注入技术，可能允许恶意用户绕过OpenAI最先进的语言模型GPT-4o的安全防护。这一发现引发了对大型语言模型（LLMs）安全性的广泛关注。

Figueroa通过一项实验展示了这一漏洞。他尝试让ChatGPT为CVE-2024-41110（一个针对Docker授权插件的严重漏洞）编写漏洞利用代码。通常情况下，ChatGPT会拒绝执行这种存在潜在危险的操作。然而，Figueroa通过将恶意指令编码为十六进制格式，成功绕过了GPT-4o的内容过滤机制。

具体来说，Figueroa将指令转换为一串由数字和字母A到F组成的十六进制代码，并提供了相应的解码指令。GPT-4o接收并执行了这些指令，最终生成了一个可用的漏洞利用代码。更令人担忧的是，ChatGPT甚至试图自行执行这段代码，尽管Figueroa并未明确要求这样做。

这一漏洞暴露了LLMs在处理复杂指令时的一个关键缺陷：它们往往只能逐步执行指令，缺乏对整体上下文的深入理解。GPT-4o分析每个单独的输入步骤，但未能评估所有步骤组合后可能产生的潜在危险结果。Figueroa指出，相比于其他AI公司，如Anthropic，OpenAI在开发GPT-4o时似乎更注重创新而非安全性。

原文链接：

https://www.darkreading.com/application-security/chatgpt-manipulated-hex-code

**雷军首次回应AI语音被恶搞：让自己很困扰！**

10月29日，小米CEO雷军通过视频首次回应雷军AI配音恶搞事件。雷军称，最近两年AI特别火，技术进步特别快，前段时间在刷视频的时候经常看到很多人在玩“雷军AI”，也就是“雷军语音包”。雷军表示：“的确让自己也挺困扰，也挺不舒服的，在这里希望大家不要再玩了，这个事情不太好。不过还是觉得AI是很好的技术，也非常实用。”

根据相关法律法规的规定，任何组织或个人未经声音权人同意，不得擅自使用、公开或侵害其声音权益。

原文链接：

https://mp.weixin.qq.com/s/QFMsAES8tbTjIlUr2313kw

**网络攻击**

**法国电信巨头遭黑客入侵，近2000万用户数据现身暗网**

日前，法国第二大电信运营商Free遭遇严重网络攻击，大量用户个人信息疑似泄露。该公司目前拥有超过2290万移动和固定电话用户，在法国互联网服务市场占据重要地位。

Free公司10月26日向法新社确认，黑客成功入侵了公司的内部管理工具，导致部分用户账户相关的个人数据被未经授权访问。虽然公司声称密码、银行卡信息以及通信内容未受影响，但泄露的信息仍然包括了姓名、电话号码、完整邮寄地址、出生日期和电子邮件等敏感数据。

更令人担忧的是，黑客已经在一个知名的网络犯罪论坛上试图出售这些被盗数据。论坛上的信息显示，有两个待售数据库，一个包含近1920万个客户账户信息，另一个包括511万个IBAN（国际银行账号）详细信息。

Free公司表示目前尚未观察到其业务和服务运营受到影响，公司已经采取了一系列紧急应对措施，包括向有关部门提交刑事投诉，并通知了相关监管机构。

原文链接：

https://securityaffairs.com/170333/data-breach/free-suffered-a-cyber-attack.html

**RansomHub勒索软件盯上墨西哥航空业，OMA成为最新受害者**

墨西哥中北部机场集团（OMA）近日遭到RansomHub勒索软件组织攻击，引发网络安全界高度关注。OMA作为墨西哥重要的机场运营商，负责管理该国十多个机场，此次事件可能对墨西哥航空业造成重大影响。

据新闻网站The Record报道，RansomHub组织声称已成功入侵OMA的内部系统，并威胁称如果OMA拒绝支付赎金，将公开3TB的敏感数据，数据量之大暗示了此次攻击的严重程度和潜在影响。

面对这一威胁，OMA目前还未直接确认RansomHub的入侵声明，但公司表示正与网络安全专家密切合作，以保护系统完整性并进行全面调查。同时，公司表示已启动备份系统，以确保北部和中部机场的正常运营。OMA强调，目前尚未发现此次事件对公司运营和财务状况造成重大不利影响，但正密切监控局势并评估可能的持续影响。

原文链接：

https://www.scworld.com/brief/mexican-airport-operator-purportedly-breached-by-ransomhub

**警惕！Black Basta勒索软件利用微软Teams平台发起新型钓鱼攻击**

据BleepingComputer报道，臭名昭著的Black Basta勒索软件团伙近期出现了新变化，将目标瞄准了广泛使用的微软Teams企业协作平台。新型攻击的整个过程巧妙而复杂。

攻击始于向目标发送恶意邮件，随后攻击者会假冒企业IT帮助台人员，通过Teams与受害者取得联系。他们声称可以帮助解决邮件垃圾问题，以此赢得受害者的信任。为了增加可信度，攻击者甚至在其Teams显示名称中巧妙地加入了"Help Desk"字样。一旦建立联系，攻击者就会诱导受害者下载AnyDesk远程访问软件或打开Windows Quick Assist工具。这些看似无害的操作实际上为攻击者部署恶意软件打开了大门。研究人员发现，攻击者会尝试部署多个恶意载荷。更令人担忧的是，攻击并未就此停止，攻击者随后会在受害者机器上安装Cobalt Strike。这是一款强大的渗透测试工具，可用于进一步的网络入侵和横向移动。

为应对这种新型威胁，安全专家建议企业应当严格限制Teams的通讯功能，特别是来自外部的未经验证的联系。同时，加强员工对社交工程攻击的认识和培训。此外，企业还应该加强对远程访问工具如AnyDesk的管控，实施严格的安装和使用政策。

原文链接：

https://www.scworld.com/brief/microsoft-teams-exploited-in-latest-black-basta-attacks

**Akira与Fog勒索软件团伙联手攻击SonicWall VPN，10小时内就可以完成入侵**

自今年8月以来，全球多个行业遭遇了一波针对SonicWall SSL VPN账户的大规模攻击，其中涉及两个臭名昭著的勒索软件团伙：Akira和Fog。据BleepingComputer报道，这些攻击利用了SonicWall SSL VPN访问控制中的一个关键漏洞（CVE-2024-40766），至少造成了30起入侵事件，其中大部分由Akira团伙发起。

此类攻击的特点在于其高效性和精准性。从初次入侵到数据加密，平均只需不到10小时。攻击者主要通过VPN/VPS进行终端访问，显示出他们对目标网络结构的深入了解。值得注意的是，大多数攻击都使用相同的基础设施，这一细节暗示Akira和Fog两个团伙可能存在某种程度的合作关系。这种合作模式并非首次出现，此前他们就曾联手利用Veeam备份系统的漏洞发起攻击。

网络安全公司Arctic Wolf的分析发现，受影响的SSL VPN账户普遍缺乏多因素身份认证（MFA）保护。这一安全缺陷为攻击者提供了可乘之机，凸显了在当前复杂的网络安全环境中实施强有力的身份验证机制的重要性。攻击者的主要目标是虚拟机和备份系统，通过快速加密这些关键系统最大化攻击的破坏性和勒索的成功率。

原文链接：

https://www.scworld.com/brief/sonicwall-ssl-vpn-accounts-targeted-by-akira-fog-ransomware-gangs

**漏洞预警**

**NVIDIA发布关键安全更新，修复GPU驱动程序中的多个高风险漏洞**

NVIDIA近日发布了针对其GPU显示驱动程序的重要安全更新，修复了多个高风险漏洞。这些漏洞可能导致远程代码执行、权限提升等严重安全风险，影响Windows和Linux系统。

其中最严重的CVE-2024-0126漏洞影响Windows和Linux系统上的NVIDIA GPU显示驱动程序，允许特权用户提升权限，可能导致代码执行、拒绝服务、信息泄露和数据篡改。另外，CVE-2024-0117至CVE-2024-0121这五个漏洞存在于Windows驱动程序版本的用户模式层，允许非特权用户导致越界读取，可能造成与CVE-2024-0126类似的影响。

NVIDIA已针对不同操作系统和驱动程序分支发布了相应的更新版本。对于Windows系统和Linux系统，GeForce、NVIDIA RTX、Quadro、NVS和Tesla系列产品的多个驱动程序分支都发布了更新。NVIDIA建议所有用户尽快应用这些安全更新，以保护系统免受潜在攻击。

原文链接：

https://cybersecuritynews.com/nvidia-gpu-display-driver-vulnerabilities/

**Realtek SD卡读卡器驱动严重安全缺陷曝光，或威胁数百万笔记本电脑**

近日，安全研究人员发现Realtek的SD卡读卡器驱动程序RtsPer.sys中存在多个严重安全缺陷，影响范围涉及戴尔、联想、惠普和微星等多家知名笔记本电脑制造商。这些漏洞有些已潜伏多年，可能被攻击者利用来泄露内存数据、写入任意内核地址，甚至从用户模式访问物理内存。

研究人员共发现7个安全缺陷，其中最为严重的缺陷可能让攻击者对内核内存进行任意写入。受影响的SD卡读卡器型号包括RTS5227、RTS5228、RTS522A、RTS5249、RTS524A、RTS5250、RTS525A、RTS5287、RTS5260、RTS5261和RTS5264。

这些安全缺陷的根源在于驱动程序存在多种问题，包括对SCSI命令的处理不当、输入验证不足，以及内存操作检查不充分。尽管Realtek已经发布了修复补丁，但研究人员指出，该公司对安全缺陷的响应逐渐变得"缓慢且不情愿"。

原文链接：

https://cybersecuritynews.com/realtek-driver-flaws-impact-laptops/

![](https://mmbiz.qpic.cn/mmbiz_png/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMnicXSRCtG4URyLibbqPegjnnibfRB0z4zIzwghbLOkV5fqGYM8vhuQdqw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

合作电话：18311333376

合作微信：aqniu001

投稿邮箱：editor@aqniu.com

![](https://mmbiz.qpic.cn/mmbiz_gif/kuIKKC9tNkAfZibz9TQ8KWj4voxxxNSGMAGiauAWicdDiaVl8fUJYtSgichibSzDUJvsic9HUfC38aPH9ia3sopypYW8ew/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

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