---
title: Ronin 黑客计中计，你听说过扭曲攻击漏洞吗？
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497294&idx=1&sn=c3270820e15569f4e6af8e8059907419&chksm=fdde88c9caa901df83a7ded5c85c5426c22d5fe6d4c8050113d5b45566e51a67276b46e53936&scene=58&subscene=0#rd
source: 慢雾科技
date: 2023-03-29
fetch_date: 2025-10-04T11:01:43.220578
---

# Ronin 黑客计中计，你听说过扭曲攻击漏洞吗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTaRcxJEQ5QIGovRibb7MuBDR4UF5PGkZVa8ibExNPdCicKVcG9sKhjGibKQw/0?wx_fmt=jpeg)

# Ronin 黑客计中计，你听说过扭曲攻击漏洞吗？

原创

慢雾安全团队

慢雾科技

By: Johan

据慢雾安全团队情报，2023 年 3 月 13 日，Ethereum 链上的借贷项目 Euler Finance 遭到攻击，攻击者获利约 2 亿美元。

黑客在攻击完 Euler 后，为了混淆视听逃避追查，转了 100 ETH 给盗取了 Ronin 6.25 亿多美金的黑客拉撒路。拉撒路顺水推舟将计就计，随即给 Euler 黑客发了一条链上加密消息[1]，并回礼了 2 枚 ETH：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTaKpfOM0X6K7LTF3IeTYWrAEu7XQ7NeJ4lXtd2yXkM1wo6ia9nQJmaMAg/640?wx_fmt=png)

消息内容是提示 Euler Exploiter 用 eth-ecies[2] 解密这条消息。

**质疑**

按道理说在公开的环境下，如果 Ronin Exploiter 只是想加密通讯，使⽤公钥加密是最简单的⽅案。

* 公钥加密：

*C = {rG, M + rQ} = {C1, C2}*

* 私钥解密：

*M = M + r(dG) − d(rG) = C2 − d(C1)*

其中密⽂ *C*，公钥 *Q*，私钥 *d*，随机数*r*，消息 *M*。协议很简单，加密过程不需要⽤到的私钥，不存在私钥泄露的路径。

使⽤ eth-ecies 加密是因为⽅便还是另有所图？随后很快就有⼈指出 eth-ecies 存在安全漏洞，Ronin Exploiter 是想窃取 Euler Exploiter 的私钥。

是否真的如此？且让我们先分析⼀下 eth-ecies 存在的是怎么样的⼀个漏洞。

**扭曲攻击漏洞**

经过分析，我们发现 eth-ecies 使⽤了 "elliptic": "^6.4.0"，这是个 Javascript 椭圆曲线库，这个版本的库存在多个安全漏洞，其中⼀个就是扭曲曲线攻击漏洞(twist attacks)，这个漏洞的成因是在计算 ECDH 共享密钥时没有验证对⽅的公钥是否在曲线上，攻击者可通过构造⼩⼦群曲线上的公钥，诱导受害者计算共享密钥，从⽽破解出受害者私钥。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZeB1aBfEnrPHz9qjRKYvk7KMzic8Ha6K5QTYzQDpPAIvgnyvwglNHrpUNeLRSxHu6zmobES2eoItw/640?wx_fmt=png)

但是这个漏洞的利⽤难度是很⾼的，需要有⾮常契合的场景才能发起攻击，Ronin Exploiter 是否有机会发起扭曲攻击呢？

**ECDH 算法⻛险**

ECDH 算法是基于椭圆曲线加密的密钥交换算法。它与传统的 Diffie-Hellman (DH) 算法类似，但是使⽤的是椭圆曲线上的数学运算来实现密钥交换，从⽽提供更⾼的安全性。

下⾯是 ECDH 算法的步骤：

1. ⽣成椭圆曲线：在密钥交换之前，通信双⽅需要选择⼀个椭圆曲线，该曲线必须满⾜⼀些数学特性，例如离散对数问题。

2. ⽣成私钥和公钥：每个通信⽅都需要⽣成⼀对私钥和公钥。私钥是⼀个随机数，⽤于计算公钥。公钥是⼀个点，它在椭圆曲线上，并由私钥计算得出。

3. 交换公钥：通信双⽅将⾃⼰的公钥发送给对⽅。

4. 计算共享密钥：通信双⽅使⽤对⽅发送的公钥和⾃⼰的私钥计算出⼀个共享密钥。这个共享密钥可以⽤于加密通信中的数据，保证通信的机密性。

为了⽅便描述下⽂ Alice 和 Bob 分别代表上⾯双⽅，G 为基点，假设：

Alice 的私钥是 a，则 Alice 公钥是 A = aG；

Bob 的私钥中 b，则 Bob 公钥是 B = bG。

核⼼知识点在共享密钥计算⽅法，根据群的乘法交换律，他们只要获取到对⽅的公钥就可以计算出共享密钥：

*S = aB = a(bG) = b(aG) = bA*

如果 Alice 想要刺探 Bob 的私钥，她可以选择⼀个阶数*q*⾮常⼩（点的数量⾮常少）的曲线点 *H*（这个点不是对应任何特定私钥的公钥，但是 Bob 并不知道），由于群是循环群，Bob 在计算*S′  = bH* 时，他得到的*S′*  将在这些少量点群以内。Alice 不知道 Bob 的私钥*b*，但可以通过穷举得到满⾜ *S′ = xH* 的*x*，此时 *b ≡ x  mod q* 。显然 *x* 很⼩，最⼤为 *q*。

仅知道⼀个模余是不够的，要知道私钥是⼀个很⼤的数，最⼤可以达到 ![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTaoYsnIRJqlwnSibeH8dFibia4lXAhIO2QdiaqrIzd4xyvfFxqtb1f8vicBVA/640?wx_fmt=png)，⼀个模余在这个范围可以推出⾮常多的解，所以需要给 Bob 多个这类扭曲的点*H*让 Bob 计算，这样就可以就可以通过计算推出唯⼀解。

需要多少个扭曲点呢？这取决于每⼀次选择的阶数 *q*，需要阶数相乘能超过私钥的最⼤值，即满⾜：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTa2EK9MeLvOqPowYcySge83HiapPcZ9fpuuuwNhSZ04dT2QWKFq3qzCqQ/640?wx_fmt=png)

如果我每次选择的*q* ⼤⼀点，那么需要交互的次数 *n*就可以少⼀点，但 *q*越⼤意味着穷举的难度越⼤，所以这⾥需要根据 Alice 的运算性能做⼀个取舍。

**事件结论**

上⾯我们分析了 ECDH 算法的⻛险和攻击原理，我们再回来看 eth-ecies 这个库，实际上它使⽤的只是⼀个类似 ECDH 的算法，它在构造共享私钥时使⽤的是临时密钥，根本不需要⽤到加密⽅的私钥，所以并不会对加密⽅构成⻛险。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZeB1aBfEnrPHz9qjRKYvk7mdzBtRYU2ky66OLxBicaF1BGESVibE56eEes5cYPVmRGVKtiaHshGPkwA/640?wx_fmt=png)

那么有没有可能 Ronin Exploiter 是想利⽤社会⼯程学引导 Euler Exploiter 使⽤其它有问题的⼯具呢？⽐如我们熟知的 PGP 加密协议？

巧的很，我们很快就发现被⼴泛使⽤的开源库 openpgpjs[3] 最新版本 v5.7.0 还在使⽤了低版本的 "@openpgp/elliptic": "^6.5.1" ，更巧的是，它⽀持基于 Curve25519 的 ECDH 协议，故事本应该进⼊⾼潮，但经过分析发现，openpgpjs 的 ECDH 协议在实现时，和 Ecies 协议⼀样引⼊了临时密钥，即使加密⽅导⼊了私钥，也仅仅⽤于消息签名，⽽不会⽤于构造共享密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZeB1aBfEnrPHz9qjRKYvk7rY4iaIdcKRq1cInbShVNJG8xWngF7nWiauBUXbFNHD8xVBDLoOrkOgHg/640?wx_fmt=png)

故事结束了，我觉得 Ronin Exploiter 使⽤低版本 elliptic 存在的漏洞去隐秘的窃取 Euler Exploiter 私钥的可能性不⼤，⾄于那条链上消息，可能真的是为了共商⼤计，更进⼀步的图谋不轨需要更加⾼超的社会⼯程学⼿段了，但 Euler Exploiter 已经警觉。

**意犹未尽**

上⾯提到了扭曲攻击的原理，实际⼯程实现上仍然有⼏个问题需要解决：

1. 如何构造扭曲的点？

2. 当 Bob ⽤共享密钥*S'* 加密消息时，它并不会把 *S'* 传输给 Alice，因为根据协议 Bob 认为 Alice 是已经知道这个密钥的，那么 Alice 如何获取 *S'* 呢？

3. ⼤恶魔 Alice 最终获取到⼀系列共享密钥 ![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTaKTmNv0EicHia4hu5H7rzpfWL6KSkOt67bJY8mGlVM544bGQtjbw46UicQ/640?wx_fmt=png)

这⾥以 Curve25519 曲线为例，它的曲线⽅程是：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTa9YEWLReYiaLyxx3csBK5POSb90B2mR8DqG1SzClhQtzO8IhFqNiaFqxQ/640?wx_fmt=png)

我们随意改变其中的⼀个参数，得到⼀条新的曲线，⽐如：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTa18W4picebOkclRsreeNpnoBqnURyTI1hpd3OVMhAy6kqILzosgkERYQ/640?wx_fmt=png)

使⽤ sagemath 数学软件来表示[4]：

```
p = 2**255-19 E = EllipticCurve(GF(p), [0,48666,0,1,0])
```

然后我们计算它的阶数，并对这个阶数进⾏因式分解：

```
Grp = E.abelian_group() G = Grp.gens()[0] Gorder = G.order() print( "{0} = {1}".format(Gorder, factor(Gorder)) )
```

计算结果：

```
...= 2 * 3049 * 14821 * 19442993 * 32947377140686418620740736789682514948650410565397852612808537
```

选择 19442993 这个⼤⼩适中的数，⽤中国剩余定理创建⼀个含有 19442993 个元素的⼦群：

```
x = crt([1,0], [19442993, Gorder//19442993]) P1 = x * G
```

到这⾥我们就得到了第⼀个扭曲的点，把它当作公钥发送给 Bob，Bob 就可以计算第⼀个共享密钥：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTaBQMe5wcnybV93flHnEQJcwHTg0w1NEn5rpibgOnHugibSticpEibVScNCA/640?wx_fmt=png)

Bob ⽤ ![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTaCbDC8hewUBvwvu16J75iavumibszxvicUUToxVkKJ7rJOdibe4TvgHwAOA/640?wx_fmt=png) 加密了⼀个消息 *M* 发送给 Alice，Alice 不知道 ![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTaCbDC8hewUBvwvu16J75iavumibszxvicUUToxVkKJ7rJOdibe4TvgHwAOA/640?wx_fmt=png)，也不知道消息 *M*，但她知道 *M* ⼀定是⼈类可读的⾃然语⾔，所以她开始穷举 ![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTaCbDC8hewUBvwvu16J75iavumibszxvicUUToxVkKJ7rJOdibe4TvgHwAOA/640?wx_fmt=png)：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTaeQm4yVYvPMGibszOhaJ0hib00r9bYicohxmYDviaHFIvsNP5LHQYj1EJ5Q/640?wx_fmt=png)

并⽤ ![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTanaLq9TjR4R3Lz6zgdfibb0dF75tia3cLRohmaShDvoXhHBeWtKr4Mf0A/640?wx_fmt=png) 去解密密⽂，如果出现了⾃然语⾔，则此时 ![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTanaLq9TjR4R3Lz6zgdfibb0dF75tia3cLRohmaShDvoXhHBeWtKr4Mf0A/640?wx_fmt=png) = ![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTaCbDC8hewUBvwvu16J75iavumibszxvicUUToxVkKJ7rJOdibe4TvgHwAOA/640?wx_fmt=png)，![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTaiaXkTUl2XuiaLrI5QJd4VJsHCYqZibTFIkC16fCgmsDoJSyUorx2ibzvnw/640?wx_fmt=png)。

⽤上⾯同样的⽅法我们可以得到 ![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTadlrUeNg1T9CiaRX5KoStgy2d01MeoyAUcbaDDuJvRJSDfQrkcwCMytw/640?wx_fmt=png)。在我的实验中我⽤了以下⼏条曲线：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTadfwyib4e8I8pT1HM3Qd2U5POWRpKFuaziaRlIl4XGXHK0sLJzEcWkm9w/640?wx_fmt=png)

最终得到的结果可表示为：

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYu3MterdLcJibiaXmbXnGYTauxLrUsf3PhrfJKNicAuRv6QaqFiaJq4YNpicMEnEticmtP6Y9j4M5KY2vw/640?wx_fmt=png)

使⽤中国剩余定理即可计算出私钥 *b*：

```
x = crt([ x1, x2, x3, x4, x5, x6, x7, x8, x9], [ 19442993, 3645143, 184879577, 5110460161, 15272631587, 208137522259, 64927105657, 60824497, 213156431]) print(x == b) print(hex(x))
```

**总结**

本⽂我们通过⼀个不同常理的对话开始研究了椭圆曲线加密算法中的扭曲曲线攻击，分析了漏洞的存在的原因，虽然漏洞利⽤场景有限，但不失为⼀个很有价值的漏洞，希望能对⼤家的学习研究有所启发。

最后，感谢领先的⼀站式数字资产⾃托管服务商 Safeheron 提供的专业技术建议。

***参考资料：***

*[1].https://etherscan.io/tx/0xcf0b3487dc443f1ef92b4fe27ff7f89e07588cdc0e2b37d50adb8158c697cea6*

*[2]. https://github.com/LimelabsTech/eth-ecies*

*[3]. GitHub - openpgpjs/openpgpjs: OpenPGP implementation for JavaScript*

*[4]. Elliptic curve constructor - Elliptic curves*

**往期回顾**

[慢雾(SlowMist) 为阿里云(Alibaba Cloud) 的 Web3 安全工具提供技术支持](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497194&idx=1&sn=fb4dab91ce6d8f87d1ea29db16ba7ec6&chksm=fdde8b6dcaa9027bd33f517274ec59ad7ecc083192c41e22fc86296354aa92806f47376f2970&scene=21#wechat_redirect)

[火爆出圈的“最强 AI” —— GPT 是否可用于合约安全审计？](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497189&idx=1&sn=682e685052c146cec22e9260461e8119&chksm=fdde8b62caa90274edad632864adc81c8caa81f4d83cb6431b8d98809e2191ac4f094b7dec73&scene=21#wechat_redirect)

[慢雾(SlowMist) 与 HashKey Group 达成战略合作，打造前沿、安全的数字资产服务](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497146&idx=1&sn=cbd9ea95f7838de348625e165e10a16b&chksm=fdde8b3dcaa9022b36602cbc5fe22dd7832e90db22e45166f15a1...