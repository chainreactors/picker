---
title: OpenWRT 使用 Android/iOS USB 网络
url: https://jiajunhuang.com/articles/2022_12_04-openwrt_usb.md.html
source: Jiajun的编程随想
date: 2022-12-05
fetch_date: 2025-10-04T00:30:41.444623
---

# OpenWRT 使用 Android/iOS USB 网络

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

* [OpenWRT 使用 Android/iOS USB 网络](#OpenWRT%2b%25E4%25BD%25BF%25E7%2594%25A8%2bAndroid%252FiOS%2bUSB%2b%25E7%25BD%2591%25E7%25BB%259C)

# OpenWRT 使用 Android/iOS USB 网络

我所在的地方网络不好，于是计划用 4G/5G 网络，但是开热点有个缺点，那就是WiFi本身新号未必稳定，第二无法让它经过OpenWRT
实现全局科学上网。一个方案是购买 CPE，也就是 4G路由器，或者5G路由器，将手机信号转换成有线信号，然后作为 OpenWRT 的
网络入口。

但是，作为一个折腾党(qiong)，怎么会花 400⁄1200 去买一个CPE呢？于是，我将目光转向了旧的安卓手机。

> 我试过，iPhone 也可以，不过最后我用旧安卓来做了，因此下文使用安卓作为示例。

由于我的OpenWRT是在虚拟机里，所以我可以直接将手机通过数据线插到主机的USB接口上，然后在virt manager上，将宿主机的USB
设备穿透给虚拟机。如果你使用的是实体刷了OpenWRT的机器，就需要你的机器上有一个USB接口。

然后要做的事情是在 OpenWRT 上安装软件包，用于识别安卓/iOS设备：

```
# opkg update
# opkg install kmod-usb-net-rndis kmod-usb-net-cdc-ncm kmod-usb-net-huawei-cdc-ncm kmod-usb-net-cdc-eem kmod-usb-net-cdc-ether kmod-usb-net-cdc-subset kmod-nls-base kmod-usb-core kmod-usb-net kmod-usb-net-cdc-ether kmod-usb2
```

> 直接全装了，因为我是虚拟机，磁盘足够大。如果是路由器，那么请酌情减少，主要还是看你的手机需要哪个包。

如果是 iOS 设备，执行：

```
opkg update
opkg install kmod-usb-net-ipheth usbmuxd libimobiledevice usbutils

# Call usbmuxd
usbmuxd -v

# Add usbmuxd to autostart
sed -i -e "\$i usbmuxd" /etc/rc.local
```

接着就可以在手机上打开USB共享网络，然后在 luci 页面上，增加设备和接口，并且将 `usb0` 设置为 `WAN`。

> 在 Network - Interfaces - Devices 查看是否有 usb0 的网络设备，如果没有，说明没有设置成功

在 Network - Interface - Interfaces 上点击左下角 “Add New Interface”，名字自己选，设备选择 `usb0`。

这个时候，就可以通过安卓设备，用USB数据线传输数据，来进行上网了。

---

ref:

* <https://openwrt.org/docs/guide-user/network/wan/smartphone.usb.tethering>

---

##### 相关文章

* [Collections 源码阅读与分析](/articles/2017_01_06-collections_source_code.md.html)
* [Redis通信协议阅读](/articles/2017_01_06-redis_protocol_specification.md.html)
* [2016年就要结束了，2017年就要开始啦！](/articles/2016_12_31-2016_is_over_and_2017_is_coming.md.html)
* [unittest 源代码阅读](/articles/2016_12_29-unittest_source_code.md.html)
* [APUEv3 - 重读笔记](/articles/2016_12_26-apue_v3.md.html)
* [Mock源码阅读与分析](/articles/2016_12_22-mock_source_code.md.html)
* [Thinking in Python](/articles/2016_12_16-thinking_in_python.md.html)
* [我的代码进CPython标准库啦](/articles/2016_12_15-my_code_in_python_stdlib.md.html)
* [Python零碎小知识](/articles/2016_12_09-python_fragments.md.html)
* [工作一年的总结](/articles/2016_12_07-work.md.html)
* [Python和单元测试](/articles/2016_12_07-python_unittest.md.html)
* [MongoDB 的一些坑](/articles/2016_12_06-mongodb.md.html)
* [Python 的继承](/articles/2016_12_06-python_c3_mro.md.html)
* [Python的yield关键字有什么作用？](/articles/2016_11_29-python_yield.md.html)
* [借助coroutine用同步的语法写异步](/articles/2016_11_27-python_coroutine.md.html)

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