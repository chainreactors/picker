---
title: Python 面向对象编程——属性和类关键字
url: https://mp.weixin.qq.com/s/WrhSXMFr79qKj7BooU4vFg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:21:42.233520
---

# Python 面向对象编程——属性和类关键字

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6OibpDQ66VYQtFznRDhKHEqO0nvkabNLQkMnImXNTiaFLk7qnC5mhgT4K12pOjKNnV2j3AVEvflHwE0nRjg6ghSA/0?wx_fmt=jpeg)

# Python 面向对象编程——属性和类关键字

原创

Lino

网络技术联盟站

![]()

在小说阅读器中沉浸阅读

各位同学，大家好！我是你们的 Python 讲师 Lino。

![](https://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQtFznRDhKHEqO0nvkabNLQjqTDTlLZ6zGqNAOuY6FlLibMNibq6dUib6zLtKNuU2qNmEMFdnqojNvGw/640?wx_fmt=png&from=appmsg)

在 Python 的面向对象体系里，**`class` 不是语法糖，属性也不是随便挂的变量**。

如果你只把它们当成“能跑就行”，那么在规模稍微大一点的代码里，问题会迅速暴露。

这一节我们只做两件事：

1. 把 class 这个关键字讲清楚
2. 把“属性到底存在哪里、怎么查找”讲清楚

## `class` 到底做了什么？

从解释器角度看，`class` 干了三件事：

1. 创建一个新的类对象
2. 执行类体代码
3. 把类体中定义的名字，收集到类的命名空间

看一个最简单的例子：

```
```
class Demo:
    x = 10

    def foo(self):
        return self.x
```
```

你可以验证：

```
```
print(Demo)
print(type(Demo))
print(Demo.__dict__.keys())
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQtFznRDhKHEqO0nvkabNLQRx6Dic4CxJmpuSvia5aicpic3YTyckvqRHpNOM74A1LfRrRPJd0E97JtWQ/640?wx_fmt=png&from=appmsg)

你会看到：

* Demo 本身是一个对象
* 类型是 type
* x、foo 都存在于 Demo.\_\_dict\_\_

**重要结论：**

> 类本身也是对象，属性首先存放在类对象上。

## 属性的两大类：类属性 vs 实例属性

这是本节最核心的内容。

### 类属性

```
```
class User:
    role = "guest"
```
```

`role` 存在于：

```
```
User.__dict__
```
```

所有实例**默认共享**它。

---

### 实例属性

```
```
class User:
    def __init__(self, name):
        self.name = name
```
```

`name` 存在于：

```
```
u = User("alice")
u.__dict__
```
```

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