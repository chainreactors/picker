---
title: 直观解读 JuiceFS 的数据和元数据设计（二）：看山不是山（2024）
url: https://arthurchiao.github.io/blog/juicefs-data-metadata-design-illustrative-guide-2-zh/
source: ArthurChiao's Blog
date: 2024-10-28
fetch_date: 2025-10-06T18:45:48.558905
---

# 直观解读 JuiceFS 的数据和元数据设计（二）：看山不是山（2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# 直观解读 JuiceFS 的数据和元数据设计（二）：看山不是山（2024）

Published at 2024-10-27 | Last Update 2024-10-27

本系列分为三篇文章，试图通过简单的实地环境来**直观理解** JuiceFS
的**数据（data）和元数据（metadata）**设计。

![](/assets/img/juicefs-data-metadata-design/juicefs-obj-naming.png)

Fig. JuiceFS object key naming and the objects in MinIO.

水平及维护精力所限，文中不免存在错误或过时之处，请酌情参考。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

* [直观解读 JuiceFS 的数据和元数据设计（一）：看山是山（2024）](/blog/juicefs-data-metadata-design-illustrative-guide-1-zh/)
* [直观解读 JuiceFS 的数据和元数据设计（二）：看山不是山（2024）](/blog/juicefs-data-metadata-design-illustrative-guide-2-zh/)
* [直观解读 JuiceFS 的数据和元数据设计（三）：看山还是山（2024）](/blog/juicefs-data-metadata-design-illustrative-guide-3-zh/)

---

* [1 引言](#1-引言)
* [2 对象存储中 JuiceFS 写入的文件](#2-对象存储中-juicefs-写入的文件)
  + [2.1 Bucket 内：每个 volume 一个“目录”](#21-bucket-内每个-volume-一个目录)
  + [2.2 每个 volume 的目录： `{chunks/, juicefs_uuid, meta/, ...}`](#22-每个-volume-的目录-chunks-juicefs_uuid-meta-)
    - [2.2.1 `juicefs_uuid`：JuiceFS volume 的唯一标识](#221-juicefs_uuidjuicefs-volume-的唯一标识)
    - [2.2.2 `meta/`：JuiceFS 元数据备份](#222-metajuicefs-元数据备份)
    - [2.2.3 `chunks/`](#223-chunks)
  + [2.3 小结](#23-小结)
* [3 JuiceFS 数据的设计](#3-juicefs-数据的设计)
  + [3.1 顶层切分：一切文件先切 chunk](#31-顶层切分一切文件先切-chunk)
    - [3.1.1 示意图](#311-示意图)
    - [3.1.2 对象存储：不存在 chunk 实体](#312-对象存储不存在-chunk-实体)
  + [3.2 Chunk 内的一次连续写入：Slice](#32-chunk-内的一次连续写入slice)
    - [3.2.1 Slice 的重叠问题](#321-slice-的重叠问题)
    - [3.2.2 读 chunk 数据时的多 slice 处理：碎片化和碎片合并](#322-读-chunk-数据时的多-slice-处理碎片化和碎片合并)
    - [3.2.3 对象存储：不存在 slice 实体](#323-对象存储不存在-slice-实体)
  + [3.3 Slice 切分成固定大小 Block（e.g. 4MB）：并发读写对象存储](#33-slice-切分成固定大小-blockeg-4mb并发读写对象存储)
  + [3.4 object key 命名格式（及代码）](#34-object-key-命名格式及代码)
  + [3.5 将 chunk/slice/block 对应到对象存储](#35-将-chunksliceblock-对应到对象存储)
  + [3.6 小结：光靠对象存储数据和 slice/block 信息无法还原文件](#36-小结光靠对象存储数据和-sliceblock-信息无法还原文件)
* [4 JuiceFS 元数据的设计（`TKV` 版）](#4-juicefs-元数据的设计tkv-版)
  + [4.1 TKV 类型 key 列表](#41-tkv-类型-key-列表)
  + [4.2 元数据引擎中的 key/value](#42-元数据引擎中的-keyvalue)
    - [4.2.1 扫描相关的 TiKV key](#421-扫描相关的-tikv-key)
    - [4.2.2 解码成 JuiceFS metadata key](#422-解码成-juicefs-metadata-key)
* [5 总结](#5-总结)
* [参考资料](#参考资料)

---

# 1 引言

上一篇从功能的角度体验了下 JuiceFS，这一篇我们深入到背后，看看 JuiceFS
分别在数据和元数据上做了哪些设计，才给到用户和本地文件系统一样的体验的。

# 2 对象存储中 JuiceFS 写入的文件

本篇以 MinIO 为例，来看 JuiceFS 写入到对象存储中的文件是怎样组织的。
其他云厂商的对象存储（AWS S3、阿里云 OSS 等）也都是类似的。

## 2.1 Bucket 内：每个 volume 一个“目录”

可以用上一篇介绍的 `juicefs format` 命令再创建两个 volume，方便观察它们在 bucket 中的组织关系，

![](/assets/img/juicefs-data-metadata-design/minio-bucket-volume-list.png)

Fig. MinIO bucket browser: volume list.

如上图所示，bucket 内的**顶层“目录”就是 JuiceFS 的 volumes**，

我们这里提到**“目录”**时加双引号，是因为对象存储是扁平的 key-value 存储，**没有目录的概念**，
前端展示时**模拟出目录结构**（key 前缀一样的，把这个前缀作为一个“目录”）是为了查看和理解方便。
简单起见，后文不再加双引号。

## 2.2 每个 volume 的目录： `{chunks/, juicefs_uuid, meta/, ...}`

每个 volume 目录内的结构如下：

```
{volume_name}/
  |-chunks/         # 数据目录，volume 中的所有用户数据都放在这里面
  |-juicefs_uuid
  |-meta/           # `juicefs mount --backup-meta ...` 产生的元数据备份存放的目录
```

### 2.2.1 `juicefs_uuid`：JuiceFS volume 的唯一标识

可以把这个文件下载下来查看内容，会发现里面存放的就是 juicefs format 输出里看到的那个 uuid，
也就是这个 volume 的唯一标识。

删除 volume 时需要用到这个 uuid。

### 2.2.2 `meta/`：JuiceFS 元数据备份

如果在 `juicefs mount` 时指定了 `--backup-meta`，JuiceFS 就会定期把元数据（存在在 TiKV 中）备份到这个目录中，
用途：

1. 元数据引擎故障时，可以从这里恢复；
2. 在不同元数据引擎之间迁移元数据。

详见 [JuiceFS 元数据引擎五探：元数据备份与恢复（2024）](/blog/juicefs-metadata-deep-dive-5-zh/)。

### 2.2.3 `chunks/`

![](/assets/img/juicefs-data-metadata-design/minio-juicefs-block-list.png)

Fig. MinIO bucket browser: files in a bucket.

`chunks/` 内的目录结构如下，

```
{volume_name}/
  |-chunks/
  |   |-0/                # <-- id1 = slice_id / 1000 / 1000
  |   |  |-0/             # <-- id2 = slice_id / 1000
  |   |     |-1_0_16      # <-- {slice_id}_{block_id}_{size_of_this_block}
  |   |     |-3_0_4194304 #
  |   |     |-3_1_1048576 #
  |   |     |-...
  |-juicefs_uuid
  |-meta/
```

如上，所有的文件在 bucket 中都是用数字命名和存放的，分为三个层级：

1. 第一层级：纯数字，是 sliceID 除以 100 万得到的；
2. 第二层级：纯数字，是 sliceID 除以 1000 得到的；
3. 第三层级：纯数字加下划线，`{slice_id}_{block_id}_{size_of_this_block}`，表示的是这个 chunk 的这个 slice 内的 block\_id 和 block 的大小。

不理解 chunk/slice/block 这几个概念没关系，我们马上将要介绍。

## 2.3 小结

通过以上 bucket 页面，我们非常直观地看到了**一个 JuiceFS volume 的所有数据在对象存储中是如何组织的**。

接下来进入正题，了解一下 JuiceFS 的数据和元数据设计。

# 3 JuiceFS 数据的设计

## 3.1 顶层切分：一切文件先切 chunk

对于**每个文件**，JuiceFS 首先会按**固定大小（64MB）切大块**，
这些大块称为「**`Chunk`**」。

* 这是为了读或修改文件内容时，**方便查找和定位**。
* 不管是一个**只有几字节的文本文件**，还是一个**几十 GB 的视频文件**，
  在 JuiceFS 中都是切分成 chunk，只是 chunk 的数量不同而已。

### 3.1.1 示意图

![](/assets/img/juicefs-data-metadata-design/file-to-chunk.png)

Fig. JuiceFS: split each file into their respective chunks (with max chunk size 64MB).

### 3.1.2 对象存储：不存在 chunk 实体

结合上一节在对象存储中看到的目录结构，

```
{volume_name}/
  |-chunks/
  |   |-0/                # <-- id1 = slice_id / 1000 / 1000
  |   |  |-0/             # <-- id2 = slice_id / 1000
  |   |     |-1_0_16      # <-- {slice_id}_{block_id}_{size_of_this_block}
  |   |     |-3_0_4194304 #
  |   |     |-3_1_1048576 #
  |   |     |-...
  |-juicefs_uuid
  |-meta/
```

1. Chunk 在对象存储中 **没有对应任何实际文件**，也就是说在**对象存储中没有一个个 64MB 的 chunks**；
2. 用 JuiceFS 的话来说，Chunk 是一个逻辑概念。暂时不理解没关系，接着往下看。

## 3.2 Chunk 内的一次连续写入：Slice

chunk 只是一个“框”，在这个框里面对应**文件读写**的，是 JuiceFS 称为「Slice」 的东西。

* chunk 内的**一次连续写入**，会**创建一个 slice**，对应这段连续写入的数据；
* 由于 slice 是 chunk 内的概念，因此它不能跨 Chunk 边界，长度也不会超 max chunk size 64M。
* slice ID 是**全局唯一**的；

### 3.2.1 Slice 的重叠问题

根据写入行为的不同，一个 Chunk 内可能会有多个 Slice，

* 如果文件是由一次**连贯的顺序**写生成，那每个 Chunk **只包含一个 Slice**。
* 如果文件是**多次追加写**，每次追加均调用 **`flush`** 触发写入上传，就会产生**多个 Slice**。

![](/assets/img/juicefs-data-metadata-design/chunks-to-slices.png)

Fig. JuiceFS: chunks are composed of slices, each slice corresponds to a continues write operation.

拿 chunk1 为例，

1. 用户先写了一段 ~30MB 数据，产生 **`slice5`**；
2. 过了一会，从 ~20MB 的地方重新开始写 45MB（删掉了原文件的最后一小部分，然后开始追加写），
   * chunk1 内的部分产生 **`slice6`**；
   * 超出 chunk1 的部分，因为 slice 不能跨 chunk 边界，因此产生 **`chunk2`** 和 **`slice7`**；
3. 过了一会，从 chunk1 ~10MB 的地方开始修改（覆盖写），产生 **`slice8`**。

由于 Slice 存在重叠，因此引入了几个字段标识它的有效数据范围，

```
// pkg/meta/slice.go

type slice struct {
    id    uint64
    size  uint32
    off   uint32
    len   uint32
    pos   uint32
    left  *slice // 这个字段不会存储到 TiKV 中
    right *slice // 这个字段不会存储到 TiKV 中
}
```

### 3.2.2 读 chunk 数据时的多 slice 处理：碎片化和碎片合并

![](/assets/img/juicefs-data-metadata-design/chunks-to-slices.png)

Fig. JuiceFS: chunks are composed of slices, each slice corresponds to a continues write operation.

对 JuiceFS 用户来说，文件永远只有一个，但在 JuiceFS 内部，这个文件对应的 Chunk 可能会有多个重叠的 Slice，

* 有重叠的部分，以最后一次写入的为准。
* 直观上来说，就是上图 chunk 中的 slices 从**上往下看，被盖掉的部分都是无效的**。

因此，读文件时，需要查找「当前读取范围内最新写入的 Slice」，

* 在大量重叠 Slice 的情况下，这会显著影响读性能，称为文件「碎片化」。
* 碎片化不仅影响读性能，还会在对象存储、元数据等层面增加空间占用。
* 每当写入发生时，客户端都会判断文件的碎片化情况，并异步地运行碎片合并，将一个 Chunk 内的所有 Slice 合并。

### 3.2.3 对象存储：不存在 slice 实体

跟 chunk 类似，在对象存储中 slice 也没有 **没有对应实际文件**。

```
{volume_name}/
  |-chunks/
  |   |-0/                # <-- id1 = slice_id / 1000 / 1000
  |   |  |-0/             # <-- id2 = slice_id / 1000
  |   |     |-1_0_16      # <-- {slice_id}_{block_id}_{size_of_this_block}
  |   |     |-3_0_4194304 #
  |   |     |-3_1_1048576 #
  |   |     |-...
  |-juicefs_uuid
  |-meta/
```

## 3.3 Slice 切分成固定大小 Block（e.g. 4MB）：并发读写对象存储

为了加速写到对象存储，JuiceFS 将 Slice 进一步拆分成一个个「Block」（默认 4MB），**多线程并发**写入。

![](/assets/img/juicefs-data-metadata-design/slices-to-blocks.png)

Fig. JuiceFS: slices are composed of blocks (4MB by default), each block is an object in object storage.

Block 是 JuiceFS 数据切分设计中**最后一个层级**，也是 chunk/slice/block
三个层级中**唯一能在 bucket 中看到对应文件的**。

![](/assets/img/juicefs-data-metadata-design/minio-juicefs-block-list.png)

Fig. MinIO bucket browser: objects in a bucket.

* **连续写**：前面 Block 默认都是 4MB，最后一个 Block 剩多少是多少。
* **追加写**：数据不足 4MB 时，最终存入对象存储的也会是一个小于 4M 的 Block。

从上图的名字和大小其实可以看出分别对应我们哪个文件：

1. `1_0_16`：对应我们的 `file1_1KB`；
   * 我们上一篇的的**追加...