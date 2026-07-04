---
title: 每周高级威胁情报解读(2026.06.26~07.02)
url: https://mp.weixin.qq.com/s/fch-cGOjTSunPUidozD-RQ
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:43:43.323459
---

# 每周高级威胁情报解读(2026.06.26~07.02)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOq8qdH3icAxoLS49IS6Cdaa5D5feS5iaytK7JSFy4ykNxNIwQFKLzHj7bhnHsYmueFk0gAtzVwu9zDYpgNZlQ32Kvn18aj4ibicAFog/0?wx_fmt=jpeg)

# 每周高级威胁情报解读(2026.06.26~07.02)

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026.06.26~07.02

**攻击团伙情报**

* 伊朗-Nexus TAG-182 分发 MarkiRAT 监控工具
* PolinRider：与朝鲜有关的供应链活动正在开源生态系统中蔓延
* APT-C-20利用explorer劫持和LSB隐写等技术实施隐蔽攻击活动分析
* 与 Lazarus 关联的 npm 恶意软件伪装成 Rollup Polyfill
* Turla新型STOCKSTAY后门针对乌克兰及欧洲进行情报收集

**攻击行动或事件情报**

* 加密货币 Clipper 浏览器扩展程序攻击活动
* Kaspersky披露The Gentlemen勒索组织定制后门与不断演变的攻击战术
* 从必应搜索到勒索软件：Bumblebee 和 AdaptixC2 推出 Akira
* TONResolver RAT 滥用 TON 区块链攻击日本酒店业
* Blackpoint披露TaskWeaver Node.js加载器与Djinn Stealer跨平台凭证窃取链

**恶意代码情报**

* 伪造的谷歌和 Cloudflare 验证页面传播多种恶意软件家族
* JADEPUFFER：用于自动化数据库勒索的代理勒索软件
* Cisco Talos披露ARToken：EvilTokens附属PhaaS面板全面解析
* RustDuck: 双阶段僵尸网络深度剖析
* VIPERTUNNEL Python后门利用LOLBAS技术与SOCKS5隧道隐蔽攻击

**漏洞情报**

* 苹果发布 iOS、macOS Tahoe 和 Safari 的安全补丁
* Citrix 内存泄漏无限扩大（Citrix NetScaler 预授权内存过度读取 CVE-2026-8451）

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqib1MHNXvgUIPHEN3CoGmybg1jVzHwtNiaCzXP6rxTT3scj8Ix5KM6HT8IfEwQL9AmFk1aA9gGthPNWn3pR0pQwmMm08ufX4ymLw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqicxr4gUraZv1ic7pS9rc9lyBUmCQzWuVz9UxUlAk73rEXNicekz6W8aLtmjPfkGqlpo5acbxtSUqhLfgLTibl0jtStu8aJ3mjEuZM/640?wx_fmt=gif&from=appmsg)

**攻击团伙情报**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq8sPk8rbw58kjzQDnXz6J6MOCGw78Hnm27l02eULdUwCBSyHXZkH8ibRwfTDhRSXFt84y13HEePYoexVFuzDFIx9MK2yRicxvnW4/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq9ekngUaDiaof7lvicPwuMKicReKFiaK6ClUfgbMONtngVTQaFQPLsDgGGTYYDibX104HW75ibVIqBj6FlWMrQKafNpDu8838Siberz4Q/640?wx_fmt=gif&from=appmsg)

**01**

**伊朗-Nexus TAG-182 分发 MarkiRAT 监控工具**

**披露时间：**2026年7月1日

**情报来源：**https://www.recordedfuture.com/research/nexus-tag182-disseminates-markirat

**相关信息：**

Recorded Future Insikt Group披露了伊朗关联威胁集群TAG-182的监控活动，该组织通过分发伪装成VPN和媒体播放器（如YEPlayer和Pis2rayVPN）的木马化软件传播MarkiRAT远程访问木马，利用BITSAdmin进行载荷投递，通过伪装成svchost.exe的svehost.exe进程实现持久化，并借助伪造域名和PHP-based C2端点进行数据外泄和监控。该活动在2026年5月26日伊朗部分恢复战时互联网限制后显著加剧，被评估为伊朗国内安全监控行动的一部分，可能与IRGC、Basij Cyber Council、FATA和MOIS等组织有关。

**02**

**PolinRider：与朝鲜有关的供应链活动正在开源生态系统中蔓延**

**披露时间：**2026年7月1日

**情报来源：**https://socket.dev/blog/polinrider-north-korea-linked-supply-chain-campaign-expands

**相关信息：**

Socket Threat Research Team披露PolinRider攻击活动，该活动与朝鲜Contagious Interview及Famous Chollima行动关联，攻击者通过向tailwind.config.js、postcss.config.js、eslint.config.mjs等常见配置文件注入恶意代码，利用Tron区块链交易作为死信投递解析C2地址，避免硬编码URL被封锁。该活动最初通过劫持@common-stack/generate-plugin等npm包传播，使用特定解码种子"rmcej%otb%"进行混淆，在安装阶段即触发载荷获取。据OpenSourceMalware统计，PolinRider已入侵超过700个GitHub仓库，远超GlassWorm和TasksJacker等同类活动。攻击者不仅针对npm生态，还将恶意载荷扩展至Packagist PHP包、Go模块及Chrome浏览器扩展，形成跨平台、多生态系统的供应链攻击矩阵

**03**

**APT-C-20利用explorer劫持和LSB隐写等技术实施隐蔽攻击活动分析**

**披露时间：**2026年7月1日

**情报来源：**https://mp.weixin.qq.com/s/TDb\_UzNfebMzMxh\_bQdMvA

**相关信息：**

近期360高级威胁研究院在对APT-C-20组织的持续跟踪过程中发现,该组织用携带恶意宏的诱饵文档作为初始载体，宏代码执行后，会从文档内部解析并释放恶意组件，随后利用COM劫持建立用户级持久化机制，并借助资源管理器初始化COM对象的过程触发恶意DLL加载。加载后的核心模块进一步从经过隐写处理的图片资源中提取并执行Shellcode，最终在内存中构建基于合法云存储平台Filen.io的隐蔽控制框架，实现无文件化驻留与远程控制能力。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq8Rkp2TKY24vsJbKNlaYLzmPIPeKlmEicTBWjuGTQGzJRlD5kHMpoGXufRhZF2HibVe9MngPaLbsoZyZTlJe57Aom106iaHfoVW34/640?wx_fmt=png&from=appmsg)

**04**

**与 Lazarus 关联的 npm 恶意软件伪装成 Rollup Polyfill**

**披露时间：**2026年6月30日

**情报来源：**https://research.jfrog.com/post/rollup-polyfill-masquerading/

**相关信息：**

JFrog Security Research发现Lazarus关联的攻击者通过rollup-packages-polyfill-core等六个npm包伪装Rollup polyfill工具，经多层依赖链从JSONKeeper获取eval载荷，最终部署具备远程控制、浏览器凭证窃取、剪贴板监控和文件收集能力的完整后门。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqicLloaB3FA612YqJlTPLnlJF3F123IzAaob1zIiaJuzLFhebibpfHKYXqichicIBW2qGNeiaupyyM3h3QoWHNOBjnicxNuIYeMichktrw/640?wx_fmt=png&from=appmsg)

**05**

**Turla新型STOCKSTAY后门针对乌克兰及欧洲进行情报收集**

**披露时间：**2026年6月26日

**情报来源：**https://cloud.google.com/blog/topics/threat-intelligence/stockstay-turla-intelligence-gathering

**相关信息：**

Google威胁情报小组分析了Turla组织自2022年12月起部署的STOCKSTAY后门，主要针对乌克兰政府和军事机构及欧洲外交相关实体。该后门采用.NET编写，通过WebSocket加密通信，由三组件构成：STOCKBROKER负责网络隧道，STOCKMARKET负责配置与协调，STOCKTRADER执行文件操作、注册表修改、屏幕截图和命令执行等任务。早期版本伪装成股市数据工具，后演变为PDF查看器等常见应用，配置文件中嵌入加密货币相关URL作为诱饵。STOCKSTAY与Turla另一工具KAZUAR存在显著重叠，包括2025年引入的K1MORPHERSquirrel3字符串混淆机制、多组件分离架构和环境键控防御，表明可能由同一开发团队维护。攻击者通过学术和外交主题钓鱼邮件、恶意RDP文件及利用CVE-2025-8088的WinRAR漏洞分发该后门，并利用Render等第三方平台托管WebSocket服务器以隐藏基础设施。Turla在攻击不同阶段使用STOCKSTAY，初期采用硬编码密码，后期结合环境键控实施精准投放。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqicK5JflQ0dBOMDsRAv8pIaMUexKDJhlMo4iadKmOtxHNOqg2ibibaSyFrBsJaq3KeterBa7YJNBLHvXhbgjtSx9wKAQPqAeCzmMhU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqicnY0dmTWcViackdqAjIkOBVTVqc9kxick8tCibYGX1P2wNMibwUsIlNONAoSjUXp9m83tNNV1uEbEBFKEZ3TMLP5bibqh6uQlwwz4U/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqictPia4iaBM9grIS2dBHX7AWybQ1qDVlK3mLzXuJep63WYNG1QXhsayOOX1MzLHFDkuXggicBAj6yapjBxNwDgEIRW5HUhwwx8ong/640?wx_fmt=gif&from=appmsg)

**攻击行动或事件情报**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqicLUgzWicmyhzybjolq6WJp1ic8ibeniaQsKsMp0YXaxQhVTqnU5knVVvM9AbQ7Z7NuRtudHP9R5aAuABEa3Rr2vL1ToTYTkmu2SicQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq9oL0SuC2VF1Yq7w1R9E5hl4XHxtg84SczSLZezJMxbCZfQwczkjQkC6dTR5cUMibibicUSBhJpqJtcK7lRx53IfDtKcNia6j8MV6Q/640?wx_fmt=gif&from=appmsg)

**01**

**加密货币 Clipper 浏览器扩展程序攻击活动**

**披露时间：**2026年6月30日

**情报来源：**https://www.mcafee.com/blogs/other-blogs/mcafee-labs/crypto-clipper-wallet-swapping-browser-extension-malware/

**相关信息：**

McAfee发现了一场通过恶意浏览器扩展窃取加密货币的大规模活动。攻击者通过未签名的.NET或Golang安装包，向Chrome、Edge、Brave等浏览器植入伪装成“Google Notes”的恶意扩展。该扩展监控剪贴板，利用正则表达式识别比特币、以太坊等链上钱包地址，在用户粘贴前将收款地址替换为攻击者控制的地址，导致资金直接转入攻击者钱包。为绕过浏览器安全机制，安装包会修改Secure Preferences文件并重新计算HMAC值，使扩展看起来像合法安装，同时程序化开启开发者模式以维持加载。扩展的C2地址不硬编码，而是通过查询以太坊智能合约动态解析，攻击者仅需更新链上数据即可轮换基础设施，增加了封堵难度。扩展对主流币种实施按受害者地址一一映射的替换策略，Solana等则使用统一地址。McAfee遥测显示感染遍布全球，以印度最为集中。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq9JK6aLfRdBPjjVqjPuHRXowsU42YWVibk42L2sZ32f6JzjO8QSGa1evUicD4Aslze1JU2fwGBjCoRRge5iclJh9FQq2HWo9O1Fe0/640?wx_fmt=png&from=appmsg)

**02**

**Kaspersky披露The Gentlemen勒索组织定制后门与不断演变的攻击战术**

**披露时间：**2026年6月30日

**情报来源：**https://securelist.com/the-gentlemen-raas/120447/

**相关信息：**

Gentlemen勒索软件团伙自2026年初活跃，已跻身全球前十大勒索组织，主要针对制造业、IT、医疗、金融等行业的全球大型企业。攻击者通常通过漏洞利用或初始访问代理获取权限，而后使用SharpADws、NetScan和netsh进行内网侦察和流量嗅探，窃取敏感凭证。横向移动通过GPO脚本和PsExec实现，同时使用多种BYOVD驱动、kavrmvr.exe及注册表修改等手段禁用安全软件。该团伙部署了Go编写的定制后门，通过Yamux库建立与C2的持久隧道，支持命令执行和SOCKS代理。Go勒索软件采用密码反沙箱、Curve25519与XChaCha20混合加密，支持GPO批量横向扩散，加密前会终止虚拟机和服务并删除卷影副本。新发现的C开发中勒索软件使用AES256-GCM+RSA加密，通过电邮联系，表明团伙正扩展技术栈。攻击通常在取得权限数小时内完成，部分案例中访问权限提前数月已被建立，暗示存在外部初始访问代理合作。

**03**

**从必应搜索到勒索软件：Bumblebee 和 AdaptixC2 推出 Akira**

**披露时间：**2026年6月29日

**情报来源：**https://thedfirreport.com/2026/06/29/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira-3/

**相关信息：**

攻击始于用户通过Bing搜索ManageEngine OpManager时被SEO投毒诱骗至仿冒网站，下载带毒MSI安装包。IT管理员执行该MSI后，通过DLL侧加载启动BumbleBee加载器，该加载器规避独联体地区后，连接DGA生成域名建立C2，约五小时后投放AdaptixC2后门。攻击者利用该后门进行内网侦察，创建域管理员账户并安装RustDesk实现持久化。随后通过RDP横向移动至域控和备份服务器，使用wbadmin导出NTDS.dit、通过lsassy转储LSASS内存、并利用psql窃取Veeam凭据。借助反向SSH隧道和Cloudflare隧道规避防火墙，使用FileZilla经SFTP外传超75GB数据，包括SYSVOL和用户凭证。最后部署Akira勒索软件，通过WMI删除卷影副本，并针对根域和子域执行加密。Swisscom关联案例中攻击者还使用了BYOVD尝试终止安全防护。整个入侵持续约五天，攻击者熟练运用多种开源工具和Living-off-the-land技术。

**04**

**TONResolver RAT 滥用 TON 区块链攻击日本酒店业**

**披露时间：**2026年6月29日

**情报来源：**https://www.trendmicro.com/en\_us/research/26/f/tonresolver.html

**相关信息：**

攻击者针对日本Booking.com合作酒店，发送伪装成客人投诉的钓鱼邮件，诱骗员工打开恶意LNK文件。该LNK中的PowerShell通过大整数运算解码域名，下载PS1脚本，部署Node.js并执行恶意载荷TONResolver。该RAT采用虚拟机混淆，通过WebSocket加密通信，C2地址不硬编码，而是从TON区块链智能合约动态解析，攻击者可随时更换C2，难以封堵。TONResolver具备保活、文件操作、命令执行和PowerShell执行功能，后续已观察到窃取浏览器凭证。攻击者还利用日程工具合法通知服务绕过SPF/DKIM。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOq8vGMnFpXKREFFZ1FPCqZDfBGOASvfHObTo6rsLSh7H9MANZmuV6ACBZo5XkKhQYA7FdolQQt92w7wYsgpic5F20BbYWA1Qqlfk/640?wx_fmt=png&fr...