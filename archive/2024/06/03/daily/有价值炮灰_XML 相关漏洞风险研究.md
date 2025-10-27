---
title: XML 相关漏洞风险研究
url: https://mp.weixin.qq.com/s?__biz=MzA3MzU1MDQwOA==&mid=2247484988&idx=1&sn=0aeb2158b68b18db537c9694446cf052&chksm=9f0c191ba87b900dc17943cbe32151b713d4a7ae6295657deb9614b1a2f01641652dc9234782&scene=58&subscene=0#rd
source: 有价值炮灰
date: 2024-06-03
fetch_date: 2025-10-06T17:32:29.324869
---

# XML 相关漏洞风险研究

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3eicVGzibzClBwcGgibVewXdv6ZodAdTntn2ZXUj4WWGiakf3bJ3cKrMPYCcCiasQmcudaCWOY2DT5RzcDlYeJ6Zn2g/0?wx_fmt=jpeg)

# XML 相关漏洞风险研究

原创

evilpan

有价值炮灰

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3eicVGzibzClBwcGgibVewXdv6ZodAdTntng7fEt55X7cFfxRxMWkNVwlpsSTL2RGBKcfMo4yyWPuwict52auTcRuw/640?wx_fmt=png&from=appmsg "null")

# 前言

经常看到有关 XXE 的漏洞分析，大概知道原理，但是对 XML 中相关的定义却一知半解。XEE 全称为 XML External Entity 即 XML 外部实体，但除了常见的 EXP 还有哪些触发方法？XML 相关的漏洞除了 XXE 还有什么其他攻击面？为了回答这些问题，本文先从开发者的角度先学习 XML 的基本结构和一些进阶用法，然后再引申出相关的攻击场景。

# XML 101

XML 是一个文档标准，用于描述结构化的文本文档，使其同时实现机器可读且人类也可读的目标。其全称为 Extensible Markup Language，即可拓展标记语言。一个简单的 XML 示例如下:

```
<?xml version="1.0" encoding="UTF-8"?>
<foo>hello</foo>
```

其中第一部分为可选的声明(Prolog 或者 Declaration)，描述文档使用的版本以及编码等信息；第二部分是一个标签(Tag)，为 XML 文档中的基本单位，可以嵌套使用但需要正确闭合。

当然 XML 标准中还定义了许多核心概念，如属性(Attributes)、命名空间(Namespaces)、字符数据(CDATA)等，本节关注其中比较重要的几个概念，完整文档可以参考:

* • Extensible Markup Language (XML) 1.0 (Fifth Edition)[1]
* • XML - wikipedia[2]

## DTD

DTD 全称为 **Document Type Definition**，即文档类型定义，主要用于定义 XML 文档的结构，比如指定文档中允许存在哪些元素、元素的内容和属性、元素的嵌套规则等。

我们先看一个 DTD 的经典用法:

```
<?xml version="1.0"?>
<!DOCTYPE note [
<!ELEMENT note (to,from)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
]>
<note>
    <to>Alice</to>
    <from>Bob</from>
</note>
```

上面定义了一个 XML 文档，根结点为 `note`，包含 `to`、`from` 这两个子元素(标签)，且这两个子标签都是文本标签，即其子元素为文本数据，使用 `#PCDATA` 表示(Parsed Character Data)。

将文档类型定义写在 XML 文档中称为内部 DTD，除此之外，还可以写在单独的文件中进行引用，称为外部 DTD，比如写在下面的 `note.dtd` 中:

```
<!ELEMENT note (to,from)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
```

原始的 XML 可以改成:

```
<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to>Alice</to>
    <from>Bob</from>
</note>
```

我们也可以在引入外部 dtd 的同时定义额外的内部 dtd 规则:

```
<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "note.dtd" [
<!ELEMENT msg (#PCDATA)>
]>
<note>
    <to>Alice</to>
    <from>Bob</from>
    <msg>hello</msg>
</note>
```

在 XML 标准中对于 DTD 的格式定义如下(EBNF格式):

```
doctypedecl ::= '<!DOCTYPE' S Name (S ExternalID)? S? ('[' intSubset ']' S?)? '>'

S ::=  (#x20 | #x9 | #xD | #xA)+
ExternalID ::=  'SYSTEM' S SystemLiteral
              | 'PUBLIC' S PubidLiteral S SystemLiteral
intSubset  ::= (markupdecl | DeclSep)*
```

外部 DTD 除了可以用 `SYSTEM` 引入系统磁盘文件，还可以使用 `PUBLIC` 引入网络文件，比如:

```
<?xml version="1.0"?>
<!DOCTYPE note PUBLIC "-//W3C//DTD XMLNote 1.0//EN" "http://evilpan.com/note.dtd">
<note>
    <to>Alice</to>
    <from>Bob</from>
</note>
```

> 其中 PUBLIC 后的字符串 `"-//W3C//...` 为 Public Identifier，用于描述 DTD 的格式。比如针对 HTML 的示例:

* • -//W3C//DTD HTML 4.01//EN[3]
* • -//W3C//DTD HTML 4.01 Transitional//EN[4]
* • -//W3C//DTD HTML 4.01 Frameset//EN[5]

关于 DTD 的详细介绍可以参考下面的文档:

* • Document\_type\_definition - Wikipedia[6]
* • Prolog and Document Type Declaration[7]

## Entity

在 XML 中另外一个重要的概念就是实体(Entity)。对于编程人员来说，实体可以理解为变量。实体的引用**通常**以 `&` 开头且以 `;` 结尾，除了参数实体以 `%` 开头。XML 文档中定义了五个标准实体，分别是:

* • `&amp;` 表示与字符：`&` (ampersand)
* • `&apos;` 表示单引号：`'` (apostrophe)
* • `&quot;` 表示双引号：`"` (quotation mark)
* • `&lt;` 表示小于号：`<` (less than)
* • `&gt;` 表示大于号：`>` (greater than)

实体根据类型主要分为字符实体、命名实体、外部实体和参数实体。

字符实体可以用数字表示任意字符，比如字符 `A` 可以表示为 `&#65;`(十进制) 或者 `&#x41;`(十六进制)；

命名实体在 XML 规范中也称为内部实体，命名实体在内部或者外部 DTD 中进行声明，在 XML 文档解析过程中，实体引用会被替换成其定义的值。XML 文档中对于实体定义的规范如下:

```
[70]    EntityDecl  ::=    GEDecl | PEDecl
[71]    GEDecl      ::=    '<!ENTITY' S Name S EntityDef S? '>'
[72]    PEDecl      ::=    '<!ENTITY' S '%' S Name S PEDef S? '>'
[73]    EntityDef   ::=    EntityValue | (ExternalID NDataDecl?)
[74]    PEDef       ::=    EntityValue | ExternalID
```

其中 `71` 定义内部/外部实体，`72`定义的是参数实体。

一个示例的(内部)实体定义如下:

```
<?xml version="1.0"?>
<!DOCTYPE note [
<!ELEMENT note (to,from)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ENTITY sb "evilpan">
]>
<note>
    <to>&sb;</to>
    <from>&sb;</from>
</note>
```

在 XML 解析时，实体会被替换成引用的值，即:

```
<note>
    <to>evilpan</to>
    <from>evilpan</from>
</note>
```

同时实体的定义中也可以嵌套引用其他实体，比如

```
<!ENTITY c "Hello">
<!ENTITY ch "&c; World">
```

> 注意: 循环引用会导致 XML 解析器报错。

外部实体的定义与上一节中对 DTD 的 `ExternalID` 的定义是一致的:

```
ExternalID ::=  'SYSTEM' S SystemLiteral
              | 'PUBLIC' S PubidLiteral S SystemLiteral
```

外部实体的一个使用示例如下:

```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE root [
<!ENTITY header SYSTEM "header.xml">
]>
<root>
&header;
<body>hello</body>
</root>
```

由于外部实体可以引用文件系统中的文件，因此如果攻击者可控可能会导致信息泄露的风险，这也是 XXE 漏洞的根因，后文会详细介绍。

上面介绍的这些实体统称为一般实体(General Entities)，与之相对应的是参数实体(Parameter Entities)。参数实体同样定义在 DTD 中，但名称前会加一个百分号 `%`，并且参数实体只能在 DTD 中使用 `%name;` 进行引用:

```
<!ENTITY % YN '"Yes"' >
<!ENTITY WhatHeSaid "He said %YN;" >
```

* • Character and Entity References[8]
* • XML entity[9]
* • 在 XML 中添加实体[10] (备份[11])
* • List of XML and HTML character entity references[12]

## Namspace

XML命名空间（XML Namespaces）是一种机制，用于避免XML文档中元素和属性名的冲突。当不同的文档或不同的组织使用相同的名称但定义不同的元素时，通过为元素和属性名提供一个命名空间，可以明确它们的身份和范围。

XML命名空间通过在元素开始标签中使用`xmlns`属性来声明。`xmlns`属性可以定义一个默认命名空间或一个带前缀的命名空间：

* • **默认命名空间**：`xmlns="命名空间URI"`，声明后，当前元素及其子元素（除非另有指定）都属于指定的命名空间。
* • **前缀命名空间**：`xmlns:前缀="命名空间URI"`，仅适用于使用该前缀的元素和属性。

命名空间的使用示例如下，定义了一个默认命名空间和一个前缀命名空间，其中 message 元素属于前缀命名空间 `ex`:

```
<?xml version="1.0"?>
<note xmlns="http://www.evilpan.com/note"
      xmlns:ex="http://www.example.com/foo">
    <to>Alice</to>
    <from>Bob</from>
    <ex:message id="1337">Foo</ex:message>
</note>
```

详见:

* • XML namespaces[13]

## XSD

前面说过 XML 的文档格式定义和校验主要基于文档类型声明 DTD，但其存在许多局限性，比如:

* • 对于一些新的 XML 特性没有明确支持，主要包括 XML namespace；
* • 缺乏表现力，对于一些特殊的文档格式无法进行描述；
* • 缺乏可读性，DTD 的编写大都把 Entity 当做宏来使用，导致难以阅读；
* • ……

为了解决这些问题，W3C 提出了一种新的文档声明格式 XML Schema Definition，即 XSD。与基于DTD（文档类型定义）的验证相比，XML Schema 提供了更丰富的数据类型支持、更强的约束定义能力以及命名空间的支持。

还是以上文中的 note 为例，其 XML 文档内容使用 XML Schema 约束的示例如下:

```
<?xml version="1.0"?>
<note xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:noNamespaceSchemaLocation="note.xsd">
    <to>Alice</to>
    <from>Bob</from>
</note>
```

`note.xsd` 文件同样是一个合法的 XML 文件:

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <!-- 定义根元素 note -->
  <xs:element name="note">
    <xs:complexType>
      <xs:sequence>
        <!-- note 元素包含 to 和 from 子元素 -->
        <xs:element name="to" type="xs:string"/>
        <xs:element name="from" type="xs:string"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

可以看到 XML Schema 可以对元素和属性做出更精确的定义，不过由于其语法相对繁琐也经常被开发者所诟病。关于 XSD 更多的数据结构和数据类型定义，可以参考下面的文档:

* • XML Schema (W3C)[14]
* • W3Cs XML Schema Primer[15]

## XInclude

XML Inclusions (XInclude) 也是 W3C 的一个建议标准，主要用于对 XML 文档进行结构化拆分和包含，一个典型的用法如下:

```
<?xml version="1.0"?>
<note xmlns:xi="http://www.w3.org/2001/XInclude">
    <xi:include parse="xml" href="foo.xml"/>
</note>
```

前文我们学习了 XSD，下面则是 XInclude 元素的 XSD 描述:

* • https://www.w3.org/2001/XInclude/XInclude.xsd

主要定义了 `include` 标签和 `fallback` 子标签，其中 fallback 的作用主要提供在 include 加载失败时的默认信息。

`include` 标签中包含 href、parse 等属性。

```
<xs:complexType name="includeType" mixed="true">
    <xs:choice minOccurs="0" maxOccurs="unbounded">
        <xs:element ref="xi:fallback"/>
        <xs:any namespace="##other" processContents="lax"/>
        <xs:any namespace="##local" processContents="lax"/>
    </xs:choice>
    <xs:attribute name="href" use="optional" type="xs:anyURI"/>
    <xs:attribute name="parse" use="optional" default="xml" type="xi:parseType"/>
    <xs:attribute name="xpointer" use="optional" type="xs:string"/>
    <xs:attribute name="encoding" use="optional" type="xs:string"/>
    <xs:attribute name="accept" use="optional" type="xs:string"/>
    <xs:attribute name="accept-language" use="optional" type="xs:string"/>
    <xs:anyAttribute namespace="##other" processContents="lax"/>
</xs:complexType>
```

其中，

* • href: 指定包含的文件 URI，可以是本地文件路径，也可以是网络地址；
* • parse: 表示所包含文件的格式，为 `xml` 或者 `text`，默认为 `xml`；
* • xpointer: 表示当 parse 为 xml 时，用于指定包含目标 XML 的范围，即选择包含部分的 XML 内容，其语法见 XPointer Framework[16]；
* • encoding: 指定包含文件的编码，仅对 `parse="text"` 有效；
* • accept: 当 href 为网络地址时，用于指定 Accept 头的内容；
* • accept-lang...