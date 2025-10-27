---
title: 在Go语言中调用C代码的技巧
url: https://blog.csdn.net/nokiaguy/article/details/141889277
source: 一个被知识诅咒的人
date: 2024-09-05
fetch_date: 2025-10-06T18:23:56.939451
---

# 在Go语言中调用C代码的技巧

# 在Go语言中调用C代码的技巧

![](https://i-operation.csdnimg.cn/images/cf31225e169b4512917b2e77694eb0a2.png)Go 语言中调用 C 代码的技巧

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2024-09-04 11:42:06 发布

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量884
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

5

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
5

CC 4.0 BY-SA版权

分类专栏：
[《Go语言编程全解--理论与实践》](https://blog.csdn.net/nokiaguy/category_12773266.html)
文章标签：
[golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[c语言](https://so.csdn.net/so/search/s.do?q=c%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/141889277>

[![](https://i-blog.csdnimg.cn/direct/6d4320254d4d47de985b6dbab91d4b6f.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

《Go语言编程全解--理论与实践》
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12773266.html "《Go语言编程全解--理论与实践》")

25 篇文章

订阅专栏

#### 在 Go 语言中调用 C 代码的技巧

虽然 Go 语言旨在提升编程体验，减少 C 语言的复杂性，但 C 语言依然是非常强大的编程语言，并且在很多情况下依然十分有用。比如在使用数据库或设备驱动程序时，它们可能是用 C 语言编写的。这意味着在某些情况下，你可能需要在 Go 项目中调用 C 代码。

##### 在同一个文件中调用 C 代码

最简单的调用 C 代码的方式是将 C 代码直接包含在 Go 源文件中。虽然这需要一些特殊处理，但这种方式速度很快，也不算太复杂。不过，如果你在同一个项目中多次使用这种功能，可能需要重新考虑这种方式是否合适，或者是否应该换一种编程语言。

下面展示了一个包含 C 代码和 Go 代码的文件 `cGo.go`，它分为三部分：

```
package main

// #include <stdio.h>
// void callC() {
//     printf("调用 C 代码！\n");
// }
import "C"

import "fmt"

func main() {
    fmt.Println("这是 Go 语言中的一条语句！")
    C.callC()
    fmt.Println("这是另一条 Go 语言中的语句！")
}
```

在上面的代码中，`callC()` C 函数通过 `C.callC()` 调用。运行该代码会产生以下输出：

```
$ go run cGo.go
这是 Go 语言中的一条语句！
调用 C 代码！
这是另一条 Go 语言中的语句！
```

##### 使用单独文件调用 C 代码

接下来讨论如何在 C 代码位于单独的文件时，从 Go 程序中调用它。假设我们有两个已经编写好的 C 函数，不想在 Go 中重写它们。

###### C 代码

首先，C 代码包含在两个文件中：`callC.h` 和 `callC.c`。

`callC.h` 文件内容如下：

```
#ifndef CALLC_H
#define CALLC_H
void cHello();
void printMessage(char* message);
#endif
```

`callC.c` 文件内容如下：

```
#include <stdio.h>
#include "callC.h"

void cHello() {
    printf("来自 C 语言的问候！\n");
}

void printMessage(char* message) {
    printf("Go 语言发送的消息是: %s\n", message);
}
```

这两个文件存储在 `callClib` 目录下。当然，你也可以使用任何其他目录名称。

###### Go 代码

接下来是 Go 源代码，它被命名为 `callC.go`，分为三部分展示：

```
package main

// #cgo CFLAGS: -I${SRCDIR}/callClib
// #cgo LDFLAGS: ${SRCDIR}/callC.a
// #include <stdlib.h>
// #include <callC.h>
import "C"

import (
    "fmt"
    "unsafe"
)

func main() {
    fmt.Println("即将调用 C 函数！")
    C.cHello()

    fmt.Println("即将调用另一个 C 函数！")
    myMessage := C.CString("这是来自 Mihalis 的消息！")
    defer C.free(unsafe.Pointer(myMessage))
    C.printMessage(myMessage)

    fmt.Println("调用完成！")
}
```

在 Go 中传递字符串给 C 函数时，需要使用 `C.CString()` 创建一个 C 字符串，同时要使用 `defer` 语句来确保不再需要时释放内存。

##### 编译和执行混合的 Go 和 C 代码

当你编写好 C 代码和 Go 代码后，接下来就是编译并执行这些文件。幸运的是，所有关键信息都已经包含在 Go 文件中，唯一的重点是编译 C 代码以创建一个静态库。你可以执行以下命令来完成这些操作：

```
$ ls -l callClib/
total 16
-rw-r--r--@ 1 mtsouk  staff  162 Jan 10 09:17 callC.c
-rw-r--r--@ 1 mtsouk  staff   89 Jan 10 09:17 callC.h

$ gcc -c callClib/*.c

$ ls -l callC.o
-rw-r--r--  1 mtsouk  staff  952 Jan 22 22:03 callC.o

$ /usr/bin/ar rs callC.a *.o
ar: creating archive callC.a

$ ls -l callC.a
-rw-r--r--  1 mtsouk  staff  4024 Jan 22 22:03 callC.a
```

完成这些步骤后，`callC.a` 文件将位于与 `callC.go` 文件相同的目录中。此时你可以编译 Go 代码：

```
$ go build callC.go

$ ls -l callC
-rwxr-xr-x  1 mtsouk  staff  2403184 Jan 22 22:10 callC
```

执行生成的可执行文件：

```
$ ./callC
即将调用 C 函数！
来自 C 语言的问候！
即将调用另一个 C 函数！
Go 语言发送的消息是: 这是来自 Mihalis 的消息！
调用完成！
```

##### 总结

如果你只需要调用少量的 C 代码，那么在同一个 Go 文件中同时包含 C 和 Go 代码是一个简洁的选择。然而，当涉及到更复杂的项目时，创建一个静态的 C 库可能是更好的选择。

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

  5

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

[摘要：2025年机器人产业正经历技术驱动的深度变革，AI初创企业通过创新算法和低成本方案挑战传统巨头。本文剖析产业洗牌动因，包括AI融合、融资热潮和应用场景扩展，重点解析人形机器人等关键...