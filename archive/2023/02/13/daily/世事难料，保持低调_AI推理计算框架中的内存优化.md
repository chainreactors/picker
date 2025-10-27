---
title: AI推理计算框架中的内存优化
url: https://blog.csdn.net/ariesjzj/article/details/128979978
source: 世事难料，保持低调
date: 2023-02-13
fetch_date: 2025-10-04T06:27:18.977926
---

# AI推理计算框架中的内存优化

# AI推理计算框架中的内存优化

最新推荐文章于 2025-04-18 10:15:43 发布

原创
最新推荐文章于 2025-04-18 10:15:43 发布
·
4.2k 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

7

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

17
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#深度学习](https://so.csdn.net/so/search/s.do?q=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#内存优化](https://so.csdn.net/so/search/s.do?q=%E5%86%85%E5%AD%98%E4%BC%98%E5%8C%96&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#TensorFlow Lite](https://so.csdn.net/so/search/s.do?q=TensorFlow+Lite&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)
[#人工智能](https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756916.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

AI
专栏收录该内容](https://blog.csdn.net/ariesjzj/category_1243833.html "AI")

43 篇文章

订阅专栏

## 背景

内存管理是AI计算中非常重要的一部分。我们希望模型计算时占用内存尽可能小，这样我们训练或推理时就可以用更大的batch size使其尽快收敛，或者提高吞吐率。又或者让我们可以使用参数更多、或更复杂的模型从而达到更好的准确率。由于现代深度学习模型大多在GPU上运行，而GPU的显存相比CPU小得多，因此我们这里主要关注的是GPU memory。

首先看下我们需要重点关注哪些GPU memory。对于模型在计算中需要用到的GPU memory，论文《Estimating GPU Memory Consumption of Deep Learning Models》做了比较具体的总结。对推理计算而言，主要有这么几类：

* **权重参数（Weight Parameter）**：这个不用多说，模型中的参数。
* **中间张量（Intermediate Tensor）**：网络中每层的输出与输入张量。
* **其它**：计算中需要的临时内存（如kernel中使用的一些memory，cuDNN的workspace），还有一些常驻的内存（如CUDA context）。

其中第三类本身占的空间不大，也比较难优化。第一类减少权重内存占用的话可以通过一些模型压缩方法，如量化，剪枝。之前写过一些相关文章如[《闲话模型压缩之量化（Quantization）篇》](https://blog.csdn.net/jinzhuojun/article/details/106955059?spm=1001.2014.3001.5501)和[《闲话模型压缩之网络剪枝（Network Pruning）篇》](https://blog.csdn.net/jinzhuojun/article/details/100621397)，有兴趣可以参考。相比之下，第二类，即中间张量的优化空间更大，因此很多业界的工作也是针对它来优化。优化的思路有很多，比如：

* **内存重用（Memory reuse）**：由于有些中间张量的生命周期间互不重叠，因此可以reuse。MegEngine, IREE, TensorRT等框架都做了memory usage相关的优化。
* **重计算（Recomputation）**：该技术主要用于训练中。它将模型中的一些节点作为checkpoint，其它节点的输出可丢弃，当在计算梯度时需要时通过最近的checkpoint重新计算生成。因此被称为checkpointing技术。该问题也被称为tensor rematerialization优化问题。相关论文如适用于静态网络的offline方法《Training Deep Nets with Sublinear Memory Cost》，适用于动态网络的online方法《Dynamic Tensor Rematerialization》，建模为MILP进行求解的《Checkmate: Breaking the Memory Wall with Optimal Tensor Rematerialization》等。
* **交换（Swap）**：基本思想是将显存中的数据交换到CPU上，相当于把GPU memory当成CPU memory的cache。一些塞不进GPU显存的层，如DLRM模型的embedding层可能会用到这种技术。相关的论文如《Supporting Massive DLRM Inference Through Software Defined Memory》，《vDNN: Virtualized Deep Neural Networks for Scalable, Memory-Efficient Neural Network Design》等。
* **压缩（Compression）**：将数据进行压缩，如《Gist: Efficient Data Encoding for Deep Neural Network Training》，根据特定层输出特点对层的输出，即feature map数据进行编码压缩。
* …

后面几种都会一定程度上牺牲性能，这里我们主要关注第一种。它在对延迟关注的推理场景用得尤其多一些。比如TensorFlow Lite利用该技术可以显著减少内存占用（详见https://blog.tensorflow.org/2020/10/optimizing-tensorflow-lite-runtime.html）。

对于网络前面层的输出，到计算后面的层时可能已经不再使用了。换句话说，对于中间层的输出张量，它们的生命周期可能是没有重叠的，对于它们便可以进行重用。下面是最简单情况下的示意图：
 ![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4e87371498bb565bdb7c1be496ec8fb9.png#pic_center)

但实际中的情况远没有这么简单。网络中不总是线性结构，另外张量的大小可能各不相同，给重用带来困难。要得到其最优的分配策略，是一个NP-complete问题。因此实际当中，我们可以倾向于一些heuristic方法，这样可以在合理时间内得到一个近似最优解。

那如何优化呢？在不少地方，如TensorRT会提到基于register allocation的思想。任何一本编译器的教材中都会介绍register allocation，在此不展开。大体会先通过liveness analysis得到变量的live range，然后根据它生成inference graph，转为着色问题来解。业界也有采用这种方法的做法，如《Memory Allocation for Neural Networks using Graph Coloring》。但是，memory planning与register allocation所面临的问题还是有所区别的，比如：

* **大小不确定**：Register的大小基本是相同，或者说是差不多的，而memory的大小可能差异很大，重用一块过大或过小的memory会产生问题。
* **拷贝成本高**：Register拷贝一下还好，但memory拷贝开销比较大，尤其是大块的memory。因此理想情况下我们希望不要拷贝。
* **Fallback机制**：Register实在分配不了会产生spill，即放到memory中。虽然memory要不不够理论上也能往更下一层存储器上搬，业界也有这方面的研究，但很多情况下因为时延等原因不会这么做。

另外，从静态/动态角度，内存的管理方式大体有动态分配与静态规划两种：

* **动态分配（Dynamic Memory Allocation）**：内存分配在运行时进行。由于从系统中分配的开销较大，通常维护一个memory pool。需要时从中分配，不再需要时放回到pool。如TensorFlow中的BFC allocator。
* **静态规划（Static Memory Planning）**：内存分配在运行前进行，常见于基于编译器的计算框架。通过规划进一步减少内存使用，减少OOM带来的不确定性，同时最少化运行时内存管理的开销。如MXNet与MegEngine/MegCC中的static memory planning。

光看概念有些抽象，下面就以一个实例 - TensorFlow Lite（TF Lite）中的内存优化来看看具体的实现。其实在论文《Efficient Memory Management for Deep Neural Net Inference》与《On-Device Neural Net Inference with Mobile GPUs》中对其原理已经介绍得比较清楚了。下面主要是结合代码理解下它的实现。

## 代码走读

### 基础数据结构

先来看几个关键数据结构。它们定义在`types.h`文件中。结构体`TensorUsageRecord`即论文中提到的Tensor usage record，用于记录张量的使用记录。它主要包含三个信息：tensor size, 以及第一个与最后一个使用它的task。代表这两个task的成员`first_task`与`last_task`即它的生命周期。

```
using UsageGraph = std::vector<std::vector<size_t>>;

template <typename TensorSizeT>
struct TensorUsageRecord {
  TensorSizeT tensor_size;
  TaskId first_task;
  TaskId last_task;
  ...
};
```

注意它是个模板类，有针对`size_t`，`uint2`，`uint3`与`BHWC`的特化（实现在`memory_management.c`文件）。

结构体`ObjectsAssignment`与`OffsetsAssignment`都用于存放分配结果。

```
// Information about assignment of tensors to shared objects
template <typename TensorSizeT>
struct ObjectsAssignment {
  // shared_object_ids_[i] is ID of shared object, that tensor i will be using.
  std::vector<size_t> object_ids;
  // shared_object_sizes_[i] is a size of shared object with ID equal to i.
  std::vector<TensorSizeT> object_sizes;
};

// Information about assignment of tensors to offsets for the case, when all of
// them are going to be allocated in one continuous memory block.
struct OffsetsAssignment {
  std::vector<size_t> offsets;
  size_t total_size;
};
```

它们对应后面会提到的两种分配方式。前者用于shared object（指可以用于多个tensor的内存块）分配，后者用于从大块连续内存中分配子内存区域。

为了解它的使用，可以参考它的测试用例`memory_management_test.cc`。比较典型的有几个case：`OneRecord`，`ChainRecords`，`ComplexRecords`，分别对于只有一个节点，链式（即线性）计算图，和复杂计算图。
 ![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/0bddceb1e7ff1862346d0b2e172e02a4.png#pic_center)

以`ChainRecords`这个case为例：

```
TEST(Model, ChainRecords) {
  std::vector<TensorUsageRecord<size_t>> usage_records{
      {/*size=*/16, /*first=*/0, /*last=*/1},
      {/*size=*/8, /*first=*/1, /*last=*/2},
      {/*size=*/64, /*first=*/2, /*last=*/3},
      {/*size=*/32, /*first=*/3, /*last=*/4},
      {/*size=*/8, /*first=*/4, /*last=*/5},
  };

  ObjectsAssignment<size_t> assignment;
  ASSERT_TRUE(
      AssignObjectsToTensors(usage_records, MemoryStrategy::NAIVE, &assignment)
          .ok());
  EXPECT_THAT(assignment.object_ids, ElementsAre(0, 1, 2, 3, 4));
  EXPECT_THAT(assignment.object_sizes, ElementsAre(16, 8, 64, 32, 8));
  ...
```

可以看到，其中最核心的是`AssignObjectsToTensors()`函数。该函数基于由`TensorUsageRecord`数组表示的张量使用记录（按拓扑序排列），根据指定的分配策略（由`MemoryStrategy`表示），计算得到分配结果（由`ObjectsAssignment`对象表示）。

### Object分配方式

注意`AssignObjectsToTensors()`是个模板函数，根据`TensorUsageRecord`的类型不同有多种实现。以最简单的`TensorUsageRecord<size>`的情况（即tensor的大小以一个`size_t`类型表示）为例，相关代码如下：

```
template <>
absl::Status AssignObjectsToTensors(
    const std::vector<TensorUsageRecord<size_t>>& usage_records,
    MemoryStrategy strategy, ObjectsAssignment<size_t>* assignment,
    const UsageGraph* reallocation_graph) {
  switch (strategy) {
    case MemoryStrategy::NAIVE:
      return NaiveAssignment(usage_records, assignment);
    case MemoryStrategy::EQUALITY:
      return EqualityAssignmentWithHash(usage_records, assignment);
    case MemoryStrategy::GREEDY_IN_ORDER:
      return GreedyInOrderAssignment(usage_records, assignment,
                                     reallocation_graph);
    case MemoryStrategy::GREEDY_BY_BREADTH:
      return GreedyByBreadthAssignment(usage_records, assignment);
    case MemoryStrategy::GREEDY_BY_SIZE:
      return GreedyBySizeDistPriorityAssignment(usage_records, assignment);
    case MemoryStrategy::GREEDY_BEST:
      return BestGreedy(usage_records, assignment);
    ca...