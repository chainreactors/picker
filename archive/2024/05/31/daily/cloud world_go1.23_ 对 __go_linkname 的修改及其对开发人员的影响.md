---
title: go1.23: 对 //go:linkname 的修改及其对开发人员的影响
url: https://cloudsjhan.github.io/2024/05/30/go1-23-%E5%AF%B9-go-linkname-%E7%9A%84%E4%BF%AE%E6%94%B9%E5%8F%8A%E5%85%B6%E5%AF%B9%E5%BC%80%E5%8F%91%E4%BA%BA%E5%91%98%E7%9A%84%E5%BD%B1%E5%93%8D/
source: cloud world
date: 2024-05-31
fetch_date: 2025-10-06T16:50:44.431703
---

# go1.23: 对 //go:linkname 的修改及其对开发人员的影响

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## go1.23: 对 //go:linkname 的修改及其对开发人员的影响

posted

2024-05-30

|

in

[Go](/categories/Go/)

|

visitors:

|

|

wordcount:

991
|

min2read ≈

4

![](https://)

上周，Go 1.23 进入冻结期，这意味着不会添加任何新功能，已经添加的功能也不太可能被删除。今天，我们将讨论 Go 1.23 中 //go:linkname 指令的变化。
相关的 issue 是：[cmd/link: lock down future uses of linkname · Issue #67401 · golang/go](https://github.com/golang/go/issues/67401 "linkname issue")

> 注：//go:linkname 指令不是官方推荐使用的指令，不能保证向前或向后的兼容性。明智的做法是尽可能避免使用该指令。

有鉴于此，让我们深入了解这些新变化。

### linkname 的作用是什么

简单来说，链接名指令用于向编译器和链接器传递信息。根据使用情况，可将其分为三类：

#### 1. Pull

`pull` 的用法是：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` import _ "unsafe" // Required to use linkname  ​  import _ "fmt" // The pulled package must be explicitly imported (except the runtime package)  ​  //go:linkname my_func fmt.Println  func my_func(...any) (n int, err error) ``` |

该指令格式为 //go:linkname <本地函数或包级变量> <本包或其他包中完全定义的函数或变量>。它告诉编译器和链接器 my\_func 应直接使用 fmt.Println，使 my\_func 成为 fmt.Println 的别名。

这种用法可以忽略函数或变量是否被导出，甚至可以使用包私有元素。不过，这种方法有风险，如果出现类型不匹配，可能会引起 panic。

#### 2. Push

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` import _ "unsafe" // Required to use linkname  ​  //go:linkname main.fastHandle  func fastHandle(input io.Writer) error {  ...  }  ​  // package main  func fastHandle(input io.Writer) error  ​  // The main package can directly use fastHandle ``` |

在这里，只需将函数或变量名作为第一个参数传递给指令，并指定使用该函数或变量的软件包名称。这种用法表示函数或变量将被命名为 xxx.yyy。

#### 3. HandShake

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ```  package mypkg  ​  import _ "unsafe" // Required to use linkname  ​  //go:linkname fastHandle  func fastHandle(input io.Writer) error {  ...  }  ​  package main  ​  import _ "unsafe" // Required to use linkname  ​  //go:linkname fastHandle mypkg.fastHandle  func fastHandle(input io.Writer) error ``` |

这种用法意味着两端要握手，明确标记哪个函数或变量应被链接。

### 使用 linkname 的风险

主要风险是在软件包不知情的情况下使用软件包私有函数或变量的能力。 例如：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` // pkg/mymath/mymath.go  package mymath  ​  func uintPow(n uint) uint {      return n * n  }  ​  // main.go  package main  ​  import (      "fmt"      _ "linkname/pkg/mymath"      _ "unsafe"  )  ​  //go:linkname pow linkname/pkg/mymath.uintPow  func pow(n uint) uint  ​  func main() {      fmt.Println(pow(6)) // 36  } ``` |

通常，uintPow 不应在其软件包之外被访问。但 linkname 绕过了这一限制，可能导致严重的类型相关内存错误或运行时 panic。

### linkname 也有有用的时候

尽管存在风险，但 linkname 的存在还是有其合理的原因，例如在 Go 程序启动时。例如，在 Go 的运行时：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` // runtime/proc.go  ​  //go:linkname main_main main.main  func main_main()  ​  // runtime.main  func main() {      fn := main_main      fn()  } ``` |

这里，linkname 允许运行时调用用户定义的主函数。

### Go 1.23 中对 linkname 的更改

考虑到上述风险，Go 核心团队决定限制链接名的使用：

* 新的标准库软件包将禁止 linkname。
* 新增了一个 ldflag -checklinkname=1 来执行限制。默认值为 0，但在 1.23 的最终版本中将设置为 1。
* 标准库将禁止只拉链接名，只允许握手模式。

例如，以下代码在 1.23 版中就无法编译：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` package main  import _ "unsafe"  //go:linkname corostart runtime.corostart  func corostart()  ​  func main() {      corostart()  } ``` |

### linkname 的未来

长期目标是只允许使用握手模式。作为开发者，我们应该:

* 使用 -checklinkname=1 审核并删除不必要的链接名使用。
* 建议在必要时公开私有 API。
* 最后，使用 -ldflags=-checklinkname=0 禁用限制。

### 总结

总之，我们还是应避免使用 `//go:linkname` 以防止出现不可预见的问题。

---

-------------The End-------------

Title:[go1.23: 对 //go:linkname 的修改及其对开发人员的影响](/2024/05/30/go1-23-%E5%AF%B9-go-linkname-%E7%9A%84%E4%BF%AE%E6%94%B9%E5%8F%8A%E5%85%B6%E5%AF%B9%E5%BC%80%E5%8F%91%E4%BA%BA%E5%91%98%E7%9A%84%E5%BD%B1%E5%93%8D/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年05月30日 - 16:05

Last Update:2024年05月30日 - 16:05

Original Link:[https://cloudsjhan.github.io/2024/05/30/go1-23-对-go-linkname-的修改及其对开发人员的影响/](/2024/05/30/go1-23-%E5%AF%B9-go-linkname-%E7%9A%84%E4%BF%AE%E6%94%B9%E5%8F%8A%E5%85%B6%E5%AF%B9%E5%BC%80%E5%8F%91%E4%BA%BA%E5%91%98%E7%9A%84%E5%BD%B1%E5%93%8D/ "go1.23: 对 //go:linkname 的修改及其对开发人员的影响")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

微信支付

![cloud sjhan 支付宝](/images/alipay.jpg)

支付宝

[Go](/tags/Go/)

(>给这篇博客打个分吧<)

[掌握 Golang Mutex：安全并发的最佳实践](/2024/05/29/%E6%8E%8C%E6%8F%A1-Golang-Mutex%EF%BC%9A%E5%AE%89%E5%85%A8%E5%B9%B6%E5%8F%91%E7%9A%84%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/ "掌握 Golang Mutex：安全并发的最佳实践")

[如何用 golang 从 OpenAI,Ollama 和 Claude 获取可靠的结构化输出?](/2024/06/03/%E5%A6%82%E4%BD%95%E7%94%A8-golang-%E4%BB%8E-OpenAI-Ollama-%E5%92%8C-Claude-%E8%8E%B7%E5%8F%96%E5%8F%AF%E9%9D%A0%E7%9A%84%E7%BB%93%E6%9E%84%E5%8C%96%E8%BE%93%E5%87%BA/ "如何用 golang 从 OpenAI,Ollama 和 Claude 获取可靠的结构化输出?")

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

1. [1. linkname 的作用是什么](#linkname-的作用是什么)
   1. [1.1. 1. Pull](#1-Pull)
   2. [1.2. 2. Push](#2-Push)
   3. [1.3. 3. HandShake](#3-HandShake)
2. [2. 使用 linkname 的风险](#使用-linkname-的风险)
3. [3. linkname 也有有用的时候](#linkname-也有有用的时候)
4. [4. Go 1.23 中对 linkname 的更改](#Go-1-23-中对-linkname-的更改)
5. [5. linkname 的未来](#linkname-的未来)
6. [6. 总结](#总结)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;