---
title: 探索 Goja：Golang 中的 JavaScript 运行时
url: https://cloudsjhan.github.io/2024/09/11/%E6%8E%A2%E7%B4%A2-Goja%EF%BC%9AGolang-%E4%B8%AD%E7%9A%84-JavaScript-%E8%BF%90%E8%A1%8C%E6%97%B6/
source: cloud world
date: 2024-09-12
fetch_date: 2025-10-06T18:25:35.660686
---

# 探索 Goja：Golang 中的 JavaScript 运行时

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 探索 Goja：Golang 中的 JavaScript 运行时

posted

2024-09-11

|

in

[Go](/categories/Go/)

|

visitors:

|

|

wordcount:

2,241
|

min2read ≈

9

![](https://)

# 探索 Goja：Golang 中的 JavaScript 运行时

![](https://files.mdnice.com/user/4760/91540ba6-dbc5-4474-b236-bf62483142ed.png)

这篇文章探讨了 [Goja](https://github.com/dop251/goja "goja")，这是 Golang 生态系统中的一个 JavaScript 运行时库。Goja 作为一个在 Go 应用程序中嵌入 JavaScript 的强大工具，提供了独特的优势，尤其是在操作数据和提供不需要 go build 过程中的 SDK。

## 背景：Goja 的需求

在我的项目中，我在查询和操作大型数据集时遇到了挑战。最初，一切都是用 Go 编写的，这在效率上是有利的，但在处理复杂的 JSON 响应时变得笨拙。虽然 Go 的极简主义方法通常是一个优势，但特定任务所需的冗长性减慢了我的速度。

使用嵌入式脚本语言可以简化这个过程，这让我探索了各种选项。Lua 是我的首选，因为它以轻量级和可嵌入而闻名。但我很快发现，Go 中的 Lua 库在实现、版本（5.1、5.2 等）和活跃支持方面参差不齐。

然后我调查了 Go 生态系统中其他流行的脚本语言。我考虑了 [Expr](https://github.com/expr-lang/expr/ "expr")、[V8](https://github.com/tommie/v8go "v8") 和 [Starlark](https://github.com/google/starlark-go "starlark-go") 等选项，但最终 Goja 成为了最有希望的候选者。

这里是我在这些库上进行基准测试的 [GitHub 仓库](https://github.com/jtarchie/benchmark-tests/blob/22789057b4fcf95443ea8cb61f261dea31935cda/eval_benchmark_test.go "test repo")，测试了它们的性能和与 Go 的集成便利性。

## 为什么选择 Goja？

Goja 因其与 Go 结构体的无缝集成而赢得了我的青睐。当你将一个 Go 结构体分配给 JavaScript 运行时中的一个值时，Goja 会自动推断字段和方法，使它们在 JavaScript 中可访问，而不需要单独的桥接层。它利用 Go 的反射能力来调用这些字段上的 getter 和 setter，提供了 Go 和 JavaScript 之间强大而透明的交互。

让我们通过一些示例来看看 Goja 的实际应用。这些示例突出了我发现有用的特性，但我希望在文档中有更多示例。

## 赋值和返回值

首先，让我们来看一个简单的例子，我们将一个从 1 到 100 的整数数组从 Go 传递到 JavaScript 运行时，并过滤出偶数值。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``` | ``` package main  import ( 	"fmt"  	"github.com/dop251/goja" )  func main() { 	vm := goja.New()  	// 从 1 到 100 传递一个整数数组 	values := []int{} 	for i := 1; i <= 100; i++ { 		values = append(values, i) 	}  	// 定义 JavaScript 代码以过滤偶数值 	script := ` 		values.filter((x) => { 			return x % 2 === 0; 		})   `  	// 在 JavaScript 运行时中设置数组 	vm.Set("values", values)  	// 运行脚本 	result, err := vm.RunString(script) 	if err != nil { 		panic(err) 	}  	// 将结果转换回 Go 的空接口切片 	filteredValues := result.Export().([]interface{})  	fmt.Println(filteredValues) 	// 输出：[2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100]  	first := filteredValues[0].(int64) 	fmt.Println(first) } ``` |

在这个例子中，你可以看到在 Goja 中遍历数组不需要显式类型注释。Goja 能够根据内容推断数组的类型，这得益于 Go 的反射机制。在过滤值并返回结果时，Goja 将结果转换回空接口切片（[]interface{}）。这是因为 Goja 需要在 Go 的静态类型系统中处理 JavaScript 的动态类型。

如果你需要在 Go 中处理结果值，你将不得不执行类型断言以提取整数。在内部，Goja 将所有整数表示为 int64。

## 结构体和方法调用

接下来，让我们探索 Goja 如何处理 Go 结构体，特别关注方法和导出字段。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 ``` | ``` package main  import (     "fmt"     "github.com/dop251/goja" )  type Person struct {     Name string     age  int }  // 获取年龄的方法（未导出） func (p *Person) GetAge() int {     return p.age }  func main() {     vm := goja.New()      // 创建一个新的 Person 实例     person := &Person{         Name: "John Doe",         age:  30,     }      // 在 JavaScript 运行时中设置 Person 结构体     vm.Set("person", person)      // JavaScript 代码以访问结构体的字段和方法     script := `         const name = person.Name;    // 访问导出字段         const age = person.GetAge(); // 通过 getter 访问未导出字段         name + " is " + age + " years old.";     `      result, err := vm.RunString(script)     if err != nil {         panic(err)     }      fmt.Println(result.String()) // 输出：John Doe is 30 years old. } ``` |

在这个例子中，我定义了一个 Person 结构体，它有一个导出的 Name 字段和一个未导出的 age 字段。GetName 方法是导出的。当从 JavaScript 访问这些字段和方法时，Goja 遵循结构体上的命名约定。方法 GetAge 被访问为 GetName。

有一个模式是通过 [FieldNameMapper](https://pkg.go.dev/github.com/dop251/goja#FieldNameMapper "FieldNameMapper") 将 JavaScript 命名约定的小驼峰式转换为 Golang 命名约定。这允许 Go 方法 GetAge 在 JavaScript 调用中被调用为 getAge。

## 异常处理

当 JavaScript 中发生异常时，Goja 使用标准的 Go 错误处理来管理它。让我们探索一个运行时异常的例子——除以零。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` | ``` package main  import ( 	"errors" 	"fmt"  	"github.com/dop251/goja" )  // 触发除以零错误的 JavaScript 代码 const script = ` 	// 在 JavaScript 中使用 BigInt 表示法 	const a = 1n / 0n; `  func main() { 	vm := goja.New()  	// 执行 JavaScript 代码 	_, err := vm.RunString(script)  	// 处理发生的任何错误 	var exception *goja.Exception 	if errors.As(err, &exception) { 		fmt.Printf("JavaScript error: %s\n", exception.Error()) 		// 输出：JavaScript error: RangeError: Division by zero at <eval>:1:1(3) 	} else if err != nil { 		// 处理其他类型的错误（如果有） 		fmt.Printf("Error: %s\n", err.Error()) 	} } ``` |

返回的错误值是 \*goja.Exception 类型，它提供了有关引发 JavaScript 异常的信息以及失败的位置。虽然我没有强烈的需求去检查这些错误之外的记录它们到像 New Relic 或 DataDog 这样的服务，但 Goja 确实提供了这样做的工具，如果需要的话。

此外，Goja 可以引发其他类型的异常，如 *goja.StackOverflowError、*goja.InterruptedError 和 \*goja.CompilerSyntaxError，这些异常对应于解释器的特定问题。这些异常在处理执行 JavaScript 代码的客户端时，有助于处理和报告，特别是。

## 使用 VM 池沙箱用户代码

在开发我的应用程序时，我注意到初始化 VM 需要相当长的时间。每个 VM 都需要在运行时对用户可用的全局模块。Go 提供了 sync.Pool 来帮助重用对象，这非常适合我的情况，避免了沉重的初始化开销。

下面是一个 Goja VM 池的例子：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``` | ``` package main  import ( 	"fmt" 	"sync"  	"github.com/dop251/goja" )  var vmPool = sync.Pool{ 	New: func() interface{} { 		vm := goja.New()  		// 在每个 VM 中定义全局函数 		vm.Set("add", func(a, b int) int { 			return a + b 		})  		// ... 设置其他全局值 ...  		return vm 	}, }  func main() { 	vm := vmPool.Get().(*goja.Runtime) 	// 将 VM 放回池中重用 	defer vmPool.Put(vm)  	script := ` 		const result = add(5, 10); 		result; 	`  	value, err := vm.RunString(script) 	if err != nil { 		panic(err) 	}  	fmt.Println("Result:", value.Export()) 	// 结果：15 } ``` |

由于 [sync.Pool](https://pkg.go.dev/sync#Pool "sync.pool docs") 有详细的文档，让我们专注于 JavaScript 运行时。在这个例子中，用户声明了一个变量 result，它的值被返回。然而，我们遇到了一个限制：VM 不能像现在这样重用。

全局命名空间已经被变量 result 污染了。如果我用同一个池重新运行相同的代码，我会收到以下错误：SyntaxError: Identifier ‘result’ has already been declared at :1:1(0)。有一个 GitHub 问题推荐每次清除 result 的值。然而，我发现这种模式由于在处理用户提供的代码时增加的复杂性而不切实际。

到目前为止，我给出的例子都是预定义代码的演示。然而，我的应用程序允许用户在 Goja 运行时中提供自己的代码。这需要一些实验、探索和采用模式来避免“已经声明”的错误。

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` value, err := vm.RunString("(function() {" + userCode + "})()") if err != nil { 	panic(err) } ``` |

沙箱用户代码的最终解决方案涉及在它自己的范围内执行 userCode 在一个匿名函数中。由于函数没有命名，它没有被全局分配，因此不需要清理。经过一些基准测试后，我确认垃圾收集有效地清理了它。

## 结论

我们已经解锁了一种灵活高效的方式来处理复杂的脚本任务，而不会牺牲性能。这种方法大大减少了在繁琐任务上花费的时间，让你有更多的时间专注于其他重要的方面，并通过提供无缝和响应迅速的脚本环境来增强整体用户体验。

---

-------------The End-------------

Title: [探索 Goja：Golang 中的 JavaScript 运行时](/2024/09/11/%E6%8E%A2%E7%B4%A2-Goja%EF%BC%9AGolang-%E4%B8%AD%E7%9A%84-JavaScript-%E8%BF%90%E8%A1%8C%E6%97%B6/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年09月11日 - 11:09

Last Update:2024年09月11日 - 11:09

Original Link:[https://cloudsjhan.github.io/2024/09/11/探索-Goja：Golang-中的-JavaScript-运行时/](/2024/09/11/%E6%8E%A2%E7%B4%A2-Goja%EF%BC%9AGolang-%E4%B8%AD%E7%9A%84-JavaScript-%E8%BF%90%E8%A1%8C%E6%97%B6/ " 探索 Goja：Golang 中的 JavaScript 运行时")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

![cloud sjhan 支付宝](/images/alipay.jpg)

支付宝

[Go](/tags/Go/)

(>给这篇博客打个分吧<)

[在Go 1.23 及更高版本中使用 Telemetry](/2024/09/08/%E5%9C%A8Go-1-23-%E5%8F%8A%E6%9B%B4%E9%AB%98%E7%89%88%E6%9C%AC%E4%B8%AD%E4%BD%BF%E7%94%A8-Telemetry/ "在Go 1.23 及更高版本中使用 Telemetry")

[构建由大型语言模型（LLM）驱动的 Go 应用程序](/2024/09/14/%E6%9E%84%E5%BB%BA%E7%94%B1%E5%A4%A7%E5%9E%8B%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%EF%BC%88LLM%EF%BC%89%E9%A9%B1%E5%8A%A8%E7%9A%84-Go-%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F/ "构建由大型语言模型（LLM）驱动的 Go 应用程序")

* Conte...