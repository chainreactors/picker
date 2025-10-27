---
title: Go语言中的队列与栈：基础与实践
url: https://blog.csdn.net/nokiaguy/article/details/142095958
source: 一个被知识诅咒的人
date: 2024-09-11
fetch_date: 2025-10-06T18:26:13.106724
---

# Go语言中的队列与栈：基础与实践

# Go语言中的队列与栈：基础与实践

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-09-10 12:55:35 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量938
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

6

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
6

CC 4.0 BY-SA版权

分类专栏：
[《Go语言编程全解--理论与实践》](https://blog.csdn.net/nokiaguy/category_12773266.html)
文章标签：
[golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[后端](https://so.csdn.net/so/search/s.do?q=%E5%90%8E%E7%AB%AF&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[go](https://so.csdn.net/so/search/s.do?q=go&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142095958>

[![](https://i-blog.csdnimg.cn/direct/6d4320254d4d47de985b6dbab91d4b6f.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

《Go语言编程全解--理论与实践》
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12773266.html "《Go语言编程全解--理论与实践》")

25 篇文章

订阅专栏

在日常编程中，数据结构是不可或缺的一部分。无论是开发复杂的系统，还是编写小型工具，选择合适的数据结构都能显著提高程序的效率和可读性。在Go语言中，队列和栈是两种常用的基础数据结构。本文将详细介绍如何在Go中实现队列与栈，并补充一些扩展内容，以帮助大家更好地理解和应用这些结构。

### 队列：先进先出（FIFO）的数据结构

队列（Queue）是一种特殊的链表结构，新元素总是插入到链表的头部，删除元素则从尾部开始。你可以想象排队去银行办事，只有前面的人完成了业务，你才能上前与柜员交谈。这种“先来先服务”的处理方式就是队列的本质。

#### 队列的优势

队列的最大优势在于它的简单性。我们只需要两个函数：一个用于向队列添加元素，另一个用于从队列中移除元素。由于操作有限，这也意味着程序中出错的概率更低。同时，队列的实现方式也相对灵活，只要能支持这两个操作，具体的实现方式是多种多样的。

#### Go语言中的队列实现

下面是一个基于链表的队列实现示例，我们通过编写`Push()`和`Pop()`函数，分别实现添加和移除节点的功能。

##### 定义节点结构与全局变量

```
package main

import (
    "fmt"
)

type Node struct {
    Value int     // 节点存储的值
    Next  *Node   // 指向下一个节点的指针
}

var size = 0     // 用于记录队列的大小
var queue *Node  // 队列的头节点
```

在上面的代码中，我们定义了一个`Node`结构体，它包含一个存储值的字段`Value`，以及指向下一个节点的指针`Next`。此外，使用全局变量`size`记录队列中的元素个数，`queue`作为队列的起始节点。

##### 实现Push函数

`Push()`函数用于向队列中添加元素。它通过创建一个新节点，并将其插入到队列的头部。

```
func Push(t *Node, v int) bool {
    if queue == nil {
        queue = &Node{v, nil} // 如果队列为空，则新节点成为队列的第一个节点
        size++
        return true
    }
    t = &Node{v, nil}       // 创建新节点
    t.Next = queue          // 将新节点插入到队列的头部
    queue = t
    size++
    return true
}
```

这个`Push()`函数逻辑简单：当队列为空时，直接将新节点作为队列的起始节点。否则，新节点插入队列的头部，成为新的队列头。

##### 实现Pop函数

`Pop()`函数用于从队列中移除最早加入的元素（队尾元素）。如果队列为空，返回`false`表示无法移除元素。

```
func Pop(t *Node) (int, bool) {
    if size == 0 {
        return 0, false // 队列为空时，无法移除元素
    }
    if size == 1 {
        queue = nil      // 只有一个元素时，移除后队列为空
        size--
        return t.Value, true
    }

    temp := t
    for t.Next != nil {  // 遍历队列找到最后一个节点
        temp = t
        t = t.Next
    }
    v := temp.Next.Value // 取出队尾元素的值
    temp.Next = nil      // 移除队尾节点
    size--
    return v, true
}
```

这个`Pop()`函数根据队列的大小执行不同的操作：如果队列只有一个元素，则直接将队列设为空；如果队列有多个元素，则遍历到队尾并移除它。

##### 遍历队列的辅助函数

为了更直观地查看队列中的元素，我们可以实现一个`traverse()`函数，用于遍历并打印队列的所有节点。

```
func traverse(t *Node) {
    if size == 0 {
        fmt.Println("队列为空！")
        return
    }
    for t != nil {
        fmt.Printf("%d -> ", t.Value)
        t = t.Next
    }
    fmt.Println()
}
```

这个函数会从队列头开始，依次输出每个节点的值，直到遍历完所有节点。

##### 主函数测试

下面是主函数，通过调用`Push()`和`Pop()`函数来测试队列的功能。

```
func main() {
    queue = nil
    Push(queue, 10)
    fmt.Println("队列大小:", size)
    traverse(queue)

    v, b := Pop(queue)
    if b {
        fmt.Println("移除元素:", v)
    }
    fmt.Println("队列大小:", size)

    for i := 0; i < 5; i++ {
        Push(queue, i)
    }
    traverse(queue)
    fmt.Println("队列大小:", size)

    v, b = Pop(queue)
    if b {
        fmt.Println("移除元素:", v)
    }
    fmt.Println("队列大小:", size)

    traverse(queue)
}
```

运行结果将显示队列的操作过程：

```
队列大小: 1
10 ->
移除元素: 10
队列大小: 0
4 -> 3 -> 2 -> 1 -> 0 ->
队列大小: 5
移除元素: 0
队列大小: 4
4 -> 3 -> 2 ->
```

通过上面的代码，我们可以看到，队列的操作符合先进先出的原则。

---

### 栈：后进先出（LIFO）的数据结构

栈（Stack）是一种与队列类似的数据结构，但其操作规则是“后进先出”，即最后进入栈的元素会最先被取出。这种结构可以类比为堆叠的盘子，最上面的盘子总是最先被使用。

#### Go语言中的栈实现

栈的实现与队列非常相似，都是基于链表。在实现过程中，我们需要两个核心函数：`Push()`用于添加元素，`Pop()`用于移除元素。

##### 定义节点结构与全局变量

```
package main

import (
    "fmt"
)

type Node struct {
    Value int     // 节点存储的值
    Next  *Node   // 指向下一个节点的指针
}

var size = 0     // 用于记录栈的大小
var stack *Node  // 栈的顶端节点
```

##### 实现Push函数

`Push()`函数用于向栈中添加元素，将新元素放在栈的顶部。

```
func Push(v int) bool {
    if stack == nil {
        stack = &Node{v, nil} // 如果栈为空，创建第一个节点
        size = 1
        return true
    }
    temp := &Node{v, nil}   // 创建新节点
    temp.Next = stack       // 新节点指向当前栈顶
    stack = temp            // 更新栈顶为新节点
    size++
    return true
}
```

##### 实现Pop函数

`Pop()`函数用于移除栈顶元素，并返回其值。

```
func Pop() (int, bool) {
    if size == 0 {
        return 0, false // 栈为空时，无法移除元素
    }
    v := stack.Value
    stack = stack.Next  // 移除栈顶元素
    size--
    return v, true
}
```

##### 主函数测试

我们可以通过以下主函数来测试栈的功能：

```
func main() {
    v, b := Pop()
    if !b {
        fmt.Println("栈为空，无法弹出元素")
    }

    Push(100)
    Push(200)
    for i := 0; i < 5; i++ {
        Push(i)
    }

    for i := 0; i < 6; i++ {
        v, b := Pop()
        if b {
            fmt.Println("弹出元素:", v)
        }
    }
}
```

运行结果如下：

```
栈为空，无法弹出元素
弹出元素: 4
弹出元素: 3
弹出元素: 2
弹出元素: 1
弹出元素: 0
弹出元素: 200
```

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

  6

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  6

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

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不...