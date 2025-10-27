---
title: Linux系统通过LVM扩容逻辑卷方法
url: https://blog.upx8.com/3187
source: 黑海洋 - WIKI
date: 2023-01-16
fetch_date: 2025-10-04T03:59:49.873057
---

# Linux系统通过LVM扩容逻辑卷方法

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux系统通过LVM扩容逻辑卷方法

发布时间:
2023-01-15

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
12729

前言：之前教程讲过如何将磁盘创建LVM逻辑卷分区方法,本文介绍了linux如何通过LVM（Logical Volume Manager）扩容一个逻辑卷LV（Logical Volume）的详细方法。
**提醒：数据无价,操作前,务必做好备份,以免误操作数据丢失。**
**创建LVM逻辑卷分区方法：**<https://blog.upx8.com/3188>
**1、使用以下命令查看ECS实例中已经创建的逻辑卷LV信息**

> lvdisplay

查询结果如下,表示已经创建了/dev/lvm\_01/lv01逻辑卷，拥有19 GiB空间

> [root@blog.tag.gg~]# lvdisplay
>   --- Logical volume ---
>   LV Path                /dev/lvm\_01/lv01
>   LV Name                lv01
>   VG Name                lvm\_01
>   LV UUID                Fli6Tf-uv01-6l9Y-CzNc-mgzu-y2Zr-35QotA
>   LV Write Access        read/write
>   LV Creation host, time blog.tag.gg, 2022-12-04 13:56:33 +0800
>   LV Status              available
>   # open                 0
>   LV Size                19.00 GiB
>   Current LE             4864
>   Segments               1
>   Allocation             inherit
>   Read ahead sectors     auto
>   - currently set to     8192
>   Block device           252:0

**2、使用以下命令扩容物理卷PV（Physical Volume）。**
命令格式：

> pvresize <物理卷名称>

以下示例为扩容物理卷（/dev/vdc），您需要根据实际情况修改物理卷名称

> pvresize /dev/vdc

执行结果如下：

> [root@blog.tag.gg~]# pvresize /dev/vdc
>   Physical volume "/dev/vdc" changed
>   1 physical volume(s) resized or updated / 0 physical volume(s) not resized

使用以下命令查看物理卷（PV）使用情况

> pvs

显示如下：

> [root@blog.tag.gg~]# pvs
>   PV         VG     Fmt  Attr PSize   PFree
>   /dev/vdc   lvm\_01 lvm2 a--  <35.00g <16.00g

**3、使用以下命令扩容逻辑卷。**
命令格式：

> lvextend [-L <逻辑卷大小>] <逻辑卷名称>

以下示例为扩容逻辑卷容量。

> lvextend -L +15G /dev/lvm\_01/lv01

**注意：**15G是指这块磁盘新增加的容量,比如原来我磁盘是20G,我将磁盘扩容到了35G,所以35-20=15G
本示例中变量说明如下，您需要根据实际情况修改。
+15G：增减容量，卷组VG（Volume Group）必须有剩余容量时才可以执行扩容逻辑卷操作。
/dev/lvm\_01/lv01：逻辑卷名称。
执行结果如下：

> [root@blog.tag.gg~]# lvextend -L +15G /dev/lvm\_01/lv01
>   Size of logical volume lvm\_01/lv01 changed from 19.00 GiB (4864 extents) to 34.00 GiB (8704 extents).
>   Logical volume lvm\_01/lv01 successfully resized.

**4、使用以下命令扩容逻辑卷文件系统**
您需要根据逻辑卷的文件系统类型执行不同的扩容命令，以下以ext4和xfs文件系统为例：
**说明**如果您不清楚逻辑卷的文件系统类型，可以通过df -Th命令查询。
如果是ext4文件系统，使用以下命令扩容。

> resize2fs /dev/lvm\_01/lv01

如果是xfs文件系统，使用以下命令扩容。

> xfs\_growfs /dev/lvm\_01/lv01

执行结果如下：

> [root@blog.tag.gg~]# resize2fs /dev/lvm\_01/lv01
> resize2fs 1.42.9 (28-Dec-2013)
> Filesystem at /dev/lvm\_01/lv01 is mounted on /media/lv01; on-line resizing required
> old\_desc\_blocks = 3, new\_desc\_blocks = 5
> The filesystem on /dev/lvm\_01/lv01 is now 8912896 blocks long.

5、扩容完成后执行命令查看扩容后的信息。

> df -Th

> [root@blog.tag.gg~]# df -h
> Filesystem               Size  Used Avail Use% Mounted on
> devtmpfs                 461M     0  461M   0% /dev
> tmpfs                    471M     0  471M   0% /dev/shm
> tmpfs                    471M  564K  471M   1% /run
> tmpfs                    471M     0  471M   0% /sys/fs/cgroup
> /dev/vda1                 40G  2.1G   36G   6% /
> tmpfs                     95M     0   95M   0% /run/user/0
> /dev/mapper/lvm\_01-lv01   34G   48M   32G   1% /media/lv01

[取消回复](https://blog.upx8.com/3187#respond-post-3187)

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