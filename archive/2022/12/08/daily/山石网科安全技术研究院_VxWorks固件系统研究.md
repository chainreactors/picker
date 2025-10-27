---
title: VxWorks固件系统研究
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247498755&idx=1&sn=a4fc5c6469ba08b04a93ee658fd115db&chksm=fa5229bdcd25a0aba9751d2d0e1c9dab3d5c075de87f53ee0ae99ae08900fcf340dd45c289ba&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-12-08
fetch_date: 2025-10-04T00:53:41.400776
---

# VxWorks固件系统研究

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3q231ibCnXKS6HGU4ia7KRtkJDU2aicPASmUJm5n8G0tDmuvaRGias6gsXZg/0?wx_fmt=jpeg)

# VxWorks固件系统研究

原创

工控安全实验室

山石网科安全技术研究院

本文对真实的VxWorks固件进行分析。首先介绍VxWorks系统，随后从设备固件提取到加载地址和固件格式的分析，并结合VxWorks源码对一些常用函数进行符号恢复。

**0****1**

**Vxworks 概览**

VxWorks是美国风河（WindRiver）公司1983年设计的一款实时操作系统（Real Time Operating System，RTOS），多用于各种嵌入式和IoT设备，也用于工控设备、通信、军事、航空、卫星通讯等高精尖技术。VxWorks操作系统不同于一般的Linux，它自己实现了一套进程通信、任务调度、内存管理和中断机制，通常VxWorks文件系统与内核系统合并到一起编译成一整个固件。

对于VxWorks系统安全性研究，研究难点主要体现在以下几个方面：

1. VxWorks闭源，对其进行编译需要风河公司的商业软件进行编译，无法获取源码和编译参数，资料较少，需要投入大量精力进行逆向分析；

2. 风河公司使用自家编译器，并非GNU提供的发行版gcc，编译逻辑和汇编特征与通常的Linux gcc有所不同；

3. 对于无符号的VxWorks固件函数的精准识别与名称恢复比较困难；

4. 不同厂商不同设备的固件可能是定制化的，不同的固件存在较大差异；

5. VxWorks系统模拟困难，调试困难。

由于这些研究难点的存在，国内外对其研究成果极其少。

**0****2**

**案例分析**

从实际的某路由器设备VxWorks系统进行分析，包含固件提取、固件分析过程研究记录。

**2.1 提取固件**

现有的设备固件提取方法一般有以下几种：

1. 通过UART调试接口获取shell直接进行调试；

2. 热风枪拆下芯片，通过编程器离线读取；

3. 通过导线连接编程器读取固件；

接下来我将描述在尝试这些方式时遇到的一些问题和得出的结论。

**1）通过UART调试接口获取shell**

拆卸设备外壳，在PCB板上找到UART接口后，通过USB-TTL串口进行通信，飞线连接RX、TX、GND，这一步网上有很多教程，这里就不再赘述了。因为不知道波特率是多少，尝试了多个波特率，最后设置为波特率为57600不会发生乱码，得到路由器启动信息如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qR6TsGPeX4KauZOzF26XJMQHuVXsJM4jNEz0DCg5H1d25cs2AIT9vzQ/640?wx_fmt=png)

从以上信息可以看到U-boot在启动时可选择4个选项，但并没有调试相关选项，并且在实际接入过程中，无法发送中断信号中断下来进行选择，所以这个方法无效。对于这种情况有一些猜测：

1. 该系统并不提供调试接口；

2. 是否有一种只有开发人员知道的进入调试的方法。

排除获取调试接口这一选项后，可以通过其他方式对固件进行分析：

1. 改刷U-Boot，优点是可以获取调试shell，缺点是风险大，容易把设备弄坏；

2. 提取设备固件进行分析，优点是风险小，缺点是需要大量逆向工作。

**2）拆下芯片读取**

观察整个PCB板，只存在一个flash芯片，型号为QH16B-104H1P。由于一些设备的原因，并且还是想让这个路由器设备尽量保持原样，所以没有选择拆下芯片，不到万不得已我不考虑这种方法。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qfvxOLexk6vaaicVo71nZ0qichWtxACOVIvby9DhXpbQQKMgibI5IXUQhg/640?wx_fmt=png)

**3）通过导线连接编程器读取固件**

排除上面两种方法后选择通过导线连接编程器读取固件，这种方式风险比较小。我通过芯片上面的标识，用半导小芯APP查询到芯片资料如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qHPOpP27IykpibusMJq7b7FGia1MeWA14FcrsJYRgWqEUPLrhJaS9NxAA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qndlSO1PDGrSjmUZeoG8uvRzT46LrsrQhSzR0gRfzm2hquFFXibiaAUlQ/640?wx_fmt=png)

可以看到这是一个8 Pin 的 NOR Flash存储器，这种flash可以直接在存储器上执行代码，不必把代码读取到RAM中。另外还有一种NAND的Flash，通常这两种flash配合使用。这里有了引脚信息之后开始考虑如何通过飞线读取固件，有两种方式：

1. 通过编程器读取；

2. 通过树莓派读取；

首先尝试了第一种方式，因为我主力机是Mac，没有USB 2.0的接口，这里存在一个问题，编程器不支持USB 3.0，导致无法读出flash数据。然而USB 2.0的转接头不太好买，所以我换了Windows台式机读取。（图中用的这种夹子连接引脚，这里其实我手上是有编程夹的，只是为了试试这个夹子，这种夹子没有整体的那种牢固，容易脱落，还卖得比较贵，可能更适用于其他场景吧）

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qqBDic79b3Kqy06lrQWKFshOU2oHmic9xwQztErpjPHiaJUxIMr0dGPDxQ/640?wx_fmt=png)

在断电状态下，通过编程器读取出来的固件不包含任何的VxWorks信息，binwalk解析如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qgy5LDJibHXkUcBV7VicouJ2f84P1KhbKPGLFbodj4ulCJfkn1YCTvibRg/640?wx_fmt=png)

一般来说在固件系统中应该有一块比其他内容都要大的文件，也就是内核文件，但这里没有。那么这时候就有了一些猜测，断电状态难道没办法读取到系统内核文件吗？是否需要U-Boot启动才能读取到内核文件？

对于这些猜想，我对于通电情况做了一个测试。

这里要注意一下，由于编程夹有8个引脚，接到编程器上难免会接到或者触碰到VCC供电，可能会造成短路引发一些不可预测的后果。为了保险起见，这里通电就不用编程器读取了，换用树莓派来读取固件，不接VCC。当然这种通电读取的方式肯定有一些的风险存在，可能会烧掉树莓派。

树莓派有很多引脚，需要按照以下的标识来接入芯片：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qj5QrndibOLUxSqJjSJuexoUkOIDEEZYWTJ7C3WZKU1s5AnBmhic0Z7kA/640?wx_fmt=png)

对于8 Pin的芯片，接下面的引脚就够了，排除VCC：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qZeSyX70zF1k5JkDciaVM4ickwQl2T8d7icMppKu78CPgud8G6ZJiaZITAw/640?wx_fmt=png)

根据芯片的资料接入：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qQqGSj2I6HMpMS2OozmicbdwFk5CXzL5BnDcbE7tyPlu3kwWhXwibtqqg/640?wx_fmt=png)

通过网线连接树莓派，配置主机与树莓派同一网段，ssh连上树莓派，确定SPI接口后，使用flashrom工具来提取固件。提取过程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qPkTLiaBaUPib1dUWx8Iszk8HXibJIx9mr9RushQVbQsOrEueZ2Yib1wA4w/640?wx_fmt=png)

这一次提取出的固件就包含了VxWorks的内核文件：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qemev3Zn0CUWldMPA7OLpntuPJahWibeTOP4VrO2Rg09ia8BjhmoRwsmg/640?wx_fmt=png)

把第一块大文件提取出来，然后用binwalk解析，就看到了VxWorks系统信息。如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3q2uUn5v6n7f3ibsUyEajeYO1Kkj9AcicysUJbdwh8Bn41xTK3LTNeAfWQ/640?wx_fmt=png)

到这一步就算是把固件系统从设备中提取出来了，接下来对固件进行分析。

**2.2 初步分析**

有了固件之后，先尝试使用 `binwalk -e` 直接提取固件内容。这一步会提取出来非常多的文件，原因是因为binwalk对于这种RTOS，或者是加密的固件系统提取效果并不理想，存在很多杂乱的信息，下图就是一个例子：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3q8hDtMjmicgkafBiaIkV5Leve8l49UN8bLViaibHjicj3picuXPLicFRFicJCcQ/640?wx_fmt=png)

可以从文本中看出来一些HTML标签的特征，暂且认为它是一个HTML文件。但在开头一行解压出来的内容却是一些不可见字符，说明binwalk提取是不够准确的，也可能是固件进行了某种加密。用binwalk查看固件熵值如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qFEKHqdz5PPhL0nicyh0rtIiaQYeadX1qicP9PqdDYX1b8LenZEFtpYKEg/640?wx_fmt=png)

从熵值得知了一些信息，看起来这个固件至少在开头是没有进行加密的，也就是在U-Boot位置是可以分析的，这算是一个入手点，可以通过分析U-Boot加载过程来分析固件系统。中间位置暂时无法判断是经过加密还是压缩过的，需要进一步分析。

在binwalk解析结果的最大的一块内容一般是内核文件：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qlzkHYLg9IR6yC8N2SPk2TuF2EXjZlt3Uo9GAxTLWnldQ2meZDYf2JQ/640?wx_fmt=png)

可以手动剥离这一部分，然后手动lzma解压出来：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qTF2bCVtld92dict7uqzGDL55fD39rwibVIice9tyeyb7B9UkVytRCOApw/640?wx_fmt=png)

解压之后再用binwalk查看，很明显就是一个VxWorks系统了，但遗憾的是并没有发现有相关的符号表信息，可能是一个去符号的固件：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qM73HhEqEHXku9rwMn6EOZxdkhvpmzt4tYXia82V6V4Wuj1xCL6Hn8ibA/640?wx_fmt=png)

binwalk解析出固件为VxWorks 5.5.1 MIPS Little Endian，把这个VxWorks文件放到IDA进行解析，现在并不知道固件加载地址，不需要输入加载地址，因为现在的主要目的还不是逆向它，我们得先搞清楚这个固件是不是有加密导致的binwalk解析不准确。

在初步分析固件的时候，最容易入手的一个点就是查找字符串，然后根据字符串引用找到调用函数。庆幸的是我们找到了如下字符串：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qO4GuD7jPSxhkRr0d9O2UicNbvjhpichuwEGIgBtxTK6Phk5lnXG3CUJQ/640?wx_fmt=png)

很明显这是一些关于请求的字符串，说明这个VxWorks文件并没有其他加密，只是套了一层lzma压缩而已。这里尝试了一下查找字符串引用是不成功的，因为我还没有对加载地址进行分析。另外，尝试了对bzero、usrInit、bfill等VxWorks初始化函数名称进行搜索无果，再次证明这是一个没有任何符号的固件。

通过以上结论，即然所有文件都是lzma文件进行压缩，那么就可以对lzma文件格式进行分析，手动提取出其中的某个lzma文件，然后手动解压看看还有没有乱码的情况。

这里需要知道lzma压缩格式的一些关键知识。lzma文件头前13字节为文件描述，包括魔术字、文件夹大小、未压缩大小，分别占用byte、dword、qword。固件中部分内容如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qMYX3Gx29Gfbjux7CyE9pOXaiao6TBoichubNW42Wj5peaEaxqniaeuHyg/640?wx_fmt=png)

第一、二、三部分组成header，第四部分为压缩的内容content，直到以四个“00”字符结束。第一部分properties由lc、lp、pb通过位运算得到0x5A，用lzmainfo命令可以查看他们的具体值，第二部分为文件夹大小dictionary size。第三部分为未压缩大小uncompressed size。我们以此规律通过十六进制编辑器找到了VxWorks压缩时的起始地址和终止地址，分别为0x15200和0x11c240，总大小为0x107040，跟刚才binwalk解析后我们手动剥离的大小一样。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qhm0h9IjfQQ0vIpRrbELQDUIhSoI98mLkpUghib6ib4qYQnuX7ia7wQm6g/640?wx_fmt=png)

结束位置其实出现了一些偏差，很明显上面有个MINIFS字符串，往上是0xFF填充，往下紧邻另一部分lzma头部信息，那么就不该是这四个“0”字符结束，而是在0xFF填充之前结束，这个其实解析的时候手动修正偏差即可。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qrB5Obgt8OMicNj9wuib6T3IDPibpeU6sesPDXiaqmZoS6n7RicGYfC7XFmw/640?wx_fmt=png)

现在尝试提取出0x11C240开始，结束位置为0x122de4的lzma文件，然后手动解压出来，得到如下内容：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qpPEy70mGccyb0UQa6Z1DhxJrmFqH0aNlK6GTLxE2OqZpgMPrYaSQxA/640?wx_fmt=png)

在开头位置还是有不可见字符，说明不管是我们手动提取还是binwalk解析提取，出来的结果都是相同的。

其实在手动解析lzma的时候，发现了一个比较有意思的事情：在上一部分的lzma内容中，最后的几个字节存储着下一部分lzma的大小，简单理解就是这些lzma文件是连接在一起的。如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qAvNeMicZXbEKq4icm5VtJknDYNG8vM2EW7QhVcSE1jWIR6vKupNGWkUA/640?wx_fmt=png)

上图中，第三处为lzma头部标识，lzma文件从这里开始，0x5A是由lc、lp和pb三个标志位计算得出的。第四处为小端序未压缩大小，它的长度是qword，而第一处是大端序未压缩大小，长度为dword，第一处和第四处的值相同。第二处则表示上一个文件结束，紧接着就是lzma压缩文件的内容。

在分析过程中有一些MINIFS字符串，在固件中全局搜索，发现有四处MINIFS，并且他们之上都是以0xFF进行填充：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qrSxhqZicRIz4VWlnniaiaMBOZWr9iasEVueeqWJp4N4B5bKwOuiabicbsoYQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qg3pXUhm8A3tJYqwortppT89auczP4T8wSVgibsoPsOibvDiaiaduEIDT9Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXNG9X22Dh1Au1QFHdmw3qxpZFGQib8Snl3piagEN7ewwC45HItjQicWIEcrLrkRZRsrCdCm7BALnOw/640?wx_fmt=png)

![](https://mmbiz.qp...