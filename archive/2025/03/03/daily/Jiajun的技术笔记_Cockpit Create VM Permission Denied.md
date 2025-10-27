---
title: Cockpit Create VM Permission Denied
url: https://jiajunhuang.com/articles/2025_03_02-cockpit_vm_create_permission_denied.md.html
source: Jiajun的技术笔记
date: 2025-03-03
fetch_date: 2025-10-06T21:56:03.510995
---

# Cockpit Create VM Permission Denied

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

* [Cockpit Create VM Permission Denied](#Cockpit%2bCreate%2bVM%2bPermission%2bDenied)

# Cockpit Create VM Permission Denied

I’ve met an error:

When I’m creating a Windows VM by using “Cockpit Virtual Machine”, I want to use
virtio so I have to append an virtio iso image as cdrom. But once you click
the “Install” button, you will meet the error:

“permission denied” on creating system VM with iso file in home directory”.

I’ve searched for the error in the internet but no resolution found, after several
times trying I got how to resolve the problem:

Simply do not insert an virtio cdrom, just click “Install” button, and after
you run into the Windows installation program, return to the Cockpit WebUI
and then eject the windows iso cdrom, and inject virtio iso cdrom, after scan and
install the virtio driver, reject the virtio iso cdrom and then inject the windows
iso cdrom again.

Simple but a working solution :)

---

##### 相关文章

* [MySQL 零碎知识 - MySQL必知必会](/articles/2017_07_26-mysql.md.html)
* [Golang slice 源码阅读与分析](/articles/2017_07_18-golang_slice.md.html)
* [经典好书推荐(2017)](/articles/2017_07_15-books.md.html)
* [Golang log库 源码阅读与分析](/articles/2017_07_11-golang_log.md.html)
* [毕业后一年](/articles/2017_07_02-one_year_after_graduate.md.html)
* [ansible 简明教程](/articles/2017_06_22-ansible.md.html)
* [自己写个搜索引擎](/articles/2017_06_02-write_yourself_a_simple_search_engine.md.html)
* [HTTP 路由的两种常见设计形式](/articles/2017_05_24-http_router_design.md.html)
* [Golang的short variable declaration](/articles/2017_05_12-golang_short_variable_declaration.md.html)
* [Greenlet和Stackless Python](/articles/2017_04_26-greenlet.md.html)
* [写一个简单的ORM](/articles/2017_04_25-write_your_own_orm.md.html)
* [从源码看Python的descriptor](/articles/2017_04_19-python_descriptor_from_source_code.md.html)
* [Python字符串格式化](/articles/2017_04_16-python_string_format.md.html)
* [Gunicorn 简明教程](/articles/2017_04_08-gunicorn.md.html)
* [Raft 论文阅读笔记](/articles/2017_03_29-raft.md.html)

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