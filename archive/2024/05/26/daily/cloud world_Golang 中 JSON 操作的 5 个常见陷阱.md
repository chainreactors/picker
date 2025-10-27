---
title: Golang 中 JSON 操作的 5 个常见陷阱
url: https://cloudsjhan.github.io/2024/05/25/Golang-%E4%B8%AD-JSON-%E6%93%8D%E4%BD%9C%E7%9A%84-5-%E4%B8%AA%E5%B8%B8%E8%A7%81%E9%99%B7%E9%98%B1/
source: cloud world
date: 2024-05-26
fetch_date: 2025-10-06T16:49:20.546841
---

# Golang 中 JSON 操作的 5 个常见陷阱

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## Golang 中 JSON 操作的 5 个常见陷阱

posted

2024-05-25

|

in

[Go](/categories/Go/)

|

visitors:

|

|

wordcount:

2,880
|

min2read ≈

12

Golang 中 JSON 操作的 5 个常见陷阱

![](https://)

JSON 是许多开发人员在工作中经常使用的一种数据格式。它一般用于配置文件或网络数据传输等场景。由于其简单、易懂、可读性好，JSON 已成为整个 IT 界最常用的格式之一。对于这种情况，Golang 和许多其他语言一样，也提供了标准库级别的支持, [encoding/json](https://pkg.go.dev/encoding/json "encoding/json")。

就像 JSON 本身很容易理解一样，用于操作 JSON 的编码/JSON 库也非常容易使用。但我相信，很多开发者可能会像我第一次使用这个库时一样，遇到各种奇怪的问题或 bug。本文总结了我个人在使用 Golang 操作 JSON 时遇到的问题和错误。希望能帮助更多阅读本文的开发者掌握 Golang 的使用技巧，更正确地操作 JSON，避免调用不必要的”坑”。

本文内容基于 Go 1.22。不同版本之间可能存在细微差别。读者在阅读和使用时请注意。同时，本文列出的所有案例均使用 `encoding/json`，不涉及任何第三方 JSON 库。

### 基本用法

先来看下 `encoding/json` 的基本用法。
作为一种数据格式，JSON 的核心操作只有两个：序列化和反序列化。序列化是将 Go 对象转换为 JSON 格式的字符串（或字节序列）。反序列化则相反，是将 JSON 格式的数据转换成 Go 对象。

这里提到的对象是一个宽泛的概念。它不仅指结构对象，还包括切片和映射类型的数据。它们也支持 JSON 序列化。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` | ``` import (   "encoding/json"   "fmt" )  type Person struct {  ID   uint  Name string  Age  int } func MarshalPerson() {  p := Person{   ID:   1,   Name: "Bruce",   Age:  18,  }  output, err := json.Marshal(p)  if err != nil {   panic(err)  }  println(string(output)) } func UnmarshalPerson() {  str := `{"ID":1,"Name":"Bruce","Age":18}`  var p Person  err := json.Unmarshal([]byte(str), &p)  if err != nil {   panic(err)  }  fmt.Printf("%+v\n", p) } ``` |

核心是两个函数 `json.Marshal` 和 `json.Unmarshal`，分别用于序列化和反序列化。这两个函数都会返回错误，在这里我只是简单地 panic 一下。
使用过 `encoding/json` 的读者可能知道，还有另一对工具会经常用到：NewEncoder 和 NewDecoder。简单看一下源代码就会发现，这两个工具的底层核心逻辑调用与 Marshal 是一样的，所以我就不在这里举例说明了。

### 常见的 ‘坑’

#### 1. public or private 字段处理

这可能是刚接触 Go 的开发人员最容易犯的错误。也就是说，如果我们使用结构体处理 JSON，那么结构体的成员字段必须是公有的，即首字母大写的，而私有成员是无法解析的。
例如：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` | ``` type Person struct {   ID   uint   Name string   age  int }  func MarshalPerson() {  p := Person{   ID:   1,   Name: "Bruce",   age:  18,  }  output, err := json.Marshal(p)  if err != nil {   panic(err)  }  println(string(output)) } func UnmarshalPerson() {  str := `{"ID":1,"Name":"Bruce","age":18}`  var p Person  err := json.Unmarshal([]byte(str), &p)  if err != nil {   panic(err)  }  fmt.Printf("%+v\n", p) } // Output Marshal: {"ID":1,"Name":"Bruce"} // Output Unmarshal: {ID:1 Name:Bruce age:0} ``` |

在这里，age 被设置为私有变量，因此序列化的 JSON 字符串中没有 age 字段。同样，在将 JSON 字符串反序列化为 Person 时，也无法正确读取 age 的值。
原因很简单。如果我们深入研究 Marshal 下的源代码，就会发现它实际上使用了 `reflect` 来动态解析 `struct` 对象：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` // .../src/encoding/json/encode.go  func (e *encodeState) marshal(v any, opts encOpts) (err error) {  // ...skip  e.reflectValue(reflect.ValueOf(v), opts)  return nil } ``` |

而 Golang 在语言设计层面禁止对结构的私有成员进行反射式访问，因此这种反射式解析自然会失败，反序列化也是如此。

#### 2. 警惕结构体组合

Go 是面向对象的，但它没有类，只有结构，而结构没有继承性。因此，Go 使用一种组合来重用不同的结构。在许多情况下，这种组合非常方便，因为我们可以像操作结构本身的成员一样操作组合中的其他成员，就像下面这样：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` | ``` type Person struct {   ID   uint   Name string   address }  type address struct {  Code   int  Street string } func (a address) PrintAddr() {  fmt.Println(a.Code, a.Street) } func Group() {  p := Person{   ID:   1,   Name: "Bruce",   address: address{    Code:   100,    Street: "Main St",   },  }  // Access all address's fields and methods directly  fmt.Println(p.Code, p.Street)  p.PrintAddr() } // Output 100 Main St 100 Main St ``` |

结构体组合使用起来确实挺方便。不过，在使用 JSON 解析时，我们需要注意一个小问题。请看下面的代码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` | ``` // The structure used here is the same as the previous one,  // so I won't repeat it. error is also not captured to save space.  func MarshalPerson() {  p := Person{   ID:   1,   Name: "Bruce",   address: address{    Code:   100,    Street: "Main St",   },  }  // It would be more pretty by MarshalIndent  output, _ := json.MarshalIndent(p, "", "  ")  println(string(output)) } func UnmarshalPerson() {  str := `{"ID":1,"Name":"Bruce","address":{"Code":100,"Street":"Main St"}}`  var p Person  _ = json.Unmarshal([]byte(str), &p)  fmt.Printf("%+v\n", p) } // Output MarshalPerson: {   "ID": 1,   "Name": "Bruce",   "Code": 100,   "Street": "Main St" } // Ouptput UnmarshalPerson: {ID:1 Name:Bruce address:{Code:0 Street:}} ``` |

这里先声明一个 Person 对象，然后使用 MarshalIndent 美化序列化结果并打印出来。从打印输出中我们可以看到，整个 Person 对象都被扁平化了。就 Person 结构而言，尽管进行了组合，但它看起来仍有一个地址成员字段。因此，有时我们会想当然地认为 Person 的序列化 JSON 看起来是这样的：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` // The imagine of JSON serialization result {   "ID": 1,   "Name": "Bruce",   "address": {     "Code": 100,     "Street": "Main St"   } } ``` |

但事实并非如此，它被扁平化了。这更符合我们之前直接通过 Person 访问地址成员时的感觉，即地址成员似乎直接成为了 Person 的成员。这一点需要注意，因为这种组合会使序列化后的 JSON 结果扁平化。

另一个有点违反直觉的问题是，地址结构是一个私有结构，而私有成员似乎不应该被序列化？没错，这也是这种组合结构体做 JSON 解析的缺点之一：它暴露了私有组合对象的公共成员。
如果没有特殊需要（例如，原始 JSON 数据已被扁平化，并且有多个结构体的重复字段需要重复使用），从我个人的角度来看，建议这样编写：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` type Person struct {   ID      int   Name    string   Address address } ``` |

#### 3. 反序列化部分成员字段

直接查看代码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` | ``` type Person struct {   ID   uint   Name string }  // PartUpdateIssue simulates parsing two different  // JSON strings with the same structure func PartUpdateIssue() {  var p Person  // The first data has the ID field and is not 0  str := `{"ID":1,"Name":"Bruce"}`  _ = json.Unmarshal([]byte(str), &p)  fmt.Printf("%+v\n", p)  // The second data does not have an ID field,   // deserializing it again with p preserves the last value  str = `{"Name":"Jim"}`  _ = json.Unmarshal([]byte(str), &p)  // Notice the output ID is still 1  fmt.Printf("%+v\n", p) } // Output {ID:1 Name:Bruce} {ID:1 Name:Jim} ``` |

从代码注释中可以知道，当我们重复使用同一结构来反序列化不同的 JSON 数据时，一旦某个 JSON 数据的值只包含部分成员字段，那么未包含的成员就会使用最后一次反序列化的值，会产生脏数据污染问题。

#### 4. 处理指针字段

许多开发人员一听到指针这个词就头疼不已，其实大可不必。但 Go 中的指针确实给开发人员带来了 Go 程序中最常见的 panic 之一：空指针异常。当指针与 JSON 结合时会发生什么呢？

看下面的代码:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` type Person struct {   ID      uint   Name    string   Address *Address }  func UnmarshalPtr() {  str := `{"ID":1,"Name":"Bruce"}`  var p Person  _ = json.Unmarshal([]byte(str), &p)  fmt.Printf("%+v\n", p)  // It would panic this line  // fmt.Printf("%+v\n", p.Address.Street) } // Output {ID:1 Name:Bruce Address:<nil>} ``` |

我们将 Address 成员定义为指针，当我们反序列化一段不包含 Address 的 JSON 数据时，指针字段会被设置为 nil，因为它没有对应的数据。如果我们直接调用 p.Address.xxx，程序会因为 p.Address 为空而崩溃。

因此，如果有一个指针指向我们结构中的一个成员，请记住在使用它之前先确定指针是否为 nil。这有点繁琐，但也没办法。毕竟，编写几行代码与生产环境中的 panic 所造成的损失相比可能并不算什么。

此外，在创建带有指针字段的结构时，指针字段的赋值也会相对繁琐：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` type Person struct {   ID   int       Name string    Age  *int    }  func Foo() {  p := Person{   ID:   1,   Name: "Bruce",   Age:  new(int),  }  *p.Age = 20  // ... } ``` |

#### 5. 零值（默认值）可能造成的问题

零值是 Golang 变量的一个特性，我们可以简单地将其视为默认值。也就是说，如果我们没有显式地给变量赋值，Golang 就会给它赋一个默认值。例如，我们在前面的例子中看到，int 的默认值为 0，string 的默认值为空字符串，指针的零值为 nil，等等。

处理带有零值的 JSON 有哪些隐患？
请看下面的例子：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` type Person struct {   Name        string   ChildrenCnt int }  func ZeroValueConfusion() {  str := `{"Name":"Bruce"}`  var p Person  _ = json.Unmarshal([]byte(str), &p)  fmt.Printf("%+v\n", p)  str2 := `{"Name":"Jim","ChildrenCnt":0}`  var p2 Person  _ = json.Unmarshal([]byte(str2), &p2)  fmt.Printf("%+v\n", p2) } // Output {Name:Bruce ChildrenCnt:0} {Name:Jim ChildrenCnt:0} ``` |

我们在 `Person` 结构中添加了一个 ChildrenCnt 字段，用于计算该人的子女数量。由于该字段的值为零，当 p 加载的 JSON 数据中没有 ChildrenCnt 数据时，该字段的赋值为 0。在 Bruce 和 Jim 的例子中，由于数据缺失，其中一个的子女数为 0，而另一个的子女数为 0...