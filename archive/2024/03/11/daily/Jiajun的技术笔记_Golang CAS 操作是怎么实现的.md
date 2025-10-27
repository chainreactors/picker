---
title: Golang CAS 操作是怎么实现的
url: https://jiajunhuang.com/articles/2024_03_10-golang_cas.md.html
source: Jiajun的技术笔记
date: 2024-03-11
fetch_date: 2025-10-04T12:07:59.255205
---

# Golang CAS 操作是怎么实现的

[Jiajun的技术笔记](/)

搜索

* [EN](https://blog.jiajunhuang.com)
* [归档](/archive)
* [分享](/sharing)
* [随想](/notes)
* [友链](/friends)
* 工具

  [面试题库](https://tiku.jiajunhuang.com)
  [幻灯片](https://jiajunhuang.com/page/index.md)
* [关于](/aboutme)

目录

* [Golang CAS 操作是怎么实现的](#Golang%2bCAS%2b%25E6%2593%258D%25E4%25BD%259C%25E6%2598%25AF%25E6%2580%258E%25E4%25B9%2588%25E5%25AE%259E%25E7%258E%25B0%25E7%259A%2584)

# Golang CAS 操作是怎么实现的

在Go语言中，CAS(Compare and Swap) 操作一般都是通过 `atomic` 操作来实现的，我们来探究一下底层是怎么实现的。

我们以 `CompareAndSwapInt32` 为例，首先找到源码，位于 `doc.go`：

```
// CompareAndSwapInt32 executes the compare-and-swap operation for an int32 value.
// Consider using the more ergonomic and less error-prone [Int32.CompareAndSwap] instead.
func CompareAndSwapInt32(addr *int32, old, new int32) (swapped bool)
```

在Go语言中，这种只有函数声明，没有函数实现的，通常意味着函数的实现在Go汇编中。在 `asm.s` 中可以找到定义：

```
TEXT ·CompareAndSwapInt32(SB),NOSPLIT,$0
	JMP	runtime∕internal∕atomic·Cas(SB)
```

然后跟着路径找 `internal/atomic/atomic_amd64.s`：

```
// bool Cas(int32 *val, int32 old, int32 new)
// Atomically:
//	if(*val == old){
//		*val = new;
//		return 1;
//	} else
//		return 0;
TEXT ·Cas(SB),NOSPLIT,$0-17
	MOVQ	ptr+0(FP), BX
	MOVL	old+8(FP), AX
	MOVL	new+12(FP), CX
	LOCK
	CMPXCHGL	CX, 0(BX)
	SETEQ	ret+16(FP)
	RET
```

我们来看下这段汇编代码的意思，以下解释来自ChatGPT：

```
TEXT ·Cas(SB),NOSPLIT,$0-17
```

这行代码定义了一个名为 `Cas` 的函数，`SB` 是一个汇编器符号，表示当前包的起始地址。
`NOSPLIT` 表示该函数不会发生栈的分裂，`$0-17` 表示函数没有输入参数，但有 17 个字节的输出参数。

```
MOVQ	ptr+0(FP), BX
```

这行代码将函数的第一个输入参数 `ptr` 的值加载到寄存器 `BX` 中。

```
MOVL	old+8(FP), AX
```

这行代码将函数的第二个输入参数 `old` 的值加载到寄存器 `AX` 中。

```
MOVL	new+12(FP), CX
```

这行代码将函数的第三个输入参数 `new` 的值加载到寄存器 `CX` 中。

```
LOCK
```

这行代码是一个前缀指令，用于告诉处理器后面的指令是原子操作，需要获取总线锁。

```
CMPXCHGL	CX, 0(BX)
```

这行代码使用 CMPXCHG 指令进行比较和交换操作。它比较内存地址 `0(BX)` 处的值与寄存器 `CX` 的值是否相等，如果相等，则将寄存器 `CX` 的值写入内存地址 `0(BX)` 中。

```
SETEQ	ret+16(FP)
```

这行代码根据 CMPXCHG 指令的结果设置标志位，如果比较和交换成功，则将标志位设置为 1，否则设置为 0。

```
RET
```

这行代码表示函数的返回。

总的来说，这段汇编代码实现了一个 CAS 操作，它比较内存地址中的值与期望值是否相等，如果相等，则将新的值写入内存地址中，并返回操作是否成功。这个 CAS 操作使用了 CMPXCHG 指令来实现原子的比较和交换操作。

其实说到底，Golang的CAS操作，就是依靠 `LOCK` + `CMPXCHGL` 来实现的，其他的语言也是一样的，需要依赖CPU提供这种底层
能力，才能够真正的做到 CAS。

---

##### 相关文章

* [Go DiskQueue源码阅读](/articles/2020_08_22-go_diskqueue.md.html)
* [NSQ源码分析](/articles/2020_08_16-nsq_source_code.md.html)
* [NSQ简明教程](/articles/2020_08_15-nsq.md.html)
* [结合Redis与MySQL实现又快又好的数据方案](/articles/2020_08_11-redis_mysql.md.html)
* [程序员的MySQL手册(五)：索引优化](/articles/2020_07_28-mysql_part5.md.html)
* [程序员的MySQL手册(四)：索引设计](/articles/2020_07_27-mysql_part4.md.html)
* [程序员的MySQL手册(三)：数据库设计](/articles/2020_07_26-mysql_part3.md.html)
* [Linux窗口管理器下的截图](/articles/2020_07_25-linux_screenshot.md.html)
* [Go设计模式：facade模式和观察者模式](/articles/2020_07_23-go_design_pattern_facade.md.html)
* [程序员的MySQL手册(二): 监控与benchmark](/articles/2020_07_23-mysql_part2.md.html)
* [Go设计模式: 责任链模式](/articles/2020_07_21-go_design_pattern_chain.md.html)
* [我们真的需要这么复杂的技术栈吗？](/articles/2020_07_15-do_we_need_these.md.html)
* [Go设计模式：装饰器模式](/articles/2020_07_14-go_design_pattern_decorator.md.html)
* [程序员的MySQL手册(一): 安装，基本配置](/articles/2020_07_05-mysql_part1.md.html)
* [ElasticSearch学习笔记](/articles/2020_07_04-elasticsearch.md.html)

---

加载评论

* [![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=dedfc09c3066&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
* [![](/static/email.png)
  邮件 订阅](https://eepurl.com/guVPMj)
* [![](/static/rss.png)
  RSS 订阅](/rss)
* [![](/static/web.png)
  Web开发简介系列](/articles/2017_10_19-web_dev_series.md.html)
* [![](/static/computer.png)
  数据结构的实际使用](/tutorial/data_structure/index.md)
* [![](/static/golang.png)
  Golang 简明教程](/tutorial/golang/index.md)
* [![](/static/python.png)
  Python 教程](/tutorial/python/index.md)

本站热门

* [socks5 协议详解](/articles/2019_06_06-socks5.md.html)
* [zerotier简明教程](/articles/2019_09_11-zerotier.md.html)
* [搞定面试中的系统设计题](/articles/2019_04_29-system_design.md.html)
* [frp 源码阅读与分析(一)：流程和概念](/articles/2019_06_11-frpc_source_code_part1.md.html)
* [用peewee代替SQLAlchemy](/articles/2020_05_29-use_peewee.md.html)
* [Golang(Go语言)中实现典型的fork调用](/articles/2018_03_08-golang_fork.md.html)
* [DNSCrypt简明教程](/articles/2019_10_31-dnscrypt.md.html)
* [一个Gunicorn worker数量引发的血案](/articles/2020_03_11-gunicorn_worker.md.html)
* [Golang validator使用教程](/articles/2020_04_10-golang_validator.md.html)
* [Docker组件介绍（二）：shim, docker-init和docker-proxy](/articles/2018_12_24-docker_components_part2.md.html)
* [Docker组件介绍（一）：runc和containerd](/articles/2018_12_22-docker_components.md.html)
* [使用Go语言实现一个异步任务框架](/articles/2020_04_24-gotasks.md.html)
* [协程(coroutine)简介 - 什么是协程？](/articles/2018_04_03-coroutine.md.html)
* [SQLAlchemy简明教程](/articles/2019_10_30-sqlalchemy.md.html)
* [Golang的template(模板引擎)简明教程](/articles/2019_08_23-golang_html_template.md.html)

[@jiajunhuang](https://github.com/jiajunhuang) 2015-2024, All Rights Reserved。本站禁止转载，引用请注明作者与原链。