---
title: JuiceFS 元数据引擎初探：高层架构、引擎选型、读写工作流（2024）
url: https://arthurchiao.github.io/blog/juicefs-metadata-deep-dive-1-zh/
source: ArthurChiao's Blog
date: 2024-09-13
fetch_date: 2025-10-06T18:25:40.992107
---

# JuiceFS 元数据引擎初探：高层架构、引擎选型、读写工作流（2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# JuiceFS 元数据引擎初探：高层架构、引擎选型、读写工作流（2024）

Published at 2024-09-12 | Last Update 2024-10-16

![](/assets/img/juicefs-metadata-deep-dive/juicefs-tikv-cluster.png)

Fig. JuiceFS cluster initialization, and how POSIX file operations are handled by JuiceFS.

* [JuiceFS 元数据引擎初探：高层架构、引擎选型、读写工作流（2024）](/blog/juicefs-metadata-deep-dive-1-zh/)
* [JuiceFS 元数据引擎再探：开箱解读 TiKV 中的 JuiceFS 元数据（2024）](/blog/juicefs-metadata-deep-dive-2-zh/)
* [JuiceFS 元数据引擎三探：从实践中学习 TiKV 的 MVCC 和 GC（2024）](/blog/juicefs-metadata-deep-dive-3-zh/)
* [JuiceFS 元数据引擎四探：元数据大小评估、限流与限速的设计思考（2024）](/blog/juicefs-metadata-deep-dive-4-zh/)
* [JuiceFS 元数据引擎五探：元数据备份与恢复（2024）](/blog/juicefs-metadata-deep-dive-5-zh/)

水平及维护精力所限，文中不免存在错误或过时之处，请酌情参考。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

---

* [1 JuiceFS 高层架构与组件](#1-juicefs-高层架构与组件)
  + [1.1 JuiceFS client](#11-juicefs-client)
  + [1.2 Metatdata engine（元数据引擎）](#12-metatdata-engine元数据引擎)
  + [1.3. Object store](#13-object-store)
* [2 JuiceFS 元数据存储引擎对比：`tikv vs. etcd`](#2-juicefs-元数据存储引擎对比tikv-vs-etcd)
  + [2.1 设计与优缺点对比](#21-设计与优缺点对比)
  + [2.2 几点解释](#22-几点解释)
  + [2.3 例子：TiKV 集群 engine size 和内存使用监控](#23-例子tikv-集群-engine-size-和内存使用监控)
* [3 JuiceFS + TiKV：集群启动和宏观读写流程](#3-juicefs--tikv集群启动和宏观读写流程)
  + [3.1 架构](#31-架构)
  + [3.2 TiKV 集群启动](#32-tikv-集群启动)
    - [3.2.1 TiKV & PD 配置差异](#321-tikv--pd-配置差异)
    - [3.2.2 服务启动](#322-服务启动)
  + [3.3 宏观读写流程](#33-宏观读写流程)
* [4 TiKV 内部数据初探](#4-tikv-内部数据初探)
  + [4.1 简单脚本 `tikv-ctl.sh/pd-ctl.sh`](#41-简单脚本-tikv-ctlshpd-ctlsh)
  + [4.2 `tikv-ctl scan` 扫描 key/value](#42-tikv-ctl-scan-扫描-keyvalue)
  + [4.3 `tikv-ctl mvcc` 查看给定 key 对应的 value](#43-tikv-ctl-mvcc-查看给定-key-对应的-value)
  + [4.4 `tikv-ctl --decode <key>` 解除字符转义](#44-tikv-ctl---decode-key-解除字符转义)
  + [4.5 `tikv-ctl --to-hex`：转义表示 -> 十六进制表示](#45-tikv-ctl---to-hex转义表示---十六进制表示)
  + [4.6 `tikv-ctl --to-escaped <value>`：十六进制 value -> 带转义的字符串](#46-tikv-ctl---to-escaped-value十六进制-value---带转义的字符串)
* [5 总结](#5-总结)
* [参考资料](#参考资料)

---

# 1 JuiceFS 高层架构与组件

![](/assets/img/juicefs-metadata-deep-dive/juicefs-components-1.png)

Fig. JuiceFS components and architecutre.

如图，最粗的粒度上可以分为三个组件。

## 1.1 JuiceFS client

* `juicefs format ...` 可以创建一个 volume；
* `juicefs config ...` 可以修改一个 volume 的配置；
* `juicefs mount ...` 可以把一个 volume 挂载到机器上，然后用户就可以在里面读写文件了；

## 1.2 Metatdata engine（元数据引擎）

* 用于**存储 JuiceFS 的元数据**，例如每个文件的文件名、最后修改时间等等；
* 可选择 etcd、TiKV 等等；

## 1.3. Object store

实际的对象存储，例如 S3、Ceph、阿里云 OSS 等等，存放 JuiceFS volume 内的数据。

# 2 JuiceFS 元数据存储引擎对比：`tikv vs. etcd`

## 2.1 设计与优缺点对比

|  | TiKV as metadata engine | etcd as metadata engine |
| --- | --- | --- |
| **管理节点**（e.g. leader election） | PD (TiKV cluster manager) | etcd server |
| **数据节点**（存储 juicefs metadata） | TiKV server | etcd server |
| **数据节点对等** | 无要求 | **完全对等** |
| **数据一致性粒度** | region-level (TiKV 的概念，`region < node`) | node-level |
| **Raft 粒度** | region-level (multi-raft，TiKV 的概念) | node-level |
| **缓存多少磁盘数据在内存中** | 一部分 | **所有** |
| **集群支持的最大数据量** | **`PB`** 级别 | 几十 GB 级别 |
| **性能**（JuiceFS 场景） | 高（猜测是因为 raft 粒度更细，并发读写高） | **低** |
| 维护和二次开发门槛 | 高（相比 etcd） | 低 |
| 流行度 & 社区活跃度 | 低（相比 etcd） | 高 |
| 适用场景 | **大和超大 JuiceFS 集群** | 中小 JuiceFS 集群 |

## 2.2 几点解释

etcd 集群，

* 每个节点完全对等，既负责管理又负责存储数据；
* 所有数据**全部缓存在内存中**，每个节点的数据完全一致。
  这一点限制了 etcd 集群支持的最大数据量和扩展性，
  例如现在官网还是建议不要超过 8GB（实际上较新的版本在技术上已经没有这个限制了，
  但仍受限于机器的内存）。

TiKV 方案可以可以理解成把管理和数据存储分开了，

* PD 可以理解为 **`TiKV cluster manager`**，负责 leader 选举、multi-raft、元数据到 region 的映射等等；
* 节点之间也**不要求对等**，PD 按照 region（比如 96MB）为单位，将 N（默认 3）个副本放到 N 个 TiKV node 上，而实际上 TiKV 的 node 数量是 M，`M >= N`；
* 数据放在 TiKV 节点的磁盘，内存中**只缓存一部分**（默认是用机器 45% 的内存，可控制）。

## 2.3 例子：TiKV 集群 engine size 和内存使用监控

TiKV 作为存储引擎，总结成一句话就是：**根据硬件配置干活，能者多劳** ——
内存大、磁盘大就多干活，反之就少干活。

下面的监控展示是 7 台 TiKV node 组成的一个集群，各 **node 内存不完全一致**：
3 台 256GB 的，2 台 128GB 的，2 台 64GB 的，
可以看到每个 TiKV server 确实只用了各自所在 node 一半左右的内存：

![](/assets/img/juicefs-metadata-deep-dive/tikv-engine-size.png)

Fig. TiKV engine size and memory usage of a 7-node (with various RAMs) cluster.

# 3 JuiceFS + TiKV：集群启动和宏观读写流程

## 3.1 架构

用 TiKV 作为元数据引擎，架构如下（先忽略其中的细节信息，稍后会介绍）：

![](/assets/img/juicefs-metadata-deep-dive/juicefs-tikv-cluster.png)

Fig. JuiceFS cluster initialization, and how POSIX file operations are handled by JuiceFS.

## 3.2 TiKV 集群启动

### 3.2.1 TiKV & PD 配置差异

两个组件的几个核心配置项，

```
$ cat /etc/tikv/pd-config.toml
name = "pd-node1"
data-dir = "/var/data/pd"

client-urls = "https://192.168.1.1:2379" # 客户端（例如 JuiceFS）访问 PD 时，连接这个地址
peer-urls   = "https://192.168.1.1:2380" # 其他 PD 节点访问这个 PD 时，连接这个地址，也就是集群内互相通信的地址

# 创建集群时的首批 PD
initial-cluster-token = "<anything you like>"
initial-cluster = "pd-node1=https://192.168.1.3:2380,pd-node2=https://192.168.1.2:2380,pd-node3=https://192.168.1.1:2380"
```

可以看到，**PD 的配置和 etcd 就比较类似，需要指定其他 PD 节点地址**，它们之间互相通信。

TiKV 节点（tikv-server）的配置就不一样了，

```
$ cat /etc/tikv/tikv-config.toml
[pd]
endpoints = ["https://192.168.1.1:2379", "https://192.168.1.2:2379", "https://192.168.1.3:2379"]

[server]
addr = "192.168.1.1:20160"        # 服务地址，JuiceFS client 会直接访问这个地址读写数据
status-addr = "192.168.1.1:20180" # prometheus
```

可以看到，

1. TiKV 会配置所有 PD 节点的地址，以便自己注册到 PD 作为一个数据节点（存储JuiceFS 元数据）；
2. TiKV 还会配置一个地址的 server 地址，这个读写本节点所管理的 region 内的数据用的；
   正常流程是 JuiceFS client 先访问 PD，拿到 region 和 tikv-server 信息，
   然后再到 tikv-server 来读写数据（对应 JuiceFS 的元数据）；
3. TiKV **不会配置其他 TiKV 节点的地址**，也就是说 TiKV 节点之间不会 peer-to-peer 互连。
   属于同一个 raft group 的多个 region 通信，也是先通过 PD 协调的，最后 region leader 才发送数据给 region follower。
   详见 [1]。

### 3.2.2 服务启动

![](/assets/img/juicefs-metadata-deep-dive/juicefs-tikv-cluster.png)

Fig. JuiceFS cluster initialization, and how POSIX file operations are handled by JuiceFS.

对应图中 step 1 & 2：

* step 1. PD 集群启动，选主；
* step 2. TiKV 节点启动，向 PD 注册；每个 TiKV 节点称为一个 store，也就是元数据仓库。

## 3.3 宏观读写流程

对应图中 step 3~5：

* step 3. JuiceFS 客户端连接到 PD；发出读写文件请求；

  + JuiceFS 客户端中会初始化一个 TiKV 的 transaction kv client，这里面又会初始化一个 PD client，
  + 简单来说，此时 JuiceFS 客户端就有了 PD 集群的信息，例如哪个文件对应到哪个 region，这个 region 分布在哪个 TiKV 节点上，TiKV 服务端连接地址是多少等等；
* step 4. JuiceFS （内部的 TiKV 客户端）直接向 TiKV 节点（准确说是 region leader）发起读写请求；
* step 5. 元数据处理完成，JuiceFS 客户端开始往对象存储里读写文件。

# 4 TiKV 内部数据初探

TiKV 内部存储的都是 JuiceFS 的元数据。具体来说又分为两种：

1. 用户文件的元数据：例如用户创建了一个 `foo.txt`，在 TiKV 里面就会对应一条或多条元数据来描述这个文件的信息；
2. JuiceFS 系统元数据：例如每个 volume 的配置信息，这些对用户是不可见的。

TiKV 是扁平的 KV 存储，所以以上两类文件都放在同一个扁平空间，通过 key 访问。
本文先简单通过命令看看里面的元数据长什么样，下一篇再结合具体 JuiceFS 操作来深入解读这些元数据。

## 4.1 简单脚本 `tikv-ctl.sh/pd-ctl.sh`

简单封装一下对应的命令行工具，使用更方便，

```
$ cat pd-ctl.sh
tikv-ctl \
        --ca-path /etc/tikv/pki/root.crt --cert-path /etc/tikv/pki/tikv.crt --key-path /etc/tikv/pki/tikv.key \
        --host 192.168.1.1:20160 \
        "$@"

$ cat pd-ctl.sh
pd-ctl \
        --cacert /etc/tikv/pki/root.crt --cert /etc/tikv/pki/pd.crt --key /etc/tikv/pki/pd.key \
        --pd https://192.168.1.1:2379  \
        "$@"
```

## 4.2 `tikv-ctl scan` 扫描 key/value

tikv-ctl **不支持只列出所有 keys**，所以只能 key 和 value 一起打印（扫描）。

扫描前缀是 `foo` 开头的所有 key：

```
$ ./tikv-ctl.sh scan --from 'zfoo' --to 'zfop' --limit 100
...
key: zfoo-dev\375\377A\001\000\000\000\000\000\000\377\000Dfile3.\377txt\000\000\000\000\000\372
key: zfoo-dev\375\377A\001\000\000\000\000\000\000\377\000Dfile4.\377txt\000\000\000\000\000\372
...
key: zfoo-dev\375\377setting\000\376
        default cf value: start_ts: 452330324173520898 value: 7B0A22...
```

扫描的时候一定要在 key 前面加一个 `z` 前缀，这是 TiKV 的一个[设计](https://tikv.org/docs/3.0/reference/tools/tikv-ctl/)，

> The raw-scan command scans directly from the RocksDB. Note that to scan data keys you need to add a ‘z’ prefix to keys.

代码出处 [components/keys/src/lib.rs](https://github.com/tikv/tikv/blob/v5.0.0/components/keys/src/lib.rs#L29)。
但对用户来说不是太友好，暴露了太多内部细节，没有 `etcdctl` 方便直接。

## 4.3 `tikv-ctl mvcc` 查看给定 key 对应的 value

```
$ ./tikv-ctl.sh mvcc -k 'zfoo-dev\375\377A\001\000\000\000\000\000\000\377\000Dfile1.\377txt\000\000\000\000...