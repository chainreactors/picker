---
title: 编程语言中的 context 是什么？
url: https://jiajunhuang.com/articles/2024_07_21-context.md.html
source: Jiajun的技术笔记
date: 2024-07-22
fetch_date: 2025-10-06T17:38:34.798726
---

# 编程语言中的 context 是什么？

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

* [编程语言中的 context 是什么？](#%25E7%25BC%2596%25E7%25A8%258B%25E8%25AF%25AD%25E8%25A8%2580%25E4%25B8%25AD%25E7%259A%2584%2bcontext%2b%25E6%2598%25AF%25E4%25BB%2580%25E4%25B9%2588%25EF%25BC%259F)

# 编程语言中的 context 是什么？

最近在看 CSAPP3e，看到讲 context，想起这个概念在学习编程的时候经常遇到，却没有一个准确清晰的定义。随着在工作中逐渐积累，
才有一些感觉。准确的来说，context，就是一堆状态(state)。举几个例子来看不同场景下的 context：

进程/线程切换：进程切换的时候，需要保存当前进程的状态，包括寄存器、内存等，这些状态就是 context。

![进程切换](./img/context_switch.png)

对于进程来说，操作系统把它切换以后，未来的某个时刻还需要切换回来恢复执行，恢复执行所需要的状态，就是进程的上下文。

函数调用：函数调用的时候，需要保存当前函数的状态，包括参数、局部变量、返回地址等，这些状态就是 context。

```
int add(int a, int b) {
    return a + b;
}

int main() {
    int c = add(1, 2);
    return 0;
}
```

在调用 `add` 函数的时候，需要保存当前函数的状态，包括参数 `a` 和 `b`，返回地址等，这些状态就是函数的上下文。

Go语言中的 context， 比如GIN框架中的 `gin.Context`，用来在请求之间传递上下文信息，这个上下文信息就是 context。

```
func Ping(c *gin.Context) {
    c.JSON(200, gin.H{
        "message": "pong",
    })
}
```

我们可以把一些状态信息放到 `gin.Context` 中，然后在对应的请求处理函数中获取这些状态信息，比如当前用户信息，请求参数等。

Python 中的 `contextlib` 模块：Python 中的 `contextlib` 模块，用来管理上下文，这个上下文就是 context。

```
from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
```

这个例子中，`tag` 函数返回一个上下文管理器，`with` 语句中的代码块会在进入和退出上下文的时候执行，这个上下文就是 context。

因此，我们可以这样理解：context 就是一堆状态(state)，在不同的场景下，context 的具体内容和作用是不同的，但是都是用来保存和传递状态信息的。

---

##### 相关文章

* [我的代码进CPython标准库啦](/articles/2016_12_15-my_code_in_python_stdlib.md.html)
* [Python零碎小知识](/articles/2016_12_09-python_fragments.md.html)
* [工作一年的总结](/articles/2016_12_07-work.md.html)
* [Python和单元测试](/articles/2016_12_07-python_unittest.md.html)
* [MongoDB 的一些坑](/articles/2016_12_06-mongodb.md.html)
* [Python 的继承](/articles/2016_12_06-python_c3_mro.md.html)
* [Python的yield关键字有什么作用？](/articles/2016_11_29-python_yield.md.html)
* [借助coroutine用同步的语法写异步](/articles/2016_11_27-python_coroutine.md.html)
* [Python3函数参数中的星号](/articles/2016_11_21-py3k_asterisk.rst.html)
* [使用Git Hooks](/articles/2016_11_08-use_git_hooks.rst.html)
* [Token Bucket 算法](/articles/2016_11_05-token_bucket.rst.html)
* [nginx配置笔记](/articles/2016_11_03-nginx_conf.rst.html)
* [阅读Flask源码](/articles/2016_09_15-flask_source_code.rst.html)
* [尤克里里](/articles/2016_08_25-ukulele.rst.html)
* [学习使用Bootstrap4的栅格系统](/articles/2016_06_20-bootstrap_v4_grid_system.rst.html)

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