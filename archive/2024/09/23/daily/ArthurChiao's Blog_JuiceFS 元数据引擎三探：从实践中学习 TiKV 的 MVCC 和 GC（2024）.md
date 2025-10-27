---
title: JuiceFS 元数据引擎三探：从实践中学习 TiKV 的 MVCC 和 GC（2024）
url: https://arthurchiao.github.io/blog/juicefs-metadata-deep-dive-3-zh/
source: ArthurChiao's Blog
date: 2024-09-23
fetch_date: 2025-10-06T18:20:06.775399
---

# JuiceFS 元数据引擎三探：从实践中学习 TiKV 的 MVCC 和 GC（2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# JuiceFS 元数据引擎三探：从实践中学习 TiKV 的 MVCC 和 GC（2024）

Published at 2024-09-22 | Last Update 2024-10-10

![](/assets/img/juicefs-metadata-deep-dive/tikv-mvcc-gc-mechanisms.png)

Fig. TiKV MVCC GC mechanisms.

* [JuiceFS 元数据引擎初探：高层架构、引擎选型、读写工作流（2024）](/blog/juicefs-metadata-deep-dive-1-zh/)
* [JuiceFS 元数据引擎再探：开箱解读 TiKV 中的 JuiceFS 元数据（2024）](/blog/juicefs-metadata-deep-dive-2-zh/)
* [JuiceFS 元数据引擎三探：从实践中学习 TiKV 的 MVCC 和 GC（2024）](/blog/juicefs-metadata-deep-dive-3-zh/)
* [JuiceFS 元数据引擎四探：元数据大小评估、限流与限速的设计思考（2024）](/blog/juicefs-metadata-deep-dive-4-zh/)
* [JuiceFS 元数据引擎五探：元数据备份与恢复（2024）](/blog/juicefs-metadata-deep-dive-5-zh/)

水平及维护精力所限，文中不免存在错误或过时之处，请酌情参考。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

---

* [1 概念与实测](#1-概念与实测)
  + [1.1 MVCC（多版本并发控制）](#11-mvcc多版本并发控制)
    - [1.1.2 TiKV MVCC 测试](#112-tikv-mvcc-测试)
    - [1.1.2 JuiceFS client 日志](#112-juicefs-client-日志)
    - [1.1.3 小结](#113-小结)
  + [1.2 GC（垃圾回收）](#12-gc垃圾回收)
  + [1.3 Safepoint（可安全删除这个时间戳之前的版本）](#13-safepoint可安全删除这个时间戳之前的版本)
* [2 TiKV MVCC GC](#2-tikv-mvcc-gc)
  + [2.1 历史：从 TiDB 里面拆分出来，功能不完整](#21-历史从-tidb-里面拆分出来功能不完整)
  + [2.2 TiKV GC 设计和配置项](#22-tikv-gc-设计和配置项)
    - [2.2.1 设计：两种 GC 触发方式](#221-设计两种-gc-触发方式)
    - [2.2.2 `tikv-server` 启动日志中的 GC 配置信息](#222-tikv-server-启动日志中的-gc-配置信息)
    - [2.2.3 `tikv-ctl compact/compact-cluster` 触发被动 GC 例子](#223-tikv-ctl-compactcompact-cluster-触发被动-gc-例子)
    - [2.2.4 小结](#224-小结)
  + [2.3 TiDB 中触发 TiKV GC 的方式](#23-tidb-中触发-tikv-gc-的方式)
  + [2.4 JuiceFS 触发 TiKV GC 的方式](#24-juicefs-触发-tikv-gc-的方式)
    - [2.4.1 定期更新 `gc safepoint` 的代码](#241-定期更新-gc-safepoint-的代码)
    - [2.4.2 配置：META URL `\?gc-interval=1h`](#242-配置meta-url-gc-interval1h)
    - [2.4.3 `juicefs gc` 手动触发 TiKV GC](#243-juicefs-gc-手动触发-tikv-gc)
  + [2.5 外挂组件 `github.com/tikv/migration/gc-worker`](#25-外挂组件-githubcomtikvmigrationgc-worker)
* [3 GC 不及时导致的问题一例](#3-gc-不及时导致的问题一例)
  + [3.1 问题现象](#31-问题现象)
    - [3.1.1 监控：TiKV db size 暴增，磁盘空间不断减小](#311-监控tikv-db-size-暴增磁盘空间不断减小)
    - [3.1.2 `tikv-server` 错误日志：failed to split region](#312-tikv-server-错误日志failed-to-split-region)
  + [3.2 问题排查](#32-问题排查)
  + [3.3 问题根因](#33-问题根因)
  + [3.4 解决方式](#34-解决方式)
  + [3.5 问题小结](#35-问题小结)
* [4 问题讨论](#4-问题讨论)
  + [4.1 允许的**最小 GC 间隔**太大](#41-允许的最小-gc-间隔太大)
  + [4.2 GC 配置放在客户端，增加了用户的认知负担和学习成本](#42-gc-配置放在客户端增加了用户的认知负担和学习成本)
  + [4.3 管理员运维困境](#43-管理员运维困境)
  + [4.4 小结](#44-小结)
* [参考资料](#参考资料)

---

# 1 概念与实测

## 1.1 MVCC（多版本并发控制）

来自 [wikipedia 的定义](https://en.wikipedia.org/wiki/Multiversion_concurrency_control)，

> Multiversion concurrency control (MCC or MVCC), is a **`non-locking`** concurrency
> control method commonly used by database management systems to provide
> **`concurrent access`** to the database and in programming languages to implement
> **`transactional`** memory.

TiKV 支持 MVCC，当更新数据时，旧的数据不会被立即删掉，而是新老同时保留，以时间戳来区分版本。
官方有几篇很不错的博客 [1,3]。

下面进行一个简单测试来对 MVCC 有一个初步的直观认识。

### 1.1.2 TiKV MVCC 测试

参考上一篇，新创建一个新 volume，里面什么文件都没有，有 **8 条记录**，

```
$ tikv-ctl.sh scan --from 'zfoo' --to 'zfop' | grep "key:" | wc -l
8
```

然后进入这个 volume 的挂载目录，在里面**创建一个文件**，

```
$ cd <mount dir>
$ echo 1 > foo.txt
```

再次扫描这个 volume 对应的所有 keys，

```
$ tikv-ctl.sh scan --from 'zfoo' --to 'zfop' | grep "key:" | wc -l
16
```

可以看到变成 16 条记录，比之前**多了 8 条**。内容如下，依稀能看出大部分条目的用途
（**行末的注释**是本文加的），

```
key: zfoo-dev\375\377A\001\000\000\000\000\000\000\377\000Dfoo.tx\377t\000\000\000\000\000\000\000\370 # foo.txt
key: zfoo-dev\375\377A\002\000\000\000\000\000\000\377\000C\000\000\000\000\000\000\375
key: zfoo-dev\375\377A\002\000\000\000\000\000\000\377\000I\000\000\000\000\000\000\371
key: zfoo-dev\375\377ClastCle\377anupFile\377s\000\000\000\000\000\000\000\370                         # lastCleanupFile
key: zfoo-dev\375\377ClastCle\377anupSess\377ions\000\000\000\000\373                                  # lastCleanupSessions
key: zfoo-dev\375\377CtotalIn\377odes\000\000\000\000\373                                              # totalInodes
key: zfoo-dev\375\377CusedSpa\377ce\000\000\000\000\000\000\371                                        # UsedSpace
key: zfoo-dev\375\377U\001\000\000\000\000\000\000\377\000\000\000\000\000\000\000\000\370
```

接下来继续**更新这个文件 1000 次**（每次都是一个整数，由于文件内容极小，不会导致 TiKV 的 region split 等行为），

```
$ for n in {1..1000}; do echo $n > bar.txt; done
```

再次查看元数据条目数量：

```
$ tikv-ctl.sh scan --from 'zfoo' --to 'zfop' | grep key | wc -l
59
```

又**多了 43 条**。多的条目大致长这样：

```
key: zfoo-dev\375\377L\000\000\000\000f\356\221\377\231\000\000\000\000\000\000\000\3777\000\000\000\000\000\000\000\370
key: zfoo-dev\375\377L\000\000\000\000f\356\221\377\233\000\000\000\000\000\000\000\377j\000\000\000\000\000\000\000\370
key: zfoo-dev\375\377L\000\000\000\000f\356\221\377\234\000\000\000\000\000\000\000\377\235\000\000\000\000\000\000\000\370
...
key: zfoo-dev\375\377L\000\000\000\000f\356\221\377\271\000\000\000\000\000\000\003\377\362\000\000\000\000\000\000\000\370
```

> TiKV supports MVCC, which means that there can be multiple versions for the
> same row stored in RocksDB. **`All versions of the same row share the same prefix`**
> (the row key) but have **`different timestamps as a suffix`**.
>
> https://tikv.org/deep-dive/key-value-engine/rocksdb/

下面我们再看看执行以上文件更新操作期间，juicefs 客户端的日志。

### 1.1.2 JuiceFS client 日志

在执行以上 for 循环期间，JuiceFS client 的日志，

```
$ juicefs mount ...
...
<DEBUG>: PUT chunks/0/0/170_0_4 (req_id: "xx", err: <nil>, cost: 32.002516ms) [cached_store.go:669]
<DEBUG>: PUT chunks/0/0/171_0_4 (req_id: "xx", err: <nil>, cost: 32.002516ms) [cached_store.go:669]
<DEBUG>: PUT chunks/0/0/172_0_4 (req_id: "xx", err: <nil>, cost: 32.002516ms) [cached_store.go:669]
...
```

这个似乎对应的就是以上多出来的条目。

### 1.1.3 小结

本节的例子让我们看到，虽然 volume 里面**从头到尾只有一个文件**，
但随着我们不断覆盖这个文件内的值，元数据引擎 **TiKV 内的条目数量就会持续增加**。
多出来的这些东西，对应的就是这份数据的多个版本，也就是 MVCC 里面 **`multi-version`** 的表现。

显然，没有冲突的话，只保留最后一个版本就行了，**其他版本都可以删掉** —— 这就是**垃圾回收（GC）**的作用。

## 1.2 GC（垃圾回收）

垃圾回收 (GC) 的功能是清理 MVCC 留下的旧版本。比如同一份数据保存了 1000 个版本，那原则上前面大部分版本都可以清掉了，只保留最新的一个或几个。

那如何判断哪些版本可以**安全**地清掉呢？TiKV 引入了一个时间戳概念：
**`safepoint`**。

> GC is a process to clean up garbage versions (versions older than the configured lifetime) of each row.
>
> https://tikv.org/deep-dive/key-value-engine/rocksdb/

## 1.3 Safepoint（可安全删除这个时间戳之前的版本）

> In order to ensure the correctness of all read and write transactions, and make
> sure the GC mechanism works, TiKV/TiDB introduced the concept of safe-point.
> There is a guarantee that
> **`all active transactions and future transactions’ timestamp is greater than or equal to the safe-point`**.
> It means **`old versions whose commit-ts is less than the safe-point can be safely deleted`** by GC. [3]

# 2 TiKV MVCC GC

以上看到，TiKV 有 GC 功能，但由于其“历史出身”，也存在一些限制。

## 2.1 历史：从 TiDB 里面拆分出来，功能不完整

TiKV 是从 TiDB 里面拆出来的一个产品，并不是从一开始就作为独立产品设计和开发的。
这导致的一个问题是：MVCC GC 功能在使用上有点蹩脚：

1. 默认情况下，靠底层 RocksDB 的 compaction 触发 GC，这周触发周期不确定且一般比较长；
2. TiKV+PD 也内置了另一种 GC 方式，但并不会自己主动去做，而是将 GC 接口暴露出来，**靠 TiDB 等在使用 TiKV 的更上层组件来触发**（见下节的图）；
3. `tikv-ctl/pd-ctl` 等等命令行工具也都**没有提供 GC 功能**，这导致 TiKV 的运维很不方便，比如有问题想快速手动触发时用不了。

下面具体看看 TiKV 中的 GC 设计。

## 2.2 TiKV GC 设计和配置项

![](/assets/img/juicefs-metadata-deep-dive/tikv-mvcc-gc-mechanisms.png)

Fig. TiKV MVCC GC mechanisms.

### 2.2.1 设计：两种 GC 触发方式

1. **被动 GC**：TiKV 底层的 RocksDB compact 时进行垃圾回收。
   * 通过 tikv-server 的 [enable-compaction-filter](https://github.com/tikv/tikv/blob/v8.3.0/etc/config-template.toml#L1351) 配置项控制；
   * **默认启用**；
   * 触发 RocksDB compaction 时才能进行 GC。
   * **`tikv-ctl compact/compact-cluster`** 可以手动触发这种 compact，进而 GC。
2. **半主动 GC**：内置了 GC worker，
   * 定期获取 PD 里面的 gc safepoint，然后进行 GC；会占用一些 CPU/IO 资源；
   * PD 不会主动更新这个 gc safepoint，一般是由**在使用 TiKV 的更外围组件**来更新的，例如 TiDB、JuiceFS 等等；
   * 所以本文把这种方式称为“半主动”。

### 2.2.2 `tikv-server` 启动日志中的 GC 配置信息

`tikv-server.log`，

```
[INFO] [server.rs:274] ["using config"] [config="{..., "enabl...