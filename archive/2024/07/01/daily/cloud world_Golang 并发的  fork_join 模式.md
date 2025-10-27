---
title: Golang 并发的  fork/join 模式
url: https://cloudsjhan.github.io/2024/06/30/Golang-%E5%B9%B6%E5%8F%91%E7%9A%84-fork-join-%E6%A8%A1%E5%BC%8F/
source: cloud world
date: 2024-07-01
fetch_date: 2025-10-06T17:40:58.308922
---

# Golang 并发的  fork/join 模式

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## Golang 并发的 fork/join 模式

posted

2024-06-30

|

in

[Go](/categories/Go/)

|

visitors:

|

|

wordcount:

841
|

min2read ≈

4

Golang 并发的 fork/join 模式

![](https://)

在软件开发领域，对更快、更高效地处理数据的需求与日俱增。并行计算技术（如 fork/join 模式）为利用多个 CPU 内核并发执行任务提供了强大的解决方案，从而大大缩短了大规模计算的执行时间。本文通过分解一个使用并发 goroutines 对数组求和的示例，探讨了 fork/join 模式在 Go 中的实现。

### Fork/Join 并发模型介绍

Fork/Join 模式是一种并行技术，包括将任务分成较小的任务块，并行处理这些任务块（分叉），然后将这些任务的结果合并为最终结果（join）。这种模式尤其适用于任务相互独立，可以并发执行而互不影响的情况。

![](https://files.mdnice.com/user/4760/2ec02bb0-0c46-4df3-93d3-352a98e436ab.png)

### 简单的示例：并发对数组求和

#### 1. 初始化：程序初始化一个整数数组。程序还设置了数组应划分的部分数，每个部分由一个独立的程序处理。

#### 2.并发设置：

2.1 Fork: 将数组划分为指定的部分，并为每个部分启动一个 goroutine 来计算该部分的总和。

2.2 Channel 通信：每个 “程序 “都会通过通道将计算出的总和发送回主进程，以确保同步通信。

2.3 Join: 当所有 Goroutine 完成计算后，主进程收集并汇总这些部分结果，得出总和。
2.4 Logging: 日志记录在整个过程中，程序会打印信息，显示数组的划分、每个工作者计算的总和以及收到的部分总和。

### 代码示例

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 ``` | ``` import (  "fmt"  "sync" )  var (  parts = 4 )  func main() {  numbers := []int{3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5} // Example array  totalSum := concurrentSum(numbers, parts)         // Divide the array into 4 parts for summing  fmt.Println("Total Sum:", totalSum) }  // sumPart sums a part of the array and sends the result to a channel. func sumPart(workerId int, nums []int, result chan<- int, wg *sync.WaitGroup) {  defer wg.Done() // Ensure the WaitGroup counter decrements on function completion.  sum := 0  for _, num := range nums {   sum += num  }  fmt.Printf("Worker %d calculated sum: %d\n", workerId, sum)  result <- sum // Send the partial sum to the result channel. }  // concurrentSum takes an array and the number of parts to divide it into, // then sums the array elements using concurrent goroutines. func concurrentSum(numbers []int, parts int) int {  n := len(numbers)  partSize := n / parts // Determine the size of each subarray  fmt.Printf("Dividing the array of size %d into %d parts of size %d\n", n,    parts, partSize)  results := make(chan int, parts) // Channel to collect results with a buffer size   var wg sync.WaitGroup  // Fork step: Launch a goroutine for each part of the array  for i := 0; i < parts; i++ {   start := i * partSize   end := start + partSize   if i == parts-1 { // Ensure the last goroutine covers the remainder of the array    end = n   }   wg.Add(1)   go sumPart(i, numbers[start:end], results, &wg)  }   // Close the results channel once all goroutines are done  go func() {   wg.Wait()   close(results)  }()   // Join step: Combine results  totalSum := 0  for sum := range results {   fmt.Printf("Received partial sum: %d\n", sum)   totalSum += sum  }   return totalSum } ``` |

![](https://files.mdnice.com/user/4760/2b012de1-3e54-4e2b-88ad-28c485cdd20d.png)

### 结论

上面的示例展示了使用 Go 进行并发编程时 fork/join 模式的效率。通过将数组求和的任务分给多个 Worker，程序在多核处理器上的运行速度明显加快，使用 Go 进行并发编程任务具有的强大功能和简便性。这种模式同样可应用于其他各种计算问题。

---

-------------The End-------------

Title:[Golang 并发的 fork/join 模式](/2024/06/30/Golang-%E5%B9%B6%E5%8F%91%E7%9A%84-fork-join-%E6%A8%A1%E5%BC%8F/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年06月30日 - 11:06

Last Update:2024年06月30日 - 11:06

Original Link:[https://cloudsjhan.github.io/2024/06/30/Golang-并发的-fork-join-模式/](/2024/06/30/Golang-%E5%B9%B6%E5%8F%91%E7%9A%84-fork-join-%E6%A8%A1%E5%BC%8F/ "Golang 并发的  fork/join 模式")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

![cloud sjhan 支付宝](/images/alipay.jpg)

[Go](/tags/Go/)

(>给这篇博客打个分吧<)

[Go 1.22 提供的更加强大的 Tracing 能力](/2024/06/21/Go-1-22-%E6%8F%90%E4%BE%9B%E7%9A%84%E6%9B%B4%E5%8A%A0%E5%BC%BA%E5%A4%A7%E7%9A%84-Tracing-%E8%83%BD%E5%8A%9B/ "Go 1.22 提供的更加强大的 Tracing 能力")

[构建并运行 eBPF 应用 - Part one](/2024/07/14/%E6%9E%84%E5%BB%BA%E5%B9%B6%E8%BF%90%E8%A1%8C-eBPF-%E5%BA%94%E7%94%A8-Part-one/ "构建并运行 eBPF 应用 - Part one")

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

1. [1. Fork/Join 并发模型介绍](#Fork-Join-并发模型介绍)
2. [2. 简单的示例：并发对数组求和](#简单的示例：并发对数组求和)
   1. [2.1. 1. 初始化：程序初始化一个整数数组。程序还设置了数组应划分的部分数，每个部分由一个独立的程序处理。](#1-初始化：程序初始化一个整数数组。程序还设置了数组应划分的部分数，每个部分由一个独立的程序处理。)
   2. [2.2. 2.并发设置：](#2-并发设置：)
3. [3. 代码示例](#代码示例)
4. [4. 结论](#结论)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;