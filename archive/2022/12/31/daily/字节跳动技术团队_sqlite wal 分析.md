---
title: sqlite wal 分析
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247500931&idx=1&sn=d53f68403d9a53a7f71bfe60e66eeca8&chksm=e9d30f61dea48677a53222b59ebe20707beb49e2e5ce9012c288fda7daf4cbe4951045c162a6&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2022-12-31
fetch_date: 2025-10-04T02:48:15.630528
---

# sqlite wal 分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOiabQ31eu8QVHgJvf2EX3EfNicQLOqOZefkaafSc1nTA4xGmHPPUG1NPWVUcAvbZ0zuHYUEGqx4H3UA/0?wx_fmt=jpeg)

# sqlite wal 分析

原创

FD

字节跳动技术团队

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

sqlite 提供了一种 redo log 型事务实现，支持读写的并发，见 write-ahead log（https://sqlite.org/wal.html）。本文将介绍 wal 原理，并源码剖析 checkpoint 过程，同时讨论下 wal 使用中的一些注意点。由于 sqlite 的复杂性，会省略掉一些细节，重点放在核心流程和 wal 并发的实现。

# 1. wal 原理

## 1.1 redo log

sqlite wal 是一种简单的 redo log 事务实现，redo log 概念这里简述下。**数据库事务需要满足满足 acid，其中原子性(a)，即一次事务内的多个修改，要么全部提交成功要么全部提交失败，不存在部分提交到 db 的情况。** redo log 的解决思路是将修改后的日志按序先写入 log 文件(wal 文件)，每个完成的事务会添加 checksum，可鉴别事务的完整性。事务写入日志文件后，即代表提交成功，读取时日志和 db 文件合并的结果构成了 db 的完整内容。同时定期 checkpoint，同步 wal 中的事务到 db 文件，使 wal 文件保持在合理的大小。日志文件持久化到磁盘后，已提交成功的事务按序 checkpoint 执行的结果都是一样的，**不受 crash 和掉电的影响。**

sqlite 的 wal 也是这种思路的实现，**只是 sqlite 提供的是一种简化实现，同时只允许一个写者操作日志文件，日志也是 page 这种物理日志。redo log 还能将 undo log 的随机写转化为顺序写，具有更高的写入性能，**这里不赘述。

想对 redo log 进一步了解，可以参考以下资料：

https://zhuanlan.zhihu.com/p/35574452

https://developer.aliyun.com/article/1009683

## 1.2 sqlite wal

sqlite wal 写操作不直接写入 db 主文件，而是写到“db-wal”文件（以下简称'wal'文件）的末尾。读操作时，将结合 db 主文件以及 wal 的内容返回结果。**wal 模式同时具有简单的 mvvc 实现，支持文件级别的读写并发，提供了相对 delete(rollback) 模式 (undo log 事务) 更高的并发性。** 具体可看图加深理解。

下图中：

1. pgx.y，x 表示当前 page 的 num，y 表示当前 page 的版本，每个提交的事务都保存当前修改后的 page 副本；
2. 图中 wal 中提交了两个事务，wal 中**蓝色框表示一个完整事务**修改的所有 page；
3. **wal 实际中保存的单位是 wal frame，除了修改的页面还会保存 page number checksum 等信息，这里为了突出展示了 page，** 详细格式见：https://www.sqlite.org/fileformat2.html

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiabQ31eu8QVHgJvf2EX3EfN3uibX87W0WupvH5ic1xBccsZLaibsyvkovPcaEplcnricnf5W1tT2EFDDA/640?wx_fmt=png)

关于写

1. 写操作总是发生在 wal 文件上；
2. 写操作总是追加在 wal 文件末尾，由 commit 触发；
3. 写入 wal 文件中是原始 page 修改后的副本；
4. 写操作对 wal 文件的访问是独占串行的；
5. 事务写入只有成功落盘（写入磁盘)才算成功提交，checkpoint 前会调用 wal 文件的 fsync，保证日志提交持久性和一致性；
6. 没有调用 fsync 不代表日志提交一定失败，会由文件系统定期回写；
7. 如果 fsync 回写之前发生 crash 或系统崩溃，导致事务 2 的 pg4.2 写 wal 失败，可校验出事务 2 不完整，则 wal 中成功提交的事务只有事务 1; 如果 pg0.1 回写失败，则 wal 中没有成功提交的事务。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiabQ31eu8QVHgJvf2EX3EfNlVOz0IDk3wbwmUy4A5BHTNBDfz6PCPB0ltfA0ZdVvdHwicL7wU4yuQg/640?wx_fmt=png)关于读

1. 读与写可以并发；
2. 每个读事务会记录 wal 文件中一个 record 点，作为它的 read mark，每个事务执行过程中 read mark 不会发生改变，新提交的事务产生的修改不会影响旧的事务。read mark 会选择事务完整提交后的位置。原始 db 文件和 wal 中 read mark 之前的记录构成了数据库的一个固定的版本记录；
3. 读事务读一个 page 优先读 wal 文件，没有则读原始文件；
4. 如果一个 page 在 wal 中有多个副本，读 read mark 前的最后一个；
5. 同一个 read mark 可以被多个读事务使用。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiabQ31eu8QVHgJvf2EX3EfNiaZ4ibs9MNfyrvv0eOQg9cqib2IicOT9Xo56lNP4Yq320KSribZ8KOOuic2Q/640?wx_fmt=png)

关于 checkpoint:

1. checkpoint 针对 wal 中已经成功落盘的事务，每次 checkpoint 前会执行 fsync；
2. 每次 checkpoint 从前到后按序回写 wal 文件中尚未提交的事务到 db；
3. 如果 checkpoint 中途 crash，由于事务已持久化到 wal 文件，下次启动重新按序回写 wal 中的事务即可；
4. wal 中所有的事务 checkpoint 后，wal 文件会从头开始使用；
5. checkpoint 并不一定都会提交 wal 中全部的事务，如果只是部分提交，下次写入还是会写入 wal 文件的末尾，wal 文件可能会变很大；
6. 只有 truncate 的 checkpoint 才能清理已经异常变大的 wal 文件，会 truncate 文件大小到 0。

2. wal 实现

wal 的实现大部分代码集中在 wal.c 中，从 sqlite 的架构划分应该主要算是 pager 层的实现。

https://www.sqlite.org/arch.html。wal 实现从逻辑上由 3 部分组成：

## 2.1 wal 和 wal-index 文件格式

文件格式定义，官方文档见：

https://www.sqlite.org/walformat.html

https://www.sqlite.org/fileformat2.html

这一层细节比较多，主要是些二进制定义。**核心是 wal 格式提供了一种 page 格式的 redo log 组织格式，保证 crash 后 recover 过程满足一致性。**

wal-index 文件(db-shm)只是一种对 wal 文件的快速索引，后文为了省事，也统称 wal 文件。

## 2.2 文件多副本抽象

即 wal 和 db 文件对外表现为一个统一的文件抽象，并提供文件级别的 mvcc，对 pager 层屏蔽 wal 细节。

由于 wal 和 db 一样都是以 pgno 的方式索引 page，按 pgno 替换就可以构造出不同版本的 b 树，比较简单。**mvcc 主要通过 read lock 的 read mark 实现，前面有介绍过，** 后面并发控制部分会详细举例介绍。

具体实现可看：

写入：https://github.com/sqlite/sqlite/blob/version-3.15.2/src/pager.c#L3077

读取：https://github.com/sqlite/sqlite/blob/version-3.15.2/src/wal.c#L2593

## 2.3 并发控制

通过文件锁保证并发操作不会损坏数据库文件，下一节详细讲解。

# 3. wal 下的并发

**wal 支持读读、读写的并发，相比最初的 rollback journal 模式提供了更大的并发力度。**但 wal 实现的是文件级别的并发，没有 mysql 表锁行锁的概念，一个 db 文件同时的并发写事务同时只能存在一个，不支持写的同时并发。checkpoint 也可能会 block 读写。

wal 并发实现上主要通过**文件锁，和文件级别 mvcc 来实现文件级别的读写并发。** 锁即下文源码中的 WAL\_CKPT\_LOCK，WAL\_WRITE\_LOCK 和WAL\_READ\_LOCK，出于简化问题考虑省略了 WAL\_RECOVER\_LOCK 等相关性不大的其他锁的讨论。mvcc 即通过文件多副本和 read mark 实现，后文也会详细介绍。

## 3.1 锁的分类和作用

官方介绍：https://www.sqlite.org/walformat.html

可看 ***2.3.1节 How the various locks are used***

也可看下面简化分析：

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiaskTAswqC0qG26Q2dj3PkVq1Alvoic64Oebib3WSVzc5YT6gSjSmBGP8ZXMEpzic7A1iaf9ehxRC80Yw/640?wx_fmt=png)

## 3.2 锁的持有情况

数据库的访问，可以分为 3 类：读、写和checkpoint。事务对锁的持有不总是在事务一开始就持有，后文为了简化分析，会假设读写事务对锁的持有在事务开始时是已知的，并且与事务同生命周期。**实际在读事务某些执行路径上也可能会持有 write lock，这里专注主线逻辑。**

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiabQ31eu8QVHgJvf2EX3EfNXkXZW9DlCN0dibejiauaiagHBR2aLlicAWNCJHX0F2F53x48XjEr62tnCg/640?wx_fmt=png)

## 3.3 锁的应用

**这部分可以和源码分析部分参照起来看，是整个 wal 里面相对复杂的部分，重点，需要来回反复看。**

commit transaction：表示已经提交但没有 checkpoint 的事务，蓝框中表示事务修改的页面。

ongoing transition : 表示正在进行中的事务，同时也表示一个活跃的数据库连接，蓝线表示 read mark 的位置。

pgx.y: 表示 page 的页号和版本。

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiabQ31eu8QVHgJvf2EX3EfNJcoTXerwkOtCia4Bic27LRonwCiamfrKaLrNng4J55MqibSccXxjTL24Lg/640?wx_fmt=png)

### 3.3.1 读写

如图可知：

1. wal文件存在 4 个已经提交的事务

   第一个事务修改了 page0，第二个事务修改了 page0、1、3，依此类推。
2. 当前数据库上存在 4 个活跃的连接，包括 3 个读事务和 1 个写事务；
3. 写事务独占了 WAL\_WRITE\_LOCK，所以此时不能再发起一个写事务；
4. 写事务占有 1（4）读锁，**所以写事务读取不到 read mark 4 之后的修改，只能读取 read mark 4 之前的修改。即写事务读取 page4 时不能读取到 page4.3，只能读取 page4.0；**
5. 3 个读事务占有 0（0），1（4），2（5）三个读锁，**read mark 只能在事务结束的位置，不会处于中间 page 的位置；**
6. 后续如果发起一个读事务，会占有读锁 3（7）。理论上可以发起任意多个读请求，读锁可以被 sqlite 连接共享。

### 3.3.2 checkpoint

**这部分要和源码分析结合，**如果此时发起 checkpoint。

1. 由于事务 0 持有 read lock 0，read mark 0，计算 mxSafeFrame 为 0，不会发生 checkpoint。

   如果事务 0 结束后发起 checkpoint。
2. 由于写事务存在，不能发起非 passive 的 checkpoint。

   如果事务 1 结束后执行 checkpoint。
3. 计算 mxSafeFrame 等于 4，会提交前 4 个 page，没有完全提交，wal 文件不会重新利用，新的写入还是会写入 commit transaction3 之后。

   如果所有事务结束后执行 checkpoint。
4. 提交所有页面，下次写入 wal 文件头部。

# 4. checkpoint 源码分析

源码对应 sqlite 3.15.2，通过直接调用 checkpoint 观察整个过程。

https://github.com/sqlite/sqlite/tree/version-3.15.2/src

## 4.1 调用链路

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOiabQ31eu8QVHgJvf2EX3EfNL8DJZVE92KQy3k8Fe7c5vLZxevP7WZVXKcVTiaciaY9MyIaxk1RwAX6g/640?wx_fmt=png)

## 4.2 sqlite3\_wal\_checkpoint\_v2

https://github.com/sqlite/sqlite/blob/version-3.15.2/src/main.c#L2065

主要是加锁和一些参数校验。

## 4.3 sqlite3Checkpoint

https://github.com/sqlite/sqlite/blob/version-3.15.2/src/main.c#L2146

ndb 上循环 checkpoint，大多数时候只有一个 db 文件。

## 4.4 sqlite3BtreeCheckpoint

https://github.com/sqlite/sqlite/blob/version-3.15.2/src/btree.c#L9472

检查 btree 是否 locked，也是前置检查逻辑。

## 4.5 sqlite3PagerCheckpoint

https://github.com/sqlite/sqlite/blob/version-3.15.2/src/pager.c#L7198

也是前置的处理逻辑。不过有个和 checkpoint 逻辑有关的。

```
 /* 只在非SQLITE_CHECKPOINT_PASSIVE模式时设置xBusyHandler
  * 即SQLITE_CHECKPOINT_PASSIVE时如果获取不到锁，立即返回，不进行等待并retry
  */
 if( pPager->pWal ){
    rc = sqlite3WalCheckpoint(pPager->pWal, db, eMode,
        (eMode==SQLITE_CHECKPOINT_PASSIVE ? 0 : pPager->xBusyHandler),
        pPager->pBusyHandlerArg,
        pPager->walSyncFlags, pPager->pageSize, (u8 *)pPager->pTmpSpace,
        pnLog, pnCkpt
    );
  }
```

## 4.6 sqlite3WalCheckpoint

https://github.com/sqlite/sqlite/blob/version-3.15.2/src/wal.c#L3192

```
int sqlite3WalCheckpoint(
  Wal *pWal,                      /* Wal connection */
  int eMode,                      /* PASSIVE, FULL, RESTART, or TRUNCATE */
  int (*xBusy)(void*),            /* Function to call when busy */
  void *pBusyArg,                 /* Context argument for xBusyHandler */
  int sync_flags,                 /* Flags to sync db file with (or 0) */
  int nBuf,                       /* Size of temporary buffer */
  u8 *zBuf,                       /* Temporary buffer to use */
  int *pnLog,                     /* OUT: Number of frames in WAL */
  int *pnCkpt                     /* OUT: Number of backfilled frames in WAL */
){
  int rc;                         /* Return code */
  int is...