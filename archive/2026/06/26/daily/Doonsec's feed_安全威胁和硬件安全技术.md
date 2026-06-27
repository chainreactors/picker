---
title: 安全威胁和硬件安全技术
url: https://mp.weixin.qq.com/s/1Ws9HVHTR-7YhZ75D3IjBQ
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:48:04.986034
---

# 安全威胁和硬件安全技术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaC2So2bwJxUrsX6sp2a3XnErDF71QvfWkVFyxiaIOKoNa4VZGpnxSwVyicTMFC5Ha96td5592sax5T78YTHGZviazCpqOhKwTzjSY/0?wx_fmt=jpeg)

# 安全威胁和硬件安全技术

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

**01**

**硬件安全技术是什么？**

一、传统视角：

硬件安全=密码芯片安全，特别是智能卡、可信计算、Ukey等芯片攻击防御技术

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD6qZD5Yx95uB1RaOWcx8QvMpvwS6ib5eyxLCORV6my8kx5SxgvSNz7ib1ZndvKg4ndicyw56psTPbM9pjydLQmxLib40AnRVB0fko/640?wx_fmt=png&from=appmsg)

密码芯片的逻辑接口、物理接口安全；

核心功能：具备防攻击能力，能有效保护秘钥存储、进行安全密码运算；

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCEsU4rKPoKz97thMNj2VEuYkK86S5nWKXFOUaVBuUnQDhgGedu8KicntEI3Ifia4R2Pl7UVzuFN791QVCAqBMY3hmic0a8cNYZjs/640?wx_fmt=png&from=appmsg)

密码芯片是一个边界清楚，作为一个黑盒子，放在系统中，起到安全密码运算、防攻击等功能。

**02**

**智联时代**

1、万物互联+智能化：

云、端协作、数字孪生、海量数据，如智能家居、智慧城市、电力网络等迈向智能时代。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBweKy3wlLojibkTSgXQBMQibJKicfTXSZIyATiarx2I5miaSldnibgmnmepnXAQWjjfThNHSI6pibfqCurY7lCiaHTngr0BCXSmicicV91Q/640?wx_fmt=png&from=appmsg)

2、网络攻击进入物理世界:

攻击截面扩大，风险巨大，如黑客操控物理世界产品，威胁从“谋财”升级为“害命”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBexptnoO3M0TxP5Mia5KOBibjmAcYySkmFibWybjykXXnNdPgNFmkxoNkrTysJYDbL26j621iag9SRkvNdrTSkyOcEvnPkiaIAE0BQ/640?wx_fmt=png&from=appmsg)

因此，需要相关的技术来解决安全问题。

**03**

**真实世界安全问题层出不穷**

1. 监控摄像头的攻击
2. 智能音箱攻击
3. 服务器攻击
4. 个人电脑攻击
5. 电力、网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDogNHlKbsk293k8P9okicfIMjsoBZxBFQuMkZxAib0OZevqmCxicLAQbfxzmFK8b8mwz6V1P4UTwZKas9ykkvOp7QAhw0ibyREGL8/640?wx_fmt=png&from=appmsg)

如何减少这类事件的发生，因此，硬件安全技术可以有效的解决这类事件发生的概率。

**04**

**硬件安全：新视角**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDx5wTcnokoUfgyeqgvCHos4E8MdBHw0TAGOCy6NSIINYPuhSE0yRcPfqr0ouanGib7lkeiadn2AOR6dhxQRzK0T9FOMgP0h5C9Q/640?wx_fmt=png&from=appmsg)

解决安全问题，可以分为四个部分来进行问题解决：

应用软件，操作系统，底层软件，硬件层（如硬件电路）

系统和固件是密不可分；

系统信任跟由硬件+底层软件共同保护；

如果底层有漏洞，那么系统肯定会被破解；

因此，硬件安全研究不仅仅局限传统的独立密码芯片研究范畴，现在考虑的是在更复杂的、开放的系统中，硬件安全能够做什么？

传统的硬件安全保护秘钥，未来的硬件安全除了要保护秘钥，还要保护软件，再由软件再保护上层应用。

硬件安全用在什么地方，所有联网的设备，必须用到硬件安全技术

举一个简单的IoT例子：（物联网设备、智能手机、云）

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCbziatFToibrhiaXIkpO2ONheRbIZ6RyJWbjzs7KgiczIRJEf05wbkoib4fKao1S341L1QpiaKianqc38iaEtzTibh2yly0ibA20SKAlm7c/640?wx_fmt=png&from=appmsg)

1、设备端：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDeRczgr1pSSfbIxJIW29ib954LdQoiaxSlKeLB0TuCxV8FwZC6IXwmaLMQicy1sHV3CspiaicSEun46TWf9DEMOz2SR9pMngVDwbBI/640?wx_fmt=png&from=appmsg)

2、手机端：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAEZYOzUIj3V6DpUZvgzFVZXzGW88U9VNw5RV0iaszFZXicIa2TQb470uyBQkuvxF8ia9JzyA3kQ4gjibG7n8UicY5MB6riaPBnVBq3o/640?wx_fmt=png&from=appmsg)

3、云端：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBhSEVCsfxD4VLnkjYXc8wLz9aIE9kTYTHu8JCIPHL90G6LkV9PjRoACF9CzVNttOr13yyehftOXzXJDFkuK2gicWrJbD7lKaY8/640?wx_fmt=png&from=appmsg)

硬件安全扮演的角色：

虽然云和端所用的芯片架构不一样，如算力、软件等。但是却有相同的硬件安全要求。

例如：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCMiaoGkh2wwydLSsbqHicIrL3x6BJ3VmVB9PYDawAK7UCMoPodVVibt4tGrXVkM95I5Dj1k2RgiaUSfJzicvVXBYMOjhnRYlqt8wUg/640?wx_fmt=png&from=appmsg)

对于手机端，可能还有安全执行环境，需要run应用，如指纹、人脸。

对于云端，考虑运行在虚拟机上的多个用户安全需求，如每个用户可能有自己秘钥存储需求；OS的安全启动、数据安全需求；TLS的卸载等

**05**

**生命周期安全设计**

生命周期安全设计是硬件安全需要考虑的重点内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAfRe8ichrRicwZQfia5k5C2XZFECIVOqNtLmnlxOUiaIl5QSWOM0ZfwCGibjq3TNib3YiaFMziaQ0rggicwbX8knZHGBn2eR2RfxcpJdyg/640?wx_fmt=png&from=appmsg)

实际在芯片的最初的RTL设计，到交付至用户的，存在很多环节。很多环节有可能导致秘钥、固件或者其他敏感信息的泄露，那么硬件安全如何在开放的供应链上构建信任根和信任链？这一点是硬件安全需要解决的问题。

**06**

**硬件安全技术**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAlXBOEIWjqpLCrXRFy7AZoGiakibEccM5Q9DQ1fCEhxyH1KCMb1Z0wWw5mNTbpZyMkS4JhIHynfCvoX8y2ibdMdLV5MSQmWHRQI4/640?wx_fmt=png&from=appmsg)

硬件安全上主要研究内容可分为以下四个部分：

1. 硬件安全架构
2. 物理攻击技术
3. 抗攻击设计
4. 面向软件安全的硬件设计

**07**

**侧信道攻击**

1、侧信道攻击

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAF5QU8hp3hKzJOiau0zIia93d0QZgljk0VVN2vicvrtsYZDXHM7gsjRgxXlNYqQCMRfTlQb2ILThBKzicT1CTADpKZRozY1sEBDZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBG1Pnr0oznbLo16NZdpeeRpJic0CWsxaibYiag1xGAQlcKrjEAhVAbxnaE4Ba1DslZlEeyt0vJXQGJic4TaUDG2TFITDRynFfBrq4/640?wx_fmt=png&from=appmsg)

SCA本质上利用芯片在计算时，边信道的泄露，内部的电路的状态取决于算法的设计，例如对于8bit的寄存器，若初始值为0，一旦我们往里面写入一个字节的数据，那么在写入的过程中，部分寄存器的状态会翻转，即会引起功耗的变化（电容）。实际上，这种泄露是很危险的，并且在电路中一直存在的。

侧信道的攻击对象发展有经历了如下过程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD5ed9QiaBTRxMaNjSNkR8EicqYKR8PkYyxoDAe0epR5gQHFy1oy1HicFKAy7uEnwmbuzFfBPHcQZNUpnrJhC11D4nWOP7ahEGIwA/640?wx_fmt=png&from=appmsg)

一直存在的误解是，人们经常认为侧信道攻击只是对工艺落后的芯片才能进行攻击，却认为对面积大、工艺先进的芯片没有威胁，实际上这个观点是错误的，只要芯片在做密码相关的计算，就可能存在侧信道信息的泄露。

2、侧信道攻击的分类

除了从瞬时功耗的角度发现了可以攻击密码芯片外，此外还有电磁辐射，光子泄露，计算时间等侧信道的信息。

侧信道攻击不需要破坏芯片或者修改软件，就可以攻击，因此其攻击门槛低，威胁较大。

因此，抵抗侧信道攻击是安全芯片的主要的技术难点之一。

**08**

**微架构侧信道（MASCA）**

侧信道的其中一个分支为微架构侧信道，最近几年比较热门的侧信道。

微架构侧信道分析：利用处理器架构的特点，获取与敏感信息（如秘钥）相关的信息泄露（如时间），来破解系统安全防护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDkDhVqdPY9GjSQPqDpKDdYfgwfTpqLSFVUNRq5XmoRoGE2MysLg4ns1HcFLPaiawqAdTEZOBIRvUw5jqooovj1DEqEauIENsE8/640?wx_fmt=png&from=appmsg)

如2017年，熔断和幽灵：滥用CPU推演执行功能，来构造攻击场景，对大量intel CPU均有效；
2018年，Foreshadow：滥用CPU推演执行破解了SGX;

2019年，NCC 高通 QSEE攻击：利用分支预测和cache的时序泄露，获得Trustzone之中的ECDSA私钥。

传统的攻击是需要黑客去靠近设备来达到攻击的目的，不能够批量的攻击设备，但是微结构侧信道攻击可以远程进行批量攻击。

**09**

**公钥密码算法**

公钥算法的演进：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBlcYAsbIibqpYfibmAzA4q1iaZSoQI1D5w8GDSHbicKDtpM0iblrbVrFMdlFweTL2WficoXicwn89CODxDb2VUuNTkf9JK2zCV9Fwb0Y/640?wx_fmt=png&from=appmsg)

**10**

**硬件安全的内在挑战**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaARRlXnM3uiacyEObGWYhWjLa5DXJUUKMoRUECY45aydfOibQfmANf2ytBfYQZjibWUm6tox3aetH1JiaqYTiccicy6zoqOqV2ut5kvE/640?wx_fmt=png&from=appmsg)

硬件安全设计和其他信息安全设计一样，也面临着内在的挑战。

首先，随着时间推移，新的攻击方法、新工具也会层出不穷，攻击者会变得越来越强，但是产品并不会变得更加抗攻击。

其次，设备所在的系统会更加复杂，包括网络结构、芯片架构、软件应用等。

因此，在安全设计时，最小化的安全假设，同时保持足够的功能和架构的安全性。

来源：

https://weivid.blog.csdn.net/article/details/117250046?spm=1001.2014.3001.5502

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaD9qjQXZdMwY876TkFlhIUib1kn4wc72e4cib9eharylSOXtAgAq234jTmZYKrXsGd0OALDotYN7MYS8h0mElMEuPddlDZic56KCg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572912&idx=3&sn=58184d21d6dabc713e8d93a0c1d80e40&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUj...