---
title: 为什么要把复杂的联表操作拆成多个单表查询？
url: https://jiajunhuang.com/articles/2023_02_03-mysql.md.html
source: Jiajun的编程随想
date: 2023-02-04
fetch_date: 2025-10-04T05:39:12.572557
---

# 为什么要把复杂的联表操作拆成多个单表查询？

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

* [为什么要把复杂的联表操作拆成多个单表查询？](#%25E4%25B8%25BA%25E4%25BB%2580%25E4%25B9%2588%25E8%25A6%2581%25E6%258A%258A%25E5%25A4%258D%25E6%259D%2582%25E7%259A%2584%25E8%2581%2594%25E8%25A1%25A8%25E6%2593%258D%25E4%25BD%259C%25E6%258B%2586%25E6%2588%2590%25E5%25A4%259A%25E4%25B8%25AA%25E5%258D%2595%25E8%25A1%25A8%25E6%259F%25A5%25E8%25AF%25A2%25EF%25BC%259F)

# 为什么要把复杂的联表操作拆成多个单表查询？

我们在系统优化的时候，常见的一个操作，就是把复杂的联表操作，拆解成多个单表操作，然后在应用程序中进行联接。为什么要
这样做呢？相信大家都可以列出几点。不过《高性能MySQL 第四版》对此有很好的总结，值得细品。摘录如下：

* 让缓存的效率更高。应用程序中，简单查询对应的代码也会更简单，也就更好设计缓存，应用程序可以拆开来，缓存其中的结果，以便
  下次使用复用
* 将查询分解后，执行单个查询可以减少锁的竞争
* 在应用层做联接，可以更容易对数据库进行拆分，更容易做到高性能和可扩展
* 查询本身的效率可能也会有所提升
* 可以减少对冗余记录的访问，MySQL联表操作可能会访问很多数据，并且可能是重复的访问

除此之外，我个人的补充：

* 将联表操作放到应用层，很大的一个好处是可扩展性。扩展应用层，比扩展数据库要容易的多，通常应用层都是stateless的，可以直接scale
* simple is better，无论对于什么来说都是
* 把操作拆成多个小任务，可以在多个事务中执行，如果一个大事务中，有加锁或者等待，就会阻塞其他事务，拆开以后概率会降低
* 对于整体操作的控制粒度变得更加精细，很多操作都变得更加可控

---

##### 相关文章

* [一个Gunicorn worker数量引发的血案](/articles/2020_03_11-gunicorn_worker.md.html)
* [MySQL Boolean类型的坑](/articles/2020_03_06-mysql_boolean_tinyint_index.md.html)
* [pip freeze是魔鬼](/articles/2020_03_04-pip_list.md.html)
* [一个feed流系统的演进](/articles/2020_03_02-feed_system_design.md.html)
* [Android 使用view binding](/articles/2020_03_01-android_view_binding.md.html)
* [系统调用的过程](/articles/2020_02_27-syscall.md.html)
* [MySQL charset不同导致无法使用索引的坑](/articles/2020_02_26-mysql_charset_index.md.html)
* [微服务的缺点](/articles/2020_02_19-should_i_use_microservice.md.html)
* [远程工作一周有感](/articles/2020_02_14-remote_work.md.html)
* [Python中的并发控制](/articles/2020_02_12-python_concurrency.md.html)
* [KVM spice协议在高分屏上的分辨率问题](/articles/2020_02_08-kvm_spice_high_dpi.md.html)
* [计算机中的权衡(trade-off)](/articles/2020_01_11-paradigm.md.html)
* [[声明]本站所有文章禁止转载](/articles/2020_01_10-please_do_not_copy.md.html)
* [Golang不那么蛋疼的sort](/articles/2020_01_07-golang_sort_slice.md.html)
* [Flutter给Android应用签名](/articles/2020_01_06-flutter_sign_android_apk.md.html)

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