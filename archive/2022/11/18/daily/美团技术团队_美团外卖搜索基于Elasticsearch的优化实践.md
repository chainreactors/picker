---
title: 美团外卖搜索基于Elasticsearch的优化实践
url: https://mp.weixin.qq.com/s?__biz=MjM5NjQ5MTI5OA==&mid=2651772026&idx=1&sn=6ff4cb024bb416c46d5d2850a6ae77d1&chksm=bd120d378a6584217f1838c0f951204023e5c32b0ad413a731078e2f11f8f0009b39c3dec4ea&scene=58&subscene=0#rd
source: 美团技术团队
date: 2022-11-18
fetch_date: 2025-10-03T23:07:39.533375
---

# 美团外卖搜索基于Elasticsearch的优化实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUUbRV1cVqTqicZlOle4Eia62UFKAgjpZ9mTZYzH4pcsNpfJdVLsFZzIK1hezzThyyXll0asTDg2Sxg/0?wx_fmt=jpeg)

# 美团外卖搜索基于Elasticsearch的优化实践

原创

泽钰 张聪 晓鹏

美团技术团队

![](https://mmbiz.qpic.cn/mmbiz_png/hEx03cFgUsU2zk0q52HtKQjubeUEyZHBVHPgeBXgTUj0ib1Kwfosl82xO1Aw7x6gccLuuYs1dbxI7REI7OcjbGw/640?wx_fmt=png)

**总第544****篇**

**2022年 第061篇**

![](https://mmbiz.qpic.cn/mmbiz_png/hEx03cFgUsU2zk0q52HtKQjubeUEyZHBic5ADGrKxgSd0tibyMiasOHXjb46qFBw7PTfuWAxXzWq32lDkL05icwkMg/640?wx_fmt=png "undefined")

美团外卖搜索工程团队在Elasticsearch的优化实践中，基于Location-Based Service（LBS）业务场景对Elasticsearch的查询性能进行优化。该优化基于Run-Length Encoding（RLE）设计了一款高效的倒排索引结构，使检索耗时（TP99）降低了84%。本文从问题分析、技术选型、优化方案等方面进行阐述，并给出最终灰度验证的结论。

* 1. 前言
* 2. 背景
* 3. 挑战及问题

+ 3.1 倒排链查询流程
+ 3.2 倒排链合并流程

* 4. 技术探索与实践

+ 4.1 倒排链查询优化
+ 4.2 倒排链合并
+ 4.3 基于 RLE 的倒排格式设计
+ 4.4 功能集成

* 5. 性能收益
* 6. 总结与展望
* 7. 作者简介
* 8. 参考文献

## 1. 前言

最近十年，Elasticsearch 已经成为了最受欢迎的开源检索引擎，其作为离线数仓、近线检索、B端检索的经典基建，已沉淀了大量的实践案例及优化总结。然而在高并发、高可用、大数据量的 C 端场景，目前可参考的资料并不多。因此，我们希望通过分享在外卖搜索场景下的优化实践，能为大家提供 Elasticsearch 优化思路上的一些借鉴。

美团在外卖搜索业务场景中大规模地使用了 Elasticsearch 作为底层检索引擎。其在过去几年很好地支持了外卖每天十亿以上的检索流量。然而随着供给与数据量的急剧增长，业务检索耗时与 CPU 负载也随之上涨。通过分析我们发现，当前检索的性能热点主要集中在倒排链的检索与合并流程中。针对这个问题，我们基于 Run-length Encoding（RLE）[1] 技术设计实现了一套高效的倒排索引，使倒排链合并时间（TP99）降低了 96%。我们将这一索引能力开发成了一款通用插件集成到 Elasticsearch 中，使得 Elasticsearch 的检索链路时延（TP99）降低了 84%。

## 2. 背景

当前，外卖搜索业务检索引擎主要为 Elasticsearch，其业务特点是具有较强的 Location Based Service（LBS） 依赖，即用户所能点餐的商家，是由商家配送范围决定的。对于每一个商家的配送范围，大多采用多组电子围栏进行配送距离的圈定，一个商家存在多组电子围栏，并且随着业务的变化会动态选择不同的配送范围，电子围栏示意图如下：

![](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUUbRV1cVqTqicZlOle4Eia62LsicdBHKPHDaU80G8t05oZu5OZMibyaFyskj7CPUnAa0kTNtViafib2VnQ/640?wx_fmt=jpeg)

图1 电子围栏示意图

考虑到商家配送区域动态变更带来的问题，我们没有使用 Geo Polygon[2] 的方式进行检索，而是通过上游一组 R-tree 服务判定可配送的商家列表来进行外卖搜索。因此，LBS 场景下的一次商品检索，可以转化为如下的一次 Elasticsearch 搜索请求：

```
POST food/_search
{
   "query": {
      "bool": {
         "must":{
            "term": { "spu_name": { "value": "烤鸭"} }
           //...
         },
         "filter":{
           "terms": {
              "wm_poi_id": [1,3,18,27,28,29,...,37465542] // 上万
            }
         }
      }
   }
  //...
}
```

对于一个通用的检索引擎而言，Terms 检索非常高效，平均到每个 Term 检索不到 0.001 ms。因此在早期时，这一套架构和检索 DSL 可以很好地支持美团的搜索业务——耗时和资源开销尚在接受范围内。然而随着数据和供给的增长，一些供给丰富区域的附近可配送门店可以达到 20000~30000 家，这导致性能与资源问题逐渐凸显。这种万级别的 Terms 检索的性能与耗时已然无法忽略，仅仅这一句检索就需要 5~10 ms。

## 3. 挑战及问题

由于 Elasticsearch 在设计上针对海量的索引数据进行优化，在过去的 10 年间，逐步去除了内存支持索引的功能（例如 RAMDirectory 的删除）。为了能够实现超大规模候选集的检索，Elasticsearch/Lucene 对 Term 倒排链的查询流程设计了一套内存与磁盘共同处理的方案。

一次 Terms 检索的流程分为两步：分别检索单个 Term 的倒排链，多个 Term 的倒排链进行合并。

### 3.1 倒排链查询流程

1. 从内存中的 Term Index 中获取该 Term 所在的 Block 在磁盘上的位置。
2. 从磁盘中将该 Block 的 TermDictionary 读取进内存。
3. 对倒排链存储格式的进行 Decode，生成可用于合并的倒排链。

可以看到，这一查询流程非常复杂且耗时，且各个阶段的复杂度都不容忽视。所有的 Term 在索引中有序存储，通过二分查找找到目标 Term。这个有序的 Term 列表就是 TermDictionary ，二分查找 Term 的时间复杂度为 O(logN) ，其中 N 是 Term 的总数量 。Lucene 采用 Finite State Transducer[3]（FST）对 TermDictionary 进行编码构建 Term Index。FST 可对 Term 的公共前缀、公共后缀进行拆分保存，大大压缩了 TermDictionary 的体积，提高了内存效率，FST 的检索速度是 O(len(term))，其对于 M 个 Term 的检索复杂度为 O(M \* len(term))。

### 3.2 倒排链合并流程

在经过上述的查询，检索出所有目标 Term 的 Posting List 后，需要对这些 Posting List 求并集（OR 操作）。在 Lucene 的开源实现中，其采用 Bitset 作为倒排链合并的容器，然后遍历所有倒排链中的每一个文档，将其加入 DocIdSet 中。

伪代码如下：

```
Input:  termsEnum: 倒排表；termIterator：候选的term
Output: docIdSet : final docs set
for term in termIterator:
  if termsEnum.seekExact(term) != null:
     docs = read_disk()  // 磁盘读取
     docs = decode(docs) // 倒排链的decode流程
     for doc in docs:
        docIdSet.or(doc) //代码实现为DocIdSetBuilder.add。
end for
docIdSet.build()//合并，排序，最终生成DocIdSetBuilder，对应火焰图最后一段。
```

假设我们有 M 个 Term，每个 Term 对应倒排链的平均长度为 K，那么合并这 M 个倒排链的时间复杂度为：O(K \* M + log(K \* M))。可以看出倒排链合并的时间复杂度与 Terms 的数量 M 呈线性相关。在我们的场景下，假设一个商家平均有一千个商品，一次搜索请求需要对一万个商家进行检索，那么最终需要合并一千万个商品，即循环执行一千万次，导致这一问题被放大至无法被忽略的程度。

我们也针对当前的系统做了大量的调研及分析，通过美团内部的 JVM Profile 系统得到 CPU 的火焰图，可以看到这一流程在 CPU 热点图中的反映也是如此：无论是查询倒排链、还是读取、合并倒排链都相当消耗资源，并且可以预见的是，在供给越来越多的情况下，这三个阶段的耗时还会持续增长。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUUbRV1cVqTqicZlOle4Eia62qLr8ayEc3C6wCx9trAokDkgEp7wyp6ldfRWZcmQvmUNCqs05nFaTlw/640?wx_fmt=jpeg)

图2 profile 火焰图

可以明确，我们需要针对倒排链查询、倒排链合并这两个问题予以优化。

## 4. 技术探索与实践

### 4.1 倒排链查询优化

通常情况下，使用 FST 作为 Term 检索的数据结构，可以在内存开销和计算开销上取得一个很好的平衡，同时支持前缀检索、正则检索等多种多样的检索 Query，然而在我们的场景之下，FST 带来的计算开销无法被忽视。

考虑到在外卖搜索场景有以下几个特性：

* Term 的数据类型为 long 类型。
* 无范围检索，均为完全匹配。
* 无前缀匹配、模糊查找的需求，不需要使用前缀树相关的特性。
* 候选数量可控，每个商家的商品数量较多，即 Term 规模可预期，内存可以承载这个数量级的数据。

因此在我们的应用场景中使用空间换取时间是值得的。

对于 Term 查询的热点：可替换 FST 的实现以减少 CPU 开销，常见的查找数据结构中，哈希表有 O(1) 的查询复杂度，将 Term 查找转变为对哈希表的一次查询。

对于哈希表的选取，我们主要选择了常见的 HashMap 和 LongObjectHashMap。

我们主要对比了 FST、HashMap 和 LongObjectHashMap（哈希表的一种高性能实现）的空间和时间效率。

* **在内存占用上**：FST 的内存效率极佳。而 HashMap/LongObjectHashMap 都有明显的劣势；
* **在查询时间上**：FST 的查询复杂度在 O (len(term))，而 Hash/LongObjectHashMap 有着 O(1) 的查询性能；

> 注：检索类型虽然为 Long，但是我们将底层存储格式进行了调整，没有使用开源的 BKD Tree 实现，使用 FST 结构，仅与 FST 进行对比。BKD Tree 在大批量整数 terms 的场景下劣势更为明显。

我们使用十万个 <Long, Long> 的键值对来构造数据，对其空间及性能进行了对比，结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/hEx03cFgUsUUbRV1cVqTqicZlOle4Eia62ZBx7wKxEpUgQKcW37b8trmdhKZJ7m5LfrNNAu1uRcYc3ibLCApBWgEA/640?wx_fmt=png)

可以看到， 在内存占用上 FST 要远优于 LongObjectHashMap 和 HashMap。而在查询速度上 LongObjectHashMap 最优。

我们最终选择了 LongObjectHashMap 作为倒排链查询的数据结构。

### 4.2 倒排链合并

基于上述问题，我们需要解决两个明显的 CPU 热点问题：倒排链读取 & 倒排链合并。我们需要选择合适的数据结构缓存倒排链，不再执行磁盘 /page cache 的 IO。数据结构需要必须满足以下条件：

* 支持批量 Merge，减少倒排链 Merge 耗时。
* 内存占用少，需要处理千万数量级的倒排链。

在给出具体的解决方案之前，先介绍一下 Lucene 对于倒排合并的原生实现、RoaringBitMap、Index Sorting。

#### 4.2.1 原生实现

Lucene在不同场景上使用了不同的倒排格式，提高整体的效率（空间/时间），通过火焰图可以发现，在我们的场景上，TermInSetQuery 的倒排合并逻辑开销最大。

TermInSetQuery 的倒排链合并操作分为两个步骤：倒排链读取和合并。

1. 倒排链读取：

Lucene 倒排链压缩存储在索引文件中，倒排链读取需要实时解析，其对外暴露的 API 为迭代器结构。

**2. 倒排链合并：**

倒排链合并主要由 DocIdSetBuilder 合并生成倒排链，先使用稀疏结构存储 Doc ID，当  Doc ID 个数超过一定阈值时，升级到稠密结构（FixedBitSet）存储，实现方式如下（对应代码 IntArrayDocIdSet/BitDocIdSet）：

* 稀疏数据：存储采用 List<int[]> array 方式存储 Doc ID，最终经过 Merge 和排序形成一个有序数组 int[]，耗时主要集中在数组申请和排序。
* 稠密数据：基于 long[] 实现的 bitmap 结构（FixedBitSet），耗时主要集中在 FixedBitSet 的插入过程，由于倒排链需要实时 Decode 以及 FixedBitSet 的底层实现，无法实现批量 Merge，只能循环单个 Doc ID 插入，数据量大的情况下，耗时明显。

> 我们采用线上流量和数据压测发现该部分平均耗时约 7 ms。

#### 4.2.2 RoaringBitmap

当前 Elasticsearch 选择 RoaringBitMap 做为 Query Cache 的底层数据结构缓存倒排链，加快查询速率。

RoaringBitmap 是一种压缩的位图，相较于常规的压缩位图能提供更好的压缩，在稀疏数据的场景下空间更有优势。以存放 Integer 为例，Roaring Bitmap 会对存入的数据进行分桶，每个桶都有自己对应的 Container。在存入一个32位的整数时，它会把整数划分为高 16 位和低 16 位，其中高 16 位决定该数据需要被分至哪个桶，我们只需要存储这个数据剩余的低 16 位，将低 16 位存储到 Container 中，若当前桶不存在数据，直接存储 null 节省空间。RoaringBitmap有不同的实现方式，下面以 Lucene 实现（RoaringDocIdSet）进行详细讲解：

如原理图中所示，RoaringBitmap 中存在两种不同的 Container：Bitmap Container 和 Array Container。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUUbRV1cVqTqicZlOle4Eia62OBbAsNoTicRFa81LjWYaoUV1QwQULQdQJmiahtSCxtHbwibnRwxXg07MA/640?wx_fmt=jpeg)

图3 Elasticsearch中Roaringbitmap的示意图

这两种 Container 分别对应不同的数据场景——若一个 Container 中的数据量小于 4096 个时，使用 Array Container 来存储。当 Array Container 中存放的数据量大于 4096 时，Roaring Bitmap 会将 Array Container 转为 Bitmap Container。即 Array Container 用于存放稀疏数据，而 Bitmap Container 用于存放稠密数据，这样做是为了充分利用空间。下图给出了随着容量增长 Array Container 和 Bitmap Container 的空间占用对比图，当元素个数达到 4096 后（每个元素占用 16 bit ），Array Container 的空间要大于 Bitmap Container。

备注：Roaring Bitmap 可参考官方博客[4]。

#### 4.2.3 Index Sorting

Elasticsearch 从 6.0 版本开始支持 Index Sorting[5] 功能，在索引阶段可以配置多个字段进行排序，调整索引数据组织方式，可以调整文档所对应的 Doc ID。以 city\_id，poi\_id 为例：

![](https://mmbiz.qpic.cn/mmbiz_jpg/hEx03cFgUsUUbRV1cVqTqicZlOle4Eia62snxWJ3Y90A38eEnBkribZtbW96ycWBbepV5FTkbo70EFVib2RS5fIOZg/640?wx_fmt=jpeg)

图4 Index Sorting 示意图

如上示例所示：Index Sorting 会将给定的排序字段（如上图的 city\_id 字段）的文档排序在一起，相同排序值的文档的 Doc ID 严格自增，对该字段建立倒排，那么其倒排链为自增数列。

### 4.3 基于 RLE 的倒排格式设计

基于以上的背景知识以及当前 Elasticsearch/Lucene 的解决方案，可以明确目前有 2 个改造点需要考虑。

* 合适的倒排结构，用于存储每个 Term 的倒排链。
* 合适的中间结构，用于存储多个 Term 合并后的倒排链。

对于索引倒排格式 PostingsEnum，支持接口为：

```
public abstract class DocIdSetIterator {
  public abstract int docID();
  public abstract int nextDoc();
  public abstract int advance(int target);
}
```

倒排仅支持单文档循环调用，不支持批量读取，因此需要为倒排增加批量顺序读取的功能。

对于多倒排链的合并，由于原结构 DocIdSetBu...