---
title: 会话密钥实现OTA的设备认证
url: https://mp.weixin.qq.com/s/I3KdeqkkbIpk282a5XLEWg
source: Doonsec's feed
date: 2026-01-07
fetch_date: 2026-01-08T03:28:08.780245
---

# 会话密钥实现OTA的设备认证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9ndicwjOX3DQcozfAlD8uedZEMGJnnsB8YHziaAjPzBDoIRJqNt3gf8J20SqdyECPEjBcX3oRfibicbA/0?wx_fmt=jpeg)

# 会话密钥实现OTA的设备认证

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDj35QtelfANiaT02jEgnILSunGiau3UuDTOv2qX6O4hhDic8KG4o42ibTJBQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563583&idx=2&sn=c73d1a26f0b229d865acaf1cade3c761&scene=21#wechat_redirect)

**01**

**会话密钥**

汽车电子会话密钥在汽车电子系统中起着至关重要的作用，主要在OTA升级过程中的作用：

**1、安全通信加密**

防止数据泄露：在汽车内部网络中，不同电子控制单元（ECU）之间需要进行大量的数据交互，或者ECU与外部加密芯片的通讯。会话密钥用于对这些数据进行加密，使传输的数据变成密文形式。即使数据在传输过程中被截取，没有正确的密钥也无法解密获取其中的内容，从而保护了车辆的敏感信息（如OTA升级的验签密钥）不被泄露。

**2、身份认证**

服务器或诊断仪设备接入认证：当汽车与外部设备（诊断仪）进行连接时，也需要使用会话密钥进行身份认证。例如，当ECU需要OTA升级时，汽车和诊断仪会使用预先共享的密钥或通过密钥协商机制生成会话密钥，然后利用该密钥进行身份验证和数据加密传输，确保只有授权的设备才能与汽车进行通信，保护用户和车辆的安全。

**02**

**会话密钥 - 算法**

**1、ECDHE算法**

ECDHE（Elliptic Curve Diffie - Hellman Ephemeral）即椭圆曲线临时 Diffie - Hellman 算法，它是基于椭圆曲线密码学的一种密钥交换协议，属于 Diffie - Hellman 密钥交换算法的变体，它利用椭圆曲线的数学特性，在不安全的通信信道上，使通信双方能够安全地协商出一个共享密钥，常见的椭圆曲线有 NIST P - 256、Curve25519 。

**2、KDF算法**

KDF 即密钥派生函数（Key Derivation Function），是密码学里的关键工具，其用途是从给定的初始密钥材料（如密码、主密钥等）派生出一个或多个密钥，主要用途如下。

2.1、密钥扩展

在某些场景下，输入的密钥材料可能长度不足或不适合直接使用，KDF 可将其扩展为满足需求的密钥长度。

2.2、密码存储

当需要存储用户密码时，不直接存储明文密码，而是使用 KDF 函数对密码进行处理后存储，提高安全性。

2.3、生成会话密钥

在通信双方建立安全通信时，可使用 KDF 从共享的密钥材料派生出会话密钥。

**2.4、KDF不同Option说明**

表1、表2和表3列举了辅助函数H的可能性，并提供了有关相关参数值的附加信息，例如H\_outputBits和max\_H\_inputBits。表格还指出了在SP 800-56A或SP 800-56B中指定的密钥建立方案的密钥派生函数中，H的每种选择所支持的安全强度范围参考NIST SP 800-56C 4.1章节。KDF常用Option 1方式，HASH选择SHA-256。Option方式分别如下：

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8LLQ4I1BKqhlHg9wTfUt0PUwSmntvFAthGkof5qO5EXSl90hRyGBv3fyq8Iiaic1YpuZyVorQTIdNg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8LLQ4I1BKqhlHg9wTfUt0PEnB01TkhbE1Nax7AKHiadf3GNT2jNAccyg61vOnT28yjicPrtZrOlBRg/640?wx_fmt=png&from=appmsg)

建议对所选盐的长度没有限制，除了要求其字节长度大于零，但不大于用于实现hmac哈希的哈希函数hash的单个输入块的长度。然而，这种选择的自由在某种程度上是虚幻的，因为HMAC算法会将输入的盐值（根据需要）转换为指定的依赖于哈希长度的字符串。一个较短的salt（被H用作HMAC密钥）将通过附加一个全零位字符串来填充，以获得指定长度的字符串（哈希函数的单个输入块的长度，hash）；一个较长的salt将被散列以产生一个较短的字符串（位长度为H\_outputBits），然后将其填充（通过添加一个全零位字符串）以获得指定长度的字符串（参见[FIPS 198]了解更多信息）。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8LLQ4I1BKqhlHg9wTfUt0PM9KFgnSOQPbNM7Zsy6urR5hicuHlqkjszpnVl7nFkblxRUAOHOftxWQ/640?wx_fmt=png&from=appmsg)

**03**

**会话密钥如何实现设备认证**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8LLQ4I1BKqhlHg9wTfUt0PibIVWomF50gWjOZBXrrJ1M91N6nLwpLrkOAbqXLkcp8DjLxAxKE29Sg/640?wx_fmt=png&from=appmsg)

**04**

**会话密钥的验证脚本实现**

#pip install cryptography 如何脚本执行错误，需要执行此命令安装一下

from cryptography.hazmat.primitives.asymmetric import ec

from cryptography.hazmat.primitives.kdf.hkdf import HKDF

from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

# 选择椭圆曲线，这里使用 SECP256R1

curve = ec.SECP256R1()

# 生成 Alice 的私钥和公钥

alice\_private\_key = ec.generate\_private\_key(curve)

alice\_public\_key = alice\_private\_key.public\_key()

# 生成 Bob 的私钥和公钥

bob\_private\_key = ec.generate\_private\_key(curve)

bob\_public\_key = bob\_private\_key.public\_key()

# Alice 从 Bob 那里获取公钥，计算共享密钥

alice\_shared\_secret = alice\_private\_key.exchange(ec.ECDH(), bob\_public\_key)

# 使用 HKDF 对共享密钥进行派生，增强安全性

alice\_derived\_key = HKDF(

    algorithm=hashes.SHA256(),

    length=32,

    salt=None,

    info=b'handshake data',

).derive(alice\_shared\_secret)

# Bob 从 Alice 那里获取公钥，计算共享密钥

bob\_shared\_secret = bob\_private\_key.exchange(ec.ECDH(), alice\_public\_key)

# 使用 HKDF 对共享密钥进行派生，增强安全性

bob\_derived\_key = HKDF(

    algorithm=hashes.SHA256(),

    length=32,

    salt=None,

    info=b'handshake data',

).derive(bob\_shared\_secret)

# 验证双方计算出的派生密钥是否相同

assert alice\_derived\_key == bob\_derived\_key

print("双方计算出的派生密钥相同，密钥交换成功！")

print(f"派生密钥: {alice\_derived\_key.hex()}")

来源：

https://blog.csdn.net/xiaoxinxinxinxin/article/details/147284426

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

特斯拉、合众新能源-哪吒、理想、极氪、小米、宾理汽车、极越、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

*...