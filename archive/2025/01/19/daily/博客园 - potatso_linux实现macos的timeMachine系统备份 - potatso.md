---
title: linux实现macos的timeMachine系统备份 - potatso
url: https://www.cnblogs.com/potatso/p/18678521
source: 博客园 - potatso
date: 2025-01-19
fetch_date: 2025-10-06T20:04:31.387708
---

# linux实现macos的timeMachine系统备份 - potatso

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

# [linux实现macos的timeMachine系统备份](https://www.cnblogs.com/potatso/p/18678521 "发布于 2025-01-18 15:46")

在上一篇文章中，我们详细介绍了Btrfs文件系统的基本使用方法和核心原理。本文将重点讲解如何利用Btrfs的特性来实现系统备份功能。

实现原理其实很简单：Linux内核支持直接从Btrfs的子卷（subvolume）启动系统。基于这个特性，我们可以通过计划任务定期为系统根目录创建快照，再配合btrfs-linux自动生成对应的GRUB启动项，从而实现完整的系统备份和恢复功能。

为了简化操作流程，我推荐使用TimeShift或Snapper这类工具。它们提供了图形化界面，让系统备份和恢复变得更加直观和便捷。

# 准备工作

timeshift需要根子卷（@）以及home子卷（@home）这两个特殊的子卷。但是Ubuntu在默认安装时候并不会创建这两个子卷。所以我们要手工创建一下。

在安装Ubuntu时，强烈建议将/boot目录单独分区。这是因为GRUB在读取grub.cfg配置文件时不支持Btrfs子卷机制。如果不单独分区，当系统挂载到@子卷后，新生成的grub.cfg会位于@子卷的/boot目录下，而不是原始根目录的/boot下，导致GRUB引导配置失效。如果你在安装时未进行单独分区，请不用担心，后续章节会详细介绍解决方案。

在这里默认你已经将ubuntu安装到btrfs中。

步骤：

1. 创建@子卷。
   `sudo btrfs subvolume snapshot / /@`
2. 创建@home子卷
   `sudo btrfs subvolume create /@home`
3. 复制home文件夹的内容到@home子卷
   `sudo cp -a /home/* /@home`
4. 修改grub，在linux启动参数中新增btrfs子卷
   修改/etc/default/grub，在`GRUB_CMDLINE_LINUX_DEFAULT`这行追加`rootflags=subvol=@`
5. 执行 `sudo update-grub`更新grub引导
6. 重启
7. 修改/etc/fstab，直接原有的 `/` 挂载上修改，删除subvolid=x字段，如果存在subvol，否则追加`subvol=/`改成`/@`。如下所示

```
/dev/disk/by-uuid/uuid / btrfs defaults,subvol=/@ 0 1
```

8. 复制上面一行的内容，将/改成/home ,subvol=/@改成/@home，目的为了挂载@home子卷

```
/dev/disk/by-uuid/uuid /home btrfs defaults,subvol=/@home 0 1
```

9. 重启

# Timeshift

首先安装Timeshift
`sudo apt install timeshift`
按照下一步下一步，开启timeshift备份即可。
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/7e81aebd2a424552b9ee6a40b8e2f8b8.png#pic_center)

# grub备份

下面我们讲解一下，如何将btrfs的备份通过grub-btrfs生成grub参数。

参考安装grub-btrfs
<https://github.com/Antynea/grub-btrfs>

使用`make && make install`即可安装。

在安装过程中需要你手动安装inotify。
`sudo apt-get install inotify-tools`

启动grub-btrfs服务。
`sudo systemctl start grub-btrfsd`

检查grub-btrfs的服务状态 `sudo systemctl status grub-btrfsd`
检查一下如果出现这种，就代表设置成功

```
 grub-btrfsd.service - Regenerate grub-btrfs.cfg
     Loaded: loaded (/etc/systemd/system/grub-btrfsd.service; disabled; preset:>
     Active: active (running) since Sat 2025-01-18 15:36:57 CST; 1min 56s ago
   Main PID: 4862 (bash)
      Tasks: 3 (limit: 18694)
     Memory: 1.3M (peak: 4.1M)
        CPU: 48ms
     CGroup: /system.slice/grub-btrfsd.service
             ├─4862 bash /usr/bin/grub-btrfsd --syslog -t
             ├─4867 bash /usr/bin/grub-btrfsd --syslog -t
             └─4873 inotifywait -q -q -e create -e delete /run/timeshift
```

最终在系统启动中的效果如下:
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/67b9fe384e2b4654af5cd85bebe1a7b3.jpeg#pic_center)

posted @
2025-01-18 15:46
[potatso](https://www.cnblogs.com/potatso)
阅读(56)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025