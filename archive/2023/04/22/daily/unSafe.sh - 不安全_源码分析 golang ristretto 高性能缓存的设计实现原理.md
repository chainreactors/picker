---
title: 源码分析 golang ristretto 高性能缓存的设计实现原理
url: https://buaq.net/go-159857.html
source: unSafe.sh - 不安全
date: 2023-04-22
fetch_date: 2025-10-04T11:32:23.237862
---

# 源码分析 golang ristretto 高性能缓存的设计实现原理

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/d1717919e4e6f90fd09daf5044d42917.jpg)

源码分析 golang ristretto 高性能缓存的设计实现原理

ristretto 是 golang 社区里排头部的高性能的数据缓存库，支持键值过期和 LFU 缓存淘汰，还支持最大的内存空间限制，根据写时传入 cost 计算已使用的
*2023-4-21 21:58:47
Author: [xiaorui.cc(查看原文)](/jump-159857.htm)
阅读量:26
收藏*

---

ristretto 是 golang 社区里排头部的高性能的数据缓存库，支持键值过期和 LFU 缓存淘汰，还支持最大的内存空间限制，根据写时传入 cost 计算已使用的内存值，通常 cost 为对象的 size，但也可以当个数使用。其他缓存库多按照条数进行限制，不合理使用时容易造成 OOM 的风险。

其相比 freecache、bigcache 来说，存储 value 可以为任意值 interface{}。而 freecache、bigcache 内部通过一个大的 ringbuffer 来存放 value，而 value 需要是 []byte 字节数组，该设计对于 golang gc 很友好，但应用上受限，读写的时候需要对进行编码解码，这个开销不低的。

ristretto 在混合读写压测场景下，其吞吐表现要比其他 go cahce 库要好，当然压测的 case 通常是偏向自己的，懂的自然懂。

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202304/202304021219763.png)

**ristretto 使用方法**

```
func main() {
    cache, err := ristretto.NewCache(&ristretto.Config{
        NumCounters: 1e7,     // number of keys to track frequency of (10M).
        MaxCost:     1 << 30, // maximum cost of cache (1GB).
        BufferItems: 64,      // number of keys per Get buffer.
    })
    if err != nil {
        panic(err)
    }

    // 写数据，cost 为 1.
    cache.Set("key", "value", 1)

    // 由于 ristretto 是异步写，所以需要等待协程消费处理完.
    cache.Wait()

    // 获取数据
    value, found := cache.Get("key")
    if !found {
        panic("missing value")
    }
    fmt.Println(value)

    // 删除数据
    cache.Del("key")
}
```

**ristretto 项目地址:**

## ristretto 设计原理

`ristretto` 的 kv 存储使用分片map来实现的，而缓存淘汰则使用 tinyLFU 实现。

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202304/202304021250524.png)

### ristretto store 的结构

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202304/202304012015179.png)

`ristretto` 设计了一个长度为 256 的分片集合，该结构类型为 `shardedMap`，其每个分片里有一个存数据的 map 和独立的锁，其目的是为了减少锁竞争，提高读写性能。增删改查的时候，通过对 key 进行取摸定位数据在哪一个 shard 分片上。

`shardedMap` 内部使用 `expirationMap` 来存键值过期数据的，所有分片共用一个 `expirationMap` 对象，`ristretto` 没有使用分片来构建过期数据集。

```
// 最大的分片数量，常量不能改.
const numShards uint64 = 256

type shardedMap struct {
    shards    []*lockedMap
    expiryMap *expirationMap
}

func newShardedMap() *shardedMap {
    sm := &shardedMap{
        shards:    make([]*lockedMap, int(numShards)),
        expiryMap: newExpirationMap(),
    }
    for i := range sm.shards {
        sm.shards[i] = newLockedMap(sm.expiryMap)
    }
    return sm
}

type lockedMap struct {
    sync.RWMutex
    data map[uint64]storeItem // 该 map 的 key 为数据key的哈希值.
    em   *expirationMap
}

type expirationMap struct {
    sync.RWMutex
    buckets map[int64]bucket // 该 map 的 key 过期时间的索引值，计算方法为 `ts/5 + 1`
}

// key 为键值 key 的 hash 值，value 为 conflict 值，是另一个 hash 值.
type bucket map[uint64]uint64
```

`shardedMap` 里不存储真正的 key 值，而是存储数据 key 两个 hash 值，为什么使用两个 hash 值标记对象，为了避免概率上的冲突，所以另使用另一个 xxhash 算法计算 hash 值，该值在 ristretto 定义为 conflict 哈希值。

`KeyToHash` 是 ristretto 默认的 hash 方法，传入的 key 不能是指针类型，也不能是 struct。返回值为两个 hash 值，其内部的 `MemHash` 其实是 `runtime.memhash` 映射的方法，golang 内部的 map 也使用该 hash 算法。xxhash 则为社区中较为火热的 hash 库。

```
func KeyToHash(key interface{}) (uint64, uint64) {
    if key == nil {
        return 0, 0
    }
    switch k := key.(type) {
    case uint64:
        return k, 0
    case string:
        return MemHashString(k), xxhash.Sum64String(k)
    case []byte:
        return MemHash(k), xxhash.Sum64(k)
    case byte:
        return uint64(k), 0
    case int:
        return uint64(k), 0
    case int32:
        return uint64(k), 0
    case uint32:
        return uint64(k), 0
    case int64:
        return uint64(k), 0
    default:
        panic("Key type not supported")
    }
}
```

### ristretto 缓存驱逐策略

社区中常常使用 LRU 和 LFU 算法来实现缓存淘汰驱逐，ristretto 则使用 LFU 算法，但由于 LFU 标准实现开销过大，则使用 TinyLFU 实现数据淘汰。

TinyLFU 里主要使用 `count-min sketch` 统计算法粗略记录各个 key 的缓存命中计数。该 `count-min Sketch` 算法通常用在不要求精确计数，又想节省内存的场景，虽然拿到的计数缺失一定的精准度，但确实节省了内存。

但就 ristretto 缓存场景来说，记录 100w 个 key 的计数也才占用 11MB 左右，公式是 ( 100 \* 10000 ) \* (8 + 4) / 1024/ 1024 = 11MB，这里的 8 为 key hash 的大小，而 4 为 hit 的类型 uint32 大小。

#### count-min sketch 统计算法实现

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202304/202304012218253.png)

count-min sketch 中的 increment 和 estimate 方法实现原理很简单，流程如下。

1. 选定 d 个 hash 函数，开一个 dm 的二维整数数组作为哈希表 ;
2. 对于每个元素，分别使用d个hash函数计算相应的哈希值，并对m取余，然后在对应的位置上增1，二维数组中的每个整数称为sketch ;
3. 要查询某个元素的频率时，只需要取出d个sketch, 返回最小的那一个。

ristretto 对 count-min sketch 并不是一直累计累加的，在 policy 累计对象超过 resetAt 时，则会对 cm-sketch 统计对象进行重置。不然一直递增，缓存淘汰场景下，对于新对象很不友好。

#### policy 数据结构的设计

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202304/202304021251549.png)

```
type defaultPolicy struct {
    sync.Mutex
    admit    *tinyLFU // 实现了 tinyLFU 淘汰算法.
    evict    *sampledLFU // 记录最大 cost，已使用 cost，及 key 对应的 cost 值.

    // 异步的维护缓存淘汰策略.
    itemsCh  chan []uint64
    stop     chan struct{}
    isClosed bool
    metrics  *Metrics
}

type sampledLFU struct {
    maxCost  int64 // 最大 cost 阈值
    used     int64 // 已使用 cost 值
    metrics  *Metrics // 指标
    keyCosts map[uint64]int64 // key 为数据的 key hash，value 为对应的 cost 值.
}

type tinyLFU struct {
    freq    *cmSketch // count min sketch
    door    *z.Bloom  // bloomfilter
    incrs   int64
    resetAt int64
}
```

#### policy tinylfu

policy 在实例化是除了实例化 defaultPolicy 对象，还会启动一个协程运行 `processItems` 方法，该方法用来监听 cache 传递的增删改事件，在 tinylfu count-min-sketch 里做记录，超过一定阈值后会重置，其目的为了避免老的 lfu freq 越来越大，不容易被淘汰掉。

```
func newDefaultPolicy(numCounters, maxCost int64) *defaultPolicy {
    p := &defaultPolicy{
        admit:   newTinyLFU(numCounters),
        evict:   newSampledLFU(maxCost),
        itemsCh: make(chan []uint64, 3),
        stop:    make(chan struct{}),
    }
    go p.processItems()
    return p
}

func (p *defaultPolicy) processItems() {
    for {
        select {
        case items := <-p.itemsCh:
            p.Lock()
            p.admit.Push(items)
            p.Unlock()
        case <-p.stop:
            return
        }
    }
}

func (p *tinyLFU) Push(keys []uint64) {
    for _, key := range keys {
        p.Increment(key)
    }
}

func (p *tinyLFU) Increment(key uint64) {
    // Flip doorkeeper bit if not already done.
    if added := p.door.AddIfNotHas(key); !added {
        // Increment count-min counter if doorkeeper bit is already set.
        p.freq.Increment(key)
    }
    p.incrs++
    if p.incrs >= p.resetAt {
        p.reset()
    }
}
```

#### 写时缓存淘汰驱逐

`ristretto` 没有实现后台协程主动淘汰驱逐的逻辑，而是采用了写时淘汰驱逐，每次写数据时，判断是否有足够的 cost 插入数据。如果不足，则进行驱逐。采样驱逐的方法有点类似 redis 的方案，每次从 simpleLFU 里获取 5 个 key，然后遍历计算这 5 个 key 的命中率，淘汰掉命中率最低的 key，然后再判断是否有空闲 cost 写入，不足继续采样淘汰，知道满足当前 key 的写入。

命中率是通过 tinyLFU 来计算的，由于该实现是通过 count-min sketch 算法实现，所以计算出的缓存命中数会产生些偏差。

```
func (p *defaultPolicy) Add(key uint64, cost int64) ([]*Item, bool) {
    p.Lock()
    defer p.Unlock()

    // 添加的 cost 不能超过总 cost 阈值.
    if cost > p.evict.getMaxCost() {
        return nil, false
    }

    // 如果 simpleLfu 里有 key 值，则更新 cost 值.
    if has := p.evict.updateIfHas(key, cost); has {
        return nil, false
    }

    // 如果 key 在 simpleLFU 不存在，则走下面的逻辑.
    // 计算减去 cost 后还剩多少可用的 cost.
    room := p.evict.roomLeft(cost)
    if room >= 0 {
        // 如果足够 cost 开销，则更新 lfu 内指标.
        p.evict.add(key, cost)
        // 这里的 nil 代表，没有需要淘汰的数据，true 代表可以插入.
        return nil, true
    }

    incHits := p.admit.Estimate(key)

    // 构建一个可以放 5 条采样数据的集合
    sample := make([]*policyPair, 0, lfuSample)

    // 需要删除的 key
    victims := make([]*Item, 0)

    // 尝试淘汰数据，直到有空余的 cost.
    for ; room < 0; room = p.evict.roomLeft(cost) {
        // 采样获取 5 条 key，并填满 sample 数组.
        sample = p.evict.fillSample(sample)

        // 在取样集合里获取中最少被使用的 key，也就是缓存命中率最低的 key.
        minKey, minHits, minId, minCost := uint64(0), int64(math.MaxInt64), 0, int64(0)
        for i, pair :=...