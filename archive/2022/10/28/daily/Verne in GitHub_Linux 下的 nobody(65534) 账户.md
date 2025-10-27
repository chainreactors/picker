---
title: Linux 下的 nobody(65534) 账户
url: https://einverne.github.io/post/2022/10/unix-nobody-65534.html
source: Verne in GitHub
date: 2022-10-28
fetch_date: 2025-10-03T21:06:24.155789
---

# Linux 下的 nobody(65534) 账户

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

# Linux 下的 nobody(65534) 账户

Posted on 10/27/2022
, Last modified on 10/27/2022
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2022-10-27-unix-nobody-65534.md)

在使用 linx-server 的时候，发现作者在 Dockerfile 中将存储文件的目录授予了 65534 这个用户权限，于是好奇为什么是 65534，于是有了这篇文章。

首先找到的是 [Wikipedia](https://en.wikipedia.org/wiki/User_identifier#Special_values) 上关于 Linux 中用户 `nobody` 的 UID，历史上，用户 nobody 有多好几个不同的 UID，最早的时候一些操作系统使用 `-2`，还有一些操作系统，比如 OpenBSD 使用 2^(15) - 1 = 32767 ，为了兼容 16-bit 和 32-bit UID，现在许多 Linux 发行版将 nobody 的 ID 设置为 2^16-2 = 65534.

[Ubuntu wiki](https://wiki.ubuntu.com/nobody) 说 nobody 通常是 NFS 服务器中当不信任用户时使用的。

## nobody 用户的作用

nobody 账户通常会用来运行一些不需要任何权限的程序。 nobody 账户是让一些守护程序以最小权限运行的。[1](#fn:1) 通常会用在一些容易受到攻击的服务上，比如 httpd 等，即使这些服务被 hack，这些服务也只会对系统造成最低的伤害。

相比于使用一个真正的用户执行程序，如果这些程序被攻破了（比如 web 服务器执行了恶意代码），那么这些程序以用户账户运行的话，就拥有了这个用户账号可以访问的一切资源。在某种程度上不使用 root 账户也是一样的道理。用一个隔离的账户来执行这些程序可以提高系统的安全性。

### 如何访问 nobody

执行 `sudo grep nobody /etc/shadow` 可以知道 `nobody` 账户是没有密码的，无法使用 `su` 输入密码登录。最简单的方法是使用 `sudo su nobody`

## 什么时候使用 nobody

当程序不需要任何权限的时候，比如在 linx-server 的 data 目录中保存的是用户上传的临时文件，这个文件不需要任何权限。

另外一个现实的例子就是 `memcached` 一个 k-v 的基于内存的存储，直接可以通过 nobody 运行，因为不需要任何写磁盘的操作。

## reference

* <https://askubuntu.com/a/329716/407870>

1. <https://groups.google.com/g/linux.debian.user/c/oNtzOORNQlk> [↩](#fnref:1)

## Related Posts

* [Linux 下的 nobody(65534) 账户](/post/2022/10/unix-nobody-65534.html) - 10/27/2022
* [Docker Compose 中使用环境变量](/post/2021/08/docker-compose-environment-variables.html) - 08/29/2021
* [docker volumes 中 -v 和 -mount 区别](/post/2018/03/docker-v-and-mount.html) - 03/13/2018
* [搭建自己的文件共享服务 linx server](/post/2018/02/linx-server.html) - 02/26/2018
* [Dockerfile 基础镜像](/post/2017/05/dockerfile-base-image.html) - 05/02/2017
* [Vim 中不同模式间的切换](/post/2015/05/vim-mode-switch.html) - 05/05/2015

---

* [← Previous（前一篇）](/post/2022/10/japanese-learning-tools.html "日语学习相关工具")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2022/10/principles-life-and-work.html "《原则》读书笔记")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2022/10/unix-nobody-65534.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [学习笔记 496](/categories.html#学习笔记)

* [linux 435](/tags.html#linux)
* [nobody-account 1](/tags.html#nobody-account)
* [linx-server 2](/tags.html#linx-server)
* [dockerfile 7](/tags.html#dockerfile)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").