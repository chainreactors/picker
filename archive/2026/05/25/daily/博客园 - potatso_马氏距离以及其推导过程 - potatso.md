---
title: 马氏距离以及其推导过程 - potatso
url: https://www.cnblogs.com/potatso/p/20150670
source: 博客园 - potatso
date: 2026-05-25
fetch_date: 2026-05-26T06:09:15.434838
---

# 马氏距离以及其推导过程 - potatso

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [周边](https://cnblogs.vip/store)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19316348)
* [YouClaw](https://youclaw.dev/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://www.cnblogs.com/my "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://www.cnblogs.com/my)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [马氏距离以及其推导过程](https://www.cnblogs.com/potatso/p/20150670 "发布于 2026-05-25 10:54")

在欧式距离中，我们默认各个维度均值为0，方差为1，且相互独立。但是在实际情况中，会出现以下两类大问题：
-　**纲（尺度）不同**：比如身高（m）和体重（kg），数值范围完全不同。

* **特征相关性**：比如身高和体重往往高度正相关。

如果直接算欧氏距离，数据在概率密度高的方向（相关性方向）上的距离会被放大。马氏距离的本质，就是**先将原始数据进行旋转和缩放（去相关和标准化），在这个新空间中再计算欧氏距离**。

## 数学推导过程

假设我们有一个随机向量 \(X = [x\_1, x\_2, \dots, x\_d]^T\)，其均值为 \(\mu = [\mu\_1, \mu\_2, \dots, \mu\_d]^T\)，协方差矩阵为 \(\Sigma\)。我们的目标是计算 \(X\) 到均值 \(\mu\) 的马氏距离。

### 步骤一：去中心化

首先，将数据减去均值，移动到原点：

\[Y = X - \mu
\]

### 步骤二：消除相关性（线性变换）

因为特征之间存在相关性，协方差矩阵 \(\Sigma\) 不是对角矩阵。根据线性代数，协方差矩阵 \(\Sigma\) 是一个实对称矩阵，我们对其进行**特征分解（Eigendecomposition）**：

\[\Sigma = P \Lambda P^T
\]

其中：

* \(P\) 是正交矩阵（\(P^T P = I\)），其列向量是 \(\Sigma\) 的特征向量。它代表了一个**旋转变换**。
* \(\Lambda\) 是对角矩阵，对角线上的元素 \(\lambda\_i\) 是特征值（代表数据在特征向量方向上的方差）。

为了消除相关性，我们通过正交矩阵 \(P^T\) 对去中心化的数据 \(Y\) 进行旋转（等距变换），得到新坐标系下的向量 \(Z\)：

\[Z = P^T Y = P^T (X - \mu)
\]

此时，新变量 \(Z\) 的各个维度之间已经互不相关了，其协方差矩阵变成了对角阵 \(\Lambda\)。

### 步骤三：标准化（消除方差影响）

虽然 \(Z\) 的各维度互不相关，但它们在各个方向上的方差（即特征值 \(\lambda\_i\)）依然不同。为了让每个方向的标准差都变为 1，我们需要对每个维度除以其标准差 \(\sqrt{\lambda\_i}\)。

在线性代数中，这相当于左乘 \(\Lambda^{-1/2}\)：

\[W = \Lambda^{-1/2} Z = \Lambda^{-1/2} P^T (X - \mu)
\]

此时，新向量 \(W\) 的每个维度不仅互不相关，而且方差均为 1（即 \(\Sigma\_W = I\)）。

### 步骤四：计算新空间中的欧氏距离

在经过“去相关”和“标准化”后的完美空间（\(W\) 空间）中，我们直接计算 \(W\) 到原点的普通欧氏距离。

欧氏距离的平方为：

\[D^2 = W^T W
\]

现在，我们将前面步骤中 \(W\) 的表达式代入：

\[D^2 = \left[ \Lambda^{-1/2} P^T (X - \mu) \right]^T \left[ \Lambda^{-1/2} P^T (X - \mu) \right]
\]

根据矩阵转置的性质 \((AB)^T = B^T A^T\)，展开左半部分：

\[D^2 = (X - \mu)^T P (\Lambda^{-1/2})^T \Lambda^{-1/2} P^T (X - \mu)
\]

因为 \(\Lambda\) 是对角阵，所以 \((\Lambda^{-1/2})^T = \Lambda^{-1/2}\)，且 \(\Lambda^{-1/2} \Lambda^{-1/2} = \Lambda^{-1}\)：

\[D^2 = (X - \mu)^T P \Lambda^{-1} P^T (X - \mu)
\]

回想一下步骤二中 \(\Sigma = P \Lambda P^T\)，我们求它的逆矩阵：

\[\Sigma^{-1} = (P \Lambda P^T)^{-1} = (P^T)^{-1} \Lambda^{-1} P^{-1}
\]

因为 \(P\) 是正交阵，所以 \(P^{-1} = P^T\) 且 \((P^T)^{-1} = P\)。因此：

\[\Sigma^{-1} = P \Lambda^{-1} P^T
\]

正好对应了公式中间的部分！我们将其替换掉：

\[D^2 = (X - \mu)^T \Sigma^{-1} (X - \mu)
\]

这就是**马氏距离的平方**公式。

## 3. 最终公式

因此，向量 \(X\) 与均值 \(\mu\) 之间的**马氏距离**定义为：

\[D\_M(X, \mu) = \sqrt{(X - \mu)^T \Sigma^{-1} (X - \mu)}
\]

如果是计算两个样本点 \(X\_i\) 和 \(X\_j\) 之间的马氏距离，公式同理为：

\[D\_M(X\_i, X\_j) = \sqrt{(X\_i - X\_j)^T \Sigma^{-1} (X\_i - X\_j)}
\]

## 4. 总结

* **当 \(\Sigma = I\)（单位矩阵）时**：意味着数据各个维度独立且方差均为 1，此时马氏距离**退化为普通的欧氏距离**。
* **当 \(\Sigma\) 是对角阵时**：意味着数据各维度独立但方差不同，此时马氏距离就是**标准化欧氏距离**（Normalized Euclidean Distance）。

**一句话理解马氏距离的推导：**

它通过协方差矩阵的逆 \(\Sigma^{-1}\)，默默地对原始数据做了一次**旋转（消除相关性）**和**缩放（消除方差尺度）**，使得原本呈椭圆状分布的数据变成了正圆状分布，从而能用欧氏距离进行公平的测量。

posted @
2026-05-25 10:54
[potatso](https://www.cnblogs.com/potatso)
阅读(4)
评论(0)

收藏
[举报](https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fpotatso%2Fp%2F20150670&targetId=20150670&targetType=0)

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202604/35695-20260423213336272-1914399152.webp)](https://www.volcengine.com/activity/codingplan?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=cnblogs)

### 公告

[博客园](https://www.cnblogs.com/)
  ©  2004-2026