---
title: Dridex 扩大攻击范围，冒充正常邮件攻击macOS平台
url: https://www.4hou.com/posts/r7Op
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-04
fetch_date: 2025-10-04T05:39:52.728440
---

# Dridex 扩大攻击范围，冒充正常邮件攻击macOS平台

Dridex 扩大攻击范围，冒充正常邮件攻击macOS平台 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Dridex 扩大攻击范围，冒充正常邮件攻击macOS平台

gejigeji
[新闻](https://www.4hou.com/category/news)
2023-02-03 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)138483

收藏

导语：趋势科技研究人员发现了一个Dridex变体以MacOS平台为目标，攻击者使用一种新的技术将嵌入恶意宏的文档传递给用户。

趋势科技研究人员发现了一个Dridex变体以MacOS平台为目标，攻击者使用一种新的技术将嵌入恶意宏的文档传递给用户。

通常情况下，包含恶意宏的文档会伪装成正常文档通过电子邮件附件进入用户的系统。这是目前进入系统的主要方法，但攻击者还有其他方法进入受害者的系统。

本文主要说的是Dridex，它是目前全球活跃且技术比较先进的木马之一，又被称为BUGAT和Cridex，主要目的是从受感染设备的用户那里窃取网上银行和系统信息，进行欺诈性交易，原来Dridex的目标用户是Windows用户。本文分析的这个变种已经将MacOS平台作为攻击目标了，攻击者不是伪装成发票或其他业务相关文档，而是采用了一种新的技术，向用户提供嵌入了恶意宏的文档。

**基本信息**

研究人员发现的Dridex样本以Mach-o可执行文件:a.o out(趋势科技人员将其命名为Trojan.MacOS.DRIDEX.MANP)的形式到达。在Virus Total (VT)中首次提交这个文档的时间是2019年，当时它被安全厂商标记为恶意，没有具体的检测名称。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071661257134.png "1673071661257134.png")

包含文档头、加载命令和段的Mach-o区域

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071681859987.png "1673071681859987.png")

从2019年4月到2022年12月对a.out的检测情况

**分段安装**

**(a) \_\_DATA\_\_data段**

样本的数据段包含了恶意的嵌入式文档，并被\_payload\_doc变量使用。下图中的反汇编显示，该恶意软件执行了一个循环，\_payload\_doc的内容被复制，直到计数器达到\_payload\_doc\_len，即恶意代码的大小。 这是为覆盖程序做准备。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071714182977.png "1673071714182977.png")

对\_\_DATA\_\_data段的反汇编

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071736200015.png "1673071736200015.png")

反汇编样本将数据写入目标文档的过程

**(b) \_\_DATA\_cstring段**

一旦恶意代码准备就绪，cstring段就会在将代码覆盖到目标文档中发挥作用。此段包含以下bash脚本命令。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071753112385.png "1673071753112385.png")

首先，恶意软件使用find ~ -name "\*.doc "命令搜索当前用户（~/User/{user name}）目录中使用.doc文档扩展名的文档。 然后，它使用for循环遍历每个文件（i），然后通过echo '%s'命令（其中%s是数据段的恶意代码）写入恶意代码。

在脚本中添加xxd -r -p意味着恶意代码将以纯十六进制转储形式写入，而不是实际内容。脚本中的>$i部分意味着输出的内容将被打印在每个文件上。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071768176219.png "1673071768176219.png")

对\_\_DATA\_\_cstring段的反汇编

下图的反汇编显示了将写入文档的%s值，它所覆盖的恶意代码有一个D0CF文档格式的签名，这意味着它是一个微软的文件。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071894151751.png "1673071894151751.png")

显示搜索和覆盖命令样本的反汇编

**嵌入文档的分析**

以下恶意嵌入式文档于2015年首次在野外被发现，其包含的信息如下：

SHA256: 70c7bf63bfe1fb83420905db6e65946d721e171db219034a52b27116795ae53e；

文件名：pmB3A6.doc；

检测名称：W2KM\_DRIDEX.SPB；

使用oletools，一个用于分析OLE和微软文档的python包，研究人员观察到受影响的.doc文件现在包含宏。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071908981321.png "1673071908981321.png")

显示此文档文件包含宏的文本提示符

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071923210016.png "1673071923210016.png")

使用oletools提取的被覆盖的.doc文件中包含的宏

根据提取的宏，该.doc文件包含可疑的组件。 为了详细说明，下面是被覆盖的文档中的VBA组件。

ThisDocument是一个包含autoopen宏的对象，该宏调用恶意函数。这些函数使用普通的名称来伪装成常规函数。例如，CreatePicture和CreateColor通常用于创建与图像相关的对象，但在这个VBA项目中，它们执行恶意任务。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071940463845.png "1673071940463845.png")

来自autoopen宏的代码片断

Module1在临时(TEMP)文件夹中创建一个可执行文件，然后运行它。该恶意软件使用字符串连接作为混淆其创建的可执行文件的名称的方法。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071958347679.png "1673071958347679.png")

Module1的代码片段，显示了恶意软件如何创建和执行可执行文件

Module2包含一个例程，它解密一组字符串(URL)，然后连接到它，使用GET命令检索文件。恶意软件使用基本的字符串加密来隐藏它连接到的恶意URL。它调用RuBik()函数来执行解密例程。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071973379099.png "1673071973379099.png")

Module2的代码片段显示了连接到加密URL的解密程序

Module3将在Module2中检索到的文件的内容写入在Module1中创建的可执行文件。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673071988844927.png "1673071988844927.png")

Module3中的代码片段显示恶意软件写入可执行文件的位置

**相关的URL和释放的文件**

在本节中，我们将分析恶意软件释放的有效载荷。注意，因为它是一个exe文件，所以它不会在MacOS环境中运行。有可能我们分析的变种仍处于测试阶段，还没有完全转换到基于macos的设备上。

当打开文档并启用宏时，恶意软件会连接到Module2中解密的URL，使用GET命令检索文件(87i4g3d2d2.exe):

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673072003602491.png "1673072003602491.png")

虽然Microsoft Word中的宏功能默认禁用，但恶意软件将覆盖当前用户的所有文档文件，包括干净的文件。这使得用户更难以确定文件是否恶意，因为它不是来自外部源。

在连接到域之后，可移植的可执行文件（PE）的内容被写入trume1.exe（aa6873a6002e152669f54c80801ca7d500ee8c00d5a6a8c223203303b1cbaf50），正如Module1、2和3中分析的那样，然后将执行trume1.exe文件。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673072020146222.png "1673072020146222.png")

分析样本中的网络活动，显示了它所连接的URL的详细信息

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673072036683532.png "1673072036683532.png")

打开启用宏的文档时样本的有效载荷

被释放的可执行文件的内容是HTML格式，而不是PE文档格式，因为它试图访问的URL已经被关闭。它试图下载的PE文档是Dridex加载器。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673072277618184.png "1673072277618184.png")

由恶意软件释放的可执行文件的内容

**总结**

Dridex不是一个新的恶意软件，它已经在野外出现了好几年了。尽管它已经出现很久了，但它仍在被继续使用，并且多年来甚至出现了许多技术接待。它进入用户系统的途径原来是通过电子邮件附件，但本文的研究表明，使用Dridex的攻击者也在努力寻找新的目标和更有效的攻击方法。

目前，这个Dridex变体对MacOS用户的影响已经降到最低，因为有效载荷是一个exe文件(因此不兼容MacOS环境)。然而，它仍然覆盖文档文件，这些文件现在是Dridex恶意宏的载体。此外，这一变体背后的攻击者可能会实施进一步的修改，使其与MacOS兼容。

建议用户不要点击链接或打开电子邮件中的附件和嵌入式文档，以避免被使用社会工程和恶意文档的攻击所感染。

本文翻译自：https://www.trendmicro.com/en\_us/research/23/a/-dridex-targets-macos-using-new-entry-method.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?A1oFLFJl)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/FpAB1n2wt6I0zw18n_Sz-3Nj9Ctg)

# [gejigeji](https://www.4hou.com/member/mqy0)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/mqy0)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)...