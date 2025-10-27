---
title: 浅谈JspWebshell之编码
url: https://y4tacker.github.io/2022/11/27/year/2022/11/%E6%B5%85%E8%B0%88JspWebshell%E4%B9%8B%E7%BC%96%E7%A0%81/
source: Y4tacker's Blog
date: 2022-11-28
fetch_date: 2025-10-03T23:54:43.192797
---

# 浅谈JspWebshell之编码

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. 浅谈JspWebshell之编码](#%E6%B5%85%E8%B0%88JspWebshell%E4%B9%8B%E7%BC%96%E7%A0%81)
   1. [1.1. 写在前面](#%E5%86%99%E5%9C%A8%E5%89%8D%E9%9D%A2)
   2. [1.2. 环境相关及其他说明](#%E7%8E%AF%E5%A2%83%E7%9B%B8%E5%85%B3%E5%8F%8A%E5%85%B6%E4%BB%96%E8%AF%B4%E6%98%8E)
   3. [1.3. 正文](#%E6%AD%A3%E6%96%87)
      1. [1.3.1. 关于xml格式的一些简单说明](#%E5%85%B3%E4%BA%8Exml%E6%A0%BC%E5%BC%8F%E7%9A%84%E4%B8%80%E4%BA%9B%E7%AE%80%E5%8D%95%E8%AF%B4%E6%98%8E)
         1. [1.3.1.1. xml声明](#xml%E5%A3%B0%E6%98%8E)
         2. [1.3.1.2. 如何识别我们的文件内容是xml格式](#%E5%A6%82%E4%BD%95%E8%AF%86%E5%88%AB%E6%88%91%E4%BB%AC%E7%9A%84%E6%96%87%E4%BB%B6%E5%86%85%E5%AE%B9%E6%98%AFxml%E6%A0%BC%E5%BC%8F)
      2. [1.3.2. 如何决定一个文件的编码](#%E5%A6%82%E4%BD%95%E5%86%B3%E5%AE%9A%E4%B8%80%E4%B8%AA%E6%96%87%E4%BB%B6%E7%9A%84%E7%BC%96%E7%A0%81)
         1. [1.3.2.1. 如何从字节顺序标记(BOM)判断文本内容编码](#%E5%A6%82%E4%BD%95%E4%BB%8E%E5%AD%97%E8%8A%82%E9%A1%BA%E5%BA%8F%E6%A0%87%E8%AE%B0-BOM-%E5%88%A4%E6%96%AD%E6%96%87%E6%9C%AC%E5%86%85%E5%AE%B9%E7%BC%96%E7%A0%81)
         2. [1.3.2.2. 无法根据前四个字节判断文本编码怎么办](#%E6%97%A0%E6%B3%95%E6%A0%B9%E6%8D%AE%E5%89%8D%E5%9B%9B%E4%B8%AA%E5%AD%97%E8%8A%82%E5%88%A4%E6%96%AD%E6%96%87%E6%9C%AC%E7%BC%96%E7%A0%81%E6%80%8E%E4%B9%88%E5%8A%9E)
         3. [1.3.2.3. 为什么上面这个有一定局限性](#%E4%B8%BA%E4%BB%80%E4%B9%88%E4%B8%8A%E9%9D%A2%E8%BF%99%E4%B8%AA%E6%9C%89%E4%B8%80%E5%AE%9A%E5%B1%80%E9%99%90%E6%80%A7)
         4. [1.3.2.4. 更灵活的双编码jspwebshell](#%E6%9B%B4%E7%81%B5%E6%B4%BB%E7%9A%84%E5%8F%8C%E7%BC%96%E7%A0%81jspwebshell)
         5. [1.3.2.5. 避免双编码踩坑](#%E9%81%BF%E5%85%8D%E5%8F%8C%E7%BC%96%E7%A0%81%E8%B8%A9%E5%9D%91)
         6. [1.3.2.6. 任意放置的jspReader.matches与%@](#%E4%BB%BB%E6%84%8F%E6%94%BE%E7%BD%AE%E7%9A%84jspReader-matches%E4%B8%8E)
         7. [1.3.2.7. 三重编码](#%E4%B8%89%E9%87%8D%E7%BC%96%E7%A0%81)
   4. [1.4. 其他](#%E5%85%B6%E4%BB%96)

# 浅谈JspWebshell之编码

Y4tacker

2022-11-27 (Updated: 2024-08-04)

[Java](/categories/Java/)

[Java](/tags/Java/), [Webshell](/tags/Webshell/)

# 浅谈JspWebshell之编码

## 写在前面

​ 最近@phithon在知识星球中分享了一个多重编码的webshell姿势后，先膜一下大佬

![](/2022/11/27/year/2022/11/%E6%B5%85%E8%B0%88JspWebshell%E4%B9%8B%E7%BC%96%E7%A0%81/0.png)

出于对代码实现的好奇简单看了看tomcat的具体实现以及尝试是否能够更深入的目的也便有了本篇，当然后面也发现这种方式不太灵活是`有一定编码限制`的，后面也会提到，当然最终经过我的努力，发现了其他`三种实现双重编码的方式`，甚至最后发现可以实现`三重编码`

那么下面就进入正文吧

## 环境相关及其他说明

​ 本篇以tomcat8.0.50为例进行分析，后文简称为tomcat，同时讨论的是第一次访问并编译jsp的过程(有小区别不重要)并且不涉及到其他小版本差异

## 正文

这里没有那么多废话，我们知道其实jsp是Servlet技术的扩展，它本身也是一种模板，通过对这个模板内容的解析，根据一定规则拼接到一个java文件后最终会编译为一个class文件并加载，在这个过程当中就涉及的很多解析的过程，这里由于主题限制，我们不必太过关心，我们重点偏向于去了解它的编码是如何被识别的即可.

对于这部分处理逻辑其实是由`org.apache.jasper.compiler.ParserController#determineSyntaxAndEncoding`做处理，在这个类方法当中有两个比较重要的属性`isXml`与`sourceEnc`，字面理解就能得出一个判定是否jsp格式是通过xml格式编写，另一个`sourceEnc`也就决定着jsp文件的编码相关

### 关于xml格式的一些简单说明

#### xml声明

这里我们我们只需要知道encoding属性可以决定内容编码即可

tomcat对于xml格式还算比较严格，其中如果需要用到xml声明`<?xml`要求“必须”在首位，说明下这里的必须指的是需要解析并获取这个标签中的属性，比如encoding就决定着后续内容的编码，我们需要它生效就需要将这个xml声明放置在文件内容最前面(Ps：这里的最前面指的是被解码后的字符在文件最前面，并不是一定要求是原生的字符串<?xml)，当然如果不需要其实这里就不太重要了

|  |  |
| --- | --- |
| ``` 1 ``` | ``` <?xml version="1.0" encoding="utf-8" ?> ``` |

如果个人比较好奇这部分代码逻辑可以自行看看`org.apache.jasper.xmlparser.XMLEncodingDetector#getEncoding(java.io.InputStream, org.apache.jasper.compiler.ErrorDispatcher)`

#### 如何识别我们的文件内容是xml格式

接下来再来简单说说是如何识别我们的文件是xml格式的呢？

首先是根据后缀名`.jspx`或`.tagx`，当然这俩不在我们今天讨论的范围内

如果后缀名不符合则根据文本内容是否包含有形如`<xxx:root`格式的文本，如果有也会识别为一个xml格式

### 如何决定一个文件的编码

#### 如何从字节顺序标记(BOM)判断文本内容编码

简单来说这部分逻辑其实和W3C所定义的一致

W3C定义了三条XML解析器如何正确读取XML文件的编码的规则：
1.如果文挡有BOM(字节顺序标记)，就定义了文件编码
2.如果没有BOM，就查看XML encoding声明的编码属性
3.如果上述两个都没有，就假定XML文挡采用UTF-8编码

我们的tomcat对这部分实现也是手写根据文件前4个字节(BOM)来决定文件的编码(`org.apache.jasper.compiler.ParserController#determineSyntaxAndEncoding`)

具体是通过函数`XMLEncodingDetector#getEncoding`来动态决定编码

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` private Object[] getEncoding(InputStream in, ErrorDispatcher err)   throws IOException, JasperException {   this.stream = in;   this.err=err;   createInitialReader();   scanXMLDecl();    return new Object[] { this.encoding,                        Boolean.valueOf(this.isEncodingSetInProlog),                        Boolean.valueOf(this.isBomPresent),                        Integer.valueOf(this.skip) }; } ``` |

在这里有两个关键函数，它们都能决定整个文件内容的编码

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` createInitialReader(); scanXMLDecl(); ``` |

其中`createInitialReader`作用有两个一个是根据前四个字节(bom)决定encoding也就是编码，接着往里看在`org.apache.jasper.xmlparser.XMLEncodingDetector#getEncodingName`中

![](/2022/11/27/year/2022/11/%E6%B5%85%E8%B0%88JspWebshell%E4%B9%8B%E7%BC%96%E7%A0%81/1.png)

逻辑很简单，就是根据前4个字节顺序标记判定文件编码

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 ``` | ``` private Object[] getEncodingName(byte[] b4, int count) {         if (count < 2) {             return new Object[]{"UTF-8", null, Boolean.FALSE, Integer.valueOf(0)};         }         int b0 = b4[0] & 0xFF;         int b1 = b4[1] & 0xFF;         if (b0 == 0xFE && b1 == 0xFF) {             return new Object [] {"UTF-16BE", Boolean.TRUE, Integer.valueOf(2)};         }         if (b0 == 0xFF && b1 == 0xFE) {             return new Object [] {"UTF-16LE", Boolean.FALSE, Integer.valueOf(2)};         }          if (count < 3) {             return new Object [] {"UTF-8", null, Boolean.FALSE, Integer.valueOf(0)};         }          int b2 = b4[2] & 0xFF;         if (b0 == 0xEF && b1 == 0xBB && b2 == 0xBF) {             return new Object [] {"UTF-8", null, Integer.valueOf(3)};         }            if (count < 4) {             return new Object [] {"UTF-8", null, Integer.valueOf(0)};         }          int b3 = b4[3] & 0xFF;         if (b0 == 0x00 && b1 == 0x00 && b2 == 0x00 && b3 == 0x3C) {             return new Object [] {"ISO-10646-UCS-4", Boolean.TRUE, Integer.valueOf(4)};         }         if (b0 == 0x3C && b1 == 0x00 && b2 == 0x00 && b3 == 0x00) {             return new Object [] {"ISO-10646-UCS-4", Boolean.FALSE, Integer.valueOf(4)};         }         if (b0 == 0x00 && b1 == 0x00 && b2 == 0x3C && b3 == 0x00) {             return new Object [] {"ISO-10646-UCS-4", null, Integer.valueOf(4)};         }         if (b0 == 0x00 && b1 == 0x3C && b2 == 0x00 && b3 == 0x00) {             return new Object [] {"ISO-10646-UCS-4", null, Integer.valueOf(4)};         }         if (b0 == 0x00 && b1 == 0x3C && b2 == 0x00 && b3 == 0x3F) {             return new Object [] {"UTF-16BE", Boolean.TRUE, Integer.valueOf(4)};         }         if (b0 == 0x3C && b1 == 0x00 && b2 == 0x3F && b3 == 0x00) {             return new Object [] {"UTF-16LE", Boolean.FALSE, Integer.valueOf(4)};         }         if (b0 == 0x4C && b1 == 0x6F && b2 == 0xA7 && b3 == 0x94) {             return new Object [] {"CP037", null, Integer.valueOf(4)};         }          return new Object [] {"UTF-8", null, Boolean.FALSE, Integer.valueOf(0)};      } ``` |

`createInitialReader`另一个作用就是初始化Reader对象(`reader = createReader(stream, encoding, isBigEndian)`)，在Reader里面带有我们对文件编码以及字节序列大小端的关键信息，为下一步调用`scanXMLDecl`扫描解析xml的申明内容做了一个前置准备，在`scanXMLDecl`当中我们其实只需要关注和编码相关的属性(Ps:具体逻辑可以自己看看代码也比较简单，这里相关度不高不多提)，也就是上面xml小节里面提到的

|  |  |
| --- | --- |
| ``` 1 ``` | ``` <?xml version="1.0" encoding="utf-8" ?> ``` |

这里面xml属性的encoding也可以决定整个文件的编码内容，同时我们可以发现这个encoding可以覆盖掉上一步的函数`createInitialReader();`(通过前四字节识别出的编码识别的encoding)，因此配合这个我们也可以构造出一种新的双编码jspwebshell，最后会提到

#### 无法根据前四个字节判断文本编码怎么办

当无法根据前四个字节判断文本编码时，jsp还提供了另一种方式帮助识别编码，对应下图中的`getPageEncodingForJspSyntax`

![](/2022/11/27/year/2022/11/%E6%B5%85%E8%B0%88JspWebshell%E4%B9%8B%E7%BC%96%E7%A0%81/4.png)

有兴趣看看这个函数的实现

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 ``` | ``` private String getPageEncodingForJspSyntax(JspReader jspReader,             Mark ...