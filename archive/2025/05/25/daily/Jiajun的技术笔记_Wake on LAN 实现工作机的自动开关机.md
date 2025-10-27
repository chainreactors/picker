---
title: Wake on LAN 实现工作机的自动开关机
url: https://jiajunhuang.com/articles/2025_05_24-wake_on_lan.md.html
source: Jiajun的技术笔记
date: 2025-05-25
fetch_date: 2025-10-06T22:26:36.382728
---

# Wake on LAN 实现工作机的自动开关机

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

* [Wake on LAN 实现工作机的自动开关机](#Wake%2bon%2bLAN%2b%25E5%25AE%259E%25E7%258E%25B0%25E5%25B7%25A5%25E4%25BD%259C%25E6%259C%25BA%25E7%259A%2584%25E8%2587%25AA%25E5%258A%25A8%25E5%25BC%2580%25E5%2585%25B3%25E6%259C%25BA)
* [自动关机](#%25E8%2587%25AA%25E5%258A%25A8%25E5%2585%25B3%25E6%259C%25BA)
* [自动开机](#%25E8%2587%25AA%25E5%258A%25A8%25E5%25BC%2580%25E6%259C%25BA)

# Wake on LAN 实现工作机的自动开关机

我的工作机是一台配置较高的台式机，同时也就意味着，开机以后，功率比较高。之前还不觉得，买了一个统计功率的插座发现，待机
都能80多瓦，为了避免不必要的浪费，因此决定折腾一下自动开关机。

## 自动关机

这个简单，root用户设置一个crontab就可以：

```
0 22 * * * /usr/sbin/shutdown -h now
```

## 自动开机

这就需要用 Wake on LAN。原理就是，在主板打开这个功能，网卡设置好的情况下，局域网内一台机器向指定的MAC地址发送一个魔术包，
机器收到以后就会自启动。

首先，使用 NetworkManager 设置对应的网卡，启用 Wake on LAN。然后，在主板上找到对应的开关，打开它。

然后，由于我的路由器是 OpenWRT，所以可以直接也添加一个 crontab:

```
0 8 * * * /usr/bin/etherwake -D -i br-lan <MAC地址>
```

这样就可以在早上 8 点自动开机了。

---

Ref:

* <https://wiki.archlinux.org/title/Wake-on-LAN>

---

##### 相关文章

* [Nginx 源码阅读（一）: 启动流程](/articles/2022_03_21-nginx_source_code_1.md.html)
* [Go 泛型简明教程](/articles/2022_03_17-go_generics.md.html)
* [KVM 显卡穿透给 Windows](/articles/2022_03_15-kvm_windows_gpu_passthrough.md.html)
* [使用 HTTP Router 处理 Telegram Bot 按钮回调](/articles/2022_03_12-tgbot_httprouter.md.html)
* [使用反射(reflect)对结构体赋值](/articles/2022_01_10-reflect_binding_args.md.html)
* [GIN 是如何绑定参数的](/articles/2022_01_09-gin_binding_args.md.html)
* [你好 2022(2021 年终总结)](/articles/2021_12_30-hello_2022.md.html)
* [用Go导入大型CSV到PostgreSQL](/articles/2021_12_11-go_copy_large_file_to_pg.md.html)
* [使用 OpenWRT 搭建软路由](/articles/2021_12_01-openwrt.md.html)
* [使用软KVM切换器 barrier 共享键鼠](/articles/2021_11_26-use_barrier.md.html)
* [SQL 防注入及原理](/articles/2021_11_04-sql_injection.md.html)
* [使用 gomock 测试 Go 代码](/articles/2021_10_12-go_mock.md.html)
* [gevent不是黑魔法(二): gevent 实现](/articles/2021_10_11-gevent_is_good_part2.md.html)
* [gevent不是黑魔法(一): greenlet 实现](/articles/2021_09_29-gevent_is_good_part1.md.html)
* [用 entgo 替代 gorm](/articles/2021_09_06-use_entgo.md.html)

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