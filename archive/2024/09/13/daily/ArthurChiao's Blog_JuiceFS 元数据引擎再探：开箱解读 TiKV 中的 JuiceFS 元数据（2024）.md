---
title: JuiceFS 元数据引擎再探：开箱解读 TiKV 中的 JuiceFS 元数据（2024）
url: https://arthurchiao.github.io/blog/juicefs-metadata-deep-dive-2-zh/
source: ArthurChiao's Blog
date: 2024-09-13
fetch_date: 2025-10-06T18:25:30.291143
---

# JuiceFS 元数据引擎再探：开箱解读 TiKV 中的 JuiceFS 元数据（2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# JuiceFS 元数据引擎再探：开箱解读 TiKV 中的 JuiceFS 元数据（2024）

Published at 2024-09-12 | Last Update 2024-09-12

![](/assets/img/juicefs-metadata-deep-dive/juicefs-volume-bw-control.png)

Fig. JuiceFS upload/download data bandwidth control.

* [JuiceFS 元数据引擎初探：高层架构、引擎选型、读写工作流（2024）](/blog/juicefs-metadata-deep-dive-1-zh/)
* [JuiceFS 元数据引擎再探：开箱解读 TiKV 中的 JuiceFS 元数据（2024）](/blog/juicefs-metadata-deep-dive-2-zh/)
* [JuiceFS 元数据引擎三探：从实践中学习 TiKV 的 MVCC 和 GC（2024）](/blog/juicefs-metadata-deep-dive-3-zh/)
* [JuiceFS 元数据引擎四探：元数据大小评估、限流与限速的设计思考（2024）](/blog/juicefs-metadata-deep-dive-4-zh/)
* [JuiceFS 元数据引擎五探：元数据备份与恢复（2024）](/blog/juicefs-metadata-deep-dive-5-zh/)

水平及维护精力所限，文中不免存在错误或过时之处，请酌情参考。
**传播知识，尊重劳动，年满十八周岁，转载请注明[出处](https://arthurchiao.art)**。

---

* [1 创建一个 volume](#1-创建一个-volume)
  + [1.1 JuiceFS client 日志](#11-juicefs-client-日志)
  + [1.2 JuiceFS client 中的 `TiKV/PD client` 初始化/调用栈](#12-juicefs-client-中的-tikvpd-client-初始化调用栈)
  + [1.3 `tikv-ctl` 查看空 volume 的系统元数据](#13-tikv-ctl-查看空-volume-的系统元数据)
  + [1.4 例子：`tikv-ctl mvcc` 解码 volume setting 元数据](#14-例子tikv-ctl-mvcc-解码-volume-setting-元数据)
    - [1.4.1 对应 JuiceFS `Format` 结构体](#141-对应-juicefs-format-结构体)
* [2 将 volume 挂载（mount）到机器](#2-将-volume-挂载mount到机器)
  + [2.1 JuiceFS client 挂载日志](#21-juicefs-client-挂载日志)
  + [2.2 查看挂载信息](#22-查看挂载信息)
  + [2.3 查看 JuiceFS 隐藏（系统）文件](#23-查看-juicefs-隐藏系统文件)
    - [2.3.1 `.accesslog`](#231-accesslog)
    - [2.3.2 `.config`](#232-config)
    - [2.3.3 `.stats`](#233-stats)
    - [2.3.4 `.trash`](#234-trash)
* [3 创建、更新、删除文件](#3-创建更新删除文件)
  + [3.1 创建文件](#31-创建文件)
    - [3.1.1 创建文件](#311-创建文件)
    - [3.1.2 JuiceFS `.accesslog`](#312-juicefs-accesslog)
    - [3.1.3 TiKV 元数据](#313-tikv-元数据)
  + [3.2 删除文件操作](#32-删除文件操作)
    - [3.2.1 删除文件](#321-删除文件)
    - [3.2.2 JuiceFS `.accesslog`](#322-juicefs-accesslog)
    - [3.2.3 TiKV 元数据](#323-tikv-元数据)
  + [3.3 更新（追加）文件](#33-更新追加文件)
    - [3.3.1 更新文件](#331-更新文件)
    - [3.3.2 JuiceFS `.accesslog`](#332-juicefs-accesslog)
    - [3.3.3 TiKV 元数据](#333-tikv-元数据)
* [4 元数据操作和 TiKV key/value 编码规则](#4-元数据操作和-tikv-keyvalue-编码规则)
  + [4.1 JuiceFS key 编码规则](#41-juicefs-key-编码规则)
    - [4.1.1 每个 key 的公共前缀：`<vol_name> + 0xFD`](#411-每个-key-的公共前缀vol_name--0xfd)
    - [4.1.2 每个 key 后面的部分](#412-每个-key-后面的部分)
    - [4.1.3 最终格式：字节序列](#413-最终格式字节序列)
  + [4.2 TiKV 对 JuiceFS key 的进一步编码](#42-tikv-对-juicefs-key-的进一步编码)
  + [4.3 例子：查看特殊元数据：volume 的 setting/format 信息](#43-例子查看特殊元数据volume-的-settingformat-信息)
* [5 总结](#5-总结)
* [参考资料](#参考资料)

---

有了第一篇的铺垫，本文直接进入正题。

* 首先创建一个 volume，然后在其中做一些文件操作，然后通过 tikv-ctl 等工具在 TiKV 中查看对应的元数据。
* 有了这些基础，我们再讨论 JuiceFS metadata key 和 TiKV 的编码格式。

> 之前有一篇类似的，开箱解读 etcd 中的 Cilium 元数据：
> [What’s inside Cilium Etcd (kvstore)](/blog/whats-inside-cilium-etcd/)。

# 1 创建一个 volume

创建一个名为 `foo-dev` 的 JuiceFS volume。

## 1.1 JuiceFS client 日志

用 juicefs client 的 **`juicefs format`** 命令创建 volume，

```
$ juicefs format --storage oss --bucket <bucket> --access-key <key> --secret-key <secret key> \
  tikv://192.168.1.1:2379,192.168.1.2:2379,192.168.1.3:2379/foo-dev foo-dev

<INFO>: Meta address: tikv://192.168.1.1:2379,192.168.1.2:2379,192.168.1.3:2379/foo-dev
<INFO>: Data use oss://xxx/foo-dev/
<INFO>: Volume is formatted as {
  "Name": "foo-dev",
  "UUID": "ec843b",
  "Storage": "oss",
  "BlockSize": 4096,
  "MetaVersion": 1,
  "UploadLimit": 0,
  "DownloadLimit": 0,
  ...
}
```

* 对象存储用的是阿里云 OSS；
* TiKV 地址指向的是 **PD 集群地址**，上一篇已经介绍过，`2379` 是 PD 接收客户端请求的端口；

## 1.2 JuiceFS client 中的 `TiKV/PD client` 初始化/调用栈

下面我们进入 JuiceFS 代码，看看 JuiceFS client 初始化和**连接到元数据引擎**的调用栈：

```
mount
 |-metaCli = meta.NewClient
 |-txnkv.NewClient(url)                                          // github.com/juicedata/juicefs: pkg/meta/tkv_tikv.go
 |  |-NewClient                                                  // github.com/tikv/client-go:    txnkv/client.go
 |     |-pd.NewClient                                            // github.com/tikv/client-go:    tikv/kv.go
 |     |    |-NewClient                                          // github.com/tikv/pd:           client/client.go
 |     |       |-NewClientWithContext                            // github.com/tikv/pd:           client/client.go
 |     |          |-createClientWithKeyspace                     // github.com/tikv/pd:           client/client.go
 |     |             |-c.pdSvcDiscovery = newPDServiceDiscovery  // github.com/tikv/pd:           client/pd_xx.go
 |     |             |-c.setup()                                 // github.com/tikv/pd:           client/pd_xx.go
 |     |                 |-c.pdSvcDiscovery.Init()
 |     |                 |-c.pdSvcDiscovery.AddServingURLSwitchedCallback
 |     |                 |-c.createTokenDispatcher()
 |     |-spkv, err := tikv.NewEtcdSafePointKV
 |     |-tikv.NewRPCClient
 |     |-tikv.NewKVStore(uuid, pdClient, spkv, rpcClient)        // github.com/tikv/client-go:    tikv/kv.go
 |         |-oracles.NewPdOracle
 |         |-store := &KVStore{}
 |         |-go store.runSafePointChecker()
 |         |     |-check key "/tidb/store/gcworker/saved_safe_point" from etcd every 10s
 |         |-go store.safeTSUpdater()
 |-metaCli.NewSession
    |-doNewSession
       |-m.setValue(m.sessionKey(m.sid), m.expireTime())  // SE
       |-m.setValue(m.sessionInfoKey(m.sid), sinfo)       // SI
```

这里面连接到 TiKV/PD 的代码有点绕，

* 传给 `juicefs` client 的是 **PD 集群地址**，
* 但代码使用的是 **tikv 的 client-go 包**，创建的是一个 **`tikv transaction client`**，
* 这个 tikv transaction client 里面会去创建 **`pd client`** 连接到 PD 集群，

所以，**架构上看 juicefs 是直连 PD**，但实现上**并没有直接创建 pd client**，
也没有直接使用 pd 的库。

![](/assets/img/juicefs-metadata-deep-dive/juicefs-tikv-cluster.png)

Fig. JuiceFS cluster initialization, and how POSIX file operations are handled by JuiceFS.

## 1.3 `tikv-ctl` 查看空 volume 的系统元数据

现在再把目光转到 TiKV。看看这个空的 volume 在 TiKV 中对应哪些元数据：

```
$ ./tikv-ctl.sh scan --from 'zfoo' --to 'zfop'
key: zfoo-dev\375\377A\001\000\000\000\000\000\000\377\000I\000\000\000\000\000\000\371  # attr?
key: zfoo-dev\375\377ClastCle\377anupSess\377ions\000\000\000\000\373                    # lastCleanupSessions
key: zfoo-dev\375\377CnextChu\377nk\000\000\000\000\000\000\371                          # nextChunk
key: zfoo-dev\375\377CnextIno\377de\000\000\000\000\000\000\371                          # nextInode
key: zfoo-dev\375\377CnextSes\377sion\000\000\000\000\373                                # nextSession
key: zfoo-dev\375\377SE\000\000\000\000\000\000\377\000\001\000\000\000\000\000\000\371  # session
key: zfoo-dev\375\377SI\000\000\000\000\000\000\377\000\001\000\000\000\000\000\000\371  # sessionInfo
key: zfoo-dev\375\377setting\000\376                                                     # setting
```

以上就是我们新建的 volume `foo-dev` 的所有 entry 了。
也就是说一个 volume 创建出来之后，默认就有这些 **JuiceFS 系统元数据**。

TiKV 中的**每个 key 都经过了两层编码**（JuiceFS 和 TiKV），我们后面再介绍编码规则。
就目前来说，根据 **key 中的字符**还是依稀能看出每个 **key 是干啥用的**，
为方便起见直接注释在上面每行的最后了。比如，下面两个 session 相关的 entry 就是上面调用栈最后两个创建的：

* `session`
* `sessionInfo`

## 1.4 例子：`tikv-ctl mvcc` 解码 volume setting 元数据

TiKV 中的每个 entry 都是 key/value。现在我们尝试解码最后一个 entry，key 是
**`zfoo-dev\375\377setting\000\376`**，
我们**来看看它的 value —— 也就是它的内容 —— 是什么**：

```
$ value_hex=$(./tikv-ctl.sh mvcc -k 'zfoo-dev\375\377setting\000\376' --show-cf=default | awk '/default cf value:/ {print $NF}')
$ value_escaped=$(./tikv-ctl.sh --to-escaped $value_hex)
$ echo -e $value_escaped | sed 's/\\"/"/g' | jq .
```

输出：

```
{
  "Name": "foo-dev",
  "UUID": "1ce2973b",
  "Storage": "S3",
  "Bucket": "http://xx/bucket",
  "AccessKey": "xx",
  "SecretKey": "xx",
  "BlockSize": 4096,
  "MetaVersion": 1,
  "UploadLimit": 0,
  "DownloadLimit": 0,
  ...
}
```

可以看到是个 JSON 结构体。这其实就是这个 volume 的配置信息。如果对 JuiceFS 代码有一定了解，
就会看出来它对应的其实就是 `type Format` 这个 struct。

### 1.4.1 对应 JuiceFS `Format` 结构体

```
// https://github.com/juicedata/juicefs/blob/v1.2.0/pkg/meta/config.go#L72

typ...