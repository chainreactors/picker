---
title: Linux提权系列4：揭秘 SUID 和 SGID 位
url: https://mp.weixin.qq.com/s?__biz=MzU4NjY0NTExNA==&mid=2247488773&idx=1&sn=bc74af262dedf199a6a40850288026cc&chksm=fdf97e10ca8ef706d62118e48e8b7d8b7f32184436bdc1635a2d0d37e1f30541805ea1a45811&scene=58&subscene=0#rd
source: 奶牛安全
date: 2023-03-29
fetch_date: 2025-10-04T11:02:07.823391
---

# Linux提权系列4：揭秘 SUID 和 SGID 位

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QXsgGBUcicbw0Cpdib2hmT2JxN3JzL1HmAjwGOsx9tvJiaic1rv4tbibq6bdxKU9KTymYE7KHNMRNiaO5WgSibv0avNZA/0?wx_fmt=jpeg)

# Linux提权系列4：揭秘 SUID 和 SGID 位

原创

debugeeker

奶牛安全

在上一篇文章中，了解了文件的三种权限类型：读、写和可执行，以及这些权限对文件和目录的作用有何不同。

此外，使用符号表示来更改该帖子中的权限，因为对于初学者来说它很容易理解。在`Linux` 中，还有另一种通过数字为文件分配权限的方法。

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbw0Cpdib2hmT2JxN3JzL1HmAhrOkEic9Pqz46TzesRryBa0t7y0iblMu1gXY0rYS5xCfLIgwoveia6kyA/640?wx_fmt=png)

上面每组是以3位的二进制来表示。这意味着`RWX`可以写成二进制形式的**111**，即 **7**。查看下表来了解符号和二进制的映射。

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbw0Cpdib2hmT2JxN3JzL1HmAHk7Fyu1e5B8wDPdy4jjTtg5cia3SJNIsyGicP0rakplhAvlTLpmBMs6Q/640?wx_fmt=png)

## SUID – SGID – 粘滞位

到现在可知，当使用`chmod 777`时，是用三组权限。其实，在前面还有一个额外的字节，默认为0。也就是说，**777**其实是**0777**。

下面是`strace chmod 777`的日志片段

```
fchmodat(AT_FDCWD, "domains.json", 0777) = 0
```

即使使用了 777，`chmod`仍将其转换为 0777。

第一个权限集称为特殊权限。和 RWX 一样，还有其他三个位。

* `SUID`:设置用户 ID
* `SGID`:设置组ID
* 粘滞位

由于这 3 位的权限集中在符号表示中没有其他可用空间，因此它取代了所有三组中的 `x` 权限。

表示如下

* `rwsrw-r-x`:SUID 位设置且二进制文件可执行
* `rwSrw-r-x`: 设置了 SUID 位并且二进制文件不可执行
* `rwxrwsr-x`: SGID 位设置且二进制文件可执行
* `rwxrwSr-x`: SGID 位设置且二进制文件不可执行

暂时忘记粘性位。将在“粘滞位与不可变文件”标题下讨论它。

运行一个启用了 SUID 位的文件时，它是当前用户ID运行，但有效ID却是文件属主的用户ID。

## 文件与目录上的 SUID / SGID

已经看到 SUID 和 SGID 在文件中的有效性。但是，将在这篇文章中进一步探讨它。但在此之前，解释一下在目录上设置时的效果。

SUID 位在大多数 Unix/Linux 中被忽略，因此它不会影响在目录中创建的文件。但是，当在目录上设置 SGID 位，然后在该目录中创建一个文件时，新文件的组将与目录的组相同。也就是说，假如用户的组是`hello`，在没有`SGID`的目录下创建文件，文件的组是`hello`，但如果在有`SGID`的目录下创建文件，如果这个目录的组是`world`，那么，这个文件的组是`world`。

```
$ mkdir mydir
$ chmod g+s,o+rwx mydir
$ stat -c "%A %n" mydir
drwxr-srwx mydir
$ ls -la mydir/
total 0
drwxr-srwx 2 terabyte terabyte  40 Aug  8 00:06 .
drwxr-xr-x 3 terabyte terabyte 100 Aug  8 00:06 ..
$ su amit -c "touch mydir/file"
Password:
$ ls -l mydir/
total 0
-rw-r--r-- 1 amit terabyte 0 Aug  8 00:07 file
```

## 运行中进程的用户 ID

基本上，对于每个进程，组和用户各有两个 ID。

* 有效ID(EUID)：文件所有者的用户/组（仅在 SUID/SGID 的情况下）
* 真实ID(RUID)：启动进程的用户/组

通常进程RUID和EUID相同。但是对于启用 SUID/SGID 位的程序，EUID 更改为文件所有者/组，而 RUID是启动进程的用户/组。要使进程"实际"具有提升权限的操作，仍然需要使用 `setuid` 系统调用.

这是一种临时提升权限然后在使用后删除它们的安全方法

```
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main(void) {
    // store the uids
    uid_t ruid = getuid();
    uid_t euid = geteuid();
    // store the gids
    gid_t rgid = getgid();
    gid_t egid = getegid();

    printf("Before execution UID: %d and EUID: %d\n", ruid, euid);
    printf("Before execution GID: %d and EGID: %d\n", rgid, egid);

    // elevate the privileges
    setuid(euid);
    setgid(egid);

    // perform action
    system("id > /tmp/output");

    // drop privileges
    if (setuid(ruid)) {
        fprintf(stderr, "Drop user privileges setuid(%d) failed!\n", ruid);
    }
    if (setgid(rgid)) {
        fprintf(stderr, "Drop group privileges setgid(%d) failed!\n", rgid);
    }

    printf("After execution UID: %d and EUID: %d\n", getuid(), geteuid());
    printf("After execution GID: %d and EGID: %d\n", getgid(), getegid());
    printf("Completed! Check output in /tmp/output\n");
    return 0;
}
```

编译代码并分配适当的权限

```
$ gcc -Wall -o program program.c
$ sudo chown root:root program
$ sudo chmod +sx program
```

用户和组 ID 的转换如下所示

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbw0Cpdib2hmT2JxN3JzL1HmA1RDicXmINlx5cV9xF46gQ4Lj3Ka8w0QNfXlZYzcwpqRGGXgVUkMUW6Q/640?wx_fmt=png)

在 `setuid(1000)` 之后删除组权限将失败，这是有道理的，因为 ID 为 1000 的用户没有调用 `setgid()` 系统调用的权限。

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbw0Cpdib2hmT2JxN3JzL1HmAAkAWNyWd7FBSlO8jW9ibFhn4UErv2JFR4at4gawrgFHXqqlyGCEXghw/640?wx_fmt=png)

## 粘滞位与不可变文件

有没有想过这样的情况，希望拥有一个全局可写的目录，只允许文件的所有者删除或重命名它？好吧，这就是粘滞位的作用。专门针对目录进行删除/重命名操作。

它占据`others`权限集的`x`位置

* `rwxrwxrwt`: 粘滞位已设置且目录具有可执行权限
* `rwxrwxrwT`:设置了粘滞位且该目录没有可执行权限

此功能的一个案例是 `/tmp` 目录

```
$ ls -l / | grep tmp
drwxrwxrwt  19 root root        720 Aug  8 20:55 tmp
```

在学习这些概念时，不可变文件让人感到困惑。当在文件上设置不可变标志时，作为文件的所有者不能修改或删除文件。

```
$ lsattr program.c
--------------e------- program.c
$ sudo chattr +i program.c
$ lsattr program.c
----i---------e------- program.c
$ ls -l program.c
-rw-r--r-- 1 terabyte terabyte 975 Aug  8 20:11 program.c
$ rm -rf program.c
rm: cannot remove 'program.c': Operation not permitted
$ sudo chattr -i program.c
$ lsattr program.c
--------------e------- program.c
$ ls -l program.c
-rw-r--r-- 1 terabyte terabyte 975 Aug  8 20:11 program.c
$ rm -rf program.c
$ ls -l program.c
ls: cannot access 'program.c': No such file or directory
```

## SUID 的局限性

已经看到谈论 SUID / SGID 适用于二进制文件。不能在 `shebang`脚本上设置 `suid` 并将其提升为特权。因为`shebang`告诉`Linux`内核包含第一行定义的解释器。

> `shebang`是指那些第一行以`#!`开头的脚本

一个简单的`python`脚本

```
#!/bin/env python3

import os

os.setuid(0)
os.system("/bin/bash")
```

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbw0Cpdib2hmT2JxN3JzL1HmAXF4ONoLT84zyBnhAicaZYT9FaJAVtkxwrMbtAdjia6XyEibP9tFjvKtnA/640?wx_fmt=png)

strace的日志:

```
$ strace ./program.py
execve("/usr/bin/python3", ["python3", "./program.py"], 0x7ffc627e5988 /* 91 vars */) = 0
```

因为解析器不是`SUID`，所以，即使在脚本里使用`setuid`，也是无法提权的。

其次，如果在使用 `nosuid` 选项挂载的文件系统中放置了一个 `SUID` 二进制文件，它将无效。换句话说，在运行该文件时，无法提升权限

在我的例子中，`/tmp` 目录是使用 `nosuid` 选项挂载的。也可以使用以下命令检查自己的分区

```
mount | grep nosuid | grep tmp
```

这里使用一个简单的 `C` 程序将 `uid` 设置为 0 并生成 `/bin/sh`

```
// save as shell.c
// compile: gcc -o shell shell.c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main() {
        printf("uid before: %d\n", getuid());
        printf("euid before: %d\n", geteuid());

        setuid(0);

        printf("uid after: %d\n", getuid());
        printf("euid after: %d\n", geteuid());

        system("/bin/sh");
}
```

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbw0Cpdib2hmT2JxN3JzL1HmAR8jfOm8NhGWL5JZ5JaM1ZTo9Cw8AMxU26s4epGdHmTLfx3muPh27Eg/640?wx_fmt=png)

因此，即使文件仍然归`root`用户所有，`setuid` 也是不可能的。这是 `strace` 命令的输出 (`strace -e setuid ./shell`)

```
setuid(0)    = -1 EPERM (Operation not permitted)
```

第三，当在没有使用 `nosuid` 选项安装的文件系统中的目录中启用了 `setuid` 位时，它具有许可集但不具有有效集的能力。在这种情况下，`setuid` 函数将返回 0，表明它已成功执行，但内核将由于能力检查而放弃特权。在例子中，`python` 同时设置了 `suid` 位和允许的 `cap_setuid` 功能

![](https://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbw0Cpdib2hmT2JxN3JzL1HmATSb6H6TM9mM6XqFrfYzP5PnyX21QqeYyv4deLo1ysWhT95WTtXngjQ/640?wx_fmt=png)

`setuid` 函数的执行没有失败，但是当检查 `whoami` 命令的输出时，它仍然是`terabyte`

> 关于`Linux`能力，这系列后面会提及

****请点一下右下角的“在看”，谢谢！！****

**暗号：d1320**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

奶牛安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/QXsgGBUcicbx6xrcgOW7u8WSYofSfx2y0VWAmzT5CR8RNMDIgmWTZbyepagBpxicbYUUcBrMzEHLpHRRB2bPJTeA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过