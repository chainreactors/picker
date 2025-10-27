---
title: 给本子安装 manjaro 出现无法关机的解决办法 - 糖醋鱼的小破站
url: https://buaq.net/go-130991.html
source: unSafe.sh - 不安全
date: 2022-10-16
fetch_date: 2025-10-03T20:01:27.380437
---

# 给本子安装 manjaro 出现无法关机的解决办法 - 糖醋鱼的小破站

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

给本子安装 manjaro 出现无法关机的解决办法 - 糖醋鱼的小破站

2018-04-29
*2022-10-15 17:27:32
Author: [expoli.tech(查看原文)](/jump-130991.htm)
阅读量:39
收藏*

---

2018-04-29 / 2018-04-29
/
[Manjaro](https://expoli.tech/tags/Manjaro)
[坑](https://expoli.tech/tags/%E5%9D%91)

## 给本子安装 manjaro 出现无法关机的解决办法

![image5392afeff1aea1e6.md.png](https://expoli.tech/articles/2018/04/29/18-04-29-fix-manjaro-can-t-shoutdown-problem/image5392afeff1aea1e6.md.png?imageView2/2/w/1280/format/jpg/interlace/1/q/100)

### 给本子安装manjaro 出现无法关机的解决办法

**manjaro-kde-17.1.8-stable** 和 **win10** 双系统 总是发现在关机或者重启的时候，无法关掉电源，只能按电脑的电源按钮才可以强行关掉， 最后通过以下办法才解决。

### 方案一

* 首先编辑 `/etc/default/grub*` 文件，再该文件下查找`GRUB_CMDLINE_LINUX=""`一行，修改为：

```
GRUB_CMDLINE_LINUX="reboot=efi"
```

* 然后执行如下命令：

```
$ sudo update-grub
```

* 更新 `/boot/grub/grub.cfg`文件。

  + 注：更新完了之后，默认grub菜单的选择时间为10秒，可以按照自己的需求修改。
  + 注：如果上边修改的 `/etc/default/grub` 文件，没有作用，可以继续尝试替换为下边的几种内容。

```
GRUB_CMDLINE_LINUX="reboot=bios"

GRUB_CMDLINE_LINUX="reboot=acpi"

GRUB_CMDLINE_LINUX="reboot=pci"
```

### 方案二

在终端用打开编辑 `/boot/grub/grub.cfg`文件：

```
$ sudo vi  /boot/grub/grub.cfg
```

找到下面内容（在第 **140** 行附近）：

```
inux --class gnu --class os {

        recordfail

        gfxmode $linux_gfx_mode

        insmod gzio

        insmod part_msdos

        insmod ext2

        set root='(hd0,msdos11)'

        search --no-floppy --fs-uuid --set=root ed532c1f-b89a-470c-ad6f-539a3f04b993

        linux   /boot/vmlinuz-3.2.0-24-generic-pae root=UUID=ed532c1f-b89a-470c-ad6f-539a3f04b993 ro   quiet splash $vt_handoff **acpi=force**

        initrd  /boot/initrd.img-3.2.0-24-generic-pae

}
```

如上面 **acpi=force** 标记，在此处加上 **acpi=force** **保存退出**。

### 方案三

**有可能是显卡驱动的问题**

```
$ sudo vim /etc/modprobe.d/blacklist.conf
```

然后添加如下内容：

```
blacklist vga16fb

blacklist nouveau

blacklist rivafb

blacklist nvidiafb

blacklist rivatv
```

**重启测试**

### 方案四

```
# 1.安装 watchdog
$ sudo apt install watchdog

# 2.开启 watchdog 服务
$ sudo systemctl enable watchdog.service

# 3.马上启用 watchdog 服务
$ sudo systemctl start watchdog.service
```

**我 Asus FX50V 主板 采用的是 `方案一` 的 `ACPI 参数` 和 `方案 二` 进行解决的**

**希望能够帮到你!**

* [给本子安装manjaro 出现无法关机的解决办法](#b3_solo_h3_0)
* [方案一](#b3_solo_h3_1)
* [方案二](#b3_solo_h3_2)
* [方案三](#b3_solo_h3_3)
* [方案四](#b3_solo_h3_4)

文章来源: https://expoli.tech/articles/2018/04/29/1564656228192.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)