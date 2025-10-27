---
title: 一些在 Golang 中高效处理 Collection 类型的库
url: https://cloudsjhan.github.io/2024/05/05/%E4%B8%80%E4%BA%9B%E5%9C%A8-Golang-%E4%B8%AD%E9%AB%98%E6%95%88%E5%A4%84%E7%90%86-Collection-%E7%B1%BB%E5%9E%8B%E7%9A%84%E5%BA%93/
source: cloud world
date: 2024-05-06
fetch_date: 2025-10-06T17:15:20.729710
---

# 一些在 Golang 中高效处理 Collection 类型的库

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 一些在 Golang 中高效处理 Collection 类型的库

posted

2024-05-05

|

in

[Golang](/categories/Golang/)

|

visitors:

|

|

wordcount:

5,753
|

min2read ≈

29

一些在 Golang 中高效处理 Collection 类型的库

![](https://)

处理集合是构建任何应用程序的重要部分。通常，您需要以下几类操作：

* 转换：将某个函数应用于集合中的每个元素，以创建一个新类型的新集合；
* 过滤：选择满足特定条件的集合中的元素；
* 聚合：从集合中计算出单个结果，通常用于汇总；
* 排序/排序：根据某些标准重新排列集合的元素；
* 访问：根据其属性或位置检索元素的操作；
* 实用程序：与集合一起工作的通用操作，但不一定完全适合上述分类。

尽管Go具有许多优点，但对于高级集合操作的内置支持相对有限，因此如果需要，您需要使用第三方包。在本文中，我将探讨几个流行的Go库，这些库可以增强语言的能力，以有效地处理集合，涵盖它们的功能和功能。这篇评论将帮助您选择合适的工具，以简化Go项目中的数据处理任务。

### Introduction

让我们从上面的每个集合操作类中回顾一些流行的方法。

#### 转换

Map — 对集合中的每个元素应用一个函数，并返回结果集合；
FlatMap — 将每个元素处理为一个元素列表，然后将这些列表展平为一个列表。

#### 过滤

Filter — 删除不匹配谓词函数的元素；
Distinct — 从集合中删除重复的元素；
TakeWhile — 返回满足给定条件的元素，直到遇到不满足条件的元素为止；
DropWhile — 删除满足给定条件的元素，然后返回剩余的元素。

#### 聚合

Reduce — 使用给定的函数组合集合的所有元素，并返回组合结果；
Count — 返回满足特定条件的元素数量；
Sum — 计算集合中每个元素的数字属性之和；
Max/Min — 确定元素属性中的最大值或最小值；
Average — 计算集合中元素的数字属性的平均值。

#### 排序/排序

Sort — 根据比较器规则对集合的元素进行排序；
Reverse — 颠倒集合中元素的顺序。

#### 访问

Find — 返回匹配给定谓词的第一个元素；
AtIndex — 检索特定索引处的元素。

#### 实用程序

GroupBy — 根据键生成器函数将元素分类为组；
Partition — 根据谓词将集合分成两个集合：一个用于满足谓词的元素，另一个用于不满足谓词的元素；
Slice Operations — 修改集合视图或划分的操作，如切片或分块。

### Go 内置的能力

在Go语言中，有几种类型可用于处理数据集合：

数组（Arrays） — 固定大小的元素集合。数组大小在声明时定义，例如 `var myArray [5]int`；
切片（Slices） — 动态大小的元素集合。切片建立在数组之上，但与数组不同的是，它们可以增长或缩小。声明方式：`mySlice := []int{1, 2, 3}`；
映射（Maps） — 键-值对的集合。映射可以动态增长，且键的顺序不受保证。例如 `myMap := map[string]int{"first": 1, "second": 2}` 创建了一个字符串键和整数值的映射；
通道（Channels） — 类型化的通信原语，允许在goroutine之间共享数据。例如 `myChan := make(chan int)` 创建了一个传输整数的通道。

Go标准库提供了其他结构和实用程序，可以作为集合或增强集合的功能，例如：

堆（Heap） — container/heap包为任何sort.Interface提供了堆操作。堆是具有以下特性的树：每个节点都是其子树中值最小的节点；
链表（List） — container/list包实现了双向链表；
环形链表（Ring） — container/ring包实现了环形链表的操作。

此外，作为Go标准库的一部分，还有用于处理切片和映射的包：

slices — 该包定义了与任何类型的切片一起使用的各种有用的函数；
maps — 该包定义了与任何类型的映射一起使用的各种有用的函数。

通过内置功能，您可以对集合执行一些操作：

获取数组/切片/映射的长度；
通过索引/键访问元素，对切片进行“切片”；
遍历项目。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``` | ``` package main  import "fmt"  func main() {  s := []int{1, 2, 3, 4, 5}  m := map[int]string{1: "one", 2: "two", 3: "three"}   fmt.Printf("len(s)=%d\n", len(s))  fmt.Printf("len(m)=%d\n", len(m))  fmt.Printf("cap(s)=%d\n", cap(s))  // fmt.Printf("cap(m)=%d\n", cap(m)) // error: invalid argument m (type map[int]string) for cap   // panic: runtime error: index out of range [5] with length 5  // fmt.Printf("s[5]=%d\n", s[5])   // panic: runtime error: index out of range [5] with length 5  // s[5] = 6   s = append(s, 6)  fmt.Printf("s=%v\n", s)  fmt.Printf("len(s)=%d\n", len(s))  fmt.Printf("cap(s)=%d\n", cap(s))   m[4] = "four"  fmt.Printf("m=%v\n", m)   fmt.Printf("s[2:4]=%v\n", s[2:4])  fmt.Printf("s[2:]=%v\n", s[2:])  fmt.Printf("s[:2]=%v\n", s[:2])  fmt.Printf("s[:]=%v\n", s[:]) } ``` |

上面的代码会打印：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` len(s)=5 len(m)=3 cap(s)=5 s=[1 2 3 4 5 6] len(s)=6 cap(s)=10 m=map[1:one 2:two 3:three 4:four] s[2:4]=[3 4] s[2:]=[3 4 5 6] s[:2]=[1 2] s[:]=[1 2 3 4 5 6] ``` |

让我们逐个看下 Go 内置的 Package。

### Slices

切片 slices包最近才出现在Go标准库中，从Go 1.21版本开始。这是语言中的一个重大进步，但我仍然更喜欢使用外部库来处理集合（您很快就会明白原因）。让我们来看看这个库如何支持所有的集合操作类别。

#### Aggregation

slices 能够快速在切片中找到最小/最大值：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` | ``` package main  import (  "fmt"  "slices" )  type Example struct {  Name   string  Number int }  func main() {  s := []int{1, 2, 3, 4, 5}   fmt.Printf("Min: %d\n", slices.Min(s))  fmt.Printf("Max: %d\n", slices.Max(s))   e := []Example{   {"A", 1},   {"B", 2},   {"C", 3},   {"D", 4},  }   fmt.Printf("Min: %v\n", slices.MinFunc(   e,   func(i, j Example) int {    return i.Number - j.Number   }),  )   fmt.Printf("Max: %v\n", slices.MaxFunc(   e,   func(i, j Example) int {    return i.Number - j.Number   }),  ) } ``` |

上面的代码打印：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` Min: 1 Max: 5 Min: {A 1} Max: {D 4} ``` |

#### Sorting/Ordering

slices 能够使用比较函数对切片进行排序：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` | ``` package main  import (  "fmt"  "slices" )  type Example struct {  Name   string  Number int }  func main() {  s := []int{4, 2, 5, 1, 3}   slices.Sort(s)  fmt.Printf("Sorted: %v\n", s)   slices.Reverse(s)  fmt.Printf("Reversed: %v\n", s)   e := []Example{   {"C", 3},   {"A", 1},   {"D", 4},   {"B", 2},  }   slices.SortFunc(e, func(a, b Example) int {   return a.Number - b.Number  })   fmt.Printf("Sorted: %v\n", e)   slices.Reverse(e)  fmt.Printf("Reversed: %v\n", e) } ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` Sorted: [1 2 3 4 5] Reversed: [5 4 3 2 1] Sorted: [{A 1} {B 2} {C 3} {D 4}] Reversed: [{D 4} {C 3} {B 2} {A 1}] ``` |

不过这个方法有个缺点，就是排序是原地进行的，修改了原始切片。如果该方法返回一个新的排序后的切片，从而保留原始数组会更好一点。

#### 访问元素

`slices`暴露了一些方法，允许用户在切片中查找元素的位置：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` | ``` package main  import (  "fmt"  "slices" )  type Example struct {  Name   string  Number int }  func main() {  s := []int{4, 2, 5, 1, 3}   i := slices.Index(s, 3)  fmt.Printf("Index of 3: %d\n", i)   e := []Example{   {"C", 3},   {"A", 1},   {"D", 4},   {"B", 2},  }   i = slices.IndexFunc(e, func(a Example) bool {   return a.Number == 3  })   fmt.Printf("Index of 3: %d\n", i) } ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` Index of 3: 4 Index of 3: 0 ``` |

如果你正在处理已排序的切片，你可以使用 BinarySearch 或 BinarySearchFunc 在排序的切片中搜索目标，并返回目标被找到的位置或目标将出现在排序顺序中的位置；它还返回一个布尔值，指示目标是否在切片中被找到。切片必须按递增顺序排序。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` package main  import (  "fmt"  "slices" )  func main() {  s := []int{4, 2, 5, 1, 3}   slices.Sort(s)   i, found := slices.BinarySearch(s, 3)  fmt.Printf("Position of 3: %d. Found: %t\n", i, found)   i, found = slices.BinarySearch(s, 6)  fmt.Printf("Position of 6: %d. Found: %t\n", i, found) } ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` Position of 3: 2. Found: true Position of 6: 5. Found: false ``` |

#### 实用函数

slices提供了许多实用函数：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``` | ``` package main  import (  "fmt"  "slices" )  type Example struct {  Name   string  Number int }  func main() {  e1 := []Example{   {"C", 3},   {"A", 1},   {"D", 4},   {"B", 2},  }   e2 := []Example{   {"A", 1},   {"B", 2},   {"C", 3},   {"D", 4},  }   fmt.Printf("Compare: %v\n", slices.CompareFunc(e1, e2, func(a, b Example) int {   return a.Number - b.Number  }))   fmt.Printf("Contains: %v\n", slices.ContainsFunc(e1, func(a Example) bool {   return a.Number == 2  }))   fmt.Printf("Delete: %v\n", slices.Delete(e1, 2, 3))  fmt.Printf("Equal: %v\n", slices.Equal(e1, e2))   fmt.Printf("Is Sorted: %v\n", slices.IsSortedFunc(e1, func(a, b Example) int {   return a.Number - b.Number  })) } ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` Compare: 2 Contains: true Delete: [{C 3} {A 1} {B 2}] Equal: false Is Sorted: false ``` |

`slices` 包的官方文档[地址](https://pkg.go.dev/slices?source=post_page-----8387cecdb8a4-------------------------------- "slices")

### Map

类似于slices，maps也是从Go 1.21开始出现在Go标准库中的。它定义了各种方法来操作 maps。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` package main  import (  "fmt"  "maps" )  func main() {  m := map[int]string{1: "one", 2: "two", 3: "three"}  c := maps.Clone(m)   c[4] = "four"   fmt.Printf("Original: %v\n", m)  fmt.Printf("Clone: %v\n", c)   maps.DeleteFunc(c, func(k int, v string) bool { return k%2 == 0 })  fmt.Printf("DeleteFunc: %v\n", c)   fmt.Printf("Equal: %v\n", maps.Equal(m...