---
title: 探究窃密木马FormBook免杀手段——多变的加载器
url: https://mp.weixin.qq.com/s?__biz=MzI3NjYzMDM1Mg==&mid=2247519879&idx=1&sn=064a0b33b31d2615c9a49dc32b81c1f2&chksm=eb7050b8dc07d9aee365ea288b52a0d369a03ac728711d57e6f9df24b913e2bf77c6b8f58b12&scene=58&subscene=0#rd
source: 火绒安全
date: 2024-09-13
fetch_date: 2025-10-06T18:28:29.996430
---

# 探究窃密木马FormBook免杀手段——多变的加载器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0icdicRft8tz53quORD8wyw3glQISQ0A4gV5CsKdcB316LmCZyaIjzpxPaGphppurSeCmHw9SdGls9am8uRreakw/0?wx_fmt=jpeg)

# 探究窃密木马FormBook免杀手段——多变的加载器

原创

火绒安全

火绒安全

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4nrnOI1emtFr0UYnrLKytAvy2gia6ZuIUJs14h2pEIwpiaWPCTTuCQIDibx9dlfXoyrNyVEWb8DVUUA/640?wx_fmt=gif&from=appmsg)

近期，火绒工程师在日常关注安全动态时发现FormBook木马家族存在利用多种加载器混淆处理进行免杀的行为，因此火绒工程师对其木马家族多种样本进行横向分析，分析发现该木马家族多个样本的主要功能几乎没有变化，只有加载器不断变化，且加载器核心机制仍然由读取、解密和注入三个步骤组成。其中注入的FormBook代码通过自修改代码（SMC）和多次注入以及通过天堂之门实现免杀。火绒安全产品可对上述窃密木马进行拦截查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4ga1ZeoLpArWac6EU0ibroDhIAWKEqnoUYZnvDKdydSuP3xmx3W2ONMtg/640?wx_fmt=png&from=appmsg)

火绒6.0查杀图

FormBook是一种商业窃密木马，主要用于窃取浏览器的Cookies等敏感信息。同时，它还包含一个后门模块，能够下载并执行代码，因此也被认为是一种多功能木马。该木马最早于2016年在Hack Forums平台上公开售卖。当时，它并不是以窃密木马的名义售卖，而是宣称其用途是监控员工或儿童的浏览行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gsGriblteRQu1DtC1byN5m2SdL6UfanoTUN8bMkJZvzBibF6MC6EJH26A/640?wx_fmt=png&from=appmsg)

FormBook售卖帖子

一年后，FormBook的作者发布了一款C#加密器，虽然其代码相对简单，但如今出现的各种C#加载器中都能看到这段加密器代码的影子。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gG7XpqSqY8a1ATY6vvGByOr7ibq8wgZp5Wgrq7ibEV7sByuRic6a4UzNmA/640?wx_fmt=png&from=appmsg)

FormBook C#加密器帖子

FormBook攻击流程基本相同，下图是最新FormBook木马攻击流程图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gwyKd8DpoArbvstayypQysQDp12icX7x9NXbKq92XUaVgTXzkyEUnYfw/640?wx_fmt=png&from=appmsg)FormBook流程图

**一**

**样本分析**

**加载器**

加载器是用于加载FormBook代码的程序。通常情况下，受害者打开的文件就是加载器，加载器随后会解密出代码执行恶意操作。

FormBook的加载器有多种形式，包括AutoIt、C#、NSIS和C等。它们的目的都是一样的：解密出FormBook木马并将其注入到某个程序中执行。不同之处在于每种加载器的解密、注入次数、方法，以及所使用的混淆技术存在差异。

### **AutoIt加载器**

最近的FormBook木马最外层使用的是AutoIt脚本编译出的可执行程序，通常包含一个解密器和一个被加密的FormBook木马文件。以下是反编译得出来的原始脚本内容，因略微混淆过，所以比较复杂。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4goYta3tu06kCHW29jvpdhpPSP2sbYb94iajvtRlPxeict2gaA9fz5TdUw/640?wx_fmt=png&from=appmsg)

AutoIt脚本

对代码进行部分还原后，可以看到此代码先读取meshummad文件，然后对其文件数据进行解密，并使用VirtualAlloc分配一个可读、可写且可执行的内存块，将解密后的内容复制到该内存块中，最后调用内存地址0x23b0处的代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4g1tmibx5u8kibs3FkGgjQ71J7Xww54fRciaGlPvwD0RiaURYRAjczDk6Rug/640?wx_fmt=png&from=appmsg)

AutoIt还原后代码

0x23b0处的代码会先读取spiketop文件，然后对其文件数据进行解密并将解密后的数据注入到目标进程中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gzOlD0X82hicWrkJaDXQJoP7qx8cep1h48XPPck5KR3f83ziaoVaW8yGg/640?wx_fmt=png&from=appmsg)

spiketop解密注入

创建目标进程svchost.exe时，使用CREATE\_SUSPENDED属性，使进程在启动时立即挂起。随后，通过创建共享内存块，将进程的入口点修改为FormBook木马的代码入口点。![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gZBAHvYuBUtvRNnjRNzibNfmY6W8hFRx72ia5f4BlIRes2og0YBN8JpGg/640?wx_fmt=png&from=appmsg)

注入代码

**C#加载器**

大部分C#加载器的代码结构都如图所示，核心逻辑通常都嵌入在窗体初始化的代码中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gTM2yQzLEoV1G9TgavCklIhPNo1pjFgcHnwPuHAATDiafJbhxsEpR2AQ/640?wx_fmt=png&from=appmsg)

入口点

通过获取资源数据并对其进行异或运算解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gE26E7D0bRXObeaibU0iamJlcibO9YzW6CKCCIXJ8ZvQuNCvmzODu37vDQ/640?wx_fmt=png&from=appmsg)

获取资源并解密

加载解密后的代码，并调用其中的某个方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gQicJBcaYcutr2GLsDxAoGhcIpe1OVIUMUu1d8K6AkTSrRO6xbEhf5Og/640?wx_fmt=png&from=appmsg)

加载后调用方法

其方法中包含Sleep函数，先睡眠十秒，之后会从Cinema.Properties.Resources中获取whRP资源并对该资源数据进行解密。解密是通过调用该资源中的另一个方法实现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gicicvlgKic0xyLkFePgDSXnnVFPdjqwxVG80bcxFKC2GBRzM39vwkSuxw/640?wx_fmt=png&from=appmsg)

获取资源并解密

解密后加载代码并调用其中的方法，即注入相关代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gkjoicUA5Ff7TzpZoOLADupkLUnGstrJ7nicQBjaR3Qxen0CqL1HpIlpA/640?wx_fmt=png&from=appmsg)

加载后调用方法

在注入之前，会获取注入所需函数的地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gPeFOicxSBPM4RrN15Ty6UiaSllhh6P68cTOtnMMrPmibABeVdNoAo62EA/640?wx_fmt=png&from=appmsg)

获取函数地址

获取资源，该资源就是被加密的FormBook木马数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4g8q0e2dGohmic8LvvVG1ThCIyelK4Riax443zhGhYLWbCtEibmE2BSewAw/640?wx_fmt=png&from=appmsg)

获取资源

通过异或算法解密资源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gAx0LwpWPiaJLzElCtFGicLMEibgTuKH38cAEu6vxqcMDpOZibVibuxw6iaLg/640?wx_fmt=png&from=appmsg)

异或解密

最后再次创建该进程，将FormBook注入该进程中，执行FormBook代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4g625mLmmSuoCS5R8VN0icaebsBAop7H7dpOicEHXCfRbsUibcfdO9FrnHg/640?wx_fmt=png&from=appmsg)

创建进程并注入

**NSIS加载器**

NSIS加载器也有不少，从下方NSIS脚本中可以看出，其会释放三个文件，并执行其中一个名为rvoplhkaevivic的文件中的代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gRWQfo7zyvwknK53NP7VGich2FUfQ4eRyyiaKnPGapj3XXn4Kcoux2J9Q/640?wx_fmt=png&from=appmsg)

读取执行

读取文件df4h5cv6nhh38o8mk08，解密后执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gtVl2QicDFiaPZIg5DZl3W0FUAW0pm3lhQV043rTPgfCaAWa4aNqA8Qicw/640?wx_fmt=png&from=appmsg)

解密执行

执行的代码与前述的AutoIt加载器中的解密后注入手段一样，最终注入的就是FormBook木马。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gLf9MG8NekIq859LjodKHJ8g60X2y4qyDcUDhqFNlfHnGg0vsPibcPhA/640?wx_fmt=png&from=appmsg)

注入

还有一些方法是释放三个文件，执行mbvbvnxc.exe程序，并传入uelcqq参数。该程序会对uelcqq文件进行解密后执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gy9vZY0l58Dtic4mToQzRrNUSibGJy4HusiaAQKwHV64MPibHAVbPKOu0ng/640?wx_fmt=png&from=appmsg)

释放执行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gYqr6aibAMUDg8efE3N1lM40STHhPxYib4icbs30BamhoiaFX7hKZQguyWw/640?wx_fmt=png&from=appmsg)

读取文件解密执行

其中有些NSIS脚本中的部分字符串经过了混淆处理，图示的脚本是对部分字符串做了替换处理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gAV6LCw00ULgqnRobNxvosiaicmgSlAEWdZRROC3H4s34CMr5BOwrPnRA/640?wx_fmt=png&from=appmsg)

NSIS脚本

### **C加载器**

C加载器是在很早之前就出现过的，一般会在第二层加载器中出现。

图示方法是在WndProc函数中解密某块数据，然后分配执行权限并执行。最终执行的就是FormBook木马。这种方法是最简单的加密手段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gAwN60eKgI6aDHo4CIiaTJbLtajOyNnTKic8joA0JAyFVNicCyjqEWYQXw/640?wx_fmt=png&from=appmsg)

简单加密

除了上述简单的加密手段，还有一些比较复杂的变体。该方法通常涉及多轮解密和大量无意义的计算，最终都会调用FormBook代码。这种类型的木马最近较为常见，通常具有自我修改代码的特性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4guNyreWmdm1JZicE0f20BhfLLJ0qDx1zDpKBEFBiaISTTRQM2EMrJzCicg/640?wx_fmt=png&from=appmsg)

复杂加密

**窃密模块**

通过加载器加载出FormBook代码后，就会开始执行恶意操作，如窃密和后门操作。

在进入窃密和后门模块之前，会经过一段网络检测阶段。该阶段的代码通过随机选择并注入到该进程的兄弟进程中来实现网络检测。过程中会判断目标进程是否在Wow64环境下运行。如果是，则直接进行注入；如果不是，则通过执行x64位代码的方式来注入网络检测代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gWTBEUTSk0OsceHTk8O3UBueGnNFKArpm3I7k3aXn2wjsMnTDhJ05Yg/640?wx_fmt=png&from=appmsg)

选择进程后注入网络检测代码

被注入的进程会直接执行以下操作：发送窗口标题和剪切板等信息到远程服务器。如果网络连接正常，则会继续进行下一步的窃密操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gF0c87GjYmiaUyFb5o08HVclBHQ39jiaHpbsQCU5clPsh6wVPAcMC30wA/640?wx_fmt=png&from=appmsg)

网络检测代码

其中获取剪贴板记录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gmFVLrs9yhNpvqA9A5ZGz94z1Kfb5eMMlI1gxFMYIyGBkw8zFYJ0m9w/640?wx_fmt=png&from=appmsg)

剪贴板记录

检测网络正常后正式开始执行窃密操作，其中窃取的信息主要是浏览器、邮箱、凭据等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gNDf3OtEn82Yo1cqL6HabnJIvRricmb87ib9m0VNAX9zNEYR62aMTqVSw/640?wx_fmt=png&from=appmsg)

窃密操作

****后门模块****

尽管FormBook的主要功能是窃取敏感数据，但它还具有后门功能，包括：下载并执行文件、清除残留痕迹、以及控制计算机的重启和关机等操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gn4cN3UuhpTHiaLiaTIxR6icEq6S5CqNL3iaU8O59A9mT88qWlmjgdNJc9g/640?wx_fmt=png&from=appmsg)

后门操作

**其他各种对抗技巧**

FormBook自历史版本以来就使用多种技术手段进行对抗，包括“地狱之门”、“天空之门”、动态获取函数地址、反调试、反虚拟机、反沙盒等。后来，它又引入了SMC（自修改代码）技术，进一步增强了其对抗能力。

地狱之门：读取ntdll.dll文件，将数据复制到分配的内存中，然后通过遍历函数名并计算Hash值的方式来获取函数地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz53quORD8wyw3glQISQ0A4gy9iaeRqdOMghW5ZequPV83vRAibYyE9nYkib37licLyh0BlbJIrFic6Al2w/640?wx_fmt=png&from=appmsg)

地狱之门

由于需要手动调用系统调用，因此需要将...