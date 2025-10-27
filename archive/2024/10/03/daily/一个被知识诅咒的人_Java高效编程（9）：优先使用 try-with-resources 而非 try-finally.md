---
title: Java高效编程（9）：优先使用 try-with-resources 而非 try-finally
url: https://blog.csdn.net/nokiaguy/article/details/142620673
source: 一个被知识诅咒的人
date: 2024-10-03
fetch_date: 2025-10-06T18:51:41.071421
---

# Java高效编程（9）：优先使用 try-with-resources 而非 try-finally

# Java高效编程（9）：优先使用 try-with-resources 而非 try-finally

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[蒙娜丽宁](https://unitymarvel.blog.csdn.net "蒙娜丽宁")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png)
已于 2024-10-03 08:38:03 修改

![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
阅读量846
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

12

![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)
点赞数
18

CC 4.0 BY-SA版权

分类专栏：
[Java高效编程](https://blog.csdn.net/nokiaguy/category_12795365.html)
文章标签：
[java](https://so.csdn.net/so/search/s.do?q=java&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[开发语言](https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-10-02 10:00:00 首次发布

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/nokiaguy/article/details/142620673>

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Java高效编程
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12795365.html "Java高效编程")

19 篇文章

订阅专栏

[解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588?spm=1001.2014.3001.5502)

在Java编程中，许多资源（如 `InputStream`、`OutputStream` 和 `java.sql.Connection`）必须在使用后手动关闭。然而，开发者常常忘记关闭这些资源，导致严重的性能问题。虽然终结器（详见【条目8】）曾经被用作安全网，但它们并不可靠。在 Java 7 之前，`try-finally` 语句是确保资源正确关闭的唯一方式，即使在异常或提前返回时，`try-finally` 也能保证资源关闭：

```
// 使用 try-finally 关闭资源 - 不再是最佳方式
static String firstLineOfFile(String path) throws IOException {
    BufferedReader br = new BufferedReader(new FileReader(path));
    try {
        return br.readLine();
    } finally {
        br.close();
    }
}
```

虽然这种方式看起来并不坏，但在处理多个资源时，它会变得非常繁琐：

```
// 使用 try-finally 处理多个资源时代码显得复杂
static void copy(String src, String dst) throws IOException {
    InputStream in = new FileInputStream(src);
    try {
        OutputStream out = new FileOutputStream(dst);
        try {
            byte[] buf = new byte[BUFFER_SIZE];
            int n;
            while ((n = in.read(buf)) >= 0) {
                out.write(buf, 0, n);
            }
        } finally {
            out.close();
        }
    } finally {
        in.close();
    }
}
```

即使是优秀的程序员，也经常在 `try-finally` 中犯错。事实上，Java 库中有三分之二的 `close` 方法调用在2007年是错误的。

#### 使用 try-finally 的问题

即使 `try-finally` 可以正确关闭资源，但它存在一个微妙的问题：`try` 块和 `finally` 块中的代码都可能抛出异常。例如，在 `firstLineOfFile` 方法中，`readLine` 方法可能由于设备故障抛出异常，而 `close` 方法也可能因此失败。在这种情况下，后续的异常会掩盖第一个异常，导致调试变得非常困难。虽然可以编写代码来抑制第二个异常，但几乎没有人会这么做，因为代码会变得冗长复杂。

#### Java 7 的解决方案：try-with-resources

Java 7 引入了 `try-with-resources` 语句，解决了 `try-finally` 的所有问题。要使用该语句，资源类必须实现 `AutoCloseable` 接口，该接口只有一个返回 `void` 的 `close` 方法。Java 库和第三方库中的许多类现在都实现了该接口。以下是使用 `try-with-resources` 重写的 `firstLineOfFile` 方法：

```
// 使用 try-with-resources - 最佳资源关闭方式
static String firstLineOfFile(String path) throws IOException {
    try (BufferedReader br = new BufferedReader(new FileReader(path))) {
        return br.readLine();
    }
}
```

`try-with-resources` 同时处理多个资源时，代码更加简洁：

```
// 使用 try-with-resources 处理多个资源 - 简洁明了
static void copy(String src, String dst) throws IOException {
    try (InputStream in = new FileInputStream(src);
         OutputStream out = new FileOutputStream(dst)) {
        byte[] buf = new byte[BUFFER_SIZE];
        int n;
        while ((n = in.read(buf)) >= 0) {
            out.write(buf, 0, n);
        }
    }
}
```

#### try-with-resources 的优势

与 `try-finally` 相比，`try-with-resources` 更加简洁且易于维护。它不仅减少了冗余的代码，还提供了更好的异常处理机制。如果在 `try` 块和 `close` 方法中同时抛出异常，`try-with-resources` 会抑制后续异常，并保留最重要的第一个异常。抑制的异常不会被简单忽略，而是记录在异常堆栈中，并带有“抑制异常”的说明。你可以通过 `Throwable.getSuppressed` 方法程序化地访问这些抑制的异常。

你也可以像在普通 `try-finally` 中一样，为 `try-with-resources` 添加 `catch` 子句来处理异常。如下所示是一个不抛出异常的 `firstLineOfFile` 版本，它在无法打开文件时返回默认值：

```
// 带有 catch 子句的 try-with-resources
static String firstLineOfFile(String path, String defaultVal) {
    try (BufferedReader br = new BufferedReader(new FileReader(path))) {
        return br.readLine();
    } catch (IOException e) {
        return defaultVal;
    }
}
```

通过这种方式，你可以优雅地处理异常，而无需增加代码的嵌套层次。

#### 总结

`try-with-resources` 是关闭资源的最佳方式。它不仅代码简洁、清晰，而且能够正确处理多个异常，确保抛出的异常是最有用的，抑制的异常也不会丢失。与 `try-finally` 相比，`try-with-resources` 的优势明显，强烈建议在需要关闭资源的场景下使用这一语句。

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
2251

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与计算机视觉的利器。本书通过循序渐进的方式，让读者从零基础到掌握高级图像处理技能，帮助你实现从初学者到高手的跃升。](https://unitymarvel.blog.csdn.net/article/details/143574491)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

09-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3140

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专家李宁编写，通过丰富的实战案例，帮助读者在工作和项目中高效应用Python，提升编程技能。无论是新手还是有经验的开发者，这本书都将带你深入探索Python的无限可能，开启一段充满创意与实用性的编程之旅。](https://unitymarvel.blog.csdn.net/article/details/141889588)
...