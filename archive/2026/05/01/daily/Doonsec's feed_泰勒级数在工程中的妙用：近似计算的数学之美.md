---
title: 泰勒级数在工程中的妙用：近似计算的数学之美
url: https://mp.weixin.qq.com/s/_U5gnItWUNE24_ej3vk_rA
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:58:34.480142
---

# 泰勒级数在工程中的妙用：近似计算的数学之美

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hyaRUFucbbrCDjFRqN9nibQcc3d9g054SLrACWlJSqUIibOwv35nMGoicu7npvVsJw7xNmmUM2A3PZxUPQfQ32Q6TQy3WOzSsMxb27m4jfxyib8/0?wx_fmt=jpeg)

# 泰勒级数在工程中的妙用：近似计算的数学之美

原创

代码小铺
代码小铺

代码小铺

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 代码小铺 · 用数学的语言，拆解世界的运行规则

---

## 引言

想象一个场景：你的计算器要计算 sin(0.1)，但它并没有内置三角函数表。它是怎么做到的？答案藏在一个 300 多年前由布鲁克·泰勒发现的公式里——**泰勒级数**。

今天，从你手机里的人脸识别，到火箭发射的轨道计算，再到深度学习框架里的激活函数近似，泰勒级数无处不在。它是工程师手中的「万能撬棍」：把复杂的函数拆解成简单的多项式，让不可能计算的事情变得触手可及。

## 核心概念：用多项式「模仿」复杂函数

泰勒级数的核心思想非常直觉：**如果你知道一个函数在某一点的所有导数信息，你就能用它周围的多项式来逼近这个函数。**

打个比方：你想知道一个人的性格，不需要了解他的全部人生。只要知道他在某个关键时刻的反应（函数值）、他反应的速度变化（一阶导数）、加速度的变化（二阶导数）……知道得越多，你对这个人的了解就越接近真实。

数学上，函数 f(x) 在 x = a 处的泰勒展开为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbo6Yf1QTIBeqiaUiaI3ibrnGuWoomPs36UdMZTmk5tvz23cZH4JWrl6YeicVkibYHojOxWpglkXW2aGbs3EWicicFQpKnbiafXYEZ3oK1k/640?from=appmsg)

写成紧凑的求和形式：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbqMEd3DJPiauuTE7y6K4FAffVQtYF5c4GpIBf5FlMY0XcZTcgGF7JRAxUAlxUyXZc2aR8TdTrIibTWZKS8eoYbCX6TkzqJicGxgyo/640?from=appmsg)

当 a = 0 时，这个展开有一个特别的名字——**麦克劳林级数**。

## 公式推导：从 sin(x) 看泰勒级数的威力

让我们拿最经典的例子 sin(x) 来演示。在 a = 0 处展开：

* • f(0) = sin(0) = 0
* • f'(0) = cos(0) = 1
* • f''(0) = -sin(0) = 0
* • f'''(0) = -cos(0) = -1
* • f''''(0) = sin(0) = 0

奇数阶导数交替出现 1 和 -1，偶数阶导数全是 0。于是：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbrFbtVa5BXvzyKfcFt7iaGZobic06WrtCoMTbeRyw76UyMjjYPn1KegkYn7iblLzEEBicwQfCbJx1JKtAy145IbK8kVbPZnnWxrPJk/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbboFdoGElRGzezzjEdsYhrFJdJiaAnciafgdH7P3FByQk41libjLhyz8Z0RMGOBRJR6xEu029aib7zcH5IGIkYG4P7fG17a3LvjL7gc/640?from=appmsg)

现在我们来验证一下精度。取 x = 0.1：

* • 只取第一项：0.1
* • 取前两项：0.1 - 0.001/6 ≈ 0.099833
* • 取前三项：0.1 - 0.001/6 + 0.00001/120 ≈ 0.0998334

而真实值 sin(0.1) ≈ 0.0998334... **仅用三项，精度就已经达到了小数点后七位！**

更令人惊叹的是，泰勒级数的误差有一个漂亮的上界。如果只取前 n 项，误差满足：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbo9ngk4ucBib0V9mzg7tRHXBTL1icYG0G8PXiakfJ4cKuajc6xsZUwWQYgSkmcQFAI8AQoibj8LBM0zX5rBOAZ5PV4J0HFWHWzPvpQ/640?from=appmsg)

其中 M 是 f 的 (n+1) 阶导数在区间内的最大值。因为分母是阶数增长，误差收敛得飞快。

## 实际应用场景

### 1. 计算器与芯片设计

你手机里的处理器不会为每个 sin、cos、exp 建立庞大的查找表。相反，它们用泰勒级数的前几项做近似。为什么？因为多项式运算——加减乘——是硬件最擅长的事情。

以 e^x 的展开为例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbboybCvP6wnIXyxE1EBR3CibTVB0klDY5ibbKhIYzoJRphtQdkmvc7sRgFzAfC0ELHuA5h7uhMbDOAPia0NCNMGv38UI6licibkHdZSo/640?from=appmsg)

在 x 较小时，只取前 5-7 项就能达到单精度浮点数的要求。芯片设计者会在精度和计算速度之间找到最优平衡点。

### 2. 物理学中的小角度近似

单摆运动中，恢复力正比于 sin(θ)。当 θ 很小时，用泰勒级数一阶近似：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbboGHUeiac5EmmbhhAbCBmQowoZ4vtz3v4wibur9aEflRXFevdrAPGrsR0BqFOpAM01KMEVjrcVvS2Yq8sDBUxjXjBLK7d0QtE5XE/640?from=appmsg)

这个简单的近似把非线性的单摆方程变成了线性微分方程，让我们能直接得到解析解。这就是为什么高中物理里单摆周期公式 T = 2π√(L/g) 只在「小角度」下成立——因为那时我们偷偷用了泰勒展开。

### 3. 机器学习中激活函数的近似

在神经网络硬件加速中，像 GELU 这样的激活函数包含 erf（误差函数），计算成本很高。工程师们用泰勒多项式在特定区间内近似它，在 GPU 上可以大幅提升推理速度。

### 4. 数值分析与工程仿真

有限元分析、流体力学仿真中，复杂的非线性本构关系经常在工作点附近做泰勒展开，把问题线性化后求解，再用迭代逐步修正。这就是牛顿法的本质——**用一阶泰勒展开来寻找函数的零点**。

牛顿法的迭代公式：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbpsRrQhkPdURIJRHvC1ia6HEaod220ZR7m7ezKtpic88NChecNibIXxjtibK55yubB85PXCwxt49qa3mlh6fdbSvOObBibmLlGZSicLA/640?from=appmsg)

它的推导正是来自一阶泰勒近似 f(x) ≈ f(xₙ) + f'(xₙ)(x - xₙ) = 0。

## 总结

泰勒级数的魅力在于它的**普适性**：几乎所有光滑函数都能被拆解成简单的多项式之和。它告诉我们一个深刻的道理——**复杂往往只是简单的叠加**。

下次当你用手机计算一个三角函数，或者看到火箭精确入轨的新闻时，不妨在心里向 300 年前的布鲁克·泰勒致敬。那个把函数拆成多项式的天才想法，至今仍在驱动着整个现代工程世界。

---

*代码小铺，用通俗的语言讲透技术原理。如果觉得有收获，欢迎关注我们～*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/XrMnA4yTvjvhoROhAP2xiak56A4IOMjIEIrN56l3cn3vHZXxxfusUjIdhWfLXeSyx73b3DjgT6mdVdVkNPklxug/0?wx_fmt=png)

代码小铺

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/XrMnA4yTvjvhoROhAP2xiak56A4IOMjIEIrN56l3cn3vHZXxxfusUjIdhWfLXeSyx73b3DjgT6mdVdVkNPklxug/0?wx_fmt=png)

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