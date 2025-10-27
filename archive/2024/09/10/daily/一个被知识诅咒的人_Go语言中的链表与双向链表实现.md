---
title: Go语言中的链表与双向链表实现
url: https://blog.csdn.net/nokiaguy/article/details/142056191
source: 一个被知识诅咒的人
date: 2024-09-10
fetch_date: 2025-10-06T18:25:07.908811
---

# Go语言中的链表与双向链表实现

# Go语言中的链表与双向链表实现

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)Go语言实现链表与双向链表

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-09-09 13:06:24 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.4k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

8

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
19

CC 4.0 BY-SA版权

分类专栏：
[《Go语言编程全解--理论与实践》](https://blog.csdn.net/nokiaguy/category_12773266.html)
文章标签：
[golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[链表](https://so.csdn.net/so/search/s.do?q=%E9%93%BE%E8%A1%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[go](https://so.csdn.net/so/search/s.do?q=go&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142056191>

[![](https://i-blog.csdnimg.cn/direct/6d4320254d4d47de985b6dbab91d4b6f.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

《Go语言编程全解--理论与实践》
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12773266.html "《Go语言编程全解--理论与实践》")

25 篇文章

订阅专栏

### 链表基础

链表是一种由有限元素组成的数据结构，其中每个元素至少使用两个内存空间：一个存储实际数据，另一个存储指向下一个元素的指针，从而形成一个元素序列构成链表。链表的第一个元素称为头结点，而最后一个元素通常被称为尾结点。为了操作链表，保持对头结点的引用非常重要，因为头结点是我们访问整个链表的唯一入口。如果丢失了指向头结点的指针，将无法再次找到链表的其他元素。

#### 链表的操作

在链表中，移除节点时，主要操作是调整要删除节点的前一个节点的指针，使其指向要删除节点的下一个节点。

#### Go中的链表实现

我们通过Go语言的链表实现来更好地理解链表的操作过程。

```
package main

import (
    "fmt"
)

// 定义链表节点结构
type Node struct {
    Value int
    Next  *Node
}

// 全局变量root，保存链表的头结点
var root = new(Node)
```

在以上代码中，定义了链表节点的结构，包含一个`Value`用于存储节点的值，一个`Next`指针指向链表的下一个节点。此外，还定义了一个全局变量`root`，用于保存链表的头结点。

#### 添加节点

链表通常不允许重复元素，并且当链表未排序时，新节点通常添加到链表末尾。以下是添加节点的代码实现：

```
func addNode(t *Node, v int) int {
    if root == nil {
        t = &Node{v, nil}
        root = t
        return 0
    }
    if v == t.Value {
        fmt.Println("节点已存在:", v)
        return -1
    }
    if t.Next == nil {
        t.Next = &Node{v, nil}
        return -2
    }
    return addNode(t.Next, v)
}
```

在`addNode`函数中，首先检查链表是否为空，如果为空，则将新节点作为头结点插入。接着，检查链表中是否已有待插入的值，避免重复元素。如果当前节点的`Next`指针为空，说明已到达链表末尾，便将新节点添加到链表的末尾。若以上情况均不满足，则递归地继续检查下一个节点。

#### 遍历链表

遍历链表的代码如下：

```
func traverse(t *Node) {
    if t == nil {
        fmt.Println("-> 空链表!")
        return
    }
    for t != nil {
        fmt.Printf("%d -> ", t.Value)
        t = t.Next
    }
    fmt.Println()
}
```

`traverse`函数通过循环遍历链表，并输出每个节点的值，直到遍历到最后一个节点。

#### 查找节点与计算链表长度

```
func lookupNode(t *Node, v int) bool {
    if root == nil {
        t = &Node{v, nil}
        root = t
        return false
    }
    if v == t.Value {
        return true
    }
    if t.Next == nil {
        return false
    }
    return lookupNode(t.Next, v)
}

func size(t *Node) int {
    if t == nil {
        fmt.Println("-> 空链表!")
        return 0
    }
    i := 0
    for t != nil {
        i++
        t = t.Next
    }
    return i
}
```

`lookupNode`用于检查链表中是否存在某个值，而`size`函数用于计算链表的长度，即节点的数量。通过递归或循环，分别遍历链表的每个节点，返回结果。

#### 主函数测试

```
func main() {
    fmt.Println(root)
    root = nil
    traverse(root)
    addNode(root, 1)
    addNode(root, -1)
    traverse(root)
    addNode(root, 10)
    addNode(root, 5)
    addNode(root, 45)
    traverse(root)
    if lookupNode(root, 100) {
        fmt.Println("节点存在!")
    } else {
        fmt.Println("节点不存在!")
    }
    fmt.Println("链表长度:", size(root))
}
```

输出结果：

```
&{0 <nil>}
-> 空链表!
1 -> -1 ->
1 -> -1 -> 10 -> 5 -> 45 ->
节点不存在!
链表长度: 5
```

### 链表的优势

链表的优势在于其灵活性和实现的简单性，适合处理各种数据类型。链表在进行顺序查找时效率较高，特别是在动态数据管理（如插入和删除）时优于数组等静态数据结构。此外，链表可以动态增长，且删除节点的操作较为简单，尤其是有序链表。

### 双向链表

双向链表是一种特殊的链表结构，每个节点不仅有一个指向下一个节点的指针，还有一个指向前一个节点的指针。这样可以实现双向遍历。双向链表的头节点的前一个节点为`nil`，尾节点的下一个节点也为`nil`。

#### Go中的双向链表实现

双向链表的节点定义如下：

```
type Node struct {
    Value    int
    Previous *Node
    Next     *Node
}
```

该结构体中有两个指针字段：一个指向前一个节点，一个指向下一个节点。

#### 添加节点

```
func addNode(t *Node, v int) int {
    if root == nil {
        t = &Node{v, nil, nil}
        root = t
        return 0
    }
    if v == t.Value {
        fmt.Println("节点已存在:", v)
        return -1
    }
    if t.Next == nil {
        temp := t
        t.Next = &Node{v, temp, nil}
        return -2
    }
    return addNode(t.Next, v)
}
```

与单链表类似，双向链表的节点通常添加到链表末尾。

#### 遍历与反向遍历

```
func traverse(t *Node) {
    if t == nil {
        fmt.Println("-> 空链表!")
        return
    }
    for t != nil {
        fmt.Printf("%d -> ", t.Value)
        t = t.Next
    }
    fmt.Println()
}

func reverse(t *Node) {
    if t == nil {
        fmt.Println("-> 空链表!")
        return
    }
    temp := t
    for t != nil {
        temp = t
        t = t.Next
    }
    for temp.Previous != nil {
        fmt.Printf("%d -> ", temp.Value)
        temp = temp.Previous
    }
    fmt.Printf("%d -> ", temp.Value)
    fmt.Println()
}
```

`reverse`函数实现了反向遍历，先遍历到链表末尾，再通过`Previous`指针反向输出节点值。

#### 双向链表的优势

双向链表相比单链表，优势在于可以进行双向遍历，删除和插入操作更加灵活。如果丢失了头结点的指针，仍可以通过尾节点找到链表的其他节点。但双向链表需要维护两个指针，增加了存储空间的消耗和代码的复杂性。

### 结语

链表和双向链表作为基础的数据结构，在处理动态数据和顺序查找中具有显著优势。通过对Go语言中链表的实现，读者可以更深入理解如何在实际开发中使用这些数据结构来提高程序的性能和可维护性。

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

  19

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

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不面对一个核心问题：AIGC将如何影响未来的工作？会让人类的大多数工作消失，还是会创造出全新的职业机会？](https:/...