---
title: 直观解读 JuiceFS 的数据和元数据设计（三）：看山还是山（2024）
url: https://arthurchiao.github.io/blog/juicefs-data-metadata-design-illustrative-guide-3-zh/
source: ArthurChiao's Blog
date: 2024-10-28
fetch_date: 2025-10-06T18:45:35.812046
---

# 直观解读 JuiceFS 的数据和元数据设计（三）：看山还是山（2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# 直观解读 JuiceFS 的数据和元数据设计（三）：看山还是山（2024）

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

* [1 如何从数据和元数据中恢复文件](#1-如何从数据和元数据中恢复文件)
  + [1.2 理论步骤](#12-理论步骤)
  + [1.2 `juicefs info` 查看文件 chunk/slice/block 信息](#12-juicefs-info-查看文件-chunksliceblock-信息)
* [2 如何判断 `{volume}/chunks/` 中的数据是否是合法](#2-如何判断-volumechunks-中的数据是否是合法)
  + [2.1 原理](#21-原理)
  + [2.2 改进：pending delete slices](#22-改进pending-delete-slices)
  + [2.3 工具：`juicefs gc`](#23-工具juicefs-gc)
    - [2.3.1 核心代码](#231-核心代码)
      * [从元数据引擎 list 所有 slice 信息](#从元数据引擎-list-所有-slice-信息)
      * [从对象存储 list 所有 objects 信息](#从对象存储-list-所有-objects-信息)
      * [遍历所有 objects，跟元数据引擎中的 slice 信息比对](#遍历所有-objects跟元数据引擎中的-slice-信息比对)
    - [2.3.2 使用方式](#232-使用方式)
* [3 问题讨论](#3-问题讨论)
  + [3.1 chunk id 和 slice id 的分配](#31-chunk-id-和-slice-id-的分配)
  + [3.2 JuiceFS pending delete slices 和 background job](#32-juicefs-pending-delete-slices-和-background-job)
    - [3.2.1 设计初衷](#321-设计初衷)
    - [3.2.2 代码](#322-代码)
    - [3.2.3 潜在的问题](#323-潜在的问题)
  + [3.3 JuiceFS 支持的单个最大文件 128PiB 是怎么来的](#33-juicefs-支持的单个最大文件-128pib-是怎么来的)
  + [3.4 为什么 JuiceFS 写入对象存储的文件，不能通过对象存储直接读取？](#34-为什么-juicefs-写入对象存储的文件不能通过对象存储直接读取)
  + [3.5 JuiceFS 不会对文件进行合并](#35-juicefs-不会对文件进行合并)
* [4 总结](#4-总结)
* [参考资料](#参考资料)

---

# 1 如何从数据和元数据中恢复文件

## 1.2 理论步骤

对于一个给定的 JuiceFS 文件，我们在上一篇中已经看到两个正向的过程：

1. **文件本身**被切分成 Chunk、Slice、Block，然后写入对象存储；
2. **文件的元数据**以 inode、slice、block 等信息组织，写入元数据引擎。

有了对正向过程的理解，我们反过来就能从对象存储和元数据引擎中恢复文件：
对于一个给定的 JuiceFS 文件，

1. 首先扫描元数据引擎，通过文件名、inode、slice 等等信息，拼凑出文件的大小、位置、权限等等信息；
2. 然后根据 slice\_id/block\_id/block\_size 拼凑出对象存储中的 object key；
3. 依次去对象存储中根据这些 keys 读取数据拼到一起，得到的就是这个文件，然后写到本地、设置文件权限等等。

但这个恢复过程不是本文重点。本文主要看几个相关的问题，以加深对 JuiceFS 数据/元数据 设计的理解。
更多信息见官方文档 [2]。

## 1.2 `juicefs info` 查看文件 chunk/slice/block 信息

JuiceFS 已经提供了一个命令行选项，能直接查看文件的 chunk/slice/block 信息，例如：

```
$ ./juicefs info foo-dev/file2_5MB
foo-dev/file2_5MB :
  inode: 3
  files: 1
   dirs: 0
 length: 5.00 MiB (5242880 Bytes)
   size: 5.00 MiB (5242880 Bytes)
   path: /file2_5MB
 objects:
+------------+--------------------------------+---------+--------+---------+
| chunkIndex |           objectName           |   size  | offset |  length |
+------------+--------------------------------+---------+--------+---------+
|          0 | foo-dev/chunks/0/0/3_0_4194304 | 4194304 |      0 | 4194304 |
|          0 | foo-dev/chunks/0/0/3_1_1048576 | 1048576 |      0 | 1048576 |
+------------+--------------------------------+---------+--------+---------+
```

和我们在 MinIO 中看到的一致。

# 2 如何判断 `{volume}/chunks/` 中的数据是否是合法

bucket 中的数据是 JuiceFS 写入的，还是其他应用写入的呢？
另外即使是 JuiceFS 写入的，也可能有一些数据是无效的，比如 size 为 0 的 block、超出所属 slice 范围的 block 等等。
我们来看看基于哪些规则，能对这些非法数据进行判断。

## 2.1 原理

准备工作：

1. 从 JuiceFS 的元数据引擎中读取所有 slice size，这对应的是**元数据信息**；
2. 从 object storage 中读取所有 object key，这对应的**数据信息**。

接下来，根据几条标准，判断 bucket 中 `{volume}/chunks/` 内的数据是否是合法的 JuiceFS 数据：

1. 如果 object 不符合命名规范
   `{volume}/chunks/{slice_id/1000/1000}/{slice_id/1000}/{slice_id}_{block_id}_{block_size}`，
   那么这个 object 就不是 JuiceFS 写入的；
2. 如果符合以上命名规范，，那么这个 object 就是 JuiceFS 写入的，接下来，
   1. 如果 object 大小为零，那可以清理掉，因为这种 object 留着没意义；
   2. 如果 object 大小不为零，根据元数据内记录的 slice/block 信息计算这个 block 应该是多大，
      1. 如果大小跟 object 一致，那这个 object 就是一个合法的 JuiceFS 数据（Block）；
      2. 否则，说明这个 object 有问题。

这个过程是没问题的，但需要对所有 object 和所有元数据进行遍历和比对，效率比较低。
有没有更快的方法呢？

## 2.2 改进：pending delete slices

回忆上一篇，在元数据引擎中其实已经记录了**待删除的 slice/block 信息**，
这里“待删除”的意思是 JuiceFS 中已经把文件删掉了（**用户看不到了，volume usage 统计也不显示了**），
但还没有从对象存储中删掉，

* `D` 开头的记录：**`d`**eleted inodes
* 格式：`D{8bit-inode}{8bit-length}`，

这种记录是 JuiceFS 在从 object storage 删除文件之前插入到元数据引擎中的，
所以扫描所有 `D` 开头的记录，可以找到所有待删除的 slice/block 信息。

## 2.3 工具：`juicefs gc`

结合 2.1 & 2.2，就可以快速判断 bucket 中的数据是否是 JuiceFS 合法数据，不是就删掉；
基于 juicefs 已有的代码库，就可以写一个工具 —— 但用不着自己写 —— JuiceFS 已经提供了。

### 2.3.1 核心代码

完整代码见 pkg/cmd/gc.go。

#### 从元数据引擎 list 所有 slice 信息

```
func (m *kvMeta) ListSlices(ctx Context, slices map[Ino][]Slice, delete bool, showProgress func()) syscall.Errno {
    if delete
        m.doCleanupSlices()

    // 格式：A{8digit-inode}C{4digit-blockID}   file chunks
    klen := 1 + 8 + 1 + 4
    result := m.scanValues(m.fmtKey("A"), -1, func(k, v []byte) bool { return len(k) == klen && k[1+8] == 'C' })

    for key, value := range result {
        inode := m.decodeInode([]byte(key)[1:9])
        ss := readSliceBuf(value) // slice list
        for _, s := range ss
            if s.id > 0
                slices[inode] = append(slices[inode], Slice{Id: s.id, Size: s.size})
    }

    if m.getFormat().TrashDays == 0
        return 0

    return errno(m.scanTrashSlices(ctx, func(ss []Slice, _ int64) (bool, error) {
        slices[1] = append(slices[1], ss...)
        if showProgress != nil
            for range ss
                showProgress()
        return false, nil
    }))
}
```

#### 从对象存储 list 所有 objects 信息

```
    // Scan all objects to find leaked ones
    blob = object.WithPrefix(blob, "chunks/")
    objs := osync.ListAll(blob, "", "", "", true) // List {vol_name}/chunks/ 下面所有对象
```

#### 遍历所有 objects，跟元数据引擎中的 slice 信息比对

```
    for obj := range objs {
        // key 格式：{slice_id/1000/1000}/{slice_id/1000}/{slice_id}_{index}_{size}
        parts := strings.Split(obj.Key(), "/")     // len(parts) == 3
        parts = strings.Split(parts[2], "_")       // len(parts) == 3

        sliceID, _ := strconv.Atoi(parts[0])       // slice id, JuiceFS globally unique
        blockID, _ := strconv.Atoi(parts[1])       // blockID in this slice
        blockSize, _ := strconv.Atoi(parts[2])     // block size, <= 4MB
        sliceSizeFromMetaEngine := sliceSizesFromMetaEngine[uint64(sliceID)]       // tikv 中记录的 slice size

        var isEmptySize bool
        if sliceSizeFromMetaEngine == 0 {
            sliceSizeFromMetaEngine = sliceSizesFromTrash[uint64(sliceID)]
            isEmptySize = true
        }
        if sliceSizeFromMetaEngine == 0 {
            foundLeaked(obj)
            continue
        }

        if blockSize == chunkConf.BlockSize { // exactly 4MB
            if (blockID+1)*blockSize > sliceSizeFromMetaEngine
                foundLeaked(obj)
        } else {                              // < 4MB
            if blockID*chunkConf.BlockSize+blockSize != sliceSizeFromMetaEngine
                foundLeaked(obj)
        }
```

1. slice size 为 0，说明这个 slice 在元数据引擎中被 compact 过了；
2. slice size 非零，
   * block size == 4MB，可能是也可能不是最后一个 block；
   * block size != 4MB，说明这个 block 是最后一个 block；

### 2.3.2 使用方式

```
$ ./juicefs gc -h
NAME:
   juicefs gc - Garbage collector of objects in data storage

USAGE:
   juicefs gc [command options] META-URL
```

大致效果：

```
$ ./juicefs gc tikv://192.168.1.1:2379,192.168.1.2:2379,192.168.1.3:2379/foo-dev
<INFO>: TiKV gc interval is set to 3h0m0s [tkv_tikv.go:138]
<INFO>: Data use minio://localhost:9000/juicefs-bucket/foo-dev/ [gc.go:101]

Pending deleted files: 0                             0.0/s
 Pending deleted data: 0.0 b     (0 Bytes)           0.0 b/s
Cleaned pending files: 0                             0.0/s
 Cleaned pending data: 0.0 b     (0 Bytes)           0.0 b/s
        Listed slices: 6                             327.3/s
         Trash slices: 0                             0.0/s
           Trash ...