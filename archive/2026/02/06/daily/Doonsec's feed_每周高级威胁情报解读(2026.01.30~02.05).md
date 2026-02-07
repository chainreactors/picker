---
title: 每周高级威胁情报解读(2026.01.30~02.05)
url: https://mp.weixin.qq.com/s/I57-AHmKS6SXldu-_XIJ6Q
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:05:01.602742
---

# 每周高级威胁情报解读(2026.01.30~02.05)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/odcL3w4qOq8ib6Hl1KhgglaPNyDwlX6Cww2NHtjN33AlRP0ZWVQqfyOtOM5tiaibV37JsCJSYV1CSFQh04diaZC2Miao4bH3DQoubpV574JaP1eY/0?wx_fmt=jpeg)

# 每周高级威胁情报解读(2026.01.30~02.05)

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器中沉浸阅读

2026.01.30~02.05

**攻击团伙情报**

* 深入分析APT42组织的PowerShell后门程序TAMECAT
* 追踪 Lazarus 更先进的 OtterCookie 恶意软件
* APT28 利用 CVE-2026-21509 和云 C2 基础设施发起多阶段攻击活动
* Lazarus 利用 Teams 会议进行 macOS 凭证窃取
* LABYRINTH CHOLLIMA 已经演变为三个不同的行动小组
* 波兰电力部门攻击事件背后的攻击归因

**攻击行动或事件情报**

* 深入分析Notepad++供应链攻击
* Rublevka Team团伙专门从事大规模加密货币盗窃
* RedKitten：利用人工智能加速针对伊朗抗议活动的行动
* 自称Punishing Owl的威胁组织入侵俄罗斯政府安全机构网络
* 针对 eScan 防病毒软件的供应链攻击
* ShinyHunters 组织勒索活动正在扩张

**恶意代码情报**

* Aisuru僵尸网络以31.4 Tbps的DDoS攻击创下新纪录
* 攻击者利用虚假约会应用作为诱饵针对巴基斯坦进行间谍活动
* 新型多阶段恶意软件攻击活动传播Pulsar RAT
* 黑客利用最新React Native CLI漏洞部署Rust木马
* 深入分析与“CyberAv3ngers”有关的进攻性OT框架

**漏洞情报**

* 面向互联网的 AI 代理网关中的 CVE-2026-25253
* CISA将SolarWinds、FreePBX和GitLab漏洞加入KEV目录

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq9SbXWnBqVfOIgaibf69cY6gzzMC6IlaKeYOxpMNccicvDpnfq6YCVh8belwoIqLBpodfXlICJYePaYPfzqgFqYzt2c8GzpwUBpI/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqibCl1kLZSH0TAjkrRGM8PbbiaDj4rPhaUJLib3aJoFCe43mdia0yMSGvll7794NekamqQcern1vaIx4mViafc2yDEwUxVU1MhtgyI4/640?wx_fmt=gif&from=appmsg)

**攻击团伙情报**

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq82H528AmRbeCLoI2CyLWSss4ZfJIjY7ECibM0bW7B5LuxfFrw1rUtNT3BzvltUhd2tujbXz6YOYDPJmIicszbNK1uPUw3dNyFqM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqib7oBLeW2Z6H9Fex47icMFSQ4doMMiaKz4jFrmFCx4Asw4y4UsYKNuf7Xt6QAgLp85eM2m0lUiaemyHXyM1ianm4u3JPOa06gHwSxc/640?wx_fmt=gif&from=appmsg)

**01**

**深入分析APT42组织的PowerShell后门程序TAMECAT**

**披露时间：**2026年1月29日

**情报来源：**https://blog.pulsedive.com/tamecat-analysis-of-an-iranian-powershell-based-backdoor/

**相关信息：**

TAMECAT是一种由伊朗国家支持的APT42组织使用的PowerShell恶意软件，主要用于间谍活动。该恶意软件通过VBScript脚本下载第一阶段代码，该脚本会检查系统上运行的杀毒软件，并根据检测结果选择使用PowerShell或cmd.exe来下载第二阶段代码。TAMECAT能够通过AES加密和解密数据，并通过Telegram机器人接收指令以下载额外的脚本。它还能够从Microsoft Edge中提取数据、截取屏幕截图以及从Chrome中收集数据。研究人员发现，TAMECAT的命令和控制（C2）服务器使用Web协议进行通信，并通过加密通道传输数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOq89XoZCC7rqnkUJ6EGEGeWpbUQkofdyyRCT847s2ExToBd857NI3gBiaq1gfsvkvvKpHweZiciaibtvjtNzABSYtG6ZrVicSSQc93X4/640?wx_fmt=png&from=appmsg)

**02**

**追踪 Lazarus 更先进的 OtterCookie 恶意软件**

**披露时间：**2026年2月1日

**情报来源：**https://redasgard.com/blog/hunting-lazarus-part3-infrastructure-too-perfect

**相关信息：**

Red Asgard 团队在追踪 Lazarus 组织“传染性面试”活动过程中，发现了更高级的恶意软件家族OtterCookie，其具备键盘记录、多屏截图、持久化机制和针对27个钱包扩展的窃取能力，并映射出约20个具有标准化端口配置（如1244、5918）的C2服务器；然而，在尝试利用11类漏洞攻击该基础设施全部失败后，结合暴露的私钥、无条件接受上传等六个异常指标，研究人员以70%的置信度评估该基础设施可能是一个精心设计的蜜罐或反情报陷阱，而非真实的Lazarus运营平台，这引发了关于攻击者与防御者之间侦查与反侦查的复杂博弈的深刻疑问。

**03**

**APT28 利用 CVE-2026-21509 和云 C2 基础设施发起多阶段攻击活动**

**披露时间：**2026年2月4日

**情报来源：**https://www.trellix.com/blogs/research/apt28-stealthy-campaign-leveraging-cve-2026-21509-cloud-c2/

**相关信息：**

APT28（又称Fancy Bear）近期发起了一项针对欧洲多国军事、政府及海事运输机构的复杂网络间谍活动，利用新公开的Microsoft Office漏洞CVE‑2026‑21509在24小时内制作钓鱼文档，通过多阶段感染链投放包括NotDoor Outlook后门和BeardShell植入物在内的恶意载荷，并滥用合法云存储服务filen.io作为隐蔽的命令与控制基础设施，以高度混淆和内存执行技术规避检测，持续窃取敏感信息。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqic4xaiaxyFz888bQW1c6w8aSXpFvh1Zqav2oS5UdKyicDt1JzEUTKbqkF10pqyVQiag7X7KaiaqIp6aHppiay6tsmxFiaNme9M3ECclg/640?wx_fmt=png&from=appmsg)

**04**

**Lazarus 利用 Teams 会议进行 macOS 凭证窃取**

**披露时间：**2026年2月2日

**情报来源：**https://daylight.ai/blog/prospect-call-microsoft-teams-meetings

**相关信息：**

Daylight Security调查了一起与朝鲜Lazarus Group下属的BlueNoroff组织相关的针对性社会工程学攻击事件。攻击者通过Telegram联系受害者，伪装成潜在客户或合作伙伴，并迅速将互动升级到Microsoft Teams会议。在会议中，攻击者以音频问题为借口，指导受害者运行终端命令，下载并执行恶意二进制文件。攻击者利用macOS的本地工具（如curl、chmod、codesign和nohup）进行“利用本地资源”的攻击，窃取用户的Keychain数据库中的凭据，并将数据打包准备外泄。从威胁情报角度看，此次攻击与BlueNoroff的GhostCall活动模式一致，该模式通过即时通讯平台将受害者引入会议陷阱，实现实时命令执行和macOS及Windows上的凭据盗窃。

**05**

**LABYRINTH CHOLLIMA 已经演变为三个不同的行动小组**

**披露时间：**2026年1月29日

**情报来源：**https://www.crowdstrike.com/en-us/blog/labyrinth-chollima-evolves-into-three-adversaries/

**相关信息：**

LABYRINTH CHOLLIMA是CrowdStrike Intelligence追踪的最活跃的朝鲜背景黑客组织之一，负责朝鲜一些最著名的入侵事件，包括对韩国和美国实体的破坏性攻击以及全球WannaCry勒索软件事件。自2018年以来，该组织分化为三个高度专业化的子团体：GOLDEN CHOLLIMA、PRESSURE CHOLLIMA和核心LABYRINTH CHOLLIMA。GOLDEN CHOLLIMA主要针对经济发达地区，特别是加密货币和金融科技领域；PRESSURE CHOLLIMA则专注于高价值的加密货币盗窃，是朝鲜技术最先进的对手之一；核心LABYRINTH CHOLLIMA则继续专注于间谍活动，目标是工业、物流和国防公司。尽管这些团体独立运作，但它们共享工具和基础设施，表明朝鲜网络生态系统内的集中协调。这种分化增强了朝鲜政权同时追求多个目标的能力，尤其是在国际制裁继续削弱朝鲜经济的情况下，GOLDEN CHOLLIMA和PRESSURE CHOLLIMA的金融动机可能会进一步加剧。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq8q7v2s5nma7WDClQSeu6QLXxnUs0QnC2YwBJj00PLmy2FDoYtxtBWZsiaw7voWRFkGjUiaPfVcK47n3nbnXpjyvzDOdzibz5xD0w/640?wx_fmt=png&from=appmsg)

**06**

**波兰电力部门攻击事件背后的攻击归因**

**披露时间：**2026年1月31日

**情报来源：**https://pylos.co/2026/01/31/attributive-questions-in-high-profile-incidents/

**相关信息：**

2025年12月，波兰电力部门遭受攻击，导致部分电网中断。事件发生后，ESET和Dragos等机构将攻击归因于俄罗斯军事情报机构（GRU）旗下的Sandworm组织，而波兰计算机应急响应小组（CERT.PL）则认为攻击与俄罗斯联邦安全局（FSB）旗下的Berserk Bear组织有关。文章分析了这种归因差异的原因，指出不同机构的数据来源和分析方法导致了不同的结论。ESET的分析基于恶意软件DynoWiper的技术关联，Dragos的分析侧重于行为模式与过去事件的相似性，而CERT.PL则通过网络基础设施追踪得出结论。文章强调，现代网络攻击的复杂性使得单一实体归因变得困难，攻击可能涉及多个行为者或组织的协作。此外，情报偏见和数据来源的局限性也会影响归因的准确性。最终，文章指出，归因分析的目的是为了更好地理解攻击方式，以便采取有效的防御措施，而不仅仅是确定攻击者身份。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq889Hiamaw5Dk2mR0qyuV0hMzKvgjiagr2ZeHUx9ntFkCtfVxxoq5Cou1XZoCGCvoJicuZM0DWTSoMWRz2EYumbmIsR1lCm2uAt14/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqibZeDD6GLdPsktxrQHhmp4BaprDmibIb77FvgAElr2EbicTr5bwIluricnVMEYBDlwVauDZQqxOh4D2GKsxzoxqQNleJXEEzS58lQ/640?wx_fmt=gif&from=appmsg)

**攻击行动或事件情报**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqibUdC8eOmicIPlHEiaRkE2ekpxkVAP3hJfocaPcDXAukyavWS9mTVbsc3gpib2n1icIcq2icu5J0AWZlibbozibdhRmhN3F6Nk1SlAACM/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqibWTpJ3LkjZOkT6XgcotbA9ZoDBPQ4oJdb6LwBd3PxDvN8ksqofW8ULb6cNqRqpR0ZmWUcJrOfTzw0QHSkZPoKlHJ6Wk3GSwCE/640?wx_fmt=gif&from=appmsg)

**01**

**深入分析Notepad++供应链攻击**

**披露时间：**2026年2月3日

**情报来源：**https://securelist.com/notepad-supply-chain-attack/118708/

**相关信息：**

研究人员详细分析了 2025 年 6 月至 12 月期间 Notepad++ 更新基础设施被攻击者利用的事件。攻击者通过控制 Notepad++ 的更新服务器，向目标用户推送恶意更新，这些更新包含了多种复杂的执行链和恶意载荷。研究人员发现了三种不同的感染链，分别针对越南、萨尔瓦多、澳大利亚、菲律宾、萨尔瓦多和越南的个人和组织。这些感染链涉及多个阶段的恶意软件下载和执行，包括利用 Metasploit 下载器传播 Cobalt Strike Beacon 以及利用 ProShow 软件的漏洞执行恶意代码。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqic0HVgibiaicicsvjwOclxGCeTEjrw4dzjjCg0VkdMw1nZIzoo7jC7WbcHlxzu5TaC8Ml5Lc6jmgwicCSiaiaoRnXb3w8XmtLIjvibGIcQ/640?wx_fmt=png&from=appmsg)

**02**

**Rublevka Team团伙专门从事大规模加密货币盗窃**

**披露时间：**2026年2月4日

**情报来源：**https://www.recordedfuture.com/research/rublevka-team-anatomy-russian-crypto-drainer-operation

**相关信息：**

Rublevka Team是一个自2023年起活跃的俄罗斯大型加密货币盗窃组织，通过高度自动化的联盟计划，利用仿冒合法加密服务（如Phantom、Bitget等）的钓鱼页面，诱骗用户连接Solana钱包并授权恶意交易，已盗取超过1000万美元。该组织提供Telegram机器人、登录页面生成器、隐蔽技术和自动化分发基础设施，降低犯罪门槛，吸引全球联盟成员参与，其滥用云端RPC API、频繁更换域名并利用Cloudflare隐藏基础设施，呈现出服务化、规模化的网络犯罪趋势，对加密货币平台和用户构成严重威胁。

**03**

**RedKitten：利用人工智能加速针对伊朗抗议活动的行动**

**披露时间：**2026年1月29日

**情报来源：**https://harfanglab.io/insidethelab/redkitten-ai-accelerated-campaign-targeting-iranian-protests/

**相关信息：**

RedKitten是一个新发现的恶意软件活动，首次观察到的时间是2026年1月，目标包括记录伊朗人权侵犯的非政府组织和个人。该活动利用AI工具快速构建，使用GitHub作为配置和模块加载的死信投递解析器（DDR），Google Drive用于存储恶意软件模块，Telegram用于命令和控制（C2）。攻击链从带有恶意宏的Excel电子表格（XLSM）开始，这些电子表格伪装成记录伊朗抗议活动中死亡人员的文件。一旦宏被启用，它们会下载并执行一个C#植入程序，称为SloppyMIO。SloppyMIO通过从图像中提取配置信息来获取Telegram机器人令牌和模块URL，这些图像通过GitHub Gist提供。该恶意软件可以执行多种模块，包括命令执行、文件收集和进一步恶意软件部署。

**04**

**自称Punishing Owl的威胁组织入侵俄罗斯政府安全机构网络**

**披露时间：**2026年1月29日

**情报来源：**https://habr.com/ru/companies/pt/articles/990374/

**相关信息：**

2025年12月12日，一个名为Punishing Owl的新兴黑客组织对俄罗斯的关键信息基础设施发起攻击。该组织声称入侵了俄罗斯某国家机构的网络，并在社交媒体上公布了内部文件的链接，同时在Mega.nz上存储了这些文件。攻击者还篡改了目标机构的DNS配置，创建了一个子域名hacked.[REDACTED].ru，并设置了伪造的TLS证书和邮件服务。随后，该组织向目标机构的合作伙伴发送了钓鱼邮件，声称网络已被入侵，并附带了指向其DLS网站的链接。此外，攻击者还利用被入侵的邮箱发送带有恶意ZIP文件的邮件，ZIP文件内包含伪装成PDF的LNK文件，打开后会下载并执行PowerShell恶意脚本ZipWhisper，用于窃取浏览器数据并上传到C2服务器。Punishing Owl的攻击具有明显的政治动机，其目标均为俄罗斯的关键信息基础设施。

**05**

**针对 eScan 防病毒软件的供应链攻击**

**披露时间：*...