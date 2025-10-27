---
title: 新网络攻击组织使用PowerRAT和DCRAT武器展开攻击——每周威胁情报动态第197期（10.18-10.24）
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492376&idx=1&sn=040e9ed1c500345f3dd4cf0fa969719a&chksm=e90dc932de7a40240ca9b32a5ffe8ebaeb4cc7df419354c4e58599157b0e45f516e05e232dae&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2024-10-26
fetch_date: 2025-10-06T18:56:06.011053
---

# 新网络攻击组织使用PowerRAT和DCRAT武器展开攻击——每周威胁情报动态第197期（10.18-10.24）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMINeYG0xg4btBInpvgswiaLDvMezqC0jzMYgNaiagu4ktmbPMeMNPegmKe7JaecHMuibo8tvBd5w2ZUOw/0?wx_fmt=jpeg)

# 新网络攻击组织使用PowerRAT和DCRAT武器展开攻击——每周威胁情报动态第197期（10.18-10.24）

原创

BaizeSec

白泽安全实验室

**APT攻击**

* 新网络攻击组织使用PowerRAT和DCRAT武器展开攻击
* APT34组织针对中东能源行业发起网络攻击
* Lazarus APT组织利用“坦克游戏”窃取加密货币

**攻击活动**

* 攻击者瞄准Docker API服务器部署SRBMiner挖矿程序

**数据泄露**

* 墨西哥医疗行业遭遇大规模数据泄露

**恶意软件**

* 朝鲜黑客通过NFT项目“BeaverTail”部署恶意软件
* 新型RomCom恶意软件变种针对乌克兰和波兰组织发起攻击

**勒索软件**

* Akira勒索软件持续进化，对Windows和Linux主机都构成重大威胁
* 新型勒索软件即服务（RaaS）Cicada3301浮出水面

APT攻击

**新网络攻击组织使用PowerRAT和DCRAT武器展开攻击**

Cisco Talos团队最近揭露了一起由未知攻击组织发起的网络钓鱼活动，该活动使用了一个名为Gophish的开源网络钓鱼工具包。此次钓鱼活动通过精心设计的感染链，利用恶意文档（Maldoc）或基于HTML的感染方式，要求受害者的互动才能触发感染链。研究人员发现了一种未被记录过的PowerShell远程访问工具（RAT），他们将其命名为PowerRAT，以及另一种臭名昭著的远程访问工具（RAT）——DCRAT。攻击者本次攻击目标主要针对的是讲俄语的用户，这一判断基于钓鱼邮件中使用的语言、恶意文档的诱惑内容，以及伪装成VKontakte（VK）的HTML网页——VK是一个在俄罗斯、乌克兰、白俄罗斯、哈萨克斯坦、乌兹别克斯坦和阿塞拜疆等地区广受欢迎的社交媒体应用。

通过对恶意超链接的分析，发现攻击者控制的托管域名disk-yanbex.ru提供了恶意的Microsoft Word文档和一个嵌入恶意JavaScript的HTML文件。该域名解析到IP地址34.236.234.165，这是一个AWS EC2实例，其完全限定域名为ec2-34-236-234-165.compute-1.amazonaws.com。进一步分析发现，攻击者在服务器34.236.234.165上托管了Gophish工具包，运行在端口3333上。此次活动有两种初始攻击向量：一种基于恶意Word文档，另一种基于嵌入恶意JavaScript的HTML文件。一旦激活，这些向量将导致下载并激活PowerRAT或DCRAT，具体取决于初始向量。两个攻击链都需要用户干预才能在受感染的机器上触发感染。当受害者打开Microsoft Word文档并启用文档横幅中显示的“查看内容”按钮时，恶意VB宏程序将执行。宏程序首先执行一个函数，将Word文档中的诱惑内容中的特定编码符号解码或翻译成西里尔字母表中的相应字符，将诱惑内容转换为可读形式。PowerRAT作为一种有效载荷在此次活动中执行于受害者的机器内存中，它具有执行其他PowerShell脚本或命令的功能。这些脚本或命令由C2服务器指导，从而为受害者机器上的进一步感染提供了攻击向量。攻击者在此次活动中使用了嵌入恶意JavaScript的HTML文件，这些文件通过钓鱼邮件中的恶意链接传递给受害者，导致DCRAT有效载荷的感染。在DCRAT感染中，SFX脚本运行了一个恶意的Loader可执行文件，并同时打开了一个诱饵文档。这个被称为“GOLoader”的恶意Loader可执行文件是用Golang编译的。它通过执行PowerShell命令，修改了Microsoft Defender Antivirus的配置设置。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPwhCpcSHVozsVmfg9XgBEq5zRHQPq62CactJGbJRscEtdI4DeFBsCj5CialTpr8NhqbYVCQAJyaoQ/640?wx_fmt=png&from=appmsg)图 1 PowerRAT的感染过程

参考链接：

https://blog.talosintelligence.com/gophish-powerrat-dcrat/

**APT34组织针对中东能源行业发起网络攻击**

Trend Micro的研究团队一直在监控一个名为Earth Simnavaz的网络间谍组织，该组织也被称为APT34和OilRig，它一直在积极针对中东地区的知名实体进行攻击。该组织利用复杂的策略，包括部署利用Microsoft Exchange服务器进行凭证盗窃的后门，以及利用诸如CVE-2024-30088的漏洞进行权限提升。这些攻击的初始入口点被追溯到上传到脆弱Web服务器的Web Shell。这个Web Shell不仅允许执行PowerShell代码，还允许攻击者从服务器下载和上传文件，从而扩大了他们在目标网络中的立足点。一旦进入网络，APT组织将利用这些访问权限下载ngrok远程管理工具，促进了横向移动，并使他们能够到达域控制器。在他们的操作过程中，该组织利用了CVE-2024-30088——Windows内核权限提升漏洞——作为权限提升的手段，通过开源工具RunPE-In-Memory将漏洞二进制文件加载到内存中。这使他们能够注册一个密码过滤器DLL，随后部署了一个负责通过Exchange服务器外泄敏感数据的后门。外泄的数据被转发到由威胁行为者控制的邮件地址，有效地完成了感染链，并确保攻击者保持对受感染环境的控制。

Ngrok是一个合法工具，用于从本地机器到互联网创建安全隧道，允许通过公共URL访问内部服务。然而，攻击者组织可以利用ngrok绕过防火墙和网络安全控制，用于恶意目的。他们可能会使用它建立命令和控制（C&C）通信，外泄敏感数据，或通过在受感染的机器和他们的服务器之间创建未检测到的隧道来部署有效载荷，这使得安全团队更难检测到可疑活动。

多个数据点和指标将这次攻击归因于Earth Simnavaz组织，证据表明该组织仍然活跃，特别针对中东国家。这次活动，像之前报告的研究一样，涉及针对Exchange服务器并通过它们中继通信。在代码和功能级别上，攻击中使用的Exchange后门与之前活动中看到的后门之间存在显著相似性。此外，两种工具都与Karkoff后门共享特征，后者也与同一威胁行为者有关联，并利用Exchange Web Services（EWS）API进行恶意活动。Earth Simnavaz的策略也与FOX Kitten的策略重叠，后者也被观察到使用RMM工具ngrok。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPwhCpcSHVozsVmfg9XgBEqT645eMgPmicupSz5T8MBHlc3eXPRRIR0Vk25eJD8zejpOZCsl7iba67g/640?wx_fmt=png&from=appmsg)图 2 APT34 攻击链

参考链接：

https://www.trendmicro.com/en\_us/research/24/j/earth-simnavaz-cyberattacks.html

**Lazarus APT组织利用“坦克游戏”窃取加密货币**

Lazarus APT组织及其下属的BlueNoroff子小组是一个高度复杂且多面的朝鲜语威胁行为者。卡巴斯基研究人员一直在密切监控他们的活动，并经常看到他们在攻击中使用标志性的恶意软件——一个名为Manuscrypt的全功能后门。据研究发现，Lazarus APT组织至少从2013年起就开始使用这种恶意软件，研究人员已经记录了其在50多个独特活动中的使用情况，目标包括政府、外交实体、金融机构、军事和国防承包商、加密货币平台、IT和电信运营商、游戏公司、媒体机构、赌场、大学，甚至是安全研究人员——这个名单还在继续。

2024年5月13日，卡巴斯基的消费级产品全功能安全软件在俄罗斯一位居民的个人电脑上检测到了新的Manuscrypt感染。由于Lazarus APT组织很少针对个人进行攻击，这引起了研究人员的兴趣，决定深入研究。他们发现，在检测到Manuscrypt之前，他们的技术还检测到了从网站detankzone.com发起的Google Chrome网络浏览器的漏洞利用。表面上，这个网站看起来像是一个为去中心化金融（DeFi）NFT（非同质化代币）基于的多人在线战斗竞技场（MOBA）坦克游戏的专业设计产品页面，邀请用户下载试用版。但这只是伪装。在背后，这个网站有一个隐藏的脚本在用户的Google Chrome浏览器中运行，启动了一个零日漏洞利用，使攻击者完全控制了受害者的电脑。访问该网站就足以被感染——游戏只是一个分散注意力的工具。该网站是用TypeScript/React开发的，其index.tsx文件中包含了一小段加载并执行Google Chrome漏洞的代码。漏洞包含两个漏洞的代码：第一个用于获得从JavaScript读取和写入Chrome进程内存的能力，第二个用于绕过最近引入的V8沙箱。在此次攻击中Lazarus APT组织还展现了其在社交工程方面的高超技巧。他们不仅创建了一个看似合法的游戏网站，还在社交媒体上建立了强大的存在感，试图吸引有影响力的加密货币领域人物来推广他们的恶意网站。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPwhCpcSHVozsVmfg9XgBEq16SkB0iasmVbF9XXjJX5Dwc4eJ2FlxUhBCRxdVbz6vsg22NX9hML3uA/640?wx_fmt=png&from=appmsg)图 3 原始游戏

参考链接：

https://securelist.com/lazarus-apt-steals-crypto-with-a-tank-game/114282/

攻击活动

**攻击者瞄准Docker API服务器部署SRBMiner挖矿程序**

趋势科技（Trend Micro）的研究人员发现，网络攻击者正在瞄准Docker远程API服务器，以在被入侵的实例上部署SRBMiner加密货币矿机程序。攻击者利用gRPC协议通过h2c协议绕过安全措施，并在Docker主机上执行加密货币挖掘，通过gRPC方法操纵Docker功能。根据趋势科技发布的分析报告，攻击者首先检查Docker API的可用性和版本，然后通过gRPC/h2c升级请求和gRPC方法来操纵Docker功能。随后，攻击者从GitHub下载并部署SRBMiner加密货币矿机，并开始向他们的加密货币钱包和公共IP地址进行挖掘。

攻击始于扫描面向公众的Docker API主机，并检查HTTP/2升级，随后是向未加密的h2c协议的连接升级请求。然后，攻击者检查gRPC方法以执行Docker环境上的操作，包括那些可以用于执行健康检查、文件同步、认证、密钥管理和SSH转发的操作。攻击者随后通过h2c协议请求升级。一旦服务器使用gRPC请求处理了所有必需参数的连接升级请求，攻击者就会发送/moby.buildkit.v1.Control/Solve gRPC请求，以构建基于Dockerfile.srb的Docker镜像，该文件包含了基于合法Docker镜像debian:bookworm-slim的Docker容器构建细节。攻击者从GitHub下载SRBMiner，将其解压到临时目录，并在/usr/sbin目录中部署。然后攻击者使用Ripple钱包启动挖掘过程，并通过将点替换为下划线来掩盖他们的公共IP地址。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPwhCpcSHVozsVmfg9XgBEqGfzamKXM8OW0ic9rdxK4TAOTVrBzYibGoQq9Hz3picic0td37GGWTPEiaew/640?wx_fmt=png&from=appmsg)图 4 攻击示意图

参考链接：

https://securityaffairs.com/170144/malware/docker-remote-api-servers-srbminer.html

#

数据泄露

**墨西哥医疗行业遭遇大规模数据泄露**

墨西哥医疗行业近日遭受重大打击，超过500万患者的敏感信息因一起数据泄露事件而面临风险。据Cybernews研究团队于8月26日发现，一家医院的信息系统配置不当，导致一个未设密码的Kibana实例暴露了大量患者信息。Kibana是一个广泛用于数字系统中监控和分析数据的流行工具。

此次泄露的数据库包含了500GB的敏感数据，影响了墨西哥全国约530万人，约占该国人口的4%。泄露的数据包括患者的姓名、种族、国籍、宗教、血型、出生日期、性别、电话号码、电子邮件地址、墨西哥个人识别号码（CURP）、医疗服务收费、访问过的医院以及支付请求描述等。

研究人员将这一开放实例归因于总部位于德克萨斯州的软件公司eCaresoft Inc.，该公司开发并运营了两个基于云的医院信息系统——Cirrus和Anytime。这些平台被医疗机构用来管理医疗工作的各个方面，包括管理库存和药品、预约医疗、同步部门间信息以及维护每位患者的医疗记录。据该公司称，其平台用户包括超过30,000名医生、65家医院和110个门诊护理中心。

泄露的CURP号码尤其令人担忧。CURP是墨西哥政府为墨西哥公民和居民提供的身份证号码，其功能类似于美国的社会保障号码。落入威胁行为者手中的CURP号码可能被用于身份盗窃和欺诈，从获取更多敏感信息到冒充个人开设银行账户，许多非法活动都可能使受害者面临风险。Cybernews研究团队警告说，攻击者可以利用这些泄露的信息来骗取保险索赔、窃取资金或欺诈医疗系统。受害者可能会遭遇未经授权的交易和未支付的债务。此外，泄露的信息与其他在线数据点结合，可能被用来通过电子邮件和电话冒充医疗机构，发起复杂的网络钓鱼攻击。

参考链接：

https://cybernews.com/security/ecaresoft-data-leak/

恶意软件

**朝鲜黑客通过NFT项目“BeaverTail”部署恶意软件**

网络安全公司eSentire的研究人员揭露了一起复杂的网络钓鱼活动，该活动利用假冒的NFT项目“Bored BeaverTail Yacht Club”来分发名为BeaverTail的恶意软件。攻击者采用的一种新策略，被称为“Contagious Interview”。

该活动利用欺诈性的NFT市场项目来分发BeaverTail恶意软件。攻击始于通过钓鱼邮件或LinkedIn消息邀请受害者探索NFT项目，这种方法特别针对经常参与探索新技术和平台的软件开发者社区，包括NFT。一旦受害者从一个GitHub仓库下载了恶意项目，BeaverTail恶意软件就会尝试下载并执行一个名为Invisible Ferret的基于Python的后门程序。这个后门程序允许攻击者获得对受害者系统的广泛控制，可能会导致数据盗窃、间谍活动，包括InvisibleFerret后门程序或其他恶意活动。研究人员指出，他们没有观察到InvisibleFerret的部署，但他们评估了InvisibleFerret组件可能隐藏在.npl脚本中的可能性。”

eSentire的调查发现，这次攻击中使用的战术、技术和程序（TTPs）与朝鲜攻击者，特别是Lazarus Group的行动高度一致，也被称为“Contagious Interview”。Lazarus Group以针对软件开发者和加密货币平台而出名，经常使用像假工作机会或NFT项目这样的诱饵。

参考链接：

https://securityonline.info/developers-targeted-north-korean-hackers-deploy-beavertail-malware-via-nfts/

**新型RomCom恶意软件变种针对乌克兰和波兰组织发起攻击**

近期网络安全研究人员发现了一波新的网络攻击活动，这些攻击针对的是乌克兰的高级别政府实体以及波兰的组织。这些攻击使用了更新版本的RomCom恶意软件，其目的是在受害者的系统中建立长期访问权限，并窃取“战略利益”相关的数据。根据网络安全公司Cisco Talos的最新报告，攻击者可能会在受感染的设备上后续部署勒索软件，以追求经济利益。

RomCom，也被称为Storm-0978，以针对欧洲和北美的国防和政府实体而闻名。它参与了勒索软件和间谍攻击活动，并被归因于讲俄语的威胁行为者。RomCom这个名字来源于其自至少2022年以来一直在使用的定制恶意软件。在Cisco Talos分析的最新活动中，该组织通过钓鱼邮件将更新的RomCom恶意软件发送给受害者。这使得攻击者能够在受害者的设备上执行命令和下载额外的工具。

新的RomCom变种，研究人员将其标记为SingleCamper。该恶意软件会将系统信息发送到黑客控制的服务器，使他们能够评估受感染的系统是否值得进一步利用。该恶意软件还可以窃取具有特定扩展名的文件。Palo Alto Networks的研究表明，这种新的RomCom变种的最早版本——他们追踪为SnipBot——于2023年12月从乌克兰提交至VirusTotal存储库。Cisco Talos也将最新活动追溯到大约同一时间。

在研究人员发现的一封钓鱼邮件中，攻击者冒充合法组织，并使用伪装成简历的PDF文档作为诱饵。根据Palo Alto Networks的说法，RomCom使用新变种针对了包括技术、法律和农业行业的公司在内的广泛受害者。去年，与RomCom有关联的黑客在立陶宛举行的北约峰会前夕针对乌克兰及其盟友展开攻击。他们可能利用了该事件的高关注度来感染与会者所使用的恶意软件。

参考链接：

https://therecord.media/romcom-malware-variant-ukraine-poland-espionage

勒索软件

**Akira勒索软件持续进化，对Windows和Linux主机都构成重大威胁**

根据思科Talos的最新研究和分析，Akira勒索软件继续巩固其在威胁格局中最为普遍的勒索软件操作之一的地位。该组织之所以成功，部分原因是它们在不断地进化。例如，在Akira今年早些时候已经开发了他们勒索软件加密器的新版本之后，他们最近观察到另一个针对Windows和Linux主机的新迭代版本。此前，Akira通常采用双重勒索策略，...