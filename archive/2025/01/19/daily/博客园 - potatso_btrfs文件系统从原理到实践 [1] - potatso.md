---
title: btrfs文件系统从原理到实践 [1] - potatso
url: https://www.cnblogs.com/potatso/p/18678520
source: 博客园 - potatso
date: 2025-01-19
fetch_date: 2025-10-06T20:04:31.585673
---

# btrfs文件系统从原理到实践 [1] - potatso

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [btrfs文件系统从原理到实践 [1]](https://www.cnblogs.com/potatso/p/18678520 "发布于 2025-01-18 15:46")

作为Linux用户，我经常羡慕macOS系统的Time Machine功能。Time Machine就像是系统的最后一道防线，无论系统发生什么变化，它都能保护我们的数据安全，避免因误操作导致系统无法启动的困境。那么，Linux系统下是否也有类似的解决方案呢？基于这样的需求，我发现了Btrfs文件系统。

在深入了解Btrfs前，强烈建议你学习一下git的原理。二者有着很多相似之处。在后面我将大量使用通俗易懂的方式帮你掌握btrfs。

# Btrfs基本文件组织

在Btrfs中，文件系统的组织结构与Git非常相似：普通文件类似于Git中的blob对象，而目录则对应Git中的tree对象。以Linux的根目录为例，它是一个tree对象，其中包含了文件（blob对象）以及子目录（子tree对象）。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8bc84d4ee9c74309911a1dbbd1cd64f2.png#pic_center)

在Btrfs中，这些Tree对象被称为子卷（Subvolume）。子卷是Btrfs的一个核心概念，它本质上是一个特殊的目录，能够捕获并保存特定时刻的文件系统状态。这与快照（Snapshot）的概念密切相关。

创建一个空子卷

```
# 创建一个空子卷：

btrfs subvolume create <path>

# 例如，要在/mnt/btrfs下创建一个名为my_subvol的空子卷：

sudo btrfs subvolume create /mnt/btrfs/my_subvol
```

当Linux系统安装在Btrfs分区上时，系统默认会将根目录（/）设置为名为"@"的子卷。这是许多Linux发行版的标准做法，它为系统提供了更好的快照和回滚能力。

Btrfs子卷具有双重特性：它既可以作为普通目录在文件系统中进行管理，又可以像独立的分区一样被挂载到Linux系统的任意挂载点。这种灵活的特性为实现系统级别的快照和回滚功能奠定了重要基础。

## 快照

类似于Git的分支（branch）概念，Btrfs也实现了一种称为快照（Snapshot）的机制来保存文件系统的历史状态。在Btrfs中创建快照时，系统只会复制tree对象的结构，而不会复制实际的文件内容。这种设计与Git的存储机制非常相似：不同的快照之间会共享相同的文件数据（blob对象），每个快照只需要存储发生变化的部分。这种写时复制（Copy-on-Write）的策略使得快照操作既快速又节省存储空间。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/5cbd1c0358f64e52b8ce75fd2c05c5ef.png#pic_center)

在Btrfs的实现中，子卷和快照共享相同的底层数据结构。它们的主要区别在于创建方式：子卷可以作为独立的空白容器创建，而快照则必须基于现有的子卷创建，并会继承该子卷的全部数据状态。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/2065127896664476b04d0ac244840dee.png#pic_center)

btrfs创建快照的命令

```
# 创建一个名为snap的快照

btrfs subvolume snapshot -r /path/to/subvolume /path/to/snap
```

在拍摄快照的时候 `-r`参数代表创建一个只读快照。在这种情况下，快照只允许读取数据，不能进行写入操作。

## 快照的恢复

虽然Btrfs没有提供快照的直接恢复机制，但由于快照本质上是一个只读的子卷，我们可以直接访问快照中的文件内容。这种特性使得快照特别适合于选择性文件恢复的场景，用户可以方便地浏览快照中的文件，并选择所需的文件进行恢复。

首先查看系统中的快照

```
# 列出指定Btrfs文件系统中的所有子卷和快照

# 参数为Btrfs文件系统的挂载点或者子卷路径

btrfs subvolume list /
```

```
ID 256 gen 169953 top level 5 path var/lib/portables

ID 257 gen 169953 top level 5 path var/lib/machines

ID 1529 gen 192141 top level 5 path @

ID 1530 gen 192141 top level 5 path @home

ID 1532 gen 191492 top level 5 path timeshift-btrfs/snapshots/2024-12-26_10-13-46/@

ID 1533 gen 171944 top level 5 path timeshift-btrfs/snapshots/2024-12-26_10-13-46/@home

ID 1534 gen 171908 top level 5 path timeshift-btrfs/snapshots/2024-12-26_10-41-36/@

ID 1535 gen 171944 top level 5 path timeshift-btrfs/snapshots/2024-12-26_10-41-36/@home

ID 1544 gen 191492 top level 5 path timeshift-btrfs/snapshots/2024-12-27_13-39-08/@

ID 1545 gen 191492 top level 5 path timeshift-btrfs/snapshots/2024-12-31_14-51-04/@

ID 1588 gen 189590 top level 5 path timeshift-btrfs/snapshots/2025-01-02_08-39-31/@
```

输出结果中的`path`字段显示了每个子卷的路径。通常情况下，我们可以直接通过这个路径访问快照的内容。但需要注意的是，如果你的系统本身就安装在Btrfs文件系统上（根目录挂载在`@`子卷），那么这些快照可能无法通过常规路径直接访问，因为它们位于Btrfs文件系统的根层级。

#### 手动挂载

linux的mount在挂载Btrfs的时候，同时支持挂载的子卷或快照。这样我们同样实现了查看快照内容的目的。

```
# 挂载快照

# 手动挂载快照以访问

sudo mount -o subvol=快照路径 /dev/硬盘 /mnt/临时目录
```

虽然单个文件的恢复需要一些额外步骤，但对于整个系统的恢复，Btrfs提供了更优雅的解决方案：GRUB引导加载器支持直接从Btrfs的子卷或快照启动系统。这意味着我们可以在启动时选择任意一个系统快照作为根文件系统，从而实现完整的系统状态回滚。

从GRUB配置中可以看到，通过在`rootflags`参数中指定`subvol`选项，我们可以轻松地选择要启动的Btrfs子卷或快照。这种优雅的设计使得系统回滚变得异常简单。

```
insmod ext2

if [ x$feature_platform_search_hint = xy ]; then

search --no-floppy --fs-uuid --set=root 35669a62-1315-4b0b-be17-92f89eebffc2

else

search --no-floppy --fs-uuid --set=root 35669a62-1315-4b0b-be17-92f89eebffc2

fi

echo 'Loading Snapshot: 2024-10-28 16:48:06 .snapshots/1/snapshot'

echo 'Loading Kernel: vmlinuz-6.8.0-51-generic ...'

linux "/vmlinuz-6.8.0-51-generic" root=UUID=0841c522-e696-4499-8f39-3de52d1a4120 rootflags=defaults,subvol=".snapshots/1/snapshot"

echo 'Loading Initramfs: initrd.img-6.8.0-51-generic ...'

initrd "/initrd.img-6.8.0-51-generic"
```

在上面的GRUB启动linux的参数中，`rootflags`中的`subvol`就是启动linux目录的btrfs子卷或快照。是不是很简单。

# Btrfs快照备份与恢复

## Btrfs快照备份

Btrfs同样也支持把快照同步到外部存储设备上。命令也很简单

```
sudo btrfs send /path/to/snapshot | pv > 备份文件路径
```

因为`btrfs send` 发送快照的时候，默认使用输出，并且没有任何进度提示。使用`pv`命令可以实现进度提示，但是需要安装`pv`工具。

这时，你可能发现，既然压缩一下快照岂不美哉。我们可以在pv后面直接使用gzip或者tar等命令实现快照的压缩。

```
sudo btrfs send /path/to/snapshot | pv | gzip > 备份文件路径.gz
```

`btrfs send`命令需要快照为可读才能被发送到外部设备。如果快照不是可读，你需要下面的命令去设置快照为可读属性

```
sudo btrfs prop set /path/to/snapshot ro false
```

ro为true代表把快照设置为可读，false代表把快照设置为可读可写。

## Btrfs 快照恢复

Btrfs同样也支持从外部存储设备恢复快照。命令也很简单

```
pv 备份文件路径 | btrfs receive /path/to/subvolume
```

嗯，聪明的你应该想到了，可以配合btrfs快照备份功能与Grub的启动参数，实现间接的系统迁移。

# Btrfs的错误检查与恢复

与传统文件系统相比，Btrfs提供了更强大的错误检查和修复功能。它不仅能够检测文件系统的错误，还能在某些情况下自动修复这些问题。

## 文件系统检查

Btrfs提供了专门的工具用于检查文件系统的完整性：

```
# 只读模式检查文件系统

sudo btrfs check /dev/sdX

# 使用--repair选项进行修复（需要谨慎使用）

sudo btrfs check --repair /dev/sdX
```

需要注意的是，在执行修复操作之前，强烈建议先创建一个完整的数据备份。`--repair`选项虽然强大，但在某些情况下可能会导致数据丢失。

## 文件系统清理

Btrfs还提供了清理（scrub）功能，用于主动检测和修复数据错误：

```
# 启动清理操作

sudo btrfs scrub start /mount/point

# 查看清理状态

sudo btrfs scrub status /mount/point
```

清理操作会读取文件系统中的所有数据，验证校验和，并在可能的情况下自动修复发现的错误。这是一个后台进程，不会影响系统的正常使用，但可能会占用一些磁盘I/O带宽。

## 常见问题修复

1. **空间不足问题**

```
# 删除旧快照和不需要的数据

sudo btrfs subvolume delete /path/to/old_snapshot

# 平衡文件系统

sudo btrfs balance start /mount/point
```

### Btrfs平衡操作详解

Btrfs平衡操作（Balance）是系统维护的一个重要方面。它通过重新分配数据块来优化存储空间的使用，确保文件系统保持健康和高效。

#### 为什么需要平衡？

随着文件系统的使用，数据块的分布可能变得不均匀。这种情况可能导致：

* 某些存储区域过度使用而其他区域闲置
* 可用空间虽然足够，但过于分散而无法分配大文件
* 元数据和数据的分布不合理，影响性能

#### 平衡操作的作用

通过执行平衡操作，Btrfs会：

* 重新组织数据块的分布
* 回收被标记为已删除的空间
* 优化元数据的存储位置
* 提高整体存储效率

#### 执行平衡操作

```
# 平衡文件系统

sudo btrfs balance start /mount/point
```

#### 注意事项

* 在执行平衡操作之前，建议先备份重要数据
* 平衡操作可能需要较长时间，具体取决于文件系统的大小和复杂度
* 在平衡操作期间，系统可能会占用更多的磁盘I/O带宽

2. **元数据备份恢复**

```
# 重新扫描设备以查找备份的元数据

sudo btrfs rescue super-recover /dev/sdX
```

3. **碎片整理**

```
# 对指定目录进行碎片整理

sudo btrfs filesystem defragment -r /path/to/directory
```

## 最佳实践

1. 定期执行清理操作以及早发现潜在问题
2. 保持充足的可用空间（建议至少保留10%的空闲空间）
3. 定期创建数据备份，特别是在执行修复操作之前
4. 监控系统日志以及时发现文件系统警告或错误

通过这些工具和实践，我们可以有效地维护Btrfs文件系统的健康，及时发现并解决潜在的问题。

下一节，我们将重点讲一下，如何使用Btrfs去实现linux系统的备份与恢复。

posted @
2025-01-18 15:46
[potatso](https://www.cnblogs.com/potatso)
阅读(488)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-2025092...