---
title: Proxmox VE 安装 Ubuntu Server 22.04
url: https://einverne.github.io/post/2023/04/proxmox-install-ubuntu-server-22-04.html
source: Verne in GitHub
date: 2023-04-17
fetch_date: 2025-10-04T11:31:25.449634
---

# Proxmox VE 安装 Ubuntu Server 22.04

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# Proxmox VE 安装 Ubuntu Server 22.04

Posted on 04/16/2023
, Last modified on 04/16/2023
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2023-04-16-proxmox-install-ubuntu-server-22-04.md)

之前的时候，有一台小主机，在上面安装了 [[Proxmox VE]]，然后在其中安装了 [[iKuai]] 和 [[OpenWrt]] 作为软路由使用。现在已经不需要再将其作为软路由代理使用，所以今天就拿出来整理一下，正好放在家里面作为一个 Linux 小服务器，跑一些小一点的程序，然后顺便挂载一个硬盘作为一个小型的媒体服务器。

因为之前在 Proxmox VE 上安装过很多次的系统，这里就不展开，把一些重要的配置和截图放在下面。

## 准备 ISO

在创建虚拟机之前，需要到 [Ubuntu Server 官网](https://ubuntu.com/download/server) 下载最新的 ISO 镜像，然后把镜像上传到 ISO Images 中：

![643b79d2eeb21](https://img.gtk.pw/i/2023/04/16/643b79d2eeb21.png)

之后就可以开始创建 Ubuntu Server。具体的步骤如下。

## 创建虚拟机

首先第一步设置节点的名字（Name）

![643b6ae8acf5d](https://img.gtk.pw/i/2023/04/16/643b6ae8acf5d.png)

然后第二步选择需要挂载的镜像。
![643b73b26a6d2](https://img.gtk.pw/i/2023/04/16/643b73b26a6d2.png)

第三步配置 BIOS，保持默认即可。
![643b73d6849ac](https://img.gtk.pw/i/2023/04/16/643b73d6849ac.png)

第四步，选择磁盘，这里个地方可以根据自己的需要调整虚拟磁盘大小。
![643b741125266](https://img.gtk.pw/i/2023/04/16/643b741125266.png)

第五步，设置 CPU 核心，默认是不能超过物理 CPU 的数量的。
![643b7439c5ae0](https://img.gtk.pw/i/2023/04/16/643b7439c5ae0.png)

第六步，设置网络设备，我这边默认有一个 Linux 网桥（vmbr0），默认即可。
![643b748c50f63](https://img.gtk.pw/i/2023/04/16/643b748c50f63.png)

之后点击下一步，确认自己的配置，然后点击完成虚拟机的创建。

之后就可以开启虚拟机，第一次会使用设置 ISO 启动虚拟机，然后进入 Ubuntu Server 的安装界面。

## 安装 Ubuntu Server

第一次启动虚拟机之后会自动进入安装的程序，安装的过程比较简单，使用键盘选择，确认即可，基本上会分成如下几步：

* 选择语言，English
* 选择安装的类型，默认的 Ubuntu Server 即可
* 配置网络，这个地方需要注意
  + 默认情况下安装程序会根据 DHCP 自动获取一个 IP 地址，如果这个 IP 地址不是你想要的，可以使用 Mannual 自动配置一个
  + subnet 192.168.2.0/24
  + IP 选择一个想要的，比如 192.168.2.30
  + Gateway: 网关 192.168.2.1
  + Name Server: 设置一个 DNS 解析服务器，比如 8.8.8.8
  + Search Domain: 设置一个 Search Domain，Search Domain 的作用就是当本地网络的一个解析，比如设置了 Search Domain 是 `einverne.info` ，那么在 Ubuntu Server 中解析 `webserver` 的时候会首先尝试去解析 `webserver.einverne.info`
* 配置代理，不需要设置，但如果是在局域网，或者无法访问互联网的时候这个地方可以根据自己的需要设置一下
* Ubuntu Archive Mirror，默认即可
* 配置磁盘，可以根据自己的需求调整，我就按默认
* 创建用户名密码等
* 开启 SSH
* 选择是否要安装其他组件，比如 [[microk8s]], [[NextCloud]], [[weken]], [[Docker]] 等等
* 最后就是确认，等待安装完成

## 进入系统

等待安装程序安装完成之后就可以通过 IP 地址和端口，用户名和密码登录到 Ubuntu Server。

```
ssh username@ip
```

## Related Posts

* [开源跨平台终端 XPipe](/post/2025/03/xpipe.html) - 03/06/2025
* [ProxMobo 一款 Proxmox VE 管理客户端](/post/2024/05/proxmobo-proxmox-ve-management-tool.html) - 05/22/2024
* [Proxmox VE 安装 Ubuntu Server 22.04](/post/2023/04/proxmox-install-ubuntu-server-22-04.html) - 04/16/2023
* [J3455 主板无法使用 PCIe 扩展 SATA 启动系统解决](/post/2023/01/j3455-itx-cannot-boot-csm.html) - 01/02/2023
* [Proxmox VE 从 6 升级到 7](/post/2022/06/proxmox-ve-6-upgrade-to-7.html) - 06/04/2022
* [Ubuntu 20.04 使用 MergerFS](/post/2021/10/ubuntu-20-04-mergerfs.html) - 10/21/2021
* [So you Start 独服 Proxmox VE 虚拟机配置 Failover IP](/post/2021/10/so-you-start-proxmox-ve-connect-vm-to-internet-failover-ip.html) - 10/11/2021
* [Cloud-init 初始化虚拟机配置](/post/2020/03/cloud-init.html) - 03/28/2020

---

* [← Previous（前一篇）](/post/2023/04/coinpayments.html "CoinPayments 加密货币支付网关")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2023/04/chatwoot-nginx-header-underscore.html "Chatwoot Nignx 代理丢失 Header 信息")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2023/04/proxmox-install-ubuntu-server-22-04.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [proxmox 18](/tags.html#proxmox)
* [proxmox-ve 7](/tags.html#proxmox-ve)
* [ubuntu-server 1](/tags.html#ubuntu-server)
* [ubuntu 34](/tags.html#ubuntu)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").