---
title: Handlebars：一种模板渲染语言 - 郑瀚Andrew
url: https://buaq.net/go-172249.html
source: unSafe.sh - 不安全
date: 2023-07-18
fetch_date: 2025-10-04T11:52:45.872777
---

# Handlebars：一种模板渲染语言 - 郑瀚Andrew

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

![](https://8aqnet.cdn.bcebos.com/d65aaa1e7737c0f27525f334b9ac3477.jpg)

Handlebars：一种模板渲染语言 - 郑瀚Andrew

Handlebars 是一种简单的模板语言。它使用模板（template）和输入对象（input object）来生成 HTML 或其他文本格式。一个Handlebars模板看起来像带有嵌入
*2023-7-17 21:53:0
Author: [www.cnblogs.com(查看原文)](/jump-172249.htm)
阅读量:23
收藏*

---

Handlebars 是一种简单的模板语言。

它使用模板（template）和输入对象（input object）来生成 HTML 或其他文本格式。

一个Handlebars模板看起来像带有嵌入 Handlebars表达式 的正则表达式文本。

```
<p>{{firstname}} {{lastname}}</p>
```

一个Handlebars中可以包含多个Handlebars表达式，每个Handlebars表达式格式如下：

```
{{, some contents, followed by a }}
```

当Handlebars模板被执行后，表达式将替换为输入对象（input object）中的值。

## 0x1：Simple expressions

以下模板定义了两个 Handlebars 表达式，

```
<p>{{firstname}} {{lastname}}</p>
```

给定如下输入对象：

```
{
  firstname: "Yehuda",
  lastname: "Katz",
}
```

表达式将被相应的键值替换，模版渲染结果如下：

## 0x2：Nested input objects

有时，输入对象包含其他对象或数组。 例如：

```
{
  person: {
    firstname: "Yehuda",
    lastname: "Katz",
  },
}
```

在这种情况下，您可以使用“dot-notation”来访问嵌套属性

```
{{person.firstname}} {{person.lastname}}
```

一些内置帮助器允许您将当前上下文更改为嵌套对象，然后您可以像访问根对象一样访问该对象。

## 0x3：Evaluation context

每个内置的块帮助器（block-helpers）都允许您更改当前的评估上下文（evaluation context），访问方式有两种：

* each
* with

### 1、with-helper

成员帮助器（with-helper）可以访问到对象属性。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717171125503-1253369301.png)

### 2、each-helper

遍历帮助器（each-helper）迭代一个数组，允许我们通过简单的句柄表达式访问每个对象的属性。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717171617928-32581636.png)

## 0x4：Template comments

您可以在handlebars代码中使用注释，就像在代码中一样。由于程序中通常存在一定程度的逻辑，因此增加注释是一个很好的做法。

注释不会出现在结果输出中，如果你希望显示注释，只需使用 HTML 注释即可，它们就会被输出。

任何必须包含 }} 或其他handlebars标记的注释都应使用 {{!-- --}} 语法。

```
{{! This comment will not show up in the output}}
<!-- This comment will show up as HTML-comment -->
{{!-- This comment may contain mustaches like }} --}}
```

## 0x5：Custom Helpers

可以从模板中的任何上下文访问handlebars helper。 您可以使用 Handlebars.registerHelper 方法注册helper。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717173531453-269461996.png)

handlebars helper接收当前函数的上下文，并使用 this. 关键词进行访问。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717173747941-802788593.png)

## 0x6：Block Helpers

块表达式允许您定义帮助器，这些帮助器将使用与当前不同的上下文调用模板的一部分。

这些块助手由助手名称前面的 # 标识开始，并且需要同名助手名称之后的 / 结束。

下面是一个将生成 HTML 列表的助手：

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717175419547-267825351.png)

该示例创建一个名为 list 的 helper 来生成 HTML 列表。helper 接收 people 作为其第一个参数，并接收 options hash 作为其第二个参数。

* people 是一个级联对象，之前章节介绍过
* options hash 是包含一个名为 fn 的属性成员，我们可以使用上下文调用该属性，就像调用普通的 Handlebars 模板一样。

## 0x7：Partials

handlebars partials 允许通过创建共享模板来重用代码，你可以使用 registerPartial 方法注册 partials：

```
Handlebars.registerPartial(
    "person",
    "{{person.name}} is {{person.age}} years old.\n"
)
```

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717205203274-1005086159.png)

Handlebars 表达式是 Handlebars 模板的基本单元。 您可以在 {{mustache}} 中单独使用它们，将它们传递给 Handlebars 帮助器，或者将它们用作哈希参数中的值。

## 0x1：Basic Usage

Handlebars 表达式是用双花括号 {{}} 括起来的一些内容。 在下面的模板中，firstname 是一个用双花括号括起来的变量，它被称为一个表达式。

```
<p>{{firstname}} {{lastname}}</p>
```

如果以下输入对象应用于模板，

```
{
  firstname: "Yehuda",
  lastname: "Katz",
}
```

表达式被编译以产生如下输出：

## 0x2：Path expressions

Handlebars 表达式也可以是点分隔或者/间隔的路径。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717210655084-373259236.png)

## 0x3：Changing the context

#with 和 #each 等一些帮助器允许您深入嵌套对象。当你在路径中包含 ../ 时，Handlebars 将上下文切换到父级上下文。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717211149722-872292404.png)

## 0x4：Helpers

### 1、Helpers with Hash arguments

Handlebars 向 helpers 提供附加元数据（例如哈希参数）作为最终参数。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717212121330-52843047.png)

## 0x5：Whitespace Control

通过在大括号中添加 ~ 字符，可以从任何 Mustache 语句的任一侧省略模板空白。 应用时，该侧的所有空格都将被删除，直到该侧的第一个Handlebars表达式或非空格字符。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717212706657-1273312253.png)

Handlebars 允许通过 partials 实现模板重用。

Partials 是普通的 Handlebars 模板，同时它可以被其他模板直接调用。

## 0x1：Basic Partials

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717213210411-12254659.png)

## 0x2：Dynamic Partials

可以使用子表达式语法动态选择要执行的部分。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717213424003-1993722746.png)

在上图中，whichPartial 被执行，然后渲染该函数返回 partials 名称。由于子表达式不解析变量，因此 whichPartial 必须是函数。

如果一个简单变量具有 partials 名称，则可以通过 lookup helper 来解析它。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717213920752-302804905.png)

## 0x3：Partial Parameters

自定义数据可以通过哈希参数传递给 partials。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717214212958-816327307.png)

这对于将父级上下文环境中的数据公开给 partials 上下文特别有用：

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717214404738-1282734788.png)

## 0x4：Partial Blocks

尝试渲染未找到的 partials 时的正常行为是实现抛出错误。如果需要故障转移，则可以使用块语法调用 partials。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717214640168-946921180.png)

如果 myPartial partials 未注册，这将呈现故障转移内容。

此块语法还可用于将模板传递给 partials，该 partials 可以由专门命名的 @partial-block 执行。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717214901899-2132304890.png)

当以这种方式调用时，该块将在调用时的 partia 上下文中执行。 深度路径和块参数相对于 partia 块而不是部分模板进行操作。

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230717215111752-1931152371.png)

参考链接：

```
https://handlebarsjs.com/guide/partials.html#basic-partials
```

文章来源: https://www.cnblogs.com/LittleHann/p/17560242.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)