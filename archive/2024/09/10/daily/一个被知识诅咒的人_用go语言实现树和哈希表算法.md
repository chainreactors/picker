---
title: 用go语言实现树和哈希表算法
url: https://blog.csdn.net/nokiaguy/article/details/142056091
source: 一个被知识诅咒的人
date: 2024-09-10
fetch_date: 2025-10-06T18:25:09.059519
---

# 用go语言实现树和哈希表算法

# 用go语言实现树和哈希表算法

原创
于 2024-09-09 12:59:25 发布
·
980 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

21

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

12
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#算法](https://so.csdn.net/so/search/s.do?q=%E7%AE%97%E6%B3%95&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#散列表](https://so.csdn.net/so/search/s.do?q=%E6%95%A3%E5%88%97%E8%A1%A8&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#go](https://so.csdn.net/so/search/s.do?q=go&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[![](https://i-blog.csdnimg.cn/direct/6d4320254d4d47de985b6dbab91d4b6f.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

《Go语言编程全解--理论与实践》
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12773266.html "《Go语言编程全解--理论与实践》")

25 篇文章

订阅专栏

### 算法复杂度

判断一个算法的效率通常基于其计算复杂度，这主要与算法访问输入数据的次数有关。计算机科学中常用大O表示法来描述算法的复杂度。例如，O(n)的算法只需访问一次输入数据，因此优于O(n²)的算法，后者则优于O(n³)的算法，依此类推。最差的算法是O(n!)的复杂度，当输入数据超过300个元素时，这样的算法几乎无法使用。

在Go语言中，大多数内建类型的查找操作（如通过键值查找map中的元素或访问数组元素）都具有常数时间复杂度，表示为O(1)。这意味着内建类型通常比自定义类型更快，除非你希望对底层行为进行完全控制，否则应优先选择使用内建类型。

不仅如此，不同的数据结构效率各不相同。通常，数组操作比map操作要快，但map的多功能性使它具有独特的优势。因此，开发者在选择数据结构时需权衡这些特性。

### Go中的二叉树

#### 二叉树简介

二叉树是一种数据结构，每个节点最多有两个子节点，即一个节点可以与最多两个其他节点相连。二叉树的根节点是树的第一个节点。树的深度（也称为高度）是从根节点到某个节点的最长路径，而某个节点的深度是该节点到根节点的边数。没有子节点的节点称为叶子节点。

当一棵树的最长路径与最短路径之间的差值不超过1时，称其为平衡树。如果不满足这一条件，则为不平衡树。树的平衡操作通常较为复杂且耗时，因此最好在树创建时保持其平衡，特别是在节点数量较多的情况下。

#### 二叉树的实现

在Go中，二叉树的实现可以通过结构体定义节点。下面是实现一个简单二叉树的代码，并带有中文注释。

```
package main

import (
    "fmt"
    "math/rand"
    "time"
)

// 定义二叉树节点结构
type Tree struct {
    Left  *Tree // 左子节点
    Value int   // 节点的值
    Right *Tree // 右子节点
}

// 遍历二叉树
func traverse(t *Tree) {
    if t == nil {
        return
    }
    traverse(t.Left) // 递归遍历左子树
    fmt.Print(t.Value, " ") // 打印当前节点的值
    traverse(t.Right) // 递归遍历右子树
}

// 创建二叉树并填充随机值
func create(n int) *Tree {
    var t *Tree
    rand.Seed(time.Now().Unix()) // 初始化随机数种子
    for i := 0; i < 2*n; i++ {
        temp := rand.Intn(n * 2)
        t = insert(t, temp) // 插入随机值
    }
    return t
}

// 插入节点到二叉树中
func insert(t *Tree, v int) *Tree {
    if t == nil {
        return &Tree{nil, v, nil} // 创建根节点
    }
    if v == t.Value {
        return t // 如果值已存在，不做操作
    }
    if v < t.Value {
        t.Left = insert(t.Left, v) // 递归插入到左子树
        return t
    }
    t.Right = insert(t.Right, v) // 递归插入到右子树
    return t
}

func main() {
    tree := create(10)
    fmt.Println("树的根节点值为:", tree.Value)
    traverse(tree)
    fmt.Println()

    // 插入新值并再次遍历
    tree = insert(tree, -10)
    tree = insert(tree, -2)
    traverse(tree)
    fmt.Println()
    fmt.Println("树的根节点值为:", tree.Value)
}
```

运行结果：

```
树的根节点值为: 18
0 3 4 5 7 8 9 10 11 14 16 17 18 19
-10 -2 0 3 4 5 7 8 9 10 11 14 16 17 18 19
树的根节点值为: 18
```

#### 二叉树的优势

二叉树特别适合用于表示层次结构的数据，因此在编译器解析程序代码时，广泛采用二叉树。此外，二叉树是天然有序的，只需插入元素到正确位置，树结构就会保持有序。然而，删除树中的元素相对复杂，因为需要维护树的结构。

当二叉树是平衡的，其查找、插入和删除操作的时间复杂度大约为O(log n)，其中n是树中元素的数量。例如，一个包含100万个元素的平衡树，其高度大约为20，这意味着可以在不到20步内访问到树中的任意节点。

二叉树的主要缺点在于其结构取决于插入元素的顺序。如果树的键值较长且复杂，插入和查找操作可能会变慢。此外，如果树不平衡，树的性能将变得不可预测。

### 哈希表在Go中的应用

#### 哈希表的概念

哈希表是一种存储键值对的数据结构，它通过哈希函数计算出一个索引，从而定位数据。一个好的哈希函数需要能够产生均匀分布的哈希值，以避免哈希冲突。

#### Go中的哈希表实现

下面展示了如何在Go中实现一个简单的哈希表：

```
package main

import (
    "fmt"
)

// 定义哈希表的大小
const SIZE = 15

// 定义哈希表的节点结构
type Node struct {
    Value int
    Next  *Node
}

// 定义哈希表结构
type HashTable struct {
    Table map[int]*Node
    Size  int
}

// 哈希函数
func hashFunction(i, size int) int {
    return i % size
}

// 插入数据到哈希表
func insert(hash *HashTable, value int) int {
    index := hashFunction(value, hash.Size)
    element := Node{Value: value, Next: hash.Table[index]}
    hash.Table[index] = &element
    return index
}

// 遍历哈希表
func traverse(hash *HashTable) {
    for k := range hash.Table {
        if hash.Table[k] != nil {
            t := hash.Table[k]
            for t != nil {
                fmt.Printf("%d -> ", t.Value)
                t = t.Next
            }
            fmt.Println()
        }
    }
}

func main() {
    // 创建哈希表
    table := make(map[int]*Node, SIZE)
    hash := &HashTable{Table: table, Size: SIZE}
    fmt.Println("哈希表的大小为:", hash.Size)

    // 向哈希表插入数据
    for i := 0; i < 120; i++ {
        insert(hash, i)
    }

    // 遍历并打印哈希表
    traverse(hash)
}
```

运行结果：

```
哈希表的大小为: 15
105 -> 90 -> 75 -> 60 -> 45 -> 30 -> 15 -> 0 ->
110 -> 95 -> 80 -> 65 -> 50 -> 35 -> 20 -> 5 ->
...
```

#### 哈希表的优势

哈希表的最大优势在于查找速度快。当哈希表有n个键和k个桶时，查找时间复杂度从O(n)降低到O(n/k)，即使哈希表中有大量元素，查找效率也能保持在较低的时间复杂度内。

#### 补充知识点

1. **二叉树的平衡与自平衡树**：虽然普通二叉树的性能取决于插入顺序，但一些自平衡树（如AVL树和红黑树）通过自动调整树的结构，确保即使在最差情况下也能维持较优的性能。
2. **哈希碰撞处理**：在哈希表中，多个键可能会映射到同一个索引，这被称为哈希碰撞。常用的碰撞处理方法有链地址法和开放地址法。在链地址法中，每个桶包含一个链表，用于存储冲突的键值对。

通过本文的讲解，相信大家对数据结构如二叉树和哈希表在Go中的应用有了更深入的理解。掌握这些基础结构，不仅能提升代码效率，还能为复杂项目的实现打下坚实的基础。

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

  21

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  12

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

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而O...