---
title: 华为仓颉语言入门（7）：深入理解 do-while 循环及其应用
url: https://blog.csdn.net/nokiaguy/article/details/142619199
source: 一个被知识诅咒的人
date: 2024-09-29
fetch_date: 2025-10-06T18:22:14.170337
---

# 华为仓颉语言入门（7）：深入理解 do-while 循环及其应用

# 华为仓颉语言入门（7）：深入理解 do-while 循环及其应用

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-09-28 18:03:47 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量1.2k
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

6

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
9

CC 4.0 BY-SA版权

分类专栏：
[华为仓颉语言入门](https://blog.csdn.net/nokiaguy/category_12790032.html)
文章标签：
[华为](https://so.csdn.net/so/search/s.do?q=%E5%8D%8E%E4%B8%BA&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[数据库](https://so.csdn.net/so/search/s.do?q=%E6%95%B0%E6%8D%AE%E5%BA%93&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[仓颉](https://so.csdn.net/so/search/s.do?q=%E4%BB%93%E9%A2%89&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142619199>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

华为仓颉语言入门
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12790032.html "华为仓颉语言入门")

10 篇文章

订阅专栏

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

##### 用法说明

`do-while` 表达式是一种控制循环的结构，它允许代码在每次循环之后进行条件判断。在这个表达式中，无论条件一开始是否满足，代码块都会被至少执行一次。

##### 语法结构

```
do {
    // 循环体
} while (条件)
```

条件的判断发生在每次循环执行后。如果条件为 `true`，则循环继续；如果条件为 `false`，循环终止。因此，`do-while` 能确保代码块至少被执行一次。

##### 示例：输出1到10的数字

通过 `do-while` 表达式，可以实现从1到10的数字输出，代码如下：

```
main() {
    var number = 0
    do {
        number++
        print("$(number)\t")
    } while (number < 10)
}
```

**解释：**

* 初始化 `number` 为 0，之后每次循环 `number` 自增1并输出。
* 当 `number` 小于10时，继续循环，直到达到10停止。

**输出结果：**

```
1    2    3    4    5    6    7    8    9    10
```

---

#### 用 do-while 计算阶乘

除了输出数字，`do-while` 还可以用来计算阶乘。下面是使用 `do-while` 计算 1 到 10 的阶乘的示例：

```
main() {
    var number = 0
    var factorial = 1
    do {
        number++
        factorial *= number
        println("$(number)! = $(factorial)")
    } while (number < 10)
}
```

**解释：**

* `factorial` 被初始化为1。
* 每次循环中，`number` 递增，并将 `factorial` 乘以 `number`，输出当前阶乘。

**输出结果：**

```
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800
```

---

#### 使用 break 提前终止循环

在某些情况下，我们可能需要根据特定条件提前结束循环。此时可以使用 `break` 表达式，它允许立即跳出循环。

例如，下面的代码寻找一个10到100之间满足以下条件的最小数字：被3除余2且被5除余3。

```
main() {
    var counter = 10
    do {
        if ((counter % 3 == 2) && (counter % 5 == 3)) {
            break
        } else {
            counter++
        }
    } while (true)
    println("找到的数字：$(counter)")
}
```

**解释：**

* 从 `counter` = 10 开始，循环检查是否符合条件。
* 满足条件时，使用 `break` 跳出循环，输出结果。

**输出结果：**

```
找到的数字：23
```

---

#### 使用 continue 跳过本次循环

在循环中，`continue` 表达式可以用来跳过当前的某次迭代，直接进入下一次循环。

例如，下面的代码只输出1到20之间的偶数。

```
main() {
    var number = 0
    do {
        number++
        if (number % 2 != 0) {
            continue // 跳过奇数
        }
        print("$(number)\t")
    } while (number < 20)
}
```

**解释：**

* 每次循环时，`number` 递增，检查是否为偶数。
* 如果 `number` 是奇数，跳过当前迭代，直接进入下一个循环。

**输出结果：**

```
2    4    6    8    10    12    14    16    18    20
```

---

#### 处理剩余的练习

**练习 1**：使用 `do-while` 输出1到50之间所有的9的倍数，包含9。

```
main() {
    var number = 9
    do {
        if (number % 9 == 0) {
            print("$(number)\t")
        }
        number++
    } while (number <= 50)
}
```

**输出结果：**

```
9    18    27    36    45
```

此代码会检查 `number` 是否是9的倍数，并在满足条件时输出对应的数字。

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

  9

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

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[2025机器人产业大洗牌：新兴初创企业的技术革命与崛起之路](https://unitymarvel.blog.csdn.net/article/details/151067555)

09-01
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
1049

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键技术。通过ROS控制、A\*路径规划和PyTorch视觉识别等代码示例（附中文注释），展示初创企业的技术优势。文章预测Figure AI、Unitree等公司将引领消费级机器人市场，推动社会进入智能协作新时代。（150字）](https://unitymarvel.blog.csdn.net/article/details/151067555)

![](https://csdnimg.cn/release/blogv2/d...