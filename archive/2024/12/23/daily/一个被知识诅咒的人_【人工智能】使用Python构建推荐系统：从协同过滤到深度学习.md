---
title: 【人工智能】使用Python构建推荐系统：从协同过滤到深度学习
url: https://blog.csdn.net/nokiaguy/article/details/144644618
source: 一个被知识诅咒的人
date: 2024-12-23
fetch_date: 2025-10-06T19:36:00.046028
---

# 【人工智能】使用Python构建推荐系统：从协同过滤到深度学习

# 【人工智能】使用Python构建推荐系统：从协同过滤到深度学习

原创
已于 2025-01-09 16:50:49 修改
·
1.4k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

11

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

10
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#深度学习](https://so.csdn.net/so/search/s.do?q=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-12-22 12:16:04 首次发布

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
同时被 2 个专栏收录![](https://csdnimg.cn/release/blogv2/dist/pc/img/newArrowDown1White.png)](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756780.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

人工智能](https://blog.csdn.net/nokiaguy/category_1260139.html "人工智能")

195 篇文章

订阅专栏

推荐系统是现代互联网的重要组成部分，广泛应用于电商、社交媒体和流媒体平台中。本文详细介绍了如何使用Python构建推荐系统，从传统的协同过滤方法，到基于深度学习的推荐模型。我们将先了解推荐系统的基本概念，随后实现基于用户和物品的协同过滤模型，最后引入深度学习的嵌入技术，展示如何利用神经网络提升推荐效果。代码示例贯穿全篇，并配有详尽的中文注释，帮助读者逐步理解和构建推荐系统，适合对机器学习和推荐系统有一定了解的开发者。

### 目录

1. 推荐系统简介
2. 基于协同过滤的推荐系统
   * 用户协同过滤实现
   * 物品协同过滤实现
3. 使用矩阵分解提升推荐质量
4. 深度学习推荐系统
   * 神经网络嵌入实现
   * 使用TensorFlow构建深度推荐系统
5. 总结

### 1. 推荐系统简介

推荐系统是一种通过分析用户的行为和偏好，为用户提供个性化内容的系统。现代推荐系统可以分为三类：基于内容的推荐、协同过滤推荐和混合推荐。本篇文章的重点是协同过滤和深度学习方法。

协同过滤是最常见的推荐方法，它基于用户的历史行为（如评分或购买记录）来预测用户对未见内容的兴趣。协同过滤可进一步分为基于用户的协同过滤和基于物品的协同过滤。而近年来，深度学习在推荐系统中的应用也越来越广泛，凭借强大的特征提取能力，深度学习能够大幅提升推荐效果。

### 2. 基于协同过滤的推荐系统

协同过滤是一种经典的推荐技术，它假设具有相似历史行为的用户会对相似的内容感兴趣。协同过滤分为基于用户的协同过滤和基于物品的协同过滤。

#### 2.1 用户协同过滤实现

用户协同过滤的核心思想是通过找到与目标用户行为相似的其他用户，来为目标用户推荐他们可能喜欢的物品。我们可以使用余弦相似度计算用户之间的相似性。

代码示例如下：

```
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# 假设我们有一个用户-物品评分矩阵
ratings_dict = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4, 4, 5],
    'item_id': [1, 2, 3, 2, 3, 1, 4, 2, 4, 3],
    'rating': [5, 3, 4, 4, 5, 3, 2, 4, 5, 4]
}
ratings_df = pd.DataFrame(ratings_dict)

# 将数据转换为用户-物品矩阵
user_item_matrix = ratings_df.pivot_table(index='user_id', columns='item_id', values='rating').fillna(0)

# 计算用户之间的余弦相似度
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

print("用户相似性矩阵：")
print(user_similarity_df)

# 为用户1推荐物品
user_id = 1
similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
recommendations = []
for similar_user in similar_users:
    user_ratings = user_item_matrix.loc[similar_user]
    recommendations.extend(user_ratings[user_ratings > 0].index.tolist())

# 去重并去掉用户已经评分的物品
recommendations = list(set(recommendations) - set(user_item_matrix.loc[user_id][user_item_matrix.loc[user_id] > 0].index))
print(f"为用户{user_id}推荐的物品：{recommendations}")
```

#### 2.2 物品协同过滤实现

物品协同过滤通过计算物品之间的相似度来进行推荐。对于一个目标物品，我们找到与之相似的物品，再根据这些相似物品来为用户进行推荐。

以下是基于物品的协同过滤代码示例：

```
# 计算物品之间的余弦相似度
item_similarity = cosine_similarity(user_item_matrix.T)
item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

print("物品相似性矩阵：")
print(item_similarity_df)

# 为用户1推荐物品
user_id = 1
user_ratings = user_item_matrix.loc[user_id]

# 找到用户评分过的物品，并推荐相似物品
recommendations = []
for item in user_ratings[user_ratings > 0].index:
    similar_items = item_similarity_df[item].sort_values(ascending=False).index[1:3]
    recommendations.extend(similar_items)

# 去重并去掉用户已经评分的物品
recommendations = list(set(recommendations) - set(user_ratings[user_ratings > 0].index))
print(f"为用户{user_id}推荐的物品：{recommendations}")
```

### 3. 使用矩阵分解提升推荐质量

矩阵分解是一种强大的工具，特别是用于隐因子模型。矩阵分解方法将用户-物品矩阵分解为两个低秩矩阵，分别表示用户和物品的特征，进而计算用户对物品的评分。

我们可以使用SVD（奇异值分解）来实现矩阵分解。

```
from sklearn.decomposition import TruncatedSVD

# 使用SVD进行矩阵分解
svd = TruncatedSVD(n_components=2)
user_matrix = svd.fit_transform(user_item_matrix)
item_matrix = svd.components_

# 预测用户对物品的评分
predicted_ratings = np.dot(user_matrix, item_matrix)
predicted_ratings_df = pd.DataFrame(predicted_ratings, index=user_item_matrix.index, columns=user_item_matrix.columns)

print("预测的评分矩阵：")
print(predicted_ratings_df)
```

矩阵分解方法在隐因子提取上有非常好的效果，通过找到用户和物品之间的潜在联系，可以大幅提升推荐的准确性。

### 4. 深度学习推荐系统

随着深度学习的发展，推荐系统也逐渐引入了神经网络模型，特别是基于嵌入的深度学习方法。通过使用神经网络，我们可以捕捉用户和物品的复杂非线性关系，从而进一步提升推荐系统的表现。

#### 4.1 神经网络嵌入实现

神经网络嵌入是一种将离散特征（如用户ID和物品ID）映射到连续空间中的技术。这种方法通过使用嵌入层将用户和物品表示为低维的密集向量，再利用神经网络学习它们之间的交互关系。

我们将使用TensorFlow实现一个简单的深度学习推荐系统。

##### 4.1.1 数据准备

首先，我们需要将用户和物品ID转换为连续的整数值，并准备训练数据。

```
import tensorflow as tf
from sklearn.model_selection import train_test_split

# 将用户和物品ID转换为连续整数
user_ids = ratings_df['user_id'].unique()
item_ids = ratings_df['item_id'].unique()
user_id_map = {user_id: idx for idx, user_id in enumerate(user_ids)}
item_id_map = {item_id: idx for idx, item_id in enumerate(item_ids)}
ratings_df['user_id'] = ratings_df['user_id'].map(user_id_map)
ratings_df['item_id'] = ratings_df['item_id'].map(item_id_map)

# 划分训练集和测试集
train_data, test_data = train_test_split(ratings_df, test_size=0.2, random_state=42)
```

##### 4.1.2 构建深度学习模型

我们使用TensorFlow构建一个包含嵌入层的简单神经网络，用于预测用户对物品的评分。

```
class RecommenderModel(tf.keras.Model):
    def __init__(self, num_users, num_items, embedding_dim=32):
        super(RecommenderModel, self).__init__()
        self.user_embedding = tf.keras.layers.Embedding(num_users, embedding_dim)
        self.item_embedding = tf.keras.layers.Embedding(num_items, embedding_dim)
        self.dense_1 = tf.keras.layers.Dense(64, activation='relu')
        self.dense_2 = tf.keras.layers.Dense(32, activation='relu')
        self.output_layer = tf.keras.layers.Dense(1, activation='linear')

    def call(self, inputs):
        user_input, item_input = inputs
        user_vector = self.user_embedding(user_input)
        item_vector = self.item_embedding(item_input)
        x = tf.concat([user_vector, item_vector], axis=-1)
        x = self.dense_1(x)
        x = self.dense_2(x)
        output = self.output_layer(x)
        return output

num_users = len(user_ids)
num_items = len(item_ids)
model = RecommenderModel(num_users, num_items)

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
```

##### 4.1.3 模型训练

接下来，我们将模型的输入与标签分离，并训练模型。

```
# 准备输入和标签
def prepare_data(data):
    user_inputs = data['user_id'].values
    item_inputs = data['item_id'].values
    labels = data['rating'].values
    return (user_inputs, item_inputs), labels

train_inputs, train_labels = prepare_data(train_data)
test_inputs, test_labels = prepare_data(test_data)

# 训练模型
history = model.fit(
    train_inputs,
    train_labels,
    epochs=10,
    batch_size=16,
    validation_data=(test_inputs, test_labels)
)
```

##### 4.1.4 模型评估

训练结束后，我们可以评估模型的性能，并使用模型进行推荐。

```
# 模型评估
loss, mae = model.evaluate(test_inputs, test_labels)
print(f"测试集上的均方误差 (MSE)：{loss}")
print(f"测试集上的平均绝对误差 (MAE)：{mae}")

# 为用户1推荐物品
user_id = user_id_map[1]
item_candidates = np.array([item_id_map[item] for item in item_ids])
user_inputs = np.array([user_id] * len(item_candidates))
predictions = model.predict((user_inputs, item_candidates)).flatten()

# 推荐得分最高的物品
recommended_items = item_candidates[np.argsort(predictions)[-5:]]
recommended_items = [item for item, idx in item_id_map.items() if idx in recommended_items]
print(f"为用户1推荐的物品：{recommended_items}")
```

### 5. 总结

本文详细介绍了如何使用Python构建推荐系统，从传统的基于协同过滤的方法到基于深度学习的嵌入模型。通过协同过滤，我们能够较为简单地实现推荐系统，但推荐效...