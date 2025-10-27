---
title: 担心你的 Golang 程序内存泄露？看这一篇就够了！
url: https://cloudsjhan.github.io/2024/10/07/%E6%8B%85%E5%BF%83%E4%BD%A0%E7%9A%84-Golang-%E7%A8%8B%E5%BA%8F%E5%86%85%E5%AD%98%E6%B3%84%E9%9C%B2%EF%BC%9F%E7%9C%8B%E8%BF%99%E4%B8%80%E7%AF%87%E5%B0%B1%E5%A4%9F%E4%BA%86%EF%BC%81/
source: cloud world
date: 2024-10-08
fetch_date: 2025-10-06T18:50:52.529268
---

# 担心你的 Golang 程序内存泄露？看这一篇就够了！

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 担心你的 Golang 程序内存泄露？看这一篇就够了！

posted

2024-10-07

|

in

[Go](/categories/Go/)

|

visitors:

|

|

wordcount:

1,497
|

min2read ≈

7

![](https://)

本文介绍内存泄漏的常见原因以及如何避免。
无论使用哪种编程语言，内存泄漏都是一个常见问题。本文将说明可能发生内存泄漏的几种情况，让我们学习如何通过研究这些反模式来避免内存泄漏。

### 未关闭已打开的文件

结束打开文件时，应始终调用其关闭方法。否则可能会导致文件描述符数量达到上限，从而无法打开新文件或连接。这可能会导致 “too many open files”错误。

代码示例 1：不关闭文件导致文件描述符耗尽。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` func main() {       files := make([]*os.File, 0)       for i := 0; ; i++ {          file, err := os.OpenFile("test.log", os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0644)          if err != nil {             fmt.Printf("Error at file %d: %v\n", i, err)             break          } else {             _, _ = file.Write([]byte("Hello, World!"))             files = append(files, file)          }       }   } ``` |

输出：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` Error at file 61437: open test.log: too many open files ``` |

在我的 Mac 上，一个进程最多可以打开 61 440 个文件句柄。 Go 进程通常会打开三个文件描述符（stderr、stdout、stdin），因此最多只能打开 61437 个文件。可以手动调整这一限制。

### 未关闭 http.Response.Body

Go 有比较容易犯的错误，即忘记关闭 HTTP 请求的正文会导致内存泄漏。例如

代码示例 2：未关闭 HTTP 主体导致内存泄漏。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` func makeRequest() {       client := &http.Client{}       req, err := http.NewRequest(http.MethodGet, "http://localhost:8081", nil)       res, err := client.Do(req)       if err != nil {          fmt.Println(err)       }       _, err = ioutil.ReadAll(res.Body)       // defer res.Body.Close()       if err != nil {          fmt.Println(err)       }   } ``` |

### 字符串和切片内存泄漏

Go 规范没有明确说明子串是否与其原始字符串共享内存。不过，编译器允许这种行为，这通常是好事，因为它减少了内存和 CPU 的使用。但有时这会导致暂时的内存泄露。

代码示例 3：字符串导致的内存泄漏。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` | ``` func main() { 	Demo1() 	runtime.GC() 	time.Sleep(1 * time.Second) 	exit() } func exit() { 	fmt.Println("Saving heap profile...") 	// create a  heap profile 	f, err := os.Create("heap.pprof") 	if err != nil { 		log.Fatal("could not create heap profile: ", err) 	} 	runtime.GC() 	//time.Sleep(1 * time.Second) 	//  heap profile 	if err = pprof.WriteHeapProfile(f); err != nil { 		log.Fatal("could not write heap profile: ", err) 	} 	fmt.Println("Heap profile saved in heap.pprof") 	_ = f.Close() }  var packageStr1 []string  func Demo1() { 	for i := 0; i < 10; i++ { 		s := createStringWithLengthOnHeap(1 << 20) //1M 		packageStr1 = append(packageStr1, s[:50]) 	} }  func createStringWithLengthOnHeap(i int) string { 	s := make([]byte, i) 	for j := 0; j < i; j++ { 		s[j] = byte(j % 256 % (rand.Intn(256) + 1)) 	} 	return string(s) } ``` |

为了防止临时内存泄漏，我们可以使用 strings.Clone()。

代码示例 4：使用 strings.Clone() 避免临时内存泄漏。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` func Demo1() {       for i := 0; i < 10; i++ {          s := createStringWithLengthOnHeap(1 << 20) // 1MB          packageStr1 = append(packageStr1, strings.Clone(s[:50]))       }   } ``` |

### Goroutine Handler

大多数内存泄漏都是由于程序泄漏造成的。例如，下面的示例会迅速耗尽内存，导致 OOM（内存不足）错误。
代码示例 5：goroutine 处理程序泄漏。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` for {          go func() {             time.Sleep(1 * time.Hour)          }()       }   } ``` |

### 滥用 Channels

不正确地使用 channel 也很容易导致程序泄漏。对于无缓冲通道，在向通道写入数据之前，生产者和消费者都必须准备就绪，否则通道就会阻塞。在下面的示例中，函数提前退出，导致了程序泄漏。

代码示例 6：非缓冲通道滥用导致程序泄漏。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` func Example() {     a := 1     c := make(chan error)     go func() {         c <- err         return     }()     // Example exits here, causing a goroutine leak.     if a > 0 {         return     }     err := <-c } ``` |

只需将其改为缓冲通道即可解决这一问题： c := make(chan error, 1)

### 滥用 range with Channels

可以使用 range 遍历通道。但是，如果通道为空，range 将等待新数据，可能会阻塞 goroutine。

代码示例 7：滥用范围导致程序泄漏。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` func main() {       wg := &sync.WaitGroup{}       c := make(chan any, 1)       items := []int{1, 2, 3, 4, 5}       for _, i := range items {          wg.Add(1)          go func() {             c <- i          }()       }       go func() {          for data := range c {             fmt.Println(data)             wg.Done()          }          fmt.Println("close")       }()       wg.Wait()       time.Sleep(1 * time.Second)   } ``` |

要解决这个问题，请在调用 wg.Wait() 后关闭通道。

### 误用 `runtime.SetFinalizer`.

如果两个对象都使用 runtime.SetFinalizer 进行了设置，并且它们相互引用，那么即使它们不再使用，也不会被垃圾回收。

### time.Ticker

这是 Go 1.23 之前的一个问题。如果不调用 ticker.Stop()，可能会导致内存泄漏。Go 1.23 已[修复](https://go.dev/doc/go1.23#timer-changes "1.23 timer-changes")了这个问题。

### 滥用 defer

虽然使用延迟释放资源不会直接导致内存泄漏，但它会通过两种方式导致临时内存泄漏：

* 执行时间：延迟总是在函数结束时执行。如果函数运行时间过长或从未结束，则 defer 中的资源可能无法及时释放。
* 内存使用：每个延迟都会在内存中增加一个调用点。如果在循环内使用，可能会导致临时内存泄漏。

代码示例 8：延迟导致的临时内存泄漏。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` func ReadFile(files []string) {       for _, file := range files {         f, err := os.Open(file)         if err != nil {            fmt.Println(err)            return         }         // do something         defer f.Close()       }   } ``` |

这段代码会造成临时内存泄漏，并可能导致 “too many open files” 的错误。除非必要，否则应避免过度使用延迟。

## 结论

本文介绍了 Go 中可能导致内存泄漏的几种行为，其中最常见的是 goroutine 泄漏。通道的不当使用，尤其是选择和范围的不当使用，会增加检测泄漏的难度。当遇到内存泄漏时，pprof 可以帮助快速定位问题，确保我们编写出更健壮的代码。[References](https://go101.org/article/memory-leaking.html "memory-leaking")。

---

-------------The End-------------

Title:[担心你的 Golang 程序内存泄露？看这一篇就够了！](/2024/10/07/%E6%8B%85%E5%BF%83%E4%BD%A0%E7%9A%84-Golang-%E7%A8%8B%E5%BA%8F%E5%86%85%E5%AD%98%E6%B3%84%E9%9C%B2%EF%BC%9F%E7%9C%8B%E8%BF%99%E4%B8%80%E7%AF%87%E5%B0%B1%E5%A4%9F%E4%BA%86%EF%BC%81/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年10月07日 - 10:10

Last Update:2024年10月07日 - 10:10

Original Link:[https://cloudsjhan.github.io/2024/10/07/担心你的-Golang-程序内存泄露？看这一篇就够了！/](/2024/10/07/%E6%8B%85%E5%BF%83%E4%BD%A0%E7%9A%84-Golang-%E7%A8%8B%E5%BA%8F%E5%86%85%E5%AD%98%E6%B3%84%E9%9C%B2%EF%BC%9F%E7%9C%8B%E8%BF%99%E4%B8%80%E7%AF%87%E5%B0%B1%E5%A4%9F%E4%BA%86%EF%BC%81/ "担心你的 Golang 程序内存泄露？看这一篇就够了！")

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

[Varint 及其在 Golang 中的应用](/2024/09/29/Varint-%E5%8F%8A%E5%85%B6%E5%9C%A8-Golang-%E4%B8%AD%E7%9A%84%E5%BA%94%E7%94%A8/ "Varint 及其在 Golang 中的应用")

[Golang 常用的五种创建型设计模式](/2024/10/21/Golang-%E5%B8%B8%E7%94%A8%E7%9A%84%E4%BA%94%E7%A7%8D%E5%88%9B%E5%BB%BA%E5%9E%8B%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F/ "Golang 常用的五种创建型设计模式")

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

1. [1. 未关闭已打开的文件](#未关闭已打开的文件)
2. [2. 未关闭 http.Response.Body](#未关闭-http-Response-Body)
3. [3. 字符串和切片内存泄漏](#字符串和切片内存泄漏)
4. [4. Goroutine Handler](#Goroutine-Handler)
5. [5. 滥用 Channels](#滥用-Channels)
6. [6. 滥用 range with Channels](#滥用-range-with-Channels)
7. [7. 误用 runtime.SetFinalizer.](#误用-runtime-SetFinalizer)
8. [8. time.Ticker](#time-Ticker)
9. [9. 滥用 defer](#滥用-defer)

- [结论](#结论)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;