---
title: 31个！Golang常用工具来啦（建议收藏）
url: https://buaq.net/go-131029.html
source: unSafe.sh - 不安全
date: 2022-10-16
fetch_date: 2025-10-03T20:01:17.071726
---

# 31个！Golang常用工具来啦（建议收藏）

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/02563f98fbf63045f5097b4ad588199f.jpg)

31个！Golang常用工具来啦（建议收藏）

导语 | 本文主要分享Golang相关的一些使用工具，简单介绍工具作用和使用场景，不会详细介绍其使用，列举的工具也不是最全的，具体可以参考链接或自行搜索学习。Go官方的工具可以使用go help xx
*2022-10-15 23:41:23
Author: [mp.weixin.qq.com(查看原文)](/jump-131029.htm)
阅读量:61
收藏*

---

导语 | 本文主要分享Golang相关的一些使用工具，简单介绍工具作用和使用场景，不会详细介绍其使用，列举的工具也不是最全的，具体可以参考链接或自行搜索学习。

Go官方的工具可以使用go help xxx命令查看帮助文档，比如查看go get的参数标记和使用文档：

```
go help get
```

可以参考Golang官方的文档：https://golang.google.cn/cmd/go/

**一、G0官方工具**

## （一）go get

该命令可以根据要求和实际情况从互联网上下载或更新指定的代码包及其依赖包，下载后自动编译，一般引用依赖用go get就可以了。

参考：

```
go get -u "github.com/VictoriaMetrics/fastcache"
```

参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261349

## （二）go build

该命令用于编译我们指定的源码文件或代码包以及它们的依赖包。命令的常用标记说明如下：

![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe96fsTy9sN5GgRfjUtXDe4pslnCOKZ2K9iczT2R5Nsc86f35FFoqSqvwC8TWVEhLCGj5F5EI2WfAicYw/640?wx_fmt=png)

编译过程输出到文件：go build -x > result 2>&1，因为go build -x 最终是将日志写到标准错误流当中。

如果只在编译特定包时需要指定参数，可以参考包名=参数列表的格式，比如go build -gcflags='log=-N -l' main.go

参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261347

## （三）go install

该命令用于编译并安装指定的代码包及它们的依赖包。当指定的代码包的依赖包还没有被编译和安装时，该命令会先去处理依赖包。与go build命令一样，传给go install命令的代码包参数应该以导入路径的形式提供。

并且，go build命令的绝大多数标记也都可以用于go install命令。实际上，go install命令只比go build命令多做了一件事，即：安装编译后的结果文件到指定目录。

参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261348

## （四）go fmt和gofmt

Golang的开发团队制定了统一的官方代码风格，并且推出了gofmt工具（gofmt或go fmt）来帮助开发者格式化他们的代码到统一的风格。

gofmt是一个cli程序，会优先读取标准输入，如果传入了文件路径的话，会格式化这个文件，如果传入一个目录，会格式化目录中所有.go文件，如果不传参数，会格式化当前目录下的所有.go文件。

gofmt默认不对代码进行简化，使用-s参数可以开启简化代码功能

gofmt是一个独立的cli程序，而go中还有一个go fmt命令，go fmt命令是gofmt的简单封装。go fmt在调用gofmt时添加了-l -w参数，相当于执行了gofmt -l -w

参考：

https://blog.csdn.net/whatday/article/details/97682094

## （五）go env

该命令用于打印Go语言的环境信息，常见的通用环境信息如下：

![](https://mmbiz.qpic.cn/mmbiz_png/VY8SELNGe96fsTy9sN5GgRfjUtXDe4psaSfgrEgT4HTDvkp0RgT8QXHs4LghVZH2SMNUayKyclnHeNYPVCJL4Q/640?wx_fmt=png)

设置或修改环境变量值：

```
go env -w GOPROXY="https://goproxy.com,direct"
```

参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261359

## （六）go run

该命令可以运行命令源码文件，只能接受一个命令源码文件以及若干个库源码文件（必须同属于main包）作为文件参数，且不能接受测试源码文件。它在执行时会检查源码文件的类型。如果参数中有多个或者没有命令源码文件，那么go run命令就只会打印错误提示信息并退出，而不会继续执行。

在通过参数检查后，go run命令会将编译参数中的命令源码文件，并把编译后的可执行文件存放到临时工作目录中。

参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261352

## （七）go test

该命令用于对Go语言编写的程序进行测试，这种测试是以代码包为单位的，命令会自动测试每一个指定的代码包。当然，前提是指定的代码包中存在测试源码文件。

参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261353

## （八）go clean

该命令会删除掉执行其它命令时产生的一些文件和目录。

参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261350

## （九）go list

该命令的作用是列出指定的代码包的信息。与其他命令相同，我们需要以代码包导入路径的方式给定代码包。被给定的代码包可以有多个。这些代码包对应的目录中必须直接保存有Go语言源码文件，其子目录中的文件不算在内。

标记-e的作用是以容错模式加载和分析指定的代码包。在这种情况下，命令程序如果在加载或分析的过程中遇到错误只会在内部记录一下，而不会直接把错误信息打印出来。

为了看到错误信息可以使用-json标记。这个标记的作用是把代码包的结构体实例用JSON的样式打印出来。-m标记可以打印出modules而不是package。

```
# cd yky-sys-backend/cmd/bidengine# go list -json -m{        "Path": "github.com/Project/test",        "Main": true,        "Dir": "/data/test",        "GoMod": "/data/test/go.mod",        "GoVersion": "1.15"} # 进入到.go文件的目录下，可以把文件依赖打印出来go list -m -json
```

 参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261354

## （十）go mod xxx

* ### go mod init

该命令初始化并写入一个新的go.mod至当前目录中，实际上是创建一个以当前目录为根的新模块。文件go.mod必须不存在。如果可能，init会从import注释（参阅“go help importpath”）或从版本控制配置猜测模块路径。要覆盖此猜测，提供模块路径作为参数 module为当前项目名。比如：

```
go mod init demo
```

参考：

https://www.jianshu.com/p/f6d2d6db2bca

* ### go mod tidy

该命令确保go.mod与模块中的源代码一致。它添加构建当前模块的包和依赖所必须的任何缺少的模块，删除不提供任何有价值的包的未使用的模块。它也会添加任何缺少的条目至go.mod并删除任何不需要的条目。

参考：

https://www.jianshu.com/p/f6d2d6db2bca

* ### go mod vendor

该命令重置主模块的vendor目录，使其包含构建和测试所有主模块的包所需要的所有包。不包括vendor中的包的测试代码。即将GOPATH或GOROOT下载的包拷贝到项目下的vendor目录，如果不使用vendor隔离项目的依赖，则不需要使用该命令拷贝依赖。

参考：

https://www.jianshu.com/p/f6d2d6db2bca

* ### go mod download

该命令下载指定名字的模块，可为选择主模块依赖的模块匹配模式，或[[email protected]](http://mp.weixin.qq.com/cdn-cgi/l/email-protection)形式的模块查询。如果download不带参数则代表是主模块的所有依赖。download的只会下载依赖，不会编译依赖，和get是有区别的。

参考：

https://www.jianshu.com/p/f6d2d6db2bca

* go mod edit

该命令提供一个编辑go.mod的命令行接口，主要提供给工具或脚本使用。它只读取go.mod；不查找涉及模块的信息。默认情况下，edit读写主模块的go.mod文件，但也可以在标志后指定不同的目标文件。

参考：

https://www.jianshu.com/p/f6d2d6db2bca

* ### go mod graph

该命令以文本形式打印模块间的依赖关系图。输出的每一行行有两个字段（通过空格分割）；模块和其所有依赖中的一个。每个模块都被标记为[[email protected]](http://mp.weixin.qq.com/cdn-cgi/l/email-protection)形式的字符串（除了主模块，因其没有@version后缀）。

参考：

https://www.jianshu.com/p/f6d2d6db2bca

* go mod verify

该命令查存储在本地下载源代码缓存中的当前模块的依赖，是否自从下载之后未被修改。如果所有模块都未被修改，打印“all modules verified”。否则，报告哪个模块已经被修改并令“go mod”以非0状态退出。

参考：

https://www.jianshu.com/p/f6d2d6db2bca

* ### go mod why

该命令输出每个包或者模块的引用块，每个块以注释行“# package”或“# module”开头，给出目标包或模块。随后的行通过导入图给出路径，一个包一行。每个块之间通过一个空行分割，如果包或模块没有被主模块引用，该小节将显示单独一个带圆括号的提示信息来表明该事实。

参考：

https://www.jianshu.com/p/f6d2d6db2bca

## （十一）go tool xxx

go tool的可执行文件在GOROOT或GOPATH的pkg/tool目录。go doc cmd可以查看具体cmd的使用说明，比如：

```
go doc pprof
```

* ### go tool pprof

在Golang中，可以通过pprof工具对应于程序的运行时进行性能分析，包括CPU、内存、Goroutine等实时信息。

参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261357

* ### go tool trace

该命令可以追踪请求链路，清晰的了解整个程序的调用栈，可以通过追踪器捕获大量信息。

参考：

https://zhuanlan.zhihu.com/p/410590497

* ### go tool compile

该命令可以编译Go文件生成汇编代码，-N参数表示禁止编译优化， -l表示禁止内联，-S表示打印汇编，比如

```
# 会生成main.o的汇编文件go tool compile -S main.go
```

* ### go tool vet和go vet

该命令是一个用于检查Go语言源码中静态错误的简单工具。

go vet命令是go tool vet命令的简单封装。它会首先载入和分析指定的代码包，并把指定代码包中的所有Go语言源码文件和以“.s”结尾的文件的相对路径作为参数传递给go tool vet命令。其中，以“.s”结尾的文件是汇编语言的源码文件。如果go vet命令的参数是Go语言源码文件的路径，则会直接将这些参数传递给go tool vet命令。

参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261356

* ### go tool doc和go doc

该命令可以打印附于Go语言程序实体上的文档。我们可以通过把程序实体的标识符作为该命令的参数来达到查看其文档的目的。

所谓Go语言的程序实体，是指变量、常量、函数、结构体以及接口。而程序实体的标识符即是代表它们的名称。

参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261351

* ### go tool addr2line

该命令可以调用栈的地址转化为文件和行号。

```
Usage:     go tool addr2line binary Addr2line reads hexadecimal addresses, one per line and with optional 0xprefix, from standard input. For each input address, addr2line prints twooutput lines, first the name of the function containing the address andsecond the file:line of the source code corresponding to that address. This tool is intended for use only by pprof; its interface may change or itmay be deleted entirely in future releases.
```

* ### go tool asm

该命令可以将汇编文件编译成一个.o文件，后续这个.o文件可以用于生成.a归档文件，命令的file参数必须是汇编文件。

```
Usage:     go tool asm [flags] file The specified file must be a Go assembly file. The same assembler is usedfor all target operating systems and architectures. The GOOS and GOARCHenvironment variables set the desired target.
```

* ### go tool buildid

每一个 Go 二进制文件内，都有一个独一无二的 Build ID，详情参考 src/cmd/go/internal/work/buildid.go 。Go Build ID 可以用以下命令来查看：

```
go tool buildid
```

参考：

https://www.anquanke.com/post/id/215419

* ### go tool cgo

该命令可以使我们创建能够调用C语言代码的Go语言源码文件。这使得我们可以使用Go语言代码去封装一些C语言的代码库，并提供给Go语言代码或项目使用。

参考：

https://www.kancloud.cn/cattong/go\_command\_tutorial/261358

* ### go tool cover

该命令对单元测试过程中生成的代码覆盖率统计生成html文件，可以本地打开展示。

```
go test -coverprofile=a.outgo tool cover -html=a.out -o coverage.html
```

覆盖度工具不仅可以记录分支是否被执行，还可以记录分支被执行了多少次。

go test -covermode=set|count|atomic:
-covermode：

set: 默认模式，统计是否执行

count: 计数

atomic: count的并发安全版本，仅当需要精确统计时使用

通过go tool cover -func=count.out查看每个函数的覆盖度。

参考：

https://blog.csdn.net/xhdxhdxhd/article/details/120424848

* ### go tool dist

dist工具是属于go的一个引导工具，它负责构建C程序（如Go编译器）和Go工具的初始引导副本。它也可以作为一个包罗万象用shell脚本替换以前完成的零工。通过“go tool dist”命令可以操作该工具。

```
go tool distusage: go tool dist [command]Commands are: banner   ...