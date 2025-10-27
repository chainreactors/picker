---
title: 数据恢复(七)-PDF文件结构分析
url: https://zgao.top/%e6%95%b0%e6%8d%ae%e6%81%a2%e5%a4%8d%e4%b8%83-pdf%e6%96%87%e4%bb%b6%e7%bb%93%e6%9e%84%e5%88%86%e6%9e%90/
source: Zgao's blog
date: 2023-02-17
fetch_date: 2025-10-04T06:50:36.840743
---

# 数据恢复(七)-PDF文件结构分析

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 数据恢复(七)-PDF文件结构分析

* [首页](https://zgao.top)
* [数据恢复(七)-PDF文件结构分析](https://zgao.top:443/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E4%B8%83-pdf%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84%E5%88%86%E6%9E%90/)

[2月 16, 2023](https://zgao.top/2023/02/)

### 数据恢复(七)-PDF文件结构分析

作者 [Zgao](https://zgao.top/author/zgao/)
在[[数据恢复](https://zgao.top/category/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D/)](https://zgao.top/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E4%B8%83-pdf%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84%E5%88%86%E6%9E%90/)

PDF（Portable Document Format）文件是一种用于文档传输和显示的文件格式，也是结构性的文件。通过本文的分析，可以清楚PDF的文件结构和对象寻址原理，对于PDF的文件修复思路也能有自己的见解。

![](https://zgao.top/wp-content/uploads/2023/02/image-35-1024x106.png)

文章目录

[ ]

* [PDF文件结构](#PDF%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84 "PDF文件结构")
* [PDF文件读取过程分析](#PDF%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E8%BF%87%E7%A8%8B%E5%88%86%E6%9E%90 "PDF文件读取过程分析")
* [PDF内容详解](#PDF%E5%86%85%E5%AE%B9%E8%AF%A6%E8%A7%A3 "PDF内容详解")
  + [PDF文件头](#PDF%E6%96%87%E4%BB%B6%E5%A4%B4 "PDF文件头")
  + [PDF对象obj](#PDF%E5%AF%B9%E8%B1%A1obj "PDF对象obj")
  + [PDF交叉引用表xref](#PDF%E4%BA%A4%E5%8F%89%E5%BC%95%E7%94%A8%E8%A1%A8xref "PDF交叉引用表xref")
  + [PDF文件尾trailer](#PDF%E6%96%87%E4%BB%B6%E5%B0%BEtrailer "PDF文件尾trailer")
* [总结](#%E6%80%BB%E7%BB%93 "总结")

## PDF文件结构

PDF文件的结构主要包括以下4个部分：

1. 文件头：
   PDF文件的开头包含一个文件头，它标识了文件的类型和版本信息。
2. 对象：
   PDF文件中的所有内容都被表示为对象，这些对象可以是文本、图像、矢量图形等。每个对象都有一个唯一的编号，以及一些描述该对象的信息。
3. 交叉引用表(xref)：
   PDF文件通常包含一个交叉引用表，它记录了PDF文件中所有对象的位置和编号。这些对象包括页面、字体、图片等。
4. 文件尾(trailer)：
   包括文件大小、根对象的编号等信息。startxref 指向交叉引用表的位置，文件结束符 “%%EOF”。

## PDF文件读取过程分析

PDF阅读器读取渲染显示PDF文件，有如下过程。

![](https://zgao.top/wp-content/uploads/2023/02/image-35-1024x106.png)

## PDF内容详解

### PDF文件头

PDF文件的开头所包含的几个字节，用于标识这个文件的类型和版本。PDF文件头的格式是：%PDF-1.x，其中x代表版本号。

![](https://zgao.top/wp-content/uploads/2023/02/image-36-1024x339.png)

上图是“%PDF-1.0”，说明该文件是一个PDF版本1.0的文档。

### PDF对象obj

![](https://zgao.top/wp-content/uploads/2023/02/image-37-1024x431.png)

对象obj是pdf文件的主体内容。上面选中的部分是第一个完整的obj，注意obj开头的偏移地址为21。

```
1 0 obj
<<
/Length 44
>>
stream
q
595.80 0 0 842.40 0.00 0.00 cm
/Im33 Do
Q

endstream
endobj
```

对上图中所有的obj各个字段进行解释。

1. `1 0 obj` – 对象编号及版本号
2. `<< >>` – 对象属性字典的开始和结束标记
3. `/Length 44` – 图像数据的长度，单位为字节
4. `stream` – 图像数据流的开始标记
5. `q` – 图形状态保存命令，保存当前的图形状态，方便后续恢复
6. `/Im33 Do` – 在当前位置插入名称为”Im33″的图像资源
7. `Q` – 图形状态还原命令，恢复之前保存的图形状态
8. `endstream` – 图像数据流的结束标记
9. `endobj` – 对象定义的结束标记

### PDF交叉引用表xref

交叉引用表xref位于文件尾部，所有obj结束后就是xref。注意xref的偏移地址为7990754。可以搜索xref快速定位交叉引用表的位置。

![](https://zgao.top/wp-content/uploads/2023/02/image-38-1024x464.png)

```
xref
0 1
0000000000 65535 f
1 1
0000000021 00000 n
2 1
0000000118 00000 n
```

每个字段的含义解释：

1. `xref` – 交叉引用表的开始标记
2. `0` – 第一个对象的编号
3. `1` – 对象的数量
4. `0000000000 65535 f` – 第一个对象的描述，其中：
   * `0000000000` – 第一个对象在文件中的偏移量
   * `65535` – 对象的生成号，因为此处是”f”，所以表示这个对象是一个自由对象（free object），即已被删除的对象，可以被其他新对象重复使用
5. `1 1` – 第二个对象的编号和数量
6. `0000000021 00000 n` – 第二个对象的描述，其中：
   * `0000000021` – 第二个对象在文件中的偏移量
   * `00000` – 对象的生成号
   * `n` – 表示这个对象是一个普通对象（normal object），即当前被使用的对象
7. 后面的依次同上

所以上面的0 1表示的是删除对象，1 1实际对应PDF中的第一个obj，其偏移地址就是对应的之前第一个obj的地址，为21。这样pdf解析工具就能正常寻址找到文件中所有obj的对象了。

### PDF文件尾trailer

PDF文件尾trailer位于文件的末尾，在交叉引用表xref的后面。包含了PDF文件中的对象位置信息和文件总体描述信息，是解析和渲染PDF文件的必要信息。

![](https://zgao.top/wp-content/uploads/2023/02/image-39-1024x294.png)

这里startxref就是对应上面的7990754。

```
trailer
<<
/Root 74 0 R
/Size 84
>>
startxref
7990754
%%EOF
```

对trailer每个字段含义的解释：

1. `trailer` – 文件总体描述信息的开始标记
2. `<< >>` – 文件总体描述信息的属性字典，其中包含：
   * `/Root 74 0 R` – 根对象的引用，其中`74 0 R`表示该对象在文件中的编号为74，第二个数字0表示该对象在交叉引用表中的位置
   * `/Size 84` – PDF文件中的对象数量，包括自由对象和普通对象
3. `startxref` – 交叉引用表的起始位置标记
4. `7990754` – 交叉引用表在文件中的偏移量，即从文件的开头到交叉引用表的位置的字节数
5. `%%EOF` – 文件结束标记，表示PDF文件正式结束

## 总结

从分析结果来看，PDF是非常结构化的文件。搞清楚了PDF文件对象的寻址原理甚至可以自己写一个PDF解析工具，这样对任何文件系统的结构原理理解也会更加深刻。

Post Views: 902

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 目前为止有一条评论

###### https://www.causes.com/users/fastlotosite 发布于9:15 下午 - 5月 9, 2023

Thanks for the info, it will help me make the right decision.

[回复](https://zgao.top/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E4%B8%83-pdf%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84%E5%88%86%E6%9E%90/?replytocom=5289#respond)

### 发表评论 [取消回复](/%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D%E4%B8%83-pdf%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84%E5%88%86%E6%9E%90/#respond)

Δ

版权©2020 Author By : Zgao