---
title: CAN信号的Intel格式和Motorola格式有什么区别？
url: https://mp.weixin.qq.com/s/Z0Mnkhauqa9a1G1gEyJdMA
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:31:22.984252
---

# CAN信号的Intel格式和Motorola格式有什么区别？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6MmZYM3RhXe9VMUC7cpzxR5iaJoljibtYcwEbNlV5Gb9tS2P7tzr34jQOe3fWZkIBFVFzoCkQbevvcHyP0xfwic9260icSaY73y6iaWzHvRIcsVU/0?wx_fmt=jpeg)

# CAN信号的Intel格式和Motorola格式有什么区别？

谈思实验室

![]()

在小说阅读器中沉浸阅读

以下文章来源于汽车电控知识
，作者安己乐人

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6j5af2Q2k1xdAVsogZDicBJA7ibwvcRA8UDSp3GKThzmZw/0)

**汽车电控知识**
.

快乐学习汽车ECU知识、轻松进入汽车电子行业！

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247568414&idx=2&sn=e8421575011428f2d73cc0b393889274&scene=21#wechat_redirect)

我们在查看CAN总线的数据库，比如DBC文件或者通信协议描述文件时，会看到有一列的属性是Byte Order字节顺序，这个字节顺序可能是Intel也可能是Motorola。无论是软件开发、功能测试还是通信矩阵定义，都需要搞清楚这个属性，否则很容易出错，这个属性有什么用？这两种格式又有什么区别呢？

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCkEcojzdVXBFZB4zJNnoeDPS7WQdwOlhkcZUEYFjeRYAbGqL04Xp2wEWEruUWcHfxiaIKM3YQ9Bg4H3SC3iaOdW2JcdD1quvrJA/640?wx_fmt=png&from=appmsg)

DBC信号示例-Byte Order

**01**

**lsb、msb、LSB、MSB**

在介绍Byte order前，我们先要了解4个术语，首先是lsb和msb，lsb是Least Significant Bit的缩写，表示最低有效位；msb是Most Significant Bit的缩写，表示最高有效位。

这里的最高、最低是指权重的高低，比如十进制的123，其中的百位1权重最高，个位3权重最低。

二进制数据也是一样的道理，比如在1个8位的字节中，bit0权重最低，就是lsb,而bit7权重最高，就是msb。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBfyhjswjM4GcxGjgTTz7fXZB5xrbicFgFciaUlkOeQalI75vm13gMsswVSgxLriamyIMicRdRy11x7ibkXmFpjguklHFsnLZFTJ0rc/640?wx_fmt=png&from=appmsg)

1个字节中的lsb与msb

在汽车的CAN报文中，每个ID可能包含1个或多个信号signal,每个signal占用了不同的位数，每个signal中也会存在lsb和msb。

假如1个字节中有两个信号signal1和signal2，signal1占2位，signal2占6位，则每个信号的lsb和msb分布如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaB1VxwNpfwrfk8tdibFnrT2DNy46uw2yibx7uCwS2G00JR8cw3WDw93qsD5iaKyQufNWFeic3b2rKic9U6UsU3TBGKK3OCDcKCqETGQ/640?wx_fmt=png&from=appmsg)

两个信号中的lsb和msb

信号的起始位start bit就是指信号的最低有效位lsb。

字节中的位有权重，字节之间也是有权重的，如果1个信号很长，超过了1个字节，比如2个字节，那么这两个字节哪个权重更高呢？

这里又出现了两个术语LSB和MSB，LSB是Least Significant Byte的缩写，表示最低有效字节；MSB是Most Significant Byte的缩写，表示最高有效字节。

LSB、MSB与lsb、msb的缩写相同，但是表达的意思不同，一个是位，1个是字节，很容易混淆。通常用大小写来区分，大写的LSB和MSB表示字节，小写的lsb、msb表示位。

Intel格式规定，最低有效字节LSB在低字节，最高有效字节MSB在高字节，比如1个信号占了2个字节，则字节顺序如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDtsQdctE06ia8zl6icEM8j9pInIMOdqOmZEU81672MlycRw3CddDxdECrRhKJYZ8evTSwApdUSHr3CKF2I6DYCsxLXR9eib5Xfzo/640?wx_fmt=png&from=appmsg)

Intel信号中的LSB与MSB

如上图所示，某个信号占了2个字节Byte0和Byte1，共16位，其中的低字节Byte0就是LSB，高字节Byte1就是MSB。而信号的最低有效位lsb位于Byte0,bit0;最高有效位msb位于Byte1,bit7;

**02**

**Intel格式**

下面我们通过2个示例来更加直观的理解下Intel格式，首先是1个车速信号，由于常用的轿车的车速上限通常不会超过200km/h，所以1个字节的数值范围0-255就够了。我们将车速信号定义在第0个字节，共8位，分辨率是1km/h/bit。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBBHrCGbCicNnpKBE3iaoAmTxRnnlmHo5knIgU3mN1MjF33dyGJyLia0ibSfnicdXQdKopdajlMYe5AM2YhNvw9qWyLowSoTxxiahWy8/640?wx_fmt=png&from=appmsg)

车速信号示例-Intel

如上图所示，此时车速信号对应的16进制数是0x3C,即十进制的60，所以收到此报文后会将此信号解析为车速=60km/h。

接下来是1个转速信号，由于转速信号会达到几千转，1个字节的0-255范围不够，所以我们将转速信号定义在第1和第2个字节，共16位，分辨率是1rpm。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBjHp4hnymiblaNHRTvHoAYnUTLCSoUwIvPH6v09rHv5fiaPRhw8cicMosSezPicBnrBnqWRXWC7DBPCica1fchm8hkR6KvMC64gpCw/640?wx_fmt=png&from=appmsg)

转速信号示例-Intel

如上图所示，转速信号占用了2个字节，属于跨字节信号，Byte2是高有效字节MSB，对应的16进制数是0x0B；Byte1是低有效字节LSB，对应的16进制数是0xB8,所以整个转速信号就是0x0BB8，即十进制的3000，接收节点收到此报文信号后会将此信号解析为转速=3000rpm。

**03**

**Motorola格式**

Motorola格式中的位权重排序lsb、msb与Intel格式的定义是一样的，比如在1个8位的字节中，bit0权重最低，就是lsb,而bit7权重最高，就是msb。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCydOIv0ZUrOCHyZh5cWg4TZFwrMKRuXoONYZXzcpGBBguoU3NiaJlsbicf1ZKDooPybgKeYuClJic3lVl2mOFfnEL8pBbDssDpTQ/640?wx_fmt=png&from=appmsg)

1个字节中的lsb与msb

但是跨字节信号中的LSB和MSB就不一样了，Motorola格式规定最低有效字节LSB在高字节，最高有效字节MSB在低字节，比如1个信号占了2个字节，则字节顺序如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAnvRLgegxH3MjDaXy3INPRiczNqPRA4gTJfRBQ5n3Lxt6h67oDqwefCePVR4kR7IWMSVaQb1icLmrmfMMj73ib83icN70TdebHJ0c/640?wx_fmt=png&from=appmsg)

Motorola信号中的LSB与MSB

如上图所示，某个信号占了2个字节Byte0和Byte1，共16位，其中的低字节Byte0是MSB，而高字节Byte1是LSB，这与Intel格式的字节排序刚好相反。

而随着LSB和MSB的不同，信号的最低有效位lsb和最高有效位msb位置也不同，lsb位于Byte1,bit0;msb位于Byte0,bit7;

其实lsb和msb在字节内的排序规则没变，都是从低位（bit0）开始。只是由于字节排序变了，所以它俩的位置会变，是被动的改变。

下面我们通过2个与Intel相同的信号数值示例来直观的理解下Motorola格式，首先同样是1个车速信号，定义在第0个字节，共8位，分辨率是1km/h/bit。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaCZ8BpSjdibqxuO5AQPcBrjmrfANOwXN1PGErqtZVA4cvbFiblPFVtKm0mJVnsZldiaoaUcXnia6U5U4IgpictwWJ9DA7icRUeNw9d7g/640?wx_fmt=png&from=appmsg)

车速信号示例-Motorola

如上图所示，由于车速信号只有1个字节，所以整个信号没有LSB和MSB的概念，只有lsb和msb。

此时车速信号对应的16进制数是0x3C,即十进制的60，所以收到此报文信号后会将此信号解析为车速=60km/h。我们发现这个信号的解析结果与Intel格式是完全一样的。

接下来是1个转速信号，转速信号数值不变，仍然定义在第1和第2个字节，共16位，分辨率是1rpm。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBtxbrulLNibCRUNCrdaBmNuGe7gvWwuflkLgIVl3kk06SeLUTArUGiabjrgvb8tQCJIu1YiagfXCtgiabN4kkQsiagKlIrQrYMrclI/640?wx_fmt=png&from=appmsg)

转速信号示例-Motorola

如上图所示，转速信号占用了2个字节，属于跨字节信号，这里Byte2对应的16进制数仍然是0x0B；Byte1仍然是0xB8。

但是由于Byte2是低有效字节LSB，Byte1是高有效字节MSB，所以最后信号对应的16进制数是0xB80B，即十进制的47112，接收节点收到此报文信号后会将此信号解析为转速=47112rpm。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCDFXAzJNtXdhCgrTAaic6qAUntWtjWlcCPrfxFQmLibfDZ3ABwUW9mtDSw9xnQDK5ibRq2AWruic1loG733NmwTLhxLYof8v3ibkiao/640?wx_fmt=png&from=appmsg)

从这里我们可以看出，相同的报文数据，采用不同的字节顺序格式解析，结果完全不同。

**04**

**start bit 起始位**

通过以上示例还可以看出，两种字节顺序格式的起始位start bit的位置是不同的，起始位在项目开发、测试时会经常使用，通常会通过信号起始位、长度来定位信号在报文中的位置。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAPIKYzfMy5JVHwZJOe5XurEF3atKNpJQ3Y2gYQF1ianbyhhPwia6ictJaGgRCdkQUzDgbscdOyB0Ghn1NlUXT6LBF0CbABk3GVqI/640?wx_fmt=png&from=appmsg)

信号示例-起始位与长度

如上面试示例所示，第1个车速信号的起始位是0，长度是8，我们就知道这个信号占用了第0个字节的共8位；第2个信号起始位是8，长度是16，我们就知道了这个信号占用了报文的第1和第2个字节共16位。

但是实际上定位时是要结合Byte Order来确定的，上面这两个信号都是Intel格式，符合我们位顺序由小到大排列的自然习惯，容易理解，但这也会导致我们忽视对Byte Order的查看，我们再继续看下面这个示例。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBvulFTV7qrvSwM1icc7Hic9zmQiav8qkEekO3vxiaOjFsS2Mdia0D06mpXc5HXia3WfegDRV7b2GRcOhs8pvHT8oKpypwaY3rg2kHjA/640?wx_fmt=png&from=appmsg)

信号示例-起始位与长度-Motorola格式

如上面试示例所示，第1个车速信号不变，仍然占用了第0个字节的8位；第2个转速信号起始位是16，长度是16，如果还是按照Intel格式来定位，我们会认为这个转速信号占用了第2和第3个字节，跳过了第1个字节。

但是由于它是Motorola格式，它的起始位lsb位于高字节Byte2,而高字节是Byte1。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaC8CDVnDSeSkMfHUvFblDicyG9ATTjfyk78hf1yoSZ75vngrQRAJeIagGogQaXibIXV2SZxG7gXicScQkvEeHBKe9j6IgIhUPsm3U/640?wx_fmt=png&from=appmsg)

报文信号layout分布图

我们从分布图中可以更直观的看出，这个转速信号实际是占用了第1和第2个字节，这种情况在实际应用时如果不理解Byte order就很容易出错。

**05**

**小结**

Intel和Motorola格式是CAN总线信号常用的两种字节顺序(Byte order)。两种格式在字节内的位序排列规则是一样的，低位为lsb,高位为msb。

但是两种格式在跨字节信号中的字节排序是相反的。所以在DBC文件或者通信协议描述文件中必须先查看Byte Order字节顺序使用哪种格式，尤其是具有跨字节信号的通信矩阵，一旦用错，解析后的结果一定是错的。

多数情况下同一个DBC会使用同一种字节顺序格式，但是在实际项目中确实也存在混合定义的情况，就是有的信号用Intel格式，有的信号用Motorola格式。这种情况下一定要擦亮眼睛，每个跨字节信号都要仔细确认，否则一不小心就会踩坑!

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

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicHdaQsibvoH8dLYIIcT5YQibwbnuZn1MLCOMydw2SMKWbibsLpooeE2jgCt8FABvsVmlJZO5PO00Ryw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561756&idx=2&sn=f9b8c2149...