---
title: JuiceFS 元数据引擎四探：元数据大小评估、限流与限速的设计思考（2024）
url: https://arthurchiao.github.io/blog/juicefs-metadata-deep-dive-4-zh/
source: ArthurChiao's Blog
date: 2024-09-23
fetch_date: 2025-10-06T18:20:04.081946
---

# JuiceFS 元数据引擎四探：元数据大小评估、限流与限速的设计思考（2024）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (中文)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# JuiceFS 元数据引擎四探：元数据大小评估、限流与限速的设计思考（2024）

Published at 2024-09-22 | Last Update 2024-09-22

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

* [1 元数据存储在哪儿？文件名到 TiKV regions 的映射](#1-元数据存储在哪儿文件名到-tikv-regions-的映射)
  + [1.1 `pd-ctl region` 列出所有 region 信息](#11-pd-ctl-region-列出所有-region-信息)
  + [1.2 `tikv-ctl region-properties` 查看 region 属性详情](#12-tikv-ctl-region-properties-查看-region-属性详情)
  + [1.3 `tikv-ctl --to-escaped`：从 region 的 start/end key 解码文件名范围](#13-tikv-ctl---to-escaped从-region-的-startend-key-解码文件名范围)
  + [1.4 `filename -> region`：相关代码](#14-filename---region相关代码)
* [2 JuiceFS 集群规模与元数据大小（engine size）](#2-juicefs-集群规模与元数据大小engine-size)
  + [2.1 二者的关系](#21-二者的关系)
    - [2.1.1 文件数量 & 平均文件大小](#211-文件数量--平均文件大小)
    - [2.1.2 MVCC GC 快慢](#212-mvcc-gc-快慢)
  + [2.2 两个集群对比](#22-两个集群对比)
* [3 限速（上传/下载数据带宽）设计](#3-限速上传下载数据带宽设计)
  + [3.1 带宽限制：`--upload-limit/--download-limit`](#31-带宽限制--upload-limit--download-limit)
  + [3.2 JuiceFS 限速行为](#32-juicefs-限速行为)
  + [3.3 JuiceFS client reload 配置的调用栈](#33-juicefs-client-reload-配置的调用栈)
* [4 限流（metadata 请求）设计](#4-限流metadata-请求设计)
  + [4.1 为什么需要限流？](#41-为什么需要限流)
  + [4.2 打爆 TiKV API 的几种场景](#42-打爆-tikv-api-的几种场景)
    - [4.2.1 `mlocate (updatedb)` 等扫盘工具](#421-mlocate-updatedb-等扫盘工具)
      * [一次故障复盘](#一次故障复盘)
      * [`juicefs mount` 时会自动禁用 mlocate，但 CSI 部署方式中部分失效](#juicefs-mount-时会自动禁用-mlocate但-csi-部署方式中部分失效)
    - [4.2.2 版本控制工具](#422-版本控制工具)
  + [4.3 需求：对元数据引擎的保护能力](#43-需求对元数据引擎的保护能力)
    - [4.3.1 现状：JuiceFS 目前还没有](#431-现状juicefs-目前还没有)
  + [4.4 客户端限流方案设计](#44-客户端限流方案设计)
  + [4.5 服务端限流方案设计](#45-服务端限流方案设计)
* [参考资料](#参考资料)

---

# 1 元数据存储在哪儿？文件名到 TiKV regions 的映射

## 1.1 `pd-ctl region` 列出所有 region 信息

```
$ pd-ctl.sh region | jq .
{
  "regions": [
    {
      "id": 11501,
      "start_key": "6161616161616161FF2D61692D6661742DFF6261636B7570FD41FFCF68030000000000FF4900000000000000F8",
      "end_key": "...",
      "epoch": {
        "conf_ver": 23,
        "version": 300
      },
      "peers": [
        {
          "id": 19038,
          "store_id": 19001,
          "role_name": "Voter"
        },
        ...
      ],
      "leader": {
        "id": 20070,
        "store_id": 20001,
        "role_name": "Voter"
      },
      "written_bytes": 0,
      "read_bytes": 0,
      "written_keys": 0,
      "read_keys": 0,
      "approximate_size": 104,
      "approximate_keys": 994812
    },
  ]
}
```

## 1.2 `tikv-ctl region-properties` 查看 region 属性详情

```
$ ./tikv-ctl.sh region-properties -r 23293
mvcc.min_ts: 438155461254971396
mvcc.max_ts: 452403302095650819
mvcc.num_rows: 1972540
mvcc.num_puts: 3697509
mvcc.num_deletes: 834889
mvcc.num_versions: 4532503
mvcc.max_row_versions: 54738
num_entries: 4549844
num_deletes: 17341
num_files: 6
sst_files: 001857.sst, 001856.sst, 002222.sst, 002201.sst, 002238.sst, 002233.sst
region.start_key: 6e6772...
region.end_key: 6e6772...
region.middle_key_by_approximate_size: 6e6772...
```

## 1.3 `tikv-ctl --to-escaped`：从 region 的 start/end key 解码文件名范围

如上，每个 region 都会有 **`start_key/end_key`** 两个属性，
这里面编码的就是这个 region 内存放是元数据的 key 范围。我们挑一个来解码看看：

```
$ tikv-ctl.sh --to-escaped '6161616161616161FF2D61692D6661742DFF6261636B7570FD41FFCF68030000000000FF4900000000000000F8'
aaaaaaaa\377-ai-fat-\377backup\375A\377\317h\003\000\000\000\000\000\377I\000\000\000\000\000\000\000\370
```

再 decode 一把会更清楚：

```
$ tikv-ctl.sh --decode 'aaaaaaaa\377-ai-fat-\377backup\375A\377\317h\003\000\000\000\000\000\377I\000\000\000\000\000\000\000\370'
aaaaaaaa-ai-fat-backup\375A\317h\003\000\000\000\000\000I
```

对应的是一个名为 **`aaaaaaa-ai-fat-backup`** 的 volume 内的一部分元数据。

## 1.4 `filename -> region`：相关代码

这里看一下从文件名映射到 TiKV region 的代码。

PD 客户端代码，

```
    // GetRegion gets a region and its leader Peer from PD by key.
    // The region may expire after split. Caller is responsible for caching and
    // taking care of region change.
    // Also, it may return nil if PD finds no Region for the key temporarily,
    // client should retry later.
    GetRegion(ctx , key []byte, opts ...GetRegionOption) (*Region, error)

// GetRegion implements the RPCClient interface.
func (c *client) GetRegion(ctx , key []byte, opts ...GetRegionOption) (*Region, error) {
    options := &GetRegionOp{}
    for _, opt := range opts {
        opt(options)
    }
    req := &pdpb.GetRegionRequest{
        Header:      c.requestHeader(),
        RegionKey:   key,
        NeedBuckets: options.needBuckets,
    }
    serviceClient, cctx := c.getRegionAPIClientAndContext(ctx, options.allowFollowerHandle && c.option.getEnableFollowerHandle())
    resp := pdpb.NewPDClient(serviceClient.GetClientConn()).GetRegion(cctx, req)
    return handleRegionResponse(resp), nil
}
```

PD 服务端代码，

```
func (h *regionHandler) GetRegion(w http.ResponseWriter, r *http.Request) {
    rc := getCluster(r)
    vars := mux.Vars(r)
    key := url.QueryUnescape(vars["key"])
    // decode hex if query has params with hex format
    paramsByte := [][]byte{[]byte(key)}
    paramsByte = apiutil.ParseHexKeys(r.URL.Query().Get("format"), paramsByte)

    regionInfo := rc.GetRegionByKey(paramsByte[0])
    b := response.MarshalRegionInfoJSON(r.Context(), regionInfo)

    h.rd.Data(w, http.StatusOK, b)
}

// GetRegionByKey searches RegionInfo from regionTree
func (r *RegionsInfo) GetRegionByKey(regionKey []byte) *RegionInfo {
    region := r.tree.search(regionKey)
    if region == nil {
        return nil
    }
    return r.getRegionLocked(region.GetID())
}
```

返回的是 region info，

```
// RegionInfo records detail region info for api usage.
// NOTE: This type is exported by HTTP API. Please pay more attention when modifying it.
// easyjson:json
type RegionInfo struct {
    ID          uint64              `json:"id"`
    StartKey    string              `json:"start_key"`
    EndKey      string              `json:"end_key"`
    RegionEpoch *metapb.RegionEpoch `json:"epoch,omitempty"`
    Peers       []MetaPeer          `json:"peers,omitempty"` // https://github.com/pingcap/kvproto/blob/master/pkg/metapb/metapb.pb.go#L734

    Leader            MetaPeer      `json:"leader,omitempty"`
    DownPeers         []PDPeerStats `json:"down_peers,omitempty"`
    PendingPeers      []MetaPeer    `json:"pending_peers,omitempty"`
    CPUUsage          uint64        `json:"cpu_usage"`
    WrittenBytes      uint64        `json:"written_bytes"`
    ReadBytes         uint64        `json:"read_bytes"`
    WrittenKeys       uint64        `json:"written_keys"`
    ReadKeys          uint64        `json:"read_keys"`
    ApproximateSize   int64         `json:"approximate_size"`
    ApproximateKeys   int64         `json:"approximate_keys"`
    ApproximateKvSize int64         `json:"approximate_kv_size"`
    Buckets           []string      `json:"buckets,omitempty"`

    ReplicationStatus *ReplicationStatus `json:"replication_status,omitempty"`
}

// GetRegionFromMember implements the RPCClient interface.
func (c *client) GetRegionFromMember(ctx , key []byte, memberURLs []string, _ ...GetRegionOption) (*Region, error) {
    for _, url := range memberURLs {
        conn := c.pdSvcDiscovery.GetOrCreateGRPCConn(url)
        cc := pdpb.NewPDClient(conn)
        resp = cc.GetRegion(ctx, &pdpb.GetRegionRequest{
            Header:   ...