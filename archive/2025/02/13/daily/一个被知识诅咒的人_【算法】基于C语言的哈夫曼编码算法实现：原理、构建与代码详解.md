---
title: 【算法】基于C语言的哈夫曼编码算法实现：原理、构建与代码详解
url: https://blog.csdn.net/nokiaguy/article/details/145583964
source: 一个被知识诅咒的人
date: 2025-02-13
fetch_date: 2025-10-06T20:34:07.085459
---

# 【算法】基于C语言的哈夫曼编码算法实现：原理、构建与代码详解

# 【算法】基于C语言的哈夫曼编码算法实现：原理、构建与代码详解

原创
[![](https://csdnimg.cn/release/blogv2/dist/pc/img/identityVipNew.png)](https://mall.csdn.net/vip)
于 2025-02-12 08:50:03 发布
·
1.3k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

20

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

24
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#算法](https://so.csdn.net/so/search/s.do?q=%E7%AE%97%E6%B3%95&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#c语言](https://so.csdn.net/so/search/s.do?q=c%E8%AF%AD%E8%A8%80&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#机器学习](https://so.csdn.net/so/search/s.do?q=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

哈夫曼编码是一种高效的数据压缩算法，广泛应用于文本、图像和音频等数据的压缩。本文将深入讲解哈夫曼编码的工作原理，并使用C语言详细实现哈夫曼编码和解码算法。文章将从信息论的基础知识出发，逐步解释哈夫曼树的构建过程，并结合C语言代码，详细介绍如何通过树形结构来实现最优前缀编码，最终达到数据压缩的目的。

**关键词**：哈夫曼编码，数据压缩，C语言，哈夫曼树，前缀编码

**1. 引言**

在信息爆炸的时代，数据压缩技术变得至关重要。数据压缩不仅可以节省存储空间，还能加快数据传输速度，提高网络效率。哈夫曼编码作为一种经典的无损数据压缩算法，以其高效性和简洁性而备受青睐。

哈夫曼编码的核心思想是基于字符出现频率构建最优前缀编码。相较于传统的固定长度编码（如ASCII编码），哈夫曼编码为高频字符分配较短的编码，为低频字符分配较长的编码，从而有效缩短数据的平均编码长度，实现数据压缩。

本文将深入探讨哈夫曼编码的原理，并提供一个基于C语言的完整实现方案，帮助读者理解和掌握这一重要的压缩算法。

**2. 哈夫曼编码的理论基础**

要理解哈夫曼编码，首先需要了解一些信息论的基础概念：

**2.1 信息熵**

信息熵是信息论中用于度量信息不确定性的概念。在信息编码中，信息熵可以理解为编码数据所需要的平均比特数。对于一个离散随机变量 X，其概率分布为 P(X)，则信息熵 H(X) 定义为：

H(X) = - Σ P(x) \* log₂(P(x))

其中，Σ 表示对所有可能的 x 值求和，P(x) 是 x 出现的概率，log₂ 表示以 2 为底的对数。信息熵的单位是比特 (bits)。

信息熵越高，表示信息的不确定性越大，编码所需的平均比特数也越多；反之，信息熵越低，表示信息的不确定性越小，编码所需的平均比特数也越少。

**2.2 前缀编码**

前缀编码是一种重要的变长编码方式。它的特点是，任何一个编码都不是其他任何编码的前缀。这种特性保证了解码的唯一性，即在解码过程中，一旦读取到一个完整的编码，就可以立即确定其对应的字符，而无需继续读取后续的比特。

例如，假设有字符集 {A, B, C, D}，以下是一些编码方案：

* **方案一（非前缀编码）**：

  + A: 0
  + B: 01
  + C: 10
  + D: 1

  这个方案不是前缀编码，因为 ‘0’ 是 ‘01’ 的前缀，‘1’ 是 ‘10’ 的前缀。解码时可能会出现歧义，例如，编码 ‘010’ 可以被解码为 ‘BA’ 或 ‘AC’。
* **方案二（前缀编码）**：

  + A: 0
  + B: 10
  + C: 110
  + D: 111

  这个方案是前缀编码。解码时，例如编码 ‘010110’，可以被唯一地解码为 ‘ABC’。

哈夫曼编码是一种最优的前缀编码，它能够在所有前缀编码中，实现平均编码长度最小化。

**3. 哈夫曼编码的工作原理**

哈夫曼编码的核心思想是贪心算法，其构建过程主要分为以下几个步骤：

**3.1 统计字符频率**

首先，需要统计待编码数据中每个字符出现的频率。频率越高，字符的重要性越高，应该分配更短的编码。

**3.2 构建哈夫曼树**

哈夫曼树（Huffman Tree），也称为最优二叉树，是构建哈夫曼编码的关键数据结构。构建哈夫曼树的过程如下：

1. **初始化**：将每个字符及其频率作为一个独立的节点，构成森林（即一组独立的树）。每个节点都作为根节点，且权重为字符的频率。
2. **合并**：从森林中选取两个权重最小的节点，作为左右子节点构建一个新的父节点。新父节点的权重为两个子节点的权重之和。将新父节点加入森林，并从森林中移除这两个子节点。
3. **重复**：重复步骤 2，直到森林中只剩下一个节点，这个节点就是哈夫曼树的根节点。

在构建哈夫曼树的过程中，每次都选择频率最小的两个节点进行合并，保证了频率高的字符最终会更靠近树的根节点，从而获得更短的编码。

**3.3 生成哈夫曼编码**

从哈夫曼树的根节点出发，为每个分支分配编码：通常，左分支分配 ‘0’，右分支分配 ‘1’。从根节点到每个叶子节点的路径上的编码序列，就是该叶子节点所代表字符的哈夫曼编码。

由于哈夫曼树的构建过程保证了前缀特性，因此生成的哈夫曼编码一定是前缀编码。

**4. 哈夫曼树的C语言实现**

为了在C语言中实现哈夫曼编码，我们需要定义哈夫曼树的节点结构，以及构建哈夫曼树和生成哈夫曼编码的函数。

**4.1 节点结构定义**

```
typedef struct HuffmanNode {

    int frequency;      // 字符频率
    char data;         // 字符数据 (叶子节点有效)
    struct HuffmanNode *left;  // 左子节点
    struct HuffmanNode *right; // 右子节点
} HuffmanNode;
```

这个结构体 `HuffmanNode` 用于表示哈夫曼树的节点。`frequency` 存储字符的频率，`data` 存储字符数据（仅叶子节点有效），`left` 和 `right` 分别指向左右子节点。

**4.2 频率统计函数**

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHARS 256 // 假设字符集为 ASCII

int* countFrequencies(const char *text) {

    int *frequencies = (int*)calloc(MAX_CHARS, sizeof(int)); // 初始化频率数组为 0
    if (frequencies == NULL) {

        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; text[i] != '\0'; i++) {

        frequencies[(unsigned char)text[i]]++; // 统计字符频率
    }
    return frequencies;
}
```

`countFrequencies` 函数用于统计输入文本 `text` 中每个字符的频率。它使用一个大小为 `MAX_CHARS` 的整型数组 `frequencies` 来存储频率，数组索引对应字符的 ASCII 值。

**4.3 创建叶子节点函数**

```
HuffmanNode* createLeafNode(char data, int frequency) {

    HuffmanNode* node = (HuffmanNode*)malloc(sizeof(HuffmanNode));
    if (node == NULL) {

        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    node->data = data;
    node->frequency = frequency;
    node->left = node->right = NULL; // 叶子节点左右子节点为空
    return node;
}
```

`createLeafNode` 函数用于创建哈夫曼树的叶子节点，即表示字符的节点。它接收字符 `data` 和频率 `frequency` 作为参数，并返回新创建的叶子节点指针。

**4.4 构建哈夫曼树函数**

```
#include <limits.h> // 包含 INT_MAX

// 辅助函数：找到频率最小的节点索引
int findMinFrequencyNode(HuffmanNode** nodes, int n, int excludedIndex1, int excludedIndex2) {

    int minFrequency = INT_MAX;
    int minIndex = -1;
    for (int i = 0; i < n; i++) {

        if (i != excludedIndex1 && i != excludedIndex2 && nodes[i] != NULL && nodes[i]->frequency < minFrequency) {

            minFrequency = nodes[
```

![](https://csdnimg.cn/release/blogv2/dist/pc/img/lock.png)最低0.47元/天 解锁文章

200万优质内容无限畅学

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

  20

  点赞
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/unlike.png)

  踩
* ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect-active.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/toolbar/collect.png)
  ![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png)

  24

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
2559

[随着人工智能（AI）技术的迅猛发展，尤其是生成式AI（AIGC），劳动力市场正经历前所未有的变革。从内容创作到自动化生产线，几乎每个行业都在经历一场技术的洗礼。然而，这场革命并不是全然的光明，它带来了深刻的社会变动，也引发了广泛的担忧和不安。我们不得不面对一个核心问题：AIGC将如何影响未来的工作？会让人类的大多数工作消失，还是会创造出全新的职业机会？](https://unitymarvel.blog.csdn.net/article/details/145234235)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【Python图形图像】《Python OpenCV从菜鸟到高手》——零基础进阶，开启图像处理与计算机视觉的大门！](https://unitymarvel.blog.csdn.net/article/details/143574491)

11-07
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
2251

[《Python OpenCV从菜鸟到高手》是一本深入探讨Python与OpenCV技术的图像处理教程。从Python的基础知识到OpenCV的强大功能，这本书带领读者逐步掌握计算机视觉的核心技术。Python因其简洁和强大的库生态被广泛应用于数据分析、人工智能等领域，而OpenCV则是图像处理与计算机视觉的利器。本书通过循序渐进的方式，让读者从零基础到掌握高级图像处理技能，帮助你实现从初学者到高手的跃升。](https://unitymarvel.blog.csdn.net/article/details/143574491)

![](https://csdnimg.cn/release/blogv2/dist/components/img/blogType.png)
博客
[【奇妙的Python】解锁Python编程的无限可能：《奇妙的Python》带你漫游代码世界](https://unitymarvel.blog.csdn.net/article/details/141889588)

09-04
![](https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png)
3140

[《奇妙的Python——神奇代码漫游之旅》是一本面向实际应用的Python编程指南，涵盖文件操作、GUI设计、多媒体处理、自动化办公、加密解密等多个领域。由华为HDE专...