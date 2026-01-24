---
title: 在智子的监视下，如何好好的聊天？Signal协议简介
url: https://mp.weixin.qq.com/s/yHUe9XeO1Nzi8RJuKcbuew
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:29:13.669604
---

# 在智子的监视下，如何好好的聊天？Signal协议简介

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PicDhHpwdziaicgDUJlUpLicGF7aS4goOkR74aPe8tySPOmNrEvD64IuCWKvR4e5RQ1Mia61G3bicQ47jZcp5JNbC1NA/0?wx_fmt=jpeg)

# 在智子的监视下，如何好好的聊天？Signal协议简介

原创

Wh0Am1
Wh0Am1

联想全球安全实验室

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/mmbiz_gif/Z47EleuMzjvibm0lsCqZSm1P8ciar3tZZfia6GLmnJhIb2Ja38U1Wn8UNPR8WfJkpUcEzEumFWn4oXOa6MxgojVag/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/81KNibIyqq5K9KicNPrdic0TmnmpBXXlrj1QPux1Z8k2qFjoN7GBsUWypPUDs6Rk8lE8aYfoNjaL2xbenPfcG96eA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/81KNibIyqq5K9KicNPrdic0TmnmpBXXlrj1iaBkyXxldJnu5oibDCc6m545lia3yIUr1OPGCY0gFvF6D0T50Nfv1ujnw/640?wx_fmt=gif)

**在智子的监视下，如何好好的聊天？****Signal协议简介**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/81KNibIyqq5K9KicNPrdic0TmnmpBXXlrj1DFng8b4qBursN2TvY6NLPLsBDn79dMzTYzf6ib2d9uWMPxRmw2Aveyg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/81KNibIyqq5K9KicNPrdic0TmnmpBXXlrj1YCCHqv6iaBqZvcQ4RRZPnscC3Q2PV2kdAL3muzJeFT6lxtD0q9oERYg/640?wx_fmt=gif)

**引言**

危机纪元8年，罗辑已经悟出黑暗森林法则。但由于智子可以听懂人的语言，并且可以监听所有通讯方式，地球上的通信对于三体已没有任何秘密可言。那么罗辑如何把自己的所想告诉其他人来帮助他实现宇宙坐标广播装置？

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ikz78C0cbBGBkuRPAbWibk0v0bWMT1QVj7Ur6TOx1xP4SFLknnWn15CUAPGicq2YZNJdU3vOnibS7KFzbpcg50ZCw/640?wx_fmt=gif)

**01**

**Signal 协议**

这种情况就需要用到Signal协议了。Signal协议是一种端到端加密的通信协议，被广泛认为是目前最安全的通信协议之一。它的核心目标是确保通信双方的隐私和安全，即使服务器或第三方也无法解密消息内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaicgDUJlUpLicGF7aS4goOkR7uIcQYjl1O4dUN8ydQn0iadthxPkOHEQTw5k1iaVAuAjCCnSllvmJFRrA/640?wx_fmt=png)

图1：端到端加密示意图

Signal协议采用一次一密的加密方式。即便黑客获取了某个消息的密钥，也无法解密之前或之后的加密消息。因此，Signal协议能提供前向安全和后向安全。

Signal协议被广泛应用于国外主流通信工具中：

**·** What’s App

**·** Facebook Messenger

**·** Google Messages

**·** Skype

**·** Mixin Messenger

**·** Wire

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/81KNibIyqq5K9KicNPrdic0TmnmpBXXlrj1YCCHqv6iaBqZvcQ4RRZPnscC3Q2PV2kdAL3muzJeFT6lxtD0q9oERYg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ikz78C0cbBGBkuRPAbWibk0v0bWMT1QVj7Ur6TOx1xP4SFLknnWn15CUAPGicq2YZNJdU3vOnibS7KFzbpcg50ZCw/640?wx_fmt=gif)

**02**

**Signal 的历史**

Signal原本的名称是“TextSecure”的，是从OTR（Off-the-Record Messaging）协议逐步发展过来的。

2013年，TextSecure v1，开发者，Open Whisper Systems公司；

2014年2月24日，Open Whisper Systems推出了TextSecure v2，其之后被迁移到 Axolotl Ratchet 算法中。Axolotl Ratchet的设计基于OTR引入的临时密钥交换。

该协议的第三个版本TextSecure v3对加密原语和有线协议进行了一些更改。2014年10月，波鸿鲁尔大学的研究人员发表了对TextSecure v3的分析。在众多发现中，但总体来说，他们发现它是安全的。

在2016年3月，开发人员将协议重命名为Signal协议。他们还将Axolotl Ratchet重命名为双棘轮算法，以更好地区分棘轮协议和完整的通讯协议。

截至2016年10月，Signal协议仍是基于TextSecure v3，但做出了一些额外的密码学改进。

**·  2013 年：协议雏形诞生**

由Trevor Perrin和Moxie Marlinspike创立的 Open Whisper Systems 启动了协议的研发。最初版本为TextSecure v1，被应用于开源应用TextSecure应用中，为这款加密通讯软件提供基础加密能力。

**·  2014 年：关键版本迭代优化**

2月24日，TextSecure v2正式发布。此版本核心变革是采用蝾螈棘轮算法（Axolotl Ratchet），该算法结合了OTR的临时密钥交换技术与静音圈即时消息协议的对称密钥棘轮机制，不仅实现了离线消息这一重要功能，还提升了对消息乱序接收的适配性，同时简化了多人会话的加密支持。

2014年10月前，TextSecure v3推出。该版本调整了加密原语和有线协议相关内容。随后德国波鸿鲁尔大学的研究者发布了对该版本的安全性分析，虽提出了一种对该协议的未知密钥共享攻击方式，但整体认定其安全可靠。

**·  2016 年：正式更名并扩大影响力**

3月，开发者为了明确品牌标识，将TextSecure协议正式更名为Signal协议，同时把其中的蝾螈棘轮算法更名为双棘轮算法（Double Ratchet）。同年，牛津大学等机构的研究者发布论文，从学术层面证实Signal协议在密码学层面具备高安全性，这为其后续**被广泛采纳奠定了重要基础。**

**·  2017 - 2018 年：获行业认可与成立专门基金会**

2017年，Trevor Perrin和Moxie Marlinspike凭借Signa 协议的开发与推广，获得了真实世界密码学大会颁发的莱夫钦奖（Levchin Prize），该奖项认可了该协议在推动密码学走向大众领域的重大意义。

2018年，Moxie Marlinspike与WhatsApp联合创始Brian Acton共同成立Signal基金会，专门为Signal应用及Signal协议的持续研发提供支持，保障其作为开源加密技术的长期发展。

**·  后续发展：成为行业主流加密标准**

随着安全性和可靠性被反复验证，Signal协议被国外众多主流通讯应用采纳。例如WhatsApp 借助该协议为全球超十亿用户的会话加密；Facebook Messenge将其用于可选的 “秘密会话”；Skype也将其应用于私人会话加密；Google Messages更是默认对基于富媒体通信（Rich Communication Services）的一对一会话通过该协议实现端到端加密，使其成为即时通讯领域加密协议的标杆之一。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/81KNibIyqq5K9KicNPrdic0TmnmpBXXlrj1YCCHqv6iaBqZvcQ4RRZPnscC3Q2PV2kdAL3muzJeFT6lxtD0q9oERYg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Ikz78C0cbBGBkuRPAbWibk0v0bWMT1QVj7Ur6TOx1xP4SFLknnWn15CUAPGicq2YZNJdU3vOnibS7KFzbpcg50ZCw/640?wx_fmt=gif)

**03**

**核心技术与原理**

Signal协议的安全性依赖于以下两个关键技术：

**Diffie-Hellman密钥交换协议**

**01**

**Diffie-Hellman协议（以下简称“DH协议”）**

DH协议是1976年由Whitfield Diffie和Martin Hellman提出的**首个公开密钥交换协议**，核心作用是让通信双方在**不直接传输密钥**的情况下，通过公开信道安全协商出一个共享的会话密钥，后续可用于加密通讯内容（如AES加密）。

**其核心逻辑可以通俗理解为：**

1)  双方约定“公开基础信息”：比如共同选择一个大质数和一个生成元，这两个信息可以公开传输，被第三方看到也没关系。

2)  各自生成“私钥+公钥”：

**·** 甲方生成自己的私钥（仅自己保存，比如“3”），再通过公开的质数（例如“7”）和生成元（例如f(x) = x2 mod 7），计算出对应的公钥（比如“3² mod 7 = 2”），把公钥发给乙方；

**·** 乙方同理，生成自己的私钥（比如“5”），计算出公钥（比如 “5² mod 7 = 4”），把公钥发给甲方。

3)  各自计算“共享密钥”：

**·** 甲方用自己的私钥+乙方的公钥，通过相同规则计算出共享密钥（比如“4³ mod 7 = 1”）；

**·** 乙方用自己的私钥+甲方的公钥，同样计算出共享密钥（比如“2⁵ mod 7 = 1”）。

4)  关键结果：双方最终得到的共享密钥完全一致，但整个过程中，私钥从未传输，第三方哪怕截获了公开的质数、生成元、双方公钥，也无法反推出私钥或共享密钥。

DH协议允许通信双方在不安全的公共信道上协商出共享密钥。通过双方的私钥和对方的公钥计算共享密钥，即使攻击者截获了公钥，也无法推导出共享密钥。这种机制确保了通信的前向安全性。

**X3DH（Extended Triple Diffie-Hellman）协议**

X3DH协议是对DH协议的扩展，增加了更多的公钥参数以提升安全性。它通过身份密钥（IK）、已签名的预共享密钥（SPK）和一次性预共享密钥（OPK）实现异步通信，并有效防御中间人攻击和重放攻击。

**大致流程如下：**

1) 会话发起者从服务器获取接收者的公钥信息。

2) 使用DH协议计算多个共享密钥，并通过密钥衍生函数（KDF）生成初始消息密钥。

3) 消息密钥用于加密通信，确保安全性。

Signal协议中采用的是X3DH协议，以及PQXDH（Post-Quantum Extended Diffie-Hellman）协议，以确保密钥交换过程的安全性。X3DH协议的密钥交换原理，后面我们会单开一篇文章进行深入探讨。

**双棘轮算法**

**02**

**棘轮（Ratchet）**

我们先来了解一下什么是“棘轮”。如图所示，图中的齿轮只能单向转动，这就是一种棘轮。它的本质是一种**单向锁定或步进结构**——只能让运动（或状态）朝一个方向进行，无法反向回溯。比如自行车的飞轮，当你踩踏板时它带动车轮转，松开脚时车轮不会带着踏板倒转，这就是“单向锁定”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaicgDUJlUpLicGF7aS4goOkR74cwoWmcLqrsnzRyPicKAX6k8XBccibiaicib3A3ACsq2RGlPeoZgxPDNrFg/640?wx_fmt=png)

图2：棘轮（图片来自于网络）

在加密通讯的语境里，“棘轮”是个非常形象的比喻，核心意思是**“密钥只能往前滚，不能往后退**”。这意味着密钥只能更新迭代，旧密钥不能复用，且无法通过新密钥反推旧密钥。

通讯双方聊天时，每发出（收到）一条消息，就会自动生成一个新的密钥，旧密钥立刻作废。就像你和朋友聊天，第1条用密钥A，第2条自动换密钥B，第3条换密钥C……以此类推，这样就做到了所谓的“一次一密”。

**“棘轮”在Signal协议里的核心作用：**

**·  实现前向安全：**哪怕某一个新密钥意外泄露，黑客也只能破解用这个密钥加密的那一条消息，之前用A、B密钥加密的历史消息，因为没法倒回去获取旧密钥，所以永远安全；

**·** **防止密钥复用风险**：密钥不重复使用，就算黑客截获了多次通讯的加密数据，也没法通过比对找到密钥规律，进一步提升安全性。

**双棘轮算法（Double Ratchet Algorithm）**

虽然棘轮可以实现**前向安全**，但是如果某一密钥泄露后未及时更换，黑客就能通过KDF生成后续的消息密钥，无法保证**后向安全**。所以Signal采用了**对称密钥棘轮（KDF棘轮）**和**非对称密钥棘轮（DH棘轮）**的双棘轮模式，同时解决前向安全和后向安全。两个棘轮分别对应“对称密钥迭代”和“非对称密钥更新”，二者配合实现动态、不可逆的密钥管理，避免单一密钥泄露导致全量消息被破解。

**·  KDF棘轮**

* 核心原理：基于密钥派生函数（KDF）实现单向密钥链，就像接力赛跑：前一个密钥作为接力棒，通过KDF生成下一个新密钥，且只能向前传，无法回头。

* 具体流程：

a) 初始阶段，从X3DH协议协商的共享密钥中，派生出第一个链密钥（Chain Key）；

b) 每发送（接收）一条消息，就用KDF对当前链密钥做一次迭代：将链密钥拆成两部分，一部分作为下一轮的链密钥，另一部分作为当前消息的加密密钥（Message Key）；

c) 消息加密后，当前的消息密钥立即销毁，且无法通过下一轮的链密钥反推。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaicgDUJlUpLicGF7aS4goOkR7aEDZr0kcEtVZyEpadC5tzh2mZzn9ic0FNCia6Ms5Cu7GY7VOW9tF28rQ/640?wx_fmt=png)

图3：KDF棘轮（图片来自于Signal官网）

**·  DH棘轮**

* **核心原理**：基于DH密钥交换协议，定期（或按需）触发密钥交换，用新生成的共享密钥重置KDF棘轮的链密钥，实现动态更新密钥链的源头。

* **具体流程：**

a) 通信双方各自生成一对**临时DH密钥对**（私钥+公钥），并在发送消息时，将自己的DH公钥附在消息头部；

b) 当接收方看到对方的新DH公钥时，立即用自己的DH私钥+对方的新DH公钥，计算出一个**新的共享密钥**；

c) 用这个**新共享密钥**更新**链密钥**，相当于给KDF链更换了一个新的起点，后续所有消息的密钥都会基于这个新起点迭代；

d) 每次交换新DH公钥后，双方会立即生成新的DH密钥对，旧的DH私钥永久销毁，避免被复用。

e) 当一方完成棘轮步进并发送携带新公钥的消息后，需等待接收对方携带新公钥的回复消息，才会触发下一次自身的DH棘轮步进。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaicgDUJlUpLicGF7aS4goOkR7XgvD0JxCAB0rr5FWLU3u9QOntGqF8hicVLsf92U0ohicicEZawusOQRhg/640?wx_fmt=png)

图4：DH棘轮（图片来自于Signal官网）

以上是KDF棘轮和DH棘轮的一个简略介绍，其详细计算过程后面我们也会单开一篇文章进行深入探讨。

**两个棘轮的罗辑配合**

**03**

KDF棘轮和DH棘轮不是独立工作，而是形成 “动态互补”：

1.**消息加密：**主要依赖KDF棘轮，快速迭代消息密钥，保障前向安全，且运算效率高。

2.**定期重置密钥源头：**每隔一段时间（或每收发一定条数消息），DH棘轮会触发一次 DH密钥交换，用新的共享密钥重置KDF棘轮的链密钥，避免对称密钥链长期使用导致的泄露风险。

3.**离线重连适配：**若一方离线时，另一方发送了多条消息（此时，用KDF棘轮迭代的密钥加密），离线方重连后，只需通过消息头部的DH公钥，触发一次DH棘轮步进，就能同步最新的链密钥，解密所有离线消息，无需重新走完整的X3DH 协商流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/81KNibIyqq5K9KicNPrdic0TmnmpBXXlrj1YCCHqv6iaBqZvcQ4RRZPnscC3Q2PV2kdAL3muzJeFT6lxtD0q9oERYg/640?wx_fmt=gif)

**总结**

Signal 协议用双棘轮，本质是用 “两把单向的密钥迭代机制”，解决了端到端加密的核心安全痛点：

**•KDF棘轮**保证**前向安全**：不让黑客回溯破解旧消息

**•DH棘轮**保证**后向安全**：不让黑客持续破解新消息

二者结合，让加密从 “静态固定密钥”变成“动态单向密钥流”，成为Signal协议实现无法破解的端到端加密的核心技术支柱。

Signal算法通过多层次的加密机制和动态密钥管理，确保了通信的高度安全性，是现代加密通信的典范。

**—— end ——**

**往期精彩合集**

●[从 XSS 到 RCE：Electron 应用中的真实攻击链](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493436&idx=1&sn=06457e0fc73b9a16493921008063c84d&scene=21#wechat_...