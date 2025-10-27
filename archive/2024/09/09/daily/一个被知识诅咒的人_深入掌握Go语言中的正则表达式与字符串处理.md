---
title: 深入掌握Go语言中的正则表达式与字符串处理
url: https://blog.csdn.net/nokiaguy/article/details/142025361
source: 一个被知识诅咒的人
date: 2024-09-09
fetch_date: 2025-10-06T18:22:17.929472
---

# 深入掌握Go语言中的正则表达式与字符串处理

# 深入掌握Go语言中的正则表达式与字符串处理

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)Go语言正则表达式与字符串操作详解

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-09-08 13:16:20 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.8k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

20

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
13

CC 4.0 BY-SA版权

分类专栏：
[《Go语言编程全解--理论与实践》](https://blog.csdn.net/nokiaguy/category_12773266.html)
文章标签：
[golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[正则表达式](https://so.csdn.net/so/search/s.do?q=%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[mysql](https://so.csdn.net/so/search/s.do?q=mysql&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[go](https://so.csdn.net/so/search/s.do?q=go&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142025361>

[![](https://i-blog.csdnimg.cn/direct/6d4320254d4d47de985b6dbab91d4b6f.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

《Go语言编程全解--理论与实践》
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12773266.html "《Go语言编程全解--理论与实践》")

25 篇文章

订阅专栏

### Go语言中的正则表达式与模式匹配

在编程中，字符串处理是常见的需求之一，而正则表达式则是一个强大的工具，能够帮助我们实现复杂的字符串匹配、提取和替换功能。Go语言内置了对正则表达式的支持，通过`regexp`包，我们可以轻松实现模式匹配的各种操作。本文将详细介绍正则表达式在Go语言中的应用，并通过实际的代码示例来帮助你理解如何在日常编程中使用它。

#### 正则表达式的基础概念

**正则表达式**是一种用于匹配字符串的模式，它基于一组规则或语法。Go语言中的正则表达式由`regexp`包提供，正则表达式的匹配引擎是基于有限自动机的，自动机可以是确定性或非确定性的。

* **确定性有限自动机（DFA）**：对于每一个状态和输入符号，都有一个确定的下一个状态。
* **非确定性有限自动机（NFA）**：对于相同的状态和输入符号，可能有多个可能的下一个状态。

正则表达式的主要作用是根据预定义的模式对字符串进行查找、提取、替换或删除。对于复杂的文本处理任务，正则表达式是一种高效且强大的工具。虽然它可以解决许多问题，但在某些情况下，正则表达式可能并不是最佳选择，需要合理选择工具。

#### 正则表达式的语法

在深入代码之前，我们先简单介绍一下正则表达式的语法规则：

* **字符类**：用方括号定义字符集合，例如`[abc]`表示匹配’a’、'b’或’c’中的任意一个字符。
* **字符范围**：在字符类中，可以使用范围表示法，例如`[a-z]`表示匹配从’a’到’z’的任意小写字母。
* **重复次数**：`*`表示匹配0次或多次，`+`表示匹配1次或多次，`?`表示匹配0次或1次，`{n,m}`表示匹配n次到m次。
* **特殊字符**：正则表达式中的一些符号具有特殊含义，例如`.`表示任意字符，`^`表示字符串的开头，`$`表示字符串的结尾，`\d`表示数字，`\w`表示字母或数字字符。

#### 简单的正则表达式示例

我们首先来看一个简单的例子：假设你需要从一行文本中提取出某一特定列的数据。为了实现这一点，可以使用空格作为分隔符，将文本行分割为多个字段，然后选择指定的列。

##### 代码实现

```
package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

func main() {
    arguments := os.Args
    if len(arguments) < 2 {
        fmt.Printf("用法: selectColumn column <file1> [<file2> ... <fileN>]\n")
        os.Exit(1)
    }
    temp, err := strconv.Atoi(arguments[1])
    if err != nil {
        fmt.Println("列号不是整数:", temp)
        return
    }
    column := temp
    if column < 0 {
        fmt.Println("无效的列号！")
        os.Exit(1)
    }

    for _, filename := range arguments[2:] {
        fmt.Println("处理文件:", filename)
        f, err := os.Open(filename)
        if err != nil {
            fmt.Printf("打开文件出错 %s\n", err)
            continue
        }
        defer f.Close()

        r := bufio.NewReader(f)
        for {
            line, err := r.ReadString('\n')
            if err == io.EOF {
                break
            } else if err != nil {
                fmt.Printf("读取文件出错 %s", err)
                break
            }
            data := strings.Fields(line)
            if len(data) >= column {
                fmt.Println(data[column-1])
            }
        }
    }
}
```

##### 程序说明

* **`strings.Fields()`**：这个函数用于将字符串按空白字符进行分割，返回一个字符串切片。空白字符包括空格、制表符、换行符等。
* **`bufio.NewReader()`**：用于逐行读取文件的内容，通过`ReadString('\n')`可以按行读取文件，直到遇到EOF结束。

这个程序可以提取指定文本文件中的某一列数据，例如：

```
$ go run selectColumn.go 3 test.txt
```

#### 正则表达式匹配日期时间格式

正则表达式不仅可以用于简单的列提取，还可以用来处理更加复杂的模式匹配任务。下面我们来看一个匹配和转换Apache服务器日志中的日期和时间格式的例子。

##### 代码实现

```
package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "regexp"
    "strings"
    "time"
)

func main() {
    arguments := os.Args
    if len(arguments) == 1 {
        fmt.Println("请提供一个文本文件进行处理！")
        os.Exit(1)
    }
    filename := arguments[1]
    f, err := os.Open(filename)
    if err != nil {
        fmt.Printf("打开文件出错 %s", err)
        os.Exit(1)
    }
    defer f.Close()

    notAMatch := 0
    r := bufio.NewReader(f)
    for {
        line, err := r.ReadString('\n')
        if err == io.EOF {
            break
        } else if err != nil {
            fmt.Printf("读取文件出错 %s", err)
        }

        r1 := regexp.MustCompile(`.*\[(\d\d\/\w+\/\d\d\d\d:\d\d:\d\d:\d\d.*)\] .*`)
        if r1.MatchString(line) {
            match := r1.FindStringSubmatch(line)
            d1, err := time.Parse("02/Jan/2006:15:04:05 -0700", match[1])
            if err == nil {
                newFormat := d1.Format(time.Stamp)
                fmt.Print(strings.Replace(line, match[1], newFormat, 1))
            } else {
                notAMatch++
            }
            continue
        }

        r2 := regexp.MustCompile(`.*\[(\w+\-\d\d-\d\d:\d\d:\d\d:\d\d.*)\] .*`)
        if r2.MatchString(line) {
            match := r2.FindStringSubmatch(line)
            d1, err := time.Parse("Jan-02-06:15:04:05 -0700", match[1])
            if err == nil {
                newFormat := d1.Format(time.Stamp)
                fmt.Print(strings.Replace(line, match[1], newFormat, 1))
            } else {
                notAMatch++
            }
        }
    }
    fmt.Println(notAMatch, "行未匹配！")
}
```

##### 程序说明

这个程序可以处理Apache日志中的两种日期格式，并将其转换为`time.Stamp`格式。具体来说：

* **`regexp.MustCompile()`**：用于编译正则表达式。`MustCompile()`与`Compile()`的区别在于，前者在正则表达式无效时会直接触发`panic`，而`Compile()`会返回错误。
* **`time.Parse()`**：用于将日期字符串解析为`time.Time`类型。格式字符串如`"02/Jan/2006:15:04:05 -0700"`表示日期时间的格式。

运行该程序后，将输出日期格式转换后的日志内容：

```
$ go run changeDT.go log.txt
- - [Nov 21 19:28:09] "GET /file.zip HTTP/1.1" 200
2 行未匹配！
```

#### 匹配IPv4地址

在网络编程中，匹配IP地址（特别是IPv4地址）是一个常见需求。我们可以使用正则表达式来捕捉文本中的IPv4地址。

##### 代码实现

```
package main

import (
    "bufio"
    "fmt"
    "io"
    "net"
    "os"
    "regexp"
)

func findIP(input string) string {
    partIP := "(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
    grammar := partIP + "\\." + partIP + "\\." + partIP + "\\." + partIP
    matchMe := regexp.MustCompile(grammar)
    return matchMe.FindString(input)
}

func main() {
    arguments := os.Args
    if len(arguments) < 2 {
        fmt.Printf("用法: %s logFile\n", os.Args[0])
        os.Exit(1)
    }

    for _, filename := range arguments[1:] {
        f, err := os.Open(filename)
        if err != nil {
            fmt.Printf("打开文件出错 %s\n", err)
            os.Exit(1)
        }
        defer f.Close

()

        r := bufio.NewReader(f)
        for {
            line, err := r.ReadString('\n')
            if err == io.EOF {
                break
            } else if err != nil {
                fmt.Printf("读取文件出错 %s", err)
                break
            }
            ip := findIP(line)
            if net.ParseIP(ip) != nil {
                fmt.Println(ip)
            }
        }
    }
}
```

##### 程序说明

在这个程序中，我们使用正则表达式来捕捉IPv4地址，并通过`net.ParseIP()`进一步验证匹配到的IP地址是否有效。

* **`net.ParseIP()`**：用于验证一个字符串是否为有效的IP地址。

运行该程序可以从日志中提取所有IPv4地址，例如：

```
$ go run findIPv4.go /tmp/auth.log
192.168.1.1
10.0.0.1
```

#### Go语言中的字符串操作

虽然字符串并不是复合类型，但Go语言提供了丰富的字符串处理函数。在Go语言中，字符串是值类型，且默认支持UTF-8编码，这意味着你可以轻松处理Unicode字符。

##### 字符串操作示例

```
package main

import (
    "fmt"
    "strings"
)

func main() {
    fmt.Println(strings.ToUpper("hello world"))
    fmt.Println(strings.ToLower("HELLO WORLD"))
    fmt.Println(strings.TrimSpace("   Go语言   "))
    fmt.Println(stri...