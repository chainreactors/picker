---
title: 汽车网络安全之 AUTOSAR - SHE 密钥更新
url: https://mp.weixin.qq.com/s/1NnryxkMgU9X5xMZI4-BNg
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:01:41.578503
---

# 汽车网络安全之 AUTOSAR - SHE 密钥更新

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAslZXFciaBZXeqibia9OmAEYqWXChVYHnlyHO4ZKXZVGJick3BJBqxGPxjKSuRyZMCjmTzzWO8GplS7hOWAkia7xvkCCTdj74ib7ibys/0?wx_fmt=jpeg)

# 汽车网络安全之 AUTOSAR - SHE 密钥更新

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

**01**

**什么是 SHE**

SHE （Secure Hardware Extensions），安全硬件扩展，其主要目的是将对软件的攻击转移到对硬件的攻击上来，增加了黑客对系统攻击的复杂程度。

主要实现方式，是将SHE与主核分离开，SHE有自己独立的存储空间，主核可以对SHE下发加密、解密、存储的动作指令，但所有的密钥，私密信息对主核均不可见。从而避免了黑客从软件层面进行调试或注入恶意代码从而获取密钥等私密信息的可能性，想要得到密钥，必须得从硬件存储状态的角度进行破解，但想要从硬件得角度获取到密钥的信息这将是非常困难的，从而大大的提升了系统的安全性。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCqCwXDz3XgibQQ6o9eibRFhrIrzapuNBsibpNicboTL8G0r4ZrGlVef9mnGRUE9U1gjN0eJ2VvRay07puibiaGQaOVz8XWWsxe9ygJs/640?wx_fmt=jpeg&from=appmsg)

**02**

**SHE 内存槽更新流程**

本文主要对SHE规范中密钥更新流程的讨论，其他部分以后有机会再做补充。

更新一个内存槽（密钥，证书存储在内存槽中）时，外部实体必须知道知道合法的真实的另一个密钥，Table4.5描述了，需要的更新密钥和需要知道的密钥之间的对应关系。该流程图中KEYAuthID是需要上位机知道的密钥，KID是需要被更新的密钥。

例如：更新下表中对应KEY\_<n>的位置的密钥时，因此外部实体应该知道现存的MASTER\_ECU\_KEY，以及需要更新的KEY\_<n>的密钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaBHyyotCoaqicHb9xk2qG3qKsJ2q6UO7nAooCRic65ib0S7QKSiaxLO9yQPH1PFc85y6iaWrLue55PyZia1Zt3q0YK8mjXic3VZ1QYUZw/640?wx_fmt=jpeg&from=appmsg)

每一个不同的slot类型所包含的信息不同，具体参考Table 4.3。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaAjT5JV8dJibQOeTYPAFTKue0GCH0lib4ybeicVnvM3rgXFHfHdxWWtliciahLQn4xUUreaqRoBia6U796aTvicmvtoecqxibW9BzoQI5U/640?wx_fmt=jpeg&from=appmsg)

**SHE 内存槽更新流程如下图**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBqsiaZMM0lfY9ysr6WnzlNtnjqTGpGKEgPkGbiaBvljBkKmLg5YCQwtXRs4WHTqicUMmYHdH4mJPeiaEj4Ceib5j87ALNDVtaQP5uI/640?wx_fmt=jpeg&from=appmsg)

**（1）K1 = KDF(KAuthID, KEY\_UPDATE\_ENC\_C)**

如下截图中4.3.3.1所示KDF(KAuthID, KEY\_UPDATE\_ENC\_C) = AES-MP ( KAuthID | KEY\_UPDATE\_ENC\_C)。

- KAuthID是在更新KID时需要知道的Key；

- KEY\_UPDATE\_ENC\_C是基于4.3.3.1中的方式构成的，具体的值已经在该规范4.12中给出，为：0x01015348 45008000 00000000 000000B0。

此时在基于4.3.3的压缩函数得到K1。压缩函数解释如下：

长度为L个bit的message的压缩，（L + 1 + k）mod 128 与 88 mod 128 同余，求k的非负最小值，参考示例4.13.2.4，message的长度L为256，那k算出来为87，即87个数值为0的二进制值，前面加上一个数值为1的二进制数值，在加上40个bit来表示message十进制的值，即二进制表示256为0000000100。

Xi作为明文，OUTi-1作为密钥进行AES-128 ECB模式下的循环加密运算。（ECB模式是没有初始向量的，OUTi-1是作为密钥参与计算，OUT0被称之为初始向量），

每一次计算的结果会和本次的OUTi-1和Xi进行异或运算，最后的OUT的值最为压缩的结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaDSicE5LliaWGroUMS93xsMfzmrMdwALFSDtgWsTPCmhic54IbibNmFF7tOqQqfialkMcUU005ojKGTtFwM7GvtuAoNwJKEqrR0Ttxc/640?wx_fmt=jpeg&from=appmsg)

**（2）M1 = UID'| ID | AuthID**

M1是UID, ID和AuthID合并后的值，其中UID全称Device/ECU Unique Identifier，每个ECU都是唯一的。

通常UID又由三部分组成，即Serial Number, ECU HW Part Number, Security Peripheral ID串联组成。

**（3）M2 = ENCCBC,K1,IV=0(CID'|FID'|''0...0''95|KID')**

该公式含义为：以K1为密钥，初始向量为0，用AES CBC模式对数据CID'|FID'|''0...0''95|KID'进行加密，其结果赋值给M2，这里的 ' 我认为是新的参数的意思。

CID：用于防止重放攻击的counter，上文已做解释；

FID：用于使能与不使能所对应ID的key的更新，上文已做解释；

''0...0''95：95个bit长度的0；

KID：是我们需要更新的目标key。

**（4）M3 = CMACK2(M1|M2)**

该公式的含义是以K2为密钥，以AES算法的CBC模式，计算出M1和M2串联后的消息消息认证码。

**（5）CMD\_LOAD\_KEY**

CMD\_LOAD\_KEY是SHE接口函数。用于在更新时传递M1，M2，M3。在读取时传出M4，M5的值。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBrSVpA8Y3eWVdpc6ApNdvd1MWesglJ7jduYIkTl1ZkJiauSxam0NibuIPicclMib7LQVwWIfaOY4ubQq5I6VEIKrqAbzrOa4YibJ7k/640?wx_fmt=jpeg&from=appmsg)

**（6）Check write protection of KEYID**

这里检查的是ECU内部的目标Key的写保护的Flog是否使能，如果使能返回：ERC\_WRITE\_ERROR，停止更新。

写保护的Flog未使能，将M1,M2,AuthID传递到SHE的storage。

**（7）Read (AuthID)**

从第（6）步存储的位置读取AuthID所对应的KEYAuthID，并将其与M1，M2一并给到KDF压缩算法作为输入。

**(8)KDF(KEYAuthID,KEY\_UPDATE\_MAC\_C)**

基于从ECU内部读取的密钥KEYAuthID，以及从外部传递的M1,M2，再以KDF压缩算法算出的结果作为内部的K2。

具体KDF的实现参考（1）。

**（9）CMACK2(M1|M2)**

拿到K2后，以M1|M2作为明文，得到内部的M3\*。

**（10）Check(M3=M3\*)**

对比外部传过来的CMAC值M3和内部计算的M3\*，其目的是为了判断M1（涵盖了UID等信息）和M2（涵盖了需要被更新的密钥）在传输的过程中有没有被篡改过。

如果不相等，停止更新，并返回ERC\_KEY\_UPDATE\_ERROR。

**（11）Check(UID'=0)**

检查输入的UID'是否为0（直接从输入的M1中提取）。

如果不为0，从storage相应的ID中读取UID。并进行对比，若不相等，返回ERC\_KEY\_UPDATE\_ERROR；若相等读取AuthID所对应的KeyAuthID。

如果为0，需要对目标ID所对应的WILDCARD的标志位是否有使能。如果使能，说明通配符不被允许；如果没有使能，读取AuthID所对应的KeyAuthID。

**（12）KDF(KEYAuthID,KEY\_UPDATE\_ENC\_C)**

以KDF算法将KEYAuthID,KEY\_UPDATE\_ENC\_C进行压缩，得到K1（这里的算出来的K1应该与外部用的K1是一致的，因为在KEYAuthID外部也是已知的，且与内部相同）。

**（13）DECCBC,K1,IV=0(M2)**

以AES CBC的模式，算出的K1为密钥，初始向量为0，对外部给到的M2进行解密，得到外部给到的CID',FID',KID'，对比外部CID'与本地CID的大小，如果外部的常数没有大于本地的常数，说明该消息是重放的，应返回ERC\_KEY\_UPDATE\_ERROR，如果是大于本地的常数，则将最新的常数、密钥、和标志位存储进相应的位置。

**03**

**SHE内存槽更新后验证消息生成的流程**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaCnB7zbl6zVDgrnibG6bLiaqN8iar1d7VKOZOacbqRgJzUtmWduiaeLtNnSQiaSu2MHDHONgSOiciaAsbsD1ibegdiajd8rmjqPiaPrkFiafU/640?wx_fmt=jpeg&from=appmsg)

**（1）KDF(KEYID,KEY\_UPDATE\_ENC\_C)**

基于更新后的Slot位置的密钥和KEY\_UPDATE\_ENC\_C常数，以KDF算法进行压缩，得到临时的密钥K3。

**（2）ENCECB,K3(CID)**

以K3为密钥，基于ASE-128的ECB模式对从更新后的Slot位置密钥的counter参数进行加密，得到参数M4\*。此时M4\*相当于更新后的Slot位置的密钥的摘要，涵盖了其信息。

**（3）M4 = (UID | ID | AuthID | M4\*)**

将UID、Slot的ID、已知密钥的ID、和参数M4\*串联得到M4。然后将M4的数据放入响应报文里传递给上位机，此时M4相当于涵盖了UID、被更新的密钥的ID、已知密钥的ID、被更新的密钥的摘要信息，这些信息将在上位机中解析出来，并进行验证被刷写的Key的各项信息是否正确。

**（4）KDF(KEYID,KEY\_UPDATE\_MAC\_C)**

基于更新后的Slot位置的密钥和KEY\_UPDATE\_MAC\_C常数，以KDF算法进行压缩，得到临时的密钥K4。

**（5）CMACK4(M4)**

以K3为密钥，基于ASE-128的CBC模式对进行处理，生成消息认证码M5，同样将M5的数据放入响应报文里传递给上位机。因为CMAC的目的是为了保证数据的完整性，因此这里就是为了保证M4在整个传递过程中没有被第三方篡改过。

来源：鑫鑫攻城狮

https://zhuanlan.zhihu.com/p/683934717

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAgXyLqfnkPJhyibCoBSOMGSsdQ03SEf01kcUbPAEzhf5nb6vyvYWINevstJCARUgy8qNpTa2lKVo7g7RPFm8IicY9aYtviaowaTE/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD9qjQXZdMwY876TkFlhIUib1kn4wc72e4cib9eharylSOXtAgAq234jTmZYKrXsGd0OALDotYN7MYS8h0mElMEuPddlDZic56KCg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572912&idx=3&sn=58184d21d6dabc713e8d93a0c1d80e40&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jp...