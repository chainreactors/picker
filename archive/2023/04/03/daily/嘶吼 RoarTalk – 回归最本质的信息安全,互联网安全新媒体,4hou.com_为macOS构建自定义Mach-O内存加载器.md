---
title: 为macOS构建自定义Mach-O内存加载器
url: https://www.4hou.com/posts/034v
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-03
fetch_date: 2025-10-04T11:30:25.464314
---

# 为macOS构建自定义Mach-O内存加载器

为macOS构建自定义Mach-O内存加载器 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 为macOS构建自定义Mach-O内存加载器

luochicun
[技术](https://www.4hou.com/category/technology)
2023-04-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)98709

收藏

导语：这篇文章将重点介绍MacOS Ventura的AARCH64版本和针对MacOS 12.0及更高版本的XCode。

在上一篇文章中，我们介绍了如何修复dyld以恢复内存执行。这种方法的优点之一是，我们将加载Mach-O二进制文件的许多复杂工作委托给macOS。但如果我们在不使用dyld的情况下，创建我们自己的加载器呢？所有这些字节映射是如何工作的？

接下来，我们将介绍如何在不使用dyld的情况下在MacOS Ventura中为Mach-O包构建内存加载器，以及Mach-O文件的组成，dyld如何处理加载命令以将区域映射到内存中。

为了配合苹果向ARM架构的迁移，这篇文章将重点介绍MacOS Ventura的AARCH64版本和针对MacOS 12.0及更高版本的XCode。

**什么是Mach-O文件？**

首先介绍一下Mach-O文件的架构，建议先阅读一下Aidan Steele的Mach-O文件格式参考。

当我们在处理ARM版本的MacOS时，会假设正在查看的Mach-O没有被封装在Universal 2格式中，因此在文件开头我们首先会遇到的是Mach\_header\_64：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680234113267.png "1678680234113267.png")

要构造加载器，我们需要检查以下几个字段：

magic-此字段应包含MH\_magic\_64的值；

Cputype-对于M1，应为CPU\_TYPE\_ARM64。

filetype -我们将检查这篇文章的MH\_BUNDLE类型，但加载不同类型也应该很容易。

如果Mach-O是正常的，我们可以立即处理mach\_header\_64结构体后面的load命令。

**加载命令**

顾名思义，load命令是一种数据结构，用于指示dyld如何加载Mach-O区域。

每个load命令由load\_command结构表示：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680243217553.png "1678680243217553.png")

cmd字段最终决定load\_command实际表示的内容，以LC\_UUID的一个非常简单的load\_command为例，该命令用于将UUID与二进制数据关联起来。其结构如下：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680251200882.png "1678680251200882.png")

如上所述，这与load\_command结构重叠，这就是为什么我们有匹配字段的原因。以下就是我们将看到的各种负载命令所支持的情况。

**Mach-O段**

加载Mach-O时，我们要处理的第一个load\_command是LC\_SEGMENT\_64。

segment命令告诉dyld如何将Mach-O的一个区域映射到虚拟内存中，它应该有多大，应该有什么样的保护，以及文件的内容在哪里。让我们来看看它的结构：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680261178263.png "1678680261178263.png")

出于本文的目的，我们将关注：

segname -段的名称，例如\_\_TEXT；

vmaddr -应该加载段的虚拟地址。例如，如果它被设置为0x4000，那么我们将在分配的内存基数+ 0x4000处加载段；

vmsize -要分配的虚拟内存的大小；

fileoff -从文件开始到应复制到虚拟内存的Mach-O内容的偏移量；

filesize -要从文件中复制的字节数；

maxprot-应分配给虚拟内存区域的最大内存保护值；

initprot -应分配给虚拟内存区域的初始内存保护；

nsects -遵循此段结构的节数。

要注意，虽然dyld依赖mmap将Mach-O的片段拉入内存，但如果我们的初始进程是作为一个加固进程执行的(并且没有com.apple.security.cs. c . data . data之类的文件)。使用mmap是不可能的，除非我们提供的bundle是使用与代理应用程序相同的开发人员证书进行签名的。此外，我们正在尝试构建一个内存加载器，因此在这种情况下从磁盘拉二进制文件没有多大意义。

为了解决这个问题，在此POC中，我们将预先分配我们的blob内存并复制它，例如：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680272469525.png "1678680272469525.png")

与之前的dyld文章一样，我们需要在主机二进制文件中使用正确的授权来允许无符号可执行内存。

**节**

从上面的字段中可以看到，段加载命令中存在另一个引用，这就是一个节（section）。

由于节位于段中，虽然它将继承其内存保护，但它有自己的大小和要加载的文件内容。每个段的数据结构附加到segment命令中，其结构为：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680281210792.png "1678680281210792.png")

同样，我们将只关注其中几个字段，这些字段对于我们构建加载器的直接目的很有帮助：

sectname -节的名称，例如\_\_text；

segname -与此节关联的段的名称；

addr -用于此节的虚拟地址偏移量；

size -文件中(以及虚拟内存中的)节的大小；

offset - Mach-O文件中部分内容的偏移量；

flags - flags可以分配给一个节，这个节帮助确定reserved1,reserved2和reserved3中的值。

由于我们已经分配了每个段，所以加载器将遍历每个段描述符，确保将正确的文件内容复制到虚拟内存中。需要注意的是，在复制时可能需要更新内存保护。MacOS for ARM不允许读/写/执行内存页(除非com.apple.security.cs. c。allow-jit授权与MAP\_JIT一起使用)，因此我们需要在复制时适应这一点：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680292957044.png "1678680292957044.png")

**符号**

随着我们的加载器开始成型，接下来需要看看如何处理符号（Symbol）。符号在Mach-O二进制文件的加载过程中扮演着重要的角色，它将名称和序数关联到内存区域，以供我们稍后参考。

符号是通过LC\_SYMTAB的加载命令来处理的，如下所示：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680301813021.png "1678680301813021.png")

同样，我们将关注构建加载器所需的字段：

symoff -从文件开始到包含每个符号信息的nlist结构数组的偏移量；

nsyms -符号(或nlist结构)的数量；

stroff -符号查找所使用的字符串的文件偏移量。

显然，接下来我们需要知道nlist是什么：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680309168557.png "1678680309168557.png")

此结构为我们提供了有关命名符号的信息：

n\_strx -从符号字符串字段到该符号字符串的偏移量；

n\_value -包含符号的值，例如地址。

因为我们稍后需要引用符号，所以我们的加载器需要存储这些信息以备以后使用：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680318175845.png "1678680318175845.png")

**dylib’s**

接下来是LC\_LOAD\_DYLIB加载命令，该命令引用在运行时加载的额外dylib’s。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680328134058.png "1678680328134058.png")

我们需要的项在dylib结构成员中找到，特别是dylib.name.offset，它是从这个加载命令的开头到包含要加载的dylib的字符串的偏移量。

稍后，当涉及到重定位时，我们将需要这些信息，其中dylib’s的导入顺序起着重要作用，因此我们将构建一个dylib’s数组，供以后使用：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680337198096.png "1678680337198096.png")

**迁移**

现在就要介绍Mach-O更复杂的部分——迁移。

Mach-O是用XCode构建的，目标是macOS 12.0和更高版本，使用LC\_DYLD\_CHAINED\_FIXUPS的加载命令。关于这一切是如何工作的，没有太多的文档，但Noah Martin对iOS 15查找链的研究值得参考，我们还可以在这里找到苹果XNU repo中使用的结构体的详细信息。

Dyld’s的源代码告诉我们，该加载命令以结构linkedit\_data\_command开始：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680347184220.png "1678680347184220.png")

使用dataoff便能找到标头：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680356126778.png "1678680356126778.png")

我们需要做的第一件事是收集所有导入并构造一个稍后将引用的有序数组。为此，我们将使用以下字段：

symbols\_offset -从该结构开始到导入所使用的符号字符串的偏移量；

imports\_count -导入项的数量；

imports\_format -任何导入符号的格式。

imports\_offset -从该结构开始到导入表的偏移量。

每个导入项的数据结构都依赖于imports\_format字段，但通常我看到的是DYLD\_CHAINED\_IMPORT格式：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680369147354.png "1678680369147354.png")

可以看出这是一个32位数组项，有lib\_ordinal字段，它是我们之前从LC\_LOAD\_DYLIB加载命令构建的有序dylib数组的索引。索引从1开始，而不是0，这意味着第一个索引是1，然后是2……

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680409770488.png "1678680409770488.png")

如果索引值为0或253，则该项引用this-image(当前正在执行的二进制文件)。这就是我们之前构造符号字典的原因，因为现在我们可以简单地将自己二进制文件中引用的符号名称解析为其地址：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680421201315.png "1678680421201315.png")

name\_offset是从dyld\_chained\_fixups\_header收集的symbols\_offset字符串的偏移量。

使用这些信息，我们需要构建一个有序的导入数组，因为我们需要马上引用这个有序数组。

构建了一个导入列表后，将开始链式启动，这可以从dyld\_chained\_fixups\_header结构的starts\_offset标头字段中找到。

链式启动的结构是:

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680432104723.png "1678680432104723.png")

为了导航，我们需要遍历seg\_info\_offset中的每个项，这为我们提供了指向dyld\_chained\_starts\_in\_segment的指针列表：

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680446601364.png "1678680446601364.png")

首先要注意这个结构，有时segment\_offset是0，但不知道为什么，看起来dyld也识别了这个，只是忽略了它们。

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230313/1678680484577269.png "1678680484577269.png")

我们需要找到每个reloc链的开始位置的字段如下：

pointer\_format-链使用的DYLD\_CHAINED\_PTR\_结构的类型；

segment\_offset-段起始地址在内存中的绝对偏移量；

page\_count-page\_start成员数组中的页数；

page\_start-从页面到链开始的偏移量。

当我们在一个段中有一个有效的偏移量时，我们可以开始遵循reloc链。遍历每个项，我们需要检查第一位，以确定该项是一个rebase(设置为0)还是一个bind(设置为1)：

在rebase的情况下，将该项转换为dyld\_chained\_ptr\_64\_rebase，并使用...