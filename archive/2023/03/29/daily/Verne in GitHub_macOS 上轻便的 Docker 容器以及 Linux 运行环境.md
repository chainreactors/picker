---
title: macOS 上轻便的 Docker 容器以及 Linux 运行环境
url: https://einverne.github.io/post/2023/03/orbstack-docker-runtime-and-virtual-linux.html
source: Verne in GitHub
date: 2023-03-29
fetch_date: 2025-10-04T10:58:09.792276
---

# macOS 上轻便的 Docker 容器以及 Linux 运行环境

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

# macOS 上轻便的 Docker 容器以及 Linux 运行环境：OrbStack

Posted on 03/28/2023
, Last modified on 03/28/2023
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2023-03-28-orbstack-docker-runtime-and-virtual-linux.md)

今天早上在 Twitter 上连续看到三个人在同一时间推荐了一款在 macOS 上运行的 Docker 容器和 Linux 虚拟机 —- [OrbStack](https://orbstack.dev/) 。

GitHub：<https://github.com/orbstack>

而 macOS 上的 Docker Desktop 原本就是饱受诟病，慢，重，资源消耗巨大。 OrbStack 的出现就是为了解决这个问题。

macOS 从 2020 年发布 Big Sur 开始，提供了虚拟化的框架，开发者可以在 macOS 上构建基于 Intel/ARM 的 Linux 环境。macOS 上的 [[Parallels Desktop]] 和 [[Docker Desktop]] 都在使用这个框架，但这二者都比较重。

## OrbStack 使用

下载安装的过程特别简单。可以看到如下的界面可以在 macOS 上快速，轻便的创建 Docker 容器和 Linux 环境。

![OfKw](https://photo.einverne.info/images/2023/03/28/OfKw.png)

执行一下测试的容器:

```
docker run -it -p 80:80 docker/getting-started
```

然后再访问 <http://localhost/> 即可看到最基础的 Docker 教程。

在这个界面中也可以对容器进行简单的管理。
![Ou7c](https://photo.einverne.info/images/2023/03/28/Ou7c.png)

在系统的资源管理器中可以看到 OrbStack 几乎不怎么占用 CPU 和内存。

CPU 消耗

![OS4r](https://photo.einverne.info/images/2023/03/28/OS4r.png)

内存消耗

![O4Rd](https://photo.einverne.info/images/2023/03/28/O4Rd.png)

## 相关命令

OrbStack 也提供了一些管理命令 `orbctl`，可以直接在命令行使用。

```
orbctl help
```

OrbStack 在创建了 Ubuntu 等 Linux 镜像之后也可以使用 SSH 连接

```
orb -m ubuntu -u root
orb -m ubuntu -u root uname -a
```

`orb` 命令还提供了其他一些特性，比如可以在虚拟机中 push 或 pull 来传输文件。

## 目前的一些局限

OrbStack 虚拟的 Linux 是不支持 GUI 的，不过这也不妨碍，我想大部分开发应该只会使用命令行去管理 Linux 运行环境吧。大致猜想 OrbStack 应该只是用 Docker 开启了一个 Linux 的容器，所以不支持图形化界面也是可以理解的。

## alternative

* [colima](https://github.com/abiosoft/colima) 也是 macOS 上的一款容器运行时。
* [lima](https://github.com/lima-vm/lima) 也是 macOS 上的一款 Linux 虚拟机应用。

## 总结

总之如果你之前饱受 Docker Desktop 慢的问题困扰，或者之前经常使用 Virtual Box，[[VMware Fusion]] 等虚拟化工具在 macOS 上虚拟化 Linux 运行环境，不妨来试试这一款轻量的 OrbStack。

## Related Posts

* [VibeTunnel 将终端带到浏览器 开启移动化 Vibe Coding](/post/2025/08/vibetunnel.html) - 08/12/2025
* [通过 kubectl 学习 Kubernetes](/post/2024/10/kubectl.html) - 10/19/2024
* [macOS 上的多栏文件管理器 QSpace](/post/2024/07/qspace-multi-pane-finder.html) - 07/30/2024
* [使用 SyncTV 异地远程一起看视频](/post/2023/11/synctv.html) - 11/26/2023
* [macOS 上的清理工具整理合集](/post/2023/06/macos-cleaner-apps.html) - 06/10/2023
* [macOS 上轻便的 Docker 容器以及 Linux 运行环境：OrbStack](/post/2023/03/orbstack-docker-runtime-and-virtual-linux.html) - 03/28/2023
* [Visual Studio Code Server 搭建：构建一个属于自己的基于网页的开发环境](/post/2023/03/visual-studio-code-server-usage.html) - 03/07/2023
* [使用开源 Wakapi 代替 WakaTime 统计编码时间](/post/2022/09/wakapi-usage.html) - 09/22/2022
* [在停止的 Docker 中其中执行命令](/post/2022/06/run-commands-in-stopped-docker-container.html) - 06/02/2022
* [Proxmox 扩展 VM 虚拟机磁盘容量](/post/2022/05/proxmox-expand-vm-disk-qcow2.html) - 05/10/2022
* [图片压缩工具 Squoosh 离线版](/post/2022/04/squoosh-desktop-version.html) - 04/28/2022
* [自建邮件服务器的选择和比较](/post/2022/04/self-hosted-mail-server-choice.html) - 04/25/2022
* [使用 Mailcow 自建邮件服务器](/post/2022/04/mailcow-email-server.html) - 04/23/2022
* [使用 Docker 安装 Mastodon 实例搭建自己的社交网络](/post/2022/04/install-mastodon-by-docker.html) - 04/21/2022
* [充分利用 Oracle 机器避免被回收](/post/2022/03/oracle-idle.html) - 03/08/2022
* [使用 Nginx Proxy Manager 管理 Nginx 代理](/post/2022/02/nginx-proxy-manager.html) - 02/16/2022
* [搭建临时 socks5 代理](/post/2021/12/vps-socks5-proxy.html) - 12/12/2021
* [如何发现 CPU steal 并解决](/post/2021/11/best-way-to-monitor-cpu-steal.html) - 11/05/2021
* [升级 Gogs(Docker) 从 0.11.91 到 0.12.3](/post/2021/10/upgrade-gogs-0-11-91-to-0-12-3.html) - 10/30/2021
* [espanso：Rust 编写的跨平台开源文本扩展工具](/post/2021/09/espanso-text-expand.html) - 09/17/2021
* [rTorrent 和 ruTorrent 中自动下载 RSS Feed](/post/2021/09/rutorrent-rss-auto-download.html) - 09/10/2021
* [Docker Compose 中使用环境变量](/post/2021/08/docker-compose-environment-variables.html) - 08/29/2021
* [使用 Archive Box 制作自己的互联网存档](/post/2021/08/make-your-own-internet-archive-with-archive-box.html) - 08/27/2021
* [又一个简单漂亮的静态个人导航站 Homer](/post/2021/08/another-simple-static-homepage-homer.html) - 08/26/2021
* [限制 Docker 容器日志的大小](/post/2021/08/limit-docker-logs-size.html) - 08/20/2021
* [使用 Vagrant 自动创建配置虚拟机](/post/2021/08/vagrant-introduction.html) - 08/14/2021
* [A400互联VPS简单测评及使用](/post/2021/08/a400-vps-test-and-usage.html) - 08/13/2021
* [使用了半年 macOS 之后 我又回到了 Linux 的怀抱](/post/2021/03/come-back-to-linux-after-using-macos-half-an-year.html) - 03/31/2021
* [VMware Workstation 虚拟机网络设置](/post/2021/03/vmware-network-setting.html) - 03/23/2021
* [在 Linux 上使用 Clash 作代理](/post/2021/03/linux-use-clash.html) - 03/15/2021
* [WhatPulse 使用记录](/post/2021/01/whatpulse-usage.html) - 01/10/2021
* [使用 Clonezilla 将硬盘中系统恢复到虚拟机中](/post/2020/10/use-clonezilla-restore-image-to-virtual-machine.html) - 10/29/2020
* [Docker 网络与容器互联](/post/2020/07/docker-network.html) - 07/20/2020
* [Cloud-init 初始化虚拟机配置](/post/2020/03/cloud-init.html) - 03/28/2020
* [使用 flexget 实现下载更新自动化](/post/2020/02/flexget.html) - 02/18/2020
* [几个常见的 NAS 系统整理及选择](/post/2020/02/nas-operating-system-choice.html) - 02/11/2020
* [自建 RSS Reader](/post/2020/02/self-hosted-rss-reader.html) - 02/09/2020
* [自建邮件服务器解决方案](/post/2020/02/self-hosted-mail-server.html) - 02/08/2020
* [威联通折腾篇十九：Calibre-web](/post/2020/02/qnap-calibre-web.html) - 02/08/2020
* [威联通折腾篇十六：为 Container Station 更换镜像](/post/2020/01/qnap-docker-registry-mirror.html) - 01/16/2020
* [使用 Huginn 搭建自己的 IFTTT](/post/2019/01/huginn.html) - 01/11/2019
* [威联通折腾篇四：Container Station 运行 Docker 容器](/post/2018/06/qnap-container-station.html) - 06/17/2018
* [BitTorrent 客户端简单比较](/post/2018/04/bittorrent-client.html) - 04/24/2018
* [使用 yourls 专属自己的短域名服务](/post/2018/04/yourls.html) - 04/11/2018
* [Jigsaw Outline 部署和使用](/post/2018/03/jigsaw-outline-deploy-and-usage.html) - 03/26/2018
* [备份 Docker 镜像容器和数据以及无痛迁移](/post/2018/03/docker-related-backup.html) - 03/16/2018
* [树莓派中安装 Docker 及 docker compose](/post/2018/03/respberry-pi-install-docker.html) - 03/15/2018
* [VPS 云服务器能够做什么](/post/2018/03/what-can-vps-do.html) - 03/14/2018
* [docker volumes 中 -v 和 -mount 区别](/post/2018/03/docker-v-and-mount.html) - 03/13/2018
* [docker-compose 中 links 和 depends\_on 区别](/post/2018/03/docker-compose-links-vs-depends-on-differences.html) - 03/12/2018
* [Docker 容器日志相关命令](/post/2018/03/docker-logs.html) - 03/10/2018
* [dockerfile 指令](/post/2018/02/dockerfile-command.html) - 02/23/2018
* [Docker中运行 MySQL](/post/2018/02/docker-mysql.html) - 02/18/2018
* [使用 docker compose 管理多个容器](/post/2018/02/docker-compose.html) - 02/15/2018
* [搭建自己的 Weibo 转 RSS 服务](/post/2018/02/self-hosted-weibo-to-rss.html) - 02/11/2018
* [Docker 入门](/post/2017/07/docker-introduction.html) - 07/16/2017
* [Dockerfile 基础镜像](/post/2017/05/dockerfile-base-image.html) - 05/02/2017
* [Linux 安装 VMware workstation 12](/post/2017/04/linux-install-vmware-workstation-12.html) - 04/29/2017
* [Vim 中不同模式间的切换](/post/2015/05/vim-mode-switch.html) - 05/05/2015

---

* [← Previous（前一篇）](/post/2023/03/prevent-ssl-ip.html "防止 SSL 证书泄露网站 IP")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2023/03/clientexec-installation.html "ClientExec 安装及入门使用")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2023/03/orbstack-docker-runtime-and-virtual-linux.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [产品体验 185](/categories.html#产品体验)

* [orbstack 1](/tags.html#orbstack)
* [docker 86](/tags.html#docker)
* [macos 49](/tags.html#macos)
* [linux 435](/tags.htm...