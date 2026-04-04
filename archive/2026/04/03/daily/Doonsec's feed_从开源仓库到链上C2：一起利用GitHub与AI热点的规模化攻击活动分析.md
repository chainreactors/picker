---
title: 从开源仓库到链上C2：一起利用GitHub与AI热点的规模化攻击活动分析
url: https://mp.weixin.qq.com/s/04ZOdzOawFnQmaCPV04xfg
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:13:57.164837
---

# 从开源仓库到链上C2：一起利用GitHub与AI热点的规模化攻击活动分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/d1YpVG2tPVohTzXe6SSbkGPYnj4picDb2vhdR4xdLcrwUmXagbibToZk0BOhiaVHmLsvea12o5L5cibQeAG58CL6ynbP3cEgwZI2PiaRclDScNAU/0?wx_fmt=jpeg)

# 从开源仓库到链上C2：一起利用GitHub与AI热点的规模化攻击活动分析

启明星辰
启明星辰

ADLab

![]()

在小说阅读器中沉浸阅读

更多安全资讯和分析文章请关注启明星辰ADLab微信公众号及官方网站（adlab.venustech.com.cn）

**第一章**

概 述

近期，启明星辰ADLab研究团队在威胁狩猎中发现一批利用GitHub平台进行大规模恶意文件分发的攻击活动。攻击者大规模滥用代码托管平台GitHub，通过伪装热门仓库投放恶意压缩包，并结合搜索引擎优化与热点话题引流，实现对目标用户的高效诱导与投递。为了防止该攻击持续扩散，我们就这批攻击进行公开分析和披露。初期，这些样本表现为零散分布的恶意仓库与压缩包文件，整体规模有限，难以形成有效关联；但随着对样本相似性、传播路径及账号行为的持续跟踪分析，我们逐步发现，这些看似独立的攻击事件背后，实际上共享相似的投递方式、命名策略及基础设施特征，呈现出明显的同源性。进一步关联分析表明，这并非零散攻击，而是一套持续运营的攻击体系。

在诱导策略方面，攻击者紧跟当下AI生态爆发趋势，大量使用“Claude”、“DeepSeek”、“Gemini”、“Qwen”等主流大模型进行攻击载体伪装，样本中还频繁出现了“OpenClaw”、“Skill”、“Agent”等与当前AI Agent生态密切相关的关键词，反映出AI生态正逐渐演变为新一代恶意软件投放的重要载体。攻击者大量使用大模型工具链、自动化框架及相关关键词进行包装，并结合版本号、测试标签及功能描述增强可信度。同时，其诱饵类型覆盖游戏外挂、软件工具、破解资源以及AI相关应用等多个高需求场景，体现出“热点驱动 + 多场景覆盖”的投放策略，使攻击既具备广泛传播能力，又能够在特定人群中实现较高转化率。

从攻击链结构来看，该活动已形成较为完整的技术路径：在投递阶段，攻击者通过批量注册GitHub账号并构建伪装仓库，实现分布式仓库托管与动态更新策略，结合搜索引擎优化与技术热点引流吸引用户下载；在执行阶段，通过多阶段加载机制，将核心恶意逻辑隐藏于加密与混淆的后续payload中，并以内存方式运行，从而规避传统检测；更关键的是，在控制阶段，我们发现攻击者创新性地利用了Polygon区块链基础设施进行C2服务器地址的间接传递，恶意程序通过调用链上智能合约动态获取C2地址，实现间接通信与控制。该C2分发和传递技术，使得传统的流量监测和溯源变得更加困难，构成了当前网络安全领域的新挑战。

从时间演进来看，该攻击活动自去年3月开始出现，在早期阶段以小规模试探性投放为主，随着攻击者不断扩展账号资源与分发能力，其投递规模逐步增长，并在今年3月达到阶段性高峰，单月新增恶意样本数量突破1000个。整体来看，该活动呈现出由“零散试探”向“规模化运营”演进的趋势。同时，通过样本与基础设施关联，我们累计收集并去重得到2700余个恶意压缩包，关联数十个C2节点及大量GitHub账号，这些数据进一步印证了该攻击活动背后的黑客组织具备较强的组织化与自动化能力，其甚至可能将整个攻击周期都进行了自动化。

总体来看，该攻击活动已经从简单的恶意样本投递，演变为一套围绕开源平台构建、持续运营并不断扩展的攻击体系，其在规模、技术与策略层面均表现出较高成熟度。这一现象表明，攻击者正在加速利用技术生态本身作为攻击载体。基于上述发现，本文将从攻击手法、目标特征、基础设施及典型案例等方面，对该攻击活动进行系统分析，以还原其整体运作模式并评估其安全影响。

**第二章**

攻击活动分析

### 2.1  攻击手法分析

从整体攻击链来看，该攻击活动采用了典型的多阶段加载（Staged Payload）+ 合法平台滥用的组合手法。攻击者利用GitHub平台的天然可信性，通过社会工程学手段进行攻击。攻击者首先注册大量GitHub账户，通过fork正常项目伪装成正常仓库，并在README文件中添加恶意下载链接，下载链接指向攻击者在仓库中投放的经过精心命名伪装的压缩包文件，攻击者再结合搜索引擎优化或社交媒体传播等方式来吸引目标用户访问这些恶意仓库，下载并执行恶意程序。

值得注意的是，在投递阶段攻击者明显利用了当前AI工具爆发式增长的热点趋势进行诱导传播。尤其是近期围绕OpenClaw生态的广泛传播和“全民安装”现象，使其成为极具吸引力的攻击载体。大量压缩包名称直接使用主流大模型或AI工具相关关键词，例如：openclaw-awesome-skills-1.6.zip、
docker-openclaw-v3.8.zip、gemini3-starter-prompts\_1.9-beta.1.zip和DeepSeek-Pentest-AI.zip以及qwen3\_computer\_use-v1.8.zip。此类命名紧跟当前AI生态中诸如大模型工具链、Prompt工程、自动化代理（Agent）等热门方向，对开发者、安全研究人员及AI从业者具有较强吸引力。此外攻击者还使用了看似正规的软件版本号格式（如1.6.zip、v3.8.zip等）并添加alpha、beta等标识来增加可信度，并同时在攻击载体中包含"Crack"、"watermark\_Doubao\_remove"等诱人关键词，以吸引特定需求的用户主动下载。我们发现这些恶意仓库在GitHub高热度话题如“#prompt-builder”、“#ai-tools”排名中靠前（如图1所示），这更增加了恶意压缩包文件被下载和执行的概率。

![](https://mmbiz.qpic.cn/mmbiz_png/d1YpVG2tPVrORIHczuDLp08QVW6JRF7iaCgWib8V6ICP3BdYEAabaIJiay15dibv5VLC5pwqibTeQLUmtbhPpStpPhd2C7nnpVaiba94VJDick4zt8/640?wx_fmt=png&from=appmsg)

图1 利用GitHub高热度话题传播恶意压缩包

压缩包内部通常包含可执行文件或脚本组件作为第一阶段Loader使用。该Loader在运行后不会直接释放明显的恶意行为，而是在获取C2下发的第二阶段payload地址后，主动连接GitHub上的远程地址，获取第二阶段payload。在第二阶段中，攻击者进一步增强隐蔽性：payload以txt、html、css、js、json等看似正常的文件形式存在，实际内容经过加密与深度混淆处理。Loader在本地对其进行解密后，再以内存加载或反射执行的方式运行，从而规避安全软件的查杀。这种“下载—解密—内存执行”的链路，使得传统基于特征码的检测手段难以生效。

另外，攻击者通过批量GitHub账号分散托管不同阶段的恶意资源，形成去中心化分发体系。一旦部分仓库或账号被封禁，其余节点仍可继续提供payload，有效提升了攻击基础设施的抗打击能力。结合GitHub本身的高信誉属性，该攻击在传播阶段能够绕过部分网络安全策略，实现较高的投递成功率与隐蔽性。

### 2.2  攻击目标分析

我们将该攻击活动在GitHub上发布的多个伪装样本及对应伪装软件类型进行了整理，如表1所示。表中列出了攻击者在第一阶段投放的典型压缩包样本，并按照其伪装内容划分为不同类别。从样本命名特征来看，攻击者采用了高度策略化的命名方式，文件命名具有明显的“诱导下载”特征，伪装目标直接对应用户高频需求或敏感兴趣领域，使用如游戏外挂、破解软件、AI工具以及加密货币套利等多种热门主题进行伪装，覆盖不同用户群体。同时，大量使用“AI”、“Free”、“Premium”等高吸引力关键词，并结合版本号、Beta标识及知名软件名称，以提升样本在搜索引擎及GitHub平台中的曝光率与可信度。此外，部分样本通过关键词堆叠实现类似SEO优化效果，以扩大检索命中范围，并辅以随机命名及正常工具类名称混淆检测，从而增强整体投放的隐蔽性。整体来看，该类命名策略兼具诱导性、传播性，体现出明显的批量化投放及黑产运营特征。

|  |  |
| --- | --- |
| **样本** | **伪装软件类型** |
| CS2.External.Cheat.v1.6.9.zip  Apex.Legends.VisualX.Aimbot.ESP.Multi.v3.7.6.zip  Battlefield1-AutoAimToolkit.zip  DeadByDaylight-Hack.zip  Delta-Force-Hacks-2.0.zip  Fortnite\_Cheat\_External\_v3.6.zip  Interic.Fortnite.External.Cheat.v1.0.4.zip  League.of.Legends.Visuals.Cheat.v2.2.3.zip  Outlast-Trials-Cheat.zip  Pixel.Gun.3D.PC.Cheats.v3.1.9.zip | 游戏外挂/修改器 |
| Adobe.Premiere.Pro.CC.2025.v1.5.0.zip  Adobe.Photoshop.v2.8.9.zip  Avira.Phantom.VPN.Pro.Update.v1.1.5-alpha.2.zip  Burp-Suite-Professional-Latest-Patch\_v2.6.zip  VLC-Player-Pro-Unlimited.zip  SpotifyPremiumClient\_v3.3.2Alpha1.zip  CapCut.Pro.2025.v1.8.6.zip  Adobe.Acrobat.Reader.v1.6.5.zip  Adguard.Premium.Update.v3.6.4.zip  Audio-Converter.zip | 软件工具/实用程序 |
| IDM-Activator-Tool-main.zip  CleanMyPC\_Crack\_v1.5.1.zip  Agisoft-Metashape-Professional-Crack.zip  MOBILedit\_Forensic\_Express\_Pro\_Crack.zip  Microsoft-Office-Cracked.zip  Technician.Crack.v1.9.5.zip  Stata-Toolkit-Activation.zip  Internet-Download-Manager-Latest-Keygen.zip  Windows-10-Activator.zip  EaseUS.Data.Recovery.Wizard.Technician.Crack.v1.9.5.zip | 破解/激活/序列号 |
| 7-Zip-CVE-2025-0411-POC-main.zip  AsyncRAT.Dark.Mode.v3.1.4.zip  Batch.Malware.Builder.FUD.Crypter.AV.UAC.Bypass.v3.5.9.zip  ZeroTrace-Stealer-13-2026.zip  DDOS-PANEL-JoJo.zip  CyberSecurity-Keylogger.v3.3.9.zip  Pegasus\_Spyware\_2.0\_v3.4-alpha.1.zip  SQLMap.GUI.Web.Vulnerability.Scanner.v1.0.7.zip  Windows.Optimize.zip  EDR-Freeze.zip | 系统/安全/黑客工具 |
| openclaw-awesome-skills-1.6.zip  docker-openclaw-v3.8.zip  skills\_claude\_code\_startup\_v1.3.zip  gemini3-starter-prompts\_1.9-beta.1.zip  Gemini\_watermark\_Doubao\_remove\_v3.5.zip  DeepSeek-Pentest-AI.zip  kimi-cli-for-xbow\_v2.8.zip  qwen3\_computer\_use-v1.8.zip  OpenAi-Sora.zip  code-claude-manager-v1.3.zip | AI/自动化 |
| Etherum.Balance.Checker.v2.0.0.zip  Binance-alpha.zip  Fake-balance-simulation.zip  Electrum.Fake.Balance.Flash.Wallet.zip  Nova.Flash.USDT.BTC.Software.zip  MEV-by-JaredFromSubway-2.5.zip  GenBTC.zip  AI-Trading\_BOT.zip  BTC-Gen-v2.5.zip  Hunter-Wallet-v3.0.zip | 加密货币/金融 |
| youtube-viewbot.zip  YouTube.Shorts.Automation.zip  Telegram-Message-Sender-TG-3.7.zip  Instagram.Follower.Bot.v2.3.5.zip  Telegram-Adder-2025.zip  Snapchat.Username.Checker.zip  Chat-Booster-Snap.zip  Bot-Whatsapp.zip  TikTok\_Mass\_Reporting\_Bot.zip  Facebook-Checker-API.zip | 社交媒体/通讯 |
| Assignment-sphagnologist.zip  Todo.List.zip  Cheatsheet-LLM.zip  CC-Certified-in-Cybersecurity-Exam-Guide-2025.zip  IROS2025-Paper-List.zip  ICLR26\_Paper\_Finder\_3.1.zip  Linux-Basics-for-Hackers.zip  CyberSecurity-Projects.zip  Roblox-Reverse-Engineer-Handbook.zip  Delphi\_Multithreading\_English\_Edition\_Book\_Code\_2.6.zip | 教育/文档/报告 |

表1 典型恶意样本和伪装类型列表

我们又对每个伪装类型的压缩包数量进行了统计分析，以求从整体分布角度揭示攻击者的诱饵投放重点及资源倾斜方向。在此基础上，对各类型占比进行了可视化展示，如图2所示：从伪装类型分布来看，攻击者投放的恶意压缩包呈现出明显的集中趋势。游戏外挂/修改器类（23.3%）与软件工具/实用程序类（23.0%）占据最大比例，两者合计接近一半（46.3%），说明攻击者主要利用用户对游戏外挂及常用工具的强需求进行诱导传播。其次为破解/激活类（12.8%）与系统/安全工具类（12.4%），反映出攻击者针对灰色软件使用者及安全技术人员的定向投递策略。

值得关注的是，AI/自动化类占比达到9.0%，已成为重要组成部分，表明攻击者正在积极利用当前AI技术热度进行伪装投递。此外，加密货币（8.0%）与社交媒体工具（7.5%）也占据一定比例，说明攻击活动同时覆盖金融投机与流量运营人群。整体来看，该分布呈现出“高需求领域集中 + 多场景覆盖”的特点，体现出攻击者在诱导策略上的精细化设计。

![](https://mmbiz.qpic.cn/mmbiz_png/d1YpVG2tPVoBBTKe8u0os6dX7qq4tPsLZOia15K0LBdFynHQaAIgFXHYvTXd8Zlg0xJI8LLFHZIJicxycThdgyTl1XicsdTxpSQpZV29pROpk0/640?wx_fmt=png&from=appmsg)

图2 恶意样本伪装类型分布

综合上述对伪装文件类型及其分布情况的分析可以看出，攻击者在本次活动中并未针对单一目标群体，而是采用了多类型诱饵并行投放的策略，以最大化传播范围和感染概率。从占比情况来看，游戏外挂、软件工具及破解激活类资源占据较大比例，表明攻击者重点瞄准了游戏玩家、普通软件用户以及存在灰色使用需求的群体；与此同时，AI工具、自动化脚本及加密货币相关内容的占比同样不可忽视，反映出攻击者紧跟当前技术热点与高收益领域，试图吸引开发者、AI从业者及数字资产相关用户。此外，社交媒体工具与数据抓取类资源的投放，也说明攻击者对流量运营及账号体系相关人群具备一定针对性。整体来看，该攻击活动的目标呈现出明显的“广撒网”特征，但在具体方向上又集中于高活跃、高需求且安全意识相对薄弱的用户群体。

**第三章**

基础设施分析

#

在本次攻击活动的分析中，我们对前期收集的多份恶意样本进行了关联分析，并结合其网络通信特征、外联url及网络通信指纹等关键信息开展横向扩展与数据挖掘，最终获取了共计59个相关C2服务器资产，我们对这些C2服务器进行了地理位置统计分析，分析结果如图3。这些C2服务器均分布在欧洲，横跨9个国家，其中德国占25个(42.4%)占比最高，其次法国占9个(15.3%)，其余零散分布在拉脱维亚、荷兰、瑞典等其他国家。这些C2服务器有不少如“213.176.73.160”、“213.176.73.161”和“217.119.129.121”、“217.119.129.122”这样的连续段，这符合典型的"同一时间段注册、购买"的批量行为。

![](https://mmbiz.qpic.cn/mmbiz_png/d1YpVG2tPVpibicQgW4BOGOSndahavK0icgoUCkWqHyeicdib3Hmqp9Cx16Ae1eukYLFvtUR4gjl8e8WTNcnjyo8lY2ic4cxsDIwAqpQ7XN6g6Mr4/640?wx_fmt=png&from=appmsg)

图3 C2服务器IP国家分布

随后我们以这59个恶意C2服务器地址为线索，结合恶意代码二进制指纹、通信特征、样本标签等多个维度关联线索，追踪并对关联的样本哈希去重后，最终筛选出了2702个恶意伪装压缩包文件。我们对这2702个恶意伪装压缩包文件的生成时间进行了统计（见图4），数据显示这些恶意样本的投放活动从2025年3月份开始，在4月、5月、6月、7月和8月有零星投放，2025年9月后持续攀升，直至今年3月单月突破100...