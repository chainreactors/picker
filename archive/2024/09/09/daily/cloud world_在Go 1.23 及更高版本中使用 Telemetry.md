---
title: 在Go 1.23 及更高版本中使用 Telemetry
url: https://cloudsjhan.github.io/2024/09/08/%E5%9C%A8Go-1-23-%E5%8F%8A%E6%9B%B4%E9%AB%98%E7%89%88%E6%9C%AC%E4%B8%AD%E4%BD%BF%E7%94%A8-Telemetry/
source: cloud world
date: 2024-09-09
fetch_date: 2025-10-06T18:22:19.312717
---

# 在Go 1.23 及更高版本中使用 Telemetry

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 在Go 1.23 及更高版本中使用 Telemetry

posted

2024-09-08

|

in

[Go](/categories/Go/)

|

visitors:

|

|

wordcount:

1,827
|

min2read ≈

7

![](https://)

> Robert Findley
> 2024年9月3日

![](https://files.mdnice.com/user/4760/221ba11f-c5f4-4f3c-befc-2feff4ecdde0.png)

Go 1.23 提供了一种新的方式来帮助改进 Go 工具链。通过启用 Telemetry，可以选择与 Go 团队共享有关工具链程序及其使用情况的数据。这些数据将帮助 Go 贡献者修复错误，避免退步，并做出更好的决策。

默认情况下，Go Telemetry 的数据仅存储在的本地计算机上。如果启用上传，用户数据的有限子集将每周发布到 [telemetry.go.dev](https://telemetry.go.dev/ "telemetry go.dev")。

从 Go 1.23 开始，可以使用以下命令启用本地telemetry 数据的上传：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` go telemetry on ``` |

要禁用甚至本地遥测数据收集，请运行以下命令：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` go telemetry off ``` |

[Telemetry 文档](https://go.dev/doc/telemetry "telemetry docs")包含了更详细的实现描述。

## Go Telemetry 的由来

虽然软件遥测并不是一个新概念，但 Go 团队经历了多次迭代，寻找符合 Go 对性能、可移植性和透明度要求的 Telemetry 实现。

[最初的设计](https://research.swtch.com/telemetry-design "telemetry 最初设计")旨在尽可能不显眼、开放和保护隐私，以至于默认情况下可以接受启用，但许多用户在漫长的[公开讨论](https://go.dev/issue/58409 "public disscussion")中提出了担忧，最终[改变](https://research.swtch.com/telemetry-opt-in#campaign "telemetry change")了设计，要求远程上传需要用户明确同意。

新的设计在 2023 年 4 月[被接受](https://go.dev/issue/58894 "最终被接受的设计")，并在那个夏天实施。

## Telemetry in gopls¶

Go Telemetry 的第一个迭代在 2023 年 10 月的 Go 语言服务器 gopls 的 [v0.14](https://github.com/golang/tools/releases/tag/gopls/v0.14.0 "gopls v0.14.0") 版本中发布。发布后，大约有 100 名用户启用了上传，可能是受到发布说明或[Gophers Slack 频道](https://gophers.slack.com/messages/gopls/ "gopher slack channel")讨论的激励，数据开始流入。不久，遥测在 gopls 中发现了第一个错误：

![](https://files.mdnice.com/user/4760/ee761b58-ccc1-4dbd-9c32-aa0ae9d4ea89.png)

> Dan 在他上传的 telemetry 数据中注意到的堆栈跟踪导致了一个错误报告和修复。值得一提的是，我们并不知道是谁报告了这个堆栈。

## IDE Prompting¶

虽然看到遥测在实践中起作用是很好的，我们也很感激那些早期采用者的支持，但 100 名参与者并不足以测量我们想要测量的类型。

正如 Russ Cox 在他最初的[博客文章](https://research.swtch.com/telemetry-opt-in#campaign "rc blog")中指出的，遥测默认关闭的一个缺点是需要不断鼓励参与。为了维持足够大的样本量以进行有意义的定量数据分析，并代表用户群体，需要进行外展。虽然博客文章和发布说明可以提高参与度（如果您在阅读本文后启用遥测，我们将不胜感激！），但它们会导致样本偏差。例如，我们在 gopls 中的遥测早期采用者中几乎未收到来自 GOOS=windows 的数据。

为了帮助接触更多用户，我们在 VS Code Go 插件中引入了一个提示，询问用户是否想要启用遥测：

![](https://files.mdnice.com/user/4760/106091c8-90fa-4bdc-a707-d5aa063f5dd3.png)

VS Code 显示的遥测提示。
截至这篇博客文章，该提示已向 5% 的 VS Code Go 用户推出，遥测样本已增长到大约每周 1800 名参与者：

![](https://files.mdnice.com/user/4760/6b3cff33-3ef2-4fc4-88b2-439405950503.png)

每周上传与提示率，提示有助于接触更多用户。
（最初的增长可能归因于提示所有 VS Code Go 扩展的用户）。

然而，它引入了明显倾向于 VS Code 用户的偏差，与最近的 Go 调查结果相比：

![](https://files.mdnice.com/user/4760/60a9ec11-36e7-45aa-8e76-72846cd9a731.png)

我们怀疑 VS Code 在 telemetry 数据中被过度代表。
我们计划通过提示所有使用 gopls 的 LSP 功能编辑器，使用语言服务器协议本身的一个特性来解决这种偏差。

## Telemetry wins¶

出于谨慎，我们提议在 gopls telemetry 的初始发布中只收集一些基本指标。其中之一是 gopls/bug stack counter，它记录 gopls 遇到的意外或“不可能”的条件。实际上，它是一种断言，但不是停止程序，而是在遥测中记录它在某些执行中被达到，以及堆栈跟踪。

在我们的 [gopls 可扩展性工作](https://go.dev/blog/gopls-scalability.md "gopls 扩展工作")中，我们添加了许多这种类型的断言，但我们很少在测试或我们自己的 gopls 使用中观察到它们失败。我们预计这些断言几乎都无法到达。

当我们开始在 VS Code 中随机提示用户启用遥测时，我们看到许多这些条件在实践中被达到，堆栈跟踪的上下文通常足以让我们复现并修复长期存在的错误。我们开始在 gopls/telemetry-wins 标签下收集这些问题，以跟踪遥测促进的“胜利”。

![](https://files.mdnice.com/user/4760/516ae86f-29e6-4fb7-bdfc-1297b3a9efe5.png)

感谢 Paul 的建议。

来自遥测的错误最令人惊讶的方面是它们有多少是真实的。当然，有些错误对用户来说是看不见的，但相当多的错误是 gopls 的实际错误行为——比如缺少交叉引用，或者在某些罕见条件下的补全不准确。它们正是用户可能会轻微烦恼但可能不会麻烦报告为问题的那种事情。也许用户会认为这种行为是有意为之的。如果他们确实报告了一个问题，他们可能不确定如何复现错误，或者我们需要在问题跟踪器上进行长时间的来回讨论以捕获堆栈跟踪。没有遥测，这些错误中的大多数是不可能被发现的，更不用说被修复了。

而这仅仅是来自几个计数器。我们只为我们知道的潜在错误设置了堆栈跟踪。我们没有预料到的问题呢？

## 自动崩溃报告

Go 1.23 包括一个新的 [runtime.SetCrashOutput API](https://go.dev/doc/go1.23#runtimedebugpkgruntimedebug "runtime.SetCrash Output API")，可以用来通过看门狗进程实现自动崩溃报告。从 [v0.15.0](https://github.com/golang/tools/releases/tag/gopls/v0.15.0 "v0.15.0") 开始，如果 gopls 本身是用 Go 1.23 构建的，那么当它崩溃时，gopls 会报告一个 crash/crash stack counter。

当我们发布 gopls@v0.15.0 时，只有少数用户在我们的样本中使用了 Go 1.23 的未发布开发构建，但新的 crash/crash counter 仍然发现了两个 [bug](https://github.com/golang/tools/releases/tag/gopls/v0.15.2 "2 个 bug")。

## Go 工具链及更广泛的遥测

Go 1.23 在 Go 工具链中记录遥测，包括 go 命令和其他工具，如编译器、链接器和 go vet。我们已经在 vulncheck 和 VS Code Go 插件中添加了遥测，并[提议](https://go.dev/issue/68384 "delve")将其添加到 delve 中。

原始遥测博客系列为遥测如何帮助改进 Go 进行了大量头脑风暴。我们期待探索这些想法以及更多。

在 gopls 中，我们计划使用遥测来提高可靠性并为决策制定和优先级排序提供信息。随着 Go 1.23 启用的自动崩溃报告，我们预计在预发布测试中捕获更多崩溃。展望未来，我们将添加更多计数器来衡量用户体验——关键操作的延迟、各种功能的使用频率——以便我们可以集中精力在最有利于 Go 开发者的地方。

Go 将在 11 月迎来 15 岁生日，语言及其生态系统继续增长。遥测将在帮助 Go 贡献者更快、更安全地朝着正确方向前进中发挥关键作用。

---

-------------The End-------------

Title:[在Go 1.23 及更高版本中使用 Telemetry](/2024/09/08/%E5%9C%A8Go-1-23-%E5%8F%8A%E6%9B%B4%E9%AB%98%E7%89%88%E6%9C%AC%E4%B8%AD%E4%BD%BF%E7%94%A8-Telemetry/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2024年09月08日 - 20:09

Last Update:2024年09月08日 - 20:09

Original Link:[https://cloudsjhan.github.io/2024/09/08/在Go-1-23-及更高版本中使用-Telemetry/](/2024/09/08/%E5%9C%A8Go-1-23-%E5%8F%8A%E6%9B%B4%E9%AB%98%E7%89%88%E6%9C%AC%E4%B8%AD%E4%BD%BF%E7%94%A8-Telemetry/ "在Go 1.23 及更高版本中使用 Telemetry")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

![cloud sjhan 支付宝](/images/alipay.jpg)

[Go](/tags/Go/)

(>给这篇博客打个分吧<)

[Golang - 使用 GoFakeIt 生成 Mock 数据](/2024/09/01/Golang-%E4%BD%BF%E7%94%A8-GoFakeIt-%E7%94%9F%E6%88%90-Mock-%E6%95%B0%E6%8D%AE/ "Golang - 使用 GoFakeIt 生成 Mock 数据")

[探索 Goja：Golang 中的 JavaScript 运行时](/2024/09/11/%E6%8E%A2%E7%B4%A2-Goja%EF%BC%9AGolang-%E4%B8%AD%E7%9A%84-JavaScript-%E8%BF%90%E8%A1%8C%E6%97%B6/ " 探索 Goja：Golang 中的 JavaScript 运行时")

* Content
* Overview

![cloud sjhan](/images/avatar.png)

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

1. [1. Go Telemetry 的由来](#Go-Telemetry-的由来)
2. [2. Telemetry in gopls¶](#Telemetry-in-gopls¶)
3. [3. IDE Prompting¶](#IDE-Prompting¶)
4. [4. Telemetry wins¶](#Telemetry-wins¶)
5. [5. 自动崩溃报告](#自动崩溃报告)
6. [6. Go 工具链及更广泛的遥测](#Go-工具链及更广泛的遥测)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;