---
title: 【原理】Redis热点Key自动发现机制和客户端缓存方案
url: https://www.freebuf.com/news/414279.html
source: FreeBuf网络安全行业门户
date: 2024-11-02
fetch_date: 2025-10-06T19:16:59.389860
---

# 【原理】Redis热点Key自动发现机制和客户端缓存方案

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

【原理】Redis热点Key自动发现机制和客户端缓存方案

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

【原理】Redis热点Key自动发现机制和客户端缓存方案

2024-11-01 15:34:58

所属地 北京

作者：京东物流 京东物流

**本文详细讲解下Redis热点key发现机制+客户端缓存的原理。**

# 一、redis4.0之基于LFU的热点key发现机制

业务中存在访问热点是在所难免的，然而如何发现热点key一直困扰着许多用户，redis4.0为我们带来了许多新特性，其中便包括基于LFU的热点key发现机制。

## Redis中的LFU思路

**Least Frequently Used——简称LFU，意为最不经常使用，是redis4.0新增的一类内存逐出策略，**

从LFU的字面意思我们很容易联想到key的访问频率，但是4.0最初版本仅用来做内存逐出，对于访问频率并没有很好的记录，那么经过一番改造，redis于4.0.3版本开始正式支持基于LFU的热点key发现机制。它也是基于局部性原理：如果一个数据在最近一段时间内使用次数最少，那么在将来一段时间内被使用的可能性也很小

在`LFU`算法中，可以为每个key维护一个计数器。每次key被访问的时候，计数器增大。计数器越大，可以约等于访问越频繁。

## 1.1、LFU算法介绍

在redis中每个对象都有24 bits空间来记录LRU/LFU信息：

```
typedefstructredisObject {
    unsigned type:4;
    unsigned encoding:4;
    unsigned lru:LRU_BITS; /* LRU time (relative to global lru_clock) or
                            * LFU data (least significant 8 bits frequency
                            * and most significant 16 bits access time). */
    int refcount;
    void *ptr;
} robj;
```

当这24 bits用作LFU时，其被分为两部分：

1.高16位用来记录访问时间（单位为分钟）

2.低8位用来记录访问频率，简称counter

```
16 bits         8 bits
      +------------------+--------+
      + Last access time | LOG_C  |
      +------------------+--------+
```

### 1.1.1、counter：基于概率的对数计数器

**这里读者可能会有疑问，8 bits最大值也就是255，只用8位来记录访问频率够用吗？对于counter，redis用了一个trick的手段，counter并不是一个简单的线性计数器，而是用基于概率的对数计数器来实现，算法如下：**

```
void updateLFU(robj *val) {
    unsigned long counter = LFUDecrAndReturn(val);
    //counter增长函数
    counter = LFULogIncr(counter);
    val->lru = (LFUGetTimeInMinutes()<<8) | counter;
}
```

```
#define LFU_INIT_VAL 5
server.lfu_log_factor = CONFIG_DEFAULT_LFU_LOG_FACTOR; //server.c  概率因子
#define CONFIG_DEFAULT_LFU_LOG_FACTOR 10  //server.h
 //counter增长函数
 uint8_t LFULogIncr(uint8_t counter) {
//如果已经到最大值255，返回255 ，8位的最大值
      if (counter == 255) return 255;
  //取一随机小数（0-1）
      double r = (double)rand()/RAND_MAX;
//新加入的key初始counter设置为LFU_INIT_VAL,为5.不设置为0的原因是防止直接被逐出。
      double baseval = counter - LFU_INIT_VAL;
      if (baseval < 0) baseval = 0;
      double p = 1.0/(baseval*server.lfu_log_factor+1);
//可以看到,counter越大,则p越小，随机值r小于p的概率就越小。换言之,counter增加起来会越来越缓慢
      if (r < p) counter++;
      return counter;//counter 访问频率
  }
```

对应的概率分布计算公式为：

```
1/((counter-LFU_INIT_VAL)*server.lfu_log_factor+1)
```

`counter`并不是简单的访问一次就+1，而是采用了一个0-1之间的p因子控制增长。`counter`最大值为255。取一个0-1之间的随机数r与p比较，当`r<p`时，才增加`counter`控制产出的策略。p取决于当前`counter`值与`lfu_log_factor`因子，`counter`值与`lfu_log_factor`因子越大，p越小，`r<p`的概率也越小，`counter`增长的概率也就越小。

LRU本质上是一个概率计数器，称为morris counter.随着访问次数的增加,counter的增加会越来越缓慢。如下是访问次数与counter值之间的关系

```
+--------+------------+------------+------------+------------+------------+
| factor | 100 hits   | 1000 hits  | 100K hits  | 1M hits    | 10M hits   |+--------+------------+------------+------------+------------+------------+
| 0      | 104        | 255        | 255        | 255        | 255        |+--------+------------+------------+------------+------------+------------+
| 1      | 18         | 49         | 255        | 255        | 255        |+--------+------------+------------+------------+------------+------------+
| 10     | 10         | 18         | 142        | 255        | 255        |+--------+------------+------------+------------+------------+------------+
| 100    | 8          | 11         | 49         | 143        | 255        |+--------+------------+------------+------------+------------+------------+
```

factor即server.lfu\_log\_facotr配置值，默认为10.可以看到,一个key访问一千万次以后counter值才会到达255.factor值越小, counter越灵敏.可见`counter`增长与访问次数呈现对数增长的趋势，随着访问次数越来越大，`counter`增长的越来越慢。

其中LFU\_INIT\_VAL为5，我们看下概率分布图会有一个更直观的认识，以默认server.lfu\_log\_factor=10为例：

1/((counter-5)\*10+1)

![](https://image.3001.net/images/20200701/1593550745.png!small)

![KPDqIWqhFgRTt6HR8g5a.png](https://image.3001.net/images/20200701/1593550745.png!small)

从上图可以看到，counter越大，其增加的概率越小，8 bits也足够记录很高的访问频率，

也就是说，默认server.lfu\_log\_factor为10的情况下，8 bits的counter可以表示1百万的访问频率。

### 1.1.2、新生key策略

另外一个问题是，当创建新对象的时候，对象的`counter`如果为0，很容易就会被淘汰掉，还需要为新生key设置一个初始`counter`，[`createObject`](https://github.com/antirez/redis/blob/unstable/src/object.c#L41):

```
robj *createObject(int type, void *ptr) {
    robj *o = zmalloc(sizeof(*o));
    o->type = type;
    o->encoding = OBJ_ENCODING_RAW;
    o->ptr = ptr;
    o->refcount = 1;

    /* Set the LRU to the current lruclock (minutes resolution), or
     * alternatively the LFU counter. */
    if (server.maxmemory_policy & MAXMEMORY_FLAG_LFU) {
        o->lru = (LFUGetTimeInMinutes()<<8) | LFU_INIT_VAL;
    } else {
        o->lru = LRU_CLOCK();
    }
    return o;
}
```

`counter`会被初始化为`LFU_INIT_VAL`，默认5。

### 1.1.3、counter的衰减因子

从上一小节的counter增长函数LFULogIncr中我们可以看到，随着key的访问量增长，counter最终都会收敛为255，这就带来一个问题，如果counter只增长不衰减就无法区分热点key。

为了解决这个问题，redis提供了衰减因子server.lfu\_decay\_time，其单位为分钟，计算方法也很简单，如果一个key长时间没有访问那么它的计数器counter就要减少，减少的值由衰减因子来控制：

```
unsigned long LFUDecrAndReturn(robj *o) {
    //lru字段右移8位，得到前面16位的分钟时间戳
    unsignedlong ldt = o->lru >> 8;
 //lru字段与255进行&运算（255代表8位的最大值），得到8位当前counter值
    unsignedlong counter = o->lru & 255;
 //总的没访问的分钟时间/配置值，得到每分钟没访问衰减多，默认每经过一分钟counter衰减1
    unsignedlong num_periods = server.lfu_decay_time ? LFUTimeElapsed(ldt) / server.lfu_decay_time : 0;
    if (num_periods)
     //计算衰减后的值
        counter = (num_periods > counter) ? 0 : counter - num_periods;
    return counter;
}
```

默认为1的情况下也就是N分钟内没有访问，counter就要减N。

函数首先取得高16 bits的最近降低时间`ldt`与低8 bits的计数器`counter`，然后根据配置的`lfu_decay_time`计算应该降低多少。

`LFUTimeElapsed`用来计算当前时间与`ldt`的差值：

```
/* Return the current time in minutes, just taking the least significant * 16 bits. The returned time is suitable to be stored as LDT (last decrement * time) for the LFU implementation. */unsignedlongLFUGetTimeInMinutes(void) {
    return (server.unixtime/60) & 65535;
}
/* Given an object last access time, compute the minimum number of minutes * that elapsed since the last access. Handle overflow (ldt greater than * the current 16 bits minutes time) considering the time as wrapping * exactly once. */unsignedlongLFUTimeElapsed(unsignedlong ldt) {
    unsignedlong now = LFUGetTimeInMinutes();
    if (now >= ldt) return now-ldt;
    return65535-ldt+now;
}
```

具体是当前时间转化成分钟数后取低16 bits，然后计算与`ldt`的差值`now-ldt`。当`ldt > now`时，默认为过了一个周期(16 bits，最大65535)，取值`65535-ldt+now`。

然后用差值与配置`lfu_decay_time`相除，`LFUTimeElapsed(ldt) / server.lfu_decay_time`，已过去n个`lfu_decay_time`，则将`counter`减少n，`counter - num_periods`。

### 1.1.4、LFU配置

`Redis`4.0之后为`maxmemory_policy`淘汰策略添加了两个`LFU`模式：

•`volatile-lfu`：对有过期时间的key采用`LFU`淘汰算法

•`allkeys-lfu`：对全部key采用`LFU`淘汰算法

还有2个配置可以调整`LFU`算法：

```
lfu-log-factor 10
lfu-decay-time1
```

`lfu-log-factor`可以调整计数器`counter`的增长速度，`lfu-log-factor`越大，`counter`增长的越慢。

`lfu-decay-time`是一个以分钟为单位的数值，可以调整`counter`的减少速度

1.热点key发现

介绍完LFU算法，接下来就是我们关心的热点key发现机制。

其核心就是在每次对key进行读写访问时，更新LFU的24 bits域代表的访问时间和counter，这样每个key就可以获得正确的LFU值：

```
void updateLFU(robj*val) {
//首先计算是否需要将counter衰减
    unsigned long counter = LFUDecrAndReturn(val);
//根据上述返回的counter计算新的counter
    counter = LFULogIncr(counter);
//robj中的lru字段只有24bits,lfu复用该字段。高16位存储一个分钟数级别的时间戳，低8位存储访问计数
    val->lru = (LFUGetTimeInMinutes()<<8) | counter;
}
```

# 二、redis6.0 客户端缓存方案

## 1.1 client cache的问题

client cache的问题是缓...