---
title: KVM 穿透板载蓝牙和无线网卡
url: https://jiajunhuang.com/articles/2025_05_05-kvm_passthrough_bluetooth_wireless.md.html
source: Jiajun的技术笔记
date: 2025-05-06
fetch_date: 2025-10-06T22:25:25.544585
---

# KVM 穿透板载蓝牙和无线网卡

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

* [KVM 穿透板载蓝牙和无线网卡](#KVM%2b%25E7%25A9%25BF%25E9%2580%258F%25E6%259D%25BF%25E8%25BD%25BD%25E8%2593%259D%25E7%2589%2599%25E5%2592%258C%25E6%2597%25A0%25E7%25BA%25BF%25E7%25BD%2591%25E5%258D%25A1)
* [穿透无线网卡](#%25E7%25A9%25BF%25E9%2580%258F%25E6%2597%25A0%25E7%25BA%25BF%25E7%25BD%2591%25E5%258D%25A1)
* [穿透蓝牙](#%25E7%25A9%25BF%25E9%2580%258F%25E8%2593%259D%25E7%2589%2599)

# KVM 穿透板载蓝牙和无线网卡

我的Host一直是Linux，但是偶尔会打游戏，因此有一台 Windows 虚拟机，最近想要把板载蓝牙和无线网卡穿透进去，但是都遇到了一些
小困难需要解决，因此记录成文。

## 穿透无线网卡

无线网卡穿透起来和穿透显卡等硬件是一样的，由于无线网卡在一个单独的IOMMU组，直接加到 `/etc/modprobe.d/vfio.conf`
中即可，此外，我发现我本地的无线网卡总是被 `igb` 驱动优先占用导致 `vfio-pci` 无法占用网卡，我在 `/etc/modprobe.d/vfio.conf`
中加上：

```
softdep igb pre: vfio-pci
options vfio-pci ids=...无线网卡的硬件ID
```

然后重启以后，就可以穿透了。

## 穿透蓝牙

一开始我以为蓝牙是和无线网卡在一起的，后来发现蓝牙是和USB控制器在一起的，在 `virt-manager` 中，点击 `Add Hardware` - `USB Host Device`,
选择带 `Intl...Bluetooth` 的那个，穿透进去以后，如果直接开机的话，会发现这样的现象：

* Windows 可以发现蓝牙硬件，但是无法使用，安装驱动以后，点开 “我的电脑” 查看硬件详情，驱动里报错 “code: 10”

经过搜索发现，这是 `libvirt` 的一个改动导致的问题，要解决这个问题，还需要编辑XML：

```
$ sudo virsh edit --domain windows
```

在 `</domain>` 上面加上 `<qemu:capabilities>` 这一节：

```
<domain>
    <devices>
        ...
    </devices>

    <qemu:capabilities>
        <qemu:del capability="usb-host.hostdevice"/>
    </qemu:capabilities>

...
</domain>
```

此时如果保存你会发现无法通过xml校验，还需要跳到顶部，在 `<domain type='kvm'>` 改成

```
<domain type='kvm' xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0'>
```

然后保存，然后重启以后，就可以穿透蓝牙了。

---

参考文档：

* [KVM显卡穿透](https://jiajunhuang.com/articles/2022_03_15-kvm_windows_gpu_passthrough.md.html)
* [OnBoard Intel Bluetooth Error Code 10 on Windows KVM Guest](https://www.reddit.com/r/VFIO/comments/wbsqy1/how_to_fix_onboard_intel_bluetooth_error_code_10/)
* [PCI passthrough via OVMF](https://wiki.archlinux.org/title/PCI_passthrough_via_OVMF)

---

##### 相关文章

* [一起来做贼：Goroutine原理和Work stealing](/articles/2017_02_24-goroutine_and_work_stealing.md.html)
* [Go语言的defer, panic和recover](/articles/2017_02_15-go_defer_panic_and_recover.md.html)
* [再读vim help：vim小技巧](/articles/2017_01_24-vim_manual.md.html)
* [再读 Python Language Reference](/articles/2017_01_24-python_language_reference.md.html)
* [设计模式（2）- 深入浅出设计模式 阅读笔记](/articles/2017_01_22-head_first_design_patterns_2.md.html)
* [设计模式（1）- 深入浅出设计模式 阅读笔记](/articles/2017_01_21-head_first_design_patterns.md.html)
* [Cython! Python和C两个世界的交叉点](/articles/2017_01_15-cython_rocks.md.html)
* [socketserver 源码阅读与分析](/articles/2017_01_09-socketserver_source_code.md.html)
* [functools 源码阅读与分析](/articles/2017_01_08-functools_source_code.md.html)
* [contextlib代码阅读](/articles/2017_01_07-contextlib_source_code.md.html)
* [Collections 源码阅读与分析](/articles/2017_01_06-collections_source_code.md.html)
* [Redis通信协议阅读](/articles/2017_01_06-redis_protocol_specification.md.html)
* [2016年就要结束了，2017年就要开始啦！](/articles/2016_12_31-2016_is_over_and_2017_is_coming.md.html)
* [unittest 源代码阅读](/articles/2016_12_29-unittest_source_code.md.html)
* [APUEv3 - 重读笔记](/articles/2016_12_26-apue_v3.md.html)

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