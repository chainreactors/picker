---
title: Flatpak 使用小记
url: https://jiajunhuang.com/articles/2024_03_19-flatpak.md.html
source: Jiajun的技术笔记
date: 2024-03-20
fetch_date: 2025-10-04T12:07:31.650563
---

# Flatpak 使用小记

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

* [Flatpak 使用小记](#Flatpak%2b%25E4%25BD%25BF%25E7%2594%25A8%25E5%25B0%258F%25E8%25AE%25B0)
* [安装 Flatpak](#%25E5%25AE%2589%25E8%25A3%2585%2bFlatpak)
* [安装Flatpak源](#%25E5%25AE%2589%25E8%25A3%2585Flatpak%25E6%25BA%2590)

# Flatpak 使用小记

一般的软件，都是直接用apt安装，不过桌面上有一些软件例如浏览器，是更新很频繁的，apt仓库的基本都过时了老旧了，因此有了
flatpak 和 snap 这样的软件，不过我不是很喜欢snap，正好今天尝试了一下 flatpak，以Ubuntu/Debian为例。

## 安装 Flatpak

```
$ sudo apt install flatpak
```

如果是比较老版本的OS，那么可以选择用PPA：

```
$ sudo add-apt-repository ppa:flatpak/stable
$ sudo apt update
$ sudo apt install flatpak
```

## 安装Flatpak源

```
$ flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

如果在国内，可以替换为国内镜像源：

```
$ sudo flatpak remote-modify flathub --url=https://mirror.sjtu.edu.cn/flathub
```

然后重启一下系统，再次进入之后，就可以用 flatpak 安装软件了，例如安装Firefox：

```
$ flatpak install flathub org.mozilla.firefox
```

运行：

```
$ flatpak run org.mozilla.firefox
```

---

##### 相关文章

* [KVM spice协议在高分屏上的分辨率问题](/articles/2020_02_08-kvm_spice_high_dpi.md.html)
* [计算机中的权衡(trade-off)](/articles/2020_01_11-paradigm.md.html)
* [[声明]本站所有文章禁止转载](/articles/2020_01_10-please_do_not_copy.md.html)
* [Golang不那么蛋疼的sort](/articles/2020_01_07-golang_sort_slice.md.html)
* [Flutter给Android应用签名](/articles/2020_01_06-flutter_sign_android_apk.md.html)
* [使用Gitea+Drone打造自己的CI/CD系统](/articles/2020_01_01-use_gitea_with_drone.md.html)
* [2019年就要结束啦！](/articles/2019_12_31-hello_2020.md.html)
* [为什么要使用gRPC？](/articles/2019_12_27-why_grpc.md.html)
* [Matebook X Pro 2019安装Debian 10](/articles/2019_12_24-matebook_x_pro_2019_debian_10.md.html)
* [ArchLinux忽略某个包的升级](/articles/2019_12_22-archlinux_ignore_pkg.md.html)
* [SQLAlchemy使用主从与数据库autocommit](/articles/2019_12_21-autocommit.md.html)
* [Blackbox禁用IPv6](/articles/2019_12_19-blackbox_disable_ipv6.md.html)
* [Go 1.13的errors挺香](/articles/2019_12_18-golang_133_errors.md.html)
* [预防缓存击穿](/articles/2019_12_18-cache_miss.md.html)
* [flutter开发体验汇报](/articles/2019_12_16-flutter_dev.md.html)

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