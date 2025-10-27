---
title: 【技术分享】针对比特币钱包App的三种漏洞攻击与对策
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649781006&idx=1&sn=b2ff8f31e73c5f920dabda206f70b0f3&chksm=88934361bfe4ca777feaceb3be5fe1f80617eeaa505ec2d2c410f907fe14bbf0dd8fbcc062c4&scene=58&subscene=0#rd
source: 安全客
date: 2022-12-13
fetch_date: 2025-10-04T01:19:10.821192
---

# 【技术分享】针对比特币钱包App的三种漏洞攻击与对策

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Ok4fxxCpBb4wPiae9tTrnSeGQnicVxRgiagBJZLq0ApGDLShjdpbueV3vSKLl3icgeNLAO3GpMjHaCYWtzT19vPhCQ/0?wx_fmt=jpeg)

# 【技术分享】针对比特币钱包App的三种漏洞攻击与对策

原创

CDra90n

安全客

![](https://mmbiz.qpic.cn/mmbiz_jpg/Ok4fxxCpBb4wPiae9tTrnSeGQnicVxRgiag5L5n41o80eianYkzuJkaBlAuM5ibUeFyGvkSVtvosgRfnToia5SKxFw9A/640?wx_fmt=jpeg)

如今，比特币是最受欢迎的加密货币。随着智能手机和高速移动互联网的普及，越来越多的用户开始在智能手机上访问其比特币钱包。用户可以在智能手机上下载并安装各种比特币钱包应用程序（例如Coinbase，Luno，Bitcoin Wallet），并可以随时随地访问其比特币钱包。但是，这些比特币手机应用程序不一定安全，它们会扩展攻击者的新攻击面。在这项工作中探索了10种最受欢迎的比特币钱包App的不安全性，并发现了三个安全漏洞。通过利用它们，攻击者可以发起各种攻击，包括比特币去匿名，反射和放大垃圾信息以及钱包欺诈攻击。为了解决已确定的安全漏洞，本研究开发了一种工具Bitcoin Security Rectifier，以保护比特币钱包App用户的安全。开发的工具不需要对当前的钱包应用程序进行任何修改，并且符合比特币标准。

**0****1**

**Introduction**

许多消费者和企业（例如Microsoft，Newegg，Overstock，Subway，Starbucks）已接受比特币作为付款方式。随着高速移动互联网的迅速部署和智能手机的普及，越来越多的用户开始通过各种比特币钱包App访问其比特币钱包。比特币钱包App是否会为攻击者创建新的攻击媒介，从而对移动用户发起新的攻击？不幸的是，本文研究得出了肯定的答案。在这项工作中，研究了10种最受欢迎的比特币钱包App（按下载次数排名），发现了三个安全漏洞，涵盖了比特币钱包应用程序的实现和比特币钱包应用程序服务的运行。本文发现，已被各种比特币钱包App广泛使用的比特币应用程序库BitcoinJ泄漏了比特币钱包用户的隐私（例如，所有用户的比特币地址）（漏洞V1）并在不向用户提供任何通知或警报的情况下，在后台不断下载用户不想要的比特币交易（漏洞V2）。此外，发现比特币钱包App可能违反了比特币钱包服务去中心化的原则，这些应用程序的用户更容易受到金融欺诈攻击。更具威胁性的是，大多数用户没有意识到这一点（漏洞V3）。

通过利用这些漏洞，本研究设计了三种针对用户的PoC：（1）比特币去匿名攻击；（2）比特币反射和放大垃圾信息攻击；（3）比特币钱包欺诈攻击。第一种攻击使攻击者可以取消对比特币钱包使用的非真实比特币地址进行匿名处理。此攻击不仅以低错误率（例如10^(-13)％）识别比特币钱包App用户的所有比特币地址，而且还可以在满足某些使用条件的同时发现应用程序用户的真实身份。在第二种攻击中，攻击者利用中间的公共比特币网络元素（例如，全节点客户端）向比特币钱包App用户连续不断地未经请求地发送垃圾信息。垃圾信息流量由攻击期间全球所有比特币用户产生的所有新比特币交易组成。这是一种低成本的攻击；攻击者只需要向比特币网络发送一些小的发起数据包。在实验中观察到放大系数（垃圾信息流量大小与攻击发起包大小之比）接近3,666。这种攻击以两种方式攻击受害者：（1）在使用蜂窝网络服务时，受害者需要为比特币垃圾消息付费；（2）受害者的手机比未受到攻击的手机消耗更多的电能96％。第三种攻击显示了攻击者为何可以超越其他类型的金融移动程序攻击的限制，针对比特币钱包应用程序用户发起各种比特币欺诈攻击，下表总结了本文发现。

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb4wPiae9tTrnSeGQnicVxRgiag4ezVGO34iaBAYlzaTicBMcr07ARoDjQicsnYwsXAz2AJsvutrVq0xE69g/640?wx_fmt=png)

**0****2**

**Threat Model and Methodology**

比特币网络架构：下图说明了比特币网络架构。运行比特币协议的网络节点可能包含四个功能：（1）钱包，（2）矿工，（3）完整的区块链数据库和（4）网络路由。钱包功能为用户提供了比特币钱包服务。此功能控制对用户资金（即BTC，比特币的货币）的访问，包括管理私钥/公钥和地址，跟踪余额以及生成和签名交易。矿工功能瓦利约会新交易并将其附加到比特币区块链。完整的区块链数据库功能可维护所有比特币区块的完整且最新的副本。网络路由功能允许一个节点与其他节点通信。

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb4wPiae9tTrnSeGQnicVxRgiagT5WibQVsr0ictJ6q73I3HrdyauBzSJMT9E2g4KXSZWVtqVERTZjuOdJA/640?wx_fmt=png)

威胁模型：在这项研究中，攻击者是对比特币智能手机钱包用户发起远程攻击的人或组织。认为攻击者具有以下能力：（1）他们可以在公共传播信道中拦截，修改或注入任何消息；（2）他们遵守所有加密假设，例如，如果没有解密密钥，将无法解密加密消息；（3）他们无法控制受害者的智能手机和比特币网络基础设施。本文研究了10种流行的比特币钱包App，分别是Coinbase，Bit coin Wallet，Blockchain Wallet，Bitcoin.com Wallet，Luno，Mycelium，Coinomi，BRD，BitPay和Simple Bitcoin。通过两种措施以负责任的方式进行了这项研究。首先，仅将手机用作受害者。其次，没有向公众分发任何恶意的比特币应用程序或库。本研究试图披露比特币钱包App的新安全漏洞和有效攻击，但并不加剧这种破坏。

**0****3**

**Security Vulnerabilities**

###

### **V1：钱包比特币地址泄漏**

第一个安全漏洞是钱包App的比特币地址可能会泄露给攻击者。特别是，BitcoinJ是一个比特币客户端库，已被许多比特币钱包App（例如，Bitcoin Wallet，Mycelium）广泛用于与比特币网络通信，从而泄漏了比特币钱包用户的隐私。

根据比特币标准，在SPV客户端（即，比特币钱包应用程序）与比特币FNC（完整节点客户端）连接之后，filterload信息将发送到FNC。该消息用于指定比特币钱包用户对特定交易的兴趣。实际上，通常将SPV客户端配置为对涉及比特币钱包用户的比特币地址的交易的兴趣。该消息带有三个关键参数，即filter，nHashFuncs和nTweak。filter本身是位域Bloom过滤器，因此FNC可以知道其连接的比特币钱包应用程序的地址的兴趣。根据将数据元素（例如，用户的比特币地址）提供给一组不同的nHashFuncs MurmurHash3哈希函数来设置Bloom过滤器。这些nHashFuncs MurmurHash3哈希函数通过nHashNum×0xFBA4C795 + nTweak初始化，其中nHashNum是哈希函数的索引（例如1st，2nd，3rd），nTweak是SPV客户端为过滤器选择的随机数。要将数据项（例如比特币地址）添加到过滤器，该数据项必须通过nHashFuncs不同的哈希函数进行哈希处理，并通过按位或运算设置过滤器中的相应位。例如，数据项将使用2个不同的哈希函数添加到干净的6位过滤器（值为000000），并且假设第一个和第二个哈希函数的结果分别为7（000111）和9（001001），可以接受的是，将过滤器设置为001111（000111或001001）。

研究表明，为了阻止攻击者通过拦截和分析纯文本filterload消息来准确发现比特币钱包用户曾经使用过的所有比特币地址，BitcoinJ中实现了两种安全机制。首先，由于Bloom过滤器的误报率，一些不属于用户的错误地址将被过滤器过滤掉。其次，仅创建一次filterload消息并将其传输到比特币FNC（成功建立与FNC的TCP连接时），这意味着，如果攻击者从一开始就无法监视SPV客户端的所有活动，则它们将无法拦截filterload消息。

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb4wPiae9tTrnSeGQnicVxRgiagcGOHL4WYamZiaue7QpaKB2a8xu0aL2icykiaUS3hoK87LF4jW0EibgIoSw/640?wx_fmt=png)

通过进一步的分析，发现这两个安全机制并不是安全的，原因如下。首先，将BitcoinJ中使用的Bloom过滤器的误报率（假地址数占添加到过滤器的所有地址数之和）设置为0.001％。第二，在SPV客户端和FNC之间建立TCP连接之后，将包含计算得出的Bloom过滤器的filterload消息发送到FNC。但是研究表明，如果SPV客户端与FNC的现有TCP连接被断开，BitcoinJ将自动发现并与新FNC连接（参见上面的BitcoinJ code1中的HandlePeerDeath函数）。因此，SPV客户端可能会遭受TCP重置攻击（即，有意断开受害者与旧FNC的TCP连接）并将filterload消息重新传输到新FNC。最后一点是，发现在SPV客户端使用的网络接口变得无法使用超过5秒后，BitcoinJ将使用全新的随机数（即nTweak）生成filterload消息。根本原因是BitcoinJ维护一个Reset计时器（即5秒）以监视是否仍然存在可用的网络接口。收到比特币消息后，计时器将更新。一旦过期，将清除并重新初始化存储在内存中的多个变量，包括用于生成过滤器的nTweak。请注意，由于nTweak用于初始化filterload消息中使用的nHashFuncs MurmurHash3哈希函数，因此，由两个不同的nTweaks生成的两条filterload消息可以帮助攻击者显着降低推断比特币用户地址的误报率。

例如，假设有两个由两个不同的nTweaks生成的filterload消息，且误报率设置为0.001％。由于该地址需要通过两个不同的过滤器，因此每个人仅允许0.001％的错误地址通过，因此将错误的地址识别为真实地址的可能性为0.001％×0.001％。

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb4wPiae9tTrnSeGQnicVxRgiagk3gPGrRxFZravF5WxQWf8V6ticJLxDAr0Mqa7NkvARric2lBCZrJxvyw/640?wx_fmt=png)

验证：进行了如下实验来验证这种漏洞的能力，首先通过家庭Wi-Fi网络将经过测试的智能手机（例如，Samsung Galaxy S6 Edge）与互联网连接，下载并安装了经过测试的比特币钱包应用程序（例如，使用BitcoinJ的SPV客户，Bitcoin Wallet）。其次，分别将0.0001 BTC存入了SPV客户端创建的两个比特币地址中。第三，为了使SPV客户端重新传输filterload消息，针对SPV客户端发起了两种攻击：（1）使用Netwox78工具进行TCP重置攻击，该工具旨在代表SPV客户端向FNC发送TCP重置数据包，并且（ 2）使用Aircrack-ng进行Wi-Fi取消身份验证攻击，其目的是使SPV客户端的Wi-Fi断开时间超过5秒，如上图所示。第四，利用拦截的filterload中携带的过滤器消息和公共比特币交易数据库（即Blockchain.info）来推断SPV客户端使用的比特币地址。

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb4wPiae9tTrnSeGQnicVxRgiagAvCVE3ba5IKnJ3e8ybMDn7cDK0Ysr8mDBUtu2gNibicudicD6M00z7mzg/640?wx_fmt=png)

实验结果如上图所示。通过发起TCP重置攻击，攻击者可以迫使经过测试的SPV客户端重新传输带有0.001％误报率的带有过滤器的filterload消息，而Wi-Fi取消身份验证攻击则允许攻击者获取由两个不同的nTweaks生成的两个filterload消息，这可以将误报率降低到10-8％们进一步检查了公共比特币交易数据库中记录的多少比特币地址可以通过拦截的过滤器。对于被TCP重置攻击拦截的过滤器，有3288个比特币地址通过了该过滤器。但是，比特币钱包应用程序仅使用了两个地址，而其余的3286个地址则未被使用。对于通过Wi-Fi取消身份验证攻击拦截的两个过滤器，只有两个比特币地址同时通过了两个过滤器；这两个比特币地址都属于经过测试的比特币钱包应用程序。验证实验证实，BitcoinJ确实泄漏了比特币钱包应用程序使用的比特币地址。

### **V2：没有针对下载比特币交易的反垃圾信息防御**

第二个安全漏洞是，使用BitcoinJ的比特币钱包App将继续在后台从连接的比特币FNC中下载SPV客户端感兴趣的比特币交易，而不会向SPV客户端用户发出任何警报或通知。具体来说，如先前所述，SPV客户端将发送filterload消息，以指定其对特定比特币地址和交易的兴趣到比特币FNC。为了防止FNC或攻击者（中间人）准确地推断比特币用户/钱包的隐私，SPV客户端将通过配置filterload的筛选器字段来添加一些虚假数据项（即，这些内容不符合SPV客户端的兴趣）消息（将误报率设置为0.001％）。如果FNC发现任何符合SPV客户兴趣的比特币交易，则FNC将准备库存消息（即inv），其中包含匹配交易的身份，并将该消息发送给SPV客户。然后，SPV客户端使用BitcoinJ处理inv消息。

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb4wPiae9tTrnSeGQnicVxRgiagBEP3ibAQq0hdibrTia3Q0StAxzgD4TuXwJo1VibPJaz3klvGaZibu2ibrOrw/640?wx_fmt=png)

研究表明，BitcoinJ将在下载inv消息之前对所有交易进行检查。但是，检查是有缺陷的，如BitcoinJ code2所示。具体地说，进行了两次检查：（1）是否在（第11行）之前未下载交易，以及（2）交易是否不是自发的（第14行）。如果无论哪种情况都不进行交易，BitcoinJ将下载比特币交易（第19行）。这证实了BitcoinJ在下载交易之前不检查正在下载的比特币交易是否可以通过发送给FNC的先前过滤器。如果在BitcoinJ上没有部署其他安全机制（例如，与恶意FNC断开连接），则SPV客户端将下载接收到的inv消息中指定的比特币交易操作，无论这些交易是否出于其目的。因此，SPV客户端用户会遭受各种攻击，并且没有意识到这些攻击。

验证：本文进行了一项实验来验证此漏洞。首先在Samsung Galaxy S6 Edge上使用BitcoinJ安装了经过测试的比特币钱包应用程序（即Bitcoin Wallet），并通过家庭Wi-Fi网络将其连接到互联网。其次，使用ARP欺骗攻击拦截了filterload消息。由于比特币并未对所有消息字段都采用消息级加密和完整性保护，因此修改了filterload消息的消息字段Data和nFlag分别设置为0xFF … FF和0，并将修改后的filterload消息发送到SPV客户端连接到的FNC。以上修改表示用户对所有全球比特币用户产生的所有新比特币交易感兴趣。实验持续了10分钟。

![](https://mmbiz.qpic.cn/mmbiz_png/Ok4fxxCpBb4wPiae9tTrnSeGQnicVxRgiagia9bZIBnaOmFsGWkJtGZwReWHXZZIG8vB3r1U7dlwr6sNsIa4xAfIhQ/640?wx_fmt=png)

上图说明了在10分钟的实验运行中，SPV客户端从连接的FNC接收了130条清单消息并下载了2535比特币交易。有三个观察结果。首先，所有下载的比特币交易均不涉及经过测试的SPV客户端曾经使用过的任何比特币地址。其次，SPV客户并未与FNC断开连接，因为FNC出于SPV客户的利益而传输了大量比特币交易。第三，SPV客户端没有向用户显示任何警报或通知（例如，遭受垃圾信息攻击）。这些证实了SPV客户端和BitcoinJ在下载它们之前均未验证是否关注比特币交易，并且未采用任何其他安全机制来阻止由连接的FNC发送的垃圾信息。

### **V3：违反比特币钱包服务去中心化**

根据设计，比特币支付网络使用点对点（P2P）分布式网络架构，该架构允许比特币钱包客户端访问比特币网络而无需任何中间代理或服务器。这种方法不仅保护了比特币钱包用户的匿名性（例如，不需要服务器端用户注册，而且没有检查点监视所有比特币用户的活动），而且还防止了比特币钱包服务受到其中一些节点的损害。比特币网络。攻击者需要控制大多数比特币矿工和整个节点；否则，攻击者将无法篡改比特币支付交易。为了保持比特币的去中心化，比特币官方网站 https://bitcoin.org/ 还发布了比特币节点的参考实现，Bitcoin Core支持所有比特币功能（例如，钱包，网络路由，矿工 ）。

但是，Bitcoin.org仅针对PC用户（Windows，Mac OS和Linux）而非手机用户开发并发布了BitCoin Core，这意味着市场上所有比特币钱包App均由其他方开发。更糟糕的是，比特币未规定任何检查机制来检查和强制执行比特币钱包App的合规性。因此，这引发了两个问题：这些比特币钱包App是否仍将比特币去中心化？如果不是，用户是否知道违规？分别对10种流行的比特币钱包App及其用户进行了安全性研究和用户研究。结果表明上述两个问题的答案都是“否”。

有三个发现，首先某些钱包应用程序未提供理想的比特币去中心化功能。这些钱包应用程序不允许用户直接访问比特币网络。所有比特币交易必须通过安全通道（例如TLS）传输到应用程序开发人员部署的中间服务器。将这些应用程序称为违反比特币去中心化的非P2P钱包应用程序。其次发现，一些非P2P钱包应用程序的用户不能完全控制他们的比特币钱包私钥。因此，用户在其比特币地址中存放的比特币可以在未经用户事先同意的情况下由其他方转移到其他比特币地址。最后但并非最不重要的一点是，大多数钱包应用程序用户都不知道存在违反比特币去中心化的行为，这些用户可能遭受各种比特币钱包欺诈攻击。

验证：进行了一个实验来验证此漏洞，首先...