---
title: 红包系统的设计
url: https://jiajunhuang.com/articles/2023_01_31-red_envelope.md.html
source: Jiajun的编程随想
date: 2023-02-01
fetch_date: 2025-10-04T05:18:49.553004
---

# 红包系统的设计

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

* [红包系统的设计](#%25E7%25BA%25A2%25E5%258C%2585%25E7%25B3%25BB%25E7%25BB%259F%25E7%259A%2584%25E8%25AE%25BE%25E8%25AE%25A1)
* [处理峰值（削峰）](#%25E5%25A4%2584%25E7%2590%2586%25E5%25B3%25B0%25E5%2580%25BC%25EF%25BC%2588%25E5%2589%258A%25E5%25B3%25B0%25EF%25BC%2589)
* [数据准确（加锁）](#%25E6%2595%25B0%25E6%258D%25AE%25E5%2587%2586%25E7%25A1%25AE%25EF%25BC%2588%25E5%258A%25A0%25E9%2594%2581%25EF%25BC%2589)
* [分配方案](#%25E5%2588%2586%25E9%2585%258D%25E6%2596%25B9%25E6%25A1%2588)
* [分配算法](#%25E5%2588%2586%25E9%2585%258D%25E7%25AE%2597%25E6%25B3%2595)
* [数据落地方案](#%25E6%2595%25B0%25E6%258D%25AE%25E8%2590%25BD%25E5%259C%25B0%25E6%2596%25B9%25E6%25A1%2588)
* [缓存](#%25E7%25BC%2593%25E5%25AD%2598)
* [总结](#%25E6%2580%25BB%25E7%25BB%2593)

# 红包系统的设计

秒杀系统中，很常见的一种就是抢红包，还有其他的例如：双11抢购、直播间秒杀下单、一元夺宝等等。其中抢红包的特点在于无法超售，
对于下单，如果比库存超售少许，其实是可以接受的，但是对于红包，一旦用户抢到的钱比发出去的钱更多，那就是大问题了。当然，
抢购也有特定的业务复杂度，例如下单之后，用户可能没有付款，超时之后需要重新把库存加回去等。我们这里主要讨论红包系统。

对于红包系统，我们需要保证两点：

1. 扛得住并发，用户抢红包的时候带来的流量峰值是非常高的；
2. 不能超售，数据一定要准确

那么我们怎么处理这两个问题呢？

## 处理峰值（削峰）

对于单个红包来说，红包的可抢人数是有限制的，例如200个，500个，再往上就比较少了，而参与的用户，大部分只要看到红包就会
参与点击，并且大都是多次点击，直到抢完。因此，这种行为带来的一个特点，就是红包发出以后，会迎来一波比红包个数大很多的
流量，但是超过红包个数的流量基本是无用的流量。因此，对于红包系统，我们需要在请求到达真正处理的后端服务之前，加上如下
防火墙，对流量进行过滤：

* 用户组织层限流：限制群组大小，这样就限制了一个红包最大的参与人数，例如一个群组最大2万人。但是有的场景下无法限制，例如
  直播间。这一层面的限制取决于产品形态
* 用户端限流：浏览器、App、小程序等用户参与游戏的客户端，我们可以进行限速操作，例如1s点击一次，点击后1s内按钮置灰不可
  再次点击
* 网关层限流：CDN，Nginx，限速，从这里开始，就涉及到服务端的处理了，这里就涉及到多种策略，例如针对IP限速，针对用户限速等
* 服务层限流：这里需要代码进行处理，例如设置当前参与人数超过红包总数3倍，直接拒绝当前请求，一般会用Redis来存储这个信息
* 应用层限流：当红包抢完之后，可以在Redis中记录一个标记，应用检测到这个信息，就不需要进行后面的操作了，可以直接拒绝

## 数据准确（加锁）

如何保证红包的数据准确性呢？如果是使用数据库来存储的话，就需要使用事务，加上行锁，也就是 `SELECT ... FOR UPDATE` 语句，
如果是使用Redis来存储的话，就需要使用CAS操作，由于Redis中的事务并不保证ACID，但是Lua脚本是原子执行的，因此需要使用Lua
脚本来进行操作。

## 分配方案

对于红包的分配，有两种方案：

* 预分配。发送红包的时候，就提前分配好每一个人能抢到多少，抢红包的时候，取一个未抢的金额出来，分配给对应用户，并且更新状态，
  此处需要保证一个用户在一个红包下，只能抢一次。
* 实时分配。发送红包的时候不分配，在抢红包的时候进行分配，根据红包的剩余金额和剩余个数，计算一个金额给当前用户，此处也许要
  在数据库层面保证一个用户在一个红包下，只能抢一次。

## 分配算法

红包分配算法可以参考微信红包的分配算法：随机，额度在0.01和剩余平均值\*2之间。

## 数据落地方案

* 数据库事务 + `SELECT ... FOR UPDATE`，通过事务保证ACID，通过行锁保证不会产生并发更新错误。
* 数据库集群(分库sharding)，当一个数据库吃不住的时候，可以使用集群来扛并发。
* Redis Lua 脚本，当集群扛不住的时候，就可以考虑使用Redis来进行操作了。但是最终数据还是需要落库到数据库。

因此我实现时，采用的是第一种方案，也就是直接数据库+行锁来实现。使用数据库实现时，需要注意的是避免死锁场景，我就踩到
死锁的坑导致数据库连接池爆了，排查了好一会儿。这种方案对于数据库本身有一定要求，尤其是磁盘IOPS，需要好好的调校数据库以
得到一个比较好的并发性能。

## 缓存

对于红包本身，我认为缓存的必要性不大，因为每一次成功抢红包，都会导致缓存失效，还是需要数据库参与。与之相对的，反而是红包
的基本信息更加管用，例如：

* 当前红包是否已经抢完？可以用于提前拒绝请求
* 当前用户是否抢过？可以用于提前拒绝请求
* 当前用户是否最近1s抢过？可以用于限速

把这些信息写到缓存里，更有助于提高整个系统的并发能力。

## 总结

这篇文章中，总结了一个红包系统需要用到的知识，以及如何取处理流量和如何设计系统。

---

* <https://www.zybuluo.com/yulin718/note/93148>
* <https://www.postgresql.org/docs/current/explicit-locking.html#LOCKING-ROWS>

---

##### 相关文章

* [Nginx 请求匹配规则](/articles/2017_10_18-nginx_request_handle.md.html)
* [Web开发系列(六)：关系型数据库，ORM](/articles/2017_10_18-web_dev_part6.md.html)
* [Web开发系列(五)：form, json, xml](/articles/2017_10_17-web_dev_part5.md.html)
* [Web开发系列(四)：Flask, Tornado和WSGI](/articles/2017_10_16-web_dev_part4.md.html)
* [Web开发系列(三)：什么是HTML,CSS,JS？](/articles/2017_10_15-web_dev_part3.md.html)
* [Web开发系列(二)：HTTP协议](/articles/2017_10_14-web_dev_part2.md.html)
* [Web开发系列(一)：从输入网址到最后，这个过程经历了什么？](/articles/2017_10_13-web_dev_part1.md.html)
* [SNI: 让Nginx在一个IP上使用多个证书](/articles/2017_10_11-sni.md.html)
* [Haskell: infixl, infixr, infix](/articles/2017_09_27-haskell_infix.md.html)
* [Haskell简明教程（五）：处理JSON](/articles/2017_09_26-learn_you_a_haskell_part_5.md.html)
* [Haskell简明教程（四）：Monoid, Applicative, Monad](/articles/2017_09_25-learn_you_a_haskell_part_4.md.html)
* [HTTPS 的详细流程](/articles/2017_09_22-https_processes.md.html)
* [OAuth2 为什么需要 Authorization Code?](/articles/2017_09_21-oauth2.md.html)
* [任务队列怎么写？python rq源码阅读与分析](/articles/2017_09_20-task_queue_python_rq.md.html)
* [XMonad 配置教程](/articles/2017_09_19-xmonad.md.html)

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