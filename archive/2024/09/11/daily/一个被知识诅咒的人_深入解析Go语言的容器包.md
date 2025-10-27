---
title: 深入解析Go语言的容器包
url: https://blog.csdn.net/nokiaguy/article/details/142096002
source: 一个被知识诅咒的人
date: 2024-09-11
fetch_date: 2025-10-06T18:26:12.448596
---

# 深入解析Go语言的容器包

# 深入解析Go语言的容器包

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)Go语言环形链表与双向链表实现及应用

原创
于 2024-09-10 12:59:07 发布
·
1k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

18

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

8
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#windows](https://so.csdn.net/so/search/s.do?q=windows&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#go](https://so.csdn.net/so/search/s.do?q=go&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[![](https://i-blog.csdnimg.cn/direct/6d4320254d4d47de985b6dbab91d4b6f.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

《Go语言编程全解--理论与实践》
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12773266.html "《Go语言编程全解--理论与实践》")

25 篇文章

订阅专栏

在Go语言中，`container`标准包为开发者提供了三个非常有用的数据结构：堆（heap）、链表（list）和环（ring）。这些数据结构的实现分别位于`container/heap`、`container/list`和`container/ring`中。理解这些数据结构以及它们的实现方式，可以帮助我们更高效地处理各种复杂的数据存储和操作任务。

### 环形链表简介

环（ring）是一种特殊的链表，它的最后一个元素指向第一个元素，这意味着它没有明确的起点和终点。环形链表中的每个节点在逻辑上是等价的，可以从任何一个节点开始遍历整个环。通过这种结构，我们可以方便地循环遍历数据。

#### 链表的应用

环形链表在许多实际应用中非常有用。例如，假设你有一组固定大小的数据，想要在这组数据之间不停循环操作，环形链表能够避免重新初始化数据的开销。此外，环形链表在某些游戏循环、操作系统调度器等需要循环处理任务的场景中非常常见。

#### 开始使用`container/ring`

接下来，我们将通过代码示例来介绍如何使用`container/ring`包。在此之前，先简单解释一下它的基本操作。`container/ring`包提供了少量函数，其中最重要的就是`Next()`和`Do()`。`Next()`函数用于获取当前节点的下一个节点，`Do()`函数则用于对环中的每个节点执行指定操作。

##### 示例代码：创建环形链表

首先，我们定义一个环形链表的大小，并使用`ring.New()`来初始化一个环：

```
package main

import (
    "container/ring"
    "fmt"
)

var size int = 10  // 环的大小

func main() {
    myRing := ring.New(size + 1) // 创建一个大小为size+1的环
    fmt.Println("空环:", *myRing)

    // 给环形链表的每个节点赋值
    for i := 0; i < myRing.Len()-1; i++ {
        myRing.Value = i
        myRing = myRing.Next()
    }

    myRing.Value = 2  // 在最后一个节点赋值
}
```

在这个代码段中，我们首先创建了一个大小为`size+1`的环。然后，通过一个`for`循环为环中的每个节点赋值。在最后一步，我们手动将最后一个节点的值设置为`2`，尽管该值在循环中已经出现过。

##### 使用`Do()`函数遍历环

我们可以使用`ring.Do()`来遍历环中的每个节点，并对节点值进行操作。下面的代码将遍历环中的每个节点，并计算节点值的总和：

```
sum := 0
myRing.Do(func(x interface{}) {
    t := x.(int)  // 类型断言，确保节点的值是整数
    sum += t      // 累加每个节点的值
})
fmt.Println("总和:", sum)
```

`ring.Do()`是一个非常简洁的遍历方式，它通过传入一个函数，依次处理环中的每个元素。如果你不修改环中的结构，`Do()`函数可以安全使用，且代码更加简洁。

##### 使用`Next()`函数遍历环

虽然`Do()`是遍历环的简洁方式，但你也可以通过`Next()`函数手动遍历环：

```
for i := 0; i < myRing.Len()+2; i++ {
    myRing = myRing.Next()  // 获取下一个节点
    fmt.Print(myRing.Value, " ")
}
fmt.Println()
```

在这个例子中，我们使用`Next()`函数遍历了环，并输出了每个节点的值。需要注意的是，由于环没有明确的终点，调用`Next()`可以无限次循环，因此我们通过`Len()`函数来控制循环次数。

#### 执行结果

当你运行上面的代码时，输出可能类似如下：

```
空环: {0xc00000a080 0xc00000a1a0 <nil>}
总和: 45
0 1 2 3 4 5 6 7 8 9 2 0 1
```

可以看到，环中可以包含重复值，并且遍历过程中，环会不断循环下去，除非我们人为设定结束条件。

---

### 使用`container/list`实现链表

与环形链表不同，链表（list）是一种线性数据结构，每个节点指向下一个节点。在Go的`container/list`包中，实现了一个双向链表（doubly linked list），既可以从头遍历到尾，也可以从尾遍历到头。双向链表的优点是我们可以方便地插入和删除元素。

#### 链表的基本操作

`container/list`包提供了链表的基本操作，比如插入、删除、遍历等。下面我们通过一个完整的例子，来演示如何使用这些操作。

##### 示例代码：链表的创建与操作

```
package main

import (
    "container/list"
    "fmt"
    "strconv"
)

func printList(l *list.List) {
    // 从尾部向头部遍历
    for t := l.Back(); t != nil; t = t.Prev() {
        fmt.Print(t.Value, " ")
    }
    fmt.Println()

    // 从头部向尾部遍历
    for t := l.Front(); t != nil; t = t.Next() {
        fmt.Print(t.Value, " ")
    }
    fmt.Println()
}

func main() {
    values := list.New()        // 创建一个新的链表
    e1 := values.PushBack("一")  // 插入元素到链表尾部
    e2 := values.PushBack("二")
    values.PushFront("三")      // 插入元素到链表头部
    values.InsertBefore("四", e1) // 在e1之前插入"四"
    values.InsertAfter("五", e2)  // 在e2之后插入"五"

    values.Remove(e2)           // 移除元素e2
    printList(values)

    values.Init()               // 初始化链表
    fmt.Println("链表初始化后:", values)

    // 插入一组数字
    for i := 0; i < 10; i++ {
        values.PushFront(strconv.Itoa(i))
    }
    printList(values)
}
```

在这个代码段中，我们演示了链表的常见操作，包括在链表的头部和尾部插入元素、在指定元素前后插入新元素、移除元素以及遍历链表。

#### 执行结果

当你运行上面的代码时，输出可能如下：

```
五 四 一 三
三 一 四 五
链表初始化后: &{{0xc000012000 0xc000012000 <nil> <nil>} 0}
9 8 7 6 5 4 3 2 1 0
0 1 2 3 4 5 6 7 8 9
```

可以看到，链表的初始化将链表清空，之后的循环插入操作重新填充了链表。

通过本文的介绍，我们详细讲解了Go语言中`container`包的环形链表和双向链表的实现与应用。掌握这些数据结构后，你可以在需要灵活的数据存储和遍历时高效地选择合适的结构。

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

  18

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

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HD...