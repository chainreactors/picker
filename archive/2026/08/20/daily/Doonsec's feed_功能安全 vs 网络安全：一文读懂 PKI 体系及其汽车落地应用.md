---
title: 功能安全 vs 网络安全：一文读懂 PKI 体系及其汽车落地应用
url: https://mp.weixin.qq.com/s/XNcQWtG-xC-TkNoCYxl_0w
source: Doonsec's feed
date: 2026-08-20
fetch_date: 2026-08-21T02:59:43.838699
---

# 功能安全 vs 网络安全：一文读懂 PKI 体系及其汽车落地应用

# 功能安全 vs 网络安全：一文读懂 PKI 体系及其汽车落地应用

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247576684&idx=2&sn=99b4244a2b1c95bd46442f3151ac6b4b&scene=21#wechat_redirect)

**01**

**基本概念**

**1.1 功能安全与网络安全**

“功能安全”对汽车行业的工程师而言，是老熟人了，标准流程体系都很完善。随着汽车的“网联化”，“网络安全”出现了，所以很多人第一反应是“这两者有什么区别”？

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaA0tVPlISo77icJV1DBnlZXkrujKeqGRTA3iaEIUR5C0ibRHicibiaskEibUPDeYQXic6DLfhu5D7Dic2zvqg8Hbs0Cc7scTyz1S7CbVNeM/640?wx_fmt=jpeg&from=appmsg)

网络安全：网络安全是指网络系统的硬件、软件及其系统中的数据受到保护，不因偶然的或者恶意的原因而遭受到破坏、更改、泄露。

功能安全：是指电子电气系统在设计或实施上受到保护，从而避免其发生故障后导致的人身、财产损害。

这两者的区别在于“Cyber Security”防范的是外部的恶意，如车主的好奇心、黑客的攻击等；而“Functional Safety”防范的是失效/故障，这个故障可能是自身老化/设计导致的，也可能由于外部的常见工况导致的，如沙尘、振动、下雨等。

这两者的也是互相关联的，比如说网络安全也可能导致功能失效，因此建议各个有功能安全要求的件，最好也考虑一下网络安全。这一块很多文章都讲的比较多，大家可以自行搜索一下。

**1.2 网络安全防护的目的**

上文中提到网络安全防范的是“外部的恶意”。对一个系统而言，“外部的恶意”是存在极大的不确定性的，取决于以下几个因素：

* 当前系统对攻击者的价值
* 当前系统与攻击者的关系
* 攻击者的心情
* 攻击者的兴趣
* ....

这些因素除了第1条之外，其他的都无法预测、无规律的，除了劝你为人低调一些之外好像毫无办法，所以，我们只能针对“当前系统对攻击者的价值”对“外部的恶意”来进行评估。而攻击者的目的呢，相应的我们也简化为理性的“获取利益”。

所以，从理性的角度上来讲“网络安全”就是一场“道高一尺，魔高一丈”、“无止尽”的攻防游戏。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCOTLVWib1rYPGxNWtPdagRMVA1PrE3xQhrmJ1Tso9ibPcibVcttfKkosrLeRbibMHOibwicfS8vbib3LdxWdMgrKQc3ibADCwmJ3xmTYI/640?wx_fmt=jpeg&from=appmsg)

而网络安全防护的目的与其他的攻防游戏一样，是“让攻击者付出的代价比攻破此系统带来的收益低”。这里，非常典型的例子，就是“人民币的造假”。人民币的造假现象现在相对比较少，是因为：

* 要想造出真的人民币，比如说仿制100元人民币，单张的制造成本要高于100元
* 央行不断推进新版人民币，采用新技术，始终将仿制成本高于安全线
* 造假的人民币，一旦被抓获，要处三年以上有期徒刑甚至无期徒刑

从上面这个例子，也可以看出，这个攻防游戏是“无止尽”的。因为随着技术的进步，攻击者达到同样的攻击水平，需要付出的成本会越来越低，这时网络安全防护则需要不断升级自己的技术，重新提高攻击者的攻击成本。

OK，讲了这么多概念，接下来讲一讲干货，现代电子商务的基石——公钥基础设施PKI

**02**

**PKI与非对称加解密**

公钥基础设施这个名词讲起来比较拗口，要想把它彻底搞清楚，大家可以买一本书去看，从底向上，我将其分为5个层级。为避免过程过于枯燥，先从最常见的”数字证书“讲起。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAafxovbiaNtySeqJuN1Jr3TiaVjcG8to4s1Au4kAmn2DT3QNPCBr0tmL5aia5XUt4x7NpPnJrtqj2kibicmdB06mjiavo62EibEicLYb0/640?wx_fmt=jpeg&from=appmsg)

**2.1 层级四：数字证书**

现代电子商务或网络通信的一大问题在于，如何在不可信的环境中做到身份认证，即"如何证明我是我?”在中国，用“身份证”，在数字领域，用“数字证书”。

咱们可以随便打开一个网页，如果是chrome的话，可以点击网址左边的“锁”，打开其“证书”，主要可以看到如下信息。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaARlKQlCG92jwQML8spETXBNzYtWqOOtgJ0HzppBNxGxren33992HJBLmLW57RJtibFN2jgTjQy6DSPOhibkEsSL0Xawicq1WiarsA/640?wx_fmt=jpeg&from=appmsg)

数字证书的信息大概包含这么三类：

1. 使用者信息

* 使用者：最重要的域，目前一般为域名，用户个人使用则为姓名。
* 公钥：非对称加密中用户公开的那个密钥，谁都能看到
* 有效期

2. 颁发者信息

* 颁发者：谁颁发的这个证书？
* 颁发者的签名：颁发者对该证书的所有信息的数字签名，表明他对这个证书的真实性负责。

3. 其他：如证书的版本号、序列号等，在此略过不表

我们在打开一个网页时，如果是HTTPS网址的，浏览器会自动检查网站证书的有效性，如网站的域名与“使用者”是否匹配？证书是否有效？证书的颁发者是否有效？等等。若网站证书有问题，浏览器则会显示相应的警告。若此证书有效，则浏览器会开始使用证书内的信息（主要是公钥），用于与其进行通信。

**2.2 层级二及三：非对称加解密及数字签名**

数字证书的关键在于公钥，以及颁发者的签名。为什么公钥可以公开？为什么数字签名就可以代表颁发者？接下来讲这两个问题。

非对称加解密就是指一种特殊的加解密算法，这种算法的加密密钥（公钥）和解密密钥（私钥）是不一样的，且由公钥是极难推断出私钥的，即使有大量的明文和密文对也一样。常见的有RSA算法，及椭圆曲线(ECC)算法。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCfjPAJfxdD7n3Sy7YGDpPmfBN2fAOIOjPtIibsFfwwhjDhMT6n3liadJtRZCuEH1H9bwF98KcVeF83PdGdTC08bv71DF1M0RPHs/640?wx_fmt=jpeg&from=appmsg)

非对称加解密之公私钥

因为有一对不一样的密钥，所以其中一把密钥可以作为公钥公开出来。私钥需要自行妥状况保存，比如说存在加密机中。

这样的话，如果A要给B发送加密消息，那么就B的公钥加密一下，发送出来，只有A才能用自己的私钥解密。

那么公钥可以用于发送方加密，私钥可不可以用于发送方加密呢？也可以，只是不叫“加密”，叫签名，因为一发出去，大家都可以解密。下面是个例子：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDocybklsQrGzt6icbLcrDRyYibNkxxbrT6REUeRjkJP3Oex3ufrp4TgwlR7JEP4VZiclHYq0TcP7AwFKU5Y18iaJ4ictRVyB1ReFlQ/640?wx_fmt=jpeg&from=appmsg)

上图中，B使用公钥验签后，发现生成的摘要与原摘要一致，就算验签成功。因为能使用A的公钥解密的信息，只可能是用A的私钥加密的。由于只有A才会拥有A的私钥，所以可以确定“这段明文”确实是由A发送的。

**2.3 层级五：PKI体系**

前文中反复提到了“使用A的公钥验签”、“使用A的公钥签名”，那么如何获取A的公钥呢？获取到了之后，如何相信A的公钥真的是A的公钥呢？这就需要使用到PKI体系了。下面是百度中的定义：

公钥基础设施是一个包括硬件、软件、人员、策略和规程的集合，用来实现基于公钥密码体制的密钥和证书的产生、管理、存储、分发和撤销等功能。

其核心是证书的产生和分发层级：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaBRXIzqGgx7ooxQfvRAjEiccQZugkhjskNblXsQRbsbASCNOibNQLP4j48aruZKzqUy33t7wzrGAAAKQUzmfBj15ewLuf61nDSYY/640?wx_fmt=jpeg&from=appmsg)

关键的流程就两个：

1.证书的签发流程：即怎么样才能拿我自己的证书呢？简单的说，填个表，找个子CA，付一笔年费，就可以拿到了，上面写着大伽A证明大牛B证明凡人C是凡人C。复杂的说：

* 全世界有大概几十家左右的根CA（Certificate Authority)，计算机上都会预置这些CA的数字证书。比如Amazon、Verisign这种，他们有一整套的机制保证自己是可信的。基于此，他们有自己的数字证书，及与之匹配的私钥。
* 若想建立自己的子CA，则可向这些家申请，要每年付不菲的年费。那么这些根CA会给你的子CA生成一个私钥以及配对的数字证书（公钥）。
* 若普通用户要获取自己的数字证书，则向子CA申请即可，流程与上一步一样。

2. 证书的信任流程：即我为什么相信你是你呢？简单的说，就是因为你手上拿了个证明信，上面有某某单位的公章，我因为相信这个单位，又相信这个公章不是伪造的，所以相信你是你。复杂的说（拿http://www.bing.com为例）：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaCia8xkfOkiaDgfnf2RaV33YxGgw4eOotVOEAuvF0A200lxOibFxicYHYAxSbPMBYOaibFrC7uLYJvE9tCwIHK3ibhxwyzVQpsibka2fo/640?wx_fmt=jpeg&from=appmsg)

* 先查验DigiCert Baltimore Root的证书，是否与我本地预置的证书一致。
* 再检查Microsoft IT TLS CA 2的证书上的数字签名，是不是真的是由DigiCert Baltimore Root生成的？
* 再检测http://www.bing.com的证书上的数字签名，是不是真的由Microsoft IT TLS CA 2生成的？

由以上两个流程就可产生分层级的信任关系，而在不可信的网络中建立了信任关系（信任锚）之后，其他的应用业务就好开展了。

PKI体系还有另外一些问题：

* 证书的吊销——给某人发了证书后，这人用此证书从事非法经营怎么办？把他的证书吊销了。具体的方法有OCSP及CRL。
* 证书的更新——给某人发了证书后，这证书过期了咋办？如何更新呢？所以证书的有效期的选择也需要谨慎考虑，太短的话频繁失效，更新起来麻烦。太长的话，它又有可能出现私钥的保存问题。
* 私钥的存储——私钥是信任的核心，如果私钥被他人窃取或复制，那么整个信任体系就失效了，特别是ROOT CA的。所以，私钥最好不要离开生成的机器，且在物理上与外界隔绝，如使用加密机：私钥始终不可见，只可重新生成，不可拷贝等。

**2.4 层级一：NPC问题（附加题）**

前文有提到过，在知道“公钥”及很多“明文密文对”时，也很难推断出“私钥”，这是为什么呢？此节简要讲一下这个问题，这属于密码学的范畴。

RSA的数学基础是大数的分解问题，属于NPC（非确定性多项式完全问题）问题；椭圆曲线的本质是离散对数问题，也属于NPC问题。

NPC问题是指这样的一类问题：无法在多项式时间复杂度内计算出问题的答案，但一旦知道答案可在多项式时间复杂度内验证答案是否正确。用计算机的语言表达是指其时间复杂度>O(n^a)，可能为指数级O(2^n)，甚至O(n!)。当需要求解的n较大时，这类问题的求解就远超出当前计算机的计算能力。

以RSA为例，当前使用较多的密钥长度为2048位，超级计算机需要数十年才能破解。即使随着科技发展2048位被破解了，那就用4096位吧，破解所需要算力上升2^2048倍。而加密、解密所需的代价只上升几十倍（具体没算过，但NPC问题的验证为多项式复杂度，可控）。

所以，只要NPC问题未被解决，即证明其可转化为P问题，PKI体系仍是坚如磐石。因为即使量子计算机可轻松破解2048位的RSA密钥，那大不了就增加一点难度吧，用4096位的。

**2.4 PKI在汽车行业的应用场景**

PKI体系在汽车行业的应用场景非常广泛，如远程车控、近场车控、安全启动、Ethernet通信安全等等。在此处讲一个优先级最高的“远程车控”的实例。

1.企业应该先行建立自己的PKI体系，即引入一个PKI供应商，将证书的颁发、申请、吊销等公用模块建立起来。接下来，在其之上，建立各应用的流程。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAYfLjz53ObmCP6hSibHEuk82GpRkjdtib2OYaBvmREeQkI1USua4BaTP6dfaPqmuaY7gUIGE6ZiaADBLg2ofJwWQDQ8XrupMPFjo/640?wx_fmt=jpeg&from=appmsg)

2. 手机端、云端与车端Tbox，都在本地生成自己的私钥，并在云端申请完自己的证书。这也需要制定相应的业务流程。

三端都需要妥善保管好自己的私钥，手机端可以将私钥存储在TEE中，云端可存储的选择会较多，车端可存储在HSM或TEE中。若没有这些硬件的存储方式，可以使用软件的白盒加密方法，安全性也有一定保障。白盒加密也就是说即使遭遇白盒攻击，其密钥也较难被破解。

3. 大家都具备证书与私钥后，业务流程就变的相当简单：

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAibuPW56SbRAbgfDFxOl4Yfia4PcQwODEohlfGym7jjcHMPbJXBrW60lvaNxw1SpibcWZeXAcabKz3pGMicMBGR2v0rUm6kGLcMXs/640?wx_fmt=jpeg&from=appmsg)

* 云端与车端由于交互较多，建议两端通过双向认证交换“会话密钥”（对称密钥）。因为对称加密要比非对称加密要快上千倍，根据密钥长度不同会稍有变化。交换会话密钥的流程可参考TLS的双向认证的握手流程。
* 手机端将车端指令发给云端，并使用自己的私钥进行签名。云端收到之后，使用手机A的数字证书，进行验签。
* 云端将车控指令用协商好的“会话密钥”加密后，发送给车端。车端验证后，即可在内部执行。

在采用PKI体系之前，业内的“远程车控”也有解决方案，只是这些方案的根基都在于“方案设计”的保密性，无法防范内部员工或离职员工的攻击。而基于PKI体系的方案，不依赖于任何个人，没有脆弱性。

来源：知乎

https://zhuanlan.zhihu.com/p/237155609

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247576684&idx=2&sn=99b4244a2b1c95bd46442f3151ac6b4b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMW...