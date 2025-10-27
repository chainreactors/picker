---
title: Sandworm APT组织初始访问子组全球范围展开网络攻击——每周威胁情报动态第212期  （02.14-02.20）
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492549&idx=1&sn=00a65de5b81992b861daaa4e22846f45&chksm=e90dc9efde7a40f9e943eeb2f3f4bf95ad3e6ea0bb079cb04ecfc91eb362d4f9136c98171aa5&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2025-02-22
fetch_date: 2025-10-06T20:38:17.201742
---

# Sandworm APT组织初始访问子组全球范围展开网络攻击——每周威胁情报动态第212期  （02.14-02.20）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMINeYG0xg4btBInpvgswiaLDvMezqC0jzMYgNaiagu4ktmbPMeMNPegmKe7JaecHMuibo8tvBd5w2ZUOw/0?wx_fmt=jpeg)

# Sandworm APT组织初始访问子组全球范围展开网络攻击——每周威胁情报动态第212期 （02.14-02.20）

原创

BaizeSec

白泽安全实验室

APT攻击

* Sandworm APT组织初始访问子组全球范围展开网络攻击
* 朝鲜黑客组织Kimsuky利用Dropbox和PowerShell脚本展开攻击

攻击活动

* 印度政府和金融网站遭黑客SEO投毒攻击

数据泄露

* Thermomix食谱论坛数据泄露事件：330万用户信息曝光

恶意软件

* 新型“Snake”键盘记录器变种利用AutoIt脚本逃避检测
* 新型恶意软件“FrigidStealer”通过伪装浏览器更新攻击macOS用户

勒索软件

* ###

  ###

  ###

  ###

  ###

  ###

  Abyss Locker勒索软件攻击剖析
* 美国指控两名俄罗斯男子与Phobos勒索软件有关

APT攻击

**Sandworm APT组织初始访问子组全球范围展开网络攻击**

近期，俄罗斯Sandworm APT组织的初始访问子组在全球范围内发起了大规模网络攻击活动，引发了国际社会的广泛关注。根据微软威胁情报团队的研究，该子组被称为“BadPilot”，主要负责为Sandworm组织获取初始访问权限，并为后续的网络攻击奠定基础。Sandworm APT组织（也被称为Seashell Blizzard、APT44等）与俄罗斯军事情报局（GRU）第74455部队密切相关，是一个活跃多年的高级持续威胁（APT）组织。自2022年以来，该组织的攻击目标逐渐从主要针对乌克兰扩展到全球范围，涉及北美、欧洲、中亚、中东以及亚太地区。2024年，该组织进一步将攻击重点聚焦于美国、加拿大、澳大利亚和英国等英语国家。Sandworm组织的攻击目标广泛，涵盖能源、石油和天然气、电信、航运、武器制造等关键基础设施领域，以及国际政府机构。其攻击动机不仅包括获取战略情报，还可能与政治因素相关，例如2024年全球多国大选期间，该组织的活动频率显著增加。BadPilot子组通过利用公开的漏洞扫描数据库，针对目标组织的互联网暴露面进行攻击。已知其利用了多个高危漏洞，包括Microsoft Exchange、Zimbra Collaboration、OpenFire、JetBrains TeamCity、Microsoft Outlook、Connectwise ScreenConnect和Fortinet FortiClient EMS等。

在获取初始访问权限后，该子组通过部署Web Shell和合法的远程监控与管理（RMM）工具（如Atera和Splashtop）来实现持久化控制。此外，他们还利用ShadowLink技术，将受感染系统注册为Tor隐藏服务，从而通过Tor网络实现隐蔽访问，规避传统安全审计。

Sandworm的攻击活动不仅对全球关键基础设施构成了严重威胁，还可能为俄罗斯的军事和政治行动提供支持。例如，该组织曾通过数据擦除恶意软件（如KillDisk和NotPetya）对乌克兰发动破坏性攻击。此外，其攻击活动还可能导致机密信息泄露、网络中断和经济损失。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIMsCicbVibbia3tB2DCibwoKoynBJ6zAEuc7qnicQgsK76EblicjHhqX3gvG11P0UUMbZKIr74eHwdRoNKA/640?wx_fmt=png&from=appmsg)

图 1 Sandworm APT子组的运营生命周期

参考链接：

https://www.helpnetsecurity.com/2025/02/13/sandworm-apts-initial-access-subgroup-hits-organizations-accross-the-globe/

**朝鲜黑客组织Kimsuky利用Dropbox和PowerShell脚本展开攻击**

近期，网络安全研究人员发现了一起由朝鲜政府支持的黑客组织Kimsuky（也称为APT43）发起的网络间谍活动，该活动自2024年底以来针对韩国企业、政府机构和加密货币用户。此次行动被Securonix研究人员命名为“DEEP#DRIVE”，其利用钓鱼诱饵、混淆的PowerShell脚本和Dropbox的基础设施来绕过安全防御并窃取敏感数据，凸显了该组织对可信云平台和隐蔽战术的日益依赖。此次攻击活动以韩国企业、政府机构和加密货币用户为主要目标，通过钓鱼邮件分发包含恶意Windows快捷方式（.LNK）文件的ZIP压缩包，这些文件伪装成合法的韩语文档，利用Windows默认隐藏文件扩展名的行为欺骗用户执行它们。攻击活动始于钓鱼邮件，这些邮件分发包含恶意Windows快捷方式（.LNK）文件的ZIP压缩包，文件名如“종신안내장V02\_곽성환D.pdf.lnk”，利用Windows默认隐藏文件扩展名的特性，诱骗用户执行这些恶意文件。恶意LNK文件触发一个多阶段的PowerShell脚本，该脚本结合了侦察、有效载荷投递和持久化机制。脚本使用混淆技术，包括无意义的变量名、垃圾代码插入和字符串拼接，以阻碍静态分析。例如，脚本动态构造API调用，使用如“'Invoke-WebRe' + 'quest'”的分割字符串，从而绕过基于关键词的检测。Dropbox在攻击中扮演了关键角色，既作为有效载荷存储库，又作为数据泄露通道。攻击者使用OAuth令牌与Dropbox API进行交互，实现被盗系统数据的自动化上传到预定义目录，如“/github/cjfansgmlans1\_first/”。这种对可信平台的滥用使攻击者能够绕过网络级别的防御措施，避免被IP或域名阻止列表所拦截。攻击中的一个关键组件是从Dropbox下载的Gzip压缩的.NET程序集（system\_drive.dat）。该有效载荷被解压缩，修改其头部以绕过签名检查，并直接加载到内存中执行“Main”方法，这种无文件技术避免了基于磁盘的检测。此次攻击活动不仅窃取了大量敏感数据，还展示了朝鲜黑客组织在利用可信云平台和隐蔽战术方面的高超技能。这种攻击方式使得传统安全防御措施难以奏效，给目标组织带来了巨大的安全隐患。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIMsCicbVibbia3tB2DCibwoKoyn6ITmW5LlYKicfRB4zqAe0CqP5zZpYDQKic9oILHcdvRkWjRJDnvMYPVQ/640?wx_fmt=png&from=appmsg)

图 2 解码的 PowerShell 脚本

参考链接：

https://cybersecuritynews.com/north-korean-hackers-using-dropbox-powershell-scripts/

攻击活动

**印度政府和金融网站遭黑客SEO投毒攻击**

CloudSEK研究人员发现了一起大规模的搜索引擎投毒（SEP）活动，目标是印度政府、教育和金融网站。网络犯罪分子操纵搜索引擎排名，误导用户，将他们重定向到拉米（Rummy，一种纸牌游戏）和投资诈骗网站。报告指出，超过150个印度政府门户网站（使用.gov.in和.ac.in域名）受到了影响。搜索引擎投毒（SEP）是一种欺骗性技术，网络犯罪分子通过操纵搜索引擎算法，使欺诈或有害内容在搜索结果中排名更高。用户在搜索合法信息时，不知不觉地进入了恶意网站，通常会导致诈骗、网络钓鱼或恶意软件感染。

CloudSEK研究人员确定了此次活动中使用的多种黑帽SEO技术：

**Referrer Header Manipulation（引用头篡改）**

通过JavaScript注入篡改引用头，误导搜索引擎和用户。

**Cloaking（伪装）**

网络犯罪分子向搜索引擎爬虫和人类用户显示不同的内容，使欺诈页面难以被发现。

**Keyword Stuffing（关键词堆砌）**

攻击者嵌入流行关键词和金融品牌名称，以提高搜索排名。

**Backlinking Abuse（反向链接滥用）**

通过欺诈性的链接农场人为提高诈骗网站的排名，使其看起来更可信。

**Exploiting System Vulnerabilities（利用系统漏洞）**

威胁行为者利用CMS（内容管理系统）漏洞注入恶意脚本并托管欺骗性内容。

此次活动中最复杂的方面之一是用户基于设备类型和用户代理的重定向方式。CloudSEK报告强调了政府网站中嵌入的恶意JavaScript片段如何确定访客是否应被重定向到诈骗网站。

该脚本的工作原理如下：

* 获取引用URL：检查访客是否来自搜索引擎。
* 检测移动用户：使用预定义的用户代理字符串（例如“iPhone”和“Android”）检测移动用户。
* 重定向到拉米诈骗网站：例如，将用户重定向到yono-allslots[.]com，该网站进一步重定向到indorummy[.]net。

研究人员通过使用Google开发者工具调整浏览器设置，确认了这种重定向。他们发现桌面用户反而被提供了一个404错误页面，这进一步证实了用户代理伪装的存在。

研究人员还发现，一些Telegram群组和自由职业者平台（如Fiverr）被用来买卖SEO操纵服务。他们发现一个共同的Telegram账号与这些网站的反向链接咨询有关，但该账号目前已不活跃。

这种现象不仅限于印度。研究人员还在马来西亚发现了类似的活动，马来西亚当局正在处理相同的黑客SEO渗透问题，表明这是一种全球性的滥用模式。

参考链接：

https://securityonline.info/black-hat-seo-poisoning-indian-government-and-financial-websites/

#

数据泄露

**Thermomix食谱论坛数据泄露事件：330万用户信息曝光**

近日，Thermomix官方食谱论坛Rezeptwelt.de遭遇数据泄露事件，导致330万用户的个人信息被盗。据运营该论坛的Vorwerk公司称，此次泄露是由于未经授权访问了外部服务提供商的下属服务器，暴露了部分用户资料信息。受影响的用户来自捷克、西班牙、法国、意大利、波兰、葡萄牙和澳大利亚等国家的平台及其相关论坛。Vorwerk公司表示，此次安全事件并未涉及密码、财务信息或关键内部系统的泄露。

泄露的数据取决于用户在个人资料中提供的信息类型，可能包括：

* 姓名
* 地址
* 出生日期
* 电话号码
* 电子邮件地址
* 烹饪偏好

所有受影响的用户已被告知此次事件，Vorwerk已采取立即行动以降低进一步的风险。安全漏洞存在于2025年1月30日至2月3日之间，目前已完全解决。后续的取证分析确认，此次事件仅限于Rezeptwelt.de论坛及其相关本地化版本。Vorwerk的其他所有平台，包括Thermomix®生态系统、Cookidoo®、Vorwerk网店和其他服务均未受影响。

参考链接：

https://www.bitdefender.com/en-us/blog/hotforsecurity/data-breach-at-thermomix-recipe-forum-exposes-profile-information-of-3-3-million-users

恶意软件

**新型“Snake”键盘记录器变种利用AutoIt脚本逃避检测**

近期，网络安全领域发现了一种新型的“Snake”键盘记录器恶意软件变种，该变种正在积极针对中国、土耳其、印度尼西亚、台湾和西班牙的Windows用户发起攻击。据Fortinet FortiGuard Labs的研究显示，自今年年初以来，该恶意软件已在全球范围内导致超过2.8亿次感染尝试被阻止。“Snake”键盘记录器是一种设计用于窃取敏感信息的恶意软件，通常通过包含恶意附件或链接的钓鱼邮件传播。它能够通过记录按键、捕获凭证以及监控剪贴板的方式，从流行的网络浏览器（如Chrome、Edge和Firefox）中窃取用户信息。此次发现的新型变种通过利用AutoIt脚本语言来传递和执行主要有效载荷，从而绕过传统的检测机制。新型“Snake”键盘记录器变种的核心特点是利用AutoIt脚本语言。AutoIt是一种用于自动化Windows GUI操作的脚本语言，而此次攻击中，攻击者将恶意软件编译为AutoIt二进制文件，从而在编译脚本中嵌入有效载荷，增加了静态分析的复杂性，并且能够模拟良性自动化工具的行为，从而逃避检测。

一旦启动，该恶意软件会将自身的一个副本放置在“%Local\_AppData%\supergroup”文件夹中，命名为“ageless.exe”。同时，它还会在Windows启动文件夹中放置一个名为“ageless.vbs”的文件，确保每次系统重启时，该恶意软件能够通过Visual Basic Script（VBS）自动启动，从而实现持久化，即使相关进程被终止，恶意软件仍可继续其恶意活动。

此外，该恶意软件通过将主要有效载荷注入到合法的.NET进程中（例如“regsvcs.exe”），利用进程空壳技术（process hollowing）隐藏自身，从而绕过安全检测。这种技术使得恶意软件能够在受信任的进程中运行，而不易被发现。

“Snake”键盘记录器不仅能够记录按键，还会利用类似checkip.dyndns.org的网站检索受害者的IP地址和地理位置信息。它通过调用Windows的SetWindowsHookEx API，设置低级键盘钩子（WH\_KEYBOARD\_LL，标志13），监控按键输入，从而窃取敏感信息，例如银行凭证。

此外，该恶意软件还会通过简单邮件传输协议（SMTP）和Telegram机器人将窃取的信息发送到攻击者控制的服务器，使攻击者能够访问被盗的凭证和其他敏感数据。

参考链接：

https://thehackernews.com/2025/02/new-snake-keylogger-variant-leverages.html

**新型恶意软件“FrigidStealer”通过伪装浏览器更新攻击macOS用户**

近期，网络安全研究人员发现了一种名为“FrigidStealer”的新型恶意软件，该软件专门针对macOS用户，通过伪装成浏览器更新的方式进行传播。此次攻击活动被归因于一个此前未被记录的威胁行为者TA2727，该行为者还与针对Windows平台的Lumma Stealer（或DeerStealer）以及针对Android平台的Marcher恶意软件有关。TA2727是一个以经济利益为动机的威胁行为者，其活动最早可追溯至2022年9月。该行为者通过恶意流量分发系统（TDS）操作，利用被入侵的网站和恶意JavaScript注入，伪装成浏览器更新，向用户推送各种恶意软件。此次针对macOS用户的攻击活动是TA2727的最新动向，其攻击链根据用户的地理位置或设备类型提供不同的恶意软件载荷。此次攻击活动的核心是通过恶意网站注入和伪装成浏览器更新的方式，诱导用户下载恶意软件。当用户访问被入侵的网站时，根据其地理位置和设备类型，攻击者会提供不同的恶意软件。例如：

* 在法国或英国的Windows用户会被提示下载一个MSI安装文件，该文件会启动Hijack Loader（又名DOILoader），进而加载Lumma Stealer。
* 使用Android设备的用户则会被引导下载名为Marcher的银行木马，该木马已在野外被检测到超过十年。
* 自2025年1月起，攻击活动更新为针对北美以外地区的macOS用户，通过伪装成浏览器更新的页面下载FrigidStealer。

FrigidStealer的安装程序需要用户明确启动未签名的应用程序，以绕过macOS的Gatekeeper保护机制。随后，一个嵌入的Mach-O可执行文件会被运行以安装恶意软件。该可执行文件使用Go语言编写，并通过WailsIO项目在用户的浏览器中渲染内容，进一步增强其伪装成合法Chrome或Safari安装程序的可信度。安装完成后，FrigidStealer利用AppleScript提示用户输入系统密码，从而获得提升的权限，用于从网络浏览器、Apple Notes以及与加密货币相关的应用程序中收集文件和各种敏感信息。这种攻击方式与针对macOS系统的其他信息窃取恶意软件类似，但FrigidStealer的出现表明攻击者正在不断扩展其攻击目标，以涵盖更多平台。

参考链接：

https://thehackernews.com/2025/02/new-frigidstealer-malware-targets-macos.html

勒索软件

###

A**byss Locker勒索软件攻击剖析**

Abyss Locker勒索软件是一种新型的网络威胁，于2023年出现，以其迅速且破坏性强的攻击方式著称，专门针对关键网络设备。Abyss Locker在2024年活跃度较高，导致多起安全事件发生。该威胁组织通常通过部署恶意软件来控制关键网络设备，从而在网络内部进行活动。其攻击目标包括VPN设备、网络附加存储（NAS）和ESXi服务器等。Abyss Locker的攻击通常从利用未修补的VPN设备开始。例如，攻击者利用已知漏洞（如CVE-2021-20038）入侵未修补的SonicWall VPN设备，从而获得对内部网络设备和主机的访问权限，并部署额外的隧道工具以保持持久性和促进进一步访问。一旦进入受感染网络，Abyss Locker经常 targeting 备份设备。这些设备通常使用高权限服务账户，攻击者利用修改版的开源PowerShell工具‘Veeam-Get-Creds.ps1’来收集Veeam备份系统中存储的本地和域账户凭据。此外，攻击者还通过远程转储Windows安全账户管理器（SAM）和安全注册表蜂巢来获取凭据材料。Abyss Locker采用多种技术来规避检测并禁用受感染主机上的安全控制，包括：

* 通过修改注册表键

  ‘HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender’并将‘DisableAntiSpyware’值设置为‘1’来禁用Windows Defender。
* 使用任务管理器或以SYSTEM账户运行来移除EDR代理或停止其进程。
* 使用‘自带易受攻击驱动程序’（BYOVD）技术来禁用终端保护控制，例如使用Ze...