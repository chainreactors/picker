---
title: 每天学习一个命令：wrk 单机性能测试工具
url: https://blog.einverne.info/post/2024/10/wrk-benchmark-tool.html
source: Verne in GitHub
date: 2024-10-06
fetch_date: 2025-10-06T18:45:31.619635
---

# 每天学习一个命令：wrk 单机性能测试工具

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# 每天学习一个命令：wrk 单机性能测试工具

Posted on 10/05/2024
, Last modified on 10/05/2024
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2024-10-05-wrk-benchmark-tool.md)

[wrk](https://github.com/wg/wrk) 是一个使用 C 编写的 HTTP 压力测试工具，性能基准测试工具。可以在单机多核 CPU 的条件下，充分利用系统的高性能 IO，epoll，kqueue 等，通过多线程和事件，对目标机产生大量的负载。

wrk 采用了和 Redis 一样的 ae 异步事件驱动框架。

## 优势

* 轻量
* 安装简单
* 使用手册简单
* 自带高性能 IO，通过很少线程即可产生很大的并发量

## 缺点

目前只支持单机压测，设计的目的不是为了代替专业的 [[Apache JMeter]] 以及 [[LoadRunner]] 等测试工具。

wrk 比较适合于后端对接口的性能测试。

wrk 只能被安装在类 Unix 系统上。Windows 则需要开启 Ubuntu 子系统。

## 安装

macOS

```
brew install wrk
wrk -v
```

## 使用

```
wrk -t12 -c400 -d30s http://127.0.0.1:8080/index.html
```

这一行命令会使用 12 线程，测试 30 秒，并且保持 400 HTTP 连接。

更多命令选项

```
Usage: wrk <options> <url>
  Options:
    -c, --connections <N>  Connections to keep open
    -d, --duration    <T>  Duration of test
    -t, --threads     <N>  Number of threads to use

    -s, --script      <S>  Load Lua script file
    -H, --header      <H>  Add header to request
        --latency          Print latency statistics
        --timeout     <T>  Socket/request timeout
    -v, --version          Print version details

  Numeric arguments may include a SI unit (1k, 1M, 1G)
  Time arguments may include a time unit (2s, 2m, 2h)
```

可以通过 Lua 脚本的方式来产生 POST，PUT 等请求。

## Related Posts

* [每天学习一个命令：wrk 单机性能测试工具](/post/2024/10/wrk-benchmark-tool.html) - 10/05/2024
* [使用 k6 做一次负载性能测试](/post/2023/07/k6-load-testing.html) - 07/01/2023
* [VPS 性能测试](/post/2021/07/vps-benchmark.html) - 07/30/2021

---

* [← Previous（前一篇）](/post/2024/09/estonia-e-residency-activated-email-forward.html "爱沙尼亚电子公民身份启动及邮件转发")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2024/10/sanity.html "现代化的内容管理系统 Sanity 使用")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2024/10/wrk-benchmark-tool.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [每天学习一个命令 78](/categories.html#每天学习一个命令)

* [wrk 1](/tags.html#wrk)
* [jmeter 2](/tags.html#jmeter)
* [load-testing 2](/tags.html#load-testing)
* [benchmark 2](/tags.html#benchmark)
* [vps-benchmark 2](/tags.html#vps-benchmark)
* [benchmark-testing 1](/tags.html#benchmark-testing)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").