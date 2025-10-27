---
title: PostgreSQL 当MQ来使用
url: https://jiajunhuang.com/articles/2024_03_09-postgresql_as_mq.md.html
source: Jiajun的技术笔记
date: 2024-03-10
fetch_date: 2025-10-04T12:08:18.387109
---

# PostgreSQL 当MQ来使用

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

* [PostgreSQL 当MQ来使用](#PostgreSQL%2b%25E5%25BD%2593MQ%25E6%259D%25A5%25E4%25BD%25BF%25E7%2594%25A8)
* [设计存储表](#%25E8%25AE%25BE%25E8%25AE%25A1%25E5%25AD%2598%25E5%2582%25A8%25E8%25A1%25A8)
* [生产任务](#%25E7%2594%259F%25E4%25BA%25A7%25E4%25BB%25BB%25E5%258A%25A1)
* [取任务消费](#%25E5%258F%2596%25E4%25BB%25BB%25E5%258A%25A1%25E6%25B6%2588%25E8%25B4%25B9)
* [更新任务状态](#%25E6%259B%25B4%25E6%2596%25B0%25E4%25BB%25BB%25E5%258A%25A1%25E7%258A%25B6%25E6%2580%2581)
* [任务重试](#%25E4%25BB%25BB%25E5%258A%25A1%25E9%2587%258D%25E8%25AF%2595)
* [定期清理过期任务](#%25E5%25AE%259A%25E6%259C%259F%25E6%25B8%2585%25E7%2590%2586%25E8%25BF%2587%25E6%259C%259F%25E4%25BB%25BB%25E5%258A%25A1)
* [总结](#%25E6%2580%25BB%25E7%25BB%2593)

# PostgreSQL 当MQ来使用

一般我们都是用 Redis/RabbitMQ等等 来做MQ，那么，能不能使用关系型数据库来做这件事情呢？显然，可以。

## 设计存储表

首先我们要创建一张表，来存储消息：

```
create table pg_queue (
    id serial primary key,
    queue_name text not null,
    payload jsonb not null,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone default now(),
    executed_at timestamp with time zone default now(),
    status text default 'pending'
);

-- add index
create index pg_queue_queue_name_status_idx on pg_queue (queue_name, status, executed_at);
```

请注意，上面的字段中，`executed_at` 是执行时间，这样我们可以实现定时执行，这在常见的MQ里可是一个相对高级的属性了，
`status` 为该任务的状态，我设计的MQ里，有 `pending`, `processing`, `done`, `failed` 等几种状态，如果想要实现ACK，
那完全可以再加一种 `ack` 的状态进去。`queue_name` 是队列名，有这一个字段就可以实现多个队列，`payload` 是消息内容。

然后创建一个联合索引，这可不就妥妥的一个高级队列出来了么。

### 生产任务

```
-- add task to queue
INSERT INTO pg_queue (queue_name, payload) VALUES ('test', '1');
INSERT INTO pg_queue (queue_name, payload) VALUES ('test', '2');
INSERT INTO pg_queue (queue_name, payload) VALUES ('test', '3');
INSERT INTO pg_queue (queue_name, payload) VALUES ('test', '4');
INSERT INTO pg_queue (queue_name, payload) VALUES ('test', '5');
INSERT INTO pg_queue (queue_name, payload) VALUES ('test', '6');
INSERT INTO pg_queue (queue_name, payload) VALUES ('test', '7');
INSERT INTO pg_queue (queue_name, payload) VALUES ('test', '8');
INSERT INTO pg_queue (queue_name, payload) VALUES ('test', '9');
INSERT INTO pg_queue (queue_name, payload) VALUES ('test', '10');
```

上述SQL会插入任务，默认的执行时间就是立即执行，如果需要做延时的话，就可以指定 `executed_at` 字段。

## 取任务消费

```
-- get task from queue
UPDATE pg_queue SET status = 'processing', updated_at = NOW() WHERE id = (
    SELECT id FROM pg_queue WHERE queue_name = 'test' AND status = 'pending' AND executed_at <= NOW() ORDER BY id LIMIT 1 FOR UPDATE SKIP LOCKED
) RETURNING id, queue_name, payload, created_at, updated_at, executed_at, status;
```

这里的SQL，意思是取 `test` 队列中，状态为 `pending` 且到了执行时间的任务，一次取一个（可以调整为多个），跳过已经被锁定的任务。

## 更新任务状态

```
-- mark task as done
UPDATE pg_queue SET status = 'done', updated_at = NOW() WHERE id = 1;
```

```
-- mark task as failed
UPDATE pg_queue SET status = 'failed', updated_at = NOW() WHERE id = 1;
```

## 任务重试

```
-- auto retry task if status is failed
UPDATE pg_queue SET status = 'pending', updated_at = NOW(), executed_at = NOW() WHERE queue_name = 'test' AND status = 'failed' AND executed_at <= NOW();
```

## 定期清理过期任务

```
-- auto truncate pg_queue
DELETE FROM pg_queue WHERE created_at < NOW() - INTERVAL '1 day';
```

## 总结

不愧是PG，通过这么几个简单的SQL，就可以实现一个高级队列，支持：

* 持久化、事务支持
* 多端写入
* 多端消费
* 延时任务、定时任务
* 历史消息记录
* ACK(如果想要的话完全可以用 `status` 字段实现)
* 多队列(框架内可以实现优先队列)支持，延时队列，死信队列(加一个状态即可)
* 批量发送和接收
* 重试、重入队列

其余的高级特性，都可以通过一个辅助性框架来实现。

---

##### 相关文章

* [Python Requests 简明教程](/articles/2019_05_18-requests.md.html)
* [密码技术简明教程(三)：证书和TLS](/articles/2019_05_15-crypto_part3.md.html)
* [密码技术简明教程(二)：散列、消息认证码和数字签名](/articles/2019_05_14-crypto_part2.md.html)
* [SEO学习笔记](/articles/2019_05_14-seo.md.html)
* [密码技术简明教程(一)：对称加密和非对称加密](/articles/2019_05_12-crypto.md.html)
* [Kubernetes 笔记](/articles/2019_05_10-kubernetes_tutorial.md.html)
* [go mod 和 logrus 路径大小写的问题](/articles/2019_05_09-go_mod_logrus.md.html)
* [Flask自动加载Blueprint](/articles/2019_05_08-flask_load_bp_automaticly.md.html)
* [在KVM里安装Minikube](/articles/2019_05_07-minikube_kvm.md.html)
* [搞定面试中的系统设计题](/articles/2019_04_29-system_design.md.html)
* [Crontab + Sendmail实现定时任务并且通知](/articles/2019_04_25-crontab_sendmail.md.html)
* [Nginx设置Referer来防止盗图](/articles/2019_04_23-nginx_referer.md.html)
* [Graphviz dot简明教程](/articles/2019_04_20-graphviz_dot.md.html)
* [jQuery简明教程](/articles/2019_04_19-jquery.md.html)
* [Python RQ(Redis Queue)添加gevent支持](/articles/2019_04_18-python_rq_gevent.md.html)

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