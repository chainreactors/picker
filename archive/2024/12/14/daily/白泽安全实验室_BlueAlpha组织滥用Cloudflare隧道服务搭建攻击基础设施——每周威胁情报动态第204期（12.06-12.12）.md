---
title: BlueAlpha组织滥用Cloudflare隧道服务搭建攻击基础设施——每周威胁情报动态第204期（12.06-12.12）
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492463&idx=1&sn=e61375f68d33fac1c00911454ed6cd95&chksm=e90dc945de7a40537fc4a981bc0fb0565e22cb3989574df5ce9c5f9e0680ad75f91238bfda9e&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-12-14
fetch_date: 2025-10-06T19:41:51.529748
---

# BlueAlpha组织滥用Cloudflare隧道服务搭建攻击基础设施——每周威胁情报动态第204期（12.06-12.12）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMINeYG0xg4btBInpvgswiaLDvMezqC0jzMYgNaiagu4ktmbPMeMNPegmKe7JaecHMuibo8tvBd5w2ZUOw/0?wx_fmt=jpeg)

# BlueAlpha组织滥用Cloudflare隧道服务搭建攻击基础设施——每周威胁情报动态第204期（12.06-12.12）

原创

BaizeSec

白泽安全实验室

APT攻击

###

* ###

  ### BlueAlpha组织滥用Cloudflare隧道服务搭建攻击基础设施
* ###

  ###

  ###

  ### TA4557/FIN6组织利用“卓越简历”诱饵文档发起网络攻击

攻击活动

* ###

  ###

  ###

  ### 罗马尼亚选举系统在总统选举前遭受85,000次攻击

数据泄露

* ###

  ###

  ###

  ### 美国数据中介SL Data Services遭受大规模数据泄露
* ### 印度AI聊天机器人公司WotNot泄露34.6万份敏感文件

恶意软件

* ###

  ###

  ###

  ### MoqHao恶意软件利用iCloud和VK平台针对Apple和Android设备攻击
* ### DroidBot新型安卓木马威胁全球金融机构

勒索软件

* ###

  ###

  ### "Termite"勒索软件组织疑似利用Cleo软件0day漏洞发起攻击
* ### Black Basta勒索软件组织利用MS Teams和电子邮件轰炸传播恶意软件
* ###

  ### 罗马尼亚能源巨头Electrica Group遭受勒索软件攻击

APT攻击

### **BlueAlpha组织滥用Cloudflare隧道服务搭建攻击基础设施**

俄罗斯联邦安全局（FSB）支持的网络威胁组织BlueAlpha，与Gamaredon、Shuckworm、Hive0051和UNC530等组织重叠，自2014年以来一直活跃，主要通过鱼叉式网络钓鱼活动针对乌克兰组织分发定制恶意软件。自2023年10月以来，该组织一直在传递GammaLoad恶意软件，这是一种定制的VBScript恶意软件，能够实现数据泄露、凭证盗窃和对被妥协网络的持久访问。最近，BlueAlpha进一步发展了其恶意软件传递链，利用Cloudflare隧道服务为GammaDrop恶意软件搭建攻击基础设施，这是一种网络犯罪团伙广泛使用的策略。

BlueAlpha组织利用Cloudflare的免费隧道服务TryCloudflare工具，创建隧道并使用trycloudflare.com的随机生成子域名，将所有请求通过Cloudflare网络代理到攻击者控制的Web服务器，以隐藏其GammaDrop的攻击基础设施。此外，该组织通过HTML走私技术，利用嵌入式JavaScript在HTML附件中传递恶意软件，并通过复杂的技术绕过电子邮件安全系统。BlueAlpha的恶意软件套件包括GammaDrop和GammaLoad，其中GammaDrop作为投递器，将GammaLoad写入磁盘并确保其持久性，而GammaLoad则能够向其C2发出信标并执行额外的恶意软件。BlueAlpha使用大量垃圾代码和随机变量名等混淆技术，以复杂化恶意软件分析。

参考链接：

https://malware.news/t/bluealpha-abuses-cloudflare-tunneling-service-for-gammadrop-staging-infrastructure/89062

### **TA4557/FIN6组织利用“卓越简历”诱饵文档发起网络攻击**

在2024年3月，一起由TA4557/FIN6组织发起的复杂网络攻击活动被曝光。攻击者通过发送带有恶意简历的电子邮件诱饵，成功感染了一个用户端点，并进一步横向移动到环境中的两台服务器。攻击者利用了多种技术来逃避检测和增强持久性，包括滥用LOLbins（如ie4uinit.exe和msxsl.exe）来执行恶意操作，使用Cobalt Strike和基于Python的C2 Pyramid进行后期利用活动，以及利用CVE-2023-27532漏洞来促进横向移动和权限提升。此外，攻击者还安装了Cloudflared以协助隧道RDP流量，增强隐蔽性。

攻击活动始于一个看似无害的电子邮件，其中包含一个指向在线简历网站的链接。受害者下载并执行了假的简历压缩文件中的恶意.lnk文件，触发了一系列的恶意操作。攻击者首先使用ie4uinit.exe侧加载恶意.inf文件，然后通过WMI执行恶意DLL，创建了计划任务，并最终加载了more\_eggs恶意软件，建立了与命令和控制服务器的通信。在后期利用活动中，攻击者部署了Cobalt Strike Beacon，并使用了vssadmin工具创建影子副本，可能用于访问凭证。攻击者还使用了SharpShares和Seatbelt等工具进行主机和环境枚举，并尝试部署Pyramid C2，尽管其活动和通信较少。攻击者还利用了Veeam服务器的CVE-2023-27532漏洞，创建了新的本地管理员账户，并通过RDP连接到备份服务器。在备份服务器上，攻击者部署了Cobalt Strike payload并继续进行发现活动。这起事件揭示了TA4557/FIN6组织如何利用社会工程学和漏洞利用技术进行复杂的网络攻击。攻击者展示了其在逃避检测、横向移动和权限提升方面的高级能力。这一事件强调了组织必须投资于先进的检测和响应能力，以对抗这些复杂的威胁。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPnHjSqWLEKFSRFja5gib9P2CVZib2NYCVHJm9JXfVg9ppcthcWoCmhIUGCJwicLmZ7ibP1EPbMrpgDVg/640?wx_fmt=png&from=appmsg)图 1 攻击流程示意图

参考链接：

https://thedfirreport.com/2024/12/02/the-curious-case-of-an-egg-cellent-resume/

攻击活动

### **罗马尼亚选举系统在总统选举前遭受85,000次攻击**

罗马尼亚最新披露，该国选举系统在即将举行的总统选举前遭受了超过85,000次网络攻击，这些攻击导致了与选举相关的网站凭证被泄露在俄罗斯的网络犯罪论坛上。据路透社报道，这些访问数据可能是通过针对合法用户或利用合法培训服务器获得的。罗马尼亚情报部门表示，这些攻击旨在利用系统漏洞，而莫斯科方面否认对罗马尼亚选举系统发动任何攻击。

罗马尼亚情报部门在一份解密文件中指出，攻击在选举日及选举后的夜间持续密集发生，其操作模式和规模表明攻击者拥有特定于攻击国家的相当资源。文件还显示，亲俄总统候选人Calin Georgescu在TikTok上通过协调账户和付费广告被“积极”推广，这引发了对其胜选的怀疑。

2024年12月6日，罗马尼亚宪法法院以宪法第146条(f)款为依据，因担忧公平性和合法性问题，一致决定取消整个总统选举过程，并要求政府设定新的选举日期和相应的行动计划。罗马尼亚情报机构警告称，该国选举系统仍然脆弱，威胁行为者可能会再次对其进行破坏。

据研究人员报道发现了攻击者从超过33个国家发起了SQL注入和XSS攻击。此外，还有报告发现了一场影响力活动，其中超过100名拥有800万以上追随者的罗马尼亚TikTok影响者被付费推广亲俄候选人Calin Georgescu。罗马尼亚外国情报服务(SIE)认为，俄罗斯将罗马尼亚作为影响东欧民主选举的更广泛努力的一部分，尽管俄罗斯在最近对罗马尼亚的攻击和活动中的直接作用没有得到明确确认。

参考链接：

https://securityaffairs.com/171758/cyber-warfare-2/romanias-election-systems-hit-by-85000-attacks.html

###

#

数据泄露

### **美国数据中介SL Data Services遭受大规模数据泄露**

美国数据中介SL Data Services近期遭受了一起严重的数据泄露事件，导致644,869个个人PDF文件在互联网上曝光。这些泄露的记录包含了个人详细信息、车辆记录、财产所有权文件、背景调查和法庭记录等敏感信息，且这些文件未经过加密或密码保护。网络安全专家Jeremiah Fowler发现了此次泄露，并在713.1 GB的数据库中识别出了样本记录，其中95%的文件被标记为“背景调查”。这些信息提供了个人的完整档案，引发了潜在的隐私问题。泄露的文件包含了居住地址、联系方式、就业数据、姓名、社交媒体账户、家庭成员和犯罪记录历史等敏感信息。Fowler确认了泄露文件中与被命名个人相关的居住地址的准确性。泄露发生的原因是因为SL Data Services的财产报告存储在一个可通过Web门户访问的数据库中，攻击者通过已知的文件路径访问了这些文件。该公司使用单一数据库为多个域名提供服务，且没有适当的数据隔离措施。在Fowler报告泄露事件后，数据库访问被封锁了一周，但在这段时间内，又有超过150,000条记录被暴露。当Fowler联系SL Data Services时，他只能接触到呼叫中心的代理，他们否认了泄露事件，并声称他们的系统使用了SSL和128位加密。然而，暴露的记录表明数据安全实践存在严重漏洞。泄露的信息可能会导致犯罪分子利用关于家庭成员、就业或刑事案件的信息来获取更多的敏感个人信息、财务数据或其他隐私威胁。公开暴露的数据使威胁行为者能够发起网络钓鱼活动或社会工程攻击、使用被盗信息伪造身份，或针对背景调查文件中出现的数据的目标受害者。

参考链接：

https://www.cysecurity.news/2024/12/database-service-provider-leak-results.html

### **印度AI聊天机器人公司WotNot泄露34.6万份敏感文件**

印度AI聊天机器人初创公司WotNot因一个配置错误的Google Cloud Storage存储桶，不慎泄露了近35万份敏感文件。

这些文件包括：

* 护照扫描件；
* 身份证明文件；
* 医疗记录；
* 简历；
* 旅行行程等。

这一安全漏洞在2024年8月27日被Cybernews的研究人员发现，涉及的文件对互联网上任何人都开放访问，无需密码。考虑到泄露信息的性质，这些数据足以使网络犯罪分子轻易实施身份盗窃。Cybernews在9月9日尝试通知WotNot此问题，并在多次发送跟进邮件后，公司花了两个多月时间才修复这一安全漏洞。WotNot解释称，泄露的存储桶被其服务的免费层用户使用，由于云存储桶策略被修改以适应特定用例，却未能彻底验证其可访问性，导致数据暴露。尽管WotNot向其企业客户保证，他们的数据未受此次安全漏洞影响，但这一事件仍然引发了对非付费用户隐私保护不足的担忧。

参考链接：

https://www.bitdefender.com/en-us/blog/hotforsecurity/ai-chatbot-startup-wotnot-leaks-346-000-files-including-passports-and-medical-records

恶意软件

### **MoqHao恶意软件利用iCloud和VK平台针对Apple和Android设备攻击**

最近，研究人员发现了与Roaming Mantis有关联的MoqHao恶意软件家族（也称为Wroba和XLoader）的新活动。这一活动利用了苹果iCloud和俄罗斯社交媒体服务VK等受信任的平台，通过复杂的网络钓鱼和恶意软件分发手段，针对Android和iOS用户。攻击始于一条看似无害的日文短信，声称有投递失败的尝试，并将收件人指向一个在X/Twitter上托管的短链接。短信显示出语言上的不一致性，暗示了其欺诈性质。点击链接后，用户被重定向到根据其设备类型定制的网络钓鱼页面，要么模仿iOS用户的Apple ID登录门户，要么为Android设备提供恶意APK文件。攻击者展示了其基础设施的高水平复杂性。当iOS用户访问链接时，他们被引导至一个本地化的网络钓鱼页面，这些页面使用特定区域的URL。这些假冒的Apple ID登录页面旨在通过首先拒绝用户的初始密码尝试来收集凭证，制造合法性的假象。对于Android用户，攻击活动分发了名为Chrome\_up1732156036129.apk的文件，伪装成Google Chrome更新。这个APK被VirusTotal上的多个供应商标记，直接从苹果的合法iCloud基础设施下载，攻击者滥用了这一点来托管恶意软件。为了进一步掩盖其操作，攻击者依赖于动态DNS服务（如DuckDNS）和中介平台（如VK）。命令和控制（C2）地址编码在VK用户资料中，作为中介以掩盖C2服务器的真实位置。这种多层次的方法，结合了受信任的平台和一次性域名，使得检测和归属更加困难。MoqHao的操作者已经调整了他们的技术以逃避安全措施。从使用苹果的iCloud进行恶意软件分发到利用VK进行C2通信，他们展示了网络犯罪活动日益增长的复杂性。通过使用多个托管提供商和动态DNS子域，他们确保了即使特定域名被标记或关闭，其基础设施的弹性。

参考链接：

https://securityonline.info/moqhao-malware-targets-apple-ids-and-android-devices-using-icloud-and-vk-platforms/

### **DroidBot新型安卓木马威胁全球金融机构**

Cleafy Threat Intelligence and Response (TIR)团队近期披露了一个名为DroidBot的新型安卓远程访问木马（RAT），该木马与土耳其的一个新兴恶意软件即服务（MaaS）行动有关。DroidBot以其先进的功能和针对欧洲、拉丁美洲的银行机构、加密货币交易所和国家组织的积极活动，标志着移动恶意软件威胁的重大升级。DroidBot首次于2024年6月被检测到，它结合了包括隐藏VNC、叠加攻击和类似间谍软件的键盘记录等高级功能，使其成为设备欺诈的强大工具。该恶意软件采用双通道通信，使用MQTT进行数据外发和HTTPS接收命令，确保了灵活性和弹性。DroidBot目前针对英国、意大利、法国、西班牙和葡萄牙等国家的77个实体，有迹象表明其正在扩展到拉丁美洲。与传统的恶意软件活动不同，DroidBot作为MaaS运营，允许合作伙伴通过订阅模式访问其能力。每个合作伙伴都被分配了独特的标识符，一个Telegram频道以每月3000美元的费用广告DroidBot的功能。

DroidBot通过社交工程手段进行分发，伪装成合法的安全或银行应用。它滥用安卓辅助服务执行恶意行为，包括键盘记录、叠加攻击、类似VNC的例程和远程控制，使攻击者能够模拟用户交互和操纵设备。DroidBot利用MQTT为其命令与控制（C2）基础设施，这是一种通常在物联网系统中使用的协议。这种非传统的选择有助于逃避检测并增强操作弹性。Cleafy的分析显示，DroidBot仍在积极开发中，其样本中存在占位符功能和不同程度的混淆。证据表明，其开发者是土耳其语使用者，并且为英语、意大利语、西班牙语和土耳其语用户提供了本地化。DroidBot对金融机构和高价值目标构成了重大威胁，其运营模式提升了监控和防御此类攻击的规模和复杂性。Cleafy警告称，这种新的分发和合作模式将把攻击面的监控提升到一个全新的水平。

参考链接：

https://securityonline.info/droidbot-a-new-android-threat-exposes-global-financial-institutions/

勒索软件

###

### **"Termite"勒索软件组织疑似利用Cleo软件0day漏洞发起攻击**

近期，Cleo软件的LexiCom、VLTransfer和Harmony产品被曝存在零日漏洞，而"Termite"勒索软件团伙可能是此次攻击的幕后黑手。这一漏洞允许未经认证的远程代码执行（RCE），Cleo曾在10月份披露此漏洞并发布了修复版本5.8.0.21，但最新的情报显示，即使应用了该补丁的系统仍然面临被利用的风险。攻击活动始于2024年12月3日，至今已有至少10个不同行业的受害者，包括消费品、货运和航运以及食品工业。安全研究人员通过搜索互联网上暴露的易受攻击的Cleo系统推测，实际受害者数量可能更高。Rapid7也收到了涉及Cleo漏洞的妥协和后利用活动的多起报告，并建议受影响组织采取“紧急行动”以降低风险。Cleo软件被广泛应用于物流、交通、制造业和批发分销等多个行业，包括Brother、New Balance、Duraflame、TaylorMade、Barilla America和Mohawk Global等知名企业。Huntress Labs的安全研究人员指出，尽管Cleo已经发布了针对CVE-2024-50623漏洞的补丁，但所有先前受影响的版本，包括打了补丁的5.8.0.21，仍然容易受到攻击。Huntress Labs强烈建议将任何暴露在互联网上的Cleo系统置于防火墙之后，直到发布新的补丁。Cleo已经承认了这一问题，并计划发布新的CVE标识符。公司发言人在声明中强调了这一漏洞的严重性，并已通知客户有关威胁，同时提供了在补丁可用之前减轻风险的建议。Cleo鼓励客户定期检查其安全公告网页以获取最新信息。Huntress Labs的分析显示，攻击者在被妥协的端点上部署了类似Web shell的功能以建立持久性，并使用nltest.exe和其他域侦察工具枚举潜在的Active Directory资产。Huntress的敌对战术总监Jamie Levy表示，有证据指向"Termite"是此次攻击的实施者，且"Termite"可能与已知的勒索软件团伙Cl0p有关联。

### 参考链接：

https://www.darkreading.com/cyberattacks-data-breaches/termite-ransomware-behind-cleo-zero-day-attacks

### **Black Basta勒索软件组织利用MS Teams和电子邮件轰炸传播恶意软件**

网络安全厂商Rapid7的研究人员发现了Black Basta勒索软件组织（也称为UNC4393）发起的复杂社会工程攻击活动，该组织通过电子邮件轰炸和Microsoft Teams冒充IT支持人员，诱骗受害者授予远程访问权限，从而传播恶意软件。攻击者利用Azure/Entr...