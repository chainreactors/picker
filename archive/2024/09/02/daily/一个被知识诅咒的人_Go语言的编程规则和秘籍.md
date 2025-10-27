---
title: Go语言的编程规则和秘籍
url: https://blog.csdn.net/nokiaguy/article/details/141788814
source: 一个被知识诅咒的人
date: 2024-09-02
fetch_date: 2025-10-06T18:22:51.336084
---

# Go语言的编程规则和秘籍

# Go语言的编程规则和秘籍

原创
已于 2024-09-01 20:10:17 修改
·
1k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

9

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

4
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#后端](https://so.csdn.net/so/search/s.do?q=%E5%90%8E%E7%AB%AF&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#go](https://so.csdn.net/so/search/s.do?q=go&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-09-01 19:51:00 首次发布

[![](https://i-blog.csdnimg.cn/direct/6d4320254d4d47de985b6dbab91d4b6f.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

《Go语言编程全解--理论与实践》
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12773266.html "《Go语言编程全解--理论与实践》")

25 篇文章

订阅专栏

Go语言有一些严格的编码规则，这些规则旨在帮助你避免常见的错误和漏洞，同时也使你的代码更易于被Go社区理解。本文将介绍其中两条重要的规则。

首先需要记住，Go编译器的目的是帮助你提升代码质量，而不是让你的开发过程变得复杂。因此，Go编译器的主要任务就是编译代码并提高其质量。

##### 1. 包的使用规则

Go对包的使用有非常严格的规定。你不能随意引入可能需要的包而在代码中不使用它们。即使在使用`go run`命令时，Go编译器仍然会创建一个可执行文件。这个文件在程序执行后会自动删除，因此你可能不会注意到它的存在。

来看下面这个简单的程序，保存在`unusedPackageExample.go`文件中：

```
package main

import (
    "fmt"
    "os"
)

func main() {
    fmt.Println("你好，世界！")
}
```

如果你运行`unusedPackageExample.go`，你会收到以下错误信息，程序将无法执行：

```
$ go run unusedPackageExample.go
# 命令行参数
./unusedPackageExample.go:5:2: 导入但未使用: "os"
```

这表明`os`包在程序中被导入了，但并未实际使用。要解决这个问题，你可以将`os`包从`import`列表中删除，修改后的代码如下：

```
package main

import (
    "fmt"
)

func main() {
    fmt.Println("你好，世界！")
}
```

删除`os`包后，这段代码就能正常编译并运行了。你可以试试看。

虽然此时讨论如何绕过Go的规则似乎有些不合时宜，但还是有一种方法可以避免这个限制。在`import`语句中使用下划线前缀可以引入包而不使用它，并且不会产生编译错误。如下所示：

```
package main

import (
    "fmt"
    _ "os"
)

func main() {
    fmt.Println("你好，世界！")
}
```

运行这段代码时，输出如下：

```
$ go run unusedPackageExample.go
你好，世界！
```

通过在`os`包前面加上`_`，我们告诉编译器虽然包被导入了，但我们不会使用它，从而避免了错误。

##### 2. 大括号的格式要求

Go语言对大括号的使用也有严格要求。看下面这个名为`curlyBraceExample.go`的Go程序：

```
package main

import (
    "fmt"
)

func main()
{
    fmt.Println("Go 对大括号的使用有严格的要求！")
}
```

虽然代码看起来没有问题，但如果你尝试执行它，你会发现编译器会给出如下的语法错误信息，代码无法编译和运行：

```
$ go run curlyBraceExample.go
# 命令行参数
./curlyBraceExample.go:7:6: 缺少 "main" 函数的函数体
./curlyBraceExample.go:8:1: 语法错误: 在 { 前的分号或换行符
```

错误信息的原因在于Go需要在许多上下文中使用分号作为语句的终止符，编译器会自动在需要时插入分号。因此，如果你将左大括号`{`放在新的一行，Go编译器会在前一行（即`func main()`之后）自动插入一个分号，这就是引发错误的原因。

为避免此问题，Go要求大括号 `{` 必须和函数声明在同一行。修改后的代码如下：

```
package main

import (
    "fmt"
)

func main() {
    fmt.Println("Go 对大括号的使用有严格的要求！")
}
```

现在，这段代码将正常编译和运行，输出如下：

```
$ go run curlyBraceExample.go
Go 对大括号的使用有严格的要求！
```

##### 下载Go包

尽管Go的标准库非常丰富，但有时你仍然需要下载外部包来扩展功能。以下是如何下载并使用外部包的简单步骤。

看下面这个保存在`externalPackageExample.go`文件中的简单程序：

```
package main

import (
    "fmt"
    "github.com/customuser/customrepo/customPackage"
)

func main() {
    fmt.Println(customPackage.AddTwo(5, 6))
}
```

这个程序引入了一个外部包`customPackage`，它位于`github.com/customuser/customrepo/customPackage`。如果你直接运行`externalPackageExample.go`，你会看到如下错误信息：

```
$ go run externalPackageExample.go
externalPackageExample.go:5:2: 找不到包 "github.com/customuser/customrepo/customPackage"
```

这表示本地系统上缺少这个外部包。要解决这个问题，你需要执行以下命令来下载该包：

```
$ go get -v github.com/customuser/customrepo/customPackage
```

下载完成后，你可以在本地目录中找到这些文件：

```
$ ls -l ~/go/src/github.com/customuser/customrepo/customPackage/
总用量 8
-rw-r--r--  1 mtsouk  staff  66 10月 17 21:47 customPackage.go
```

此外，`go get`命令还会自动编译该包，相关的编译文件存放在以下目录：

```
$ ls -l ~/go/pkg/darwin_amd64/github.com/customuser/customrepo/customPackage.a
-rw-r--r--  1 mtsouk  staff  1050 10月 17 21:47 /Users/mtsouk/go/pkg/darwin_amd64/github.com/customuser/customrepo/customPackage.a
```

此时，你可以成功运行`externalPackageExample.go`，输出如下：

```
$ go run externalPackageExample.go
11
```

如果你需要删除下载的中间文件，可以执行以下命令：

```
$ go clean -i -v -x github.com/customuser/customrepo/customPackage
cd /Users/mtsouk/go/src/github.com/customuser/customrepo/customPackage
rm -f customPackage.test customPackage.test.exe
rm -f /Users/mtsouk/go/pkg/darwin_amd64/github.com/customuser/customrepo/customPackage.a
```

同样地，如果要删除整个下载的Go包，可以使用`rm`命令删除其源文件：

```
$ rm -rf ~/go/src/github.com/customuser/customrepo/customPackage
```

在执行这些命令后，如果再次需要使用这个包，则需要重新下载。

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

  4

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

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。]...