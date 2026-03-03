---
title: Linux 内核攻击 USMA 解析
url: https://mp.weixin.qq.com/s/olkZ7SDlLIVa5k1h59otUg
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:10:00.849422
---

# Linux 内核攻击 USMA 解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G0KwjfdJmjlH4Ttf7tDXz5v9h4O8VWjKxLh1wXjOkMRaYVJVPj4icKgOTUsd9dFiaM5aTy7rlMZmNw/0?wx_fmt=jpeg)

# Linux 内核攻击 USMA 解析

Elenia
Elenia

看雪学苑

![]()

在小说阅读器中沉浸阅读

**0****1**

**Pakcet Socket**

USMA 利用的是 socket 的 pgv 数组,所以我们在这里先深入了解一下 PacketSocket 的数据结构,在这里我们还是主要关注 pgv 的创建和映射,关于Socket其他板块的详细解析可以看我其他的文章。

### 数据结构

#### packet\_socket

> 我们这里主要关注 rx\_ring/tx\_ing,这是我们后续利用的关键数据结构。
>
> 所以相当于除去 struct socket 以外其他均为 packetsocket 独有的结构.

* sk: 继承的通用 socket \*
* fanout: fanout 组
* rx\_ring/tx\_ring: 接收/发送环形缓冲区（mmap）
* prot\_hook: 协议钩子，用于接收数据包
* ifindex: 绑定的网络设备索引
* tp\_version: TPACKET 版本（V1/V2/V3）

```
struct packet_sock {
/* struct sock has to be the first member of packet_sock */
struct sock             sk;
struct packet_fanout    *fanout;
union  tpacket_stats_u  stats;
struct packet_ring_buffer       rx_ring;
struct packet_ring_buffer       tx_ring;
int                     copy_thresh;
spinlock_t              bind_lock;
struct mutex            pg_vec_lock;
unsignedlong           flags;
int                     ifindex;        /* bound device         */
        u8                      vnet_hdr_sz;
        __be16                  num;
struct packet_rollover  *rollover;
struct packet_mclist    *mclist;
atomic_long_t           mapped;
enum tpacket_versions   tp_version;
unsignedint            tp_hdrlen;
unsignedint            tp_reserve;
unsignedint            tp_tstamp;
struct completion       skb_completion;
struct net_device __rcu *cached_dev;
struct packet_type      prot_hook ____cacheline_aligned_in_smp;
atomic_t                tp_drops ____cacheline_aligned_in_smp;
};
```

#### packet\_ring\_buffer [核心]

正常 Linux Socket 的传输数据需要进行用户层到内核层的拷贝，然后发送后又需要内核层到用户层的拷贝，比较消耗性能。所以类似于 zerocopy 的设计思想，Linux 在 PacketSocket 中设计了共享环形结构，让用户态可以直接将数据写入环形结构避免了拷贝操作。当然如果设置了 ring\_buffer ，但是不使用mmap是没有使用到 zerocopy 的。

ring\_buffer 是 packet\_socket 独有的数据结构。当没有设置 PACKET\_RX\_RING 或 PACKET\_TX\_RING 时，Packet\_socket 和正常的 socket 一样都使用标准的 sk\_receive\_queue/sk\_write\_queue。

* pg\_vec 是 pgv 数组，每个元素对应一个 block
* pg\_vec\_len 是 block 数量
* pg\_vec\_pages 是每个 block 的页数
* pg\_vec\_order 是页分配阶数

```
struct packet_ring_buffer {
struct pgv              *pg_vec;

unsignedint            head;
unsignedint            frames_per_block;
unsignedint            frame_size;
unsignedint            frame_max;

unsignedint            pg_vec_order;
unsignedint            pg_vec_pages;
unsignedint            pg_vec_len;

unsignedint __percpu   *pending_refcnt;

union {
unsignedlong                   *rx_owner_map;
struct tpacket_kbdq_core        prb_bdqc;
        };
};
```

#### Pg\_vec [漏洞目标结构]

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G0KwjfdJmjlH4Ttf7tDXz55PicT9icMLCvHdpMHibxHUtialjq1jWoZPl9fwicR7QqVNUfjc3Ouuj79Ww/640?wx_fmt=other&from=appmsg)

* pgv（Page Vector）是页向量，每个 pgv 指向一个内存块（block）的起始地址，一个block对应一个或者多个完整的page。
* buffer 指向该 block 的实际内存，Block 用于存储我们的网络请求等信息。

```
struct pgv {
char *buffer;
};
```

#### Socket 缓冲区对比

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G0KwjfdJmjlH4Ttf7tDXz5JqCBugdIn2y3mM8J1TdxmERK7CnUNj7hwRHvhFz6sG1myZibTnszXVg/640?wx_fmt=other&from=appmsg)![]()

### Socket 创建流程

#### 调用链

```
用户空间: socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))
    ↓
sys_socket()
    ↓
__sock_create()
    ↓
pf->create() [packet_proto.create = packet_create]
    ↓
packet_create()
    ├─ sk_alloc()                    // 分配 sock 和 packet_sock
    ├─ packet_alloc_pending()         // 分配 pending 结构
    ├─ sock_init_data()              // 初始化 sock 数据
    ├─ mutex_init(&po->pg_vec_lock)  // 初始化 pg_vec 锁
    ├─ po->prot_hook.func = packet_rcv  // 设置接收函数
    └─ __register_prot_hook()        // 注册协议钩子
        └─ dev_add_pack(&po->prot_hook)  // 添加到协议栈
```

### Setsockopt 设置 RingBuffer

> 用户通过 setsockopt 设置 PACKET\_RX\_RING 或 PACKET\_TX\_RING，最终调用 packet\_set\_ring，设置环形缓冲区。

#### 调用链

```
用户空间: setsockopt(fd, SOL_PACKET, PACKET_RX_RING, &req, sizeof(req))
    ↓
sys_setsockopt()
    ↓
sock_setsockopt()
    ↓
packet_setsockopt()
    ↓
case PACKET_RX_RING:
packet_set_ring()
        ├─ 参数验证
        ├─ order = get_order(req->tp_block_size)  // 计算页阶数
        ├─ alloc_pg_vec(req, order)                // 分配 pg_vec 数组
        │   ├─ kcalloc(block_nr, sizeof(struct pgv))  // 分配 pg_vec 数组
        │   └─ for each block:
        │       └─ alloc_one_pg_vec_page(order)    // 分配每个 block 的内存
        │           ├─ __get_free_pages()          // 优先使用连续物理页
        │           ├─ vzalloc()                   // 失败则使用虚拟连续内存
        │           └─ __get_free_pages()          // 最后重试（允许 swap）
        ├─ init_prb_bdqc() [V3 only]              // 初始化 V3 块描述符
        │   ├─ p1->pkbdq = pg_vec                 // 设置 pg_vec 指针
        │   └─ prb_open_block()                   // 打开第一个 block
        ├─ 临时卸载协议钩子
        ├─ swap(rb->pg_vec, pg_vec)               // 交换 pg_vec
        ├─ 设置 ring buffer 参数
        └─ 重新注册协议钩子
            └─ po->prot_hook.func = tpacket_rcv   // 切换到 tpacket_rcv
```

#### packet\_set\_ring(入口)

* 参数校验（block\_size、frame\_size 等）
* 计算 order（页分配阶数）
* 调用 alloc\_pg\_vec 分配 pg\_vec
* 根据版本初始化（V3 调用 init\_prb\_bdqc，V1/V2 分配 rx\_owner\_map）
* 临时卸载协议钩子，设置 pg\_vec，再重新注册
* 若设置了 rx\_ring.pg\_vec，将接收函数切换为 tpacket\_rcv

```
static int packet_set_ring(struct sock *sk, union tpacket_req_u *req_u,
                int closing, int tx_ring)
{
struct pgv *pg_vec = NULL;
struct packet_sock *po = pkt_sk(sk);
        unsigned long *rx_owner_map = NULL;
        int was_running, order = 0;
struct packet_ring_buffer *rb;
struct sk_buff_head *rb_queue;
        __be16 num;
        int err;
/* Added to avoid minimal code churn */
struct tpacket_req *req = &req_u->req;

        rb = tx_ring ? &po->tx_ring : &po->rx_ring;
        rb_queue = tx_ring ? &sk->sk_write_queue : &sk->sk_receive_queue;

        err = -EBUSY;
if (!closing) {
if (atomic_long_read(&po->mapped))
                        goto out;
if (packet_read_pending(rb))
                        goto out;
        }

if (req->tp_block_nr) {
                unsigned int min_frame_size;

/* Sanity tests and some calculations */
                err = -EBUSY;
if (unlikely(rb->pg_vec))
                        goto out;

switch (po->tp_version) {
                case TPACKET_V1:
                        po->tp_hdrlen = TPACKET_HDRLEN;
break;
                case TPACKET_V2:
                        po->tp_hdrlen = TPACKET2_HDRLEN;
break;
                case TPACKET_V3:
                        po->tp_hdrlen = TPACKET3_HDRLEN;
break;
                }

                err = -EINVAL;
if (unlikely((int)req->tp_block_size <= 0))
                        goto out;
if (unlikely(!PAGE_ALIGNED(req->tp_block_size)))
                        goto out;
                min_frame_size = po->tp_hdrlen + po->tp_reserve;
if (po->tp_version >= TPACKET_V3 &&
                    req->tp_block_size <
BLK_PLUS_PRIV((u64)req_u->req3.tp_sizeof_priv) + min_frame_size)
                        goto out;
if (unlikely(req->tp_frame_size < min_frame_size))
                        goto out;
if (unlikely(req->tp_frame_size & (TPACKET_ALIGNMENT - 1)))
                        goto out;

                rb->frames_per_block = req->tp_block_size / req->tp_frame_size;
if (unlikely(rb->frames_per_block == 0))
                        goto out;
if (unlikely(rb->frames_per_block > UINT_MAX / req->tp_block_nr))
                        goto out;
if (unlikely((rb->frames_per_block * req->tp_block_nr) !=
                                        req->tp_frame_nr))
                        goto out;

                err = -ENOMEM;
                order = get_order(req->tp_block_size);
                pg_vec = alloc_pg_vec(req, order);
if (unlikely(!pg_vec))
                        goto out;
switch (po->tp_version) {
                case TPACKET_V3:
/* Block transmit is not supported yet */
if (!tx_ring) {
init_prb_bdqc(po, rb, pg_vec, req_u);
                        } else {
struct tpacket_req3 *req3 = &req_u->req3;

if (req3->tp_retire_blk_tov ||
                           ...