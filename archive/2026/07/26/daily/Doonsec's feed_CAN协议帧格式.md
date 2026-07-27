---
title: CAN协议帧格式
url: https://mp.weixin.qq.com/s/hOoA-0jwGtQBvA775HnoCA
source: Doonsec's feed
date: 2026-07-26
fetch_date: 2026-07-27T05:39:57.272581
---

# CAN协议帧格式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaA480SMELuW6YGQhCbFRtJZFsvZtGYZy7ibYXzR60MnUydKuhL8qUhqia5I7MOt36NFmB6YJUZS52JMzYQ7DZjMJgHhv1a0v4nU8/0?wx_fmt=jpeg)

# CAN协议帧格式

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

CAN协议帧的格式十分重要，部分MCU中的CAN外设寄存器就是根据对应帧结构来进行设计的。

* 数据帧：用于发送单元向接收单元传送数据的帧
* 遥控帧：用于接收单元向具有相同ID的发送单元请求数据的帧
* 错误帧：用于当检测出错误时向其他单元通知错误的帧
* 过载帧：用于接收单元通知其尚未做好接收准备的帧
* 帧间隔：用于将数据帧和遥控帧与前面的帧分离开来的帧

**01**

**数据帧**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDC4wrkNXs7eIQCEo75nGXAxwhEtwrCOBVZCfmWdFhTMZvGlRUPVuvibUXGWacLuGj0IbQgxCyiaTEFddibibQvDLllmtEiaf8A7QKk/640?wx_fmt=png&from=appmsg)

（1）帧起始：标识一个数据帧的开始，用于同步，一个显性位，只有在总线空闲期间节点才能发送SOF

（2）仲裁段（场）：ID、RTR、IDE、SRR

* ID：唯一确定一条报文，表明报文的含义和优先级；（标准帧：11位ID；拓展帧：29位ID）
* RTR 远程传送请求位（0：数据帧。              1：远程帧）
* IDE 标识符拓展位     （0：11位ID，标准帧。1：29位ID，拓展帧）
* SRR 远程代替请求位   SRR = 1

以Renesas RH850的用户手册中的Receive Rule ID Register举例：其中就设计到CAN数据帧的相关设置

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBLJUt7ez6s2ic9quuXEBmPmpa3bq2W8ctSk1FYNI34iaXTuc2Smo7wpPxMJaKk32o44CxoiblU2L7SuPKR7a3EJ073EgTHYh1LKo/640?wx_fmt=png&from=appmsg)

（3）控制段（场）：主要用于表示数据段有多少个字节

* r1、r0 为保留位，默认为显性电平（逻辑0）
* DLC 数据长度码：表示数据段的字节数，表示为0~8

（4）数据段（场）：CAN数据帧要发送的数据内容

（5）CRC段（场）：用于进行CRC校验

* CRC：接收到的CRC数据，用于进行校验
* DEL 界定符：用于界定CRC序列，固定1个隐性电平（逻辑1），CRC界定符之前会进行位填充，CRC之后的位域都是固定格式，不允许位填充

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDw4epYRyKtB1ev40M0FunpQVVGEGocabzVp5cGD7jJUkClggf1STJRwZZiaMgGOwZDMJ4z8ZGhkEwYxN0mU4EnJSfQhmGPhPeo/640?wx_fmt=png&from=appmsg)

（6）ACK段（场）：确定报文被至少一个节点正确接收

发送节点在ACK发送隐性位（逻辑1）：

* 正确接收到报文的节点 =》 ACK发送显性位（逻辑0）
* 未正确接收到报文的节点 =》ACK发送隐性位（逻辑1）

发送节点检测应答位是否被显性电平覆盖（即ACK变为显性位，逻辑0）

* 没有 =》 ACK错误

（7）帧结束：7个连续的隐性位（逻辑1），表示帧结束；节点在检测11个连续的隐性位后，认为总线空闲

**02**

**遥控帧**

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA8RAfP4mJylib7ZtYozYpvP9AA5miaN8ibictxxAcy2Jeiae0byABgS3y2EeLFTibwcR9Mric39N3zicrbpiaj77DryJrvL7ALRiaBiaicNbg/640?wx_fmt=png&from=appmsg)

具体各位信息可以参考数据帧

**03**

错误帧

（1）CAN中的错误检测：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAnViaHrQVImEpHtNkmqrba8iarDXwIGY7zhsmicic9rSoXMJjyOm5OSLSydAiaQhLbTJPxsmk9YKVHmibYiaFAyo5KZygqaPEmr9Y18A/640?wx_fmt=png&from=appmsg)

* 位检测：节点检测到的位域自身送出的位数值不同。（注：仲裁段与ACK段不参与位检测）
* 填充检测：在使用位填充编码的帧段，不允许出现6个连续相同的电平
* CRC检测：节点计算CRC序列与接收到的CRC序列不同
* 格式检测：固定格式位场（CRC界定符之后），含有一个或更多非法位
* ACK检测：发送节点在ACK位期间未检测到“显性”电平

发送节点的产生错误一般有：位错误、格式错误、ACK错误

接收节点的产生错误一般有：填充错误、格式错误、CRC错误

**（2）CAN中的错误帧：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC9dHial2yoARxnuLAv8C11pvU1RNjsTtLQyYZ28SHotbOicJH45tCiasjCPOcZ8Pulm8P7QyKWK9ofsc2mM1R0RBx6iabgMh9uK00/640?wx_fmt=png&from=appmsg)

一般流程：检测错误=》发送错误帧=》通知报文错误

主动错误与被动错误的区别：

* 主动错误：只要检查到错误，它立即“主动地”发送错误标志，连续6个显性位（不满足CAN协议的“最多5个连续的同性位”要求）。
* 被动错误：如果检查到错误，它只能“被动地”等其他站点报错，等待的时候不能去动总线，发送了6个隐性位（不满足CAN协议的“最多5个连续的同性位”要求，能够部分或全部被其他节点的显性位覆盖），直到识别出其他站点报错，然后就可以去竞争总线，该干啥干啥。

错误帧的发送

* 位错误、填充错误、格式错误或ACK错误产生后：当前发送的一下位发送错误帧
* CRC错误：紧随ACK界定符后的位发送错误帧
* 错误帧发送后：总线空闲时重发出错的数据帧

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCQtd11Vx7FHuNLPQxt5YHXXyCibp57H0R9HDkn4ib1O6JSkexacIRhkRicC9zALbHt1RWrsvyYuAHK0hNiaHEoibqdmbMPoDSv4jI0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaB1Jw3G8EmfibyEZmEms18hqJta4mLwC2R3C4VrvFvCVsVorjHbMUmZQnPncfvJicpOhCkTtT4JnUxYzdVCuicpRScqLkicz8jM7q8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCVIhxDkywPG0pEDTn9jZ5fhaibFWyn1GQXvwtoqoVzYcI7vnow5miczzEviav5feW0rmYpHPF7IZFgrD9NTwN82azNaQXPKubIeA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBRBYStbEQCFGzAG5xSOsmApSAEXlaUBScmKBv2YcXVWnpjQNoLyCxy0VIsqzdbibewo2bKVKAuVyfiblx3IsdtwuicMX6rUrgiarQ/640?wx_fmt=png&from=appmsg)

**04**

**过载帧**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDm2HBoYsBD2ZYb5yA6CbmcHkYHiaSXQ3fI0sT5AicHU5kSlsK2T0XDb2zR6C9WcrLXMibNGWvTgsUl2q34evfEIXnIjPd5qCB2Rc/640?wx_fmt=png&from=appmsg)

**05**

**帧间隔**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDGFY0Rh4WicicomR5X4xHqRelickaNKjRMHHErFnL3Aaqn2bicdA6NLKHMN0xRJibM3yuRV8AmNkVpTGTkfvX3UOO7GdhKCWDJtW6Q/640?wx_fmt=png&from=appmsg)

来源：CSDN@不吃鱼的猫丿

https://blog.csdn.net/laifengyuan1/article/details/123402635

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAI8KMQg42koBCmQ8xCYRUVtiaem7dsJtOqV3DGOX6iaYEHyxflLz2KpKog3fHia0MOsJl0uRNIdyy32iaibZKpdT4LKv907eGCWcdA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247572036&idx=3&sn=2410465a682d6b6c1f8b801eb583cdae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247573595&idx=1&sn=425c418664766cc4030f3cb49a733ec6&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaA7BGa1vwHmHNlluBv83nX42cOwngUmsgRicQ6oyhxN3HmOsFIml2sUM8Yibk5GELQqiaFLt2dVzmf01r90xrW0vMWGpJX7zOsmkM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247575659&idx=3&sn=1b3acb3a33e0fc992b67b37bc4d04a0e&scene=21#wechat_redirect)

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
...