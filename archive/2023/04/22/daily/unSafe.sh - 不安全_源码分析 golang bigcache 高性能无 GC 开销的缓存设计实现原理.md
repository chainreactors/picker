---
title: 源码分析 golang bigcache 高性能无 GC 开销的缓存设计实现原理
url: https://buaq.net/go-159856.html
source: unSafe.sh - 不安全
date: 2023-04-22
fetch_date: 2025-10-04T11:32:22.384625
---

# 源码分析 golang bigcache 高性能无 GC 开销的缓存设计实现原理

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

![](https://8aqnet.cdn.bcebos.com/c2a29702daf3e4eb93937d61579c28dc.jpg)

源码分析 golang bigcache 高性能无 GC 开销的缓存设计实现原理

bigcache 是 golang 编写的高性能的缓存库，其设计很巧妙，通过数据分片解决高并发下锁竞争的问题，通过把数据存到 ringbuffer 来规避 golang
*2023-4-21 22:0:37
Author: [xiaorui.cc(查看原文)](/jump-159856.htm)
阅读量:26
收藏*

---

`bigcache` 是 golang 编写的高性能的缓存库，其设计很巧妙，通过数据分片解决高并发下锁竞争的问题，通过把数据存到 ringbuffer 来规避 golang gc 的开销。

bigcache 内部使用分片来存储数据，每个分片内又使用 hashmap 存储key 的索引，而真正的数据通过编码后放在 ringbuffer 里。bigcache 没有使用主流的 lru 和 lfu 缓存淘汰算法，而是使用覆盖写来覆盖老数据，在 ringbuffer 已满时，先删除老数据，再尝试插入新数据。另外还通过 gc 垃圾回收期删掉过期的数据。

由于 bigcache 里数据是存在 `[]byte` 类型的 ringbuffer 里，所以传入的 value 只能 `[]byte`，不能存储其他类型。这样应用场景很是受限，毕竟业务上缓存的对象较为复杂，如果每次存取都需要序列化和反序列化，那么在一定量级下 CPU 开销会很可观。

> bigcache 的实现原理跟 freecache、fastcache 大同小异，都使用了 ringbuffer 存放数据，可以很大程度降低 GC 的开销。这里的 ringbuffer 当然可以使用有名或匿名的 mmap 来构建，俗称堆外内存，但对于 golang gc 来说，mmap 和直接申请 `[]byte` 的 gc 开销没大区别。如果使用文件 mmap 映射，当系统一直有文件读写，势必会对 page cache 进行 page 淘汰，这样基于 mmap 构建的 ringbuffer，必然会受之影响。

## bigcache 高级用法

```
import (
    "log"
    "fmt"

    "github.com/allegro/bigcache/v3"
)

func main() {
    config := bigcache.Config {
            // 预设多少个数据分片，其大小必须是 2 的幂次方，因为这里使用位运算取摸，而非使用 %.
            Shards: 1024,

            // 缓存对象的生命周期，也就是过期时长
            LifeWindow: 10 * time.Minute,

            // 垃圾回收的运行周期，每隔 5 分钟尝试进行一次垃圾回收.
            CleanWindow: 5 * time.Minute,

            // rps * lifeWindow, used only in initial memory allocation
            MaxEntriesInWindow: 1000 * 10 * 60,

            // 设定的 value 的大小
            MaxEntrySize: 500,

            // bigcache 缓存的大小，单位是 MB.
            // 注意这是总大小，每个分片的大小则需要除以分片数，当为 0 时不限制。
            HardMaxCacheSize: 8192,
    }

    // 构建 bigcache 缓存对象
    cache, initErr := bigcache.New(context.Background(), config)
    if initErr != nil {
        log.Fatal(initErr)
    }

    // 写数据
    cache.Set("my-unique-key", []byte("value"))

    // 读数据
    if entry, err := cache.Get("my-unique-key"); err == nil {
        fmt.Println(string(entry))
    }
}
```

## bigcache 实现原理

这里简述下 bigcache 读写数据实现原理，写操作是把数据写到 ringbuffer 里，然后在 hashmap 里记录 key 和 ringbuffer 索引的关系，读取的时候，自然是从 hashmap 里获取 key 的 ringbuffer index 索引值，然后从 ringbuffer 获取数据。

### bigcache 中数据结构及布局

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202304/202304051153942.png)

`BigCache` 数据结构.

```
type BigCache struct {
    // 数据分片
    shards     []*cacheShard

    // 缓存对象的生存时长, 也就是 ttl
    lifeWindow uint64

    // 时钟对象
    clock      clock

    // bigcahe 只实现了 fnv hash 算法
    hash       Hasher
    config     Config

    // 用来实现取摸位运算
    shardMask  uint64
    close      chan struct{}
}
```

`cacheShard` 数据分片的结构.

```
type cacheShard struct {
    // key 为 key hashcode, value 为 ringbuffer 的 offset
    hashmap     map[uint64]uint32

    // 使用 ringbuffer 构建的队列
    entries     queue.BytesQueue
    lock        sync.RWMutex

    // 对象复用
    entryBuffer []byte

    // 删除的回调方法
    onRemove    onRemoveCallback

    // 缓存对象的生存时长, 也就是 ttl
    lifeWindow   uint64
}
```

数据在 ringbuffer 中的编码.

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202304/202304051206330.png)

### 取摸算法

关于取摸的计算, 想来大家可以一般使用 `x%len` 公式，但这个性能相对低效，而像 `java jdk` 和 redis 中的取模公式为 `x&(len-1)`，当 hashtable 的长度是 2 的幂的情况下，这两者是等价的。

通过汇编可以看到，`&` 的汇编为 `3mov+1and+1sub`, `%` 的汇编为 `2mov+1cdp+1idiv` 。

根据 intel asm 的文档资料，`&` 操作只需 5 个 CPU 周期，而 `%` 最少需要 20 个 CPU 周期，显而易见，如果在意性能我们应该使用前者。

### Set 写流程

`Set` 用来添加数据到指定的 shard 分片里。bigcache 预设了 1024 个分片，社区中高性能的 cache 库会实现分片的方法来解决锁竞争的问题。

```
// Set saves entry under the key
func (c *BigCache) Set(key string, entry []byte) error {
    // 通过 fnv hash 算法计算出 key 的 hashcode
    hashedKey := c.hash.Sum64(key)

    // 通过位运算得出 key 对应的 shard 分片
    shard := c.getShard(hashedKey)

    // 在 shard 里添加数据
    return shard.set(key, hashedKey, entry)
}
```

`set` 用来把数据写到 shard 的 ringbuffer 里，并设置 hashmap 索引，其流程如下。

1. 获取当前的秒级别的时间戳，这里抽象了 clock 方法，只要是为了方便的后面的单元测试 ;
2. 在 hashmap 里获取 key 以前的 ringbuffer 的 index 位置信息，如果不为 0，且在 ringbuffer 又可拿到该 entry，则进行删除 ;
3. 编码待写入 ringbuffer 里的结构 ;
4. 尝试把编码的数据写到 ringbuffer 里，如果空间小于 max 值，则会扩容，当无法扩容时，写入失败，说明无空闲空间，则尝试剔除最老的数据，然后再进行写入。

```
func (s *cacheShard) set(key string, hashedKey uint64, entry []byte) error {
    // 获取当前的秒级别的时间戳，这里抽象了 clock 方法，只要是为了方便的后面的单元测试.
    currentTimestamp := uint64(s.clock.Epoch())

    // 加锁，并发安全
    s.lock.Lock()

    // 在 hashmap 里获取 key 以前的 ringbuffer 的 index 位置信息.
    if previousIndex := s.hashmap[hashedKey]; previousIndex != 0 {
        // 如果不为 0，且在 ringbuffer 又可拿到该 entry，则进行删除
        if previousEntry, err := s.entries.Get(int(previousIndex)); err == nil {
            resetKeyFromEntry(previousEntry)
            delete(s.hashmap, hashedKey)
        }
    }

    // 编码待写入 ringbuffer 里的结构
    w := wrapEntry(currentTimestamp, hashedKey, key, entry, &s.entryBuffer)

    for {
        // 尝试把编码的数据写到 ringbuffer 里.
        if index, err := s.entries.Push(w); err == nil {
            // 如果成功写入，更新 hashmap 索引后，放锁返回.
            s.hashmap[hashedKey] = uint32(index)
            s.lock.Unlock()
            return nil
        }

        // 写入失败说明, 无空间，则尝试剔除最老的数据，然后再进行写入.
        if s.removeOldestEntry(NoSpace) != nil {
            s.lock.Unlock()
            return fmt.Errorf("entry is bigger than max shard size")
        }
    }
}
```

`removeOldestEntry` 在过期扫描部分再分析其实现.

#### resetKeyFromEntry 把 entry 中 hashcode 置为 0.

entry 的 [8:16] 字节存储了数据的 key hashcode，通过 `resetKeyFromEntry` 方法则可以把 hashcode 置为 0.

```
func resetKeyFromEntry(data []byte) {
    binary.LittleEndian.PutUint64(data[timestampSizeInBytes:], 0)
}
```

#### 对数据进行编码

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202304/202304051322303.png)

把要写到 []byte ringbuffer 的数据进行编码。

* 第一个字段为 8 字节，表明时间戳
* 第二个字段为 8 字节，是用 fnv(key) 拿到的 hashcode
* 第三个子弹为 2 字节，表明 key length

GC 垃圾回收通过时间戳来判断是否过期，通过 iterator 遍历缓存数据时，会过滤掉 hashcode 为 0 的数据，当delete 删除数据时，会重置 hashcode 为 0。通过 key length 拿到 key。

那么如何拿到 key 的 value ? 这是因为存到 ringbuffer 时，还会加一个总大小的 length。那么获取 value 的方法显而易见了。

```
const (
    timestampSizeInBytes = 8                                                       // Number of bytes used for timestamp
    hashSizeInBytes      = 8                                                       // Number of bytes used for hash
    keySizeInBytes       = 2                                                       // Number of bytes used for size of entry key
    headersSizeInBytes   = timestampSizeInBytes + hashSizeInBytes + keySizeInBytes // Number of bytes used for all headers
)

func wrapEntry(timestamp uint64, hash uint64, key string, entry []byte, buffer *[]byte) []byte {
    keyLength := len(key)
    blobLength := len(entry) + headersSizeInBytes + keyLength

    if blobLength > len(*buffer) {
        *buffer = make([]byte, blobLength)
    }
    blob := *buffer

    binary.LittleEndian.PutUint64(blob, timestamp)
    binary.LittleEndian.PutUint64(blob[timestampSizeInBytes:], hash)
    binary.LittleEndian.PutUint16(blob[timestampSizeInBytes+hashSizeInBytes:], uint16(keyLength))
    copy(blob[headersSizeInBytes:], key)
    copy(blob[headersSizeInBytes+keyLength:], entry)

    return blob[:blobLength]
}
```

#### ringbuffer 写时扩容

第一种库容的场景.

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202304/202304051929082.png)

第二种库容的场景.

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202304/202304051930272.png)

**ringbuffer 扩容代码**

```
func (q *BytesQueue) Push(data []byte) (int, error) {
    // 计算出 size
    neededSize := getNeededSize(len(data))

    // 如果没有足够空间插入
    if !q.canInsertAfterTail(neededSize) {
        // 回绕
        if q.canInsertBeforeHead(neededSize) {
            q.tail = leftMarginIndex
        } else if q.capacity+neededSize >= q.maxCapacity &&...