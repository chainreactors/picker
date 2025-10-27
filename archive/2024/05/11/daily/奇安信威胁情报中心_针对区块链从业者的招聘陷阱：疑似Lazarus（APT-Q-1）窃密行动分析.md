---
title: 针对区块链从业者的招聘陷阱：疑似Lazarus（APT-Q-1）窃密行动分析
url: https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247510514&idx=1&sn=e7472904209a97c0a8c6769d39c84666&chksm=ea665e85dd11d793bfc20a6e8a533e4e72aac70305e199386a4afc785a9d72d08187ca6580d1&scene=58&subscene=0#rd
source: 奇安信威胁情报中心
date: 2024-05-11
fetch_date: 2025-10-06T17:17:32.172116
---

# 针对区块链从业者的招聘陷阱：疑似Lazarus（APT-Q-1）窃密行动分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2AqAgxkehic94IzMqNFWg2fhl1J9392aGWvE1KSYofOty5WjB2bZzvreNfw1coxVhfcad7KuSNOhkHajMvD5vAQ/0?wx_fmt=jpeg)

# 针对区块链从业者的招聘陷阱：疑似Lazarus（APT-Q-1）窃密行动分析

原创

威胁情报中心

奇安信威胁情报中心

团伙背景

Lazarus是疑似具有东北亚背景的APT组织，奇安信内部跟踪编号APT-Q-1。该组织因2014年攻击索尼影业开始受到广泛关注，其攻击活动最早可追溯到2007年。Lazarus早期主要针对政府机构，以窃取敏感情报为目的，但自2014年后，开始攻击全球金融机构、虚拟货币交易场所等目标，从受害者处盗取金钱资产。Lazarus曾多次利用虚假的社交账号，以提供工作机会为伪装，向特定行业人员发起钓鱼攻击。

事件概述

近期多名安全研究人员发现一类携带恶意JS代码的ZIP压缩包[1-4]，样本涉及的恶意软件与去年11月国外Unit 42团队披露的”Contagious Interview”攻击活动[5]一致。

经过进一步调查，奇安信威胁情报中心发现，攻击者在去年底被披露后仍频繁展开攻击行动，受害者主要是区块链行业的开发者。攻击者在工作平台（比如LinkedIn、Upwork、Braintrust等）上创建虚假的身份，伪装为雇主、独立开发者或初创公司创始人，发布具有丰厚报酬或者紧急任务的工作信息，工作内容通常是软件开发或者问题修复。这些工作信息会吸引到主动搜索而来的开发者，或者借助平台的推送机制呈现在目标人群面前。在讨论具体工作内容时，攻击者试图说服应聘人员在自己设备上运行由他们提供的代码。一旦应聘者不加怀疑地运行程序，其中插入的恶意JS代码将会窃取感染设备上与虚拟货币相关的敏感信息，并植入其他恶意软件。攻击流程如下所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGvTrfSTNpQMkFRW3gvOgyyicxMOxADEt7A5metByucX8fs9paK8hczTA/640?wx_fmt=png&from=appmsg)

这批攻击样本与”Contagious Interview”行动所用的网络基础设施重叠，且攻击者发起网络钓鱼的手法特点和受害者所属行业与Lazarus组织之前的活动相似，因此这次持续进行的攻击行动可能和Lazarus组织有关。

详细分析

**网络钓鱼**

**伪造的网站**

携带恶意JS代码的部分攻击样本中提到app[.]freebling.io这个域名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGl7fgLnzt3pljKZN7nwqNbtw86rKn5MicbPibCe5urSBczicWOkSgA1gPA/640?wx_fmt=png&from=appmsg)

该域名对应网站如下，主页自称是web3营销和奖励平台。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aG7rz4lvHcDEvqpltP17XLf3LiaibZApdLYX6Uj84qQgXunGjNpIWxcrxA/640?wx_fmt=png&from=appmsg)

根据这个域名，我们发现在数月前就有不少区块链行业从业者发帖[6-9]称，收到与该网站相关的开发工作邀请，委派工作的客户要求他们在本地运行所提供的代码，部分应聘者的加密货币钱包因此失窃。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGwX0H6kdqTKNIrMZlO4dlf0PdepDU3guYGRQIGgP2fFFTNPRApXOuog/640?wx_fmt=png&from=appmsg)

**网络钓鱼方式**

对网上公开的攻击活动记录进行整理后，我们发现攻击者利用的工作信息发布平台至少包括LinkedIn[6,9,10]、Upwork[7,8]、Braintrust[11]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGUrVh0aYdjrQUIh18KN91AgAD9MG2cn8UTcqjicJynia00Aibc8ByF2Zgg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGC6s6BfiaRPAwYAibv9fDf5sbOMvu4qEIO0nsiaGTIEIlkoM5KOCUuw75A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGXoqOsXsSCjicaDbGU1R7mzsQPfJibicDjreT0B5Xs6U7U1l918PEB4YuA/640?wx_fmt=png&from=appmsg)

攻击者以伪装的身份与吸引而来的应聘人员进行沟通，向应聘人员呈现详细的项目设计和需求，增加伪装身份的说服力，并通过一系列社会工程学手段诱使应聘者在本地运行攻击者提供的代码，具体方式包括：

(1) 声称是编码挑战，为了测试应聘者的技能是否满足工作要求；

(2) 声称项目代码存在问题需要修复，让应聘者运行程序看看是否能重现问题。

**恶意代码托管**

攻击者通过代码托管平台存放包含恶意代码的软件包，供应聘者下载，使用的代码托管平台包括Github，GitLab和Bitbucket。

与攻击活动有关的Github账号如下，部分Github账号有多年的活动记录，看起来与普通账号无异。

|  |  |
| --- | --- |
| **Github****账号** | **说明** |
| https://github.com/plannet-plannet/ | 账号删除 |
| https://github.com/bmstoreJ/ | 账号删除 |
| https://github.com/CodePapaya/ | 账号删除 |
| https://github.com/Allgoritex/ | 账号删除 |
| https://github.com/bohinskamariia/ | 账号删除 |
| https://github.com/danil33110/ | 账号删除 |
| https://github.com/aluxiontemp/ | 账号删除 |
| https://github.com/komeq1120/ | 账号删除 |
| https://github.com/aufeine/ | 账号自2024-04-15开始活动 |
| https://github.com/dhayaprabhu/ | 账号自2019年开始活动  恶意代码库（dhayaprabhu/Crypto-Node.js）于2024-02-01首次提交 |
| https://github.com/MatheeshaMe/ | 账号自2021年开始活动  恶意代码库（MatheeshaMe/etczunks-marketplace）于2023-10-11提交 |
| https://github.com/Satyam-G5/ | 账号自2023年开始活动  恶意代码库（Satyam-G5/etczunks-marketplace）于2023-10-12 Fork自MatheeshaMe/etczunks-marketplace |
| https://github.com/emadmohd211/ | 账号自2021年开始活动 |
| https://github.com/alifarabi/ | 账号自2020年开始活动  恶意代码库（alifarabi/organ-management）于2024-03-30首次提交 |

GitLab存放的恶意代码库如下，涉及两个账号：Adrian John（@cleverpan43）和NYYU IO（@aminengineerings）。

|  |  |
| --- | --- |
| **GitLab****库链接** | **GitLab****账号** |
| https://gitlab.com/crypto-trading5202718/trading-initial-project | https://gitlab.com/cleverpan43 |
| https://gitlab.com/e-commerce-platform1/e-commerce-hdemo8811 |
| https://gitlab.com/nft-marketplace-platform/nft\_wallet\_hirdemo800118 |
| https://gitlab.com/initial-card-game-demo/2d\_card\_game\_demo\_kmug0801 |
| https://gitlab.com/benhermas/bh-vp-beta | https://gitlab.com/aminengineerings |
| https://gitlab.com/benhermas/bh-cryptoweb-beta |
| https://gitlab.com/ndbtechnology/ndb-school-15121-express-react |
| https://gitlab.com/ndbtechnology/ndb-school-15120-express-react |
| https://gitlab.com/ndbtechnology/ndb-school-16120-nest-react |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGZFSyH9g1FAas4ntKKUcSe1ic16ylqnT1BCV37G8AapicJZHIniaHXzMXg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGV3sib4NDBkIXg4ic7VgEStufQ2nINYicWO9KgDjP3cKKlyiaKhnEj62zHg/640?wx_fmt=png&from=appmsg)

Bitbucket存放的恶意代码库如下，代码库链接来自提及freebling网站的攻击活动记录[7-9]。

|  |
| --- |
| **Bitbucket****库** |
| https://bitbucket.org/juandsuareza/main/src/main/ |
| https://bitbucket.org/freebling/landing-web-app/src/main/ |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGbbfic5YJZrto6L2giaFK3nMtuK43RDGQcXYWnrUIpyvpyymibLzUhtdng/640?wx_fmt=png&from=appmsg)

**恶意软件**

攻击者使用的恶意软件与此前披露的”Contagious Interview”攻击活动一致，因此这里只进行简单的说明。

应聘者下载的软件包某个文件中潜藏有恶意JavaScript代码，植入的恶意代码存放在一行之内，攻击者通常在前面加上单行注释和一长串空白符，如果文本编辑器未使用换行模式，将很难发现恶意代码的存在。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aG0NTGOvGASOJeFGwLQE5Vqax9cTKaYvESn5gpVIZSKk1zNLAUiaYZV2Q/640?wx_fmt=png&from=appmsg)

**JavaScript恶意代码**

JS代码通过Base64编码和字符串切分对关键字符串进行保护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGVDiabQXhqdWqJRLafrolqygtbRe6E63QvXoX2sgVCdXRswiaRPQqhXpQ/640?wx_fmt=png&from=appmsg)

以样本（MD5: 97868b884fc9d01c0cb1f3fa4d80b09f）为例进行分析，其中携带的恶意JS代码会重复运行主函数nt多次。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aG7ojRcprLH3x3RVoXjwHq0wDtb9kZoQySrLzErXke73vZkOAhQicysyw/640?wx_fmt=png&from=appmsg)

主函数nt首先收集Windows, Linux, macOS平台上多款浏览器的敏感信息，尤其是加密货币钱包有关的浏览器插件数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGKfqTpqu3dZG6ic7LMzVaMgVGg2H7AGosxMtw0RW1WmicfQzaVC3ylcwQ/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| **平台** | **收集的信息** |
| Windows | Chrome, Brave, Opera,  Edge浏览器的加密货币钱包插件信息 |
| Linux | Chrome, Brave, Opera浏览器的加密货币钱包插件信息；  “~/.local/share/keyrings/”目录下的文件；  Chrome, Firefox浏览器保存的密码数据。 |
| macOS | Chrome, Brave, Opera浏览器的加密货币钱包插件信息；  login.keychain和login.keychain-db文件；  Chrome, Brave, Firefox浏览器保存的密码数据。 |

将收集的敏感信息回传到C2服务器(147[.]124.214.237:1244)，回传信息的URL为”/uploads”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGz8tH8nyAFbFEFL9QFUvfwNKT4Le9YBXNMIKXhRgT23DO5RjmPiaWH8g/640?wx_fmt=png&from=appmsg)

从C2服务器的”/clients/”下载后续Python脚本并运行。Linux和macOS平台直接调用python3命令执行；而在Windows平台上会先检查”%HOME%\\.pyp\\python.exe”是否存在，如果不存在，则从”/pdown”下载包含Python运行环境的ZIP压缩包，并解压到%HOME%目录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGpvExmVdiaTiaPUcYicJF2hKll7ROzExKZUfo37OabmPSRIQ6MHtGeXVTg/640?wx_fmt=png&from=appmsg)

**Python恶意代码**

从”/clients/”下载的Python脚本解密后续载荷然后执行。其中sType变量为campaign\_id的值，如果下载URL中的campaign\_id省略，sType值则为”default”，因此会因为sType值的不同导致下载得到的Python脚本hash值发生变化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aG6hMAFrudxBx5IpTguiabGWE9EOWfg0HvFDRiaSyyTcGibTzOBibXKYG4fA/640?wx_fmt=png&from=appmsg)

该脚本下载额外的两个脚本并执行：

* 从C2服务器的”/payload/”下载脚本，保存为”%HOME%/.n2/pay”；
* 如果运行平台不为macOS，从C2服务器的”/brow/”下载脚本，保存为”%HOME%/.n2/bow”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGbicyB5Fq3TgDYLoUDTl5Dtj1xDeZ53WoNkVgEhAf0Zgfz80ggb3icoaw/640?wx_fmt=png&from=appmsg)

Bow脚本同样支持Windows、Linux、macOS三个平台，用于进一步窃取多款浏览器的数据，并将其发送回C2的”/keys” URL。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGAOs1ictcNhFxNEr6lRkaraYPyl7F6KFTN8iaPgBd4vbgrbibDTIjomwcA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2AqAgxkehic94IzMqNFWg2fhl1J9392aGVNLWdKjQwJQZ5UiaqedIS4iafeQmGOHvnrwsa0xe4LReeE7Jy04pEJXQ/640?wx_fmt=png&from=appmsg)

Pay脚本包含两部分内容。第一部分用于收集设备信息，包括用户名、操作系统版本、IP和地理位置，同样发送回C2的”/keys” URL。

...