---
title: Go语言并发编程：从理论到实践
url: https://blog.csdn.net/nokiaguy/article/details/142283322
source: 一个被知识诅咒的人
date: 2024-09-16
fetch_date: 2025-10-06T18:22:02.981950
---

# Go语言并发编程：从理论到实践

# Go语言并发编程：从理论到实践

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-09-15 13:43:06 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量889
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

1

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
5

CC 4.0 BY-SA版权

分类专栏：
[Go语言并发实战](https://blog.csdn.net/nokiaguy/category_12786332.html)
文章标签：
[golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[后端](https://so.csdn.net/so/search/s.do?q=%E5%90%8E%E7%AB%AF&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[go](https://so.csdn.net/so/search/s.do?q=go&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142283322>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756757.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Go语言并发实战
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12786332.html "Go语言并发实战")

18 篇文章

¥19.90
¥99.00

订阅专栏
![](https://csdnimg.cn/release/blogv2/dist/components/img/studyVipIcon.png)超级会员免费看

并发是计算机科学领域中的一个核心概念，但对于不同的人来说，它可能意味着不同的东西。除了“并发”之外，你可能还听说过“异步”、“并行”或“多线程”等术语。一些人认为这些词是同义的，而另一些人则严格区分它们。如果我们要花整篇文章来讨论并发，那么首先明确我们所说的“并发”是什么将非常有益。

本文将深入探讨并发的概念、重要性、面临的挑战，以及Go语言如何通过其并发原语来简化并发编程。我们将结合代码示例（包含中文注释）来阐述这些概念，帮助你更好地理解并应用并发编程。

### 一、什么是并发？

当大多数人使用“并发”这个词时，他们通常指的是多个进程同时发生。通常也暗示这些进程大致在同一时间取得进展。为了更直观地理解这个概念，可以想象为人们。你现在正在阅读这篇文章，而世界上其他人也在同时过着他们的生活。他们与你是并发存在的。

并发在计算机科学中是一个广泛的话题，从这个定义中衍生出了各种主题：理论、并发建模的方法、逻辑正确性、实践问题，甚至包括理论物理学！在本文中，我们将主要关注在Go语言的背景下理解并发的实际问题，特别是：Go如何选择建模并发、这种模型会带来哪些问题，以及我们如何在这个模型中组合原语来解决问题。

### 二、并发的重要性

#### 1. 摩尔定律的终结与多核处理器的崛起

1965年，戈登·摩尔（Gordon Moore）发表了一篇三页的论文，描述了电子市场向集成电路的整合，以及集成电路中组件数量每年翻一番的趋势。这一预测后来被称为“摩尔定律”。1975年，他将这一预测修正为集成电路中的组件数量每两年翻一番。这个预测基本上一直成立，直到2012年左右。

许多公司预见到摩尔定律预测的增长速度将放缓，开始研究提高计算能力的替代方法。正如俗话所说，需求是创新之母，于是多核处理器就这样诞生了。

虽然多核处理器看起来是解决摩尔定律限制的巧妙方法，但计算机科学家很快发现自己面对着另一条定律的限制：阿姆达尔定律（Amdahl’s Law），以计算机架构师吉恩·阿姆达尔（Gene Amdahl）的名字命名。

#### 2. 阿姆达尔定律与并行化的局限

阿姆达尔定律描述了一种模型，用于预测通过并行方式实现问题的解决方案所能带来的性能提升。简单来说，它指出性能提升受到程序中必须以顺序方式编写的部分的限制。

举个例子，假设你正在编写一个主要基于GUI的程序：用户被呈现一个界面，点击一些按钮，然后发生一些操作。这个程序受到一个非常大的顺序部分的限制：人机交互。无论你为这个程序提供多少核，它总是受限于用户与界面交互的速度。

另一方面，考虑计算圆周率的数字。借助一类称为“流水线算法”（spigot algorithms）的算法，这个问题被称为“尴尬并行”（embarrassingly parallel），这实际上是一个技术术语，意味着它可以轻松地划分为并行任务。在这种情况下，通过为程序提供更多的核，可以获得显著的性能提升，你需要处理的只是如何组合和存储结果。

阿姆达尔定律帮助我们理解这两个问题之间的差异，并帮助我们决定并行化是否是解决系统性能问题的正确方法。

#### 3. 云计算与Web规模

对于那些“尴尬并行”的问题，建议你将应用程序编写成可以水平扩展的方式。这意味着你可以运行程序的多个实例，在更多的CPU或机器上运行，从而提高系统的运行速度。

云计算的兴起使得这种水平扩展变得更加容易。云计算意味着一种新的规模和应用程序部署方法，以及水平扩展的方法。开发人员可以使用相对廉价的大量计算能力来解决大型问题。

但是，云计算也带来了许多新的挑战。资源的配置、机器实例之间的通信、结果的汇总和存储都成为需要解决的问题。但其中最困难的之一是如何对代码进行并发建模。并发带来的复杂性增加了程序的理解难度和容错难度。

### 三、为什么并发难以处理？

并发代码因其难以正确实现而臭名昭著。通常需要多次迭代才能使其按预期工作，即使如此，也常常会存在多年后才因某种时机变化（如更高的磁盘利用率、更多的用户登录系统等）而显现的bug。

幸运的是，所有人在处理并发代码时都会遇到相同的问题。正因为如此，计算机科学家们能够为这些常见问题贴上标签，使我们能够讨论它们是如何出现的、为什么会出现，以及如何解决它们。

#### 1. 竞争条件（Race Conditions）

**竞争条件**发生在两个或多个操作必须以正确的顺序执行，但程序未保证这种顺序得到维护的情况下。

通常，这会以数据竞争（data race）的形式出现，其中一个并发操作试图读取一个变量，而在某个不确定的时间，另一个并发操作试图写入同一个变量。

##### 示例：

```
var data int

go func() {
    data++
}()

if data == 0 {
    fmt.Printf("数值是 %v。\n", data)
}
```

在Go语言中，你可以使用`go`关键字来并发地运行一个函数。这会创建一个**goroutine**。

在上述代码中，`data++`和`if data == 0`都在尝试访问变量`data`，但并未保证它们的执行顺序。运行这段代码可能会有三种结果：

* **什么都不打印**：`data++`在`if`语句之前执行。
* **打印“数值是 0。”**：`if`语句在`data++`之前执行。
* **打印“数值是 1。”**：`if data == 0`在`data++`之前执行，但`data++`在`fmt.Printf`之前执行。

仅仅几行代码的错误，就能为你的程序引入巨大的不确定性。

##### 解决方案：

为了避免竞争条件，需要确保操作的执行顺序，可以使用同步机制。例如，使用`sync.WaitGroup`等待goroutine执行完毕。

```
var data int
var wg sync.WaitGroup

wg.Add(1)
go func() {
    defer wg.Done()
    data++
}()

wg.Wait()

if data == 0 {
    fmt.Printf("数值是 %v。\n", data)
} else {
    fmt.Printf("数值是 %v。\n", data)
}
```

在这个示例中，我们使用`wg.Wait()`等待goroutine完成，从而确保`data++`在`if`语句之前执行。

#### 2. 原子性（Atomicity）

**原子性**意味着在操作的上下文中，它是不可分割和不可中断的。这意味着，操作要么全部完成，要么完全不发生。

##### 示例：

```
i++
```

这看起来是一个原子操作，但实际上，它包含多个步骤：

1. 读取`i`的值。
2. 将`i`的值加1。
3. 将新值写回`i`。

虽然每个步骤本身可能是原子的，但组合在一起就不一定是原子的，取决于你的上下文。如果有多个并发操作访问`i`，那么这个增量操作就不是原子的。

##### 解决方案：

为了确保操作的原子性，可以使用`sync/atomic`包提供的原子操作。

```
import "sync/atomic"

var i int32

atomic.AddInt32(&i, 1)
```

使用`atomic.AddInt32`可以确保对`i`的增量操作是原子的。

#### 3. 内存访问同步

当多个并发进程需要访问共享资源时，就需要同步内存访问，以避免竞争条件和数据竞争。

##### 示例：

```
var data int
var mutex sync.Mutex

go func() {
    mutex.Lock()
    data++
    mutex.Unlock()
}()

mutex.Lock()
if data == 0 {
    fmt.Printf("数值是 %v。\n", data)
} else {
    fmt.Printf("数值是 %v。\n", data)
}
mutex.Unlock()
```

在这个示例中，我们使用`sync.Mutex`来确保在同一时间只有一个goroutine可以访问`data`。这解决了数据竞争的问题。

#### 4. 死锁（Deadlock）

**死锁**是指所有的并发进程都在等待彼此，导致程序永远无法继续执行。

##### 示例：

```
type value struct {
    mu    sync.Mutex
    value int
}

var wg sync.WaitGroup

printSum := func(v1, v2 *value) {
    defer wg.Done()

    v1.mu.Lock()
    defer v1.mu.Unlock()

    time.Sleep(2 * time.Second)

    v2.mu.Lock()
    defer v2.mu.Unlock()

    fmt.Printf("sum=%v\n", v1.value+v2.value)
}

var a, b value
wg.Add(2)
go printSum(&a, &b)
go printSum(&b, &a)
wg.Wait()
```

运行这段代码，会出现如下错误：

```
fatal error: all goroutines are asleep - deadlock!
```

这是因为`printSum`函数中的两个goroutine相互等待对方释放锁，导致死锁。

##### 解决方案：

为了避免死锁，可以确保所有的锁按照相同的顺序获取。例如，始终先锁`v1`，再锁`v2`。

```
printSum := func(v1, v2 *value) {
    defer wg.Done()

    if v1 == v2 {
        v1.mu.Lock()
        defer v1.mu.Unlock()
    } else if v1.value < v2.value {
        v1.mu.Lock()
        defer v1.mu.Unlock()
        v2.mu.Lock()
        defer v2.mu.Unlock()
    } else {
        v2.mu.Lock()
        defer v2.mu.Unlock()
        v1.mu.Lock()
        defer v1.mu.Unlock()
    }

    fmt.Printf("sum=%v\n", v1.value+v2.value)
}
```

通过确保锁的获取顺序一致，可以避免死锁的发生。

#### 5. 活锁（Livelock）

**活锁**指的是程序虽然在积极地执行并发操作，但这些操作并没有推进程序的状态。

##### 示例：

假设两个人在走廊相遇，都试图让对方先走。他们不断地左右移动，始终无法通过。

```
var (
    left   int32
    right  int32
    wg     sync.WaitGroup
    cadence = sync.NewCond(&sync.Mutex{})
)

go func() {
    for range time.Tick(1 * time.Millisecond) {
        cadence.Broadcast()
    }
}()

takeStep := func() {
    cadence.L.Lock()
    cadence.Wait()
    cadence.L.Unlock()
}

tryDir := func(dirName string, dir *int32, out *bytes.Buffer) bool {
    fmt.Fprintf(out, " %v", dirName)
    atomic.AddInt32(dir, 1)
    takeStep()

    if atomic.LoadInt32(dir) == 1 {
        fmt.Fprint(out, ". 成功！")
        return true
    }
    takeStep()
    atomic.AddInt32(dir, -1)
    return false
}

walk := func(walking *sync.WaitGroup, name string) {
    var out bytes.Buffer
    defer func() { fmt.Println(out.String()) }()
    defer walking.Done()
    fmt.Fprintf(&out, "%v 正在尝试通过：", name)
    for i := 0; i < 5; i++ {
        if tryLeft(&out) || tryRight(&out) {
            return
        }
    }
    fmt.Fprintf(&out, "\n%v 放弃了！", name)
}

tryLeft := func(out *bytes.Buffer) bool {
    return tryDir("左边", &left, out)
}

tryRight := func(out *bytes.Buffer) bool {
    return tryDir("右边", &right, out)
}

wg.Add(2)
go walk(&wg, "小明")
go walk(&wg, "小红")
wg.Wait()
```

运行结果可能是：

```
小明 正在尝试通过： 左边 右边 左边 右边 左边 右边 左边 右边 左边 右边
小明 放弃了！
小红 正在尝试通过： 左边 右边 左边 右边 左边 右边 左边 右边 左边 右边
小红 放弃了！
```

两个人不断尝试移动，但始终无法通过，形成了活锁。

##### 解决方案：

为了避免活锁，可以引入协调机制或随机性。例如，可以让其中一方等待一段随机的时间再尝试移动，或者引入一个协调者来指挥双方的动作。

#### 6. 饿死（Starvation）

**饿死**是指并发进程无法获取执行工作所需的所有资源，导致无法完成任务。

##### 示例：

```
var wg sync.WaitGroup
var sharedLock sync.Mutex
const run...