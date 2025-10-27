---
title: HTTP 压力测试中的 Coordinated Omission
url: https://jiajunhuang.com/articles/2024_08_30-http_load_testing.md.html
source: Jiajun的技术笔记
date: 2024-08-31
fetch_date: 2025-10-06T17:59:18.447943
---

# HTTP 压力测试中的 Coordinated Omission

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

* [HTTP 压力测试中的 Coordinated Omission](#HTTP%2b%25E5%258E%258B%25E5%258A%259B%25E6%25B5%258B%25E8%25AF%2595%25E4%25B8%25AD%25E7%259A%2584%2bCoordinated%2bOmission)
* [vegata 使用示例](#vegata%2b%25E4%25BD%25BF%25E7%2594%25A8%25E7%25A4%25BA%25E4%25BE%258B)

# HTTP 压力测试中的 Coordinated Omission

HTTP负载测试工具有很多，常见的有 ApacheBench，也就是 ab，还有 wrk、vegata等。在了解这些工具时，我了解到一个新的概念：

Coordinated Omission，来看 GPT 的解释：

> “Coordinated Omission”是性能测试中一个重要的概念。在性能测试中，我们常常需要测量系统的延迟，例如一个请求从发送到收到响应所需的时间。然而，如果在系统延迟的情况下，我们暂停发送新的请求，那么我们测量的延迟就会低于实际值。这就是所谓的”Coordinated Omission”（协同遗漏）。简单来说，”Coordinated Omission”是一种测试偏差，它发生在以下情况：当系统延迟时，我们暂停发送新的请求，等待系统恢复后再发送。这样，我们就忽略了在系统延迟期间应该发送但没有发送的请求。因此，我们测量的延迟结果会低于实际值。例如，假设我们每秒发送10个请求，每个请求的预期延迟是100毫秒。然而，在某一时刻，由于系统延迟，一个请求花了200毫秒才得到响应。如果我们在这200毫秒内暂停发送新的请求，那么我们就会忽略掉这200毫秒内应该发送但没有发送的1个请求。因此，我们测量的平均延迟会低于实际值。”Coordinated Omission”的问题在于，它会导致我们低估系统在高负载情况下的真实性能。因此，在进行性能测试时，我们需要采取措施避免”Coordinated Omission”，以获得更准确的测试结果。

这个问题，会导致我们低估系统在高负载情况下的真实性能。举个简单的例子来理解，如果我们实现一个压测工具，采用的是
for循环来实现，其中一个请求耗时较长导致后续请求被阻塞，那么这个工具就会有 Coordinated Omission 问题。

wrk 就有 Coordinated Omission 的问题，因此有人提出了 wrk2 来解决这个问题。不过由于要自己编译，还挺麻烦的，我选择
使用 vegata 来进行压测(vegata可以携带 payload 进行请求)。

## vegata 使用示例

首先我们用Go语言写一个简单的HTTP服务：

```
package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.POST("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
	})
	r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
```

然后我们用 vegata 来进行压测：

```
$ echo "POST http://localhost:8080/" | vegeta attack -body post.json -rate=10000 -duration=30s | vegeta report
Requests      [total, rate, throughput]         300000, 10000.39, 10000.35
Duration      [total, attack, wait]             29.999s, 29.999s, 118.062µs
Latencies     [min, mean, 50, 90, 95, 99, max]  49.042µs, 152.644µs, 137.14µs, 181.872µs, 250.288µs, 466.057µs, 3.108ms
Bytes In      [total, mean]                     5400000, 18.00
Bytes Out     [total, mean]                     7500000, 25.00
Success       [ratio]                           100.00%
Status Codes  [code:count]                      200:300000
Error Set:
```

这样就可以看到持续30s，每秒10000个请求的情况了。

---

##### 相关文章

* [用peewee代替SQLAlchemy](/articles/2020_05_29-use_peewee.md.html)
* [Go的slice工作机制](/articles/2020_05_23-go_slice.md.html)
* [Linux系统迁移记录(从HDD到SSD)](/articles/2020_05_22-linux_clone_sys.md.html)
* [Redis是如何工作的？](/articles/2020_05_21-how_does_redis_work.md.html)
* [virsh自动关闭windows虚拟机](/articles/2020_05_18-virsh_shutdown_win.md.html)
* [Golang sort源码阅读](/articles/2020_05_16-go_sort.md.html)
* [分治的思维方式](/articles/2020_05_15-divide_and_conquer.md.html)
* [Debian 使用NetworkManager之后networking.service崩溃](/articles/2020_05_13-debian_networking.md.html)
* [httprouter源码阅读与分析](/articles/2020_05_09-httprouter.md.html)
* [《程序员的自我修养-装载、链接与库》笔记](/articles/2020_05_08-linker_and_loader.md.html)
* [Golang sync.Pool源码阅读与分析](/articles/2020_05_05-go_sync_pool.md.html)
* [MySQL操作笔记](/articles/2020_05_01-mysql_notes.md.html)
* [Go语言解析GBK编码的xml](/articles/2020_04_30-golang_gbk_xml.md.html)
* [Golang log 源码阅读](/articles/2020_04_28-golang_log.md.html)
* [使用Go语言实现一个异步任务框架](/articles/2020_04_24-gotasks.md.html)

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