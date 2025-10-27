---
title: 华为仓颉语言入门（6）：if条件表达式
url: https://blog.csdn.net/nokiaguy/article/details/142584942
source: 一个被知识诅咒的人
date: 2024-09-28
fetch_date: 2025-10-06T18:25:28.957585
---

# 华为仓颉语言入门（6）：if条件表达式

# 华为仓颉语言入门（6）：if条件表达式

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2024-09-27 09:22:33 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.6k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

9

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
31

CC 4.0 BY-SA版权

分类专栏：
[华为仓颉语言入门](https://blog.csdn.net/nokiaguy/category_12790032.html)
文章标签：
[华为](https://so.csdn.net/so/search/s.do?q=%E5%8D%8E%E4%B8%BA&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[linux](https://so.csdn.net/so/search/s.do?q=linux&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[仓颉](https://so.csdn.net/so/search/s.do?q=%E4%BB%93%E9%A2%89&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-09-27 09:21:42 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142584942>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

华为仓颉语言入门
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12790032.html "华为仓颉语言入门")

10 篇文章

订阅专栏

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

仓颉语言中的 `if` 表达式用于根据条件的值来决定是否执行相关代码逻辑。`if` 表达式有三种形式：单分支的 `if` 表达式、双分支的 `if` 表达式和嵌套的 `if` 表达式。

##### 单分支的 if 表达式

单分支的 `if` 表达式只有一个分支，其语法如下：

```
if (条件) {
    代码块
}
```

其中的条件必须是一个布尔类型的表达式，由一对匹配的花括号包围代码块。执行时，首先测试条件的值，如果条件为 `true`，就执行括号内的代码块；否则，不执行任何代码。

例如：

```
// isScorePassed 表示分数是否合格，true 表示合格，false 表示不合格
if (isScorePassed) {
    println("合格")
}
println("执行完毕")
```

在上述代码中，`isScorePassed` 为 `true` 时，将输出：

```
合格
执行完毕
```

如果 `isScorePassed` 为 `false`，则只会输出：

```
执行完毕
```

这表明，单分支的 `if` 表达式是否会执行代码，完全取决于条件的取值。值得注意的是，`if` 表达式的类型为 `Unit`，其值为 `0`。

##### 双分支的 if 表达式

双分支的 `if` 表达式包含两个分支，语法如下：

```
if (条件) {
    代码块1
} else {
    代码块2
}
```

在执行时，如果条件为 `true`，执行代码块1；如果条件为 `false`，则执行代码块2。

例如：

```
if (isScorePassed) {
    println("合格")
} else {
    println("不合格")
}
println("执行完毕")
```

如果 `isScorePassed` 为 `true`，输出结果为：

```
合格
执行完毕
```

如果 `isScorePassed` 为 `false`，输出结果为：

```
不合格
执行完毕
```

这里，`else` 分支必须在 `if` 表达式之后的代码中运行。

##### 双分支 if 表达式的类型

当 `if` 表达式的值被使用时，双分支的 `if` 表达式的类型是 `if` 分支和 `else` 分支类型的最小公共父类。

例如：

```
main() {
    var creditScore: UInt16 = 800
    var interestRate: Float64 = if (creditScore >= 600) {
        0.06
    } else {
        0.08
    }
    println(interestRate)
}
```

在这个例子中，`interestRate` 的值是根据 `creditScore` 的值决定的。如果 `creditScore` 大于或等于 600，则利率为 0.06；否则，利率为 0.08。最终输出利率的结果。

##### 嵌套的 if 表达式

当希望匹配更多的条件时，可以使用嵌套的 `if` 表达式。嵌套 `if` 表达式可以包含多个分支。其语法结构如下：

```
if (条件1) {
    代码块1
} else if (条件2) {
    代码块2
} ...
else {
    代码块n
}
```

其中每个条件都必须是布尔类型的表达式。整个 `if` 表达式的执行流程如下：

* 测试条件1的值，如果为 `true`，执行代码块1，整个 `if` 表达式结束；
* 如果条件1为 `false`，测试条件2的值，以此类推，直到找到为 `true` 的条件；
* 如果所有条件都为 `false`，则执行 `else` 分支中的代码块。

例如：

```
if (creditScore < 600) {
    interestRate = 0.08
} else if (creditScore < 800) {
    interestRate = 0.06
} else {
    interestRate = 0.05
}
println(interestRate)
```

根据 `creditScore` 的值，选择执行不同的分支，最终输出相应的利率。

#### if 表达式中的类型推断

在某些情况下，`if` 表达式不仅用于条件分支选择，还可以返回值。此时，`if` 表达式的返回值类型由 `if` 和 `else` 分支的类型决定。

例如，以下代码会根据 `creditScore` 的值，推断出 `interestRate` 的类型：

```
main() {
    var creditScore: UInt16 = 800
    var interestRate: Float64 = if (creditScore >= 600) {
        0.06
    } else {
        0.08
    }
    println(interestRate)
}
```

在这个例子中，`interestRate` 的类型被推断为 `Float64`，因为 `if` 和 `else` 分支中的返回值都是浮点数。这种情况适用于条件表达式需要返回一个值的场景。

#### 嵌套 if 表达式中的执行顺序

嵌套的 `if` 表达式可以根据多个条件执行不同的逻辑。例如，以下代码展示了如何根据不同的 `creditScore` 值调整利率：

```
if (creditScore < 600) {
    interestRate = 0.08
} else if (creditScore < 800) {
    interestRate = 0.06
} else if (creditScore < 1000) {
    interestRate = 0.05
} else {
    interestRate = 0.04
}
```

在这个例子中，程序将依次测试 `creditScore` 是否满足每个条件，直到找到符合条件的分支。如果 `creditScore` 小于 600，利率设置为 0.08；如果小于 800，但大于等于 600，利率为 0.06，以此类推。最终的输出结果取决于条件的匹配情况。

#### 条件表达式的最佳实践

对于 `if` 表达式的使用，编写整洁的代码并避免重复是非常重要的。例如，如果条件非常复杂，可以通过添加额外的条件块减少不必要的代码重复，确保代码逻辑清晰。

例如：

```
if (creditScore <= 1000) {
    if (creditScore < 600) {
        interestRate = 0.08
    } else if (creditScore < 800) {
        interestRate = 0.06
    } else if (creditScore < 900) {
        interestRate = 0.05
    } else {
        interestRate = 0.04
    }
} else {
    println("数据错误！")
}
```

这种写法将不同的条件组合在一起，确保只有在 `creditScore` 小于等于 1000 时才会进入利率设置的逻辑，如果超出此范围，将输出错误信息。这是一种防止数据错误的良好实践。

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

  31

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  9

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
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Py...