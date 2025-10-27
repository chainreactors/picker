---
title: 从 Golang 到 TinyGo：如何为 IOT 构建高效应用程序？
url: https://cloudsjhan.github.io/2024/08/01/%E4%BB%8E-Golang-%E5%88%B0-TinyGo%EF%BC%9A%E5%A6%82%E4%BD%95%E4%B8%BA-IOT-%E6%9E%84%E5%BB%BA%E9%AB%98%E6%95%88%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%EF%BC%9F/
source: cloud world
date: 2024-08-02
fetch_date: 2025-10-06T18:02:15.140682
---

# 从 Golang 到 TinyGo：如何为 IOT 构建高效应用程序？

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 从 Golang 到 TinyGo：如何为 IOT 构建高效应用程序？

posted

2024-08-01

|

in

[tinygo](/categories/tinygo/)

|

visitors:

|

|

wordcount:

1,004
|

min2read ≈

4

![](https://)

TinyGo 是专为小型设备设计的 Go 编译器。它将 Go 编程语言引入微控制器和 WebAssembly，使 Go 开发人员能够高效地为嵌入式系统和网络环境构建应用程序。TinyGo 的主要目标是缩小二进制文件的大小并提高性能，以适应小型设备的限制。

![](https://files.mdnice.com/user/4760/b9b5c1c9-803f-472d-99e9-fcfac4153091.png)

### TinyGo 的主要特性

* 小二进制文件与标准 Go 编译器 (gc) 相比，TinyGo 生成的二进制文件要小得多，因此适合存储空间有限的环境。
* 内存占用低：TinyGo 经过优化，使用的内存更少，非常适合内存有限的微控制器。
* 支持 WebAssembly：TinyGo 可将 Go 代码编译成 WebAssembly，使 Go 应用程序能在网络浏览器中运行。
* 互操作性：允许通过易于使用的应用程序接口与底层硬件直接交互，因此非常适合嵌入式系统。

### 安装

可以使用以下命令安装 TinyGo：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # Install TinyGo brew tap tinygo-org/tools brew install tinygo  # Verify the installation tinygo version ``` |

对于其他操作系统，可以按照官方[安装指南](https://tinygo.org/ "tinygo installation")进行安装。

### 编写第一个 TinyGo 程序

让我们用 TinyGo 写一个简单的 “Hello, World!”程序。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` package main  import "machine" import "time"  func main() {     led := machine.LED     led.Configure(machine.PinConfig{Mode: machine.PinOutput})      for {         led.High()         time.Sleep(time.Millisecond * 500)         led.Low()         time.Sleep(time.Millisecond * 500)     } } ``` |

### 编译和运行 TinyGo 代码

要在微控制器上编译和运行这段代码，请按照以下步骤操作：

* 将微控制器连接到电脑。
* 为特定电路板编译代码。例如，如果您使用的是 Arduino Uno：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` tinygo flash -target=arduino main.go ``` |

### Golang 和 TinyGo 的区别

虽然 Golang 和 TinyGo 有着相同的语法和许多功能，但它们也有一些关键的不同之处：

#### 目标平台

* Golang：主要设计用于服务器端应用程序、网络服务和桌面应用程序。
* TinyGo：针对微控制器、物联网设备和浏览器应用的 WebAssembly。

#### 二进制大小：

* Golang：由于其全面的运行时和标准库，产生的二进制文件相对较大。
* TinyGo：经过优化，可生成适合嵌入式系统的较小二进制文件。

#### 标准库支持

* Golang：完全支持 Go 标准库
* TinyGo：由于嵌入式环境的限制，对 Go 标准库的支持有限。不过，它包含了基本的软件包，并为不支持的功能提供了替代方案。

#### 内存使用情况：

* Golang：优化了性能，但使用更多内存。
* TinyGo：内存使用量更少，非常适合低内存环境。

#### 并发性：

* Golang完全支持 goroutines 和并发编程。
* TinyGo：对 goroutines 的基本支持，但由于目标平台的限制而受到一些限制。

### 使用 TinyGo 的示例项目

#### 闪烁的 LED：在微控制器上闪烁 LED 的简单程序。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` package main  import "machine" import "time"  func main() {     led := machine.LED     led.Configure(machine.PinConfig{Mode: machine.PinOutput})      for {         led.High()         time.Sleep(time.Millisecond * 500)         led.Low()         time.Sleep(time.Millisecond * 500)     } } ``` |

#### 温度传感器从温度传感器读取数据并显示。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` package main  import (     "machine"     "time" )  func main() {     sensor := machine.ADC{Pin: machine.ADC1}     sensor.Configure(machine.ADCConfig{})      for {         value := sensor.Get()         println("Temperature:", value)         time.Sleep(time.Second)     } } ``` |

#### WebAssembly 示例

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` package main  import "fmt"  func main() {     fmt.Println("Hello, WebAssembly!") } ``` |

将其编译为 WebAssembly：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` tinygo build -o main.wasm -target wasm main.go ``` |

### 总结

TinyGo 通过 WebAssembly 将 Go 编程语言的强大功能和简易性扩展到微控制器和网络浏览器等受限环境。TinyGo 能够生成小二进制文件并高效使用内存，是物联网和嵌入式系统开发的理想选择。与完整的 Go 编译器相比，WebAssembly 有一些局限性，但它为 Go 开发人员在新领域创建创新应用提供了新的可能性。

---

-------------The End-------------

Title:[从 Golang 到 TinyGo：如何为 IOT 构建高效应用程序？](/2024/08/01/%E4%BB%8E-Golang-%E5%88%B0-TinyGo%EF%BC%9A%E5%A6%82%E4%BD%95%E4%B8%BA-IOT-%E6%9E%84%E5%BB%BA%E9%AB%98%E6%95%88%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%EF%BC%9F/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年08月01日 - 11:08

Last Update:2024年08月01日 - 11:08

Original Link:[https://cloudsjhan.github.io/2024/08/01/从-Golang-到-TinyGo：如何为-IOT-构建高效应用程序？/](/2024/08/01/%E4%BB%8E-Golang-%E5%88%B0-TinyGo%EF%BC%9A%E5%A6%82%E4%BD%95%E4%B8%BA-IOT-%E6%9E%84%E5%BB%BA%E9%AB%98%E6%95%88%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%EF%BC%9F/ "从 Golang 到 TinyGo：如何为 IOT 构建高效应用程序？")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

![cloud sjhan 支付宝](/images/alipay.jpg)

支付宝

[tinygo](/tags/tinygo/)

(>给这篇博客打个分吧<)

[在 Confluent Cloud 上使用 Databend Kafka Connect 构建实时数据流同步](/2024/07/25/%E5%9C%A8-Confluent-Cloud-%E4%B8%8A%E4%BD%BF%E7%94%A8-Databend-Kafka-Connect-%E6%9E%84%E5%BB%BA%E5%AE%9E%E6%97%B6%E6%95%B0%E6%8D%AE%E6%B5%81%E5%90%8C%E6%AD%A5/ "在 Confluent Cloud 上使用 Databend Kafka Connect 构建实时数据流同步")

[从源代码中窥探 Go 的 WaitGroup 实现和应用](/2024/08/04/%E4%BB%8E%E6%BA%90%E4%BB%A3%E7%A0%81%E4%B8%AD%E7%AA%A5%E6%8E%A2-Go-%E7%9A%84-WaitGroup-%E5%AE%9E%E7%8E%B0%E5%92%8C%E5%BA%94%E7%94%A8/ "从源代码中窥探 Go 的 WaitGroup 实现和应用")

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

1. [1. TinyGo 的主要特性](#TinyGo-的主要特性)
2. [2. 安装](#安装)
3. [3. 编写第一个 TinyGo 程序](#编写第一个-TinyGo-程序)
4. [4. 编译和运行 TinyGo 代码](#编译和运行-TinyGo-代码)
5. [5. Golang 和 TinyGo 的区别](#Golang-和-TinyGo-的区别)
   1. [5.1. 目标平台](#目标平台)
   2. [5.2. 二进制大小：](#二进制大小：)
   3. [5.3. 标准库支持](#标准库支持)
   4. [5.4. 内存使用情况：](#内存使用情况：)
   5. [5.5. 并发性：](#并发性：)
6. [6. 使用 TinyGo 的示例项目](#使用-TinyGo-的示例项目)
   1. [6.1. 闪烁的 LED：在微控制器上闪烁 LED 的简单程序。](#闪烁的-LED：在微控制器上闪烁-LED-的简单程序。)
   2. [6.2. 温度传感器从温度传感器读取数据并显示。](#温度传感器从温度传感器读取数据并显示。)
   3. [6.3. WebAssembly 示例](#WebAssembly-示例)
7. [7. 总结](#总结)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;