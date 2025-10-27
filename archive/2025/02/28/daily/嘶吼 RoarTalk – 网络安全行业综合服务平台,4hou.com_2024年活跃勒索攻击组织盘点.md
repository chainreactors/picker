---
title: 2024年活跃勒索攻击组织盘点
url: https://www.4hou.com/posts/PGlA
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-28
fetch_date: 2025-10-06T20:35:29.343639
---

# 2024年活跃勒索攻击组织盘点

2024年活跃勒索攻击组织盘点 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 2024年活跃勒索攻击组织盘点

安天
[技术](https://www.4hou.com/category/technology)
2025-02-27 16:47:14

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)261898

收藏

导语：勒索攻击目前已成为全球组织机构主要的网络安全威胁之一，被攻击者作为牟取非法经济利益的犯罪工具。为了增加受害方支付勒索赎金的概率并提升赎金金额，攻击者已从单纯的恶意加密数据演变为采用“窃取文件+加密数据”的双重勒索策略。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740646189180049.jpg "1740628154122947.jpg")

**1 概述**

勒索攻击目前已成为全球组织机构主要的网络安全威胁之一，被攻击者作为牟取非法经济利益的犯罪工具。为了增加受害方支付勒索赎金的概率并提升赎金金额，攻击者已从单纯的恶意加密数据演变为采用“窃取文件+加密数据”的双重勒索策略。更有甚者，在双重勒索的基础上，增加DDoS攻击以及骚扰与受害方有关的第三方等手段，进一步演变为“多重勒索”。近年来，勒索攻击的主流威胁形态已从勒索团伙广泛传播勒索软件收取赎金，逐渐转化为“RaaS（勒索软件即服务）+定向攻击”收取高额赎金的模式。这种模式针对高价值目标，RaaS的附属成员通过购买0Day漏洞、研发高级恶意代码、收买企业内鬼和情报等手段，提高突防能力并提升勒索载荷落地成功率。这种“定向勒索+窃密+曝光+售卖”的组合链条，通过胁迫受害者支付赎金从而实现获利。为有效应对勒索风险，防御者需要改变对勒索攻击这一威胁的认知，并且更深入地了解定向勒索攻击的运行机理，才能构建有效的敌情想定，针对性的改善防御和响应能力。

2024年中，勒索攻击事件频繁发生，攻击者通过广撒网式的非定向模式和有针对性的定向模式开展勒索攻击。勒索攻击持续活跃的因素之一是RaaS商业模式的不断更新。RaaS是勒索攻击组织开发和运营的基础设施，包括定制的破坏性勒索软件、窃密组件、勒索话术和收费通道等。各种攻击组织和个人可以租用RaaS攻击基础设施，完成攻击后与RaaS组织按比例分赃。这一商业模式的兴起和成熟，使得勒索攻击的门槛大幅降低，攻击者甚至无需勒索软件开发技能，也能对目标进行定向攻击。另一重要因素是初始访问经纪人（Initial Access Broker, IAB）的助纣为虐。IAB通过售卖有效访问凭证给攻击者实现非法获利，而无需亲自进行攻击。攻击者利用这些凭证，对特定目标进行有针对性的勒索攻击，建立初始访问后展开后续恶意活动，最终实现对目标的勒索行为。

据不完全统计，2024年中至少有90个不同名称的勒索攻击组织通过Tor网站或Telegram频道等特定信息源发布受害者信息。其中，新增的50个勒索攻击组织中，有21个与已知组织存在联系。这些组织发布的受害者信息涉及约5300个来自全球不同国家或地区的组织机构，覆盖多个行业。然而，实际受害者数量可能远超这一数字，因为某些情况下，攻击者可能基于多种原因选择不公开或删除信息，例如在与受害者达成协议后，或受害者支付赎金以换取信息的移除。

相关勒索软件及勒索攻击组织信息参考计算机病毒百科（<https://www.virusview.net/>）。

表 1‑1 2024年发布受害者信息的组织

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 2024年曾发布受害方信息的勒索攻击组织（按首字母排序） | | | | |
| 0mega | 8Base | Abyss | Akira | Apos |
| APT73 | Arcus Media | Argonauts | BianLian | Black Basta |
| BlackByte | BlackCat/ALPHV | BlackSuit | BlackOut | BlueBox |
| Brain   Cipher | Cactus | Chort | Cicada3301 | Ciphbit |
| Cloak | Clop | Cuba | DaiXin | dan0n |
| Dark   Angel/Dunghill | Dark Vault | Donex | Donut | DragonForce |
| El   dorado | Embargo | Everest | FSociety | Fog |
| Gookie | HellCat | Helldown | Hunters | INC |
| Insane | InterLock | Kairos | Kill Security | Knight |
| LockBit | Lynx | Mad Liberator | Lorenz | Mallox |
| Medusa | MedusaLocker | Meow | Metaencryptor | Money Message |
| Monti | Mydata | Nitrogen | Noname | Orca |
| Play | PlayBoy | Pryx | QiLin | QiuLong |
| RA   World | RansomCortex | RansomEXX | RansomHouse | RansomHub |
| Red | Rhysida | SafePay | SEXi（APT   INC） | Sarcoma |
| Sensayq | Slug | Snatch | SpaceBears | Stormous |
| Termite | ThreeAM(3AM) | Trigona | Trinity | Trisec |
| Underground | Unsafe | Valencia | Vanir Group | WereWolves |

**目前，勒索攻击的主流威胁形式已经演变为RaaS+定向攻击收取高额赎金的运行模式。全球范围内，制造、医疗、建筑、能源、金融和公共管理等行业频繁成为勒索攻击的目标，给全球产业产值造成严重损失。现将2024年活跃勒索梳理形成攻击组织概览，进行分享**。

**2 勒索攻击行为分类**

2024年活跃的勒索攻击行为主要有以下三类：

**·加密文件**

采用此类勒索攻击方式的攻击者会使用勒索软件执行体对数据文件进行加密，执行体通过特定加密算法（如AES、RSA、ChaCha20和Salsa20等）组合利用对文件进行加密，大多数被加密文件在未得到对应密钥的解密工具时，暂时无法解密，只有少部分受害文件因勒索软件执行体存在算法逻辑错误而得以解密。

**·窃取文件**

采用此类勒索攻击方式的攻击者不使用勒索软件执行体对数据文件进行加密，仅在目标系统内驻留并窃取数据文件，窃密完成后通知受害者文件被窃取，如不按期支付勒索赎金，则会公开或出售窃取到的数据文件，给予受害者压力，从而迫使受害者尽早支付赎金。

**·窃取文件+加密文件（双重勒索）**

采用此类勒索攻击方式的攻击者发动勒索攻击前，会在目标系统内驻留一段时间，在此期间窃取数据文件，在窃取工作完成后会投放勒索软件执行体，加密系统中的文件，并通知受害者文件被窃取，如不按期支付勒索赎金，不仅现有网络环境中的文件因被加密而无法使用，而且还会公开或出售窃取到的数据文件，给予受害者压力，从而迫使受害者尽早支付赎金。

****3 2024**年活跃勒索攻击组织盘点**

回顾2024年发生的勒索软件攻击事件，根据攻击活跃度和受害者信息发布数量，对活跃的勒索攻击组织进行盘点。盘点按组织名称的首字母进行排序，排名不分先后。

表 1‑2 2024年活跃勒索组织概览

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740646190101296.png "1740628116767952.png")

**3.1 8Base**

8Base勒索软件于2022年3月首次被发现，其勒索软件代码基于Phobos勒索软件开发。该勒索软件背后的攻击组织采用RaaS和双重勒索的模式运营，疑似为RansomHouse勒索攻击组织的分支或品牌重塑。该组织主要通过漏洞武器化、有效访问凭证和搭载其他恶意软件等方式对目标系统进行突防，常利用SmokeLoader木马实现对目标系统的初始访问。在建立与目标系统的初始访问后，该组织利用多种工具作为攻击装备以实现其他恶意行为。例如，利用Mimikatz、LaZagne、VNCPassView等工具窃取系统中的凭据，利用PsExec实现横向移动，利用Rclone回传窃取到的数据。目前暂未发现公开的解密工具。

2024年，8Base受害者信息发布及数据泄露平台发布约150名受害者信息，实际受害者数量可能更多。

**3.1.1 组织概览**

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740646191558693.png "1740628100157214.png")

**3.2 Akira**

Akira[1]勒索软件被发现于2023年3月，其背后的攻击组织通过RaaS和双重勒索的模式运营该勒索软件，以RaaS模式经营和勒索赎金分成等方式实现非法获利，勒索赎金分别为用于解密被加密文件和删除被窃取的数据两部分。该勒索攻击组织主要通过有效访问凭证、未配置多重身份验证（MFA）的VPN账户和漏洞武器化等方式对目标系统突防，曾利用思科VPN相关漏洞（CVE-2023-20269）实现对目标系统的初始访问。在建立与目标系统初始访问后，利用多种工具作为攻击装备以实现其他恶意行为，例如使用AnyDesk远程控制计算机和传输文件，使用PowerTool关闭与杀毒软件有关的进程，使用PCHunter、Masscan和AdFind获取特定信息，使用Mimikatz窃取凭证，使用Rclone和FileZilla回传窃取到的数据等行为。

Akira具备针对Windows、Linux和VMware等目标系统的勒索软件。除了“窃密+加密”的行为，还存在只窃密不加密的模式，在完成对受害系统数据窃取后，攻击者选择不投放勒索软件，而是通过窃取到的数据威胁受害者进行勒索。国外安全厂商Avast发现Akira勒索软件存在漏洞[2]，并于2023年6月29日发布了解密工具，但该工具只适用于6月29日前的Akira勒索软件执行体版本，因为Akira勒索软件开发人员在此后修复了漏洞。Akira勒索攻击组织与之前退出勒索软件市场的Conti勒索攻击组织疑似存在关联，体现在勒索软件执行体的部分代码段和加密数字货币钱包地址等方面。

2024年，Akira受害者信息发布及数据泄露平台发布约310名受害者信息和窃取到的数据，实际受害者数量可能更多。

3.2.1 组织概览

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740646192708480.png "1740628087936918.png")

**3.3 Black Basta**

Black Basta勒索软件被发现于2022年4月，其背后的攻击组织通过RaaS和双重勒索的模式运营该勒索软件，由于Black Basta所使用的每个勒索软件执行体都硬编码一个唯一的识别码，故猜测该组织仅采用定向模式开展勒索攻击活动。该勒索攻击组织主要通过有效访问凭证、搭载其他恶意软件和漏洞武器化等方式对目标系统突防。该组织成员在地下论坛发帖寻求组织机构的网络访问凭证，曾利用QBot木马和PrintNightmare相关漏洞CVE-2021-34527实现对目标系统的初始访问。在建立与目标系统初始访问后，利用多种工具作为攻击装备以实现其他恶意行为，例如使用AnyConnect和TeamViewer建立远程连接，使用PsExec执行命令，使用Netcat进行扫描，使用Mimikatz转储凭证，使用Rclone回传窃取到的数据等恶意行为。2023年12月，国外网络安全研究机构Security Research发布一个名为“Black Basta Buster”的解密工具[3]，用于恢复被Black Basta勒索软件加密的文件，但该工具仅适用于2022年11月至2023年12月期间的部分勒索软件变种版本。

Black Basta勒索攻击组织与之前退出勒索软件市场的BlackMatter和Conti勒索攻击组织疑似存在关联，体现在勒索软件执行体部分代码段，受害者信息发布及数据泄露站点设计风格，通信方式和勒索谈判话术等方面。故猜测Black Basta勒索攻击组织可能是BlackMatter和Conti勒索软件组织的分支或品牌重塑。2024年，Black Basta受害者信息发布及数据泄露平台发布约190名受害者信息，实际受害者数量可能更多。

3.3.1 组织概览

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740646193137378.png "1740628071883159.png")

**3.4 BlackSuit**

BlackSuit勒索软件于2023年5月首次被发现，其背后的攻击组织采用双重勒索策略进行运营。该组织具有较为复杂的身份背景，被认为是Royal勒索软件的品牌重塑。Royal是由Zeon组织更名而来，而Zeon疑似由Conti组织的原成员参与建设。Conti组织因源代码泄露等因素而解散，Conti组织被认为是Ryuk的继承者，层层关系错综复杂。目前尚未发现BlackSuit组织通过RaaS模式招收附属成员。BlackSuit具备针对Windows、Linux和VMware等目标系统的勒索软件。该组织主要通过漏洞武器化、有效访问凭证以及搭载其他恶意软件（如SystemBC和GootLoader）等方式对目标系统进行渗透。在建立与目标系统的初始访问后，利用多种工具作为攻击装备以实现其他恶意行为。例如，使用AnyDesk、LogMeIn、AteraAgent等工具远程控制计算机和传输文件，使用Mimikatz和Nirsoft窃取系统中的凭证，使用Rclone回传窃取到的数据。目前暂未发现公开的解密工具。

2024年，BlackSuit受害者信息发布及数据泄露平台发布约150名受害者信息，实际受害者数量可能更多。

3.4.1 组织概览

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250227/1740646194944767.png "1740628058659914.png")

**3.5 Hunters**

Hunters（又名Hunters International）勒索软件于2023年10月首次被发现，其背后的攻击组织采用RaaS和双重勒索的模式运营该勒索软件。该组织所使用的勒索软件代码在技术架构和操作策略上与已被执法机构查处的Hive组织存在高度相似性。这种相似性使得安全研究人员怀疑Hunters可能是Hive的分支或品牌重塑。然而，Hunters组织否认与Hive有直接关系，声称他们只是购买了Hive的源代码和网络基础设施，并在此基础上使用Rust语言进行了优化，创建了一个独立...