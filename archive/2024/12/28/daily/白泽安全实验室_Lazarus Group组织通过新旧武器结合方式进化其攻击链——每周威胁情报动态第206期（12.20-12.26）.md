---
title: Lazarus Group组织通过新旧武器结合方式进化其攻击链——每周威胁情报动态第206期（12.20-12.26）
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492492&idx=1&sn=c5c0b62dc41c3ba27eda381ed20edd0a&chksm=e90dc9a6de7a40b07a41e81222cef34c8a281335f2f1ee0f12ba75f7d1edc2c049302a56c31f&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-12-28
fetch_date: 2025-10-06T19:40:06.769222
---

# Lazarus Group组织通过新旧武器结合方式进化其攻击链——每周威胁情报动态第206期（12.20-12.26）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMINeYG0xg4btBInpvgswiaLDvMezqC0jzMYgNaiagu4ktmbPMeMNPegmKe7JaecHMuibo8tvBd5w2ZUOw/0?wx_fmt=jpeg)

# Lazarus Group组织通过新旧武器结合方式进化其攻击链——每周威胁情报动态第206期（12.20-12.26）

原创

BaizeSec

白泽安全实验室

APT攻击

###

* ###

  ###

  ###

  ### Lazarus Group组织通过新旧武器结合方式进化其攻击链
* ###

  ###

  ###

  ###

  ###

  ### Charming Kitten APT组织使用新型C++编写的BellaCiao恶意软件变种
* ### Cloud Atlas组织在攻击活动中采用新型后门程序

攻击活动

* ### 黑客组织Diicot发起针对Linux系统的高级恶意软件攻击活动
* ### Cicada 3301黑客组织宣称对标致汽车经销商数据泄露事件负责

数据泄露

* ###

  ###

  ###

  ###

  ###

  ### Postman Workspaces 数据泄露事件暴露3万敏感API密钥和令牌
* ###

  ###

  ### Builder.ai数据库配置失误导致1.29TB敏感数据暴露

恶意软件

* ###

  ###

  ###

  ###

  ###

  ### 基于Python的NodeStealer恶意软件针对Facebook广告管理器展开攻击

勒索软件

* ###

  ###

  ###

  ###

  ### RansomHub勒索软件的攻击感染链和技术细节分析
* ###

  ###

  ### 知名医疗保健企业遭受勒索软件攻击，近600万患者信息泄露

APT攻击

### **Lazarus Group组织通过新旧武器结合方式进化其攻击链**

近期，研究人员观察到该APT组织通过假工作机会针对不同行业的员工（包括国防、航空、加密货币等全球行业）分发恶意软件的行为，这一攻击活动被称为“DeathNote 活动”，也被称为“Operation DreamJob”。最新研究揭示了Lazarus组织如何通过结合新旧攻击武器样本来定制其攻击，展示了其攻击感染链的重大变化。

Lazarus组织的攻击策略包括发送恶意文档或木马化的PDF查看器，以及分发木马化的远程访问工具，如VNC或PuTTY，以诱使目标连接到特定服务器进行技能评估。最近发现的案例属于后者，但除了初始向量外，攻击感染链已完全改变。

研究人员在最近发现的攻击案例中，目标收到了至少三个与IT职位技能评估相关的归档文件，这些文件据称与知名的航空和国防公司有关。研究人员确定其中两个实例涉及木马化的VNC实用程序。Lazarus组织向同一组织内的至少两个人（可以称为主机A和主机B）发送了第一个归档文件。一个月后，他们对第一个目标进行了更密集的攻击。

恶意软件分析：

* AmazonVNC.exe：

这是一个木马化的TightVNC版本，允许任何人编辑原始源代码。当目标执行AmazonVNC.exe时，会弹出一个窗口，要求输入存储在readme.txt文件中的IP地址和密码。一旦输入IP，就会生成一个XOR密钥，用于解密VNC可执行文件的内部资源并解压数据。解压后的数据实际上是被称之为Ranid Downloader的下载器，由AmazonVNC.exe加载到内存中以执行进一步的恶意操作。

* CookieTime：

这是另一种在受感染主机上发现的恶意软件。虽然不确定CookieTime如何被传递给主机A，但它在安装LPEClient后作为SQLExplorer服务执行。CookieTime最初通过直接从C2服务器接收和执行命令来运作，但最近它被用来下载有效载荷。

* CookiePlus：

这是一个新发现的基于插件的恶意程序，最初由ServiceChanger和Charamel Loader加载。CookiePlus能够从内部资源和外部文件（如 msado.inc）中获取C2列表，表明它具有从多个来源获取C2信息的能力。

纵观其历史，Lazarus组织只使用了少数模块化恶意软件框架，如Mata和Gopuram Loader。引入这种类型的恶意软件对他们来说是一种不同寻常的策略。事实上，他们确实引入了新的模块化恶意软件，如CookiePlus，这表明该组织一直在努力改进他们的武器库和攻击感染链，以逃避安全产品的检测。防御侧的问题是，CookiePlus的行为就像一个下载者。这使得很难调查CookiePlus是只下载了一个小插件还是下一个有意义的有效负载。根据专家的分析，它似乎仍在积极开发中，这意味着Lazarus组织可能会在未来添加更多恶意插件。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMINmA5RxJxka1Fxo0wk17mib7e0WgrMC5OHgqxsVj16ZOEzrVczsOcaqiaXSAUvAVarG1vpZBK6FuzFA/640?wx_fmt=png&from=appmsg)图 1 在受害者的主机上创建的恶意文件

参考链接：

https://securelist.com/lazarus-new-malware/115059/

### **Charming Kitten APT组织使用新型C++编写的BellaCiao恶意软件变种**

Kaspersky的研究人员在最近的一次网络入侵事件中发现了一个新型的BellaCiao恶意软件变种，该变种被命名为BellaCPP。BellaCiao是一个基于.NET的恶意软件家族，以其隐蔽的持久性和建立秘密隧道的能力而闻名。自2023年4月以来，该恶意软件家族被公开归因于APT攻击组织Charming Kitten。

在对一台受感染计算机上的BellaCiao样本进行调查时，研究人员发现了另一个可疑且可能相关的样本。经过进一步调查，该样本被确认为BellaCiao的一个旧版本的C++重写版本。BellaCiao的PDB路径非常具有描述性，暴露了与活动相关的的重要信息，例如目标实体和国家。通过对历史样本的分析，研究人员发现所有PDB路径都包含字符串“MicrosoftAgentServices”。某些样本在该字符串后附加了一个数字，如“MicrosoftAgentServices2”和“MicrosoftAgentServices3”，这通常表示恶意软件开发者使用的版本控制，可能用于区分各种迭代或更新。

BellaCPP是一个DLL文件，名为“adhapl.dll”，在C:\Windows\System32中被发现。它有一个名为“ServiceMain”的导出函数，表明这个变种像原始的BellaCiao样本一样，被设计为作为Windows服务运行。代码执行了一系列步骤，与早期版本的BellaCiao中观察到的行为非常相似。

* 使用XOR加密和密钥0x7B解密三个字符串：

C:\Windows\System32\D3D12\_1core.dll

SecurityUpdate

CheckDNSRecords

* 加载在上一步解密路径中的DLL文件，并使用GetProcAddress解析上述两个其他解密字符串的函数。
* 按照与.NET BellaCiao版本相同的方法生成域名，格式如下：

<5随机字母><目标标识符>.<国家代码>.systemupdate.info

尽管研究人员未能检索到上述D3D12\_1core.dll文件，因此无法分析过程中触发的SecurityUpdate函数，但根据传递的参数和已知的BellaCiao功能，研究人员有中等信心认为缺失的DLL创建了一个SSH隧道。

研究人员基于以下要素，以中高信心评估BellaCPP与Charming Kitten APT组织有关：

* 从宏观角度来看，BellaCPP是BellaCiao样本的C++版本，但不包含webshell功能。
* 它使用了之前归因于该组织的域名。
* 它以类似的方式生成域名，并像观察到的.NET样本一样使用该域名。
* 在受感染的机器上发现了较旧的BellaCiao样本。

Charming Kitten一直在改进其恶意软件家族库，同时也利用公开可用的工具。他们不断更新的恶意软件家族之一是BellaCiao。从研究的角度来看，这个家族特别有趣，因为PDB路径有时会提供对预期目标及其环境的一些见解。BellaCPP样本的发现突显了对网络及其受控主机进行彻底检查的重要性。因为攻击者可以部署安全检测系统可能无法检测到的未知样本，从而在删除“已知”样本后还能在网络中保持立足点。

参考链接：

https://securelist.com/bellacpp-cpp-version-of-bellaciao/115087/

### **Cloud Atlas组织在攻击活动中采用新型后门程序**

近期，研究人员发现了Cloud Atlas APT组织的一项新攻击活动，该组织自2014年以来一直针对东欧和中亚地区。此次攻击活动中，Cloud Atlas使用了一个之前未被记录的工具集，该工具集在2024年被广泛使用。受害者通过包含恶意文档的钓鱼邮件被感染，这些文档利用公式编辑器中的漏洞（CVE-2018-0802）下载并执行恶意代码。

当受害者打开文档时，会从一个由攻击者控制的远程服务器下载一个恶意模板，该模板格式为RTF文件，并包含一个公式编辑器漏洞，用于下载并运行托管在同一C2服务器上的HTML应用程序（HTA）文件。RTF和HTA文件的下载被限制在特定的时间段和受害者IP地址，只有来自目标区域的请求才被允许。恶意HTA文件提取并写入多个文件到磁盘，这些文件是VBShower后门程序的一部分。VBShower随后下载并安装另一个后门：PowerShower。这种感染模式最初在2019年被描述，并且从那时起只发生了轻微变化。VBCloud后门现在复制了可执行文件的原始功能，例如下载和执行恶意插件、与云服务器通信以及执行其他任务。研究人员首次在去年8月检测到使用此植入的攻击。自那时以来，研究人员观察到了许多变种的后门，帮助它保持在雷达之下。这次新的活动通过VBShower加载VBCloud，VBShower还下载了PowerShower模块。PowerShower探测本地网络并促进进一步渗透，而VBCloud收集有关系统的信息并窃取文件。

技术细节：

* HTA：利用RTF模板下载HTA文件并运行它，利用NTFS ADS功能在%APPDATA%\Roaming\Microsoft\Windows\路径下提取和创建多个文件，这些文件构成了VBShower后门。
* VBShower：包括一个启动器（Launcher）、清理器（Cleaner）和后门（Backdoor），负责解密和运行后门的有效载荷，并在内存中执行一系列操作。
* PowerShower：功能上与VBShower几乎相同，下载额外的PowerShell脚本并执行它们。
* VBCloud：通过VBShower安装，使用公共云存储作为C2服务器，负责下载和运行PowerShell脚本，并发送输出到C2。

在2024年，有几十个用户遭到攻击，其中82%在俄罗斯。在白俄罗斯、加拿大、摩尔多瓦、以色列、吉尔吉斯斯坦、越南和土耳其也有零星攻击记录。研究人员继续监控与Cloud Atlas相关的活动。在2023年8月开始的新活动中，攻击者对他们熟悉的工具集进行了更改。这次，他们依赖VBShower后门作为加载器，而不是可执行库来加载恶意模块。此外，他们现在在攻击中使用了一个新模块：VBCloud。这表明攻击者不断更新其技术手段，以保持攻击的有效性和隐蔽性。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMINmA5RxJxka1Fxo0wk17mib7iaBzOYFoBY3YPW72Jt5c7jPssTUWtOaSHbcVKM1JlnWV49Gv9HcFjUg/640?wx_fmt=png&from=appmsg)图 2 典型的 Cloud Atlas 感染模式

参考链接：

https://securelist.com/cloud-atlas-attacks-with-new-backdoor-vbcloud/115103/

攻击活动

### **黑客组织Diicot发起针对Linux系统的高级恶意软件攻击活动**

最近研究人员发现了一起由罗马尼亚语黑客组织Diicot（也称为Mexals）发起的针对Linux系统的先进恶意软件攻击活动。这场活动不仅展示了该组织在技术上的显著进步，也对全球Linux用户和企业的安全构成了严重威胁。

Diicot组织此次的恶意软件攻击活动在多个层面上表现出了高度的复杂性。与以往的攻击相比，更新后的恶意软件显示出了显著的技术进步，包括新的命令和控制（C2）基础设施的引入、从基于Discord的C2向HTTP的过渡，以及Zephyr协议和Monero挖矿的采用。这些改进反映了攻击者在适应和完善战术上的能力。攻击者使用了改进的混淆技术，例如修改UPX头部以包含损坏的校验和，使得标准的解包工具无法有效工作。这种技术的进步表明，攻击者正在不断努力绕过现代安全措施并规避自动化检测。此外，恶意软件能够根据运行环境的不同调整其行为，这在云设置中尤为明显，恶意软件会优先传播到其他主机，而在传统环境中则部署加密货币挖矿有效载荷。

研究人员在调查中发现的恶意软件有效载荷包括Brute-Spreader、Reverse Shell (client.go)和SSH Banner Scanner。这些有效载荷使攻击者能够在网络中传播、保持持久性、获得对被妥协机器的完全远程控制，以及识别弱SSH凭证以获得初始访问权限。这场攻击活动对运行OpenSSH的Linux系统构成了重大风险，特别是那些凭证弱和安全设置配置不当的系统。Diicot组织的主要动机是加密货币挖矿，他们已经从Monero挖矿中赚取了超过16,000美元，并且可能从Zephyr协议中获得了更难以追踪的收入。这不仅给组织带来了财务损失，还面临着数据泄露、系统被破坏和潜在的运营中断风险。

参考链接：

https://securityonline.info/diicot-threat-group-targets-linux-with-advanced-malware-campaign/

### **Cicada 3301黑客组织宣称对标致汽车经销商数据泄露事件负责**

Cicada 3301黑客组织的最新行动再次将全球汽车行业置于聚光灯下。该组织宣称成功对标致汽车在法国的经销商网络进行了一次精心策划的网络攻击，窃取了高达40GB的敏感数据，并计划在2025年1月6日对外公布这些信息。这一行动不仅对标致汽车的商业运营和客户信任构成了直接威胁，也暴露了汽车行业在网络安全方面的脆弱性。

Cicada 3301组织是一个起源于2012年神秘的黑客组织，以其难以捉摸的匿名性和复杂的网络攻击手段而闻名。该组织此次针对标致汽车经销商的攻击行动，展示了其在网络犯罪领域的技术进步和战术演变。攻击者利用复杂的社会工程学手段和网络攻击技术，绕过了标致经销商的网络安全防护措施，成功渗透系统并窃取了包括客户信息、车辆库存详情以及维修服务信息在内的敏感数据。泄露的数据中包含身份信息、车辆识别码（VIN）、车牌号码以及身份证件扫描件，主要涉及法国Lot-et-Garonne地区的客户。

此次攻击的具体技术细节尚未完全披露，但已知的是，Cicada 3301组织使用了高级的网络攻击手段，包括利用未打补丁的软件漏洞或通过钓鱼邮件等手段获取初始访问权限。一旦进入系统，攻击者便开始横向移动，寻找并窃取高价值数据。此外，攻击者还可能使用了数据擦除或加密技术，以增加勒索的筹码。

Cicada 3301组织此次行动的另一个显著特点是其对时间敏感信息的精准把控，选择在15天后公布窃取的数据，这无疑给标致汽车带来了巨大的公关和操作压力。这种策略旨在最大化心理压力，迫使标致汽车在有限的时间内做出回应。此次数据泄露事件对标致汽车的经销商网络构成了重大威胁。经销商在客户购车、维修和保养过程中扮演着关键角色，此次攻击可能导致客户信任下降，影响日常运营，甚至引发法律诉讼。此外，如果泄露的数据包括客户的财务信息，标致可能面临根据GDPR规定的巨额罚款。

参考链接：

https://www.zataz.com/les-pirates-du-groupe-cicada-3301-revendiquent-une-attaque-contre-les-concessions-peugeot/

#

数据泄露

### **Postman Workspaces 数据泄露事件暴露3万敏感API密钥和令牌**

Postman Workspaces一个广受欢迎的云基础API开发和测试平台，研究人员在一项为期一年的调查中发现其存在严重的安全漏洞。研究发现，超过30,000个公开可访问的工作空间不慎泄露了第三方API的敏感信息，包括访问令牌、刷新令牌和第三方API密钥，这对个人和企业用户会构成了重大风险。此次数据泄露事件涵盖了从小型业务到大型企业的各个行业的组织，影响到了包括GitHub、Slack和Salesforce在内的主要平台。泄露的数据不仅包括敏感的API密钥和访问令牌，还有管理员凭证，这些信息的泄露可能导致财务损失和声誉损害。泄露的原因主要是由于Postman集合的不当共享、访问控制配置错误、与公开可访问的存储库同步以及敏感数据的明文存储。

这些安全漏洞的影响是深远的。攻击者可以利用泄露的API密钥或访问令牌直接访问敏感系统和数据，这可能导致更多数据泄露、未经授权的系统访问以及增加的网络钓鱼和社会工程攻击。Postman通常存储用于API认证和通信的敏感信息，包括API密钥、密钥和个人身份信息（PII）。为了保护数据安全，组织必须采取更加严格的安全措施，包括谨慎使用环境变量、限制权限、避免使用长期令牌、采用外部密钥管理，并在共享任何集合或环境之前进行仔细检查。

CloudSEK已经向受影响的组织报告了这些发现，并帮助他们减轻风险。为了防止未来的泄露，CloudSEK建议组织采取更加可靠的安全措施，例如使用环境变量以避免硬编码敏感数据、限制权限、频繁轮换令牌、利用密钥管理工具，并在共享之前仔细检查集合。Postman在得知这些发现后，也已经实施了一项秘密保护政策，以防止敏感数据在公共工作空间中被曝光。该政策在检测到密钥时提醒用户，并提供解决方案，促进过渡到私有或团队工作空间。Postman还宣布，将从公共API网络中移除已知暴露密钥...