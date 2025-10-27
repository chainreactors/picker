---
title: 再读《程序员修炼之道-从小工到专家》
url: https://jiajunhuang.com/articles/2024_09_07-the_pragmatic_programmer.md.html
source: Jiajun的技术笔记
date: 2024-09-08
fetch_date: 2025-10-06T18:22:13.870051
---

# 再读《程序员修炼之道-从小工到专家》

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

* [再读《程序员修炼之道-从小工到专家》](#%25E5%2586%258D%25E8%25AF%25BB%25E3%2580%258A%25E7%25A8%258B%25E5%25BA%258F%25E5%2591%2598%25E4%25BF%25AE%25E7%2582%25BC%25E4%25B9%258B%25E9%2581%2593-%25E4%25BB%258E%25E5%25B0%258F%25E5%25B7%25A5%25E5%2588%25B0%25E4%25B8%2593%25E5%25AE%25B6%25E3%2580%258B)
* [测试](#%25E6%25B5%258B%25E8%25AF%2595)
* [不留破窗](#%25E4%25B8%258D%25E7%2595%2599%25E7%25A0%25B4%25E7%25AA%2597)
* [正交性](#%25E6%25AD%25A3%25E4%25BA%25A4%25E6%2580%25A7)
* [自动化](#%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596)
* [好文档，好注释](#%25E5%25A5%25BD%25E6%2596%2587%25E6%25A1%25A3%25EF%25BC%258C%25E5%25A5%25BD%25E6%25B3%25A8%25E9%2587%258A)

# 再读《程序员修炼之道-从小工到专家》

我单独拎出几个觉得很重要的点，作为笔记。

## 测试

> Test Early. Test Ofen. Test Automatically.

软件质量保证是一个非常重要的事情，其中测试就是主要手段。测试包括手动测试和自动化测试。

手动测试，是指人工操作软件，检查软件的功能是否正常。这种测试效率低，容易出错，可控性相对较低。但是很多场景还是
非常有必要的，比如变动非常快的UI界面，或者一些复杂的交互逻辑。这种场景使用自动化测试，那么测试覆盖和维护的成本
都会非常高。

自动化测试，就是机器来跑，现在的工作中，主要在这么几个场景下，配合CI/CD使用：

* 代码提交时，PR中跑单元测试和集成测试
* 代码合并时，跑单元测试和集成测试
* 部署前，拉分支时，跑单元测试和集成测试
* 定时触发 e2e 测试
* 定时触发性能测试
* 定时触发安全测试(很少见)

单元测试和集成测试的区别，单元测试是对一个模块的测试，集成测试是对多个模块的测试，主要在于一个颗粒度的不同。
e2e 测试是端到端测试，是对整个系统的测试，主要是测试系统的功能是否正常，是以用户视角来看的，一般就是模拟用户的操作，
来调用API，甚至有些场景还会模拟用户的行为，比如点击，输入等。

不仅要测试，要早测试，要多测试，而且要自动化测试(当然并不是说不要手动测试)！

## 不留破窗

有问题就要修复，越等到后面修复的成本越高。

不要温水煮青蛙，一旦习惯了破窗，就会变成习惯，最后就会变成了一种文化。

## 正交性

正交性是指，系统中的各个部分之间是独立的，互不影响。这样的系统更容易维护，更容易扩展。我们常说的解耦，其实就是
为了提高正交性。

想象一下，如果你在驾驶一辆新的汽车，汽车没有正交性。转动方向盘的时候，可能会提升车速，换挡的时候，方向盘会打转，
刹车的时候，可能会加速。这样的汽车，你敢开吗？

软件也是一样的。UNIX文化常说的 KISS 和 DRY，也是为了提高正交性。

## 自动化

能自动化的，都自动化！

## 好文档，好注释

首先要有一个好的代码，如果代码本身命名清晰，逻辑清晰，其实是不需要注释的。如果代码比较复杂，或者有一些历史逻辑或者
特殊处理，那么则需要配备对应的注释和文档。

---

##### 相关文章

* [gRPC错误处理](/articles/2020_11_26-grpc_error_handle.md.html)
* [Java collection的结构](/articles/2020_11_13-java_colletions.md.html)
* [为啥Redis使用pipelining会更快？](/articles/2020_11_02-why_pipelining_fast.md.html)
* [通过阳台种菜实现蔬菜自由](/articles/2020_10_24-vegetable.md.html)
* [从GORM里学习到的panic处理方式](/articles/2020_10_19-gorm_paniced.md.html)
* [Go使用闭包简化数据库操作代码](/articles/2020_10_17-golang_db_transaction.md.html)
* [TCMalloc设计文档学习](/articles/2020_10_10-tcmalloc.md.html)
* [Flask和requests做一个简单的请求代理](/articles/2020_09_27-flask_proxy.md.html)
* [Linux常用命令(四)：xargs](/articles/2020_09_21-linux_cmd_xargs.md.html)
* [Linux常用命令(三)：watch](/articles/2020_09_20-linux_cmd_watch.md.html)
* [Linux常用命令(二)：htop](/articles/2020_09_20-linux_cmd_htop.md.html)
* [Linux常用命令(一)：netcat](/articles/2020_09_19-linux_cmd_netcat.md.html)
* [结合Flask 与 marshmallow快速进行参数校验](/articles/2020_09_16-flask_marshmallow.md.html)
* [规整数据的重要性](/articles/2020_09_10-form_check.md.html)
* [apt安装特定包以及忽略升级某个包](/articles/2020_09_05-apt.md.html)

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