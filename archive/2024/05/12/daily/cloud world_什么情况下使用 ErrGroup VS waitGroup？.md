---
title: 什么情况下使用 ErrGroup VS waitGroup？
url: https://cloudsjhan.github.io/2024/05/11/%E4%BB%80%E4%B9%88%E6%83%85%E5%86%B5%E4%B8%8B%E4%BD%BF%E7%94%A8-ErrGroup-VS-waitGroup%EF%BC%9F/
source: cloud world
date: 2024-05-12
fetch_date: 2025-10-06T17:16:13.629358
---

# 什么情况下使用 ErrGroup VS waitGroup？

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 什么情况下使用 ErrGroup VS waitGroup？

posted

2024-05-11

|

in

[Go](/categories/Go/)

|

visitors:

|

|

wordcount:

832
|

min2read ≈

4

什么情况下使用 ErrGroup VS waitGroup？

![](https://)

Goroutine 是编写 Go 语言并发程序的强大工具。然而管理协程，特别是在处理协程的错误时，可能会变得繁琐。这时，x/sync 包中的 errgroup 就派上用场了。它提供了一种简化的方法来处理并发任务及其错误。

### Example for ErrGroup

下面是一个使用 errorGroup 的例子：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 ``` | ``` package main  import (  "context"  "errors"  "fmt"  "time"   "golang.org/x/sync/errgroup" )  func task1(ctx context.Context) error {  fmt.Println("Task 1 started successfully")  select {  case <-time.After(1 * time.Second):   fmt.Println("Task 1 completed successfully")   return nil  case <-ctx.Done():   fmt.Println("Task 1 canceled")   return ctx.Err()  } }  func task2(ctx context.Context) error {  fmt.Println("Task 2 started successfully")  select {  case <-time.After(2 * time.Second):   fmt.Println("Task 2 processed failed")   return errors.New("Task 2 processed failed due to error")  case <-ctx.Done():   fmt.Println("Task 2 canceled")   return ctx.Err()  } }  func task3(ctx context.Context) error {  fmt.Println("Task 3 started successfully")  select {  case <-time.After(3 * time.Second):   fmt.Println("Task 3 completed successfully")   return nil  case <-ctx.Done():   fmt.Println("Task 3 canceled")   return ctx.Err()  } }  func main() {  ctx, cancel := context.WithCancel(context.Background())  defer cancel() // Ensure cancellation happens when main() exits   g, ctx := errgroup.WithContext(ctx)   g.Go(func() error {   return task1(ctx)  })   g.Go(func() error {   return task2(ctx)  })   g.Go(func() error {   return task3(ctx)  })   if err := g.Wait(); err != nil {   fmt.Println("Encountered error:", err)   cancel()  } else {   fmt.Println("All tasks completed successfully")  } } ``` |

上面程序的输出是：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` Task 1 started successfully Task 2 started successfully Task 3 started successfully Task 1 completed successfully Task 2 processed failed Encountered error: Task 2 processed failed due to error ``` |

在这个例子中：

* 我们创建了一个带有可取消上下文的 `errgroup`。
* 定义了3个任务，task1 和 task3 在一定时间后模拟成功完成，而 task2 在更长的时间后通过返回错误来模拟失败。
* 使用 g.Go 在单独的 goroutine 中启动每个任务。
* 调用 g.Wait 等待所有任务完成。如果任何任务遇到错误，g.Wait() 会立即返回该错误。
  在主执行之后，task1 成功完成，task2 遇到了处理失败，而 task3 由于 task2 中的上述失败而被取消。

### ErrGroup vs WaitGroup

#### ErrGroup:

* 使用 ErrGroup 来管理并发任务中的错误。它聚合了所有协程中的错误，并返回遇到的第一个错误。
* 需要管理多个可能产生错误的并发任务。
* 想要利用上下文取消功能来优雅地关闭程序。
* 不想手动检查多个 WaitGroup 调用的错误
* 它与 Go 的上下文包无缝集成。任何来自协程的错误都会取消上下文，自动停止其他正在运行的任务。

#### WaitGroup

* 使用 WaitGroup 进行基本同步。它简单地等待指定数量的 goroutine 完成后再继续。
* ]当你只关心任务完成而不预期错误时，它是理想的选择。
* 它不直接处理错误。你需要在每个 goroutine 中检查错误并单独处理它们。

### 总结

* 使用 WaitGroup 进行简单的同步
* 使用 ErrGroup 进行错误管理，并希望在优雅关闭时有上下文感知的取消。
* 也可以同时使用它们，WaitGroup 用于基本同步，ErrGroup 用于一组任务中的详细错误处理。

相关的 [issue](https://github.com/golang/go/issues/23595 "x/sync/errgroup: get all errors")

---

-------------The End-------------

Title:[什么情况下使用 ErrGroup VS waitGroup？](/2024/05/11/%E4%BB%80%E4%B9%88%E6%83%85%E5%86%B5%E4%B8%8B%E4%BD%BF%E7%94%A8-ErrGroup-VS-waitGroup%EF%BC%9F/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年05月11日 - 20:05

Last Update:2024年05月11日 - 20:05

Original Link:[https://cloudsjhan.github.io/2024/05/11/什么情况下使用-ErrGroup-VS-waitGroup？/](/2024/05/11/%E4%BB%80%E4%B9%88%E6%83%85%E5%86%B5%E4%B8%8B%E4%BD%BF%E7%94%A8-ErrGroup-VS-waitGroup%EF%BC%9F/ "什么情况下使用 ErrGroup VS waitGroup？")

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

[Golang 实现枚举的各种方法及最佳实践](/2024/05/07/Golang-%E5%AE%9E%E7%8E%B0%E6%9E%9A%E4%B8%BE%E7%9A%84%E5%90%84%E7%A7%8D%E6%96%B9%E6%B3%95%E5%8F%8A%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/ "Golang 实现枚举的各种方法及最佳实践")

[Observability with OpenTelemetry and Go](/2024/05/13/Observability-with-OpenTelemetry-and-Go/ "Observability with OpenTelemetry and Go")

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

1. [1. Example for ErrGroup](#Example-for-ErrGroup)
2. [2. ErrGroup vs WaitGroup](#ErrGroup-vs-WaitGroup)
   1. [2.1. ErrGroup:](#ErrGroup)
   2. [2.2. WaitGroup](#WaitGroup)
3. [3. 总结](#总结)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;