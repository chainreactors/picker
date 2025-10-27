---
title: Golang 实现枚举的各种方法及最佳实践
url: https://cloudsjhan.github.io/2024/05/07/Golang-%E5%AE%9E%E7%8E%B0%E6%9E%9A%E4%B8%BE%E7%9A%84%E5%90%84%E7%A7%8D%E6%96%B9%E6%B3%95%E5%8F%8A%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/
source: cloud world
date: 2024-05-08
fetch_date: 2025-10-06T17:15:27.016309
---

# Golang 实现枚举的各种方法及最佳实践

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## Golang 实现枚举的各种方法及最佳实践

posted

2024-05-07

|

in

[Golang](/categories/Golang/)

|

visitors:

|

|

wordcount:

1,795
|

min2read ≈

7

Golang 实现枚举的各种方法及最佳实践

![](https://)

枚举提供了一种表示一组命名常量的方式。虽然 Go 语言没有内置的枚举类型，但开发者可以通过常量/自定义类型来模拟类似枚举的行为。

枚举在编程语言中扮演着至关重要的角色，提供了一种简洁而富有表现力的方式来定义一组命名常量。虽然像Java或C#这样的语言提供了对枚举的内置支持，但Go采用了不同的方法。在 Go 中，枚举并不是一种原生的语言特性，但开发者有几种技术可供使用，以实现类似的功能。
本文深入探讨了 Go 语言中的枚举，探索了定义和有效使用它们的各种技术。通过代码示例、比较和实际用例，我们的目标是掌握枚举并在 Go 项目中高效使用它们。

### Understanding Enum

在 Go 语言中，枚举（enumerations 的缩写）提供了一种表示一组命名常量的方式。虽然 Go 语言没有像其他一些语言那样内建的枚举类型，但开发者可以使用常量或自定义类型来模拟类似枚举的行为。让我们深入了解 Go 中枚举的目的和语法：

目的
可读性和可维护性：通过给特定值分配有意义的名称，枚举使代码更具可读性和自解释性。这增强了代码的可维护性，因为更容易理解每个常量的目的。
类型安全性：枚举有助于通过将变量限制为预定义的一组值来强化类型安全性。这减少了因使用错误值而引起的运行时错误的可能性。

### 实现语法

* 使用常量

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` package main  import "fmt"  // Enum defining colors using constants const (     Red   = iota // 0     Green        // 1     Blue         // 2 )  func main() {     fmt.Println(Red, Green, Blue) } ``` |

* 使用自定义类型

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` package main  import "fmt"  // Enum defining colors using custom types type CardType int  const (     VISA CardType = iota // 0     MASTER            // 1     JCB             // 2 )  func main() {     fmt.Println(VISA, MASTER, BlueJCB } ``` |

在上述示例中：

* 我们使用常量和自定义类型定义颜色枚举。
* iota 用于自动生成从 0 开始递增的值。
* 常量被分配给每个枚举值，而在自定义类型的情况下，会指定一个底层类型（通常是 int）。

Go 语言中的枚举提供了一种灵活的方式来表示一组固定值，提高了代码的清晰度和类型安全性。然而，根据你项目的具体需求，选择适当的方法（常量或自定义类型）至关重要。

### 在 Go 中使用 Enum 类型的优缺点

#### 优点

* 提高可读性：枚举通过为特定值提供有意义的名称来增强代码的可读性。这使得代码更加自解释，更易于开发人员理解。
* 类型安全性：枚举有助于通过限制变量为预定义的一组值来强化类型安全性。这减少了使用不正确或意外值的风险，从而减少了运行时错误。
* 明确定义常量：枚举允许开发人员明确定义一组常量，明确指出哪些值对于特定变量或参数是有效的。
* 增强可维护性：通过使用枚举，开发人员可以轻松地在单一位置更新或修改允许的值集，减少代码库中不一致或错误的可能性。

#### 缺点

* 没有内置枚举类型：与其他一些编程语言不同，Go语言没有内置的枚举类型。开发者必须使用诸如常量或自定义类型之类的解决方法来模拟类似枚举的行为。
* 冗长语法：使用常量或自定义类型在 Go 中实现枚举有时会导致冗长的语法，特别是当定义了一组大型的枚举值时。
* 表达力有限：Go 中的枚举缺乏其他语言枚举中的一些高级特性，例如将值或行为与个别枚举常量关联的能力。
* 潜在冲突：当使用常量作为枚举时，如果在同一代码库的不同上下文中使用了相同的常量名称，存在冲突的风险。这可能导致意外的行为或错误。
* 额外开销：使用自定义类型实现枚举可能会引入额外的开销，特别是如果为每个枚举常量定义了关联的方法或行为。

尽管存在这些限制，Go 语言中的枚举类型仍然是提高代码清晰度、可维护性和类型安全性的有价值工具，开发者可以通过理解它们的优点和局限性来有效地利用它们。

### 第三方类库

几个第三方库在 Go 语言中提供了类似枚举的功能：

go-enum：它可以从简单的定义格式生成 Go 语言的枚举代码。（点击 [go-enum GitHub](https://github.com/abice/go-enum "go-enum") 以获取更多信息）。
stringer：它为在 Go 源代码中定义的枚举自动生成字符串方法。（点击 [stringer](https://golang.org/x/tools/cmd/stringer "stinger") 工具以获取更多详情）。

### 上述三种方式该如何选择？

* 如果希望实现简单，并且枚举集较小且不需要额外特性，使用 Iota 常量即可。
* 如果需要更好的类型安全性、灵活性，以及需要与枚举关联的额外方法，使用自定义类型。
* 如果需要自动化枚举生成或需要额外特性（如字符串表示），考虑使用库，但要谨慎处理依赖性和兼容性问题。

### 一些 Use Cases

* 表示星期

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` package main  import "fmt"  // Enum for days of the week using custom types type DayOfWeek int  const (     Sunday DayOfWeek = iota     Monday     Tuesday     Wednesday     Thursday     Friday     Saturday )  func main() {     fmt.Println("Days of the week:")     fmt.Println("Sunday:", Sunday)     fmt.Println("Monday:", Monday)     fmt.Println("Tuesday:", Tuesday)     fmt.Println("Wednesday:", Wednesday)     fmt.Println("Thursday:", Thursday)     fmt.Println("Friday:", Friday)     fmt.Println("Saturday:", Saturday) } ``` |

* 表示访问级别

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` type AccessLevel int  const (     Guest AccessLevel = iota     User     Moderator     Admin ) ``` |

* 在 Go 语言中，枚举提供了一种强大的机制，用于提高代码的清晰度、可维护性和类型安全性。通过遵循最佳实践并有效利用枚举，开发者可以在他们的 Go 项目中编写更加健壮和可读的代码。

### 结论

在本指南中，我们探讨了在 Go 语言中实现枚举的各种方法，并讨论了它们各自的优势、局限性和最佳实践。

本质上，Go 语言中的枚举通过提供一种结构化的方式来表示一组固定值，赋予开发者编写更清洁、更易于维护的代码的能力。通过理解本指南中概述的不同技术和最佳实践，开发者可以有效地利用枚举来增强他们的 Go 项目。

---

-------------The End-------------

Title:[Golang 实现枚举的各种方法及最佳实践](/2024/05/07/Golang-%E5%AE%9E%E7%8E%B0%E6%9E%9A%E4%B8%BE%E7%9A%84%E5%90%84%E7%A7%8D%E6%96%B9%E6%B3%95%E5%8F%8A%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年05月07日 - 22:05

Last Update:2024年05月07日 - 22:05

Original Link:[https://cloudsjhan.github.io/2024/05/07/Golang-实现枚举的各种方法及最佳实践/](/2024/05/07/Golang-%E5%AE%9E%E7%8E%B0%E6%9E%9A%E4%B8%BE%E7%9A%84%E5%90%84%E7%A7%8D%E6%96%B9%E6%B3%95%E5%8F%8A%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/ "Golang 实现枚举的各种方法及最佳实践")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

微信支付

![cloud sjhan 支付宝](/images/alipay.jpg)

支付宝

[golang](/tags/golang/)
 [enum](/tags/enum/)

(>给这篇博客打个分吧<)

[一些在 Golang 中高效处理 Collection 类型的库](/2024/05/05/%E4%B8%80%E4%BA%9B%E5%9C%A8-Golang-%E4%B8%AD%E9%AB%98%E6%95%88%E5%A4%84%E7%90%86-Collection-%E7%B1%BB%E5%9E%8B%E7%9A%84%E5%BA%93/ "一些在 Golang 中高效处理 Collection 类型的库")

[什么情况下使用 ErrGroup VS waitGroup？](/2024/05/11/%E4%BB%80%E4%B9%88%E6%83%85%E5%86%B5%E4%B8%8B%E4%BD%BF%E7%94%A8-ErrGroup-VS-waitGroup%EF%BC%9F/ "什么情况下使用 ErrGroup VS waitGroup？")

* Content
* Overview

![cloud sjhan](/images/avatar.png)

cloud sjhan

[166
日志](/archives/)

[40
分类](/categories/index.html)

[73
标签](/tags/index.html)

[RSS](/atom.xml)

[GitHub](https://github.com/hantmac "GitHub")

E-Mail

Links

* [CSDN](https://blog.csdn.net/u012421976 "CSDN")
* [w3school](http://www.w3school.com.cn/ "w3school")
* [快搜](http://search.chongbuluo.com/ "快搜")

1. [1. Understanding Enum](#Understanding-Enum)
2. [2. 实现语法](#实现语法)
3. [3. 在 Go 中使用 Enum 类型的优缺点](#在-Go-中使用-Enum-类型的优缺点)
   1. [3.1. 优点](#优点)
   2. [3.2. 缺点](#缺点)
4. [4. 第三方类库](#第三方类库)
5. [5. 上述三种方式该如何选择？](#上述三种方式该如何选择？)
6. [6. 一些 Use Cases](#一些-Use-Cases)
7. [7. 结论](#结论)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;