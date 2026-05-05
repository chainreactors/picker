---
title: 核方法：从线性到非线性的\"升维打击\"
url: https://mp.weixin.qq.com/s/5ke-G_ng40v4FXSmQANmNg
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:00:04.640609
---

# 核方法：从线性到非线性的\"升维打击\"

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hyaRUFucbbqcwdvVzRLibyfvyjuGFRic7npBObCYEq0xPG4aXffia6Ghkj03z1O8htzN8tY9VTekPDa3ruR7zPJ3VfW6momAjULzlD3O9yp9icM/0?wx_fmt=jpeg)

# 核方法：从线性到非线性的"升维打击"

原创

代码小铺
代码小铺

代码小铺

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 代码小铺 | 用数学的眼光看机器学习

你有没有遇到过这样的场景：明明数据就摆在眼前，却怎么也找不到一条直线把它们分开？

别急着上深度学习——有时候，答案藏在一个更优雅、更深刻的数学工具里：核方法。

## 引言：那个分不开的圆

想象你在一张纸上画了两组点：内圈是红色，外圈是蓝色。

现在，请试着画一条**直线**，把红点和蓝点分开。

做不到吧？这很正常。线性分类器的本质限制就是——它只能画直线。在二维平面上，有些问题天生就是非线性的。

但如果……你把这张纸揉一揉、折一折，让红点和蓝点在某个新的空间里分开呢？

这就是核方法的核心思想：**升维打击**。

## 核心概念：映射到高维空间

核方法的思路其实非常直观：

> 如果数据在低维空间线性不可分，那就把它映射到高维空间试试。

数学上，我们用一个映射函数 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbqxKEFY5J1a90eEBKh39I82h9KlzazDLdnFKzDtpGFdyFtIQV6FaKEmz0s4eOTjeRfk5LgMLgt5reIDZvXWjjUA6V1tJFTIGyc/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbqekpZiaNe4o0z2lapBbEN6Dut3on09BIlGXQGIUpgiaFEkSyIXVUAicricc3Dz8T2npCDLY3PH3atSvk0OlWohC1Lvkbq8O55twhM/640?from=appmsg)

其中 *D \gg d*，甚至 *D* 可以是无穷大。

回到那个同心圆的例子——如果我们把二维的 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbboiboSqILGMaicZTRDeCJ8KlKazweoVH9lEt9ckGNmdbTyPFkxV6GibPHyJb536fDBeImom1tAlhXtn7sbmx5bulLb5hpabysZlbU/640?from=appmsg) 映射到三维，加一个特征 ![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbbp0sFzdQqbRDwlh4LWiblUMJNc91MlsOTF2SicFIluW0ciasqn6XGu6QUKYUkOKcYv8Q1cEVTp3JGujCV7HZ8v1gHx8GMmBEfnTPQ/640?from=appmsg)，也就是点到原点的距离。在这个新空间里，内圈和外圈的点在"高度"上就分开了！

**一条水平的平面就能把它们完美切开。**

## 公式推导：核技巧的魔力

但这里有个问题：如果高维空间是几万维、甚至无穷维，我们怎么算得过来？

答案是——**根本不需要算**。这就是核方法最精妙的地方：**核技巧（Kernel Trick）**。

### 内积是关键

在线性分类器中，真正重要的不是映射后的向量 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbpAu3icdJ6tKjwz4C7VhBduf20T8LDpmo2kUJe37cwN4GVRjx8CRLenibPkdJ6iauyMSYGrcGaEujVZVedarOLLfzYUtQUXx8WVJQ/640?from=appmsg) 本身，而是它们之间的**内积**：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbrv2VnrZMriaS5lyviau1LuNKDHYxEkFFK975qqgrFt7icVC5EoPuLJE70mHNb3OBaPXj9RcicHdNrYkppsYU36NBbgJdvEp3SGO1c/640?from=appmsg)

核方法的核心洞察是：我们不需要显式地计算 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbpAu3icdJ6tKjwz4C7VhBduf20T8LDpmo2kUJe37cwN4GVRjx8CRLenibPkdJ6iauyMSYGrcGaEujVZVedarOLLfzYUtQUXx8WVJQ/640?from=appmsg)，只需要找到一个函数 *K*，使得：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbpwto616O2c1Utgic2DG7ViacJ5uwYGMWXsaa7Vbp7XgriaH6mewCVFoBTuX0a4NapdvLSqRC49TEbsV3RQSgIAwKdcQdibTyFpKUQ/640?from=appmsg)

这个 *K* 就是**核函数**。它直接在原始空间里算出了高维空间中的内积。

### 一个经典例子：多项式核

最直观的多项式核长这样：

![](https://mmbiz.qpic.cn/mmbiz_png/hyaRUFucbboIVo1iaw9J4q1cA4bODiaeau3b6oNp8I8ZVPqAJctf9YMmrvaq4rvUQo7S2xibtz14uuX13QtOIZrL9rcI7gEZIbsLc4Il25IbX0/640?from=appmsg)

当 *p = 2*、*c = 1* 时，展开后相当于在计算所有原始特征的一次项、二次项和交叉项的内积。但你只算了一次点积加常数，然后平方——计算量从指数级降到了线性级！

### 更强大的武器：RBF核

实际中最常用的是**径向基函数核（RBF核）**，也叫高斯核：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbboxdJ8GAr8YKo2wF6dhV6Tlo5LOibyITNMDyUkdw0oL3GTicGljrZKBX8tibiaFtMibsIsExcpr6rSXiaKiaXTF24UHutux8rf5hC5rZs/640?from=appmsg)

这个核函数对应的特征空间是**无穷维**的。这意味着它理论上可以拟合任意复杂的决策边界。

直观理解：RBF核衡量的是两个样本点的"相似度"。距离越近，值越接近 1；距离越远，值趋近于 0。它相当于在每个样本点周围放了一个小"气泡"，气泡的叠加形成了最终的分类面。

### 数学保证：Mercer定理

不是随便一个函数都能当核函数。Mercer定理告诉我们：一个对称函数 *K(x, y)* 是合法核函数的充要条件是，对任意一组样本，它的核矩阵是**半正定**的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hyaRUFucbbrHXZiajnLMkgqUjkQKjZoMDpicXwlLEkKeGPWib1TvvQEygRN01Vv4AIq1NxryMvRZ8lXHEL7TjBBZMmrF2PGa7ZVTeIZANb74Wc/640?from=appmsg)

这个条件保证了核函数确实对应某个高维空间中的内积。

## 实际应用：核方法无处不在

核方法最经典的舞台是**支持向量机（SVM）**。核SVM 在深度学习崛起之前，长期是分类任务的王者。

### 文本分类

把文档表示为 TF-IDF 向量后，用线性核或 RBF 核做 SVM 分类，在垃圾邮件检测、情感分析等任务上效果出色。

### 生物信息学

蛋白质序列、基因表达数据通常样本少、维度高，核方法在这种"小样本大维度"的场景下特别有效。

### 推荐系统

通过设计合适的核函数来衡量用户和物品的相似度，核方法可以捕捉复杂的用户偏好模式。

### 一个直观的例子

用 scikit-learn 实现核SVM其实只需要几行代码：

```
  from sklearn import svm

clf = svm.SVC(kernel='rbf', gamma='scale')
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
```

把 `kernel` 从 `'linear'` 换成 `'rbf'`，同一个算法就能从只能画直线的"老实人"，变成能画出任意复杂曲线的"艺术家"。

## 核方法 vs 深度学习

有人可能会问：都2025年了，为什么还要关注核方法？

核方法有几个独特优势：

* • **理论优美**：有严格的数学保证，不是"玄学调参"
* • **小样本友好**：不需要海量数据就能训练
* • **可解释性更强**：支持向量给出了清晰的决策依据
* • **计算高效**：对中小规模问题，训练和推理都很快

当然，深度学习在处理图像、语音等大规模非结构化数据方面不可替代。但核方法和深度学习并非对立——近年来，神经正切核（Neural Tangent Kernel）理论甚至在两者之间架起了桥梁。

## 总结

核方法的精髓可以用一句话概括：

> **与其在低维空间里绞尽脑汁找非线性边界，不如把数据映射到高维空间里，让问题变回简单的线性问题。**

这种"升维打击"的思想，不仅在机器学习中大放异彩，在更广泛的科学和工程领域也有深远影响。下次遇到"分不开"的问题时，不妨想想：也许换个维度，世界就豁然开朗了。

---

*欢迎在评论区分享你对核方法的理解和应用经验！如果这篇文章让你对机器学习有了新的认识，点个"在看"就是对我最大的鼓励。*

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