---
title: 西门子PLC固件分析技术研究
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511637&idx=1&sn=7f3677671ebc4c56388848025a066f26&chksm=e89d868ddfea0f9b3271532c7e42aae6ff746c6001efccff8409797b48eedf0f42fd9ba22de4&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-11-20
fetch_date: 2025-10-06T19:18:45.239234
---

# 西门子PLC固件分析技术研究

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtrUqot0SkZIzM8YOXCQ48ZibUEJlic0P7uqxpZWIdK1P7FNkQwBiboRP9g/0?wx_fmt=jpeg)

# 西门子PLC固件分析技术研究

原创

ic3blac4

ChaMd5安全团队

**一.  摘要**

工业控制系统（ICS）在全球的关键基础设施中发挥着至关重要的作用，包括电力、水务、化工、交通以及其他重要工业领域。然而，随着数字化趋势的发展，工业控制系统也成为了潜在的网络攻击目标，面临着日益严重的安全威胁。近些年涌现了层出不穷的网络攻击事件表明工业控制系统正在遭受新的网络攻击手法的威胁，包括但不限于勒索软件、远程访问木马、恶意物理渗透等。攻击瞄准了工业控制系统的独有脆弱性，如设备间通讯的未加密，公网暴露关键资产，以及对实时运行环境的依赖性，这些都使得工控系统在当前的网络攻击环境下风险加剧。

作为工业控制系统的“大脑”，控制器更易受到恶意攻击者的关注，一旦进入生产网络后想要达到更具影响力的攻击效果大多情况下都要对控制器进行篡改逻辑攻击、篡改寄存器值攻击、精准点位攻击或者毁瘫式攻击等手段。因此在攻击发生之前，就控制器的安全性进行研究，将风险点逐一加固或者优化相关设计显得尤为重要。本文尝试以西门子PLC为例，从固件分析角度出发讲解对该方向内容的研究方法和相关技术，并且在阐述过程中配合大量的实操类说明，可以更方便相关研究人员复现实验内容。

**二. 研究现状**

工业控制器的研究可以分为多个方向，包括但不限与控制器硬件架构研究、软件架构研究、通信协议研究、Runtime内核研究、特殊算法及指令研究、操作系统研究、工程文件编译及格式研究等等，针对这些方向再次从实现原理、脆弱性、攻击面、攻击战法、加固方法等维度对每个方向进行详细剖析，通过“矩阵方式”网格化覆盖研究内容才可初步对某一款控制器有所理解和掌握。如下图为矩阵方式研究内容，每个交叉点都为一个细分研究领域。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 实现原理 | 攻击面分析 | 脆弱性分析（漏洞） | 攻击战法 | 加固方法 |
| 硬件架构研究 |  |  |  |  |  |
| 软件架构研究 |  |  |  |  |  |
| 操作系统研究 |  |  |  |  |  |
| 通信协议研究 |  |  |  |  |  |
| Runtime内核研究 |  |  |  |  |  |
| 工程文件编译研究 |  |  |  |  |  |
| 工程文件格式研究 |  |  |  |  |  |
| 特殊算法库研究 |  |  |  |  |  |
| 固件文件分析研究 |  |  |  |  |  |
| ………… |  |  |  |  |  |

目前对于全球流行的工业控制器能够覆盖所有研究方向的文章很少见，最多也是在某一个研究方向上进行详细分析。西门子工业控制器在全球较为流行，因此针对西门子PLC控制器的研究成果也更多，比如对西门子S7CommPlus通信协议的研究从2015年至今从未中断，在BlackHat上出现了《The spear to break the security wall of S7CommPlus》、《Rogue7: Rogue Engineering-Station attacks on S7-Simatic PLCs》等，笔者在BlackHat 2022会议上也针对西门子最新版本的S7CommPlus\_TLS协议做了题为《Fuzzing and Breaking Security Functions of SIMATIC PLCs》的成果分享。

但是在西门子PLC控制器固件文件分析理论和实践相结合的领域中缺乏相关技术研究，本文以西门子小型PLC为研究对象，着眼于固件文件分析研究方向，从固件获取、固件解压、函数识别、实战分析等多个技术角度出发阐述工控安全研究工作中固件文件分析研究的详细过程。

**三. 固件获取**

笔者在KCON 2022议题《解锁工控设备固件提取的各类方法》[1]中已经对S7-1200系列PLC固件获取做了详细的介绍，基本思路是利用CVE-2019-13945漏洞，搭建漏洞利用环境，利用UART特殊访问功能将内存片区dump后从中分离固件。

本文利用另外一种思路，直接从西门子官网下载S7-1200或者S7-200 SAMRT的固件，通过对固件文件分析，直接编写解压缩程序获得可分析的固件文件。S7-1200系列PLC固件下载需要注册授权，详细下载页面如下[2]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtU40DBkArrXbCuSAwwSiaibrV4HS2iaW2VtogYJSCEicMfsVfJewIs0Cz0g/640?wx_fmt=png&from=appmsg)

S7-200 SAMRT固件下载页面如下所示[3]。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOt4s5STdmwI3TfzSgoXQMGw5kTicS6XXxKV0v0YBPhCoiatTWJib8UK6s3g/640?wx_fmt=png&from=appmsg)

随意选择两个系列中的CPU模块下载对应的固件，下载后可以浏览其中的文件结构。我们下载了6ES7\_215-1AG40-0XB0\_V04.06.00的固件，在文件夹中存在S7\_JOB.S7S和FW文件夹。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtyAqCiaW3wGIasR3ic69BvLia8FeTGa2arbzlnmKTuEl5JqccKicxK0Qtrw/640?wx_fmt=png&from=appmsg)

FW文件夹中有一个.upd文件，如下所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtibhHxnJIL73yeNRrScaXNpterFrlgef6vaXsYYONOZpMUI7CiapLbKZQ/640?wx_fmt=png&from=appmsg)

S7-200 SAMRT系列CPU模块固件文件和S7-1200系列类似，不过其中的.upd文件大小明显小于S7-200 SAMRT的固件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOteibbs5eShS0OcLAl9jErFzxVZHPxlL1pbZmz2VJqBicJ9ibeLN6mMUgKg/640?wx_fmt=png&from=appmsg)

四. 固件文件格式分析

任意选取一个upd文件解读其文件格式，固件由3大块组成，第一块为固件头信息，说明了固件的基本信息：固件组成部分（红色框体），固件版本号（黄色框体），固件名称（绿色框体）,总共0X2C字节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtqvKL9aZKZ054RjBTr4AkrqcKw9kdEBhtJibYNusRsQmibrT6OQ2iaR13w/640?wx_fmt=png&from=appmsg)

第二块为固件目录信息，展示了固件的数据名称、大小、校验内容。具体格式为4字节size+4字节CRC32校验字段+6字节名称字段，如下所示红色框体内为第一个固件数据部分的大小0x20，黄色框体为CRC32校验，绿色字体为名称BG\_ABL；紧接着白色框体为第二部分的大小0xeb5372,蓝色框体为CRC32校验，绿色字体为名称A00000,同理可得出还有另外2部分内容，名称分别为B00000，FW\_SIG。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtKfRGtpib6Q0pmbGeX6ELfQ9pNJmDseCVn2h6zx3lHtNtblSqkiaQibJ6w/640?wx_fmt=png&from=appmsg)

第三块为固件数据部分，展示了每个部分固件的详细数据，其中由每个部分的6字节名称开头。比如第一部分BG\_ABL的数据如下所示，红色框体为固件部分名称，黄色框体内为具体数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtDPiazF7JS3u8SPfukIzX1xcwxz88gL6p9SbG01EboVxbMaon87dMLmg/640?wx_fmt=png&from=appmsg)

接下来的很大部分为A00000详细数据，如下所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtvnCqTGrOpmt7zkYWjtyWSRL6o7K2jbq5aY0gmjqF0fDtu9RzStuShg/640?wx_fmt=png&from=appmsg)

经过查阅相关资料得到该部分采用了LZP3压缩算法，经过查阅资料找到了LZP3压缩算法的C代码实现，测试后发现该C代码仅适用于S7-1200固件，经过笔者修改已经支持了西门子S7-200 SMART固件。由于C代码适用性灵活性不高，因此我们利用python语言重写该部分代码，并且做成了方便易用的小工具，如下图所示，在以后的研究中可以对S7-1200和S7-200 SAMRT系列新发布的固件（只要该压缩算法不改变）进行快速解压缩，以执行后续的相关分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtq0ILtEqLBqBQMS0tKc9xpkqCFVXhowIYoH6kyNLRnau6H7Wwdg706w/640?wx_fmt=png&from=appmsg)

解压缩后的固件文件中有明显完整的明文信息，如下所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOt1QiaeNibnmt4iapquNicXoyZRE5zJWUrrw72FyVrsQicyLN8cYONiceIxS4w/640?wx_fmt=png&from=appmsg)

**五. 固件初步分析**

本文中我们以S7-200 SAMRT系列SR20控制器模块固件版本V2.7.0为例做分析示例。

1.使用binwalk分析SR20-V270.BIN文件，查看文件构成。如下所示，可知文件中有gzip压缩文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOticIEPaGLDQrAymTJWjMiaYNR6sVbMmrNvOX9ktKteibVM4AsDA0CqNTMg/640?wx_fmt=png&from=appmsg)

    全部解压缩后查看0x380208后续的几个压缩文件内容，其中包含有web功能相关的配置文件，如下所示为0x380208开始解压缩文件的内容，其中包含了web读取内容的地址映射关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOt8IXeMIvRJMpibH3MZXaKj6yvC7Sa9ibU444zHMESRWqeDzyfnTbSDytQ/640?wx_fmt=png&from=appmsg)

由于存在诸多gzip文件，因此会在后续的IDA分析中存在多段识别不是很优雅的数据段，我们在分析过程中需要注意该问题。

2.导入IDA进行分析

首先需要确定架构，利用binwalk –A，如下所示显示未ARM 大端。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtWicib6JGbszImyzFl561pP1ykVSZQSKX3ZYnAEkpjlegWl8xqvibADbmw/640?wx_fmt=png&from=appmsg)

获知处理器架构后还需要确定加载基地址，导入IDA后我们先使用默认的0地址加载，加载完成后先做头部分析，得知从0x40后为ARM的中断向量入口，该部分数据可不作为分析部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtDtRlx3Dq7ybHwnibykqYD7ROfvNg7tAacGjWHCo3vN5TECUQDhQtgibQ/640?wx_fmt=png&from=appmsg)

那么就可以利用rbasefind工具寻找加载基地址再减去0x40得到真正的加载基地址，利用rbasefind工具，如下所示显示加载基地址为0x00038000

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtXVwBVfO95pPEwqqyGGdvdxtVyYZuulawpY5lyxpqcd3mCTnxKE6jBg/640?wx_fmt=png&from=appmsg)

根据上述思路算得加载基地址为0x00037FC0,此时在IDA中修改加载基地址为0x00037FC0

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtS9kOrbKMTh5gxsUYHxBLhzftdGibWEl43PusMxNObGnTHricWuluLqCw/640?wx_fmt=png&from=appmsg)

基于以上步骤IDA分析完成后可以识别大部分函数，但是还有部分未被识别，只有9045个函数，并且很多的函数没有被创建。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtkeobXvP5gwfuMjpUoup6md73VpRibjRGibXL0CuJibWJ0rQgtZeujhibJw/640?wx_fmt=png&from=appmsg)

经过分析大部分未被识别的函数都是以“PUSH”字符打头，因此我们利用python脚本来解决push部分没有被创建为新函数，脚本如下。注意此处我们识别到gzip压缩文件的前半部分，不涉及后边的web相关内容。

|  |
| --- |
| import idaapi  import idautils     staradd=0x38000  offset=0x308208     for addr in range(staradd, staradd+offset):      if idc.print\_insn\_mnem(addr) == 'PUSH':          idaapi.add\_func(addr) |

执行完脚本后分析出的函数增加了许多达到了10082个，如下所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOt4sOia4xIVxesN9ZZ92rGxKeQ2V8uxbxSs4LITY39wxKicfxXia8nicYKTw/640?wx_fmt=png&from=appmsg)

随后又发现新的问题，还是有固件数据没有被识别代码部分，如下所示需要手动按C才能转化为代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtI6dUicg74AFsTSBK1bnOpicRstia2nKhjgmwNzQb0vG5UPgF5VAsC2fiag/640?wx_fmt=png&from=appmsg)

按照同样的思路我们编写脚本来处理未能被识别为代码的部分。

|  |
| --- |
| import idaapi  import idautils     staradd=0x38000  offset=0x308208     for addr in range(staradd, staradd+offset):      # 如果当前字节是数据      if ida\_bytes.is\_unknown(ida\_bytes.get\_flags(addr)):          # 将当前字节转换为代码          idc.create\_insn(addr) |

执行完成后识别的函数进一步增多，且未被识别为代码段的部分已经被识别为PUSH函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtsGHccIFlyKQBpaChasEQJvJuuud3XWTV8nrTxLAysCEddVcTeyFv3w/640?wx_fmt=png&from=appmsg)

执行完此步骤后还需再次创建刚才被识别出的函数，同样用脚本处理即可，经过处理后的完整结果如下，此时识别出的函数已达到12439个。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRHoHDeLvm4VXeK0MnIsIOtqChuXVY6tp8iaPTVnLic0XuKtJ1iaS8MabV5ULzxJqlOyOT6ZRaBumRFg/640?wx_fmt=png&from=appmsg)

通过以上几个步骤处理后识别的函数越来越多，函数越多对后续的分析越有利，但是还存在以下问题：

A. 未能识别出不以“PUSH”打头的函数；

B. 误将部分数据段强制转换成了代码段；

C. 没有分析web部分的引用或者代码；

但是抓住主要矛盾，在详细分析过程中再次解决上述问题，毕竟现在识别到的函数已经不少了。由于之前分析过S7-1200系列PLC的固件，相较于S...