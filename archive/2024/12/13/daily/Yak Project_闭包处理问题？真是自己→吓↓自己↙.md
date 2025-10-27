---
title: 闭包处理问题？真是自己→吓↓自己↙
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247526965&idx=1&sn=a12fb6ba574d474618abaa514c35db5d&chksm=c2d11691f5a69f87279670d9bf5afbb733243573c87d2bca37f465d21a8e00881b25e29e8aa7&scene=58&subscene=0#rd
source: Yak Project
date: 2024-12-13
fetch_date: 2025-10-06T19:39:34.482722
---

# 闭包处理问题？真是自己→吓↓自己↙

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZflE6yn5hzlJ9TC2u7r7VkrVZYXjkDjGBiags5Ohl4n2n21kh8SdvkGFomqs7Wlic0EOnEz8ia5icWqng/0?wx_fmt=jpeg)

# 闭包处理问题？真是自己→吓↓自己↙

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

之前的文章中曾经和大家讨论过**Yaklang对块作用域的处理**

（前文指路：[抱歉占用公共资源，大家别猜啦，我们在一起了@Yaker](https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247521558&idx=1&sn=0a721ae96b5a00febafcacc123cd5029&scene=21#wechat_redirect)）

而在Yaklang中，对于有特殊性质的**闭包**，也有着独特的方法进行处理⬇️

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZflE6yn5hzlJ9TC2u7r7Vkr5SKtb3jIezWwMkoJZJz1kshbfv1FKcR2JNSUgduiczOQQRFJePYV5icA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZflE6yn5hzlJ9TC2u7r7VkrboFmRngzDWicf1pHffPT5KwEU04k9p0CqF3T8h3sGIdP5ZzmcTKqvPg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZflE6yn5hzlJ9TC2u7r7VkrAYQ2b2KhSAaxiacOygyUYjMgCDjicAcFUrxticgdDicv94hmDmtro6Y7og/640?wx_fmt=png&from=appmsg)

先看如下的代码：

```
package main
func main(){    a := 1    f := func(){        b := a                // freevalue        println(b)        a = 2                // side-effect    }    f()     println(a) // 2}
```

上述代码展示了闭包中的变量可能会出现的两种情况：

* 查找一个外部作用域中的变量
* 修改一个外部作用域中的变量

我们将未在闭包作用域中定义的 “a” 被称为 **freevalue**，而通过 freevalue 对外部变量的影响则被称为 **side-effe****ct****。**

可以通过 yaklang 编译上述代码，输出结果如下：

```
package: main library@inittype: () ->entry-0:
extern type:maintype: () -> nullentry-0:        <any> t28 = undefined-println        <null> t26 = call <() -> null> AnonymousFunc-2 () binding[<number> 1] member[]        <number> t27 = side-effect <number> 2 [a] by <null> t26        <any> t29 = call <any> t28 (<number> t27) binding[] member[]
extern type:AnonymousFunc-2freeValue: a:(20)a, println:(21)printlnsideEffects: atype: () -> nullentry-0:        jump -> b-1b-1: <- entry-0        <any> t22 = call <any> println (<number> a) binding[] member[]        jump -> b-2b-2: <- b-1
extern type:
```

这里的 **AnonymousFunc-2** 就是源码中的闭包函数，可以发现 yaklang 生成了一个名为 **side-effect <number> 2 [a] by <null> t26** 的特殊右值，这个右值和普通的 **<number> 2** 没什么不同，只是为了说明该右值源自于闭包函数 **AnonymousFunc-2** 对外部作用域的影响

通过将 side-effect 描述为右值，就可以将闭包函数对外部的影响给简化为一条或者多条赋值语句，等效为如下代码：

```
package main
func main(){    a := 1    a = 2    println(a) // 2}
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZflE6yn5hzlJ9TC2u7r7Vkr2niasa7ibNsDRlZicyibfrGPpMv2WuqdUebocndYFZMOBQGMkgsW3CnXdg/640?wx_fmt=png&from=appmsg)

###

上述的处理已经可以应付大多数情况下的 side-effect 了，但 side-effect 还有两个特殊的特性：**绑定和继承**。

具体可以看如下代码：

```
package main
func main() {    a := 1    f1 := func() {        a = 2    }    f2 := func() {        f1() // f2继承f1的side-effect    }    f2()    println(a) // side-effect(a,2)}
```

```
package main
func main() {    a := 1 // f1将绑定a,绑定值由闭包定义的位置决定与调用位置无关    f1 := func() {        a = 2     }    {        a := 3        f1()        println(a) // 3    }    println(a) // side-effect(a,2)}
```

在 yaklang 的处理中，side-effect 将被记录在 **FunctionType** 中，成为闭包的一个属性。通过继承闭包的 FunctionType 即可实现 side-effect 的继承。

相对较难处理的是 side-effect 的绑定机制，这里采用了延迟使用 side-effect 的方式：生成好的 side-effect 暂时不会放入作用域中，当前作用域为 **a := 1** 的子作用域时才会将 side-effect 放入。

我们可以分别编译上述两个案例，编译后的 ssa 如下：

```
package: main library@inittype: () ->entry-0:
extern type:maintype: () -> nullentry-0:        <null> t36 = call <() -> null> AnonymousFunc-3 () binding[<number> 1, <() -> null> AnonymousFunc-2] member[]        <any> t37 = side-effect <number> 2 [a] by <null> t36        <number, error> t39 = call <func(...interface {}) (int, error)> println (<any> t37) binding[] member[]
extern type:AnonymousFunc-2freeValue: a:(21)asideEffects: atype: () -> nullentry-0:        jump -> b-1b-1: <- entry-0        jump -> b-2b-2: <- b-1
extern type:AnonymousFunc-3freeValue: f1:(29)f1, a:(32)asideEffects: a // 继承自AnonymousFunc-2type: () -> nullentry-0:        jump -> b-1b-1: <- entry-0        <null> t30 = call <() -> null> f1 () binding[<number> a] member[]        <any> t33 = side-effect <number> 2 [a] by <null> t30        jump -> b-2b-2: <- b-1
extern type:error:
```

* AnonymousFunc-3 中不存在变量a，其中的 sideEffects a 继承自 AnonymousFunc-2

```
package: main library@inittype: () ->entry-0:
extern type:mainsideEffects: atype: () -> nullentry-0:        jump -> b-1b-1: <- entry-0        <null> t27 = call <() -> null> AnonymousFunc-2 () binding[<number> 3] member[]        <any> t28 = side-effect <number> 2 [a] by <null> t27 // 生成side-effect但暂时不会使用        <number, error> t30 = call <func(...interface {}) (int, error)> println (<number> 3) binding[] member[]        jump -> b-2b-2: <- b-1        <number, error> t33 = call <func(...interface {}) (int, error)> println (<any> t28) binding[] member[]
extern type:AnonymousFunc-2freeValue: a:(21)asideEffects: atype: () -> nullentry-0:        jump -> b-1b-1: <- entry-0        jump -> b-2b-2: <- b-1
extern type:error:
```

* 由于 side-effect 不在当前作用域中，因此第一个 println 查找到常量'3'，第二个 println 属于 entry-0 的子作用域，可以查找到 side-effect

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZflE6yn5hzlJ9TC2u7r7Vkroam6s1lyl1yZIlZEYRfpFJxmJEdoEvqr2fFWpdeicS8GIKkTaLNvrcw/640?wx_fmt=png&from=appmsg)

###

当前版本的 yaklang 已经能处理大多数情况下的 side-effect 了，但某些 side-effect 与 phi 值结合出现的问题还需要解决：

```
package main
func main(){    a := 0    f := func() {        if true {            a = 2        }else{
        }        println(a) // phi(freevalue,2)    }    a = 1    f()    println(a) // phi(1,2)    a = 2    f()    println(a) // phi(2,2)}
```

在这个样例中的 f 可能生成 side-effect 也可能不生成，因此应该生成一个 **phi(freevalue,2)**。而 freevalue 只是一个占位符，它将在该闭包被调用时替换为绑定变量在当前作用域中的值。

目前该功能正在实现中，敬请期待后续版本。

**END**

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yaklang.com/*
Yakit安装文档：
*https://yaklang.com/products/download\_and\_install*
Yakit使用文档：
*https://yaklang.com/products/intro/*
常见问题速查：
*https://yaklang.com/products/FAQ*

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcGEibOlRNlz6ZPic3cWicMDwdqZLq9q0hibDYiaICia6nncspoDTRnjPXFGTr3VWd9FlV4YSXRStoabxbg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZeX0EdicJxBOjGjQuecg0TvCvRgqibPwyOUp8untXs9Cl5XKux2yQQf27ibgZ0ic0Fm2yicdbYg6c4xUJg/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

Yak Project

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过