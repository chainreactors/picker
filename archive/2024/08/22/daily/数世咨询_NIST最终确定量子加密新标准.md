---
title: NIST最终确定量子加密新标准
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514821&idx=1&sn=c160ff9b388afa84df8328a95bb6efdf&chksm=c144c878f633416e68e4bdeb0bfb8cafb8e7d56ac88f0f6d27d722f9ecd02a76ab47ae29ec9f&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-08-22
fetch_date: 2025-10-06T18:04:03.368207
---

# NIST最终确定量子加密新标准

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqrwzMia41nGdnJUr2micRhaRMTzLa9ibg9z1JVNeUKO0mq2iaFPC1c7FOaRanQlPgniaheV5lUJ1SEfVjQ/0?wx_fmt=jpeg)

# NIST最终确定量子加密新标准

陈发明

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqrwzMia41nGdnJUr2micRhaRMV7KgbBWZleEIPiaAxYDONwblvY67H3sbUEvx4jjYh1nFiaaibUfRONkmg/640?wx_fmt=jpeg&from=appmsg)

在经历多年审查后，美国国家标准与技术研究所（National Institute of Standards and Technology，NIST）**选择了全球首批三种后量子加密算法作为其后量子安全策略的基础：ML-KEM、ML-DSA 和 SLH-DSA。**

NIST于2016年首次提出要求，敦促密码学家推动新标准的制定。当时量子计算机的威胁开始成为现实，它们有望破解当今使用的常见加密算法，例如RSA。

截止至2022年，共有69种此类算法提交给了NIST评估，其中4种被选中进行进一步审查。这4种候选标准中，第四个算法“Falcon”未能入围初始标准，但对其评估将继续进行。

NIST还在继续识别和评估其他算法。该机构近日宣布，预计在不久的将来将宣布大约15种算法，这些算法将进行下一轮的测试、评估和分析。

但企业应**立****即开始转换到后量子加密，而不是等待**，这是NIST数学家达斯汀•穆迪的观点，他负责后量子密码学（PQC）标准化项目。**新算法将只是NIST宣布的三种算法的备份。**

穆迪在近日的公告中表示：“**无需等待未来的标准。请立即开始使用这三种标准。**我们需做好准备，以防攻击破坏这些标准的算法。同时我们将继续制定备用计划来确保数据安全。但对于大多数应用来说，这些新标准才是重中之重。”

**01**

**基于格的密码学**

**这三个新算法都是为非对称加密设计的——也就是说，用于编码信息的密钥与用于解码信息的密钥是不同的。**你保留解码密钥作为秘密，只给自己知道，并将编码密钥公之于众。现在任何人都可以给你发送一个只有你才能阅读的秘密信息。

这被称为公钥加密，基本上是所有在线通信、网站安全、金融交易以及密钥管理系统和其他专用应用程序的基础。

**系统的核心理念是，将两个大数相乘相对容易，而将一个大数分解成其因子则极为困难。**

新型的基于格密码方法依赖于一种不同的数学机制，这种方法不仅对传统计算机构成挑战，同样也难以被量子计算机破解。

它基于一种叫做“背包问题”的东西，IBM的密码学研究员格雷戈尔•塞勒说。您有一个非常大的数字的集合，然后你从这些数字中抽出一些并将它们相加，总数是另一个很大的数字。将数字相加非常容易，但是弄清楚哪些数字是用来加起来的，这非常困难。

“当集合真的很大并且整数真的很长时，这是一个非常困难的问题，”赛勒说。

**基于格的密码学采用了这一理念，并增加了难度。**背包里不再是装满数字，而是装满了向量。如果你将一个数字想象成线上的一个点，那么向量就是指向空间中某个点的箭头。并且，你不仅可以将一组向量相加，还可以将这些向量的倍数相加。

**02**

**ML-KEM算法**

这个算法，**最初被称为CRYSTALS-Kyber，是****一种基于模格的密钥封装标准。**它最初是由IBM研究人员与其他机构合作开发的。它是一个**设计用来进行通用加密的标准**，例如    保障网站安全访问等，其快速便捷的特性使之成为理想选择。

**03**

**ML-DSA算法**

该算法**最初被称为 CRYSTALS-Dilithium**，最初也是由 IBM 开发的。**该标准是三种算法中第二快的，它被设计用于数字签名。**

根据赛勒的说法，这一算法的关键在于，要解密信息，必须知晓参与计算的所有向量乘数。

赛勒说，“数字签名主要用于验证文档或软件的真实性，有助于确保它们不会被修改或篡改。“这些签名在医疗、金融和制造业等敏感行业中尤为重要，同时也被政府机构广泛使用。因此，迫切需要转向量子安全的数字签名方法。

**04**

**SLH-DSA算法**

这是**另一种数字签名标准，但它比其他两个更为安全。**然而，这种安全性是有代价的：根据实现的是哪一种变体，它要么生成更大的签名，要么需要更多时间来创建签名。

NIST表示，**该算法旨在作为备份，以防ML-DSA被证明容易受到攻击。**

**05**

**不仅仅是算法**

除了数学加密算法外，NIST还公布了相关的实现细节。

穆迪补充道：“这些标准已经确定了，它们涉及如何将这些元素整合进产品与加密系统之中。我们建议系统管理员尽快着手进行整合工作，因为彻底完成这一过程需要一定的时间。”

**采用量子安全加密技术的转变将比以往的密码学演变更为复杂，原因在于量子安全的算法与经典加密技术截然不同。**此外，不同的应用场景需要采用多种差异化的算法。加之软件供应链的错综复杂性已达到前所未有的程度，使得这一转变更加复杂。

解决方案是要对使用的具体标准保持灵活性，汤姆•帕特森说，他是埃森哲新兴技术安全负责人。这将允许企业与可能使用不同加密标准或仍依赖于传统加密的供应商和合作伙伴进行整合。这也将允许企业在未来切换到新的、更好的或更高效的标准。

帕特森表示，**这三种标准不会是我们看到的最后的量子安全加密标准。**“在未来几年，将会有一系列不同的算法可用并被标准化，”他说。

“这对世界各地的大多数首席信息安全官来说是一个开端的信号，”帕特森说。“现在他们知道他们将要使用哪些算法了。”

 \* 本文为**陈发明**编译，原文地址：https://www.networkworld.com/article/3486075/nist-finally-settles-on-quantum-safe-crypto-standards.html
图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#数字安全交流群来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

😄 嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&token=340500352&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrwzMia41nGdnJUr2micRhaRMIic7jMR5rCvIhBPibsReicD4c6lYuicvtWvUIJTsStxhKpRibGntwqaB9lw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514804&idx=1&sn=f081a9b1cb182a220b80e7ec4cd7cb8f&chksm=c144c809f633411ff075fd7ad6bf81a705d374862da52e9815c0ed284cc0bedabf7a8aa83ab7&token=400988400&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqrwzMia41nGdnJUr2micRhaRMicXibnOFxpL6GUDuX8cicCpkiaBLWLgvBcibA6wOoiaxyNBQdZy7QgunkYzw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514264&idx=1&sn=34960d59e3146dcce9f986129c3593c2&chksm=c144ca25f633433381c6bb3bc13fe3e8f2c15984de2aa8f072497dc07648f85c713aa1347ba1&token=340500352&lang=zh_CN&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过