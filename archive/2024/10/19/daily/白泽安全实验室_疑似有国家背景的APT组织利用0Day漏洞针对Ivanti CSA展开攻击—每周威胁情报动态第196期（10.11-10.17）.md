---
title: 疑似有国家背景的APT组织利用0Day漏洞针对Ivanti CSA展开攻击—每周威胁情报动态第196期（10.11-10.17）
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492366&idx=1&sn=a4b61bc1dfa3c615999b2eb232269619&chksm=e90dc924de7a4032e1555fa467b97d3b1509e4f98c743db55e9bcaf257add39d745e94fb1aaf&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-10-19
fetch_date: 2025-10-06T18:54:16.870634
---

# 疑似有国家背景的APT组织利用0Day漏洞针对Ivanti CSA展开攻击—每周威胁情报动态第196期（10.11-10.17）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMINeYG0xg4btBInpvgswiaLDvMezqC0jzMYgNaiagu4ktmbPMeMNPegmKe7JaecHMuibo8tvBd5w2ZUOw/0?wx_fmt=jpeg)

# 疑似有国家背景的APT组织利用0Day漏洞针对Ivanti CSA展开攻击—每周威胁情报动态第196期（10.11-10.17）

原创

BaizeSec

白泽安全实验室

**APT攻击**

* 疑似有国家背景的APT组织利用0Day漏洞针对Ivanti CSA展开攻击
* APT34组织针对阿联酋和海湾地区展开网络攻击
* Water Makara组织利用Astaroth恶意软件针对巴西展开攻击

**攻击活动**

* 俄罗斯法院网站遭受亲乌克兰黑客团体攻击导致服务中断

**数据泄露**

* 丹麦体育模拟器公司TrackMan泄露110TB用户数据
* 《精灵宝可梦》开发商Game Freak遭受数据泄露

**恶意软件**

* 新型Linux变种FASTCash恶意软件瞄准金融系统
* 银行木马TrickMo攻陷13000台设备

**勒索软件**

* 日本卡西欧公司确认遭受勒索软件攻击并泄露机密信息
* Veeam漏洞被利用传播Akira和Fog勒索软件

APT攻击

**疑似有国家背景的APT组织利用0Day漏洞针对Ivanti CSA展开攻击**

Fortinet的安全研究团队近日发布报告，揭露了一起由疑似国家背景的攻击者发起的针对Ivanti Cloud Services Appliance (CSA)的网络攻击事件。攻击者展示了通过零日漏洞链获取受害者网络初始访问权限的高级持续性威胁（APT）能力。

在一次客户网络的事件响应中，安全研究团队发现了攻击者通过利用CVE-2024-8190以及另外两个先前未知的漏洞，成功进入了客户的网络。攻击者首先利用路径遍历漏洞非法访问了CSA设备上的敏感资源，例如通过向URI末尾插入%3F.php并附加要通过路径遍历访问的PHP资源的位置，成功访问了/gsb/users.php资源。FGIR在实验室环境中模拟了这一漏洞的利用，以了解可能获取的信息。随后，攻击者利用CVE-2024-8190漏洞，这是一个影响/gsb/DateTimeTab.php资源的命令注入漏洞，尝试获取CSA设备上配置的用户凭证。攻击者通过发送恶意的POST请求，将恶意命令注入到POST请求变量TIMEZONE中，从而操纵了setPhpTimeZone函数，进一步获取了管理员用户的凭证。

在成功提取凭证后，攻击者利用这些凭证进行了进一步的认证攻击，针对/gsb/reports.php资源的命令注入漏洞进行了利用。攻击者使用偷来的凭证执行了恶意命令，创建了一个名为help.php的Web Shell在CSA webroot文件夹下的/gsb目录中，从而在网络中建立了一个持久的访问点。研究人员还观察到攻击者在入侵过程中使用了多种战术和技术，包括横向移动、创建多个Web Shell、进行暴力破解攻击，以及尝试部署Linux内核对象（KO）模块形式的rootkit以维持内核级持久性。这些行为表明攻击者不仅具备高超的技术能力，而且拥有精心策划的攻击策略。

此外，攻击者在Ivanti发布CVE-2024-8190的补丁后，还在受害者网络中“修补”了/gsb/DateTimeTab.php和/gsb/reports.php资源的命令注入漏洞，阻止其他攻击者利用这些漏洞。这种自我修补的行为在历史上曾被观察到，攻击者在利用漏洞后进行修补，以防止其他入侵者干扰他们的攻击操作。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPl6zibvuUU9q8icUhrKU0f9Ok44iaFKWFUtcfQnichDb8TXtQpicMMKF9brX77cfvI8zicQeJsFhARgR4g/640?wx_fmt=png&from=appmsg)

图 1 解密base64 blob

参考链接：

https://www.fortinet.com/blog/threat-research/burning-zero-days-suspected-nation-state-adversary-targets-ivanti-csa

**APT34组织针对阿联酋和海湾地区展开网络攻击**

趋势科技（Trend Micro）的研究团队近日揭露了一起由网络间谍组织Earth Simnavaz发起的针对阿联酋和海湾地区的高级持续性威胁（APT）攻击。该组织也被称为APT34和OilRig，其攻击目标主要集中在能源部门，尤其是石油和天然气行业，以及其他关键基础设施。

Earth Simnavaz的攻击行动涉及一系列复杂的战术和技术。攻击者首先通过上传Web Shell至易受攻击的Web服务器来获得初始访问权限。这一Web Shell不仅能够执行PowerShell代码，还能下载和上传文件，使得攻击者能够在目标网络内扩展其控制范围。随后，攻击者利用了Windows Kernel Elevation of Privilege漏洞（CVE-2024-30088）进行权限提升，通过开源工具RunPE-In-Memory将exploit binary加载到内存中，注册密码过滤器DLL，并部署后门以通过Exchange服务器外泄敏感数据。此外，攻击者还滥用密码过滤器策略来获取凭证，并通过电子邮件将这些凭证外泄。攻击者进一步利用了一个名为STEALHOOK的后门工具，该工具通过检索有效的域凭证来访问Exchange服务器，并将敏感数据作为电子邮件附件发送到攻击者控制的邮箱地址。此外，攻击者还使用了远程监控和管理（RMM）工具，如ngrok，来创建从本地机器到互联网的安全隧道，绕过防火墙和网络安全控制，从而进行恶意通信和数据外泄。

此次攻击的归因分析显示，Earth Simnavaz与之前报告中的活动有显著的代码和功能相似性，这进一步证实了该组织对中东国家和政府实体的持续关注。此次行动中的Exchange后门与之前活动中观察到的后门存在显著相似性，攻击者利用这些工具通过Exchange服务器中继通信。趋势科技的研究表明，Earth Simnavaz等伊朗APT组织在中东地区，尤其是海湾地区的政府部门的活动日益频繁。这些组织的目标是建立持久的存在，并利用受影响的基础设施对其他目标发起进一步攻击。其主要目标似乎是间谍活动和窃取敏感的政府信息。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPl6zibvuUU9q8icUhrKU0f9OZqTnlLATibx5FVCibDaTibPpyd2Sicq4tUTv7ibzgu4bnOMlFhJF0gwIKeA/640?wx_fmt=png&from=appmsg)

图 2 Earth Simnavaz组织攻击链

参考链接：

https://www.trendmicro.com/en\_us/research/24/j/earth-simnavaz-cyberattacks-uae-gulf-regions.html

**Water Makara组织利用Astaroth恶意软件针对巴西展开攻击**

趋势科技的研究人员最近揭露了一个名为Water Makara的攻击组织的恶意活动激增。该组织针对巴西的企业，使用混淆的JavaScript来部署银行恶意软件，以绕过安全防御。这些鱼叉式网络钓鱼活动主要针对拉丁美洲的公司，特别是巴西的组织。受影响的行业包括制造公司、零售企业和政府机构。恶意电子邮件通常伪装成官方税务文件，利用个人所得税申报的紧迫性诱骗用户下载恶意软件。

攻击链始于一封设计得看似合法可信的鱼叉式网络钓鱼电子邮件，通常冒充知名组织或官方实体。这种常见的社会工程学策略可能会诱使收件人下载恶意的 ZIP附件。ZIP文件包含一个恶意的LNK文件，当用户执行LNK文件时，会运行嵌入的恶意JavaScript命令。在这次活动中，ZIP文件中还包含另一个具有类似混淆JavaScript命令的文件。最初，这些文件是Base64编码的，解码后揭示了隐藏的恶意脚本。通过将恶意代码嵌入到看似良性的文件中，攻击者诱骗用户执行恶意负载。此外，ZIP文件中还包含多个变体或文件扩展名，包括.pdf、.jpg、.png、.gif、.mov和.mp4。研究人员分析了LNK文件中的命令序列，这些命令用于执行LNK文件中隐藏的恶意JavaScript。每个命令都扮演特定的角色，共同促成了攻击的整体执行。混淆的JavaScript命令通过 unescape字符串解码，解码后的命令显示了一个恶意URL。使用GetObject函数的企图表明攻击者试图执行或检索一个可能引发其他恶意行为的对象。

这些URL共享几个相似的模式。例如，URLs包含域名 patrimonialsoberano.world，表明它们属于同一个域但可能指向该域内的不同子域或路径。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPl6zibvuUU9q8icUhrKU0f9O2nvmj49FJE8SicQtfnxaNVslLvTd8LF9u3Xc1VicO5ds4ARFFVl08J6g/640?wx_fmt=png&from=appmsg)

图 3 恶意软件感染链

参考链接：

https://www.trendmicro.com/en\_us/research/24/j/water-makara-uses-obfuscated-javascript-in-spear-phishing-campai.html

攻击活动

**俄罗斯法院网站遭受亲乌克兰黑客团体攻击导致服务中断**

俄罗斯普通管辖法院的网站在遭受一次网络攻击后已连续几天无法访问，此次攻击由一个支持乌克兰的黑客团体宣称负责。目前，这些网站显示错误信息。攻击者在Telegram上泄露了一份文件，该文件似乎是俄罗斯司法当局报告的一起涉及“Pravosudiye”（俄语中意为“正义”）案件管理系统和电子法院提交系统的事件。该系统被大多数俄罗斯法院使用，因此此次攻击影响广泛，不仅使使用“arbitr.ru”和“sudrf.ru”域名的俄罗斯联邦仲裁和普通管辖法院网站下线，还影响了它们的通信网络和电子邮件服务。

泄露的文件显示，受影响的服务预计至少在10月18日之前无法恢复，这距离事件发生已近两周。几家俄罗斯媒体从司法机构的消息人士那里获得了相同的文件，并证实了其真实性。此次攻击是由支持乌克兰的黑客团体BO Team宣称负责的，该团体以与乌克兰军事情报部门合作对俄罗斯进行多次行动而闻名，包括对俄罗斯主要电信供应商的子公司、一个科研中心和俄罗斯企业使用的数字签名认证联邦机构的攻击。

BO Team在Telegram上发布了其他似乎是来自Pravosudiye系统的信息，包括电子邮件和文件。与其他BO Team行动不同，乌克兰军事情报部门尚未公开声称与当前事件有任何关联。对俄罗斯法院的攻击发生在俄罗斯国家电视台和广播公司VGTRK遭受克里姆林宫描述为“前所未有”的网络攻击的同一天，该攻击也由支持乌克兰的黑客宣称负责。

由于VGTRK黑客事件的媒体关注度，Pravosudiye的攻击被忽视，最初被归因于“未计划的技术工作”。莫斯科普通管辖法院的官方Telegram频道表示，法院网站因数据中心的“技术故障”而下线。对Pravosudiye的攻击只是针对俄罗斯的一系列事件之一，这是其与乌克兰持续网络战的一部分。上周五，乌克兰军事情报部门宣布，他们黑客攻击了培训无人机操作员、数字通信专家、工程师和物理学家的俄罗斯大学系统。作为行动的结果，乌克兰成功破坏了大学的内部基础设施，包括其网站、数据库和文件存储系统，并销毁了150太字节的数据。这些信息无法独立验证。

参考链接：

https://therecord.media/russian-court-websites-down-attack-claimed-pro-ukraine-group

#

数据泄露

**丹麦体育模拟器公司TrackMan泄露110TB用户数据**

Cybernews接到信息，丹麦运动技术公司TrackMan不慎暴露了一个包含31,602,260条敏感数据记录的110TB公开可访问数据库。网络安全研究员Jeremiah Fowler发现了此次数据泄露。

* 泄露的数据包括：
* 用户姓名
* 电子邮件地址
* 服务信息，包括全球唯一标识符（GUID）
* 无线网络和设备硬件信息
* IP地址
* 摄像头日志详情
* 安全令牌

TrackMan是一款流行的体育软件提供商，专注于通过数据分析提升高尔夫和棒球等运动的表现。它提供订阅软件、室内高尔夫模拟器以及用于测量球杆速度、球速和旋转率的发射监视器等设备。该公司的系统使用多普勒雷达和成像技术详细追踪球的飞行和球员移动。TrackMan的技术也用于广播中，提供图形和统计数据以增强观众体验。此次截图显示了远程摄像头日志详情，包括API、IP地址和安全令牌。该公司的体育分析工具支持性能分析、教练和球员发展，业余和专业体育代表均使用这些工具。

参考链接：

https://cybernews.com/security/trackman-data-leak/

**《精灵宝可梦》开发商Game Freak遭受数据泄露**

日本著名视频游戏开发商Game Freak Inc.，也是广受欢迎的《精灵宝可梦》系列游戏的主要开发商，近日确认在8月份遭受了一起网络攻击，导致公司服务器遭到未经授权的访问，源代码和未发布游戏的设计图被泄露到了网上。

此次泄露的内容包括《精灵宝可梦》游戏的源代码、开发构建版本，以及未公布的游戏艺术作品和设计文档。这些敏感信息在包括Discord、Reddit和X等多个社交媒体平台上被公开。Game Freak在一份声明中表示，公司在2024年8月遭受了未经授权的服务器访问，导致员工和其他人（包括员工、承包商和退休人员）的个人信息被泄露。泄露的数据包括2,606名个体的个人数据（姓名和公司电子邮件地址）。

公司表示，正在与受影响的员工和其他人单独联系，并为那些已经退休或无法单独联系的人通过公告和设立咨询窗口来通知他们。Game Freak还表示，尽管已经重建和重新检查了服务器，但公司将继续加强安全措施，以防止此类事件再次发生。目前，Game Freak并未发现此次网络攻击对《精灵宝可梦》玩家数据产生影响，也没有威胁行为者声称对此次网络攻击负责。

值得注意的是，这并非《精灵宝可梦》系列相关公司首次遭受数据泄露。2020年，任天堂——《精灵宝可梦》系列的另一合作方——也遭受了数据泄露，攻击者泄露了源代码、内部文件和开发工具。当时，攻击者访问了30万个账户，获取了包括生日和电子邮件地址在内的个人信息，但财务数据未受影响。

参考链接：

https://securityaffairs.com/169817/data-breach/game-freak-data-breach.html

恶意软件

**新型Linux变种FASTCash恶意软件瞄准金融系统**

网络安全研究人员最近分析了一种新型的FASTCash恶意软件变种，该变种专门针对Linux系统。此变种之前未知，主要针对Ubuntu 22.04 LTS发行版。

2018年11月，赛门铁克首次发现了FASTCash木马，该木马被与朝鲜有关的APT组织Lazarus用于一系列针对ATM的攻击。专家表示，自2016年以来，该APT组织至少一直在使用此恶意软件，从亚洲和非洲的中小型银行的ATM中非法转移了数百万美元。研究人员发表的分析报告中提到：“'FASTCash'一词指的是归因于朝鲜的恶意软件，该软件安装在处理卡片交易的支付开关上，以促进未经授权的从ATM取款。”

此前的FASTCash恶意软件变种针对的是IBM AIX（FASTCash for UNIX）和微软Windows（FASTCash for Windows）。2018年10月，美国计算机应急响应团队（US-CERT）发布了来自国土安全部（DHS）、联邦调查局（FBI）和财政部的联合技术警报，警告称由臭名昭著的朝鲜APT黑客组织Hidden Cobra（也称为Lazarus Group和Guardians of Peace）使用的ATM现金盗窃计划“FASTCash”。这种之前未被检测到的Linux变种于2023年6月首次提交给VirusTotal，但很可能是在2022年4月后为Ubuntu 20.04开发的VMware VM上开发的。恶意代码拦截被拒绝的磁性刷卡交易，并为特定持卡人账户授权以土耳其里拉的随机金额。

恶意代码显示出与以前的Windows和AIX变种有多个相似之处。FASTCash Linux变种被实现为一个共享库，通过‘ptrace’系统调用注入到支付开关服务器中，拦截ISO8583交易消息。恶意软件特别拦截“拒绝”响应，用于资金不足，然后将其修改为“批准”，从而在ATM和销售点终端上启用未经授权的交易。每笔欺诈性交易生成的随机资金金额范围在12,000至30,000土耳其里拉之间。

分析继续说：“与Windows前身相比，Linux变种的功能略有减少，尽管它仍然保留了关键功能：拦截预定义的持卡人账户号码列表的已拒绝（磁性刷卡）交易消息，然后以土耳其里拉的随机金额授权交易。”一旦交易消息被修改为显示批准代码和金额，银行就会授权交易，允许钱骡代表威胁者从ATM取款。

参考链接：

https://securityaffairs.com/169860/malware/new-linux-variant-fastcash-malware-targets-financial-systems.html

**银行木马TrickMo攻陷13000台设备**

Zimperium的安全研究人员近期发布了对TrickMo最新样本的深入分析，揭示了这一银行木马的令人担忧的新能力。TrickMo最初由Cleafy在9月初披露，该变种采用了旨在逃避检测和分析的技术，包括混淆和压缩文件操作。研究人员识别出惊人的40种TrickMo变体，包括16个投放器和22个活跃的命令与控制（C2）服务器，其中许多仍未被更广泛的安全社区检测到。

尽管TrickMo的核心能力仍然集中在银行凭证盗窃上，但研究人员的分析发现了更高级的功能。这些能力使恶意软件能够有效访问设备上存储的任何类型的信息，包括一次性密码（OTP）拦截、屏幕录制、远程控制、数据泄露以及滥用辅助功能在未经用户同意的情况下自动授权和执行操作。此外，TrickMo可以显示欺骗性覆盖层以窃取凭证并促进未经授权的金融交易。

研究人员分析中最令人担忧的发现之一是TrickMo的一些变种中新发现的功能：窃取设备的解锁...