---
title: 掌握Go语言中的时间与日期操作
url: https://blog.csdn.net/nokiaguy/article/details/142001609
source: 一个被知识诅咒的人
date: 2024-09-08
fetch_date: 2025-10-06T18:23:04.348240
---

# 掌握Go语言中的时间与日期操作

# 掌握Go语言中的时间与日期操作

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-09-07 20:06:47 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.1k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

8

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
5

CC 4.0 BY-SA版权

分类专栏：
[《Go语言编程全解--理论与实践》](https://blog.csdn.net/nokiaguy/category_12773266.html)
文章标签：
[golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[linux](https://so.csdn.net/so/search/s.do?q=linux&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[go](https://so.csdn.net/so/search/s.do?q=go&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142001609>

[![](https://i-blog.csdnimg.cn/direct/6d4320254d4d47de985b6dbab91d4b6f.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

《Go语言编程全解--理论与实践》
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12773266.html "《Go语言编程全解--理论与实践》")

25 篇文章

订阅专栏

## Go语言中的时间与日期操作

在编写程序时，处理时间和日期看似是一项无关紧要的任务，但在需要同步多个任务或从文本文件中读取时间时，它的重要性便凸显出来。Go语言中的`time`包为我们提供了丰富的时间与日期操作功能。本文将详细介绍如何在Go语言中解析时间与日期字符串、在不同的格式之间进行转换，以及如何按照所需的格式输出时间和日期。

#### 初识time包

在学习如何解析字符串并将其转换为时间或日期之前，我们先通过一个简单的程序`usingTime.go`来认识`time`包。程序的第一部分代码如下：

```
package main
import (
    "fmt"
    "time"
)
```

接着是程序的第二部分：

```
func main() {
    fmt.Println("时间戳:", time.Now().Unix()) // 输出当前的Unix时间戳
    t := time.Now()
    fmt.Println(t, t.Format(time.RFC3339)) // 使用RFC3339格式化时间
    fmt.Println(t.Weekday(), t.Day(), t.Month(), t.Year()) // 输出当前的星期、日期、月份和年份
    time.Sleep(time.Second) // 暂停1秒
    t1 := time.Now()
    fmt.Println("时间差:", t1.Sub(t)) // 输出时间差
}
```

在这段代码中，`time.Now().Unix()`返回的是Unix时间戳，即从1970年1月1日00:00:00 UTC起到现在的秒数。`Format()`函数可以将时间变量转换为指定的格式。在这里，我们使用了`RFC3339`格式。`time.Sleep()`函数用于让程序暂停执行，这在模拟函数的延迟时很有用。最后，`time.Sub()`函数用于计算两个时间点之间的差值。

程序的最后一部分如下：

```
formatT := t.Format("01 January 2006") // 自定义格式化日期
fmt.Println(formatT)
loc, _ := time.LoadLocation("Europe/Paris") // 加载时区
parisTime := t.In(loc) // 转换为巴黎时间
fmt.Println("巴黎时间:", parisTime)
```

这段代码展示了如何自定义日期格式，并将时间转换为不同的时区。执行这个程序的输出如下：

```
$ go run usingTime.go
时间戳: 1548753515
2019-01-29 11:18:35.01478 +0200 EET m=+0.000339641
2019-01-29T11:18:35+02:00
星期二 29 一月 2019
时间差: 1.000374985秒
01 一月 2019
巴黎时间: 2019-01-29 10:18:35.01478 +0100 CET
```

#### 时间解析与转换

当我们有一个字符串并希望将其解析为时间时，就可以使用`time.Parse()`函数。它接受两个参数，第一个参数是字符串的预期格式，第二个参数是实际需要解析的字符串。举个例子，下面是一个解析时间的程序`parseTime.go`：

```
package main
import (
    "fmt"
    "os"
    "path/filepath"
    "time"
)

func main() {
    var myTime string
    if len(os.Args) != 2 {
        fmt.Printf("用法: %s string\n", filepath.Base(os.Args[0]))
        os.Exit(1)
    }
    myTime = os.Args[1]
    d, err := time.Parse("15:04", myTime) // 解析时间字符串
    if err == nil {
        fmt.Println("完整时间:", d)
        fmt.Println("时间:", d.Hour(), d.Minute()) // 输出小时和分钟
    } else {
        fmt.Println(err)
    }
}
```

执行这个程序的输出如下：

```
$ go run parseTime.go 12:10
完整时间: 0000-01-01 12:10:00 +0000 UTC
时间: 12 10
```

如果使用错误的格式进行解析，Go将返回相应的错误信息。

#### 日期解析

接下来，我们看一下如何解析日期字符串。我们将使用与时间解析类似的方法，不过格式不同。下面是解析日期的程序`parseDate.go`：

```
package main
import (
    "fmt"
    "os"
    "path/filepath"
    "time"
)

func main() {
    var myDate string
    if len(os.Args) != 2 {
        fmt.Printf("用法: %s string\n", filepath.Base(os.Args[0]))
        return
    }
    myDate = os.Args[1]
    d, err := time.Parse("02 January 2006", myDate) // 解析日期字符串
    if err == nil {
        fmt.Println("完整日期:", d)
        fmt.Println("日期:", d.Day(), d.Month(), d.Year()) // 输出天、月、年
    } else {
        fmt.Println(err)
    }
}
```

执行这个程序的输出如下：

```
$ go run parseDate.go "20 July 2000"
完整日期: 2000-07-20 00:00:00 +0000 UTC
日期: 20 七月 2000
```

#### 时间与日期格式的转换

在某些情况下，我们可能需要将时间和日期字符串的格式进行转换。例如，下面的程序`timeDate.go`展示了如何处理日志文件中的时间和日期格式：

```
package main
import (
    "fmt"
    "regexp"
    "time"
)

func main() {
    logs := []string{
        "127.0.0.1 - - [16/Nov/2017:10:49:46 +0200] 325504",
        "[12/Nov/2017:16:27:21 +0300]",
        "[12/Nov/2017:20:88:21 +0200]",
        "[12/Nov/2017:20:21 +0200]",
    }

    for _, logEntry := range logs {
        r := regexp.MustCompile(`.*\[(\d\d\/\w+/\d\d\d\d:\d\d:\d\d:\d\d.*)\].*`)
        if r.MatchString(logEntry) {
            match := r.FindStringSubmatch(logEntry)
            dt, err := time.Parse("02/Jan/2006:15:04:05 -0700", match[1])
            if err == nil {
                newFormat := dt.Format(time.RFC850) // 转换为RFC850格式
                fmt.Println(newFormat)
            } else {
                fmt.Println("无效的日期时间格式!")
            }
        } else {
            fmt.Println("不匹配!")
        }
    }
}
```

程序输出如下：

```
$ go run timeDate.go
星期四, 16-十一月-17 10:49:46 EET
星期四, 16-十一月-17 10:16:41 EET
无效的日期时间格式!
不匹配!
```

#### 测量执行时间

最后，我们来看一下如何测量Go程序中某些操作的执行时间。程序`execTime.go`展示了这一过程：

```
package main
import (
    "fmt"
    "time"
)

func main() {
    start := time.Now()
    time.Sleep(time.Second) // 暂停1秒
    duration := time.Since(start) // 计算执行时间
    fmt.Println("time.Sleep(1) 执行时间:", duration)

    start = time.Now()
    time.Sleep(2 * time.Second) // 暂停2秒
    duration = time.Since(start)
    fmt.Println("time.Sleep(2) 执行时间:", duration)

    start = time.Now()
    for i := 0; i < 200000000; i++ {} // 空循环
    duration = time.Since(start)
    fmt.Println("空循环执行时间:", duration)
}
```

输出结果如下：

```
$ go run execTime.go
time.Sleep(1) 执行时间: 1.000768881s
time.Sleep(2) 执行时间: 2.00062487s
空循环执行时间: 50.497931ms
```

#### 总结

本文详细介绍了如何在Go语言中处理时间和日期，包括解析、格式转换以及测量执行时间等操作。通过灵活运用`time`包中的各种功能，开发者能够轻松处理各种时间与日期相关的任务，为应用程序提供更精确的时间管理。

关注博主即可阅读全文
![](https://csdnimg.cn/release/blogv2/dist/pc/img/arrowDownAttend.png)

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png)

确定要放弃本次机会？

福利倒计时

*:*

*:*

![](https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png)
立减 ¥

普通VIP年卡可用

[立即使用](https://mall.csdn.net/vip)

[![](https://profile-avatar.csdnimg.cn/2ccacbf1fc8347338ede60bde7fb2eec_nokiaguy.jpg!1)

蒙娜丽宁](https://unitymarvel.blog.csdn.net)

关注
关注

* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/like.png)

  5

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  8

  收藏

  觉得还不错?
  一键收藏
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/collectionCloseWhite.png)
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/guideRedReward01.png)
  知道了

  [![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/comment.png)

  0](#commentBox)

  评论
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/share.png)
  分享

  复制链接

  分享到 QQ

  分享到新浪微博

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/share/icon-wechat.png)扫一扫
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/more.png)

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

...