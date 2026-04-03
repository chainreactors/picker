---
title: 干货 | 携程 JDK25 升级踩坑记：一场由 G1GC “偷走”对象引发的数据静默损坏
url: https://mp.weixin.qq.com/s/V40usdvE3y9kVdkKM6MZ3g
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:27:03.710590
---

# 干货 | 携程 JDK25 升级踩坑记：一场由 G1GC “偷走”对象引发的数据静默损坏

![cover_image](http://mmecoa.qpic.cn/sz_mmecoa_jpg/h6WFQibcNiae5uh0aXUQAYoZ8qA81q6QYyx7vkzibxtibeohZ0J6MicZ5O4pZicjElOXKwwusVr9xXa5tY8xSoAvpS5JjF3kSMmuus7Smn6kQibOh0/0?wx_fmt=jpeg)

# 干货 | 携程 JDK25 升级踩坑记：一场由 G1GC “偷走”对象引发的数据静默损坏

原创

cxzl25/lsm
cxzl25/lsm

携程技术

![]()

在小说阅读器中沉浸阅读

**作者简介**

cxzl25，携程高级软件技术专家，关注数据领域生态建设，对分布式计算和存储、调度等方面有浓厚兴趣，Apache kyuubi/ORC/Auron (P)PMC Member，Apache Celeborn Committer。

lsm，携程高级开发工程师，关注分布式计算和优化，Apache Kyuubi Committer。

导读：携程大数据平台运行着大规模的 Spark、Flink 计算集群，为充分发挥 JDK25 LTS 版本在内存效率与运行性能上的优势，我们启动了 JDK 升级计划，并完成了 多个引擎 对 JDK25 的适配改造，开始向生产环境灰度推进。

然而就在灰度期间，我们遭遇了一个极为罕见的问题：Spark、Flink 写入的 Parquet、ORC 文件出现部分损坏——写入过程无任何报错，CRC 校验也完全通过，损坏只在下游读取时才会暴露。

本文记录了我们如何从一个"Zstd 解压报错"出发，借助多款 AI 工具辅助分析，历经代码排查、JDK 版本二分、自建编译环境等多个阶段，最终将问题根因锁定到 JDK25 G1GC 的一个内部优化 Bug，并推动 OpenJDK 社区完成 backport 修复。文章还将深度解析 G1 GC 的 Optional Evacuation 机制与 JNI Pinning 原理，以及 AI 工具在整个排查链路中的具体作用。

* 一、背景
* 二、影响面：为何这个 Bug 格外危险
* 三、数据读取损坏的报错
* 四、损坏文件分析
* 五、问题怀疑方向
* 六、问题复现
* 七、代码的各种尝试
* 八、JDK 的各种尝试
* 九、数据损坏的根因分析
* 十、后续复盘
* 十一、AI 辅助排障全程回顾
* 十二、总结

一、背景

生产环境中 Spark 已基于 JDK21 运行，为使用 JDK25 LTS 版本的新特性紧凑对象头（Compact Object Headers）（JEP 519，开启参数-XX:+UseCompactObjectHeaders），实现内存占用节省、GC 效率提升与性能优化，计划将运行环境升级至 JDK25，并完成了 Spark 对 JDK25 的适配工作，支持灰度切换。

但在灰度推进阶段，用户反馈出现数据读取异常问题：实时任务中 Flink 写入 Paimon 的 Parquet 文件部分读取失败，离线任务中 Spark 写入的 ORC、Parquet 文件也存在部分读取失败的情况。

JEP 519: Compact Object Headers

<https://openjdk.org/jeps/519>

二、影响面：为何这个 Bug 格外危险

该 Bug 影响 JDK 25.0.0、25.0.1、25.0.2 全部 JDK25 已发布版本，预计 2026 年 4 月 21 日发布的 25.0.3 版本修复。任何在上述版本上开启 G1GC（JDK25 默认 GC）的 Java 应用均存在风险。可以用 -XX:+UseParallelGC 或 -XX:+UseZGC 避免此问题。在未来发布的 JDK 25.0.3 可以启用 G1。

该 Bug 的根本原因是 G1 GC 在 Optional Evacuation 阶段错误移动了被 JNI 临界区锁定的对象。因此，凡是通过 GetPrimitiveArrayCritical / ReleasePrimitiveArrayCritical 这对 JNI 接口直接操作 Java 数组内存的场景，均存在触发该 Bug 的风险。

该 Bug 最大的危险在于写入过程完全无异常抛出（静默损坏）。数据已经损坏地写入存储，只有在后续读取/解压时才会报错，数据不可恢复。

受影响的组件/库包括但不限于：

* zstd-jni：Zstd 压缩（ORC、Parquet、Kafka 消息体等大量使用）
* JDK 内置 Zip/Deflate 库：java.util.zip.Deflater / Inflater（同样基于 JNI 实现，已验证可复现）
* 其他调用 Native 压缩/加密/数学运算库等各种场景。

三、数据读取损坏的报错

作业写入流程均正常，下游作业读取特定列或某段数据时触发报错，核心报错类型集中为 Zstd 解压相关异常，具体如下：

Src size is incorrect

```
Caused by: com.github.luben.zstd.ZstdException: Src size is incorrect        at com.github.luben.zstd.ZstdDecompressCtx.decompressByteArray(ZstdDecompressCtx.java:205)        at com.github.luben.zstd.Zstd.decompressByteArray(Zstd.java:439)        at org.apache.orc.impl.ZstdCodec.decompress(ZstdCodec.java:218)        at org.apache.orc.impl.InStream$CompressedStream.readHeader(InStream.java:495)        at org.apache.orc.impl.InStream$CompressedStream.ensureUncompressed(InStream.java:522)
```

Decompression error: Destination buffer is too small

```
Caused by: java.io.IOException: Decompression error: Destination buffer is too small        at com.github.luben.zstd.ZstdInputStreamNoFinalizer.readInternal(ZstdInputStreamNoFinalizer.java:171)        at com.github.luben.zstd.ZstdInputStreamNoFinalizer.read(ZstdInputStreamNoFinalizer.java:123)        at com.github.luben.zstd.ZstdInputStream.read(ZstdInputStream.java:88)        at org.apache.paimon.shade.org.apache.parquet.hadoop.codec.ZstdDecompressorStream.read(ZstdDecompressorStream.java:43)
```

Decompression error: Corrupted block detected

```
Caused by: java.io.IOException: Decompression error: Corrupted block detected        at com.github.luben.zstd.ZstdInputStreamNoFinalizer.readInternal(ZstdInputStreamNoFinalizer.java:171)        at com.github.luben.zstd.ZstdInputStreamNoFinalizer.read(ZstdInputStreamNoFinalizer.java:123)        at com.github.luben.zstd.ZstdInputStream.read(ZstdInputStream.java:87)        at org.apache.parquet.hadoop.codec.ZstdDecompressorStream.read(ZstdDecompressorStream.java:43)        at java.io.DataInputStream.readFully(DataInputStream.java:195)
```

四、损坏文件分析

4.1 定位损坏列

从报错日志锁定异常表及对应文件，利用 Parquet、ORC 的列式存储特性，通过select sum(hash(struct(colX)))语句定位具体损坏的列（未读取损坏列时不会触发报错）。

4.2 排除存储介质问题

Parquet 默认开启parquet.page.write-checksum.enabled=true，列 Page 压缩后的数据会通过 CRC32 计算校验值并写入 Page header。开启读取校验参数parquet.page.verify-checksum.enabled=true，通过 Parquet CLI 执行校验：

```
./bin/hadoop jar parquet-cli-1.13.0-runtime.jar org.apache.parquet.cli.Main -Dparquet.page.verify-checksum.enabled=true cat data.parquet
```

校验结果无报错，说明压缩后写入文件的字节流与读取时一致，排除 HDFS 等存储介质导致的数据损坏。

4.3 验证数据损坏特征

* 对 Zstd 解压后的字节流本地落地，使用zstd -d工具解压提示Decoding error (36) : Data corruption detected，使用crc32 命令校验此文件，CRC32 校验结果与 Page Header 中的校验值一致；
* 改造 Parquet 代码实现损坏 Page 跳过逻辑，验证仅少量列的部分 Page 存在数据损坏，其余数据可正常读取。

4.4 尝试数据恢复与原因分析

* 编译开启 DEBUGLEVEL=5 的 zstd 工具，通过多个 AI 对 debug 日志分析解压失败原因，未获有效结果；
* 借助 Cursor AI 分析本地落地的二进制数据，确认其符合 Zstd 文件格式规范，并生成 Python 恢复脚本，基于 Zstd 的按 Block 分割特性恢复出部分数据。

五、问题怀疑方向

结合作业运行环境的多样性，梳理出以下核心怀疑点：

* JDK25 紧凑对象头特性是否改变对象内存布局，进而影响压缩流程；
* 压缩库如 zstd-jni ，或者列格式 Parquet、ORC，又或者计算引擎 Spark、Flink 没有完全适配 JDK25，导致压缩数据损坏；
* Linux 操作系统或内核版本是否存在兼容性问题；
* 其他未明确的环境或组件交互问题...

六、问题复现

在少量失败作业中，筛选出运行时长短、可偶现的 Spark 任务，开展复现测试，核心发现如下：

* ORC 2.0 以上的版本 Zstd 压缩支持两种实现：airlift aircompressor 的纯 Java 实现、zstd-jni 的 C 代码实现（默认使用，性能更优且支持更多压缩参数）；通过-Dorc.compression.zstd.impl=java切换为 Java 实现后，多次运行未复现问题，怀疑 zstd-jni 存在适配问题；
* 物理机集群中该任务基本无法复现，Docker 构造的集群（Spark Executor 运行在 Docker 中）可偶现，且两类集群的 OS、内核版本不一致。

七、代码的各种尝试

在 ORC Zstd 压缩实现中开启 Zstd checksum (zstdCompressCtx.setCheck sum(true)），解压仍无报错，该方案无效；

实现压缩 - 解压校验逻辑：对原始数据 a 压缩得到 b1 并立即解压，若解压失败则重新压缩 a 得到 b2 并解压，对比 b1 和 b2 的十六进制差异并日志输出；多次复现发现压缩长度一致，但字节偏移量和损坏位置无规律，该方案无法定位根因。

八、JDK 的各种尝试

* 关闭 JDK25 的紧凑对象头特性后，问题仍可复现，排除该特性的影响。
* 使用多个 JDK25 release 版本均（25.0.0、25.0.1 、25.0.2 ）均能复现问题。
* 使用 JDK21 到 JDK25 之间的几个 JDK 版本，如 JDK23 和 JDK24 最后一个版本，没有重现此问题。
* JDK26、27 因 Spark 兼容性问题未完成测试。

说明问题可能出在 JDK24 到 JDK25 的改动。

由于损坏的列的数据基本上是大文本字符串，观察到 Spark GC 耗时较为异常，尝试更换 GC 算法。

生产环境运行的 Spark 任务，原先基于 JDK8 并使用 ParallelGC 垃圾收集器。切换至 JDK21 后，初期仍沿用 ParallelGC，但运行过程中发现 Spark Executor 因物理内存使用超限被 YARN killed，日志中有Container killed by YARN for exceeding physical memory limit。经排查，该问题与 JDK 8328744: Parallel: Parallel GC throws OOM before heap is fully expanded 相关，因此在 JDK21 环境下将垃圾收集器调整为 G1GC 后上线。

在 JDK25 沿用了 JDK21 的配置，上线的时候使用默认的 G1GC，但是在 JDK25 使用 ParallelGC，ZGC 都未能重现数据损坏问题。

说明问题有可能出现在 JDK25 环境开启 G1GC 导致的数据损坏。

下载各种 JDK25 的 各开发版本测试，最终在 tag jdk-25+9 一切正常， 在 jdk-25+10 可偶现问题。

<https://github.com/adoptium/temurin25-binaries/releases>

为定位具体引入问题的 Commit，此时需要一个支持指定 Commit ID 的 JDK25 编译环境，并适用于生产环境运行的 JDK25 版本。

借助 GitHub Agents 的能力，根据需求，vibe 了一个 build JDK25 的 Workflow，方便编译多个版本的 JDK。

由于生产环境 Docker 的镜像的 glibc 版本比较低，导致在 Workflow 编译的 JDK25 并不能这个环境使用，让 GitHub Copilot 根据报错version `GLIBC\_2.34' not found直接修复，它虽然使用了 container 的方式，但是生成的 Workflow 不能运行，Copilot 多次尝试始终没有搞定。后续提示 Copilot，在 Workflow 使用 Dockerfile 的方式，Dockerfile base 基于 Centos7 编译，最终编译的 JDK25 可以在生产环境中运行。

并且因为需要在多个 Commit 二分查找具体哪个 Commit 引入导致的 Bug，编译的 JDK 需要带上 Commit id 方便跟踪，接着提了个需求，GitHub Copilot 快速了实现此功能。

GitHub Agents

![](https://mmecoa.qpic.cn/sz_mmecoa_png/h6WFQibcNiae6s4kIWoNt2n4tLYic7g8ptCMEcWzdEVjgrnibcW9q6DUOxOrMfl7c20KCdiaLkHwUplcRaY682iabZYbCC66EicYXCMGoVv0OeKDdE/640?wx_fmt=png&from=appmsg)

实现的编译 JDK 的 Workflow，支持 fork 的 JDK repo（方便修改 JDK 的代码进行测试），支持指定 commit id（方便定位具体哪个 commit 导致的问题）。

![](https://mmecoa.qpic.cn/mmecoa_png/h6WFQibcNiae7N022yvA39Xa7cxAqNRsvX3ib3rlnbkPTMTeDDhFuZiarVnKLWCPoJxRtYibMUru1O98kqxWojJS5Lw7Ars1cDAiaJ6DEkm1uACiao/640?wx_fmt=png&from=appmsg)

Build JDK，java -version，有对应的 commit id

```
$ ./bin/java -versionopenjdk version "25-internal" 2025-09-16OpenJDK Runtime Environment (build 25-internal-86cec4e)OpenJDK 64-Bit Server VM (build 25-internal-86cec4e, mixed mode, sharing)
```

通过上述方案，编译不同的 commit id 的 JDK，最终锁定是如下的 feature 引入的 bug：

* 8343782: G1: Use one G1CardSet instance for multiple old gen regions
* <https://bugs.openjdk.org/browse/JDK-8343782>
* Fix Version/s: 25
* Resolved In Build:b10

JDK-8343782 对应的 commit id 是 86cec4ea，基于此 commit id 编译的 JDK25 可以偶尔复现此问题，而它的前一个 commit id 为 006ed5c0 无问题。

汇总排查结论如下：

|  |  |  |
| --- | --- | --- |
| Configuration | Data Corruption? | Notes |
| JDK 25 + -XX:+UseG1GC | YES ✗ | Compressed data is corrupted |
| JDK 25 + -XX:+Us...