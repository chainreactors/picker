---
title: Clash 结合 工作VPN 的网络设计
url: https://jiajunhuang.com/articles/2024_03_08-clash_vpn.md.html
source: Jiajun的技术笔记
date: 2024-03-09
fetch_date: 2025-10-04T12:07:32.670984
---

# Clash 结合 工作VPN 的网络设计

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

* [Clash 结合 工作VPN 的网络设计](#Clash%2b%25E7%25BB%2593%25E5%2590%2588%2b%25E5%25B7%25A5%25E4%25BD%259CVPN%2b%25E7%259A%2584%25E7%25BD%2591%25E7%25BB%259C%25E8%25AE%25BE%25E8%25AE%25A1)

# Clash 结合 工作VPN 的网络设计

这个是我曾经探索实践过的方案，主要用于学习工作，但是看网络上有不少人有同样的疑惑，因此整理一下分享给大家。
Clash是一个网络分流工具，为了方便使用，我直接在 OpenWRT 也就是路由器这一层面搭建的Clash，因此只要在局域网内都可以获得流畅的网络。

> 请注意，本文没有写的特别详细，需要一定的网络基础功才能看懂。

但是有这么一种情况，就是有可能你公司的VPN，和clash的规则冲突，尤其是当你启用了clash的 fake-ip 功能以后。

解决方案的核心，其实就是使用 clash 规则中的 `SRC-IP-CIDR`，以及 `fake-ip-filter`。

首先我们看看出问题的网络架构：

![Network does not work with VPN](./img/network_not_work_with_vpn.png)

每个公司的VPN都有自己的一套路由规则，有的是全局代理，有的是规则代理。Clash的原理，其实也是按照规则来路由流量，
这两者很有可能就会冲突，因此我的做法就是，划分一台独立的设备，这样就可以获得局域网内一个IP地址，然后设置为固定IP。
然后在 clash 上配置，从这个IP发出的流量，一律直连，这样就相当于在局域网的网络规则中开了一个特殊通道，让VPN能够正常连上
公司的服务器。

配置方法，就是在 `config.yml` 中，`rules` 下添加一条特殊规则：

> `config.yml` 是clash的配置文件

```
rules:
- SRC-IP-CIDR,192.168.100.3/32,DIRECT
```

这样就实现了只要是从这台机器的流量，全都会直接打到 VPN server 上。但是如果你的工作VPN不是全局模式，而是规则代理模式，而
恰好你的clash使用的是 fake-ip 模式，那有可能有一些内部网站你仍然无法访问，因为 `fake-ip` 模式给了你一个假的解析出来的地址，
恰好这个IP地址没有命中VPN的路有规则，解决办法也很简单，就是在 `config.yml` 的 `fake-ip-filter` 中加入你的域名，例如：

```
fake-ip-filter:
- '*.lan'
- '*.localdomain'
- '*.example'
```

公司 VPN 的网络问题解决了，那么你的笔记本或者台式机，要怎么访问呢？我的办法是在这台独立的机器上搭建 `socks5` 服务，
然后笔记本或者台式机使用 SwitchOmega/SmartProxy 等连接到 `socks5` 服务，从而使用VPN网络中的流量，网络拓扑如下：

![Network with VPN](./img/network_work_with_vpn.png)

搭建 socks5 服务，常见的就是又搞 ss/clash 等，但是我有一个更简单的办法：

```
$ ssh -D $port_number $username@$hostname
# 例如
$ ssh -D 1081 [email protected]
```

然后笔记本或者台式机直接使用 `127.0.0.1:1081` 的 socks5 代理即可临时使用VPN网络，其余时候就关闭 SwitchOmega/SmartProxy 使用直连网络，
或者不怕麻烦的话，配置一个规则，按域名走不同的代理即可。

---

##### 相关文章

* [foldl 和 foldr 的变换](/articles/2016_05_22-foldl_and_foldr.rst.html)
* [Haskell TypeClass 笔记](/articles/2016_05_05-typeclassopedia.rst.html)
* [重新捡起你那吃灰的树莓派](/articles/2016_04_03-raspberrypi.rst.html)
* [Tornado 源码阅读](/articles/2016_03_14-tornado.rst.html)
* [JavaScript权威指南笔记](/articles/2016_03_06-notes_on_js_the_definitive_guide.rst.html)
* [Python零碎知识汇总](/articles/2016_03_05-python_fragmentary_knowledge.rst.html)
* [C语言的位操作](/articles/2016_02_06-bitwise_operation.rst.html)
* [分治](/articles/2016_01_25-divide_and_conqure.rst.html)
* [关于python的decorator和descriptor](/articles/2015_12_05-python_descriptor_and_decorator.rst.html)
* [程序设计实践笔记](/articles/2015_10_09-notes_on_the_practice_of_programming.rst.html)
* [Thinking Recursively](/articles/2015_09_05-thinking_recursively.rst.html)
* [Block I/O](/articles/2015_06_22-notes_on_linux_kernel_development_chap14.rst.html)
* [如何解读c的声明](/articles/2015_03_17-declaration_of_c_pointers.rst.html)
* [关于输入法的猜想](/articles/2015_01_11-my_guess_about_input_method.rst.html)
* [C语言与抽象思维](/articles/2014_12_12-abstractions_in_c.rst.html)

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