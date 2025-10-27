---
title: 在VPS上安装Arch Linux
url: https://blog.upx8.com/3781
source: 黑海洋 - WIKI
date: 2023-08-15
fetch_date: 2025-10-04T12:02:39.618380
---

# 在VPS上安装Arch Linux

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 在VPS上安装Arch Linux

发布时间:
2023-08-14

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
11674

此安装方法适用于一些没有远程控制台（VNC/IPMI）又不能挂载ISO的机器。

如果你想完全从头开始安装，定制更多的内容（例如给硬盘重新分区之后再安装archlinux）可以试试我这个方法。

开始前确保机器有足够的内存，建议2GB起步，低于这个就不要试了。然后按照这篇文章进入到Grml live系统内：

注：务必按照文章内的配置使用toram来引导iso（将整个系统运行在内存中）

下面所有操作步骤都是在Grml live系统里面完成，首先下载archlinux-bootstrap并解压：

```
cd /tmp
wget https://geo.mirror.pkgbuild.com/iso/2023.05.03/archlinux-bootstrap-2023.05.03-x86_64.tar.gz
tar -xzvf archlinux-bootstrap-2023.05.03-x86_64.tar.gz
```

你的机器内存很宝贵，解压完成后务必删掉压缩包：

```
rm -rf archlinux-bootstrap-2023.05.03-x86_64.tar.gz
```

编辑源配置文件：

```
nano /tmp/root.x86_64/etc/pacman.d/mirrorlist
```

取消下面的注释：

```
Server = https://geo.mirror.pkgbuild.com/$repo/os/$arch
```

避免chroot后提示硬盘空间不足：

```
mount --bind root.x86_64 root.x86_64
```

chroot：

```
/tmp/root.x86_64/bin/arch-chroot /tmp/root.x86_64/
```

初始化key：

```
pacman-key --init
pacman-key --populate archlinux
```

更新系统并安装分区需要用到的工具：

```
pacman -Syyu
pacman -S dosfstools
```

删除当前硬盘所有分区表，此操作不可逆，三思而后行，现在后悔还来得及233，一旦执行下面的命令后，硬盘的数据将全部销毁：

```
wipefs -a /dev/vda
```

给硬盘分区，推荐用cfdisk这个分区工具，简单方便易上手：

```
cfdisk /dev/vda
```

基于你机器是使用uefi还是bios引导，分区方案有所不同，我这台机器是bios引导，所以我的分区方案如下：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/06/lala.im_2023-06-01_14-30-46.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/06/lala.im_2023-06-01_14-30-46.png)

注：bios引导如果硬盘使用gpt分区表则需要创建一个1mb的bios boot分区。

这里我也给出一个uefi分区的方案：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/06/lala.im_2023-06-01_12-14-41.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/06/lala.im_2023-06-01_12-14-41.png)

创建文件系统：

```
mkfs.ext4 /dev/vda3
```

仅uefi分区需要：

```
mkfs.fat -F 32 /dev/vda1
```

初始化swap：

```
mkswap /dev/vda2
```

挂载分区：

```
mount /dev/vda3 /mnt
```

启用swap：

```
swapon /dev/vda2
```

仅uefi分区需要：

```
mount --mkdir /dev/vda1 /mnt/boot
```

安装基本的软件包：

```
pacstrap -K /mnt base linux linux-firmware grub openssh nano
```

生成fstab配置文件：

```
genfstab -U /mnt >> /mnt/etc/fstab
```

退出chroot环境：

```
exit
```

再次chroot：

```
/tmp/root.x86_64/bin/arch-chroot /tmp/root.x86_64/mnt
```

时区配置：

```
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc
systemctl enable systemd-timesyncd.service
```

配置语言环境：

```
nano /etc/locale.gen
```

取消如下注释：

```
en_US.UTF-8 UTF-8
```

生成local信息：

```
locale-gen
```

创建如下配置文件：

```
nano /etc/locale.conf
```

写入：

```
LANG=en_US.UTF-8
```

设置主机名：

```
echo imlala > /etc/hostname
```

配置网络：

```
nano /etc/systemd/network/20-wired.network
```

我的配置仅供参考，请根据自己的网络环境正确配置：

```
[Match]
Name=eth0

[Network]
Address=xxx.xxx.xxx.xxx/24
Address=xxx:xxx:xxx:xxx:xxx::xxx/80
IPv6AcceptRA=no

[Route]
Gateway=xxx.xxx.xxx.xxx
GatewayOnLink=yes

[Route]
Gateway=xxx:xxx:xxx:xxx:xxx::xxx
GatewayOnLink=yes
```

这里还是简单介绍一下systemd-networkd的dhcp配置，如果网络支持dhcp，下面是一个最简配置：

```
[Match]
Name=eth0

[Network]
DHCP=yes
```

更多关于systemd-networkd的内容可以参考：https://wiki.archlinuxcn.org/wiki/Systemd-networkd

设置systemd-networkd开机自启：

```
systemctl enable systemd-networkd
```

配置dns：

```
nano /etc/resolv.conf
```

写入如下配置：

```
nameserver 8.8.8.8
nameserver 1.1.1.1
```

这里也可以用systemd-resolved来管理dns：https://wiki.archlinux.org/title/systemd-resolved

设置root密码：

```
passwd
```

编辑ssh配置文件：

```
nano /etc/ssh/sshd_config
```

允许root用户使用密码登录：

```
PermitRootLogin yes
```

设置sshd开机自启：

```
systemctl enable sshd
```

安装grub，对于bios引导的机器请使用下面的命令，注意是安装grub到硬盘而不是某一个分区：

```
grub-install --target=i386-pc /dev/vda
```

如果使用uefi引导，则还需要安装efibootmgr：

```
pacman -S efibootmgr
```

然后使用下面的命令安装grub：

```
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
```

生成grub的主配置文件：

```
grub-mkconfig -o /boot/grub/grub.cfg
```

为避免机器重启后，网卡接口名无法与systemd-networkd内配置的接口名相匹配，从而导致机器失联，编辑grub配置文件：

```
nano /etc/default/grub
```

添加net.ifnames=0内核启动参数：

```
GRUB_CMDLINE_LINUX_DEFAULT="net.ifnames=0"
```

重新生成grub主配置文件：

```
grub-mkconfig -o /boot/grub/grub.cfg
```

退出chroot环境并重启：

```
exit
reboot
```

重新登录ssh，检查一下：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/06/lala.im_2023-06-04_20-20-46.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/06/lala.im_2023-06-04_20-20-46.png)

[取消回复](https://blog.upx8.com/3781#respond-post-3781)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")