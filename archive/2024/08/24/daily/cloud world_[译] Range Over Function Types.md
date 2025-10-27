---
title: [译] Range Over Function Types
url: https://cloudsjhan.github.io/2024/08/23/%E8%AF%91-Range-Over-Function-Types/
source: cloud world
date: 2024-08-24
fetch_date: 2025-10-06T18:04:10.618327
---

# [译] Range Over Function Types

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## [译] Range Over Function Types

posted

2024-08-23

|

in

[Go](/categories/Go/)

|

visitors:

|

|

wordcount:

6,346
|

min2read ≈

25

![](https://)

在 Go 1.22 中作为试验特性发布，在 Go 1.23 中正式发布。我们可以在 for 循环的 range 子句中使用迭代器函数。就在前几天，官方也发布了 [Range over Function Types](https://go.dev/blog/range-functions "Range Over Function Types") 的教程。

> Ian Lance Taylor
> in 20 August 2024

---

![](https://files.mdnice.com/user/4760/92215706-581f-4151-a75d-9f0cb7d7dbac.png)

# Go 1.23版本中函数类型范围遍历的新特性介绍

> 这是 Ian 在2024年GopherCon大会上演讲的博客文章版本，下面开始正文（文章较长但干货真的很多，读完会对迭代器函数的用法有新的理解）。

在 Go 1.23版本中，我们引入了一个新的语言特性：对函数类型进行范围遍历（Range over function types）。这篇博客文章将解释我们为什么要添加这个新特性，它究竟是什么，以及如何使用它。

## WHY？

自 Go 1.18 版本以来，我们就能够编写新的泛型容器类型。例如，让我们实现一个非常简单的 Set 类型，一个基于 map 实现的泛型类型。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` // Set 保存一组元素。 type Set[E comparable] struct {     m map[E]struct{} }  // New 返回一个新的[Set]。 func New[E comparable]() *Set[E] {     return &Set[E]{m: make(map[E]struct{})} } ``` |

自然地，一个 set 类型有添加元素的方法和检查元素是否存在的方法。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` // Add 向set添加一个元素。 func (s *Set[E]) Add(v E) {     s.m[v] = struct{}{} }  // Contains 报告一个元素是否在set中。 func (s *Set[E]) Contains(v E) bool {     _, ok := s.m[v]     return ok } ``` |

还需要一个函数来返回两个集合的并集。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` // Union 返回两个set的并集。 func Union[E comparable](s1, s2 *Set[E]) *Set[E] {     r := New[E]()     // 注意for/range在内部Set字段m上。     // 我们正在遍历s1和s2中的map。     for v := range s1.m {         r.Add(v)     }     for v := range s2.m {         r.Add(v)     }     return r } ``` |

让我们花一点时间看看 Union 函数的实现。为了计算两个集合的并集，我们需要一种方法来获取每个集合中的所有元素。在这段代码中，我们使用了一个 for/range 语句来遍历 set 类型的未导出字段。这只在 Union 函数定义在set包中时才有效。

但是，有很多原因可能会有人想要遍历集合中的所有元素。这个 set 包必须为其用户提供一些方法来做到这一点。

这应该怎么实现呢？

## Push Set 元素

一种方法是提供一个 Set 方法，该方法接受一个函数，并对 Set 中的每个元素调用该函数。我们将这称为 Push，因为 Set 将每个值推送到函数中。如果函数返回 false，我们停止调用它。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` func (s *Set[E]) Push(f func(E) bool) {     for v := range s.m {         if !f(v) {             return         }     } } ``` |

在 Go 标准库中，我们看到这种通用模式被用于 [sync.Map.Range](https://pkg.go.dev/sync#Map.Range "sync.Map.Range") 方法、[flag.Visit](https://pkg.go.dev/flag#Visit "flag.Visit") 函数和 [filepath.Walk](https://pkg.go.dev/path/filepath#Walk "filepath.Walk") 函数等场景。这是一个通用模式，并非完全相同的模式；实际上，这三个例子的工作原理并不完全相同。

这就是使用 Push 方法打印 Set 中所有元素的样子：你用一个函数调用 Push，该函数对元素执行你想要的操作。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` func PrintAllElementsPush[E comparable](s *Set[E]) {     s.Push(func(v E) bool {         fmt.Println(v)         return true     }) } ``` |

## 拉取 Set 元素

另一种遍历 Set 元素的方法是返回一个函数。每次调用该函数时，它将从 Set 中返回一个值，以及一个布尔值，报告该值是否有效。当循环遍历完所有元素时，布尔结果将为 false。在这种情况下，我们还需要一个停止函数，当不再需要更多值时可以调用它。

这个实现使用了一个通道对，一个用于集合中的值，一个用于停止返回值。我们使用一个 goroutine 在通道上发送值。next 函数通过从元素通道读取来从集合中返回一个元素，stop 函数通过关闭停止通道来告诉 goroutine 退出。我们需要 stop 函数以确保当不再需要更多值时 goroutine 能够退出。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` | ``` func (s *Set[E]) Pull() (func() (E, bool), func()) {     ch := make(chan E)     stopCh := make(chan bool)      go func() {         defer close(ch)         for v := range s.m {             select {             case ch <- v:             case <-stopCh:                 return             }         }     }()      next := func() (E, bool) {         v, ok := <-ch         return v, ok     }      stop := func() {         close(stopCh)     }      return next, stop } ``` |

标准库中没有任何东西完全以这种方式工作。[runtime.CallersFrames](https://pkg.go.dev/runtime#CallersFrames "runtime.CallerFreames") 和 [reflect.Value.MapRange](https://pkg.go.dev/reflect#Value.MapRange "reflect.Value.MapRange") 有些相似，尽管它们返回的是带有方法的值，而不是直接返回函数。

这就是使用 Pull 方法打印 Set 中所有元素的例子。你调用 Pull 来获取一个函数，并在 for 循环中反复调用该函数。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` func PrintAllElementsPull[E comparable](s *Set[E]) {     next, stop := s.Pull()     defer stop()     for v, ok := next(); ok; v, ok = next() {         fmt.Println(v)     } } ``` |

## 标准化方法

现在我们已经看到了两种不同的方法来遍历一个集合的所有元素。不同的 Go 包使用这些方法和几种其他方法。这意味着，当你开始使用一个新的 Go 容器包时，你可能需要学习一种新的循环机制。同时，这意味着我们不能编写一个函数来与几种不同类型的容器一起工作，因为容器类型将以不同的方式处理循环。

我们希望通过为容器遍历开发标准方法来改善 Go 生态系统。

## 迭代器

这当然是许多编程语言中出现的问题。

1994 年首次出版的流行书籍《[设计模式](https://en.wikipedia.org/wiki/Design_Patterns "Design_pattern book")》将此描述为迭代器模式。你使用迭代器来“提供一种顺序访问聚合对象元素的方法，而不需要暴露其底层表示。”这里所谓的聚合对象就是我一直所说的容器。聚合对象或容器只是保存其他值的值，比如我们一直在讨论的 Set 类型。

像编程中的许多想法一样，迭代器可以追溯到 20 世纪 70 年代 Barbara Liskov 开发的 [CLU](https://en.wikipedia.org/wiki/CLU_%28programming_language) “CLU”) 语言。

今天，许多流行的语言以这样或那样的方式提供迭代器，包括但不限于 C++、Java、Javascript、Python和Rust。

然而，在 1.23 版本之前，Go 并没有。

## For/range

正如我们所知，Go 有内置于语言的容器类型：切片、数组和 map。它有一种访问这些值的元素的方法，而不需要暴露其底层表示：for/range语句。for/range语句适用于 Go 的内置容器类型（以及字符串、channel，以及从 Go 1.22 开始的 int）。

for/range 语句是迭代，但它不是今天流行语言中出现的迭代器。尽管如此，能够使用 for/range 来迭代像Set类型这样的用户定义容器将是很好的。

然而，在 1.23 版本之前的 Go 并不支持这一点。

## 此版本中的改进

对于 Go 1.23，我们决定支持对用户定义的容器类型进行 for/range，并支持迭代器的标准化形式。

我们扩展了 for/range 语句，使其支持对函数类型进行范围遍历。我们将在下面看到这如何帮助循环遍历用户定义的容器。

我们还添加了标准库类型和函数，以支持使用函数类型作为迭代器。标准迭代器的定义让我们能够编写与不同容器类型平滑协作的函数。

## 范围遍历（部分）函数类型

改进的 for/range 语句不支持任意函数类型。截至 Go 1.23，它现在支持对接受单个参数的函数进行范围遍历。这个单一参数本身必须是一个函数，它接受零到两个参数并返回一个 bool；按照惯例，我们称之为 yield函数。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` func(yield func() bool)  func(yield func(V) bool)  func(yield func(K, V) bool) ``` |

当我们谈到 Go 中的迭代器时，我们指的是具有这三种类型之一的函数。正如我们将在下面讨论的，标准库中还有另一种迭代器：拉取迭代器。当需要区分标准迭代器和拉取迭代器时，我们称标准迭代器为推送迭代器。这是因为，正如我们将看到的，它们通过调用 yield 函数来推送一系列值。

## 标准（推送）迭代器

为了使迭代器更易于使用，新的标准库包 iter 定义了两种类型：Seq 和 Seq2。这些是迭代器函数类型的名称，是可以与for/range语句一起使用的类型。Seq的名称是sequence（序列）的缩写，因为迭代器按顺序循环遍历一系列值。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` package iter  type Seq[V any] func(yield func(V) bool)  type Seq2[K, V any] func(yield func(K, V) bool)  // 现在，没有Seq0 ``` |

Seq 和 Seq2 之间的区别只是 Seq2 是一对序列，比如来自 map 的键和值。在这篇文章中，为了简单起见，我们将专注于 Seq，但我们所说的大部分也适用于 Seq2。

最容易通过一个例子来解释迭代器是如何工作的。这里 Set 方法 All 返回一个函数。

All 的返回类型是 iter.Seq[E]，所以我们知道它返回一个迭代器。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` // All 是对s中元素的迭代器。 func (s *Set[E]) All() iter.Seq[E] {     return func(yield func(E) bool) {         for v := range s.m {             if !yield(v) {                 return             }         }     } } ``` |

迭代器函数本身接受另一个函数作为参数，即 yield 函数。迭代器用集合中的每个值调用 yield 函数。在这个例子中，迭代器，由 Set.All 返回的函数，与我们之前看到的 Set.Push 函数非常相似。

这就是迭代器的工作原理：对于某些值序列，它们用序列中的每个值调用 yield 函数。如果 yield 函数返回 false，则不再需要更多的值，迭代器可以简单地返回，执行可能需要的任何清理工作。如果 yield 函数从不返回 false，则迭代器可以在用序列中的所有值调用 yield 之后简单地返回。

这就是它们的工作原理，但让我们承认，当你第一次看到这些时，你的第一反应可能是“这里有很多函数在飞来飞去。”你对此的看法并没有错。让我们关注两件事。

第一，一旦你越过这个函数代码的第一行，这个迭代器的实际实现实际上非常简单：用集合中的每个元素调用 yield，如果 yield 返回 false 则停止。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` for v := range s.m {     if !yield(v) {         return     } } ``` |

第二，使用这个真的很容易。你调用 s.All 来获取一个迭代器，然后你使用 for/range 来循环遍历s中的所有元素。for/range 语句支持任何迭代器。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` func PrintAllElements[E comparable](s *Set[E]) {     for v := range s.All() {         fmt.Println(v)     } } ``` |

在这种代码中，s.All 是一个返回函数的方法。我们调用 s.All，然后使用 for/range 来遍历它返回的函数。在这种情况下，我们可以将 Set.All 做成一个迭代器函数本身，而不是让它返回一个迭代器函数。然而，在某些情况下，这行不通，比如如果返回迭代器的函数需要接受一个参数，或者需要做一些设置工作。作为一种惯例，我们鼓励所有容器类型都提供一个返回迭代器的 All 方法，这样程序员就不必记住是直接遍历 All 还是调用 All 来获取一个可以遍历的值。他们总是可以做后者。

如果你仔细想想，你会看到编译器必须调整循环以创建一个 yield 函数传递给 s.All 返回的迭代器。在 Go 编译器和运行时有一些复杂性，使这变得高效，并正确处理像循环中的 break 或 panic 这样的事情。我们不会在这篇博客文章中涵盖这些内容。幸运的是，当涉及到实际使用这个特性时，实现细节并不重要。

## 拉取迭代器

现在我们已经看到了如何在 for/range 循环中使用迭代器。但一个简单的循环并不是使用迭代器的唯一方式。例如，有时我们可能需要并行地遍历两个容器。我们该怎么做呢？

答案是我们使用一种不同类型的迭代器：拉取迭代器。我们已经看到，一个标准迭代器，也称为推送迭代器，是一个接受 yield 函数作为参数的函数，并通过调用 yield 函数推送序列中的每个值。

拉取迭代器的工作方式正好相反：它是一个这样的函数，每次你调用它时，它都会从序列中拉取下一个值并返回它。

我们将重复两种迭代器之间的区别，以帮助你记住：

一个推送迭代器将序列中的每个值推送到yield函数。推送迭代器是 Go 标准库中的迭代器，并且直接被 for/range语句支持。
一个拉取迭代器的工作方式正好相反。每次你调用一个拉取迭代器时，它都会从...