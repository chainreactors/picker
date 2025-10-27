---
title: Dridex 扩大攻击范围，冒充正常邮件攻击macOS平台
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247556983&idx=2&sn=1702c2663d16aa3ac112c877fd8700ea&chksm=e915cf4dde62465bb30a2ab3d1220d6960924f8363eb00047d6ab16c835527c6d7471fdec1bc&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-02-04
fetch_date: 2025-10-04T05:43:36.022116
---

# Dridex 扩大攻击范围，冒充正常邮件攻击macOS平台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VwC7PK34uZcxX7x73nNWtqxqDGoYV7xg8ZfwDVAicZ6vtl8MWbvm4wLl0pkSABXSPUkLAoxbADhg/0?wx_fmt=jpeg)

# Dridex 扩大攻击范围，冒充正常邮件攻击macOS平台

gejigeji

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

趋势科技研究人员发现了一个Dridex变体以MacOS平台为目标，攻击者使用一种新的技术将嵌入恶意宏的文档传递给用户。

通常情况下，包含恶意宏的文档会伪装成正常文档通过电子邮件附件进入用户的系统。这是目前进入系统的主要方法，但攻击者还有其他方法进入受害者的系统。

本文主要说的是Dridex，它是目前全球活跃且技术比较先进的木马之一，又被称为BUGAT和Cridex，主要目的是从受感染设备的用户那里窃取网上银行和系统信息，进行欺诈性交易，原来Dridex的目标用户是Windows用户。本文分析的这个变种已经将MacOS平台作为攻击目标了，攻击者不是伪装成发票或其他业务相关文档，而是采用了一种新的技术，向用户提供嵌入了恶意宏的文档。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtpNN3lj8X7X8TTIAOokkeClI4bpHibHqX1MPjQURxgTpLMYPxK7JTWGA/640?wx_fmt=png)
   基本信息

研究人员发现的Dridex样本以Mach-o可执行文件:a.o out(趋势科技人员将其命名为Trojan.MacOS.DRIDEX.MANP)的形式到达。在Virus Total (VT)中首次提交这个文档的时间是2019年，当时它被安全厂商标记为恶意，没有具体的检测名称。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtjQAfXh8G6K3fxuiaibEybu2jD6trD0paxYDeV8N42xMO9X3jzhs96ZMg/640?wx_fmt=png)

包含文档头、加载命令和段的Mach-o区域

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWt0KwrP0JtDXc5gMKV0LGJU9W6xoKDKyTdUaugKk1yicJ38ogvBHYLc6Q/640?wx_fmt=png)

从2019年4月到2022年12月对a.out的检测情况

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtpNN3lj8X7X8TTIAOokkeClI4bpHibHqX1MPjQURxgTpLMYPxK7JTWGA/640?wx_fmt=png)
   分段安装

**(a) \_\_DATA\_\_data段**

样本的数据段包含了恶意的嵌入式文档，并被\_payload\_doc变量使用。下图中的反汇编显示，该恶意软件执行了一个循环，\_payload\_doc的内容被复制，直到计数器达到\_payload\_doc\_len，即恶意代码的大小。这是为覆盖程序做准备。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtngVfE0gTWXdVfC3cBE8t7d5PicJ5cxEkakd2z0qibmTPxfJNF8AMZ94g/640?wx_fmt=png)

对\_\_DATA\_\_data段的反汇编

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtqibOsB3fK3V1hl8OB5OXIgSzsdicJpMY9n0KRBficQqRvw3o8EUS4Kc1w/640?wx_fmt=png)

反汇编样本将数据写入目标文档的过程

**(b) \_\_DATA\_cstring段**

一旦恶意代码准备就绪，cstring段就会在将代码覆盖到目标文档中发挥作用。此段包含以下bash脚本命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWt0wRC6sIefB1rbJkItuCnD5Vyo7R5CBPF9dMJlVn13smVust7qjoMhA/640?wx_fmt=png)

首先，恶意软件使用find ~ -name "\*.doc "命令搜索当前用户（~/User/{user name}）目录中使用.doc文档扩展名的文档。然后，它使用for循环遍历每个文件（i），然后通过echo '%s'命令（其中%s是数据段的恶意代码）写入恶意代码。

在脚本中添加xxd -r -p意味着恶意代码将以纯十六进制转储形式写入，而不是实际内容。脚本中的>$i部分意味着输出的内容将被打印在每个文件上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWt34mkt8icJQSaxW3WSqpsbJ1dDQxrCvxNRwqLtuibSSKkib3d5EdGpZTHw/640?wx_fmt=png)

对\_\_DATA\_\_cstring段的反汇编

下图的反汇编显示了将写入文档的%s值，它所覆盖的恶意代码有一个D0CF文档格式的签名，这意味着它是一个微软的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtFJC1bJJhqjtxQ2cxYjUaRic8ibO1VsvxU7nYEWzFfBPpY4zGCxGiackww/640?wx_fmt=png)

显示搜索和覆盖命令样本的反汇编

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtpNN3lj8X7X8TTIAOokkeClI4bpHibHqX1MPjQURxgTpLMYPxK7JTWGA/640?wx_fmt=png)
   嵌入文档的分析

以下恶意嵌入式文档于2015年首次在野外被发现，其包含的信息如下：

SHA256: 70c7bf63bfe1fb83420905db6e65946d721e171db219034a52b27116795ae53e；

文件名：pmB3A6.doc；

检测名称：W2KM\_DRIDEX.SPB；

使用oletools，一个用于分析OLE和微软文档的python包，研究人员观察到受影响的.doc文件现在包含宏。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtDicDNgwxFvjsAmPfOicvDia0ZFUOqo6xQztl53uOZ8m2XVhmibhaDwwsIg/640?wx_fmt=png)

显示此文档文件包含宏的文本提示符

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtq1SP08aib8hfUB2YTx8Mw9zYgQzoUbqib4icJ4nUfYB3qovnicddCca2qQ/640?wx_fmt=png)

使用oletools提取的被覆盖的.doc文件中包含的宏

根据提取的宏，该.doc文件包含可疑的组件。为了详细说明，下面是被覆盖的文档中的VBA组件。

ThisDocument是一个包含autoopen宏的对象，该宏调用恶意函数。这些函数使用普通的名称来伪装成常规函数。例如，CreatePicture和CreateColor通常用于创建与图像相关的对象，但在这个VBA项目中，它们执行恶意任务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtZSias1Uz65Ix6QNe3lEshu3HHgykjdm03IHbk3WOxpoE4poxOT9sOdA/640?wx_fmt=png)

来自autoopen宏的代码片断

Module1在临时(TEMP)文件夹中创建一个可执行文件，然后运行它。该恶意软件使用字符串连接作为混淆其创建的可执行文件的名称的方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtY8bN6nTkAJjP6h2ZM1R3YxpPdBk0HEibavTNcxzXc9bWicCxepJ4eSgw/640?wx_fmt=png)

Module1的代码片段，显示了恶意软件如何创建和执行可执行文件

Module2包含一个例程，它解密一组字符串(URL)，然后连接到它，使用GET命令检索文件。恶意软件使用基本的字符串加密来隐藏它连接到的恶意URL。它调用RuBik()函数来执行解密例程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtic4WwNy9ykzUZkqiav7zexqaDlqI3TMvUfY9lU8icibR5lHdmZqUjDA5FA/640?wx_fmt=png)

Module2的代码片段显示了连接到加密URL的解密程序

Module3将在Module2中检索到的文件的内容写入在Module1中创建的可执行文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtjuKHWEPTbD0pjCGibcW0u1U8kFyuSrLreGRt9XPPAxjicl0XBqmKu4Kw/640?wx_fmt=png)

Module3中的代码片段显示恶意软件写入可执行文件的位置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtpNN3lj8X7X8TTIAOokkeClI4bpHibHqX1MPjQURxgTpLMYPxK7JTWGA/640?wx_fmt=png)
   相关的URL和释放的文件

在本节中，我们将分析恶意软件释放的有效载荷。注意，因为它是一个exe文件，所以它不会在MacOS环境中运行。有可能我们分析的变种仍处于测试阶段，还没有完全转换到基于macos的设备上。

当打开文档并启用宏时，恶意软件会连接到Module2中解密的URL，使用GET命令检索文件(87i4g3d2d2.exe):

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtpKA1aZ5tR5RejPH3bfiblibJcOMXRmB08SXuJwibCnykel0ZpwzvRbjvA/640?wx_fmt=png)

虽然Microsoft Word中的宏功能默认禁用，但恶意软件将覆盖当前用户的所有文档文件，包括干净的文件。这使得用户更难以确定文件是否恶意，因为它不是来自外部源。

在连接到域之后，可移植的可执行文件（PE）的内容被写入trume1.exe（aa6873a6002e152669f54c80801ca7d500ee8c00d5a6a8c223203303b1cbaf50），正如Module1、2和3中分析的那样，然后将执行trume1.exe文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtWY00TWTNy6mqBSiaSmKia8k5BcRmws6mtCPTmMpyffnsvE1icZz5qH3Ew/640?wx_fmt=png)

分析样本中的网络活动，显示了它所连接的URL的详细信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtice7F5zjCU7cPBxAg5ibzLVG4IzD5WLlhpGpvJSbajgFw0IRYlqR8lcA/640?wx_fmt=png)

打开启用宏的文档时样本的有效载荷

被释放的可执行文件的内容是HTML格式，而不是PE文档格式，因为它试图访问的URL已经被关闭。它试图下载的PE文档是Dridex加载器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtcFU3CuCn06gxfp7dabhu8GXFeSr2kvvulPYoSf6LLBGibKMicH966oxA/640?wx_fmt=png)

由恶意软件释放的可执行文件的内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWtpNN3lj8X7X8TTIAOokkeClI4bpHibHqX1MPjQURxgTpLMYPxK7JTWGA/640?wx_fmt=png)
   总结

Dridex不是一个新的恶意软件，它已经在野外出现了好几年了。尽管它已经出现很久了，但它仍在被继续使用，并且多年来甚至出现了许多技术接待。它进入用户系统的途径原来是通过电子邮件附件，但本文的研究表明，使用Dridex的攻击者也在努力寻找新的目标和更有效的攻击方法。

目前，这个Dridex变体对MacOS用户的影响已经降到最低，因为有效载荷是一个exe文件(因此不兼容MacOS环境)。然而，它仍然覆盖文档文件，这些文件现在是Dridex恶意宏的载体。此外，这一变体背后的攻击者可能会实施进一步的修改，使其与MacOS兼容。

建议用户不要点击链接或打开电子邮件中的附件和嵌入式文档，以避免被使用社会工程和恶意文档的攻击所感染。

参考及来源：https://www.trendmicro.com/en\_us/research/23/a/-dridex-targets-macos-using-new-entry-method.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VwC7PK34uZcxX7x73nNWt6SJZ5Leicu7MlwB6vmapQaZWiaibbFYibJBmKkhTY2jR81fWLO0P0Y23EQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icEjy5ZrpCcgr4BicXicPv08DSsrgibDcJQpvwkZoO4OqdIpJNhj6TO5xV0ic0AnVf7f2kcPnNevQlTtQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过