---
title: J3455 主板无法使用 PCIe 扩展 SATA 启动系统解决
url: https://einverne.github.io/post/2023/01/j3455-itx-cannot-boot-csm.html
source: Verne in GitHub
date: 2023-01-03
fetch_date: 2025-10-04T02:53:54.553342
---

# J3455 主板无法使用 PCIe 扩展 SATA 启动系统解决

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

# J3455 主板无法使用 PCIe 扩展 SATA 启动系统解决

Posted on 01/02/2023
, Last modified on 01/02/2023
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2023-01-02-j3455-itx-cannot-boot-csm.md)

把自己之前用 J3455-itx 主板组的 NAS 搬回了，但突然无法启动，这里就记录一下排错的过程。

最早启动的时候，无法进入系统，启动日志里面报错：

```
ata 7: COMRESET failed (errno=16)
```

开始怀疑是搬家的时候硬盘坏了。所以拆开主机，把其中的第四块硬盘 SATA 线拔掉了。重新启动主机，发现竟然能进入系统了。并且用 fdisk 查看，所有的其他硬盘都没有问题。

![j3455 itx sata](https://photo.einverne.info/images/2023/01/02/gCQn.jpg)

这个时候我仔细的检查了一下 SATA 的连线，J3455-itx 这块主板只有 4 个 SATA 口，但是我使用 PCIe 扩展了 2 个 SATA 口，一共接了 5 块硬盘，1 块 SSD 安装了系统，4 块 HDD 机械硬盘。

为了腾位置给 SSD，所以我将一块 HDD 的 SATA 线连接到了扩展卡的 SATA 接口，就是将这个接口拔掉，才能够进入系统。这个时候我开始怀疑是不是扩展卡在搬运的过程中损坏了。于是加紧在京东又下单了一个全新的 PCIe 转 SATA 扩展卡。

今天终于把全新的扩展卡安装上来，但是发现这一块机械硬盘还是无法读取。一度又让我怀疑真的是磁盘坏了，为了排除这个嫌疑，我拿出了之前买过的 SATA 转 USB 的设备，拿了 Linux Mint 发现能正常读取这一块硬盘，因为四块机械硬盘是通过 [[MergerFS]] 合并成一块逻辑硬盘使用的，所以这一块硬盘上也能读取到部分的数据，证明机械硬盘是没有问题的。

这个时候我已经排除了机械硬盘的问题，扩展卡的问题，我又在怀疑难道是 PCIe 接口坏了。这个时候我就把 SSD 拆了下来，然后把四块机械硬盘连接到了主板上的四个 SATA 接口，通过 USB 来启动 SSD，过程中我发现系统完全启动正常，并且能够在 [[Proxmox VE]] 下安装的 [[OpenMediaVault]] 下正常挂载 4 块硬盘，读写也完全没有问题。

启动系统的过程中还遇到了 soft lockup 问题，这个时候还以为是磁盘的 IO 造成的。但后来仔细想想应该是通过 USB 启动的系统在读写上存在瓶颈导致的。

![soft lockup](https://photo.einverne.info/images/2023/01/02/g1u8.png)

那剩下的问题就肯定出在 PCIe 这个接口上。我又换回了之前的扩展卡，然后重新在 BIOS 中查看，调整配置。当我将 SSD 连接到扩展卡，并启动的时候 J3455-itx 主板无法找到可启动的设备，直接进入了 BIOS。

这个时候我突然想起来用 J3455 和扩展卡在 Google 搜索了一下。于是就看到了 [这个帖子](https://ngabbs.com/read.php?tid=17978723&rand=344) 其中的一句话惊醒了我。

> 主板 BOIS 里打开 CSM 试试

我在 BIOS 里面找到 CSM 设置，启用，然后重启系统，竟然能够从 SSD 启动了，扩展卡没有坏，硬盘没有坏，只是 BIOS 里面的一行配置变了！

## 什么是 CSM

CSM 全称是 Compatibility Support Module，是 BIOS 用来启动旧版操作系统和其他旧软件的一种特性。可以让 UEFI BIOS 兼容 Legacy+MBR 启动模式。

我已经忘记了之前安装 Proxmox VE 的时候用的什么引导了，但启用了 CSM 的时候就能够找到磁盘上的引导程序，并成功启动系统了。

至此整个 Debug 的过程才算结束。没想到的是新年假期竟然花了半天时间 Debug 硬件，o<(=╯□╰=)>o

## Related Posts

* [开源跨平台终端 XPipe](/post/2025/03/xpipe.html) - 03/06/2025
* [ProxMobo 一款 Proxmox VE 管理客户端](/post/2024/05/proxmobo-proxmox-ve-management-tool.html) - 05/22/2024
* [Proxmox VE 安装 Ubuntu Server 22.04](/post/2023/04/proxmox-install-ubuntu-server-22-04.html) - 04/16/2023
* [J3455 主板无法使用 PCIe 扩展 SATA 启动系统解决](/post/2023/01/j3455-itx-cannot-boot-csm.html) - 01/02/2023
* [Proxmox VE 从 6 升级到 7](/post/2022/06/proxmox-ve-6-upgrade-to-7.html) - 06/04/2022
* [Ubuntu 20.04 使用 MergerFS](/post/2021/10/ubuntu-20-04-mergerfs.html) - 10/21/2021
* [So you Start 独服 Proxmox VE 虚拟机配置 Failover IP](/post/2021/10/so-you-start-proxmox-ve-connect-vm-to-internet-failover-ip.html) - 10/11/2021
* [扩展 Proxmox 系统分区以及 Proxmox 文件系统初识](/post/2020/11/extend-proxmox-system-partition-and-pve-file-system.html) - 11/10/2020

---

* [← Previous（前一篇）](/post/2022/12/reading-in-year-2022.html "2022 年读书笔记")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2023/01/chatgpt-openai-register.html "ChatGPT(OpenAI) 账号注册")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2023/01/j3455-itx-cannot-boot-csm.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [j3455 1](/tags.html#j3455)
* [itx 1](/tags.html#itx)
* [openmediavault 7](/tags.html#openmediavault)
* [proxmox 18](/tags.html#proxmox)
* [proxmox-ve 7](/tags.html#proxmox-ve)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").