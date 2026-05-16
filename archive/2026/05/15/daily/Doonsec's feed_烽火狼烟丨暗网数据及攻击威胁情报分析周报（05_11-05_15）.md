---
title: 烽火狼烟丨暗网数据及攻击威胁情报分析周报（05/11-05/15）
url: https://mp.weixin.qq.com/s/6veyJePz3ELYvS2di8QE_A
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:11:34.586856
---

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（05/11-05/15）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mxwq2AF6zpMF2ZKKWg3UjH3Vica3uQjMPWjQUEtr0jlMX3OZm1BWtRRnsrXGVllGnz4kTlwomwX3EtfENgQPAfC5YnM34e8xUHxRWdUsB6p4/0?wx_fmt=jpeg)

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（05/11-05/15）

盛邦安全应急响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

WebRAY安全服务团队定期针对敏感数据泄露、热点资讯、热点技术、热点漏洞、威胁攻击等情况进行跟踪整理与监测分析，本周总体情况如下：

本周内共发现暗网数据贩卖事件601起，同比上周增加0.17%。本周内贩卖数据总量共计148818万条；累计涉及7个主要地区及6种数据分类，数据泄露来源地区分布情况如图1所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpPO1cvj408S8aZuVotN0dgK3ygVTW2xLGfxGvokrhxU5vUVNNibezoZoGygYF0g3OtytA4zjbFlcKOxHzFBsx1OvmCfVAAwetKc/640?wx_fmt=png&from=appmsg)

图1 泄露数据来源地区分布情况

本周内泄露数据涉及贸易、金融、服务等多种类型数据，具体占比如图2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpMPUyozy5sqicWn4eKXNJ46gah6xicjKoChGjFOxVCiavMl1WECibu3xEbFMsoqTNgL4ROiaJDh7iaRdZAZkr7XVW4zL1Qtl94eElfD0/640?wx_fmt=png&from=appmsg)

图2 泄露信息数据类型占比

近期安全威胁以数据泄露与漏洞攻击为主，多个政府相关服务商发现数据泄漏，本周内出现的安全漏洞中以CyberPanel命令执行漏洞危害程度较大；内部安全运营中心共发现恶意攻击来源IP7893条，主要涉及扫描探测等类型。

**01.**

**重点数据泄露事件**

**南斯塔福德郡水务公司疑似数据泄露**

泄露时间：2026-05-14

泄露内容：南斯塔福德郡水务公司是英国一家主要的自来水供应企业。在此次网络攻击中，该公司663,887名客户和员工的个人信息被提取并在暗网上发布，包括全名、实际地址、电子邮件地址、电话号码、出生日期、客户账户凭证、银行账户详情及员工人力资源数据。

泄露数据量：66万

关联行业：水务

地区：英国

**危地马拉财政部疑似数据泄露**

泄露时间：2026-05-14

泄露内容：危地马拉财政部运营的国家采购登记系统RGAE（Registro General de Adquisiciones del Estado）疑似遭到攻击。攻击者利用漏洞通过模拟普通用户流量绕过Cloudflare和WAF，从2020至2026年间提取了13万条注册记录及23.5万份敏感 PDF 文件，总计324.5GB。已公开 5000行CSV样本和200个PDF预览。

泄露数据量：13万

关联行业：政府

地区：危地马拉

**Nuvidio疑似数据泄露**

泄露时间：2026-05-14

泄露内容：巴西身份验证与生物识别服务商Nuvidio系统疑似被攻击，约40,000份文件（6.3GB）泄露，包括客户身份证件、视频通话录音、生物识别数据、生产凭证、AWS基础设施信息及部分内部系统数据。受影响客户包括Banco Pan、Bradesco、C6 Bank等。

泄露数据量：4万

关联行业：生物识别

地区：巴西

**Lightning AI疑似数据泄露**

泄露时间：2026-05-14

泄露内容：Lightning AI（PyTorch Lightning开发公司）系统疑似被攻破，泄露内部代码库、应用和平台私有代码、项目文件夹、开发资源（插件、模板、扩展、基准测试和部署材料）及工程环境相关文件，共涉及1,360个目录和10,239个文件。攻击者提到之前PyPI凭证泄露事件，并声称部分额外数据也被获取。

泄露数据量：1万

关联行业：人工智能

地区：美国

**CANTV ABA Ultra疑似数据泄露**

泄露时间：2026-05-14

泄露内容：委内瑞拉国家电信公司CANTV是该国主要电信及互联网服务提供商。疑似其关联的UISP Ubiquiti管理面板遭到攻击。据称此次事件暴露了约7,500条CANTV ABA Ultra用户记录及4,000条OLT/GPON网络设备记录，涉及用户基本信息、服务计划与账户状态，以及光纤宽带设备MAC地址、序列号、固件信息和基础设施监控数据等。

泄露数据量：1万

关联行业：运营商

地区：委内瑞拉

**02.**

**热点资讯**

**Google Android入侵日志功能发布**

谷歌推出了名为Intrusion Logging的安卓可选功能，作为高级保护模式的一部分，用于存储端到端加密的取证日志，以分析复杂间谍软件攻击。该功能每天记录应用活动、网络连接、文件传输、系统证书变更及设备锁定状态等信息，日志在谷歌服务器保存12个月，用户可离线下载。日志由设备加密，第三方无法访问，包括谷歌本身。此功能可帮助高风险用户向安全专家提供数据进行调查，同时兼顾隐私安全。此外，谷歌还发布多项隐私与安全改进，包括验证金融通话、实时威胁检测、限制无障碍API访问、增强“查找中心”功能和AI数据隔离等，进一步提升安卓平台安全性。

消息来源：

https://thehackernews.com/2026/05/android-adds-intrusion-logging-for.html

**MiniShai-Hulud供应链攻击波及npm与PyPI**

威胁行为者TeamPCP发起的新一轮Mini Shai-Hulud供应链攻击，已影响TanStack、UiPath、Mistral AI、OpenSearch及Guardrails AI的npm和PyPI软件包。被攻破的npm包包含混淆JavaScript（router\_init.js），可窃取云服务、加密钱包、AI工具、消息应用及CI系统凭证，并通过Session网络、GitHub API和typosquat域名进行数据外泄。恶意软件可在IDE中建立持久化钩子、注入GitHub Actions工作流、安装gh-token-monitor监控令牌，并具有自毁机制。TanStack事件被分配CVE-2026-45321，CVSS 9.6分，影响42个包、84个版本，攻击利用GitHub Actions OIDC令牌进行可信发布，首次实现带有效SLSA证明的恶意npm包传播。PyPI包如Mistral AI、Guardrails AI也被感染，恶意载荷含地理感知与破坏性逻辑，显示供应链攻击从孤立入侵向身份驱动、CI/CD传播升级。

消息来源：

https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html

**RubyGems因重大恶意攻击暂停注册**

RubyGems在遭遇“重大恶意攻击”后，暂时关闭账户注册。此次攻击影响数百个软件包，其中部分携带漏洞，目标主要是RubyGems注册表本身。Mend.io已移除超过120个恶意包，RubyGems封锁并删除了相关机器人账户及500多个恶意包。RubyGems正与Fastly合作，启用WAF防护并添加账户创建速率限制，预计恢复注册需2-3天。此次攻击凸显开源包管理平台在身份和注册流程安全方面的薄弱环节。

消息来源：

https://thehackernews.com/2026/05/rubygems-suspends-new-signups-after.html

**AI驱动漏洞利用与恶意软件的新威胁动态**

威胁情报组织披露了一起犯罪行动，使用AI生成的零日漏洞利用代码，针对流行开源网络管理工具中的Python脚本双因素认证缺陷，且在攻击发起前已修补。该漏洞源于高层语义逻辑错误，非传统实现缺陷，AI能够理解开发者意图并发现代码矛盾。与以往实验室研究不同，此次攻击具有明显犯罪目的，AI承担发现和编码漏洞的技术重任，人类策划整体行动。相关恶意软件如PromptSpy可自主控制Android设备、执行手势、截取生物识别数据并绕过卸载保护。有团体利用AI系统化分析漏洞、训练模型并生成利用代码，关联组织则用AI生成填充代码以隐藏恶意软件。威胁行为者通过代理中继、合并账户和影子API绕过使用控制，形成对防御方的结构性优势，使高级AI能力可被无限制滥用，从而加速漏洞利用和恶意软件开发工业化。

消息来源：

https://www.databreachtoday.com/ai-built-zero-day-nearly-powered-mass-attack-a-31659

**微软发布138个漏洞补丁并推动AI驱动漏洞发现**

微软于周二修复了其产品组合中138个安全漏洞，其中30个被评为严重，104个为重要，涉及权限提升、远程代码执行、信息泄露等多种类型。补丁包括Windows DNS堆缓冲区溢出（CVE-2026-41096）、Azure DevOps信息泄露（CVE-2026-42826）、Dynamics 365代码注入（CVE-2026-42898）等关键漏洞。部分补丁也涵盖AMD Zen 2 CPU缓存隔离缺陷和Chromium中的127个漏洞。微软强调，部分漏洞由其新型多模AI漏洞发现系统MDASH识别，表明AI辅助漏洞发现正在加速Patch Tuesday更新。组织被建议及时更新补丁、升级Windows Secure Boot证书、启用多因素认证、改善配置、分段环境及强化检测响应，以应对AI加速下的漏洞发现和攻击风险。

消息来源：

https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html

**03.**

**热点技术**

**TrickMoC木马利用TON实现高级网络控制**

网络安全研究人员发现，TrickMo最新版本TrickMo C通过TON去中心化区块链进行命令与控制（C2），活跃于法国、意大利和奥地利的银行及加密货币钱包用户。该木马依赖运行时加载的APK（dex.module），新增网络功能，包括侦察、SSH隧道和SOCKS5代理，使受感染设备可作为网络枢纽和流量出口节点。Dropper应用伪装成成人版TikTok，实际恶意软件冒充Google Play服务。新版本支持curl、dnslookup、ping、telnet和traceroute等命令，实现远程网络侦察，并利用嵌入的TON代理隐藏通信，规避传统阻断手段，同时保留未来扩展功能的可能性。

消息来源：

https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html

**GemStuffer活动利用RubyGems进行数据抓取**

安全研究人员发现，名为GemStuffer的新活动利用RubyGems仓库发布超过150用于数据存储泄露的RubyGems包，将其作为数据泄露通道而非恶意软件传播。这些.gem包通过硬编码API密钥将从英国地方政府门户收集的会议日历、议程、PDF文档和官员联系方式等信息打包为有效.gem档案并上传至RubyGems。部分变体在“/tmp”创建临时凭证环境并通过CLI推送，另一些则通过HTTP POST直接上传API。虽然信息本身公开，但系统性批量抓取可能用于展示对政府基础设施的攻击能力或测试包注册表滥用模式，攻击机制包括重复.gem生成、版本递增、硬编码凭证和嵌入抓取数据的包档案。

消息来源：

https://thehackernews.com/2026/05/gemstuffer-abuses-150-rubygems-to.html

**Exim邮件服务器发布漏洞补丁**

Exim邮件传输代理在部分使用GnuTLS的配置中存在关键用户释放（UAF）漏洞CVE-2026-45185，可被未经认证的远程攻击者利用执行任意代码，影响版本为4.97至4.99.2。漏洞在处理BDAT分块SMTP流量的TLS关闭阶段触发，可能导致服务器命令执行、邮件数据访问及进一步环境渗透。修复已在Exim 4.99.3发布，Ubuntu和Debian用户应及时更新。报告称，漏洞概念验证（PoC）开发历时七天，由其AI驱动系统与人类研究者合作完成。AI在理解代码和测试利用路径方面显著提升了效率，但研究者认为大型语言模型尚未能独立针对生产环境软件生成完整的漏洞利用程序。

消息来源：

https://www.bleepingcomputer.com/news/security/new-critical-exim-mailer-flaw-allows-remote-code-execution/

**GhostLock利用Windows文件API阻断访问**

安全研究员发布了概念验证工具GhostLock，展示如何利用Windows的CreateFileW API及其dwShareMode参数阻止本地或SMB共享文件访问。通过将dwShareMode设为0，攻击者可获得文件独占句柄，导致其他用户或应用尝试访问时出现“STATUS\_SHARING\_VIOLATION”错误。GhostLock可由标准域用户运行，无需管理员权限，并可递归锁定大量SMB文件。攻击虽非破坏性，但可作为拒绝服务或入侵诱饵，干扰IT响应。攻击持续期间，文件访问受阻，重启系统或终止SMB会话后访问恢复。研究指出，现有安全产品难以检测此类攻击，唯一可靠指标是文件服务器层每会话ShareAccess=0的开放文件计数，并在白皮书中提供了SIEM查询和NDR检测规则作为防御模板。

消息来源：

https://www.bleepingcomputer.com/news/security/new-ghostlock-tool-abuses-windows-api-to-block-file-access/

**Windows漏洞YellowKey和GreenPlasmaPoC公开**

安全研究人员发布了针对Windows的两项未修补漏洞的PoC：YellowKey和GreenPlasma。YellowKey是一种BitLocker绕过漏洞，影响Windows 11及Windows Server 2022/2025，通过在USB或EFI分区放置特制FsTx文件并在WinRE启动时触发，可访问BitLocker保护的存储卷，无需凭证。GreenPlasma为权限提升漏洞，允许非特权用户在SYSTEM可写目录中创建任意内存段，有潜在操纵内核驱动或特权服务的风险。研究者表示漏洞公开源于对微软处理报告的不满，BitLocker用户建议启用PIN码和BIOS密码进行缓解，而GreenPlasma PoC尚不完整，但存在进一步提权可能。

消息来源：

https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/

**04.**

**热点漏洞**

**WordPress插件 Plugin AAWP反射型跨站脚本漏洞（CVE-2022-50970）**

WordPress插件Plugin AAWP是一款用于在网站上展示亚马逊产品的插件，提供产品展示、比较表格和自定义功能。WordPress插件 Plugin AAWP存在反射型跨站脚本漏洞。该漏洞产生的原因是aawp-settings管理页面的tab参数未对输入内容进行有效过滤和编码，攻击者可利用该漏洞通过已认证用户身份构造带有XSS负载的URL执行任意JavaScript代码，从而影响已认证用户的会话安全。

影响版本：

Plugin AAWP <= 3.16

**CyberPanel命令执行漏洞（CVE-2021-47949）**

CyberPanel是一款基于OpenLiteSpeed的服务器管理面板，提供网站管理、文件管理和数据库管理功能。CyberPanel存在命令执行漏洞。该漏洞产生的原因是/filemanager/controller接口未对completeStartingPath参数进行有效校验，攻击者可利用该漏洞通过符号链接攻击读取任意敏感文件，并结合/websites/fetchFolderDetails接口执行任意Shell命令，从而导致服务器被完全控制。

影响版本：

CyberPanel <=  2.1

**uBidAuction反射型跨站脚本漏洞（CVE-2022-50969）**

uBidAuction是一款在线拍卖系统，提供商品管理、竞拍和日志记录等功能。uBidAuction存在反射型跨站脚本漏洞。该漏洞产生的原因是backend/mailingLog/manage模块filter功能中的date\_created、date\_from、date\_to和created\_at参数未对用户输入进行有效过滤和编码，攻击者可利用该漏洞通过远程构造恶意GET请求注入恶意脚本并在受害者浏览器中执行任意JavaScript代码，从而影响用户会话安全。

影响版本：

uBidAuction == 2.0.1

**WordPress插件 Plugin amministrazione-aperta任意文件读取漏洞（CVE-2022-50956）**

WordPress插件 Plugin amministrazione-aperta是一款用于信息公开和文档管理的WordPress插件，提供文件展示和内容管理功能。WordPress插件 Plugin amministrazione-aperta存在任意文件读取漏洞。该漏洞产生的原因是dispatcher.php文件未对open GET参数进行有效校验，攻击者可利用该漏洞通过构造恶意文件路径读取Web服务器可访问的敏感文件，从而导致敏感信息泄露。

影响版本：

Plugin amministrazione-aperta  ==  3.7.3

**Aero CMS代码注入漏洞（CVE-2022-50944）**

Aero CMS是一款内容管理系统，提供文章发布、图片上传和后台管理功能。Aero CMS存在代码注入漏洞。该漏洞产生的原因是admin/posts.php接口在source=add\_post参...