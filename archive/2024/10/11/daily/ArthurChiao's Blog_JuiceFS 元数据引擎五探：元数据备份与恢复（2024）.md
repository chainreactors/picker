---
title: JuiceFS 元数据引擎五探：元数据备份与恢复（2024）
url: https://arthurchiao.github.io/blog/juicefs-metadata-deep-dive-5-zh/
source: ArthurChiao's Blog
date: 2024-10-11
fetch_date: 2025-10-06T18:46:12.564288
---

# JuiceFS 元数据引擎五探：元数据备份与恢复（2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# JuiceFS 元数据引擎五探：元数据备份与恢复（2024）

Published at 2024-10-10 | Last Update 2024-10-10

![](/assets/img/juicefs-metadata-deep-dive/br-and-tikv-backup.png)

Fig. TiKV backup with different CLI tools (and their problems).

* [JuiceFS 元数据引擎初探：高层架构、引擎选型、读写工作流（2024）](/blog/juicefs-metadata-deep-dive-1-zh/)
* [JuiceFS 元数据引擎再探：开箱解读 TiKV 中的 JuiceFS 元数据（2024）](/blog/juicefs-metadata-deep-dive-2-zh/)
* [JuiceFS 元数据引擎三探：从实践中学习 TiKV 的 MVCC 和 GC（2024）](/blog/juicefs-metadata-deep-dive-3-zh/)
* [JuiceFS 元数据引擎四探：元数据大小评估、限流与限速的设计思考（2024）](/blog/juicefs-metadata-deep-dive-4-zh/)
* [JuiceFS 元数据引擎五探：元数据备份与恢复（2024）](/blog/juicefs-metadata-deep-dive-5-zh/)

水平及维护精力所限，文中不免存在错误或过时之处，请酌情参考。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

---

* [1 JuiceFS 元数据备份方式](#1-juicefs-元数据备份方式)
* [2 JuiceFS 自带方式（volume 级别）](#2-juicefs-自带方式volume-级别)
  + [2.1 `juicefs dump` 手动备份 volume metadata](#21-juicefs-dump-手动备份-volume-metadata)
  + [2.2 `juicefs mount --backup-meta <duration>` 自动备份](#22-juicefs-mount---backup-meta-duration-自动备份)
  + [2.3 `juicefs load` 从元数据备份文件恢复](#23-juicefs-load-从元数据备份文件恢复)
  + [2.4 限制及问题](#24-限制及问题)
* [3 从 TiKV 层面对 JuiceFS 元数据进行备份](#3-从-tikv-层面对-juicefs-元数据进行备份)
  + [3.1 TiKV backup/restore 原理](#31-tikv-backuprestore-原理)
  + [3.2 备份工具 TiDB `br` 和 TiKV `tikv-br`](#32-备份工具-tidb-br-和-tikv-tikv-br)
  + [3.3 基于 TiDB `br` 对 JuiceFS TiKV 集群进行备份与恢复的步骤](#33-基于-tidb-br-对-juicefs-tikv-集群进行备份与恢复的步骤)
  + [3.4 TiDB `br` 备份逻辑](#34-tidb-br-备份逻辑)
    - [3.4.1 `RunBackupTxn()`](#341-runbackuptxn)
    - [3.4.2 调用栈](#342-调用栈)
    - [3.4.3 `tikv-server` 备份代码](#343-tikv-server-备份代码)
* [参考资料](#参考资料)

---

# 1 JuiceFS 元数据备份方式

再复习下 JuiceFS 架构，如下图所示：

![](/assets/img/juicefs-metadata-deep-dive/juicefs-tikv-cluster.png)

Fig. JuiceFS cluster initialization, and how POSIX file operations are handled by JuiceFS.

JuiceFS 的元数据都存储在**元数据引擎**（例如，TiKV）里，
因此元数据的备份有两种实现方式：

1. 从上层备份：JuiceFS client 扫描 volume，将 volume 内所有元数据备份；
2. 元数据引擎（例如 TiKV）备份。

下面分别看看这两种方式。

# 2 JuiceFS 自带方式（volume 级别）

## 2.1 `juicefs dump` 手动备份 volume metadata

对指定 volume 进行备份，

```
$ juicefs dump tikv://ip:2379/foo-dev foo-dev-dump.json
<INFO>: Meta address: tikv://<ip>:2379/foo-dev [interface.go:406]
<WARNING>: Secret key is removed for the sake of safety [tkv.go:2571]
           Scan keys count: 357806 / 357806 [===========================]  done
      Dumped entries count: 122527 / 122527 [===========================]  done
<INFO>: Dump metadata into dump succeed [dump.go:76]
```

生成的是一个 JSON 文件，包含了 volume 的所有元数据信息，

```
{  "Setting": {
    "Name": "foo-dev",
    "UUID": "ca95c258",
    "Storage": "OSS",
    "Bucket": "http://<url>",
    "AccessKey": "ak",
    "BlockSize": 4096,
    "Capacity": 0,
    "Inodes": 0,
    "MetaVersion": 0,
    "MinClientVersion": "",
    "MaxClientVersion": "",
  },
  "Counters": {
    "usedSpace": 6164512768,
    "usedInodes": 5010,
    "nextInodes": 10402,
    "nextChunk": 25001,
    "nextSession": 118,
  },
  "FSTree": {
    "attr": {"inode":1,"type":"directory","mode":511,"atime":1645791488,"mtime":1652433235,"ctime":1652433235,"mtimensec":553010494,"ctimensec":553010494,"nlink":2,"length":0},
    "xattrs": [{"name":"lastBackup","value":"2024-05-30T13:50:25+08:00"}],
    "entries": {
      "001eb8b": {
        "attr": {...},
        "chunks": [{"index":0,"slices":[{"chunkid":15931,"size":32,"len":32}]}]
        ...
      }
   }
  },
}
```

其中，volume 中的所有文件和目录信息都描述在 `FSTree` 字段中。

## 2.2 `juicefs mount --backup-meta <duration>` 自动备份

juicefs client 默认会自动备份 volume 的元数据，

* 备份间隔通过 **`--backup-meta {duration}`** 选项控制，默认 **`1h`**，
* 备份文件在对象存储的 **`meta`** 特殊目录中，该目录在挂载点中不可见，用对象存储的文件浏览器可以查看和管理，
* 多 client 挂载同一个 volume 也不会发生备份冲突，因为 JuiceFS 维护了一个全局的时间戳，确保同一时刻只有一个客户端执行备份操作，但是，
* 当文件数太多（默认达到 100w）且备份频率为默认值 `1h` 时，为避免备份开销太大，JuiceFS 会**自动停止元数据备份**，并打印相应的告警。

## 2.3 `juicefs load` 从元数据备份文件恢复

```
$ juicefs load tikv://<ip>:2379/foo-dev-new foo-dev-dump.json
```

## 2.4 限制及问题

根据[官方文档](https://juicefs.com/docs/zh/community/metadata_dump_load/)，以上两种方式都有一些限制或问题：

* 导出过程中如果业务仍在写入，导出的文件可能不可用。如果对一致性有更高要求，需要在导出前停写。
* 对规模较大的 volume，直接在线上进行导出可能会影响业务稳定性。

另外，以上方式都是 volume 级别的备份，如果要备份整个 JuiceFS 集群，需要逐个 volume 备份，比较麻烦。
下面再看看直接从元数据引擎进行备份的方式。

# 3 从 TiKV 层面对 JuiceFS 元数据进行备份

这里假设 JuiceFS 的元数据引擎是 TiKV。

## 3.1 TiKV backup/restore 原理

从上层来说，很简单：

1. 发请求给 TiKV 集群的管理者 PD，让它对集群的所有数据进行备份；
2. 接下来，PD 会发请求给集群的所有 TiKV 节点，通知它们各自进行备份

   * TiKV 是按 region 进行多副本存储的，因此只需要一个副本进行备份就行了，
   * 在当前的设计里面就是让每个 region 的 leader 副本进行备份，
3. TiKV region leaders 把这个 region 内的数据写到指定位置。可以是本地磁盘或分布式存储。

## 3.2 备份工具 TiDB `br` 和 TiKV `tikv-br`

理论上，有两个工具可能实现以上效果，它们分别来自 TiDB 和 TiKV 社区，

![](/assets/img/juicefs-metadata-deep-dive/br-and-tikv-backup.png)

Fig. TiKV backup with different CLI tools (and their problems).

1. `br`：以前是个独立项目（图中 A.1），后来合到 tidb 仓库里了（图中 B.1），

   这个工具**主要是给 TiDB 备份用的**（虽然底层备份的是 TiDB 的 TiKV），
   所以需要一些 TiDB 知识（上下文），例如 db/table 都是 TiDB 才有的概念。
   理论上，它也能备份独立部署的 TiKV 集群（**“不依赖 TiDB 的 TiKV”**），
   所以加了 raw/txn 支持，但不是 TiDB 社区的重点，所以目前还是 experimental 特性，且用下来有 bug。
2. `tikv-br`：是个独立项目，应该是当时 TiKV 作为独立项目推进时，想搞一个配套的独立备份工具，
   但目前看起来跟 TiKV 社区一样已经**不活跃了**，它也没法对 txn 进行备份（**JuiceFS 用的 txnkv 接口**）。

至少对于 5.x TiKV 集群，测试下来**以上哪个工具都无法完成备份**：
有的工具备份和恢复都提示完成，看起来是成功的，但实际上是失败的，JuiceFS 挂载时才能发现。

最后，我们是基于目前（2024.09）最新的 TiDB br，修改了两个地方，才成功完成 TiKV 的备份与恢复。

## 3.3 基于 TiDB `br` 对 JuiceFS TiKV 集群进行备份与恢复的步骤

之所以要强调 “JuiceFS TiKV 集群”，是因为 JuiceFS 用的 **`txnkv`** 接口，这个比较特殊；
如果是 rawkv 接口，那 tikv 自带的备份工具 `tikv-br` 也许就能用了（没测过）。

1. （可选）关闭 TiKV MVCC GC；
2. `br` 执行备份，

   `br-dev` 是我们基于最新 master（202409）改过的版本。

   ```
    $ ./br-dev backup txn \
            --ca /tmp/pki/root.crt --cert /tmp/pki/pd.crt --key /tmp/pki/pd.key \
            --pd https://$pd_addr \
            --s3.endpoint $s3_addr \
            --storage $storage_path \
            --log-file /var/log/tikv/br.log \
            --ratelimit $bw_limit_per_node \
            --log-level debug \
            --check-requirements=false
   ```

   可以设置限速等参数，避免备份占用的 CPU/Memory/DiskIO/… 过大。根据 db size 等等因素，**备份的耗时是可估算的**，下面拿一个真实集群的备份为例：

   * 每个 TiKV 的 **`DB size`**：监控能看到，一般每个节点的 DB size 都差不太多，这里是 25GB per TiKV node；
   * **`MVCC`** 保留了数据的多个版本：假设平均保留两个版本，那就是 DB size \* 2
   * 限速带宽：设置为 30MB/s，这个带宽不算大，不会是磁盘和网络瓶颈，因此可以全速运行

   根据以上参数，估算耗时：**`25GB * 2 / 30MBps = 1700s = 28min`**

   ![](/assets/img/juicefs-metadata-deep-dive/tikv-backup-resource-usage.png)

   Fig. TiKV backup resource usage with `br --ratelimit=30MB/s`.

   可以看到跟预估的差不多。资源销毁方面：

   * **CPU 利用率比平时翻倍**；
   * 其中两台机器的 CPU 数量比较少，所以会比其他节点更明显。
3. 检查备份

   如果是备份到 S3，可以用 `s3cmd` 或 web 控制台查看，

   ```
    $ s3cmd du s3://{bucket}/<backup>/
    295655971082   18513 objects s3://{bucket}/<backup>/
   ```

   290GB 左右，**比监控看到的 DB size 大一倍**，因为保留了 MVCC 多版本。
   大多少倍与 **`MVCC GC`** 间隔有密切关系，
   比如写或更新很频繁的场景，1h 和 3h 的 MVCC 数据量就差很多了。
4. `br` 恢复：将备份数据恢复到一个新的 JuiceFS TiKV 集群，

   ```
    $ ./br-dev restore txn \
            --ca /tmp/pki/root.crt --cert /tmp/pki/pd.crt --key /tmp/pki/pd.key \
            --pd https://$pd_addr \
            --s3.endpoint $s3_addr \
            --storage $storage_path \
            --log-file /var/log/tikv/br.log \
            --ratelimit $bw_limit_per_node \
            --log-level debug \
            --check-requirements=false
   ```

   可能的问题：ratelimit 好像不起作用，全速恢复，网络带宽打的很高。
5. JuiceFS client 挂载，验证恢复成功

   用 juicefs 挂载目录，指定新 TiKV 集群的 PD 地址，

   ```
    $ juicefs mount tikv://<new-pd-ip>:2379/<volume name> /tmp/test

    $ cd /tmp/test && ls
    # 原来 volume 内的文件都在
   ```

## 3.4 TiDB `br` 备份逻辑

感兴趣的可以看看 `br` 源码的备份逻辑，

### 3.4.1 `RunBackupTxn()`

```
// tidb br/pkg/task/backup_txn.go

// RunBackupTxn starts a backup task inside the current goroutine.
func RunBackupTxn(c context.Context, g glue.Glue, cmdName string, cfg *TxnKvConfig) error {
    mgr := NewMgr(ctx, g, cfg.PD, cfg.TLS, GetKeepalive(&cfg.Config), cfg.CheckRequirements, f...