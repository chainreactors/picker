---
title: APT 10利用自定义后门LODEINFO向日本各类机构发起攻击
url: https://buaq.net/go-135313.html
source: unSafe.sh - 不安全
date: 2022-11-13
fetch_date: 2025-10-03T22:36:15.451992
---

# APT 10利用自定义后门LODEINFO向日本各类机构发起攻击

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/304ac72d5f5dce0cea7ba5f5304fb66f.jpg)

APT 10利用自定义后门LODEINFO向日本各类机构发起攻击

导语：本文将介绍新的感染方法的技术分析，如SFX文件和DOWNIISSA以及我们的发现。之后将介绍LODEINFO后门的技术分析，以及每个版本的后门的相关shellcode。
*2022-11-12 12:0:0
Author: [www.4hou.com(查看原文)](/jump-135313.htm)
阅读量:34
收藏*

---

导语：本文将介绍新的感染方法的技术分析，如SFX文件和DOWNIISSA以及我们的发现。之后将介绍LODEINFO后门的技术分析，以及每个版本的后门的相关shellcode。

![abstract_digital_japan-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150565104746.jpeg "1667998445134688.jpeg")

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150567107455.png "1667998453193205.png")

日本可能是LODEINFO的主要目标

此后，研究人员继续追踪LODEINFO。JPCERT/CC和Macnica Networks都报道过其迭代版本。卡巴斯基研究人员还在2021 HITCON会议上分享了新发现，涵盖2019年至2020年的LODEINFO活动。

在2022年3月，卡巴斯基研究人员观察到一个Microsoft Word文件被用作一些攻击的感染媒介。同年6月，针对日本政府或相关机构的SFX文件被发现，文件中使用了日本著名政治家的名字，并使用了含有日本内容的诱饵文件。还观察到一个名为DOWNIISSA的新的下载程序shellcode，用于部署LODEINFO后门。

接下来，我们将首先介绍新的感染方法的技术分析，如SFX文件和DOWNIISSA以及我们的发现。之后将介绍LODEINFO后门的技术分析，以及每个版本的后门的相关shellcode。

**初始感染：VBA + DLL侧加载**

在对2022年3月的攻击进行调查期间，我们发现了一封带有恶意附件的鱼叉式钓鱼电子邮件，其中安装了恶意软件持久性模块，该模块由合法的EXE文件和通过DLL侧加载技术加载的恶意DLL文件组成。例如，以下部分描述了一个上传到Virustotal的恶意Microsoft Word文件(MD5: da20ff8988198063b56680833c298113)。一旦目标打开恶意文档文件，就会显示一条日语消息：根据您的网络安全设置，单击上面黄色文档栏上的“启用编辑”和“启用内容”以打开该文件。诱饵受害者点击“启用内容”并启用嵌入式宏。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150568522213.png "1667998466494769.png")

欺骗目标点击“启用内容”并嵌入VBA代码日文信息

嵌入的VBA代码创建文件夹C:\Users\Public\TMWJPA\，并在同一文件夹中释放一个名为GFIUFR.zip (MD5: 89bd9cf51f8e01bc3b6ec025ed5775fc)的压缩文件。GFIUFR.zip包含两个文件：NRTOLF.exe和K7SysMn1.dll。NRTOLF.exe (MD5: 7f7d8c9c1b6735807aefb0841b78f389)是一个数字签名的合法EXE文件，来自K7Security Suite软件，用于DLL侧加载。K7SysMn1.dll (MD5: cb2fcd4fd44a7b98af37c6542b198f8d)是NRTOLF.exe附带加载的恶意DLL。恶意DLL文件包含LODEINFO shellcode的加载程序。这个DLL是一个已知的LODEINFO加载程序模块。它包含一个由0.5.9版本内部识别的单字节XOR加密LODEINFO外壳代码。在我们调查的前几次攻击中，攻击者也使用了这种感染方法。

除此之外，我们还发现了另外两个与LODEINFO相关的植入程序。

**初始感染2：SFX + DLL侧加载**

其中一个植入程序是RAR格式的自解压存档(SFX)文件(MD5 76cdb7fe189845a0bc243969dba4e7a3)，该文件也上传到了Virustotal。类似地，归档文件包含三个文件，分别为1.docx、K7SysMn1.dll和K7SysMon.exe，其中包含如下所示的自解压脚本命令。恶意软件开发者还添加了一条用日语写的评论，可以翻译为“以下评论包含一个自解压脚本命令”:

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150569209113.png "1667998475175976.png")

当目标用户执行这个SFX文件时，归档文件将其他文件放置到%temp% dir，并将1.docx作为一个仅包含几个日语单词的诱饵打开，如下图截图所示。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150569967966.png "1667998600702043.png")

来自1.docx的简单诱饵文档内容

在向用户显示一个诱饵文件时，归档脚本启动K7SysMon.exe，它通过DLL侧加载从K7SysMn1.dll (MD5: a8220a76c2fe3f505a7561c3adba5d4a)加载恶意DLL。k7sysmm1 .dll包含一个BLOB，其中有一个模糊的例程，在过去的活动中没有观察到。嵌入式BLOB被划分为4字节块，每个部分存储在DLL二进制文件的50个随机命名的导出函数中的一个中。这些导出函数在分配的缓冲区中重构BLOB，然后使用一个单字节的XOR键解码LODEINFO shellcode。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150574977030.png "1667998585161030.png")

重新组装有效负载BLOB

最终由该植入程序部署的负载是LODEINFO v0.6.3。

**初始感染3：SFX + DLL侧加载+额外的BLOB文件**

我们还发现了另一个类似的SFX文件，名为＜masked＞的sns电影的传播请求。攻击者利用了一位著名日本政治家的名字。嵌入的自解压脚本和文件与本文的初始感染2部分中讨论的前一个示例非常相似。但是，这个示例包含一个名为K7SysMon.Exe.db的附加文件。以前观察到的加载程序模块在可执行文件中嵌入了一个带有加密shellcode的BLOB，但是在这个示例K7SysMn1.dll中不包含BLOB。相反，加载程序模块读取K7SysMon.Exe.db文件作为加密的BLOB，并解密shellcode，这是LODEINFO v0.6.3后门。SFX文件的标题和文件的内容都是要求在SNS(社交网络服务)上传播这位著名政治家的视频的内容。根据最后的归档时间戳，我们认为该SFX文件是在2022年6月29日通过鱼叉式网络钓鱼邮件传播的。从文件名称和诱饵文件来看，目标是日本执政党或相关机构。

2022年7月4日，另一个SFX文件(MD5 edc27b958c36b3af5ebc3f775ce0bcc7)被发现。存档文件、有效载荷和C2地址与前面的示例集非常相似。唯一明显的区别是这份诱饵文件的日文标题：投保申请。我们认为这个SFX文件可能被用来针对日本媒体公司。

**初始感染4：VBA +未发现的下载程序shellcode downniissa**

早在2020年8月，我们发现了一个名为DOWNJPIT的无文件下载程序shellcode，这是LODEINFO恶意软件的一个变体，并在HITCON 2021上就其进行了演示。2022年6月，我们发现了另一个无文件下载程序shellcode，它由一个有密码保护的Microsoft Word文件提供。文件名为增强日美同盟的威慑力和应对能力.doc。该文档文件包含的恶意宏代码与之前调查的样本完全不同。打开后，该文档文件显示一条日文消息，以启用以下VBA代码。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150575464628.png "1667998572190640.png")

2022年6月发现MS Word文件中的恶意VBA代码

与过去的示例(如本文初始感染1中描述的示例)不同的是，恶意VBA宏被用来释放DLL侧加载技术的不同组件，在这种情况下，恶意宏代码直接在WINWORD.exe进程的内存中注入并加载嵌入的shellcode。这个植入程序在过去的活动中是不存在的，shellcode也是LODEINFO v0.6.5的一个新发现的多级下载程序shellcode。

这个下载程序的shellcode完全不同于DOWNJPIT的变体。新的下载程序shellcode里面有两个URL：

```
http://172.104.112[.]218/11554.htm
```

我们将这个新的下载程序命名为DOWNIISSA，其中IISSA是url中找到的文件名中的11554派生的字符串。下图显示了从恶意文档文件到DOWNIISSA下载的最终有效负载的复杂感染流程。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150576921145.png "1667998558487875.png")

通过DOWNIISSA的LODEINFO感染过程

如上所述，嵌入式宏生成DOWNIISSA shellcode并将其注入到当前进程(WINWORD.exe)中。主要的下载程序代码是base64编码的，并放在DOWNIISSA shellcode的开头，由shellcode本身进行解码和修补。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150579636891.png "1667998549175848.png")

DOWNIISSA base64解码和自修复

在它被解码后，一些重要的字符串被发现是用一个字节的异或加密。例如，两个C2目的地址用以下代码解密。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150580584907.png "1667998539193867.png")

DOWNIISSA shellcode主函数中嵌入的异或C2目的地

DOWNIISSA使用URLDownloadToFileA() API函数从URL地址下载BLOB，并将其释放在%TEMP%/${TEMP}.tmp。然后，它将文件读入当前进程中分配的内存中，并立即释放下载的临时文件。我们确认了这两个URL都提供了相同的二进制数据，该数据与存储在BLOB本身末尾的一字节XOR键进行了XOR。异或解密后，发现LODEINFO后门shellcode v0.6.5。在感染的最后阶段，DOWNIISSA创建一个msiexec.exe实例，并在进程的内存中注入LODEINFO后门shellcode。

这个涉及DOWNIISSA shellcode的新感染流在之前使用LODEINFO的活动中没有出现过，这是2022年的一个新的TTP。

除了在这个示例中找到的11554.htm文件，我们还发现了其他名称的文件，如3390.htm, 5246.htm和16412.htm，在2022年7月托管在相同的C2服务器上。3390.htm (MD5: 0fcf90fe2f5165286814ab858d6d4f2a)和11554.htm (MD5: f7de43a56bbb271f045851b77656d6bd)是通过downniissa恶意软件下载的单字节异或lodeinfo v0.6.5 shellcode。每个示例的XOR键都在文件末尾找到。5246.htm (MD5: 6780d9241ad4d8de6e78d936fbf5a922)和16412.htm (MD5: 15b80c5e86b8fd08440fe1a9ca9706c9)文件是单字节异或唯一数据结构。5246.htm文件中的数据结构如下所示：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150580592745.png "1667998528144206.png")

该数据结构包含三个文件的名称:K7SysMon.exe, K7SysMn1.dll (MD5: c5bdf14982543b71fb419df3b43fbf07)和K7SysMon.exe.db (MD5: c9d724c2c5ae9653045396deaf7e3417)。这表明一个未被发现的下载程序模块从C2下载5246.htm，以协助在受害者的设备上安装一些嵌入式文件。

LODEINFO首次发现于2019年，LODEINFO及其感染方法不断更新和改进，成为针对日本组织的更复杂的网络间谍工具。LODEINFO植入程序和加载程序模块也不断更新，以规避安全产品，并使安全研究人员的手动分析复杂化。

**LODEINFO后门shellcode的演变**

如上所述，我们已经介绍了初始感染方法在不同的攻击场景中有所不同，并且LODEINFO shellcode定期更新以用于每个感染媒介。接下来，我们将介绍2022年LODEINFO后门shellcode的改进。

卡巴斯基分别在3月、4月和6月调查了LODEINFO shellcode的新版本，即v0.5.9、v0.6.2、v0.6.3和v0.6.5。下图显示了该恶意软件自发现以来的演变时间线。

![2.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150582207480.png "1667998616145988.png")

LODEINFO发布时间表

**LODEINFO v0.5.6：使用古老的加密算法对C2通信进行多重加密**

这个从加载程序模块中提取的LODEINFO v0.5.6 shellcode演示了针对某些安全产品的几种增强规避技术，以及开发人员实现的三个新的后门命令。

在感染目标计算机之后，LODEINFO后门信标将计算机信息发送到C2，例如当前时间、ANSI代码页(ACP)标识符、MAC地址和主机名。信标还包含一个硬编码密钥(NV4HDOeOVyL)，后来被古老的Vigenere密码所使用。此外，随机生成的垃圾数据被附加到数据的末尾，可能是为了逃避基于包大小的信标检测。

![2.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150583119906.png "1667998629205637.png")

在LODEINFO v0.5.6中增加了Vigenere密码密钥和随机生成的垃圾数据

2021年12月，我们发现了LODEINFO v0.5.8，并进行了轻微修改，在Vigenere密码密钥后面添加了LODEINFO植入版本号。

用于发送数据的加密函数也被修改了，使其更加复杂。正如在前面的变体中观察到的，它取要发送的数据的SHA512哈希值的前48个字节。然后，它使用一个等于运行时间的四字节XOR键XOR数据，并在数据之前进行预处理。发送的前16个字节来自另一个SHA512哈希值，这一次来自前面提到的硬编码AES密钥(NV4HDOeOVyL)。它在base64编码的有效负载的末尾加密11个字节(用从“=”到“.”替换的填充)，以动态生成第二个Vigenere密码密钥和最终生成数据的变量。Vigenere密码使用第二个密钥加密base64编码的标头(url-safe替换了从“=”到“.”的填充)。

![2.3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150585409963.png "1667998636213943.png")

C2通信中的加密算法和数据流

最后，通过上面描述的复杂步骤，使用第二个密钥、加密标头和有效负载生成要发送到C2的数据。最终的数据包结构如下：

![2.4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221111/1668150586152191.png "1667998646946526.png")

LODEINFO v0.5.6：用于后门命令标识符的2字节异或混淆

这次更新包括修改的加密算法和后门命令标识符，这些标识符在以前的LODEINFO shellcode中定义为四字节硬编码值。LODEINFO v0.5.6后门命令标识符被一个双字节的异或操作混淆了。在比较...