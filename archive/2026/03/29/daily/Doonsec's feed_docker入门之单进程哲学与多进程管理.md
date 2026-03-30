---
title: docker入门之单进程哲学与多进程管理
url: https://mp.weixin.qq.com/s/-Oeb5smNoRQuGwrejPv59A
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:42:21.750962
---

# docker入门之单进程哲学与多进程管理

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RJrNBTwulvc7Ave3SUupgq8q203XMwcuwk3qhbLBxG1SHtRVq7184uuO1yE67nv994aibHkibBRVIRWfx4QoOSFPkibkj5WfHbITicy8uS2Gic4A/0?wx_fmt=jpeg)

# docker入门之单进程哲学与多进程管理

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器中沉浸阅读

# 缘起

今天有空，琢磨以下docker的单进程哲学与实际使用中的多进程管理

## 单进程哲学

一般解释docker的方式是：docker是轻量化的虚拟机

二者还是有着本质的区别：虚拟机通过Hypervisor模拟完整的硬件环境，每个虚拟机都运行着独立的操作系统内核和完整的系统进程。而容器则采用了完全不同的技术路径——它本质上只是宿主机上的一个进程，通过Linux Namespace和Cgroups技术实现了进程级别的隔离。

这种根本性的差异决定了容器的设计哲学。虚拟机可以承载完整的操作系统和多个进程，而容器则专注于单一职责。每个容器就像是一个"集装箱"，只装载特定的"货物"（应用程序），而不是整个"仓库"（操作系统环境）

## 多进程需求

需要澄清的是，"单进程模型"这一表述有时会引起误解。它并非指容器内只能存在一个操作系统进程，而是强调容器应该只有一个主关注点、一个核心功能。现实需求也是，很多应用系统不可能只有一个进程，例如docker安装的nginx，谁知道知道nginx有master和无数worker进程。

然而，docker的单进程哲学和技术路径，导致了他并没有完整的守护进程，所以进程的管理，就必须自己动手了。

补充知识：容器内的PID=1的进程（init进程）必须是应用程序的主进程，这个进程负责管理容器内的所有资源。

## 方案一：纯手工，Bash Shell 脚本（最原始，但最灵活）

通过编写一个 entrypoint.sh 脚本，手动启动多个后台进程，并使用 wait 命令阻塞主进程，确保容器持续运行。

```
# entrypoint.sh#!/bin/bash
# 启动第一个服务start1 > /var/log/start1.log 2>&1 &
# 启动第二个服务  start2 > /var/log/start2.log 2>&1 &
# 保持脚本运行，防止容器退出wait
```

### 📌 优点

* **零依赖**：无需安装额外工具，适合极简场景。
* **完全可控**：脚本逻辑自由，可嵌入复杂判断、日志、重启逻辑。
* **轻量**：无额外资源开销。

### ❌ 缺点

* **缺乏健壮性**：进程崩溃后不会自动重启（除非手动加 `while` 循环）。
* **难以监控**：无法实时查看各进程状态。
* **配置易出错**：需手动管理 PID、信号、日志重定向等，维护成本高。

## 方案二: 借助第三方控件

### 第一种，轻量级：Monit（轻量级进程监控工具）

开源轻量级：https://mmonit.com/monit/

```
# monitrccheck process nginx with pidfile /var/run/nginx.pid    start program = "/etc/init.d/nginx start"    stop program = "/etc/init.d/nginx stop"    if failed host 127.0.0.1 port 80 then restart
check process flask with pidfile /tmp/flask.pid    start program = "/usr/bin/python app.py"    stop program = "/usr/bin/kill -TERM `cat /tmp/flask.pid`"    if failed port 5000 then restart
```

### 📌 优点

* **自动重启**：进程异常退出后可自动拉起。
* **资源监控**：支持 CPU、内存、磁盘使用率监控。
* **配置清晰**：基于文本配置，易于理解。
* **支持告警**：可通过邮件、Webhook 发送通知。

### ❌ 缺点

* **配置稍复杂**：需编写 `.monitrc` 配置文件。
* **资源占用略高**：相比纯脚本，多一个守护进程。
* **功能较基础**：不支持复杂依赖管理或进程间通信。

### 第二种，轻量级：supervisord（轻量级进程监控工具）

地址：https://supervisord.org/

Supervisor 是 Python 编写的进程管理工具，通过配置文件定义多个进程，支持自动启动、重启、日志管理。

### 📌 优点

* **配置简单**：INI 风格配置，易读易写。
* **功能完整**：支持日志、权限、用户、事件触发。
* **社区成熟**：文档丰富，兼容性好。

### ❌ 缺点

* **资源占用高**：Python 进程 + 一个守护进程，内存开销大。
* **启动慢**：需加载 Python 环境。

怎么说呢，一般建议你做到的gitlab、apache这种类型的docker部署，否则还是不用了，太重，太复杂

不过，学是必须学的，毕竟太多重要的开源项目都用，不学点用起来不得要领啊

### 第三种，s6-overlay（现代、强大、推荐）

地址： https://github.com/just-containers/s6-overlay

S6 是一个功能强大的进程管理器，源自 `s6-overlay`，支持服务分组、依赖管理、信号转发、日志轮转等。

### 📌 优点

* **功能全面**：支持服务依赖、自动重启、日志管理、信号转发。
* **模块化设计**：每个服务独立配置，易于维护。
* **轻量高效**：相比 Supervisor，资源占用更低。
* **生产级稳定**：被广泛用于 Alpine Linux 和容器化环境。

### ❌ 缺点

* **学习成本高**：配置语法较复杂，需理解 S6 的目录结构（`/etc/s6/`）。

一般的小项目，不建议碰，磨刀的功夫超过砍柴的功夫，就得不偿失了

但是有志于提高项目质量，这就是绕不过的。

## 小结

随着越来越多的项目使用docker打包，就会对进程管理的需求越来越甚，接触到这些开源管理方案，是迟早的事儿。

之前一直跟着搜索到的文章，懵懵懂懂的照抄，今天才有空彻底的总结一下基本概念。

后面准备给每个方案，来一个实例，对比一下功能的具体功用和资源占用。

推荐其他docker文章：

[探索springboot程序打包docker的最佳方式](https://mp.weixin.qq.com/s?__biz=MzA3MDg4MjA4Mw==&mid=2649651111&idx=1&sn=efd1e7bab6a8d95247470fb876f39915&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

一只岸上的鱼

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过