---
title: Go语言结构体和元组全面解析
url: https://blog.csdn.net/nokiaguy/article/details/142001762
source: 一个被知识诅咒的人
date: 2024-09-08
fetch_date: 2025-10-06T18:23:03.436293
---

# Go语言结构体和元组全面解析

# Go语言结构体和元组全面解析

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-09-07 20:19:01 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.4k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

13

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
28

CC 4.0 BY-SA版权

分类专栏：
[《Go语言编程全解--理论与实践》](https://blog.csdn.net/nokiaguy/category_12773266.html)
文章标签：
[golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[后端](https://so.csdn.net/so/search/s.do?q=%E5%90%8E%E7%AB%AF&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[go](https://so.csdn.net/so/search/s.do?q=go&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142001762>

[![](https://i-blog.csdnimg.cn/direct/6d4320254d4d47de985b6dbab91d4b6f.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

《Go语言编程全解--理论与实践》
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12773266.html "《Go语言编程全解--理论与实践》")

25 篇文章

订阅专栏

## Go语言中的复合类型与其应用

在编程中，标准类型虽然方便，但无法满足所有需求。Go通过支持结构体和元组类型，为开发者提供了自定义数据类型的能力。本文将介绍如何定义结构体、如何使用指针操作结构体、如何通过元组返回多个值等内容，并结合实际示例展示这些功能的强大之处。

#### 复合类型简介

Go的标准类型，如整型、浮点型等，虽然非常灵活和高效，但它们无法涵盖所有数据需求。当我们需要自定义复杂数据类型时，可以使用结构体。Go语言还提供了类似元组的支持，使得函数可以返回多个值，而无需像C语言那样将它们分组到结构体中。

#### 结构体的使用

数组、切片和映射虽然实用，但它们无法将不同类型的数据聚合在一起。当需要将多个不同类型的变量组合成一个新类型时，结构体便派上用场。结构体的每个元素被称为字段。下面通过一个简单的例子来了解如何定义和使用结构体：

```
type aStructure struct {
    person string
    height int
    weight int
}
```

这个结构体包含了三种不同的字段：`person`、`height` 和 `weight`。可以通过以下方式创建一个结构体变量：

```
var s1 aStructure
```

通过字段名称访问结构体中的某个值，例如：`s1.person`。

结构体字面量可以这样定义：

```
p1 := aStructure{"张三", 175, 65}
```

然而，为了避免记忆字段顺序的麻烦，Go允许我们在定义字面量时通过字段名来初始化：

```
p1 := aStructure{weight: 65, height: 175}
```

这种方式更加清晰，不必为每个字段都赋初始值。接下来展示一个更实用的例子。

#### 结构体的实际应用

接下来，我们来看一个更复杂的例子`structures.go`，这个程序展示了如何在函数中定义结构体并操作它们。

```
package main
import (
    "fmt"
)

func main() {
    type XYZ struct {
        X int
        Y int
        Z int
    }

    var s1 XYZ
    fmt.Println(s1.Y, s1.Z)  // 输出结构体字段Y和Z的值
}
```

在这个例子中，`XYZ`结构体类型被定义在`main`函数内部，这意味着它只能在当前函数内使用。虽然通常我们会在全局定义结构体以便整个包使用，但局部定义结构体有助于隔离作用域。

接下来，创建两个结构体实例并打印它们：

```
p1 := XYZ{23, 12, -2}
p2 := XYZ{Z: 12, Y: 13}
fmt.Println(p1)  // 打印结构体p1
fmt.Println(p2)  // 打印结构体p2
```

最后，展示如何将结构体存储在数组中：

```
pSlice := [4]XYZ{}
pSlice[2] = p1
pSlice[0] = p2
fmt.Println(pSlice)  // 打印结构体数组
```

执行上述程序，输出结果如下：

```
0 0
{23 12 -2}
{0 13 12}
[{0 13 12} {0 0 0} {23 12 -2} {0 0 0}]
```

我们可以看到，结构体的零值是根据其字段类型的默认值来设置的。改变`p2`的值并不会影响已存储在数组中的结构体。

#### 结构体指针的使用

指针是Go中强大的工具，可以避免复制大量数据。我们来看一个与结构体指针相关的例子`pointerStruct.go`。

首先，定义结构体：

```
package main
import (
    "fmt"
)

type myStructure struct {
    Name    string
    Surname string
    Height  int32
}
```

接下来，通过函数创建并返回结构体指针：

```
func createStruct(n, s string, h int32) *myStructure {
    if h > 300 {
        h = 0  // 校验身高是否合法
    }
    return &myStructure{n, s, h}
}
```

这个函数通过返回结构体的指针，避免了结构体的大量复制。也可以直接返回结构体：

```
func retStructure(n, s string, h int32) myStructure {
    if h > 300 {
        h = 0
    }
    return myStructure{n, s, h}
}
```

通过这两种方式创建的结构体，在使用上有一些差异。以下是测试代码：

```
func main() {
    s1 := createStruct("李雷", "王花", 180)
    s2 := retStructure("李雷", "王花", 180)

    fmt.Println((*s1).Name)  // 输出结构体指针指向的Name
    fmt.Println(s2.Name)     // 直接输出结构体的Name
    fmt.Println(s1)          // 打印结构体指针
    fmt.Println(s2)          // 打印结构体
}
```

运行结果如下：

```
李雷
李雷
&{李雷 王花 180}
{李雷 王花 180}
```

#### 使用`new`关键字

Go支持使用`new`关键字来分配内存，并返回对象的内存地址。例如：

```
pS := new(aStructure)
```

通过`new`创建的结构体，所有字段的值都被初始化为零值。需要注意的是，`new`仅返回对象的指针，而`make`则不仅分配内存，还会对切片、映射和通道进行初始化。

#### 元组与多返回值

虽然Go语言不直接支持元组类型，但函数可以返回多个值，具有类似元组的效果。来看一个返回三个值的函数：

```
package main
import (
    "fmt"
)

func retThree(x int) (int, int, int) {
    return 2 * x, x * x, -x
}

func main() {
    fmt.Println(retThree(10))         // 输出三个返回值
    n1, n2, n3 := retThree(20)        // 接收返回值
    fmt.Println(n1, n2, n3)

    n1, n2 = n2, n1  // 交换值
    fmt.Println(n1, n2, n3)
}
```

运行结果：

```
20 100 -10
40 400 -20
400 40 -20
```

元组的这种用法非常实用，例如用于交换值，或忽略某些返回值。

#### 结论

通过结构体和元组，Go提供了强大的复合类型支持，让我们能够更好地组织和操作复杂的数据。在实际编程中，充分利用这些特性能够提高代码的可读性和效率。

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

  28

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  13

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
3139

[《奇妙的Python——神奇代...