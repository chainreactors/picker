---
title: Python 面向对象编程——多态（Polymorphism）
url: https://mp.weixin.qq.com/s/nyvtBMuQ2jhWqdBpNzz-Og
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:52:40.639810
---

# Python 面向对象编程——多态（Polymorphism）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6OibpDQ66VYSFf8Yiafk3ibSkF4NwzSLPehediatlEu2icQZSJ8dIkakKhwAY1x192QeYDZnEUyjyK6D2NkHjRvYC4g/0?wx_fmt=jpeg)

# Python 面向对象编程——多态（Polymorphism）

原创

Lino
Lino

网络技术联盟站

![]()

在小说阅读器中沉浸阅读

各位同学，大家好！我是你们的 Python 讲师 Lino。

![](https://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYSFf8Yiafk3ibSkF4NwzSLPehsojf1LEIVYNay982LhicmlbxdtmlGNjUzfG5EFaA2yia4GU3dMaRAwcg/640?wx_fmt=png&from=appmsg)

在很多教材里，多态往往被讲成一句话：

“同一个接口，不同的实现。”

这句话没错，但太抽象。

在 Python 中，多态**不是被强制出来的设计模式，而是语言机制自然支持的结果**。

## 多态到底解决什么问题？

先看一个“没有多态”的典型代码。

```
```
class Dog:
    def bark(self):
        print("wang")

class Cat:
    def meow(self):
        print("miao")
```
```

使用时你只能这样写：

```
```
def make_sound(obj):
    if isinstance(obj, Dog):
        obj.bark()
    elif isinstance(obj, Cat):
        obj.meow()
```
```

问题非常明显：

* 强耦合
* 新类型必须改旧代码
* 完全违背扩展原则

**多态的目标只有一个：**

调用方不关心对象的具体类型，只关心它“能做什么”。

## Python 中最基础的多态形式

Python 不需要接口关键字，也不需要强制继承。

```
```
class Dog:
    def speak(self):
        print("wang")

class Cat:
    def speak(self):
        print("miao")
```
```

统一调用：

```
```
def make_sound(animal):
    animal.speak()
```
```

使用：

```
```
make_sound(Dog())
make_sound(Cat())
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYSFf8Yiafk3ibSkF4NwzSLPehYfD4icVYL1ibiaia1s0YT9BEA90oaqrOIbHNZiaXa0veB4tqsOpr0nW2U7g/640?wx_fmt=png&from=appmsg)

这就是多态。

Python 的多态是**行为驱动**，而不是**类型驱动**。

## 鸭子类型：Python 多态的核心思想

那句经典的话你一定听过：

“如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子。”

示例：

```
```
class FileLogger:
    def write(self, msg):
        print(f"file: {msg}")

class SocketLogger:
    def write(self, msg):
        print(f"socket: {msg}")
```
```

统一使用：

```
```
def log(writer):
    writer.write("hello")
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYSFf8Yiafk3ibSkF4NwzSLPehShq4OxeZRtuE15DQHwtkm7DUOgz8V2iaDWQ5Xbo9S1fYPJ4g9UhNGDA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

网络技术联盟站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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