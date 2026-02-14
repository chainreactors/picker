---
title: AES128加密算法
url: https://mp.weixin.qq.com/s/3l7goN4zjGwVnJW9f_c1uw
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:05:37.365832
---

# AES128加密算法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaDvo8TTibYYaEZNrfR049Izt5Xr0NFia8NWa3RbuQfLMySOmZicZsE2dS7TpUJgiaoK4g0LyvUSgoc6zVkX8B8C0uCU4BibmcITBeC0/0?wx_fmt=jpeg)

# AES128加密算法

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247566311&idx=2&sn=27d2cf53ef824bfde9b824f90e864ec6&scene=21#wechat_redirect)

**01**

**前言**

AES（Advanced Encryption Standard）是对称加密算法的一个标准，主要用于保护电子数据的安全。AES 支持128、192、和256位密钥长度，其中AES-128是最常用的一种，它使用128位（16字节）的密钥进行加密和解密操作。AES属于分组密码，每次操作128位（16字节）的数据块。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibu3OZbZwDh8ctJU57b1j3R7ysBaKNlfkFYEVr1chrzicibADxryAPzbNKsKEHsnYqVCwZNqIqGniabA/640?wx_fmt=png&from=appmsg)

**02**

**AES128加密流程**

AES的加密过程包括以下几步：

1、密钥扩展（Key Expansion）：密钥会通过一个密钥扩展算法生成一系列称为“轮密钥”（Round Keys）的密钥。AES-128需要10轮，每轮用到一个轮密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibu3OZbZwDh8ctJU57b1j3RXp5pgicgicx0pqrJ6Jtfm1Uz6Hka3C4jO54V0xVY8c75xDm3uRBibKjZg/640?wx_fmt=png&from=appmsg)

这里的K矩阵就是原始密钥，把每一列用4维向量w来表示，就拆分成了w0,w1,w2,w3，将w3进行g中的运算，先是把4个字节左环移，然后对这4个字节进行S盒变换（字节代替），变换完后，最左面的字节与RCj相加，AES128加密要把以上步骤进行10轮，RCj在每一轮的计算中都不一样，具体如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibu3OZbZwDh8ctJU57b1j3RE0V5IlRUmVb8PDwEHEfbTSQrkqhvJjxS0QUosq8XZe0kjXR3maLErg/640?wx_fmt=png&from=appmsg)

2、初始轮（Initial Round）：在加密的初始步骤中，将数据块与初始密钥通过按位异或（XOR）进行操作。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibu3OZbZwDh8ctJU57b1j3RvWTu1mG5NVpKIgUm3kFWVU8Yhs0icvboTsAnExMTsodA5ygrlRHjddQ/640?wx_fmt=png&from=appmsg)

3、主要轮（Main Rounds，9轮）：每一轮包括四个操作：

* 字节代换（SubBytes）：将每个字节使用一个固定的查找表（S盒，Substitution Box）进行替换。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibu3OZbZwDh8ctJU57b1j3Rmvun5DggU2mEzGFWlalIHTEFYXyDgmgB4OxXeXptROZiajVicYnSFNVw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibu3OZbZwDh8ctJU57b1j3RVSDBibZWeEicNa0vC2eb0uoMkMc2DfEzcabmvP1ibQDLaweB8ez4wNOuQ/640?wx_fmt=png&from=appmsg)

* 行移位（ShiftRows）：行内移位操作，按特定规则将数据块的每一行向左循环移位。

MD遭受了一起严重的黑客入侵事件，黑客Intelbroker 大规模泄漏了AMD的数据。AMD当即发起了调查，在一份声明中表示：“我们正在与执法官员和第三方托管合作伙伴密切合作，调查该指控和数据的意义。”

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibu3OZbZwDh8ctJU57b1j3RW85GCVOcqXXMNexTpSN9Q3vJic1jEZwf6lLCiavfBusQUsABbZCY6TZQ/640?wx_fmt=png&from=appmsg)

* 列混合（MixColumns）：列内进行线性变换，使用矩阵乘法混合列的数据。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibu3OZbZwDh8ctJU57b1j3RdibSIwFyyF6aaaH7J7eUWXdUXACwqfDJxtBc7wM3USfNYZbo1ZK1e6A/640?wx_fmt=png&from=appmsg)

其中矩阵c为

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibu3OZbZwDh8ctJU57b1j3RlfuQPovdmWbzUV8YKiaJ1ErKLgKdDh2NuIgnaRKOCLqwPAv9hTuvAEg/640?wx_fmt=png&from=appmsg)

* 轮密钥加（AddRoundKey）：将当前的数据块与当前轮密钥进行按位异或操作。
* 最终轮（Final Round，第10轮）：与前9轮的步骤类似，但不包括“列混合”步骤。

**03**

**AES128解密流程**

解密过程是加密过程的逆过程，包括：

1. 密钥扩展
2. 初始轮密钥加
3. 主要轮的逆操作（Inverse ShiftRows、Inverse SubBytes、Inverse MixColumns）
4. 最终轮的逆操作（不包括逆列混合）

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibu3OZbZwDh8ctJU57b1j3R9oiaUKBb18KbyKhR34VnVOkia0JbMeI0ycdB6jAVu7v08tciaicCF3vyUA/640?wx_fmt=png&from=appmsg)

**04**

**加密模式**

上述所说是16字节数据加密和解密，对于数据大于16字节时，我们可以区分不同模式进行解决。

**ECB模式的基本原理**

1、分块加密：在ECB模式下，明文数据被分成固定大小的块（对于AES，块大小为128位，即16字节）。如果最后一个块不足16字节，则需要使用填充（如PKCS#7填充）来填充至16字节。

2、独立加密：每个明文块使用相同的密钥独立加密，生成相应的密文块。即使明文中的某个块被多次使用，得到的密文也将是相同的。

3、加密流程：

* 将明文分成多个128位的块。
* 对每个块使用AES-128加密算法进行加密，生成密文块。
* 将所有密文块连接在一起，形成最终的密文。

**ECB模式的优缺点**

**优点**

* 简单性：ECB模式实现简单，容易理解和使用。
* 并行处理：由于每个块独立加密，可以并行处理多个块，提高加密效率。

**缺点**

模式缺陷：

* 相同明文块生成相同密文块：如果明文中有相同的块，则其加密后的密文也会相同，导致模式泄露信息。
* 模式不安全：由于没有引入任何随机性，攻击者可以通过观察密文的模式来推测明文内容。例如，在图像加密中，相同的图像块将产生相同的加密输出，容易被识别。

**python实现**

**1.直接调用库**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twibu3OZbZwDh8ctJU57b1j3RxPYFpjnW8ibPjZerIpyVcwfW8R9lg0UfGIkxX8VLb76Wygib7c27uORw/640?wx_fmt=png&from=appmsg)

来源：CSDN@小夭。

原文链接：

https://blog.csdn.net/m0\_47146037/article/details/142376754

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicHdaQsibvoH8dLYIIcT5YQibwbnuZn1MLCOMydw2SMKWbibsLpooeE2jgCt8FABvsVmlJZO5PO00Ryw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561756&idx=2&sn=f9b8c214978537f47cccba736cdb5bfd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

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

**全球领先一...