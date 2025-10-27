---
title: 2的补码
url: https://jiajunhuang.com/articles/2024_07_24-twos_complement.md.html
source: Jiajun的技术笔记
date: 2024-07-25
fetch_date: 2025-10-06T17:41:12.893058
---

# 2的补码

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

* [2的补码](#2%25E7%259A%2584%25E8%25A1%25A5%25E7%25A0%2581)
* [原码](#%25E5%258E%259F%25E7%25A0%2581)
* [反码](#%25E5%258F%258D%25E7%25A0%2581)
* [什么是补码](#%25E4%25BB%2580%25E4%25B9%2588%25E6%2598%25AF%25E8%25A1%25A5%25E7%25A0%2581)
* [总结](#%25E6%2580%25BB%25E7%25BB%2593)

# 2的补码

计算机的底层是一堆的bit,具体怎么理解bit，取决于我们怎么解释，对于同样的8个bit，例如 `11111111`，我们可以把它看成是一个无符号数，也可以看成是一个有符号数。
如果我们把它看成是一个无符号数，那么它的值就是255，如果我们把它看成是一个有符号数，那么它的值就是-1, 如果理解为字符，那么它就是一个字符，具体是什么字符，取决于编码方式，如果是ASCII编码，那么它就是DEL字符。

对于无符号数，我们可以直接用二进制表示，例如 `11111111` 就是255，计算机很轻易就能理解二进制，但是人类比较熟悉十进制。我们看看换算过程：

```
1*2^7 + 1*2^6 + 1*2^5 + 1*2^4 + 1*2^3 + 1*2^2 + 1*2^1 + 1*2^0 = 255
```

但是现实情况中，数字不仅有正数，还有负数，那么我们怎么表示负数呢？我们可以用补码的方式来表示负数。

## 原码

原码是最简单的一种表示方法，就是用最高位来表示符号，0表示正数，1表示负数，其余位表示数值。例如，`00000001`表示1，`10000001`表示-1。

原码的优点是，非常直观，可以直接看出一个数是正数还是负数，但是原码的缺点也很明显，就是加减法非常麻烦，因为要考虑符号位。

比如我们要计算1+1，首先我们要找到1的原码，然后再相加，最后再判断符号位。

```
1的原码：00000001
1的原码：00000001
相加：00000010
换算成十进制：2
```

但是，如果我们要计算1-1，首先我们要找到1的原码，然后找到-1的原码，然后再相加，最后再判断符号位。

```
1的原码：00000001
-1的原码：10000001
相加：10000010
换算成十进制：-2
```

可以看到，计算结果是错误的，这是因为原码的计算中，符号位也参与了计算，导致结果错误。

因此有了反码的出现。

## 反码

反码是在原码的基础上，对负数的数值部分取反。例如，`00000001`表示1，`11111110`表示-1。

反码的优点是，加减法非常简单，只需要把两个数的反码相加即可，不需要考虑符号位。

比如我们要计算1+1，首先我们要找到1的反码，然后再相加，最后再判断符号位。

```
1的反码：00000001
1的反码：00000001
相加：00000010
换算成十进制：2
```

如果我们要计算1-1，首先我们要找到1的反码，然后找到-1的反码，再相加，最后再判断符号位。

```
1的反码：00000001
-1的反码：11111110
相加：11111111
换算成十进制：-0
```

但是反码的缺点也很明显，就是有两种0，正0和负0，这样会导致一些问题，因此有了补码的出现。

## 什么是补码

补码是一种用来表示负数的方法，它的特点是，正数的补码就是它本身，负数的补码是它的绝对值的二进制取反加1。

例如，我们要表示-1，首先我们要找到1的二进制表示，然后取反，最后加1，就是-1的补码。

```
1的二进制表示：00000001
取反：11111110
加1：11111111
```

所以-1的补码是11111111。

如果我们要计算1+1，首先我们要找到1的补码，然后再相加，最后再判断符号位。

```
1的补码：00000001
1的补码：00000001
相加：00000010
换算成十进制：2
```

如果我们要计算1-1，首先我们要找到1的补码，然后找到-1的补码，再相加，最后再判断符号位。

```
1的补码：00000001
-1的补码：11111111
相加：00000000
换算成十进制：0
```

我们可以看出，2的补码有以下优点：

1. 0的补码是00000000，所以0只有一种表示方法，不会出现正0和负0的问题。
2. 两个数相加，只需要把它们的补码相加，然后舍弃最高位的进位，就是最终的结果。
3. 两个数相减，只需要把减数的补码取反加1，然后和被减数的补码相加，然后舍弃最高位的进位，就是最终的结果。
4. 补码的表示范围是-2^(n-1)到2^(n-1)-1，其中n是bit的位数，而原码和反码的表示范围是-2^(n-1)+1到2^(n-1)-1。

可以看到，补码的形式中，只有一个0，所以不会出现正0和负0的问题，这样就避免了一种情况，同时，两个数相加和相减的操作也变得非常简单，只需要把补码相加即可，简化了硬件的实现。因此，
补码才会被广泛选择作为表示负数的方法。

## 总结

记得初学计算机的时候，觉得补码难以理解，工作以后，才慢慢理解，现实情况中，我们往往会因为实际情况拖鞋，补码就是如此，舍弃了易理解性，但是提高了计算的效率，这就是现实情况中的折中。

软件工程中，到处都是取舍，我们要根据实际情况，选择最合适的方法，往往我们都找不到完美的方案，但是却有一个最合适的方案。

---

##### 相关文章

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
* [Go设计模式：composite模式](/articles/2020_07_02-go_design_pattern_composite.md.html)
* [拯救删除ZFS之后的分区表](/articles/2020_06_25-save_partition_table_zfs.md.html)

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