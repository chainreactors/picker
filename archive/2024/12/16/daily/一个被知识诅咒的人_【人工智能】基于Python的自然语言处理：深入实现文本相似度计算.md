---
title: 【人工智能】基于Python的自然语言处理：深入实现文本相似度计算
url: https://blog.csdn.net/nokiaguy/article/details/144480576
source: 一个被知识诅咒的人
date: 2024-12-16
fetch_date: 2025-10-06T19:35:23.320869
---

# 【人工智能】基于Python的自然语言处理：深入实现文本相似度计算

# 【人工智能】基于Python的自然语言处理：深入实现文本相似度计算

原创
已于 2025-01-09 16:53:29 修改
·
1.6k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

15

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
[#自然语言处理](https://so.csdn.net/so/search/s.do?q=%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2024-12-15 08:47:42 首次发布

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

Python杂谈
同时被 2 个专栏收录![](https://csdnimg.cn/release/blogv2/dist/pc/img/newArrowDown1White.png)](https://blog.csdn.net/nokiaguy/category_12800257.html "Python杂谈")

390 篇文章

订阅专栏

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756780.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

人工智能](https://blog.csdn.net/nokiaguy/category_1260139.html "人工智能")

195 篇文章

订阅专栏

文本相似度计算是自然语言处理（NLP）中的核心任务，广泛应用于搜索引擎、推荐系统、问答系统等领域。本文全面解析文本相似度计算的核心技术，使用Python中的spaCy和sentence-transformers库实现多种方法，包括基于词向量的余弦相似度、预训练语言模型的句向量方法等。我们将从理论讲解到代码实现，涵盖预处理、特征提取、相似度计算以及性能对比。通过代码实例和中文注释，读者将掌握构建文本相似度计算系统的核心技能，并能根据应用场景选择合适的技术方案。

---

### 引言

文本相似度计算是衡量两段文本之间语义相似程度的过程。它是搜索引擎的核心技术之一，例如根据用户输入的查询推荐最相关的文档。常用的文本相似度计算方法包括：

1. **基于统计的方法**：如词频（TF-IDF）和余弦相似度。
2. **基于词嵌入的方法**：如Word2Vec或GloVe。
3. **基于预训练语言模型的方法**：如BERT、RoBERTa。

本文将使用spaCy和sentence-transformers分别实现基于词向量和句向量的文本相似度计算，并进行性能对比。

---

### 文本相似度计算的理论基础

#### 1. 余弦相似度

余弦相似度衡量两个向量之间的夹角余弦值，用于评估文本的相似性。公式为：

Cosine Similarity
=
cos
⁡
(
θ
)
=
A
⋅
B
∥
A
∥
∥
B
∥
\text{Cosine Similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}
Cosine Similarity=cos(θ)=∥A∥∥B∥A⋅B​
 其中，(\mathbf{A}) 和 (\mathbf{B}) 是文本的向量表示。

#### 2. 词向量与句向量

* **词向量**：通过Word2Vec、GloVe等方法将单词映射为高维空间的稠密向量。
* **句向量**：将整段文本映射为固定维度的向量，常用的技术包括BERT和sentence-transformers。

---

### 使用spaCy计算基于词向量的相似度

#### 安装和初始化spaCy

首先确保已安装spaCy及其语言模型。

```
pip install spacy
python -m spacy download en_core_web_md
```

```
import spacy

# 加载中型语言模型
nlp = spacy.load("en_core_web_md")
```

#### 基本用法与词向量相似度

我们可以直接利用spaCy的内置功能计算两个句子的相似度。

```
# 示例句子
doc1 = nlp("I love programming.")
doc2 = nlp("Coding is my passion.")

# 直接计算句子相似度
similarity = doc1.similarity(doc2)
print(f"文本相似度: {similarity:.4f}")
```

#### 提取词向量计算余弦相似度

spaCy的 `doc.vector` 提供整个文本的平均向量。

```
import numpy as np

# 自定义余弦相似度函数
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# 获取文本向量
vec1 = doc1.vector
vec2 = doc2.vector

# 计算余弦相似度
similarity = cosine_similarity(vec1, vec2)
print(f"余弦相似度: {similarity:.4f}")
```

#### 比较多个文本的相似度

计算一组文本之间的相似度矩阵。

```
# 示例文本
texts = ["I love programming.", "Coding is my passion.", "I enjoy hiking.", "Nature is beautiful."]

# 提取向量
vectors = [nlp(text).vector for text in texts]

# 计算相似度矩阵
similarity_matrix = np.zeros((len(texts), len(texts)))
for i in range(len(texts)):
    for j in range(len(texts)):
        similarity_matrix[i, j] = cosine_similarity(vectors[i], vectors[j])

# 打印相似度矩阵
print("相似度矩阵:")
print(similarity_matrix)
```

---

### 使用sentence-transformers实现基于句向量的相似度

#### 安装sentence-transformers

```
pip install sentence-transformers
```

#### 加载预训练模型

sentence-transformers支持多种预训练模型，如 `all-MiniLM-L6-v2`，适合高效计算句向量。

```
from sentence_transformers import SentenceTransformer

# 加载预训练模型
model = SentenceTransformer('all-MiniLM-L6-v2')
```

#### 计算句向量并计算相似度

```
# 示例文本
texts = ["I love programming.", "Coding is my passion.", "I enjoy hiking.", "Nature is beautiful."]

# 提取句向量
sentence_embeddings = model.encode(texts)

# 自定义余弦相似度函数
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# 计算相似度矩阵
similarity_matrix = np.zeros((len(texts), len(texts)))
for i in range(len(texts)):
    for j in range(len(texts)):
        similarity_matrix[i, j] = cosine_similarity(sentence_embeddings[i], sentence_embeddings[j])

# 打印相似度矩阵
print("基于句向量的相似度矩阵:")
print(similarity_matrix)
```

---

### 案例：电影描述文本相似度分析

#### 数据准备

使用IMDb电影描述数据，计算描述之间的相似度，推荐与输入电影最相似的描述。

```
# 示例电影描述
movies = [
    "A young wizard attending a school of witchcraft.",
    "A group of friends embark on an epic journey to destroy a powerful ring.",
    "A team of superheroes come together to save the world.",
    "A detective investigates a mysterious murder in a small town."
]

# 提取句向量
movie_embeddings = model.encode(movies)

# 输入新描述
new_description = "A boy discovers he is a wizard and attends a magical school."
new_embedding = model.encode([new_description])[0]

# 计算相似度
similarities = [cosine_similarity(new_embedding, movie_embedding) for movie_embedding in movie_embeddings]

# 输出最相似的电影
most_similar_idx = np.argmax(similarities)
print(f"输入描述: {new_description}")
print(f"最相似的电影描述: {movies[most_similar_idx]}")
```

---

### 性能对比

我们对spaCy和sentence-transformers进行以下对比：

1. **速度**：sentence-transformers略慢，但精度更高。
2. **语义能力**：基于预训练语言模型的sentence-transformers能够捕捉更深层次的语义关系。

#### 测试两种方法的性能

```
import time

# 测试spaCy
start = time.time()
vectors = [nlp(text).vector for text in texts]
end = time.time()
print(f"spaCy时间: {end - start:.4f}秒")

# 测试sentence-transformers
start = time.time()
sentence_embeddings = model.encode(texts)
end = time.time()
print(f"sentence-transformers时间: {end - start:.4f}秒")
```

---

### 总结

文本相似度计算是NLP中重要且基础的任务。本文结合spaCy和sentence-transformers详细解析了文本预处理、特征提取和相似度计算方法。spaCy适用于快速部署和轻量级任务，而sentence-transformers更适合需要高语义理解能力的复杂任务。希望本文为您在构建文本相似度计算系统中提供了实用参考。

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

  15

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  22

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
[AIGC撕裂劳动力市场：技术狂潮下，人类将走向乌托邦还是深渊？](ht...