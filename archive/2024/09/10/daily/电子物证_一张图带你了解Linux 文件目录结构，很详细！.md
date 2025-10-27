---
title: 一张图带你了解Linux 文件目录结构，很详细！
url: https://mp.weixin.qq.com/s?__biz=MzAwNDcwMDgzMA==&mid=2651047902&idx=1&sn=25ab4360f720e41808cc261986ab3ffd&chksm=80d0882fb7a70139a216a357ca9f376237e1fa97affce520836a291ab9b6184750392a4d443f&scene=58&subscene=0#rd
source: 电子物证
date: 2024-09-10
fetch_date: 2025-10-06T18:28:59.267047
---

# 一张图带你了解Linux 文件目录结构，很详细！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dDhDhftpRFtlZg4YKUm3x3Ek87koUzx1wm0miaNN9Q8pdvPrQbFNaHs6WCStN6SVHdjSicZFJaHHC8qSS23EIgCA/0?wx_fmt=jpeg)

# 一张图带你了解Linux 文件目录结构，很详细！

电子物证

以下文章来源于网络技术联盟站
，作者wljslmz瑞哥

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM77iaxYIxqdPOho2YXia5fR41Q5rOSDhEQGVVz9xkxicLO7Q/0)

**网络技术联盟站**
.

计算机网络技术，行业干货知识传播，网络技术分享，总有你想要的！

![](https://mmbiz.qpic.cn/mmbiz_gif/6OibpDQ66VYQNIyABHZrCWcZT6asQr23iaO5wvXibL4CtruQ1E2AY6iaaH3X4LxMnSrBXvjhQND7Y4ibRahz9FhPVBw/640?wx_fmt=gif)

> 来源：网络技术联盟站

Linux 文件目录结构是任何 Linux 系统的基本组成部分。它为系统提供了一个标准化的文件和目录组织方式，使得用户和应用程序能够以一致的方式访问和管理文件。与 Windows 系统不同，Linux 的文件系统采用单一的树形结构，从根目录（/）开始，所有文件和目录都在其下。理解这一结构不仅对于系统管理员至关重要，对于普通用户也是必不可少的，因为它可以帮助更有效地管理文件和解决问题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/6OibpDQ66VYRiaSCSKtNW0lYMOHCqMU3drTl5HJ417xGfmcgL6ibllNeicIfwBg2QNzSzNYHxneZlSBfZeiaGSNCwdg/640?wx_fmt=jpeg&from=appmsg)

## 根目录（/）

根目录（/）是 Linux 文件系统的顶层目录。所有的文件和目录都从这里开始，形成一个树形结构。根目录下的每个子目录都有其特定的功能和用途。

* **/bin**：存放基本用户命令。
* **/sbin**：存放系统管理命令。
* **/etc**：存放系统配置文件。
* **/dev**：存放设备文件。
* **/tmp**：存放临时文件。
* **/home**：存放用户主目录。
* **/var**：存放可变数据文件。
* **/usr**：存放用户级应用程序和文件。
* **/opt**：存放附加软件包。
* **/mnt**：用于临时挂载文件系统。
* **/media**：用于自动挂载的可移动设备。
* **/boot**：存放启动加载程序和内核文件。
* **/lib**：存放系统库文件和内核模块。
* **/proc**：存放系统内核和进程信息。
* **/sys**：存放系统设备和内核信息。
* **/root**：超级用户的主目录。

下面，瑞哥带大家逐一详细介绍这些目录及其子目录的具体用途和常见文件。

## /bin 目录

/bin（binary）目录包含系统启动和单用户模式下使用的基本命令。这些命令是系统正常运行所必需的，并且在单用户模式或系统紧急修复时也可以使用。

常见的命令包括：

* **ls**：列出目录内容。
* **cp**：复制文件或目录。
* **mv**：移动或重命名文件或目录。
* **rm**：删除文件或目录。
* **cat**：连接文件并显示输出。
* **echo**：显示消息。

这些命令通常是静态链接的，确保在系统启动时不依赖于其他库文件。

## /sbin 目录

/sbin（system binary）目录包含系统管理命令，这些命令通常需要超级用户权限执行。它们用于系统启动、维护和修复。

常见的命令包括：

* **ifconfig**：配置网络接口。
* **reboot**：重启系统。
* **shutdown**：关闭系统。
* **fdisk**：磁盘分区工具。
* **mkfs**：创建文件系统。

这些命令对于系统管理员来说是至关重要的，因为它们涉及到系统的核心功能和配置。

## /etc 目录

/etc 目录包含所有的系统全局配置文件。这些文件定义了系统的各种设置和参数。

常见的配置文件和目录包括：

* **/etc/passwd**：用户账号信息文件。
* **/etc/fstab**：文件系统挂载表。
* **/etc/hosts**：主机名和 IP 地址对应表。
* **/etc/hostname**：定义系统的主机名。
* **/etc/network/interfaces**：网络接口配置文件（在基于 Debian 的系统中）。

在 /etc 目录中，每个服务和应用程序通常都有自己的子目录或配置文件，例如 Apache 的配置文件在 `/etc/apache2/` 下。

## /dev 目录

/dev 目录包含设备文件，这些文件表示系统中的各种硬件设备。Linux 中的一切皆文件，包括硬件设备。

常见的设备文件包括：

* **/dev/sda**：第一个 SCSI 硬盘。
* **/dev/tty**：终端设备。
* **/dev/null**：空设备，丢弃所有写入其中的数据。
* **/dev/random**：随机数生成器。

这些设备文件允许用户和应用程序以文件的方式访问硬件设备。

## /tmp 目录

/tmp 目录用于存放临时文件。系统和应用程序在运行过程中可能会在此目录下创建临时文件。通常，系统会在每次启动时清理 /tmp 目录，以防止磁盘空间被临时文件占用过多。

/tmp 目录中的文件通常对所有用户可读写，但应注意临时文件的权限和安全性。

## /home 目录

/home 目录是用户的主目录，每个用户在 /home 目录下都有一个以其用户名命名的子目录。用户的所有个人文件和配置文件都存放在这个子目录中。例如，用户 `john` 的主目录为 `/home/john`。

常见的文件和子目录包括：

* **~/Documents**：用户的文档目录。
* **~/Downloads**：用户的下载目录。
* **~/Pictures**：用户的图片目录。
* **~/.bashrc**：Bash Shell 配置文件。
* **~/.profile**：用户的环境设置文件。

用户目录的权限设置通常是这样的，只有该用户和超级用户（root）可以访问和修改其内容。这可以保护用户的隐私和数据安全。

## /var 目录

/var 目录用于存放系统运行时产生的可变数据。不同于 /etc 目录中的配置文件，/var 中的数据是动态变化的。

常见的子目录和文件包括：

* **/var/log**：系统日志文件目录。常见的日志文件有 `/var/log/syslog`（系统日志）、`/var/log/auth.log`（认证日志）、`/var/log/kern.log`（内核日志）等。
* **/var/mail**：用户邮件存放目录。
* **/var/spool**：队列目录，用于存放打印任务、邮件队列等。
* **/var/cache**：应用程序缓存文件。
* **/var/www**：Web 服务器的根目录，存放网站文件。

/var 目录中的数据可能会迅速增长，因此需要定期清理和维护，以防止磁盘空间不足。

## /usr 目录

/usr 目录用于存放用户级应用程序和文件。这是一个非常重要的目录，包含了大量的二进制文件、库文件、文档和其他资源。

常见的子目录包括：

* **/usr/bin**：用户级命令的二进制文件。常见的命令有 `gcc`（GNU 编译器）、`perl`（Perl 解释器）等。
* **/usr/sbin**：系统管理命令的二进制文件。与 /sbin 类似，但这些命令不是启动时必须的。
* **/usr/lib**：库文件目录，存放应用程序和系统所需的共享库。
* **/usr/share**：共享数据目录，存放不特定于某个用户或系统的共享数据，如文档、图标、声音等。
* **/usr/local**：本地安装的软件和文件。用户可以在不影响系统其他部分的情况下安装和管理软件。

/usr 目录中的内容通常由系统包管理器管理，如 apt、yum 等。

## /opt 目录

/opt 目录用于安装附加软件包。通常，第三方软件或自定义应用程序会安装在此目录下。每个软件通常会在 /opt 下有一个独立的子目录，例如 `/opt/software`。这种方式可以避免与系统的其他部分产生冲突，并便于管理和卸载。

## /mnt 目录

/mnt 目录用于临时挂载文件系统。系统管理员可以将外部存储设备（如 USB 驱动器、网络文件系统等）挂载到 /mnt 下的某个子目录中。例如，可以使用 `mount /dev/sdb1 /mnt/usb` 将一个 USB 驱动器挂载到 `/mnt/usb`。

## /media 目录

/media 目录用于自动挂载的可移动设备，如光盘、U 盘等。当这些设备插入时，系统会自动将其挂载到 /media 下的一个子目录中。例如，插入一个 U 盘后，系统可能会在 `/media/user/USB` 下自动创建一个目录并挂载该设备。

## /boot 目录

/boot 目录包含启动加载程序和内核文件。系统启动时，启动加载程序（如 GRUB）会从这里加载内核和其他必要文件。

常见文件包括：

* **vmlinuz**：压缩的 Linux 内核镜像文件。
* **initrd.img**：初始 RAM 盘，用于启动时加载必要的驱动程序和文件系统。
* **grub**：GRUB 启动加载程序的配置文件和模块。

/boot 目录中的文件对于系统启动至关重要，因此应谨慎修改。

## /lib 目录

/lib 目录包含系统库文件和内核模块。系统启动时，许多关键程序依赖于这些库文件。常见的库文件包括 C 标准库（libc.so）、动态链接器（ld-linux.so）等。内核模块（如文件系统驱动、硬件驱动）通常位于 `/lib/modules` 目录中。

## /proc 目录

/proc 目录是一个虚拟文件系统，包含系统内核和进程信息。这个目录中的内容并不实际存在于磁盘上，而是由内核在运行时动态生成的。/proc 目录提供了一种方便的方式来访问系统信息和进程数据。

常见的文件和目录包括：

* **/proc/cpuinfo**：显示 CPU 的信息，包括型号、速度和核心数。
* **/proc/meminfo**：显示内存使用情况，包括总内存、可用内存和缓存。
* **/proc/uptime**：显示系统的运行时间和空闲时间。
* **/proc/[pid]/**：每个运行中的进程都有一个以其 PID（进程标识符）命名的子目录，包含该进程的详细信息，如状态、内存映射、打开的文件等。

/proc 目录中的信息对于系统管理员和开发者来说非常重要，因为它提供了对系统运行状态的实时监控和调试工具。

## /sys 目录

/sys 目录是另一个虚拟文件系统，提供系统设备和内核信息。与 /proc 类似，/sys 目录中的内容也是由内核在运行时动态生成的。/sys 目录主要用于提供内核与用户空间之间的接口，允许用户查看和配置硬件设备。

常见的文件和目录包括：

* **/sys/class/**：分类显示不同类型的设备，如网络设备（/sys/class/net）、块设备（/sys/class/block）等。
* **/sys/devices/**：显示系统中的所有设备，以设备树的形式组织。
* **/sys/module/**：显示已加载的内核模块及其参数。

通过 /sys 目录，用户和管理员可以方便地管理和配置系统硬件，进行性能调优和故障排除。

## /root 目录

/root 目录是超级用户（root）的主目录。与普通用户的主目录位于 /home 下不同，root 用户的主目录直接位于根目录下。这是因为 root 用户需要在单用户模式下进行系统维护和修复，/root 目录可以在没有挂载其他文件系统的情况下访问。常见的文件和目录包括：

* **/root/.bashrc**：root 用户的 Bash Shell 配置文件。
* **/root/.profile**：root 用户的环境设置文件。

root 用户拥有系统的最高权限，因此 /root 目录中的文件和配置通常只有 root 用户本身可以访问和修改。

## 符号链接（Symbolic Link）

符号链接是一种特殊的文件，它指向另一个文件或目录。符号链接可以简化文件路径访问和管理。创建符号链接的命令是 `ln -s`，例如：

```
ln -s /path/to/target /path/to/link
```

符号链接在文件目录结构中具有重要作用，尤其是在需要在多个位置访问同一文件或目录时。符号链接可以跨文件系统边界，并且可以指向目录或文件。

## /run 目录

/run 目录是一个临时文件系统，用于存放系统运行时的状态文件和进程信息。它是在系统启动时动态创建的，并且其内容在每次启动时都会被清空。常见的文件和目录包括：

* **/run/lock**：用于锁文件，防止多个进程同时访问同一个资源。
* **/run/user/**：用于用户相关的运行时数据，每个用户都有一个以其 UID 命名的子目录。

/run 目录中的文件和目录通常由系统服务和守护进程使用，提供了一种轻量级的进程间通信方式。

## /srv 目录

/srv 目录用于存放服务相关的数据。srv 是 "service" 的缩写，表示该目录用于存放系统提供的各种服务的数据。例如，Web 服务器的文件可以存放在 /srv/www 下，FTP 服务器的文件可以存放在 /srv/ftp 下。/srv 目录结构可以根据具体服务的需求进行自定义。

## /lost+found 目录

/lost+found 目录存在于每个使用 ext 文件系统（如 ext2、ext3、ext4）的文件系统根目录下。它用于存放文件系统在崩溃或损坏后恢复的文件碎片。当文件系统进行 fsck（文件系统一致性检查）时，找回的孤立文件会被放置在 /lost+found 目录中。系统管理员可以在检查后决定如何处理这些文件。

往期推荐

[一张图带你了解RJ45网线水晶头线序568A与568B区别！](http://mp.weixin.qq.com/s?__biz=MzIyMzIwNzAxMQ==&mid=2649460343&idx=1&sn=6ba11cd520c30591d67176580a36c84e&chksm=f03ee57bc7496c6d33ad071999f3af81ba9f97e40503009af4934b3c83342c313372f902815b&scene=21#wechat_redirect)

[一张图就把HTTPS工作原理讲明白了！](http://mp.weixin.qq.com/s?__biz=MzIyMzIwNzAxMQ==&mid=2649460322&idx=1&sn=f1f7d321fdab49718c02a326687aec38&chksm=f03ee56ec7496c789c8abcb79307cc107a86fa3f54070a8b44aecbf12266135f176a57fe4e9b&scene=21#wechat_redirect)

[三层交换机工作在哪一层？数据链路层 or 网络层？](http://mp.weixin.qq.com/s?__biz=MzIyMzIwNzAxMQ==&mid=2649460308&idx=1&sn=3d2b4a1d0f6a85314f4a3592849be4c2&chksm=f03ee558c7496c4ec3edfa47a40ad8fa9a6d0027b276105fc7b2b9b2fb2633c21c0503a7e73d&scene=21#wechat_redirect)

[神州数码DCR系列路由器命令大全，建议收藏！](http://mp.weixin.qq.com/s?__biz=MzIyMzIwNzAxMQ==&mid=2649460297&idx=1&sn=8e587327bf0ee63b014e5dad3df89686&chksm=f03ee545c7496c53f074da4494ddc2000d3f2e75755bdf2c0008d664ad922fe0fe3eddbd6a75&scene=21#wechat_redirect)

[Linux发行版三巨头，你会选择哪一个？](http://mp.weixin.qq.com/s?__biz=MzIyMzIwNzAxMQ==&mid=2649460267&idx=1&sn=66d8ce44bd6f0315632c60f4052bf620&chksm=f03ee527c7496c314963f37502795d862728ad7c6d29e91c1d55b476faa6b736029a67291533&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYSZg2GYcda1B62iaJk8Iib8wbWblGtibFOaJgUnFmDZYdq3FfAGOgkHSC5s9LR4f0tHsZibsAAtDtrokQ/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYSZg2GYcda1B62iaJk8Iib8wb37WKBy82DtAicwrzyuVtJwjzeibeGRscJcSLVUJkrDOcP0y6uog8Vb0w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/6OibpDQ66VYQNIyABHZrCWcZT6asQr23iaLWWPSz81OT88sPo7CYIHjOZuPxyOKvXpHU9UtsT7l9eJvR69dejCNA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dDhDhftpRFuouuxbQ44msKkdjic0C8WOQrHEN6rex1hiblHTTIpApR8safvHvB9zXorQTMStvvyN2zO8xjOJd5vg/0?wx_fmt=png)

电子物证

向上...