---
title: 重要可执行程序完整性保护和来源真实性验证到底能不能用消息鉴别码？
url: https://mp.weixin.qq.com/s/3KNPpbvE-52AIuUElbyiUw
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:08:05.636552
---

# 重要可执行程序完整性保护和来源真实性验证到底能不能用消息鉴别码？

# 重要可执行程序完整性保护和来源真实性验证到底能不能用消息鉴别码？

原创

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

重要可执行程序完整性保护和来源真实性验证到底能不能用消息鉴别码？

重要可执行程序的密码应用技术要求主要由完整性和真实性两个密码安全功能维度构成。

首先，来看第一个文件，GB\_T 39786-2021 信息安全技术 信息系统密码应用基本要求

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe2ca0Qye9eZMg9YE39bibrOIcXqnRzDgzkflvM4FoQ2Nzp8a5k5kfjIUjnYhyP9OxKvcWDggdplGfn7C3AZLWnYeMn0Q3bxlTibc/640?wx_fmt=png&from=appmsg)

完整性保护

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe29vg1N7aX2sP1msb1Yhq7S0ToxHNIGALgjCHibZn13kyqxQaHUb96v5kxKgjebicGpTbibkvXctHhODF2agr0RCf4BLMVHmYIoicQ/640?wx_fmt=png&from=appmsg)

真实性保护

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1nF8cKVKK6S494nRia0okMLia0gxu56bgD4w7RWGAWzGY1c444JRpzpTO1cib8l6FNyra2zDvBIs81k6d2rnnBH6k1Vjw0vj12fk/640?wx_fmt=png&from=appmsg)

根据文件解读，同时保证重要可执行程序的完整性和真实性，则采用密码技术：基于对称密码算法或密码杂凑算法的消息鉴别码机制、基于公钥密码算法的数字签名机制。

然后，来看第二个文件，GB\_T 43206-2023 信息安全技术 信息系统密码应用测评要求（GM\_T 0115）

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe0U9qKsPODZtsedM4KG8Voviadjo4PT1zlvohV5ZPH9ibItsmE3Gckly43wicugC0wEibT8u0eh7mOzbn8c5IPsffVWWKrB5IeX9oQ/640?wx_fmt=png&from=appmsg)

根据文件解读，同时保证重要可执行程序的完整性和真实性，则采用密码技术：基于公钥密码算法的数字签名机制。

到这里，标准去掉了基于对称密码算法或密码杂凑算法的消息鉴别码机制，那么，重要可执行程序完整性保护和来源真实性验证到底能不能用消息鉴别码？

回答这个问题之前，我们要先看看，为什么去掉了基于对称密码算法或密码杂凑算法的消息鉴别码机制？

主要原因可以归纳为2点，对称密钥分发困难+验证者可以篡改。

第1点，我们知道不论是基于对称密码算法的消息鉴别码机制还是基于密码杂凑算法的消息鉴别码机制，均需要采用对称密钥实现消息鉴别码。

当可执行程序属于公开下载的程序，例如Yakit-1.4.9-1016-windows-amd64.exe，软件下载量得到千万级，则对称密钥分发成为一个问题，把用于消息鉴别码生成的对称密钥同步给千万下载者，这根本不切实际。

哪怕是这一步不考虑，验证的人验证的同时只要拿到对称密钥就可以篡改计算新的消息鉴别码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe1YM1jdxzX9jUiaAjBDZyamhfcfREfwyIicY6E46d6Qk93JMfgN71BgfE4QME1Q8kjPA2tNZvibpPSRRHg5AloNF0ABHc6fpy9WT8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1jX8muVC9FLxB7NQf4cB6QhRbrB3l4Vm9RE1F80TLghpiarlD3qaJw22mB3ZP5PZUAZia7b7HnWtyiaW2lSFsEx2VTmIwqicBGNiaM/640?wx_fmt=png&from=appmsg)

然后，来看第三个文件，GM\_Y 5015-2024 政务云密码应用安全性测评研究

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe3HibfAHE8DuoLNniaNwaCfSvQONSt5cP0lwPOyJYrgY0LfkyvQdfC1NwUTSndsal6kAYTgbRnyyzWB2PmHCZH1eFJYBNkR2nia9Q/640?wx_fmt=png&from=appmsg)

根据文件解读，同时保证重要可执行程序的完整性和真实性，则采用密码技术：基于公钥密码算法的数字签名机制。

然后，来看第四个文件，信息安全技术 信息系统密码应用设计技术要求（征求意见稿）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe3oibqaTBhiaQGhZ621cgEz5MC4O5Mgn7zs3amiccYRicDDStE0URsLEia9qP52f3Lv4FywibQeLgcR6B3eCvZGsUUhHTzDpK0W59Fsw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe1qpsTCCNkFJNY5MOLgocHlwEuF9XTwDytYsX9h8XsnyAetAq5gGcAD4Gu6xFrOQ6PqQuEP7JibN3EmrCcINVPO7bMupYrSkKQY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1ib4eNbsib9H8CVrudFVb1hyFxtPBxicU7n7qIOibjLicYXv3W0lklzWHbnSibfLK47gNNmf45hMDiaFeexDc1telgOGhyia4jbsFQicKc/640?wx_fmt=png&from=appmsg)

根据文件解读，同时保证重要可执行程序的完整性和真实性，则采用密码技术：基于对称密码算法或密码杂凑算法的消息鉴别码机制、基于公钥密码算法的数字签名机制。

然后，来看第五个文件，民用航空重要网络和信息系统商用密码应用要求（征求意见稿）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0jLGw7a3qeKW2mbCAAdLBLGaiaLysxQXHm4NLaPxESBI3WUERTZVbolQaHfwqxXIFexfkdPDYOOl7xphrRGcgCOpiakg3hCZAt4/640?wx_fmt=png&from=appmsg)

根据文件解读，同时保证PLC控制器、RTU等工业控制设备的程序下载、固件升级的完整性和真实性，则采用密码技术：基于公钥密码算法的数字签名机制。

然后，来看第六个文件，GM\_Y 5011-2024 车联网密码应用标准体系研究

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe3UxXPTJQYpA5ueBh1Xiad6S3RxDRhfJrhDResgOoYwPVribj366wWbeibtR5lexzIXjDuXZYVecN0Fj4bak7OTFSUHtuVY2mTjgc/640?wx_fmt=png&from=appmsg)

根据文件解读，同时保证重要可执行程序的完整性和真实性，则采用密码技术：基于对称密码算法或密码杂凑算法的消息鉴别码机制、基于公钥密码算法的数字签名机制。

好，综合这么多文件，那么，重要可执行程序完整性保护和来源真实性验证到底能不能用消息鉴别码？

我个人认为，需要分情况考虑，如果是普通的exe可执行程序，需要分发给多人并且人员不可控，则需要用基于公钥密码算法的数字签名机制，如果是车联网这种物联网设备中的可执行程序，由于程序属于同一下发，且可以统一分发对称密钥，验证者即使篡改也无法分发程序，则可以同时使用基于对称密码算法或密码杂凑算法的消息鉴别码机制，但是，民航、工控设备这种比较重要的则只能使用基于公钥密码算法的数字签名机制。

这个思想在0028里面也有对应，我们来看一下GM\_T 0028-2024 密码模块安全要求（GB\_T 37092-2018）

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe0KKS1B2q9rjYxbqmibyRKyLwOozuGfGIHaicMicPKqfyyJQUBXtj9p0NkfhoI7MXAxkM14ON9IaR5Pvgyqx9AmibpPCLXuEcia2QKs/640?wx_fmt=png&from=appmsg)

安全等级2级的软件或密码固件可以使用基于对称密码算法或密码杂凑算法的消息鉴别码机制、基于公钥密码算法的数字签名机制，而安全等级3级及以上的软件或固件只能使用基于公钥密码算法的数字签名机制。

那么，对于可执行程序的数字签名机制如何进行验签？

我们以Yakit-1.4.9-1016-windows-amd64.exe为例

整个文件的杂凑值

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe338oibLicRnmaeK1DuzjnNAZpxicLI2dMBVwY8Ia7kic4tpyyVBp82IqrEOqhaf4qlG18btUbicNX1Cpx0JPI4maWpS9BickPzZdE5U/640?wx_fmt=png&from=appmsg)

SHA-256：

cbe52ca588b9b40f6048ccc3c13b2d8ff578a14d19971b112a1989dd3d4b4643

签名公钥

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe07NYFh7TRs2yJ7GodmGaia8Gm913XN2JrkCvmvebmlF39cpGicxsE25Nw8oIicOWhn51LPDTWTa52VxBhUHjo36f2ukJbv7eBrPo/640?wx_fmt=png&from=appmsg)

SubjectPublicKeyInfo DER（550 字节） —— 完整公钥结构（算法标识 + 位串）

```
30 82 02 0a 02 82 02 01 00 b7 3f da 0f ca 3a ec 37 47 59 7e b4 71 bc c9 7a 7f a9 ea d0 60 6c 20 ad 30 10 7b fd 65 60 74 32 04 b7 d5 09 ec c5 d1 a5 cf 3f 83 48 7d a5 3d 43 91 82 28 fa 99 4b f8 06 f7 a0 c0 15 8c 7a cb 75 8a 0d 84 b6 52 a6 71 1f 36 3e 0b 91 d6 23 93 68 6c 93 7d 15 06 7a 2c 21 94 00 99 87 0b 21 01 4b 82 fa f7 57 73 70 a3 70 3a 0e db c9 83 65 98 fa 6a f8 98 dc 32 98 85 75 e7 fc 7b 02 55 3b 3a 76 64 0c e6 c6 c7 ad 57 78 04 11 8d 7c c5 65 f0 f6 26 63 50 95 a4 73 71 9c 61 92 d1 42 da 0b fc 47 a6 84 45 b4 bf a3 7e 6c 46 f6 8b e0 cd 94 39 f1 c0 8f 27 f1 6d 25 94 61 86 1b f0 34 cd 46 59 b6 b4 84 2d 22 d1 0f b8 e7 de a7 c3 a1 7c 67 01 90 5a 69 c7 1b 16 50 f3 92 b9 54 97 c0 bb c3 f0 0f 8d b1 88 d7 81 d7 f4 fe 8a ec 19 f3 45 8d 66 65 ad 63 15 5b 08 cd a2 64 8a d2 4e 4b 43 27 4e 5b f8 ab 39 bf b3 cc e9 bb 15 65 a3 9d 88 4b 13 2d ca 72 a2 d9 7b 6c f7 a7 6c 16 22 df a1 16 a8 46 8f b3 c3 08 81 e1 bf 48 41 f6 c6 e1 1d 33 30 89 9a bf 04 e5 5e 9b 6a 8d ad 7f 4c 29 15 7a 42 f6 1f 22 00 f9 07 46 4e 03 41 02 c7 a5 0d 46 dc 2c 5c 7b dc 4a 41 46 d1 84 d8 8d 3a 8c c2 2c cb e6 e8 02 1d 2e 9d 16 56 3d d6 99 7c af c0 c5 4d af 3f 40 ed e5 76 48 2d 60 55 7d 93 5b c6 90 4c 21 6a 61 dc bd 38 6f 07 52 5b 20 29 e3 ca a3 70 cb 9e 01 30 ab 76 c4 fa 2a a9 d6 ee e7 96 60 8a 8f 84 ff 69 da 38 bc d2 c2 6f 9c 98 09 07 ed 06 e5 6b 5a da 55 d0 09 36 48 26 ff 3b e3 8e 7a 88 4b 24 db 62 cf 7f bc e8 6e 08 ea ce 88 09 a9 78 76 64 ac 0e 73 0c 3d 8b 0b e9 20 65 d2 13 2b b8 16 60 b2 96 0b 51 35 85 a1 d6 aa 3a b4 40 07 e2 af ed 6e ca 22 d5 01 19 f9 68 f2 3e 8c dd 18 a1 7f 02 03 01 00 01
```

签名者用私钥对“文件摘要 + 签名属性”做 RSA 签名，验签者用证书公钥还原并比对摘要。

签名原文 — signedAttrs 的 DER 编码（135 字节）

RSA 直接签名的数据；即 RFC5652 SignedAttributes 重编码为 SET OF，对其 SHA-256 后由私钥签名。

```
3181843018060a2b06010401823702010c310a3008a0028000a1028000301906092a864886f70d010903310c060a2b060104018237020104301c060a2b06010401823702010b310e300c060a2b060104018237020115302f06092a864886f70d01090431220420211c462dd17b528306cd4024ffc67cbae21aab6996cc750f39760f2530838d8b
```

签名值 —encryptedDigest （512 字节，PKCS#1 v1.5）

```
2673d67985eaebe2285eec89d442177bf4ee3a2c7be0595323ab9ff0124e51be413aeed61b750d1a944975e1a9c9a8e5b0fe6ec074b68b8c8e7454f90c2b697e43c9dcb195ac5f300a2899927c6f562d815aade63d12924612c90e7a62d66e30574e51d043ed77d5a208ce5918efa5eb7745b6a3664c33591faf2a47f05abd26db5dbac3449f729db3847701a2b66f8e0ee7903ae89d621549751dbb80e69617a04e9ad84e6fbd42d5af480a5942d7e96162b73efbf595ab820ef7a40757c7220f8472618ea1b702f122ca8067923e6d32eaca5418df9e8ccbcdd59859f373e2032a46dd41cac8f75225170586ca0e04b0d8addee399b3e49db9c5e0822a91473194948ec0b82f3ca5f57e8c9d72c02ffe395ba87a90791923f790194e918cceb4b28d4e3c190bf1ac26f5d7284522bbde92c65524675f79d7d48e14ed6844e14ac38977a8e2e018951536e6c367d142a4e819f6d020bb3edb1cf9e424262505ba97c3d268ab396fa2db3918667a260bbc107d2a3191c6141a65c70bfc8eebc46ffe5fe35ed704ef103ed554ee21cd816d9ea977428ece1a6787d154045947fecdd96b20013c77dd98f195771238a9908b5043e5f1e4860a77e96ac2eab4112774fc68dfe61f3ed6e08d480c309828553ee6aebdae3f9481ff2555f5c24e73ac849f9ff894617790591de7cb203aea4b4d83f2d1ed943e67ece982ec035e541e
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZaibroIiatwe0EXNQicDiaV055CibAibRa4O0RibUzDZxicJicScj3JGnPfcOJWvZPbPey7rEdQuaXCF1pcYy9ZFicicibbmlJJzax0YxPepT0AiaLVfbKRU/640?wx_fmt=png&from=appmsg)

时间戳

原文

```
3181d1301a06092a864886f70d010903310d060b2a864886f70d0109100104301c06092a864886f70d010905310f170d3236313031363039343735395a302b060b2a86...