---
title: Kali linux is Missing from Boot Menu
url: https://buaq.net/go-174343.html
source: unSafe.sh - 不安全
date: 2023-08-14
fetch_date: 2025-10-04T11:59:16.657781
---

# Kali linux is Missing from Boot Menu

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

Kali linux is Missing from Boot Menu

Hello learners, hope you all are doing well today we are going to discuss an error or misconfigurati
*2023-8-13 20:0:39
Author: [infosecwriteups.com(查看原文)](/jump-174343.htm)
阅读量:14
收藏*

---

[![Rajneesh Kumar Arya](https://miro.medium.com/v2/resize:fill:88:88/0*ojmRLBxp_zPxe_Wz)](https://medium.com/%40RajneeshKarya?source=post_page-----6bab6ae304f3--------------------------------)[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:48:48/1*A6LVtmXcJ3QJy_sdCyFx1Q.png)](https://infosecwriteups.com/?source=post_page-----6bab6ae304f3--------------------------------)

Hello learners, hope you all are doing well today we are going to discuss an error or misconfiguration that you would have encountered. Let me explain you this

As I was going to download the latest version of Kali Linux I remember a thing called mounting a system which scratch that part of my mind and I canceled the idea to reinstall Kali Linux and boot a pen drive of kali linux live USB and opened a live system of kali Linux.
After that, I start a Terminal and type the following command to find out the Linux filesystem drive name

> sudo fdisk -l

This command will list all the drives partitions search for your linux filesystem name which is something like /dev/sdaX (replace X by the number of your filesystem)

After that we need to mount this drive for that just type the following command

> sudo mount /dev/sdaX /mnt

and to use your kali linux filesystem you need to bind some more directory like /dev , /sys etc.. First, create directory for mounting by following commands

> sudo mkdir /mnt/dev
>
> sudo mkdir /mnt/proc
>
> Note : If these files are already exist in your system so the above command will tell you and you don’t need to consider that warning as an error just continue with the next step

After that just create one more directory and make sure you type the following command correctly because this is the main directory where your EFI Variables are going to store. Otherwise, you’ll get an error EFI variable not set.

sudo mkdir -p /mnt/sys/firmware/efi/efivars

now mount the and bind the directories by the following commands:-

> sudo mount — bind /dev /mnt/dev
>
> sudo mount — bind /sys /mnt/sys
>
> sudo mount — bind /proc /mnt/proc
>
> sudo mount — bind /sys/firmware/efi/efivars /mnt/sys/firmware/efi/efivars

After that create one more directory /mnt/boot/efi.

> sudo mkdir -p /mnt/boot/efi

In the above command -p is to tell the system that we need a parent directory.

Now again type the command sudo fdisk -l and find the EFI filesystem name, I am referring that name with /dev/sdaY you need to replace Y with your filesystem number.

Now, mount the EFI filesystem to /mnt/boot/efi which we just created for that just type the following command.

> sudo mount /dev/sdaY /mnt/boot/efi
>
> sudo mount -o remount,rw /dev/sdaY /mnt/boot/efi

Now after that create a directory to mount the content of run directory

> sudo mkdir /mnt/hostrun

Now mount and bind /run to /mnt/hostrun

> sudo mount — bind /run /mnt/hostrun

Ready for the magic???

Now as you typed the following command you can access to your system with CLI only but you can access any data of your filesystem you can store the data to a pendrive so that you can reinstall the kali linux without any loss of data. And the command is :

> sudo chroot /mnt

chroot : change the root directory

But you all will say that you have canceled the idea of reinstalling and now you are saying to take your data and reinstall.

Yaah! I said this but That’s only the one way to save your data Let me tell you how you can access you kali linux without reinstalling it.

Okay jokes apart, You need to create one more directory inside chroot enviroment. By following command

> mkdir /run/lvm

and as always we are created this directory because we need to mount something.

> mount — bind /hostrun/lvm /run/lvm

Now we need to install and update grub and we are almost done.

> grub-install /dev/sda
>
> update-grub

Now exit the chroot Enviroment By typing exit and unmount all the devices you have mounted.

> sudo umount /mnt/dev
>
> sudo umount /mnt/proc
>
> sudo umount /mnt/sys
>
> sudo umount /mnt/sys/firmware/efi/efivars
>
> sudo umount /mnt/boot/efi
>
> sudo umount /mnt/hostrun
>
> sudo umount /mnt/run/lvm
>
> sudo umount /mnt

After Unmounting all the devices just reboot your System and CONGRATS!! Your Kali linux is now home.

means it starts appearing in boot menu and you can run it easily as before.

> Today we are using it to resolve our problem but it can also be used as a weapon to kill someones system and get their files and data.
>
> DISCLAIMER : DO NOT USE THESE TECHNIQUE TO HACK ANYONE UNLESS YOU HAVE EXCLUSIVE PERMISSIONS

So, This is it for today till then keep Learning keep Exploring And most Important…..DO HACKING..

文章来源: https://infosecwriteups.com/kali-linux-is-missing-from-boot-menu-6bab6ae304f3?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)