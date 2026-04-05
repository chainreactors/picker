---
title: 芯片信息安全—安全启动
url: https://mp.weixin.qq.com/s/1coM9j0f-oxEkLhFtnnBFA
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:32:33.349639
---

# 芯片信息安全—安全启动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaC3QXxicXhdvnsGricRtYPMgicQDgwRpJKkRy59ia5bRHDhqLWdiat64uhsicUr0tex8GkDSnK9bI5d2iaepDsCz4GkquRXXI3QrPRNzM/0?wx_fmt=jpeg)

# 芯片信息安全—安全启动

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

**01**

**为什么需要安全启动**

安全启动又叫secureboot，它是一种通过逐级验证启动镜像，实现固件可信加载的技术。 如以下为嵌入式系统的基本启动流程：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibefoia57A62g0NWl9yuQglGfjyFHez3gKgu9TCQpHusGv8eV7mXhFuWl7K7QR2SoKACXdfURDjTsQ/640?wx_fmt=png&from=appmsg)

该流程中由bootrom开始，逐级通过spl、uboot以启动linux操作系统。我们假设spl、uboot和linux镜像都被保存在flash上，则在启动时，各级启动程序都需要从flash中加载下一级启动镜像，其流程示意图如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twibefoia57A62g0NWl9yuQglGg2VlTGmtevGHmcaUqNoGricBQ7SEoyF0gmVicCvWdibYrRLOMVmVzQRYQ/640?wx_fmt=jpeg&from=appmsg)

如果以上流程未执行secureboot，则flash中的镜像一旦被恶意攻击者替换掉，那么最终系统上将会运行被攻击者篡改过的固件。假设linux和rootfs被替换掉以后，那么启动后整个系统都将掌握在攻击者的手里。从而导致在操作系统之上构建的所有安全机制都形同虚设。

综上所述，对于需要提供安全服务的平台，其基本要求是系统本身是可信的。因此，必须要保证从系统启动时运行的第一条指令，到操作系统加载完成的整个流程中，其所有代码都经过完整性和真实性验证。而secureboot就是被设计为完成这一目标的。

**02**

**安全启动实现**

**２.1　安全启动的信任链**

由于操作系统启动时可能需要多级启动镜像，而只要其中任意一级镜像未执行secureboot流程，则其后的所有镜像实际上都是不可信的。典型的例子如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twibefoia57A62g0NWl9yuQglGhF9ibRZsbZuRNFICE6wl1PFZbuszLfKczpSg1fNDnCfibRWqMKEXxYXg/640?wx_fmt=jpeg&from=appmsg)

以上例子中bootrom验证了spl镜像，若spl未验证uboot镜像，则一旦uboot镜像被替换以后，那么攻击者就可以控制后面所有的启动流程。如被替换的uboot可以从其它位置加载非法的linux镜像，而在该linux镜像中任意植入后门等。

因此，secureboot需要建立安全启动的信任链，在启动流程中，每一级镜像都由其前级镜像执行合法性验证。这样只要保证第一级镜像是合法的，那么第二级镜像的合法性由第一级镜像保证，第三级镜像的合法性由第二级镜像保证。从而像链条一样将整个启动流程的信任链连接起来，最终保证整个系统是可信的。

**２.2　安全启动的信任根**

由于信任链建立流程中，镜像合法性是由其前级镜像验证的，那么第一级镜像的合法性如何保证呢？这就是接下来要讨论的信任根问题。既然无法由前级镜像为其背书，那么按照惯例，软件没办法解决的问题自然就需要硬件上马了。

我们知道rom是一种只读存储器，它只能被编程一次且内容在其后不能被再次更改。因此若在SOC内部集成一片ROM，并在芯片生产时就将第一级启动镜像刷到这块ROM中，那么也就保证了它是可信的，这也是现代SOC的普遍做法。

由于SOC可能会支持不同的启动方式，如xip启动可以直接从外部的norflash开始启动。因此在rom中集成bootrom镜像之后，还需要保证芯片每次启动时都必须从bootrom开始执行，否则攻击者还可以通过xip方式绕过整个secureboot流程。而一般xip启动模式都是在调试阶段用于问题定位的，因此在产品调试完成，启动secureboot前必须要关闭该模式。通常它可以通过OTP或EFUSE中的特定bit实现。

**２.3　镜像验证**

secureboot的信任链是通过逐级镜像验证实现的，而合法的镜像应该要包含以下特征：

（1）镜像是由官方发布的，即其需要验证镜像发布者的身份

（2）镜像没有被其它任何人篡改过，即镜像的内容是完整的

以上特性的验证可以通过特定的密码算法实现。如可通过消息摘要算法验证数据的完整性，而通过非对称签名验签算法验证镜像发布者的身份。

**２.3.1　消息摘要算法介绍**

消息摘要算法是通过单向散列函数，将一段消息的内容转换为另一段固定长度消息的过程，而被其计算后生成的消息称为hash值，它具有以下特征：

（1）任意长度的输入消息都会输出固定长度的hash值

（2）hash函数必须具备单向性，而无法通过hash值反向算出其消息原文

（3）不同的输入消息其输出消息也不同，即其具有强抗碰撞性

（4）hash值的计算速度要快

以上特性使其可以被很好地用于验证消息的完整性，接下来我们对其做个简单的推演：

（1）若某一段消息被篡改以后，由于hash函数具有强抗碰撞性，因此其算出的hash值就会与被篡改前内容的hash值不同。从而能很容易地知道消息是否被篡改

（2）由于hash值的单向性，即不能通过hash值推算出原文。因此即使理论上存在具有hash值相同的不同原文，攻击者也无法通过该hash值推算出原文。这就使得攻击者无法通过hash值，伪造hash值相同而原文不同的消息。从而在密码学维度可以认为hash值与原文是一一对应的

（3）由于其输出的hash值长度固定，且占用的空间很小，如sha256占256 bit，而sha512占512 bit。因此为其它消息附加hash值在存储空间上是完全可接受的

有了消息摘要算法后，我们就可以通过它验证镜像的完整性，从而很容易地就能把被篡改的镜像给识别出来。

在密码学中有多种消息摘要算法，如md5、sha1、sha256、sha512、sha3等。随着计算机技术的发展，有些原先认为具有强碰撞性的算法（如md5、sha1），在当前已经被认为并不安全，因此secureboot中一般使用sha256、sha512等算法作为完整性算法。

**２.3.2　非对称算法介绍**

非对称密码算法是相对于对称性密码算法而言的，在对称密码算法中加密和解密时使用的密钥相同。而非对称算法加密和解密时使用的密钥不同，其中私钥由密钥属主保管，且不能泄露，而公钥可以分发给其它人。且通过公钥加密的数据只能由私钥解密，通过私钥签名的数据只能由公钥验签。

在secureboot流程中，会通过私钥对镜像的hash值签名，并将其附加到镜像文件中。这样，在系统启动时只需要通过其公钥验签镜像，即可确定镜像的来源。其原理如下：

（1）由于私钥只有密钥的属主能获得，其它人无法获取到私钥，从而无法伪造签名。

（2）公钥验签时，由于只能验签其对应私钥签名的数据，而其它伪造的数据都会验签失败。即只有该公钥对应私钥属主签名的镜像才能通过验签，从而确保了镜像发布者的身份。

**２.3.3　镜像签名和验签流程**

由以上分析可知镜像签名的基本流程如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twibefoia57A62g0NWl9yuQglG6vVEXamTXYWLlI7NqtIEwcJMmgicwQPMJdegRtRIoNB3jSMw9mLbbkQ/640?wx_fmt=jpeg&from=appmsg)

（1）使用hash算法生成镜像的hash值hash(image)

（2）通过镜像发布者的私钥，使用非对称算法对镜像的hash值执行签名流程，并生成其签名值sig(hash)

最后将镜像的hash值、签名值与镜像一起发布，在芯片启动时可通过以下流程验证镜像的合法性：

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twibefoia57A62g0NWl9yuQglGV8JicGlKBsrjnFbpEmChgH1ZPULwhpl45hf2N2eM3EGXuQGN10wBWXg/640?wx_fmt=jpeg&from=appmsg)

（1）使用非对称算法的公钥和签名值，对镜像的hash值进行验签。若验签通过则可进一步校验镜像完整性。否则，启动失败。

（2）若验签通过，则重新计算镜像的hash值hash(image)’，并将其与原始hash值hash(image)比较，若其相等则表明镜像的完整性验证通过。否则启动失败。

**２.4　公钥保护**

由于验签操作依赖于公钥，若设备上的公钥被攻击者替换成他们自己的，那么攻击者只需要用与其匹配的私钥伪造镜像签名即可，因此必须要保证设备上的公钥不能被替换。一般SOC芯片的片内会含有若干OTP或EFUSE空间，它们只能被编程一次，且在被编程后不能被再次修改。

故若将公钥保存到OTP或EFUSE中，则可很好地保证其不能被修改。由于OTP的空间一般很小，而像RSA之类的公钥长度却比较长，如RSA 2048的公钥长度为2048 bits。因此为了节约OTP资源，一般在OTP中只保存公钥的hash值（如sha256的hash值为256 bits），而将公钥本身附加到镜像中。

在使用公钥之前，只需要使用OTP中的公钥hash值验证镜像附带公钥的完整性，即可确定公钥是否合法。

来源：知乎@lgjjeff

https://zhuanlan.zhihu.com/p/536007837

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......