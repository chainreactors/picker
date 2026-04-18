---
title: CAN信号的Intel格式和Motorola格式有什么区别？
url: https://mp.weixin.qq.com/s/nymnXmmWOa-9z-sMF3WHig
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:27:41.471728
---

# CAN信号的Intel格式和Motorola格式有什么区别？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6MmZYM3RhXe9VMUC7cpzxR5iaJoljibtYcwEbNlV5Gb9tS2P7tzr34jQOe3fWZkIBFVFzoCkQbevvcHyP0xfwic9260icSaY73y6iaWzHvRIcsVU/0?wx_fmt=jpeg)

# CAN信号的Intel格式和Motorola格式有什么区别？

谈思实验室

![]()

在小说阅读器读本章

去阅读

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

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

我们在查看CAN总线的数据库，比如DBC文件或者通信协议描述文件时，会看到有一列的属性是Byte Order字节顺序，这个字节顺序可能是Intel也可能是Motorola。无论是软件开发、功能测试还是通信矩阵定义，都需要搞清楚这个属性，否则很容易出错，这个属性有什么用？这两种格式又有什么区别呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaDvesyVU2OeJ9sHqd6Onf4wM2NeUZZhWZQRvEk6VGrggy6rwXvnYzrX0syuiaCWPpxzZJ9l6dMc8Gx3sF439xGTm92IDW8ECKE0/640?wx_fmt=png&from=appmsg)

DBC信号示例-Byte Order

**01**

**lsb、msb、LSB、MSB**

在介绍Byte order前，我们先要了解4个术语，首先是lsb和msb，lsb是Least Significant Bit的缩写，表示最低有效位；msb是Most Significant Bit的缩写，表示最高有效位。

这里的最高、最低是指权重的高低，比如十进制的123，其中的百位1权重最高，个位3权重最低。

二进制数据也是一样的道理，比如在1个8位的字节中，bit0权重最低，就是lsb,而bit7权重最高，就是msb。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaBQibBoQ1lYLrnhQwdD3H5gCuhpVIQ1XmUjNl4w9ice14DD54Yhe7W4ISLjVfxdicmJnaaviakGqzTCneoE26AfYB1V34NcaGuUhlg/640?wx_fmt=png&from=appmsg)

1个字节中的lsb与msb

在汽车的CAN报文中，每个ID可能包含1个或多个信号signal,每个signal占用了不同的位数，每个signal中也会存在lsb和msb。

假如1个字节中有两个信号signal1和signal2，signal1占2位，signal2占6位，则每个信号的lsb和msb分布如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDAKMAMGE0EKia7Elm4EBZzrGFyh5rk5J39xVCoH0L4KtLq2o4uUN2w2fiaDnQvE85NEYJibBubQ9mVMaN7wGIMJyQU9K3P8ibbzIs/640?wx_fmt=png&from=appmsg)

两个信号中的lsb和msb

信号的起始位start bit就是指信号的最低有效位lsb。

字节中的位有权重，字节之间也是有权重的，如果1个信号很长，超过了1个字节，比如2个字节，那么这两个字节哪个权重更高呢？

这里又出现了两个术语LSB和MSB，LSB是Least Significant Byte的缩写，表示最低有效字节；MSB是Most Significant Byte的缩写，表示最高有效字节。

LSB、MSB与lsb、msb的缩写相同，但是表达的意思不同，一个是位，1个是字节，很容易混淆。通常用大小写来区分，大写的LSB和MSB表示字节，小写的lsb、msb表示位。

Intel格式规定，最低有效字节LSB在低字节，最高有效字节MSB在高字节，比如1个信号占了2个字节，则字节顺序如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBzFHr27BEEyNqSg5cb1ySZM76TEWba5ibjWDFLCGJqLeJmjSomrkicrzMUmTL9MreBZXjZ2SW0KsqIUM9aIPlGa35bFSyMMYCO8/640?wx_fmt=png&from=appmsg)

Intel信号中的LSB与MSB

如上图所示，某个信号占了2个字节Byte0和Byte1，共16位，其中的低字节Byte0就是LSB，高字节Byte1就是MSB。而信号的最低有效位lsb位于Byte0,bit0;最高有效位msb位于Byte1,bit7;

**02**

**Intel格式**

下面我们通过2个示例来更加直观的理解下Intel格式，首先是1个车速信号，由于常用的轿车的车速上限通常不会超过200km/h，所以1个字节的数值范围0-255就够了。我们将车速信号定义在第0个字节，共8位，分辨率是1km/h/bit。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaDkSN8jVibCs9RfIzaS6uU0ia07HUJHLs8hNTUo8XcN8VXr7GibUBCLNpGyJGZISCknoATXILKDKLlVWwev3Zic67LdjqgN71niafn4/640?wx_fmt=png&from=appmsg)

车速信号示例-Intel

如上图所示，此时车速信号对应的16进制数是0x3C,即十进制的60，所以收到此报文后会将此信号解析为车速=60km/h。

接下来是1个转速信号，由于转速信号会达到几千转，1个字节的0-255范围不够，所以我们将转速信号定义在第1和第2个字节，共16位，分辨率是1rpm。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBQiaay5hUfTjd6yJ5V2Tsic9RGhYeyywxQX0L238dnye44iblos2DvVjsHGlFkKvTRLvbaNoz2zCPSwt1ICsNkc4ev6gqFLQzQxw/640?wx_fmt=png&from=appmsg)

转速信号示例-Intel

如上图所示，转速信号占用了2个字节，属于跨字节信号，Byte2是高有效字节MSB，对应的16进制数是0x0B；Byte1是低有效字节LSB，对应的16进制数是0xB8,所以整个转速信号就是0x0BB8，即十进制的3000，接收节点收到此报文信号后会将此信号解析为转速=3000rpm。

**03**

**Motorola格式**

Motorola格式中的位权重排序lsb、msb与Intel格式的定义是一样的，比如在1个8位的字节中，bit0权重最低，就是lsb,而bit7权重最高，就是msb。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaAjJwxxS8cEQRf7k2E6nfRuiaicO1rLc5mnrHf5574AebVHzNfBEWQZUkzPmoHEZIvoWMlicT17yfw6ZiaVNeicKxLy39OH3xXz4S3U/640?wx_fmt=png&from=appmsg)

1个字节中的lsb与msb

但是跨字节信号中的LSB和MSB就不一样了，Motorola格式规定最低有效字节LSB在高字节，最高有效字节MSB在低字节，比如1个信号占了2个字节，则字节顺序如下：

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAAWL5DsMrtIJvJ8GmWgdEelqvQSfZTmmsyaFJzf8MrBo5veMXCGOwibdiaywqMOolDzpCjfPHX5pa8qTsR5bjWsC9cwUuc5wxSY/640?wx_fmt=png&from=appmsg)

Motorola信号中的LSB与MSB

如上图所示，某个信号占了2个字节Byte0和Byte1，共16位，其中的低字节Byte0是MSB，而高字节Byte1是LSB，这与Intel格式的字节排序刚好相反。

而随着LSB和MSB的不同，信号的最低有效位lsb和最高有效位msb位置也不同，lsb位于Byte1,bit0;msb位于Byte0,bit7;

其实lsb和msb在字节内的排序规则没变，都是从低位（bit0）开始。只是由于字节排序变了，所以它俩的位置会变，是被动的改变。

下面我们通过2个与Intel相同的信号数值示例来直观的理解下Motorola格式，首先同样是1个车速信号，定义在第0个字节，共8位，分辨率是1km/h/bit。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBx03ATAm73iacKyA4szu6AH5Jls7ureZibKY3gThAj9mFQ4AGHZfoakfRFa07RibGNJJaS7PuXJw9ibibeqvrTqIXURYaM4ibJBibXlw/640?wx_fmt=png&from=appmsg)

车速信号示例-Motorola

如上图所示，由于车速信号只有1个字节，所以整个信号没有LSB和MSB的概念，只有lsb和msb。

此时车速信号对应的16进制数是0x3C,即十进制的60，所以收到此报文信号后会将此信号解析为车速=60km/h。我们发现这个信号的解析结果与Intel格式是完全一样的。

接下来是1个转速信号，转速信号数值不变，仍然定义在第1和第2个字节，共16位，分辨率是1rpm。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaCqFopebJ7uiayalwicZ0SicMMoet94UHF5OaOGBxYMgkiaFzrFJMArKDib4Gvu8BlyG1S6NqHs7xsvNb32YyttfIayrbVBprYp1fkY/640?wx_fmt=png&from=appmsg)

转速信号示例-Motorola

如上图所示，转速信号占用了2个字节，属于跨字节信号，这里Byte2对应的16进制数仍然是0x0B；Byte1仍然是0xB8。

但是由于Byte2是低有效字节LSB，Byte1是高有效字节MSB，所以最后信号对应的16进制数是0xB80B，即十进制的47112，接收节点收到此报文信号后会将此信号解析为转速=47112rpm。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaBmDicpKAhRZv5iaYWvKVicHyxDuf7jO7qAias5MeAvUxdw3epJE4lCkjkAqTY9MPibicVicKu3eu8SNovLENIKcH0VyfeiaClN3DFjsVk/640?wx_fmt=png&from=appmsg)

从这里我们可以看出，相同的报文数据，采用不同的字节顺序格式解析，结果完全不同。

**04**

**start bit 起始位**

通过以上示例还可以看出，两种字节顺序格式的起始位start bit的位置是不同的，起始位在项目开发、测试时会经常使用，通常会通过信号起始位、长度来定位信号在报文中的位置。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaD6LCP19BTJovAiby0CpyCkbqHAialC65P6KsNmg8zCerPicoSQug5YAZXs5mhScmibS6fhmX7mibehcoGbs1qvibiaXN32x3fxzRiaSY4/640?wx_fmt=png&from=appmsg)

信号示例-起始位与长度

如上面试示例所示，第1个车速信号的起始位是0，长度是8，我们就知道这个信号占用了第0个字节的共8位；第2个信号起始位是8，长度是16，我们就知道了这个信号占用了报文的第1和第2个字节共16位。

但是实际上定位时是要结合Byte Order来确定的，上面这两个信号都是Intel格式，符合我们位顺序由小到大排列的自然习惯，容易理解，但这也会导致我们忽视对Byte Order的查看，我们再继续看下面这个示例。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zQ19N6bPViaALdxia97R8jrlINibWtWzA5I1CDGdtRdVtiauWqMeKXc63gmVzssDl8eteOHfytiadJyQyDzfqgekIuRJhVFiclP2ibqdxUG39gUABs/640?wx_fmt=png&from=appmsg)

信号示例-起始位与长度-Motorola格式

如上面试示例所示，第1个车速信号不变，仍然占用了第0个字节的8位；第2个转速信号起始位是16，长度是16，如果还是按照Intel格式来定位，我们会认为这个转速信号占用了第2和第3个字节，跳过了第1个字节。

但是由于它是Motorola格式，它的起始位lsb位于高字节Byte2,而高字节是Byte1。

![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaC7619DDj4fE32XW1YeLQcdKuUFFPgqffVchrJOkdib4CAZSt3RMnWuk6ogjpRppniaCV0JnXdFEicIs1ypkME3houXcelZcnwBsI/640?wx_fmt=png&from=appmsg)

报文信号layout分布图

我们从分布图中可以更直观的看出，这个转速信号实际是占用了第1和第2个字节，这种情况在实际应用时如果不理解Byte order就很容易出错。

**05**

**小结**

Intel和Motorola格式是CAN总线信号常用的两种字节顺序(Byte order)。两种格式在字节内的位序排列规则是一样的，低位为lsb,高位为msb。

但是两种格式在跨字节信号中的字节排序是相反的。所以在DBC文件或者通信协议描述文件中必须先查看Byte Order字节顺序使用哪种格式，尤其是具有跨字节信号的通信矩阵，一旦用错，解析后的结果一定是错的。

多数情况下同一个DBC会使用同一种字节顺序格式，但是在实际项目中确实也存在混合定义的情况，就是有的信号用Intel格式，有的信号用Motorola格式。这种情况下一定要擦亮眼睛，每个跨字节信号都要仔细确认，否则一不小心就会踩坑!

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zQ19N6bPViaD738NK3hXLv1oL9xjlzeu0siarVOkzWt088J1LKJicdaAD8r7fCjdyPhfSticWDpGJEp8icicAezo0q95ibSQJhK9I7xtYexez76cgE/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570424&idx=3&sn=50dd348126dde62996f11475319db5db&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaASYOhicdX7k6gXj7CQY6eYvw88KiaIjiawkTOEJZ8aPmOaNLd6ic7iaA3NOEQsDvQWDLo4nN5wiajlKfDpFDPdbhxKTNCZkZqv7mEJ0/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247571811&idx=2&sn=5cd258a17258896c406c0c10a44e857b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/zQ19N6bPViaAgXyLqfnkPJhyibCoBSOMGSsdQ03SEf01kcUbPAEzhf5nb6vyvYWINevstJCARUgy8qNpTa2lKVo7g7RPFm8IicY9aYtviaowaTE/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOT...