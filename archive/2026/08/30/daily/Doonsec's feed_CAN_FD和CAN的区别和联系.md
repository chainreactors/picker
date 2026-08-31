---
title: CAN_FD和CAN的区别和联系
url: https://mp.weixin.qq.com/s/dt9i_A3hOYaVlJhXXjyn0Q
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:50:36.211606
---

# CAN_FD和CAN的区别和联系

# CAN\_FD和CAN的区别和联系

谈思实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaAf3Eh4RynoftF7dz1NtAd2SYNXWsm8EaWOewRjSXxcCjicH0t59JtNOypwHKjHNlxV8CeJft7puVrzuEzoHibdHGKJ2Bhcc4iajI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247576684&idx=2&sn=99b4244a2b1c95bd46442f3151ac6b4b&scene=21#wechat_redirect)

**01**

**宏观上的区别和联系**

**1.1：数据段传输性能上的区别，这里就是指波特率上的区别**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhrTVkfZBlHqDDMalVS18iawXTC38BFnA7MK9vXI9Fqguzea45CsepIGEg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**1. 2：数据段长度的区别**

(1)CAN标准帧和扩展帧的数据段0-8Byte

(2)CANFD的标准帧和扩展帧数据段长度是0-64Byte

**1.3：帧类型不一样**

* CAN有 1：数据帧，远程帧 ， 错误帧，扩展帧
* CAN FD 有数据帧 错误帧 扩展帧

**1.4：CAN只能以固定的波特率发送，CANfd可以有两种不同的波特率（这里指的是同一帧报文可以有两种不同的发送速率）**

如下图所示，other higher speed 指的是数据段，这也是CANfd比较神奇的地方，就是说在SOF-DLC区间内以较低的速率发送数据，而在数据段波特率突然提升，CRC-END阶段又恢复低速率运行。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhreDO6tx147BPK5KcjKbjTibl41PvxncRDmH0KJxXCOX8NxMU7ow1MCYA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**1.5：CRC位数和格式不一样**

当报文为传统CAN时，仍采用原有的CRC多项式。

当报文为CANFD且数据长度小于等于16字节时，调整为17位的CRC多项式。

当报文为CANFD且数据长度大于16字节时，则调整为21位的CRC多项式。

注意：这里只是说的是“多项式”，而不是指CRC整个占据的bit数量。1.7小结后处，做了整体的说明。

**1.6 CRC计算时机不同**

在传统CAN中，位填充（连续5位相同位后填充一位相反位）是在CRC计算之后进行。当CAN控制器发送报文时，先对需要进行校验的数据段（即：SOF-数据段的最后1bit位）CRC计算后，再填入填充位发送；接收时，则对接收数据移除填充位后，再做CRC校验。

在CANFD中，CRC计算时机调整为位填充后。也就是说，发送方发送时，先对报文进行位填充后，再做CRC计算。接收方，也使用同样的方法进行CRC计算。这种方式增加了对填充位的CRC计算，降低了错误漏检的概率。

易错理解点：

1、CAN和CANFD类型报文，接收方对数据处理时，都要去除填充位

**1.7 增加固定填充位和填充位计数**

CANFD中，CRC域采用一种固定填充位的格式：在CRC段第一位及接下来的每四位增加一个固定填充位（Fixed Stuff Bit，以下简称为FSB），填充位为上一位的反码。

以下分别为CRC17和CRC21的固定填充位（FSB）位置。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhreSicUJFRCNicsxnCQAOeVKOhshRRgt1BWGBe21XNtvqDecyU45Dcg7eA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

除了固定填充位之外，CRC域的起始还包含了3位的填充位计数，及1位填充位计数检验位，以进一步提高通信可靠性。填充位计数在CRC段的位置如下图红框所示。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5Yhr1kcT2oEYIvNzx5VAvutJCA8K97ze44OrOGAHzkuj5TnBRs6FDIl8lw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

3位填充位计数表示的值为实际填充位计数对8取模的结果，采用格雷码显示。奇偶校验位对填充位计数进行奇偶校验。详见下表。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5Yhr1bKKGdFTwpeHtjM1RzicUEPJcTC0GJ0ISPHYW7gzPPt6YexrrQMIhgA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

需要注意的是，non-ISO CANFD协议标准，无固定填充位FSB及填充位计数。若使用USBCANFD-200U时，遇到通讯的CANFD控制器为non-ISO标准，可以在打开通道时，选择CANFD标准为non-ISO，以兼容non-ISO标准CANFD控制器。

小结：CRC整体 = CRC序列（17bit或21bit）+固定填充位（6bit或7bit）+ 填充位计数（固定4bit）

（1）当数据段字节书<=16Byte时，CRC = 17+6+4 = 27bit；

（2）当数据段字节书>16Byte时，CRC = 21+7+4 = 32bit；

**1.8 CAN\_FD两种填充方式的兼容**

CAN\_FD采取了两种填充格式：

1、逢5填1

2、FSB填充法

如果出现如下情况，该如何处理？有如下两种方案

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5Yhrlfandic6r6LEx2YVsDOeqeckJic6glLIIicVxNm114hwIOU0yv7z1p7gA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

1、有些同学会说，数据段需要额外填充一个0，如这样 111110。

2、又有同学会说，不用，直接在首个（图中，从左往右首个FSB）直接填充0，即可。

实际上CANFD,采取第2种方案。

**1.9 CAN\_FD对CRC错误发生时，错误帧发送的时间**

CAN传统帧，接收方应该在检测到CRC错误后，在ACK界定符之后，开始发送错误帧。

CAN\_FD帧，接收方应该在检测到CRC错误后，在CRC界定符之后3个bit位的时间后，开始发送错误帧。

A、 CAN\_FD发送错误帧，过载帧 采取的位速率

CAN\_FD的错误帧和过载帧采取和仲裁段一致的位速率，（即，低速率发送）错误帧和过载帧。

B、 CAN\_FD的CRC填充字段发送填充位错误

**02**

**微观上的区别和联系**

**2.1 帧结构不一样**

CANFD标准帧格式

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhrRsVEGia25vutuC99LyUl5WrKZibvGFicq2TiafT38NHxeibQssAWic6W7Diaw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

1：SOF帧开始:

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhrM9O7FeWR97TJpes6llsKTnn0XDIAAVNEWlLWicJIIUkbKMNpYzreUibQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

下面这两张图，分别给出了CAN帧和CANFD 帧的标准形式和扩展形式

给大家提出几个问题

1：请总结 CANFD扩展帧格式与标准帧格式的不同

2：总结CAN   帧标准格式和扩展格式之间的区别和联系

3：总结CAN标准格式和CANFD标准格式之间的区别和联系

4：总结CAN   扩展格式和CANfd扩展格式之间的区别和联系

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5Yhr8BNGGuLvv5VNiaqaSfg1QFSxmYUSsLmEts1MWc7WjEoDvQ5TbylBk3Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhrkyDFeG0Zicx8mnr1OgfpfZg4fLrwl5dr7Emibj6icfDosgCxu4EW6m2ag/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

**2.2、DLC不一样**

注意点，我们可以观察到CAN帧和CANFD帧，DLC都为4bit，CAN帧最大发送字节为8Byte，4bit能完全表示。

但是CANFD的DLC，也只有4bit，4bit最大能表示十进制数15。fd最大发送字节为64该如何表示

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhrINdqGQykibw6SWQ8ibDJYQQwWIiboicLudHqzNnBqXs6ic2N7nVS5PicA1Eg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

前4个，二进制数值每增加1，代表长度+4。第5位+8，第6个＋16，第7个+32。成倍增加

延伸一下，如果我们使用设备，模拟发送CAN\_FD帧，DLC必须要是（0-8||12||16||20||24||32||48||64）

如果有人告诉你,他设计的CAN\_fd帧数据段长度为15，只能说明这个人是完全不懂CAN\_FD的。

**2.3 CAN\_FD中 （BRS位+CRC界定符位 ），所占用的位时间?**

过上面的学习，大家都知道，CAN\_FD中的BRS置位时，从BRS-CRC界定位速率切换为高速率。问大家一个问题：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhrA2cicnFUvRDqTLwGibPgic5qiaHM4td7r6bs9AzPeicYTVuUSJDeYhJSaoQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

问？(BRS位+CRC界定符位 ）所占用的位时间?,前提条件数据段速率2M，仲裁段为500K。

答：如果你不假思索的回答，100uS，那你就错了。因为你想当然得认为位速率切换，从BRS位开始出就开始切换为2M，然后到CRC界定符位结束处。其实是错误的。

正确的其实是如下图

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhrEzOvS1YkCV33057ibPHzHJD0DHF3c5jmZc6RR33EqxM2sc9sG4a0u4Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

这样结论就出来了， BRS位+CRC界定符位 =(一个500k的位时间)+（一个2M的位时间）。准确来说，是在采样点处，速率会发送切换。

大家可以拿示波器，去实际量一下BRS和CRC界定符实际的为时间。我先告诉你答案：

BRS位时间 =  （500k的位时间）（仲裁段采样点（百分比）+（2M的位时间）（100%- 数据段采样点（百分比）。

（500k的位时间）=2us，（2M的位时间）=500ns，假设 “仲裁段采样点（百分比）” = 70%，“数据段采样点（百分比）”=80%。

计算结果= 2us \* 70%+ 500 \*(20%)=1500ns，左右。

实测波形如下：1.499us，也证实了我们的计算。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhrlkjpgptgUbJ6YV9U1U77C8oa9hIibp7cnsJicDxhwzu3dlWXIjicqibbgw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

**03**

**总结1：CAN各种帧之间的关系**

通过以上的比较，我们能大致得出来，CAN标准帧&CAN拓展帧，CANFD标准帧和CANFD拓展帧，CAN标准远程帧&CAN拓展远程帧。下图也表示了，他们之间的关系。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhrjxV28RmhXDV1jRQmAuYicXCvZOKZUOgVw9nqmicT61Req12uau5MwYIg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

首先总结所有帧结构的相同点：

（1）只要是CAN/CANfd帧，[SOF----ID(11bit)]，任何帧之间的结构都一样。

（2）只要是CAN/CANfd帧 [DLC---CRC)，任何帧之间的结构都一样。

（3）只要是CAN/CANfd帧（CRC-EOF]，任何帧之间的结构都一样。

**04**

**总结2：从CAN总线的发展历史角度看，CAN不同帧之间的区别和联系**

我们尝试从CAN帧的发展历史来代入进来理解，从实际应用角度去切入。这会让我们更加理解为什么各种CAN帧之间的不同，以及为什么不同。

**4.1 CAN标准帧**

首先来看，最简单的CAN标准数据帧 sof+（11bitID）+RTR(远程标志位：1隐形代表：远程帧)+IDE(拓展帧标致位：1=是拓展帧)+r0+DLC+Data+CRC(15bit)+CRC界定符+ACK(1bit)+ACK界定符+EOF(7bit隐形位)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhrplRlKZXDOWdNp0YygjPKnB4Fnl23Sic0cKaJqJBMzSnJZdCwOaESxpQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

首先CAN被最开始定义出来时，规范的设计者，先设计了  帧起始+仲裁段+控制段+数据段+CRC段+ACK段+帧结束段。

帧起始段，暂时只要理解为一个位的显性位。

仲裁段。一开始设计了11Bit,位，最大能表示0x7EF(2031个ID细心的同学发现了，不对啊！11bit最大不是能表示0x7FF，这是因为11位ID,的高7bit不能全置1的原因导致的),ID段首先被发送到CAN总线上。接收节点根据事先设定，决定接收或者不接受这个帧。

当节点决定接收这个文件后，立马就要接收控制段的信息，假设CAN被开发出来的时候，控制段的前三位都是预留位，程序对该段信息直接忽略，开始接收DLC,和数据段（这才是我们需要的最重要的信息），接收完数据段后，程序开始接收CRC校验段（校验范围sof--接收的数据段最后一个字节）。然后自己开始计算CRC。最后判断 （接收的CRC） =（自身计算的CRC），来决定是否在ACK端应答。最后发送帧结束标志。至此一个帧算是正式的发送且被成功接收。

以上过程都很完美。一直过了好几年，出现了以下两种情况：

（1）汽车电子发展的越来越快，一个总线上挂载的节点越来越多，ID数量不够用了（本质上0x7EF(2031个ID是够用的)但是实际应用中 为了维持系统的稳定性，不会依次选取所有的ID），这是需要扩展ID,于是大家坐一起商量了一下，决定把ID再增加18BIT。就如图所示：扩展之后532676607位，绝对是够用了。

这还让我想到了通讯界一个很有意思的问题，就是IP地址，当初设计ip地址的时候，ip地址为4个Byte，也就是4294967295个IP可以用，出去一些特定用途的IP外（如广播，组播用途），其他IP都可以分配给个人或公司团体，大家都认为这些IP地址以及足够使用了，结果没想到互联网仅仅过了几十年的发展，目前这些IP已经快分配完了。于是大家又是想出了CIDR，又是想出了IPV6协议（也就是6个Byte的ip）。

说上面一段的原因，我是想说，很多时候，在制定标准时，好像很合理，但是随着技术的发展很多事情的发展，会大大出乎最初的意料。有时防患于未然，虽然要牺牲掉一部分性能和效率，很多时候也不失为一种合理的选择。

![图片](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw80FprVCd5qQibD6Bxgg5YhrlA90NbDfVuW0wSxYqYzhqAh...