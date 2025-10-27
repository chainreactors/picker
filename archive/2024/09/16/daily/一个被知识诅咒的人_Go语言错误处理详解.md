---
title: Go语言错误处理详解
url: https://blog.csdn.net/nokiaguy/article/details/142283260
source: 一个被知识诅咒的人
date: 2024-09-16
fetch_date: 2025-10-06T18:22:03.653366
---

# Go语言错误处理详解

# Go语言错误处理详解

原创
于 2024-09-15 13:36:03 发布
·
1k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

4

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

7
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#golang](https://so.csdn.net/so/search/s.do?q=golang&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#xcode](https://so.csdn.net/so/search/s.do?q=xcode&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#ios](https://so.csdn.net/so/search/s.do?q=ios&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#go1.19](https://so.csdn.net/so/search/s.do?q=go1.19&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#go](https://so.csdn.net/so/search/s.do?q=go&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[![](https://i-blog.csdnimg.cn/direct/6d4320254d4d47de985b6dbab91d4b6f.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

《Go语言编程全解--理论与实践》
专栏收录该内容](https://blog.csdn.net/nokiaguy/category_12773266.html "《Go语言编程全解--理论与实践》")

25 篇文章

订阅专栏

Go语言以其简洁、高效和并发能力著称。在实际开发中，错误处理是一个不可避免且至关重要的部分。本文将深入探讨Go语言中的错误处理机制，涵盖其原理、使用方法、最佳实践，并提供丰富的代码示例和中文注释。

### 一、错误处理的基本概念

在Go语言中，错误通过内置的`error`接口来表示。`error`接口定义如下：

```
type error interface {
    Error() string
}
```

任何实现了`Error()`方法的类型都被视为`error`类型。这为我们提供了灵活性，可以创建自定义错误类型。

### 二、内置错误类型和简单错误处理

Go语言提供了`errors`包，允许我们创建简单的错误对象。

#### 1. 创建基本错误

```
import "errors"

err := errors.New("这是一个错误信息")
```

#### 2. 简单的错误处理

Go语言鼓励在函数返回值中包含错误信息，常见的模式是：

```
func DoSomething() error {
    // 执行操作
    if 有错误发生 {
        return errors.New("发生了错误")
    }
    return nil
}

func main() {
    if err := DoSomething(); err != nil {
        fmt.Println("错误：", err)
    }
}
```

### 三、自定义错误类型

为了提供更丰富的错误信息，我们可以创建自定义的错误类型。

#### 1. 基础自定义错误

```
type MyError struct {
    Code    int
    Message string
}

func (e *MyError) Error() string {
    return fmt.Sprintf("错误代码：%d，错误信息：%s", e.Code, e.Message)
}

func DoSomething() error {
    // 执行操作
    if 有错误发生 {
        return &MyError{Code: 404, Message: "资源未找到"}
    }
    return nil
}
```

#### 2. 使用自定义错误

```
func main() {
    err := DoSomething()
    if err != nil {
        if myErr, ok := err.(*MyError); ok {
            fmt.Printf("捕获到自定义错误：代码=%d，信息=%s\n", myErr.Code, myErr.Message)
        } else {
            fmt.Println("错误：", err)
        }
    }
}
```

### 四、错误包装（Error Wrapping）

Go 1.13引入了错误包装机制，提供了更多处理错误的方式。

#### 1. 使用`fmt.Errorf`包装错误

```
import "fmt"

func DoSomething() error {
    err := SomeFunction()
    if err != nil {
        return fmt.Errorf("DoSomething失败：%w", err)
    }
    return nil
}
```

#### 2. 解包错误

```
import "errors"

func main() {
    err := DoSomething()
    if err != nil {
        if errors.Is(err, 特定的错误) {
            fmt.Println("发生了特定的错误")
        }
    }
}
```

### 五、`errors`包的高级用法

#### 1. `errors.Is`

用于判断错误链中是否包含特定的错误。

```
if errors.Is(err, io.EOF) {
    fmt.Println("读取到了文件末尾")
}
```

#### 2. `errors.As`

用于将错误链中的错误转换为特定类型。

```
var pathError *os.PathError
if errors.As(err, &pathError) {
    fmt.Println("路径错误：", pathError.Path)
}
```

### 六、`panic`和`recover`

#### 1. `panic`的使用

`panic`用于在程序遇到无法恢复的错误时中止执行。

```
func Divide(a, b int) int {
    if b == 0 {
        panic("除数不能为零")
    }
    return a / b
}
```

#### 2. `recover`的使用

`recover`用于捕获`panic`，使程序从异常状态恢复。

```
func ProtectDivide(a, b int) {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("捕获到panic：", r)
        }
    }()
    fmt.Println(Divide(a, b))
}
```

#### 3. `defer`、`panic`和`recover`的关系

`defer`延迟函数在`panic`发生时仍会被执行，这使得`recover`只能在`defer`函数中有效。

### 七、错误处理的最佳实践

1. **优先使用错误返回值**：Go语言提倡使用错误作为函数的返回值，而非异常机制。
2. **避免滥用`panic`**：`panic`只应用于不可恢复的错误，如程序的内部逻辑错误。
3. **提供有用的错误信息**：错误信息应尽可能清晰，包含足够的上下文。
4. **使用错误包装**：利用错误包装机制，保留原始错误信息，构建错误链。
5. **检查错误类型**：使用`errors.Is`和`errors.As`来判断和提取特定的错误信息。

### 八、完整示例

```
package main

import (
    "errors"
    "fmt"
    "io"
    "os"
)

// 自定义错误类型
type FileError struct {
    Op   string
    Path string
    Err  error
}

func (e *FileError) Error() string {
    return fmt.Sprintf("文件操作错误：%s %s：%v", e.Op, e.Path, e.Err)
}

func (e *FileError) Unwrap() error {
    return e.Err
}

// 模拟文件读取函数
func ReadFile(path string) error {
    file, err := os.Open(path)
    if err != nil {
        return &FileError{
            Op:   "打开",
            Path: path,
            Err:  err,
        }
    }
    defer file.Close()

    buf := make([]byte, 1024)
    _, err = file.Read(buf)
    if err != nil {
        if err == io.EOF {
            return nil // 正常结束
        }
        return &FileError{
            Op:   "读取",
            Path: path,
            Err:  err,
        }
    }
    return nil
}

func main() {
    err := ReadFile("不存在的文件.txt")
    if err != nil {
        // 使用errors.As提取错误类型
        var fileErr *FileError
        if errors.As(err, &fileErr) {
            fmt.Printf("操作：%s，路径：%s，错误：%v\n", fileErr.Op, fileErr.Path, fileErr.Err)
        } else {
            fmt.Println("未知错误：", err)
        }
    } else {
        fmt.Println("文件读取成功")
    }
}
```

**输出：**

```
操作：打开，路径：不存在的文件.txt，错误：open 不存在的文件.txt: The system cannot find the file specified.
```

### 九、总结

Go语言的错误处理机制简单而强大，通过`error`接口、自定义错误类型以及错误包装等手段，我们可以构建健壮的错误处理流程。遵循最佳实践，提供清晰的错误信息，有助于提高程序的可维护性和可靠性。

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

  4

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  7

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
[【Pyt...