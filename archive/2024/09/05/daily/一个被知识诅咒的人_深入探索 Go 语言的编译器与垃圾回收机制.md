---
title: 深入探索 Go 语言的编译器与垃圾回收机制
url: https://blog.csdn.net/nokiaguy/article/details/141888638
source: 一个被知识诅咒的人
date: 2024-09-05
fetch_date: 2025-10-06T18:23:57.829562
---

# 深入探索 Go 语言的编译器与垃圾回收机制

# 深入探索 Go 语言的编译器与垃圾回收机制

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)Go语言编译器与垃圾回收机制解析

原创
于 2024-09-04 11:22:59 发布
·
1.5k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

13

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

7
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#后端](https://so.csdn.net/so/search/s.do?q=%E5%90%8E%E7%AB%AF&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[![](https://i-blog.csdnimg.cn/direct/6d4320254d4d47de985b6dbab91d4b6f.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

《Go语言编程全解--理论与实践》
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12773266.html "《Go语言编程全解--理论与实践》")

25 篇文章

订阅专栏

Go 编译器

Go 编译器是通过 go 工具执行的，这个工具的功能不仅仅是生成可执行文件。你可以使用 `go tool compile` 命令来编译一个 Go 源文件。这个操作将生成一个目标文件，也就是 `.o` 后缀的文件。以下是在 macOS Mojave 系统上执行的命令和结果展示：

```
$ go tool compile unsafe.go
$ ls -l unsafe.o
-rw-r--r--  1 mtsouk  staff  6926 Jan 22 21:39 unsafe.o
$ file unsafe.o
unsafe.o: current ar archive
```

目标文件是一种包含机器代码的文件，通常是不可直接执行的。它的一个主要优势在于在链接阶段所需的内存更少。如果你使用 `-pack` 命令行参数，`go tool compile` 会生成一个归档文件，而不是目标文件：

```
$ go tool compile -pack unsafe.go
$ ls -l unsafe.a
-rw-r--r--  1 mtsouk  staff  6926 Jan 22 21:40 unsafe.a
$ file unsafe.a
unsafe.a: current ar archive
```

归档文件是一种二进制文件，包含一个或多个文件，主要用于将多个文件合并为一个文件。`ar` 是其中一种格式，Go 使用的就是这种格式。这个示例中的 `unsafe.go` 文件不包含任何特殊代码，以上的命令适用于任何有效的 Go 源文件。

#### 查看归档文件内容

你可以使用以下命令查看 `.a` 归档文件的内容：

```
$ ar t unsafe.a
__.PKGDEF
_go_.o
```

#### `-race` 标志

另一个值得一提的 `go tool compile` 命令行参数是 `-race`，它可以检测竞态条件。在并发编程中，竞态条件可能导致意想不到的错误。你可以通过以下命令生成汇编语言的输出：

```
$ go tool compile -S unsafe.go
```

这个命令会生成大量的输出，虽然它难以理解，但这意味着 Go 编译器很好地隐藏了复杂性，除非你主动要求查看这些细节。

#### 垃圾回收

垃圾回收（GC）是释放未被使用的内存空间的过程，换句话说，GC 会找到那些已经超出作用范围且无法再被引用的对象，并释放它们占用的内存空间。这个过程是在 Go 程序运行时以并发方式执行的，而不是在程序执行前或执行后才开始。Go 垃圾回收的官方文档中提到：

> “GC 与变更线程并发运行，精确类型化（也称为精确），允许多个 GC 线程并行运行。它是并发标记-清除，使用写屏障，非代际且非压缩。分配采用大小分离的每 P 分配区，以最小化碎片化，同时在常见情况下消除锁。”

其中涉及到许多术语，接下来我们会逐一解释。首先，我会展示一个查看垃圾回收过程参数的方法。

#### 使用标准库查看垃圾回收参数

幸运的是，Go 标准库提供了一些函数，可以帮助我们了解垃圾回收的运行方式。下面的代码展示了如何获取垃圾回收的相关信息：

```
package main

import (
   "fmt"
   "runtime"
   "time"
)

func printStats(mem runtime.MemStats) {
   runtime.ReadMemStats(&mem)
   fmt.Println("当前内存分配:", mem.Alloc)
   fmt.Println("内存总分配:", mem.TotalAlloc)
   fmt.Println("堆内存分配:", mem.HeapAlloc)
   fmt.Println("垃圾回收次数:", mem.NumGC)
   fmt.Println("-----")
}
```

每当你需要获取最新的垃圾回收统计信息时，你需要调用 `runtime.ReadMemStats()` 函数。`printStats()` 函数用于打印这些信息，以避免重复编写相同的代码。

接下来的部分创建了大量的 Go 切片，以分配大量内存并触发垃圾回收：

```
func main() {
   var mem runtime.MemStats
   printStats(mem)
   for i := 0; i < 10; i++ {
      s := make([]byte, 50000000)
      if s == nil {
         fmt.Println("操作失败！")
      }
      printStats(mem)
   }
}
```

最后一部分代码做了更多的内存分配操作：

```
for i := 0; i < 10; i++ {
   s := make([]byte, 100000000)
   if s == nil {
      fmt.Println("操作失败！")
   }
   time.Sleep(5 * time.Second)
}
printStats(mem)
```

运行上述代码的输出如下（以 macOS Mojave 为例）：

```
$ go run gColl.go
当前内存分配: 66024
内存总分配: 66024
堆内存分配: 66024
垃圾回收次数: 0
-----
当前内存分配: 50078496
内存总分配: 500117056
堆内存分配: 50078496
垃圾回收次数: 10
-----
当前内存分配: 76712
内存总分配: 1500199904
堆内存分配: 76712
垃圾回收次数: 20
-----
```

#### 深入理解垃圾回收

观察垃圾回收的行为能够帮助你在性能较慢的应用中发现问题。你可以通过以下命令查看更详细的 GC 信息：

```
$ GODEBUG=gctrace=1 go run gColl.go
```

输出会显示每次垃圾回收的详细数据。例如：

```
gc 4 @0.025s 0%: 0.002+0.065+0.018 ms clock, 47->47->0 MB, 48 MB goal
```

#### 三色标记-清除算法

Go 的垃圾回收基于三色标记-清除算法。这个算法将堆中的对象分为三类：白色、灰色和黑色。白色对象是垃圾回收的候选对象，而灰色对象可能指向白色对象，黑色对象则不会指向白色对象。

当垃圾回收开始时，所有对象最初是白色的，垃圾回收器会将根对象标记为灰色，并继续扫描灰色对象。如果灰色对象指向白色对象，它会将这些白色对象标记为灰色，最终所有不可达的白色对象会被回收。

在程序运行过程中，如果某个对象变得可达，写屏障机制会将其重新标记为灰色，确保其不会被错误回收。

这个三色标记-清除算法不仅适用于 Go，还可以应用于其他编程语言。

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

  13

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  7

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

  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/report.png)
  举报

专栏目录

参与评论
您还未登录，请先
登录
后发表或查看评论

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[AIGC撕裂劳动力市场：技术狂潮下，人类将走向乌托邦还是深渊？](https://unitymarvel.blog.csdn.net/article/details/145234235)

01-18
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2558

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不面对一个核心问题：AIGC将如何影响未来的工作？会让人类的大多数工作消失，还是会创造出全新的职业机会？](https://unitymarvel.blog.csdn.net/article/details/145234235)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【Python图形图像】《Python OpenCV从菜鸟到高手》——零基础进阶，开启图像处理与计算机视觉的大门！](https://unitymarvel.blog.csdn.net/article/details/143574491)

11-07
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2250

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与计算机视觉的利器。本书通过循序渐进的方式，让读者从零基础到掌握高级图像处理技能，帮助你实现从初学者到高手的跃升。](https://unitymarvel.blog.csdn.net/article/details/143574491)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

09-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3140

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.csdn.net/article/details/151067555)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1049

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码...