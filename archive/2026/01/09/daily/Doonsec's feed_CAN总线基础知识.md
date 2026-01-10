---
title: CAN总线基础知识
url: https://mp.weixin.qq.com/s/njGD7YK7yXw5X3rWlSozXA
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:21:48.512301
---

# CAN总线基础知识

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWIY4GZibrggPHuk3Kngk8QbKlviccdn8Gr0KIXK3nLeg6CAklUx5796icQ/0?wx_fmt=jpeg)

# CAN总线基础知识

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247564281&idx=2&sn=699099fdf353a20e4b133c9bb09efbe0&scene=21#wechat_redirect)

讲一个比较传统的车内总线，CAN ( Controller Area Network ) 即控制器局域网。CAN被设计作为汽车环境中的微控制器通讯，在车载各电子控制装置ECU之间交换信息，形成汽车电子控制网络。

一个由CAN总线构成的单一网络中，理论上可以挂接无数个节点。实际应用中，节点数目受网络硬件电气特性限制最多允许挂接 110 个节点。低速率的控制器和收发器比较便宜。所以CAN 高速通信速率一般是500 kbit/s甚至1M，而CAN低速通信标准速率只有125kbit/s以下，我们主要讲高速CAN。低速CAN和高速CAN物理层是不同的。下面进入正文，说个废话看起来这种文章是比较枯燥的但是认真看还是挺有意思的。

**01**

**CAN总线物理层**

CAN 总线物理层通常是使用双绞线即两根线缠绕在一起这两条线分别称为CAN-High线和CAN-Low线。在静止状态时，这两条导线上预先设定相同值大约为2.5V。当逻辑 1 被写进总线里两条线的电平是 2.5V 并被定义为隐性位。当逻辑0被写进总线里一条线被上拉到为 3.5V叫CAN高 另一条线被下拉到1.5V叫CAN低。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWgnthfRu3vOXNzIEml7UhLbXh7WNQhqN2WvCAqyzCCy9OmsR4aTaWGA/640?wx_fmt=png&from=appmsg)

这里有人就问为什么CAN将0定义为显性位，而不是跟计算机中的逻辑一样，1为显性？这是因为显性要有能覆盖隐性的能力，众所周知，在线与逻辑关系下，0才具有这种能力（1·1·1·……·1·1·0 = 0），很好理解不管多少个1与上0之后都等于0，所以将0定义为显性。1定义为隐性。

有人就问如果大家都往总线上发报文冲突了怎么办？这里就采用了CSMA/CD “载波侦听多路访问/冲突检测”（Carrier Sense Multiple Access with Collision Detect）技术。利用 CSMA 访问总线，可对总线上信号进行检测，只有当总线处于空闲状态时，才允许发送。利用这种方法，可以允许多个节点挂接到同一网络上。当检测到一个冲突位时，所有节点重新回到‘监听’总线状态，直到该冲突时间过后，才开始发送。当总线上有两个节点同时进行发送时，必须通过“无损的逐位仲裁”方法来使有最高优先权的的报文优先发送。

在 CAN 总线上发送的每一条报文都具有唯一的一个 11 位或 29 位数字的 ID。CAN 总线状态取决于二进制数‘0’而不是‘1’，所以 ID 号越小，则该报文拥有越高的优先权。因此一个为全‘0’标志符的报文具有总线上的最高级优先权。因为如果显形位0和隐性位1都被不同的节点同时写进总线里，总线显示显形位因为显性位覆盖了隐性位。

下面是一个典型的CAN总线结构

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWcs7NaWrXU6s7Gtb1ica50rHuRWAcLYtibPNQr8mpibLkOD784XCHTGwMQ/640?wx_fmt=png&from=appmsg)

为什么总线上会有两个终端电阻,因为发送方通常都有电流输入到 CAN 总线上，而接收方的阻抗通常很低。所有在总线上就有很多多余的能量，加上120 欧电阻就可以消耗掉这次多余的电流，从而防止信号反射干扰。

**02**

**CAN数据帧**

Bosch发布CAN2.0标准，分CAN2.0A标准帧(11位标识符)和CAN2.0B扩展帧(29位标识符)。注意这里的扩展帧可和CANFD没关系。目前应用的CAN器件大多符合CAN2.0规范。标准帧主要用于乘用车，扩展帧主要用于商用车。

数据帧的作用是用于传递0-8byte数据，下面是数据帧的帧格式。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOW604UcITlLETwfuS7CkknxNKn0KAtpE9Qlqk4F8LXLNBsNHTiaqJKYbg/640?wx_fmt=png&from=appmsg)

数据帧由7个不同的位场组成：

(1)帧起始（Start of Frame）

帧起始的标准和扩展格式相同，表示帧开始的段。1 个位的显性位。

(2)仲裁场（Arbitration Frame）

仲裁段表示数据的优先级的段。就是我们平时说的报文ID。标准格式的ID有11个位。禁止高 7 位都为隐性。（禁止设ID=1111111XXXX）扩展格式的 ID 有 29 个位。禁止高 7 位都为隐性。（禁止设定：基本 ID=1111111XXXX）

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWpSsMZq6Gz7Bhkf8djL1C1zmXL4ibEjaPKABPs9RfVwianCKwG8xjQLhw/640?wx_fmt=png&from=appmsg)

(3) 控制场（Control Frame）

控制段由 6 个位构成，表示数据段的字节数。标准格式和扩展格式的构成有所不同。

(4)数据场（Data Frame）

数据段传输的数据包含8个字节64个bit。MSB高位先传。在后面讲CAN矩阵的时候会详细讲数据内容。

(5)CRC场（CRC Frame）

CRC段是检查帧传输错误的帧。由15个位的CRC序列和1个位的CRC界定符（用于分隔的位）构成。CRC的计算范围包括帧起始、仲裁段、控制段、数据段。接收方以同样的算法计算CRC值并进行比较，不一致时会通报错误。

(6)应答场（ACK Frame）

ACK段用来确认是否正常接收。由ACK槽(ACK Slot)和ACK界定符2个位构成。发送单元在ACK段发送2个位的隐性位。接收到正确消息的单元在ACK槽(ACK Slot)发送显性位，通知发送单元正常接收到。ACK槽的ACK应答帧是非常奇特的，在其他通信机制里面是没有的，这个也是为什么CAN单个节点通信不了的原因。

注意，接收单元并非将整个报文重新发送一遍，而是在发送方发ACK槽期间（CRC界定符后）发送显性位，发送节点通过回读确认。只用1位电平反馈而不是整个帧，效率高，只要有一个节点确认收到，就算发送成功。

(7)帧结尾（End of Frame）

帧结束是表示该该帧的结束的段。由7个位的隐性位构成。

其实CAN消息里面还有个位填充机制，是为防止突发错误而设定的功能。当同样的电平持续5位时则添加一个位的反型数据发送单元的工作在发送数据帧和远程帧时，SOF～CRC段间的数据，相同电平如果持续5位，在下一个位（第6个位）则要插入1位与前5位反型的电平。接收单元的工作在接收数据帧和远程帧时，SOF～CRC段间的数据，相同电平如果持续5位，需要删除下一个位（第6个位）再接收。如果这个第6个位的电平与前5位相同，将被视为错误并发送错误帧。在帧内除了CRC界定符、ACK域和EOF外，其余部分均应用到位填充机制。

**03**

**什么是CAN矩阵**

下面是车载ECU开发需要用到的CAN矩阵，通过CAN矩阵就能知道应该往总线上怎么发收据和收到数据后如何解析出正确的信号。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWJmTUG7kqsphJkWA02DvRib3um4jFj4L0fYpOyEHlYRkoWnwxxx51LoA/640?wx_fmt=png&from=appmsg)

上面的图是一个比较老的CAN矩阵，其中MsgID就是CAN报文的ID也叫仲裁场，固定周期指的是某ECU会以1秒周期向总线上发送这个报文。消息长度8指的是标准CAN8个字节的数据。而这个报文里面总共有两个信号，一个信号表示总里程，一个信号表示保养公里数。

下面是报文的布局图Motorola格式，左侧从上到下的1-8指的是数据场字节1到字节8，从左往右的8到1指的是一个字节里面的8个bit。灰色的就是总里程的信号位置，紫色的是保养公里数的信号位置。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWMttrU1vIShhJ2RESMVfCndoU3RRBluqtynZh7DVibfp6PXnC3TPbOYQ/640?wx_fmt=png&from=appmsg)

LSB：least significant bit 表示二进制数据的最低位。MSB : most significant bit 表示二进制数据的最高位。在大端格式中，最重要的字节（即msb）存放在最低的内存地址处，而最不重要的字节（即lsb）存放在最高的内存地址处。这里为啥说msb最重要呢，并不是说lsb不重要，而是msb影响更大，自行理解比如说一个数10001，左侧的1最重要，所以把最左侧的1放在低内存地址处先发送。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWxKX7M8sXSJeqhJysGTAsWsmUticpj77UcDhNNxKrhcVyVWWrRcNN83A/640?wx_fmt=png&from=appmsg)

CAN矩阵表中品质因数和偏移量是干啥的，为什么会有Factor和Offset。因为CAN上没法发负数和小数。

在计算机科学中，负数通常通过二进制补码表示。在硬件层面，处理符号位需要额外的逻辑电路来处理二进制补码的表示和运算。这会增加硬件的复杂性和成本。具体来说：符号位检测：需要额外的逻辑来检测最高位是否为1，以判断数值是正数还是负数。补码运算：需要额外的逻辑来处理补码的加法和减法运算。错误检测：需要额外的逻辑来检测溢出和下溢等错误。在软件层面，处理符号位需要额外的处理步骤来正确解释和转换数据。这会增加软件的复杂性和运行时间。

CAN协议的设计目标是简单、高效、可靠，主要用于实时控制和嵌入式系统。而无符号整数的处理速度更快，使用无符号整数可以避免处理符号位带来的复杂性。所以规定CAN上只能传无符号整数。尽管CAN协议本身不支持直接表示负数和小数，但应用层可以通过以下方式实现这些功能：偏移量（Offset）：通过偏移量将无符号整数转换为负数。因子（Factor）：通过因子将无符号整数转换为小数。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWGvj5Fiano0C8Zicxb7aAlNcxAw5SUumvUBOCk3rrxEcE32qbDXlASZ7A/640?wx_fmt=png&from=appmsg)

我之前在这里总是不明白CAN上发出来的为啥叫RawValue原始值实际值却叫PhysicalValue物理值，不是应该在CAN线上传的才是物理层的值才应该叫物理值么，后来才明白，原始值指的是各控制器发出来的值，而PhysicalValue并不是物理值而是实际的物理量这样理解就好理解这个公式了。

公式的意思就是：实际物理量=CAN上收到的值\*精度+偏移。

附上AUTOSAR架构下can报文的发送和接收协议栈

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw8g7CmYo2HCyI8XPGZehPOWhXXDibzDsAwXkiaEHdqXe2jQQutHfoFLnnk7Gku4u9fDZqS4CFEy3QVA/640?wx_fmt=png&from=appmsg)

来源：风猴蓝魔

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

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaF...