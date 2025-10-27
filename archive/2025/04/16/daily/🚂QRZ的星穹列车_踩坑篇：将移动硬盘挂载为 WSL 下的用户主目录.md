---
title: 踩坑篇：将移动硬盘挂载为 WSL 下的用户主目录
url: https://qrz.today/00-notes/wsl/make-portable-disk-as-home
source: 🚂QRZ的星穹列车
date: 2025-04-16
fetch_date: 2025-10-06T22:07:26.393145
---

# 踩坑篇：将移动硬盘挂载为 WSL 下的用户主目录

## [🚂QRZ的星穹列车](../..)

搜索

Search

暗色模式亮色模式

阅读模式

## 探索

[📑Tags](/tags)[🪪About](/misc/about)[📻Radio](/z6-life/ham-radio/index)[🧑‍🤝‍🧑Friends](/misc/friends)[🚇开往](https://www.travellings.cn/go.html)

---

[Home](../../)

❯

[笔记](../../00-notes/)

❯

[wsl](../../00-notes/wsl/)

❯

踩坑篇：将移动硬盘挂载为 WSL 下的用户主目录

# 踩坑篇：将移动硬盘挂载为 WSL 下的用户主目录

2025年4月15日10分钟阅读

* [windows/wsl](../../tags/windows/wsl)

### 目录

* [前言](#前言)
* [初始步骤](#初始步骤)
* [格式化并挂载空硬盘](#格式化并挂载空硬盘)
* [挂载带内容的硬盘](#挂载带内容的硬盘)
* [奇怪的问题](#奇怪的问题)
* [正确的挂载方式](#正确的挂载方式)
* [问题成因猜测](#问题成因猜测)

虽然 Windows 已经成为了很棒的 Linux 发行版，不过在使用时会逐渐累积一个很大的 vhdx 文件。尽管我们可以[迁移子系统文件](https://zhuanlan.zhihu.com/p/660443677)到其他硬盘，但是总而言之都不是很方便使用。因此我希望将 wsl 的数据移动到移动硬盘中。

> Tldr
>
> 如果对踩坑的过程不感兴趣，请直接跳到[正确的挂载方式](#%E6%AD%A3%E7%A1%AE%E7%9A%84%E6%8C%82%E8%BD%BD%E6%96%B9%E5%BC%8F)这一节。

## 前言

移动哪些数据到外置硬盘中呢？一种思路是将整个虚拟机都放进移动硬盘。由于 wsl 本质上是一个 vhdx，因此我们可以将这个 vhdx 放入移动硬盘，在其他电脑上使用时[配置注册表](https://zhuanlan.zhihu.com/p/338280729)。但以我在移动硬盘中使用虚拟机的经验，如果突然断连大概率出现数据损坏，而且我还希望可以同时在 Linux 和 Windows 上挂载，因此我决定将 `/home/user` 目录，也就是用户主目录移动到外置硬盘中。

最终，我的目标为：挂载移动硬盘到 wsl，用 btrfs 格式化，挂载为 `/home/user`，在使用时将硬盘挂载到 `/home/user` 目录，作为 user 用户使用硬盘中的数据。恰好我手上正好有一块三星 970 Evo Plus 2TB 的版本，NVMe 1.3 的速度虽然不适合作为主硬盘，但是作为外置硬盘走雷电 4 或 USB4 跑满 10Gbps 或 20Gbps 的硬盘盒还是足够的。

## 初始步骤

新版的 wsl2 已经支持挂载硬盘，参考 <https://learn.microsoft.com/en-us/windows/wsl/wsl2-mount-disk> 中的介绍逐步执行命令：

首先看电脑中的磁盘：

```
PS C:\Users\user> GET-CimInstance -query "SELECT * from Win32_DiskDrive"
```

这里会显示连接到电脑上的设备 ID、标题、分区数量与模型：

```
DeviceID           Caption                               Partitions Size          Model
--------           -------                               ---------- ----          -----
\\.\PHYSICALDRIVE1 ZHITAI TiPlus7100 2TB                 3          2048407280640 ZHITAI TiPlus7100 2TB
\\.\PHYSICALDRIVE0 ZHITAI TiPlus7100 2TB                 1          2048407280640 ZHITAI TiPlus7100 2TB
\\.\PHYSICALDRIVE2 Realtek RTL9210 NVME SCSI Disk Device 0          2000396321280 Realtek RTL9210 NVME SCSI Disk Device
```

我的电脑上连接了两块至态 TiPlus7100 2TB 的硬盘，外置硬盘则通过 ITGZ RTL9210 硬盘盒连接（三星、至态、ITGZ 请给我打广告费.jpg）。这里我要挂载 `\\.\PHYSICALDRIVE2`，执行：

```
wsl --mount \\.\PHYSICALDRIVE2 --bare
```

这样只会添加硬盘但不会挂载：

```
$ lsblk
NAME MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda    8:0    0 388.4M  1 disk
sdb    8:16   0     4G  0 disk [SWAP]
sdc    8:32   0     1T  0 disk /mnt/wslg/distro
                               /
sdd    8:48   0   1.8T  0 disk
```

没有挂载点的 `/dev/sdd` 就是目标。

## 格式化并挂载空硬盘

接下来首先格式化硬盘为 brtfs。在 Debian 下需要先安装 `btrfs-progs`：

```
sudo apt install btrfs-progs
```

强制格式化：

```
sudo mkfs.btrfs -f /dev/sdd
```

创建目录并挂载：

```
mkdir -p /home/user
mount /dev/sdd /home/user
```

接下来创建用户并将其设置指定到 `/home/user`

```
sudo useradd -m -d /home/user -s /bin/bash user
sudo passwd user
sudo usermod -aG sudo user
```

切换到用户 `user` 并验证其 `sudo` 权限：

```
su - user
sudo whoami
```

设置 home 目录权限：

```
sudo chown -R user:user /home/user
```

切换用户：

```
su - user
```

wsl 设置主用户

/etc/wsl.conf

```
[boot]
systemd=true
[user]
default=user
```

如果要从 WSL 2 卸载和分离磁盘，运行：

```
wsl --unmount <DiskPath>
```

## 挂载带内容的硬盘

在之后的使用中，我只需要执行以下步骤：

```
# 查看硬盘 ID
GET-CimInstance -query "SELECT * from Win32_DiskDrive"
# 挂载硬盘
sudo wsl --mount \\.\PHYSICALDRIVE2 --bare
# 查看 wsl 中的硬盘设备 ID
wsl -d Debian -u root -e lsblk
# 挂载硬盘为 home 目录
wsl -d Debian -u root -e mount /dev/sdd /home/user
```

## 奇怪的问题

最开始的时候一切都很美好，但是没过多久就开始出现问题。在使用 VSCode 时，必须在 `/home/user` 目录下以相对地址的形式打开文件夹才能正确打开 VSCode，否则会触发问题：

```
/mnt/c/Users/user/AppData/Local/Programs/Microsoft VS Code/Code.exe: Exec format error
```

实际上不只是 VSCode 用不了，所有 Windows 上的程序例如 cmd、explorer 等程序都无法使用。

在网上有许多关于此问题的讨论，[大部分解答](https://www.reddit.com/r/bashonubuntuonwindows/comments/11vx61n/wsl2_error_cannot_execute_binary_file_exec_format/)都是说重启 wsl 即可，但是在我这里始终无法解决问题。

除此之外，我还观察到一个现象：注意到 `wsl --mount` 命令需要管理员权限，我可以选择通过 `sudo` 命令运行，也可以以管理员权限启动终端后直接执行 `wsl --mount`。

如果我在普通权限启动终端并执行上述命令，就会发生以上问题，且在文件管理器中无法查看到挂载后的磁盘内容。

如果我以管理员权限启动终端并执行上述命令，尽管上述问题不会发生，但我无法在普通权限终端开启的 wsl 中查看挂载的硬盘中的文件。

更有趣的是，这同时会导致 Docker Desktop 出问题，因此我选择卸载 Docker Desktop，直接在 wsl 中安装 docker，但这也有问题：在运行 docker 时指定的 volume 在移动硬盘中的话，docker 中仍然无法访问到移动硬盘中的文件。不得不说，这实在是令人心态爆炸。

---

## 正确的挂载方式

在研究了[官方文档](https://learn.microsoft.com/en-us/windows/wsl/wsl2-mount-disk)后，我认为问题在于不能在 wsl2 里面 mount，而是在外面：

```
wsl --mount \\.\PHYSICALDRIVE2 --type btrfs --name user
```

此时会挂载到 `/mnt/wsl/user`，如果之前 `home` 为 `/home/user` 的话需要修改 home 目录：

```
sudo usermod -d /mnt/wsl/user user
```

可以检查 `home` 是否设置正确：

```
grep user /etc/passwd
```

可惜 wsl 的 mount 参数不支持挂载到指定地址，只能通过 [automount](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#automount-settings) 的 `root` 参数设置所有的 mount 地址。如果我设置该参数为 `/home`，自动挂载的 C、D 盘也会被挂载到 `/home` 目录。因此我决定先保持默认设置，以后遇到问题再考虑解决。

```
--mount <Disk>
    在所有 WSL 2 分发版中附加和装载物理磁盘或虚拟磁盘。

    选项:
        --vhd
            指定 <Disk> 引用虚拟硬盘。

        --bare
            将磁盘附加到 WSL2，但不要装载它。

        --name <Name>
            使用装入点的自定义名称装载磁盘。

        --type <Type>
            装载磁盘时要使用的文件系统(如果未指定)默认为 ext4。

        --options <Options>
            其他装载选项。

        --partition <Index>
            要装载的分区的索引(如果未指定)默认为整个磁盘。
```

这样一来，所有依赖于 `/home/user` 的配置都会遭到破坏（例如 `.zshrc`），需要修改对应的地址为 `$HOME`。

对于 conda/forge，它使用了大量写死的地址，因此如果更换用户主目录，则必然会破坏 conda 和 forge 路径。目前似乎没有好的解决方案，个人用[这个方案](https://www.v2ex.com/t/938669)作为替代：

1. pyenv 管理多版本 python
2. pipx 管理 python 构建的应用程序（比如 PDM 自己）
3. pdm 管理项目的依赖，构建发布内容

如果以后遇到问题再进行解决。

## 问题成因猜测

可能因为我的需求比较小众，也可能我的环境比较特别，我并没有看到与我遇到相似问题的情况。我猜测 wsl 在挂载硬盘的逻辑上仍有一些问题，用 wsl 的 `--mount` 参数挂载更符合 windows 的逻辑，而在 wsl 里面挂载可能会绕过一些 windows 的逻辑，导致问题的出现。具体问题成因我暂时没有精力分析，这里做个简单记录，如果有人遇到了类似的问题可以进行参考。

---

### 目录

* [前言](#前言)
* [初始步骤](#初始步骤)
* [格式化并挂载空硬盘](#格式化并挂载空硬盘)
* [挂载带内容的硬盘](#挂载带内容的硬盘)
* [奇怪的问题](#奇怪的问题)
* [正确的挂载方式](#正确的挂载方式)
* [问题成因猜测](#问题成因猜测)

### 关系图谱

### 反向链接

* [欢迎！](../../)

---

Made with ❤️ by QRZ using [Obsidian](https://obsidian.md/) and [Quartz](https://quartz.jzhao.xyz/), © 2025. [RSS Feed](https://qrz.today/index.xml)