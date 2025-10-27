---
title: 【人工智能】用Python实现图卷积网络（GCN）：从理论到节点分类实战
url: https://blog.csdn.net/nokiaguy/article/details/144536005
source: 一个被知识诅咒的人
date: 2024-12-18
fetch_date: 2025-10-06T19:36:16.261607
---

# 【人工智能】用Python实现图卷积网络（GCN）：从理论到节点分类实战

# 【人工智能】用Python实现图卷积网络（GCN）：从理论到节点分类实战

原创
已于 2025-01-09 16:52:48 修改
·
2k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

19

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

22
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#网络](https://so.csdn.net/so/search/s.do?q=%E7%BD%91%E7%BB%9C&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-12-17 15:00:21 首次发布

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
同时被 2 个专栏收录![](https://csdnimg.cn/release/blogv2/dist/pc/img/newArrowDown1White.png)](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756780.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

人工智能](https://blog.csdn.net/nokiaguy/category_1260139.html "人工智能")

195 篇文章

订阅专栏

### 目录

1. [引言](#%E5%BC%95%E8%A8%80)
2. [图卷积网络理论基础](#%E5%9B%BE%E5%8D%B7%E7%A7%AF%E7%BD%91%E7%BB%9C%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80)
   * 2.1 图的基本概念
   * 2.2 卷积神经网络在图上的扩展
   * 2.3 GCN的数学模型
3. [GCN的实现](#GCN%E7%9A%84%E5%AE%9E%E7%8E%B0)
   * 3.1 环境配置
   * 3.2 数据集介绍与预处理
   * 3.3 模型构建
   * 3.4 训练与优化
4. [实战：节点分类](#%E5%AE%9E%E6%88%98%E8%8A%82%E7%82%B9%E5%88%86%E7%B1%BB)
   * 4.1 模型训练
   * 4.2 结果分析
   * 4.3 可视化
5. [代码详解](#%E4%BB%A3%E7%A0%81%E8%AF%A6%E8%A7%A3)
   * 5.1 数据预处理代码
   * 5.2 GCN模型代码
   * 5.3 训练与评估代码
6. [结论](#%E7%BB%93%E8%AE%BA)
7. [参考文献](#%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE)

---

### 引言

随着社交网络、生物网络和知识图谱等复杂图结构数据的广泛应用，传统的深度学习方法在处理非欧几里得数据时面临诸多挑战。图卷积网络（GCN）作为图神经网络（Graph Neural Networks, GNNs）的一种重要变种，通过在图结构上进行卷积操作，实现了对图数据的有效表示和学习。自2017年Kipf和Welling提出GCN以来，其在节点分类、图分类、链接预测等任务中取得了显著成果。

本文将深入探讨GCN的理论基础，详细介绍其在节点分类任务中的实现方法。通过Python和PyTorch框架，我们将从零开始构建GCN模型，涵盖数据预处理、模型设计、训练优化及结果评估等全过程。文中提供的代码示例配有详尽的中文注释，旨在帮助读者理解并掌握GCN的实现细节。

### 图卷积网络理论基础

#### 2.1 图的基本概念

在计算机科学中，\*\*图（Graph）\*\*是一种由节点（Vertices）和边（Edges）组成的数据结构，用于表示实体及其之间的关系。形式上，一个图可以表示为 ( G = (V, E) )，其中：

* ( V ) 是节点集合，节点数量为 ( N = |V| )。
* ( E ) 是边集合，边可以是有向的或无向的。

图可以用邻接矩阵（Adjacency Matrix）( A \in \mathbb{R}^{N \times N} )表示，其中 ( A\_{ij} = 1 ) 表示节点 ( i ) 和节点 ( j ) 之间存在边，反之为0。

此外，图中的每个节点可以具有特征向量 ( X \in \mathbb{R}^{N \times F} )，其中 ( F ) 是每个节点的特征维度。

#### 2.2 卷积神经网络在图上的扩展

传统的卷积神经网络（Convolutional Neural Networks, CNNs）主要应用于欧几里得数据（如图像、音频），其核心在于利用卷积操作捕捉局部特征。然而，图数据的非欧几里得性使得传统卷积难以直接应用。

为了解决这一问题，研究者提出了多种在图上进行卷积的方法，主要分为谱方法和空间方法：

* **谱方法**：基于图的谱理论，利用图拉普拉斯算子（Graph Laplacian）进行卷积操作。
* **空间方法**：直接在图的邻域结构上定义卷积操作，更加直观且易于扩展。

GCN属于谱方法的一种简化形式，通过对图拉普拉斯算子进行近似，实现高效的图卷积。

#### 2.3 GCN的数学模型

GCN的核心思想是通过多层图卷积操作，将节点的特征与其邻居节点的特征进行聚合和变换。以Kipf和Welling提出的GCN为例，其基本的图卷积层可以表示为：

H
(
l
+
1
)
=
σ
(
D
^
−
1
/
2
A
^
D
^
−
1
/
2
H
(
l
)
W
(
l
)
)
H^{(l+1)} = \sigma\left( \hat{D}^{-1/2} \hat{A} \hat{D}^{-1/2} H^{(l)} W^{(l)} \right)
H(l+1)=σ(D^−1/2A^D^−1/2H(l)W(l))

其中：

* ( H^{(l)} ) 是第 ( l ) 层的节点特征矩阵，( H^{(0)} = X )。
* ( \hat{A} = A + I\_N ) 是加上自连接后的邻接矩阵，( I\_N ) 是单位矩阵。
* ( \hat{D} ) 是 ( \hat{A} ) 的度矩阵，即 ( \hat{D}*{ii} = \sum\_j \hat{A}*{ij} )。
* ( W^{(l)} ) 是第 ( l ) 层的可学习权重矩阵。
* ( \sigma ) 是激活函数，如ReLU。

通过上述公式，GCN层实现了节点特征的聚合和线性变换，从而逐层提取更高层次的图结构信息。

### GCN的实现

#### 3.1 环境配置

在开始实现GCN之前，需要配置相应的开发环境。本文使用Python编程语言，结合PyTorch深度学习框架。以下是环境配置的主要步骤：

1. **安装Python**：建议使用Python 3.8及以上版本。
2. **安装必要的库**：

```
pip install torch torchvision
pip install numpy scipy scikit-learn
pip install matplotlib
```

3. **安装PyTorch Geometric（可选）**：虽然本文将手动实现GCN，但PyTorch Geometric提供了丰富的图神经网络工具，可供参考。

```
pip install torch-geometric
```

#### 3.2 数据集介绍与预处理

节点分类任务常用的数据集包括Cora、Citeseer和Pubmed。本文以Cora数据集为例，介绍数据的结构和预处理方法。

**Cora数据集**包含2708个科研论文，这些论文根据内容被划分为7个类别，构成一个引用图，边表示论文之间的引用关系。每个节点的特征是一个1433维的词袋向量。

**数据预处理步骤**：

1. **加载数据**：读取节点特征、标签和邻接关系。
2. **构建邻接矩阵**：基于引用关系构建稀疏邻接矩阵。
3. **特征标准化**：对节点特征进行标准化处理。
4. **划分训练集、验证集和测试集**。

以下是数据预处理的Python代码示例：

```
import numpy as np
import scipy.sparse as sp
import torch
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# 加载数据
def load_data(path="cora/", dataset="cora"):
    # 读取节点特征和标签
    idx_features_labels = np.genfromtxt("{}{}.content".format(path, dataset), dtype=np.dtype(str))
    features = sp.csr_matrix(idx_features_labels[:, 1:-1], dtype=np.float32)
    labels = idx_features_labels[:, -1]

    # 标签编码
    le = LabelEncoder()
    labels = le.fit_transform(labels)

    # 构建节点索引映射
    idx = np.array(idx_features_labels[:, 0], dtype=np.int32)
    idx_map = {j: i for i, j in enumerate(idx)}

    # 读取边信息并构建邻接矩阵
    edges_unordered = np.genfromtxt("{}{}.cites".format(path, dataset), dtype=np.int32)
    edges = np.array(list(map(idx_map.get, edges_unordered.flatten())), dtype=np.int32).reshape(edges_unordered.shape)
    adj = sp.coo_matrix((np.ones(edges.shape[0]), (edges[:,0], edges[:,1])), shape=(labels.shape[0], labels.shape[0]), dtype=np.float32)

    # 构建对称的邻接矩阵
    adj = adj + adj.T.multiply(adj.T > adj) - adj.multiply(adj.T > adj)

    return features, adj, labels

# 特征标准化
def normalize_features(features):
    rowsum = np.array(features.sum(1))
    r_inv = np.power(rowsum, -1).flatten()
    r_inv[np.isinf(r_inv)] = 0.
    r_mat_inv = sp.diags(r_inv)
    features = r_mat_inv.dot(features)
    return features

# 构建归一化的邻接矩阵
def normalize_adj(adj):
    adj = sp.coo_matrix(adj)
    rowsum = np.array(adj.sum(1))
    d_inv_sqrt = np.power(rowsum, -0.5).flatten()
    d_inv_sqrt[np.isinf(d_inv_sqrt)] = 0.
    D_inv_sqrt = sp.diags(d_inv_sqrt)
    return adj.dot(D_inv_sqrt).transpose().dot(D_inv_sqrt).tocoo()

# 构建训练、验证和测试集
def train_val_test_split(labels, train_size=0.1, val_size=0.1, test_size=0.8, random_state=42):
    idx = np.arange(len(labels))
    idx_train, idx_temp, y_train, y_temp = train_test_split(idx, labels, train_size=train_size, stratify=labels, random_state=random_state)
    idx_val, idx_test, y_val, y_test = train_test_split(idx_temp, y_temp, train_size=val_size/(val_size + test_size), stratify=y_temp, random_state=random_state)
    return idx_train, idx_val, idx_test

# 主数据处理函数
def preprocess_data():
    features, adj, labels = load_data()
    features = normalize_features(features)
    adj_normalized = normalize_adj(adj + sp.eye(adj.shape[0]))

    idx_train, idx_val, idx_test = train_val_test_split(labels)

    # 转换为torch张量
    features = torch.FloatTensor(np.array(features.todense()))
    labels = torch.LongTensor(labels)
    adj = sparse_mx_to_torch_sparse_tensor(adj_normalized)
    idx_train = torch.LongTensor(idx_train)
    idx_val = torch.LongTensor(idx_val)
    idx_test = torch.LongTensor(idx_test)

    return adj, features, labels, idx_train, idx_val, idx_test

# 稀疏矩阵转换为torch张量
def sparse_mx_to_torch_sparse_tensor(sparse_mx):
    sparse_mx = sparse_mx.tocoo().astype(np.float32)
    indices = torch.from_numpy(
        np.vstack((sparse_mx.row, sparse_mx.col)).astype(np.int64)
    )
    values = torch.from_numpy(sparse_mx.data)
    shape = torch.Size(sparse_mx.shape)
    return torch.sparse.FloatTensor(indices, values, shape)

# 执行数据预处理
adj, features, labels, idx_train, idx_val, idx_test = preprocess_data()
```

#### 3.3 模型构建

基于PyTorch框架，我们将构建一个两层的GCN模型。每一层GCN包括图卷积操作和激活函数。最终输出通过Softmax函数得到每个节点的类别概率分布。

以下是GCN模型的实现代码：

```
import torch
import torch.nn as nn
import torch.nn.functional as F

class GCNLayer(nn.Module):
    def __init__(self, in_features, out_features, dropout=0.5, activation=F.relu):
        super(GCNLayer, self).__init__()
        self.linear = nn.Linear(in_features, out...