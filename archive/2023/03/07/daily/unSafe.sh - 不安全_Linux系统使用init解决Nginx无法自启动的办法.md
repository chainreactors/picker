---
title: Linux系统使用init解决Nginx无法自启动的办法
url: https://buaq.net/go-152246.html
source: unSafe.sh - 不安全
date: 2023-03-07
fetch_date: 2025-10-04T08:47:23.086101
---

# Linux系统使用init解决Nginx无法自启动的办法

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

Linux系统使用init解决Nginx无法自启动的办法

最近遇到服务器重启后Nginx无法自启，必须开机后手动启动，也懒得排查问题在哪，直接添加开机自启动服务。虽然 Systemd 用来启动守护进程，已经成为
*2023-3-6 21:49:5
Author: [blog.upx8.com(查看原文)](/jump-152246.htm)
阅读量:17
收藏*

---

最近遇到服务器重启后Nginx无法自启，必须开机后手动启动，也懒得排查问题在哪，直接添加开机自启动服务。

虽然 `Systemd` 用来启动守护进程，已经成为现在Linux系统的标准配置。但是为了这么一句Nginx的启动命令就写一个系统服务实在有点麻烦。这时 `init` 就显得更容易了。

对于现在发行的Linux系统已经不再有 `/etc/rc.local` 文件，但 `rc.local` 服务却还是自带的：

**复制

```
[email protected] ~ # cat /lib/systemd/system/rc-local.service
#  SPDX-License-Identifier: LGPL-2.1-or-later
#
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.

# This unit gets pulled automatically into multi-user.target by
# systemd-rc-local-generator if /etc/rc.local is executable.
[Unit]
Description=/etc/rc.local Compatibility
Documentation=man:systemd-rc-local-generator(8)
ConditionFileIsExecutable=/etc/rc.local
After=network.target

[Service]
Type=forking
ExecStart=/etc/rc.local start
TimeoutSec=0
RemainAfterExit=yes
GuessMainPID=no
```

默认情况下这个服务还是关闭的状态：

**复制

```
[email protected] ~ # systemctl status rc-local
● rc-local.service - /etc/rc.local Compatibility
     Loaded: loaded (/lib/systemd/system/rc-local.service; static)
    Drop-In: /usr/lib/systemd/system/rc-local.service.d
             └─debian.conf
     Active: inactive (dead)
       Docs: man:systemd-rc-local-generator(8)
```

于是，在这里我们需要手工添加一个 `/etc/rc.local` 文件：

**复制

```
cat <<EOF >/etc/rc.local
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

exit 0
EOF
```

然后赋予权限：

**复制

```
chmod +x /etc/rc.local
```

接着启动 `rc-local` 服务：

**复制

```
systemctl enable --now rc-local
```

此时可能会弹出警告：

**复制

```
The unit files have no installation config (WantedBy=, RequiredBy=, Also=,
Alias= settings in the [Install] section, and DefaultInstance= for template
units). This means they are not meant to be enabled using systemctl.

Possible reasons for having this kind of units are:
• A unit may be statically enabled by being symlinked from another unit's
  .wants/ or .requires/ directory.
• A unit's purpose may be to act as a helper for some other unit which has
  a requirement dependency on it.
• A unit may be started when needed via activation (socket, path, timer,
  D-Bus, udev, scripted systemctl call, ...).
• In case of template units, the unit is meant to be enabled with some
  instance name specified.
```

无视警告，因为这个服务没有任何依赖的系统服务，只是开机启动 `/etc/rc.local` 脚本而已。

再次查看状态：

**复制

```
[email protected] ~ # systemctl status rc-local
● rc-local.service - /etc/rc.local Compatibility
     Loaded: loaded (/lib/systemd/system/rc-local.service; static)
    Drop-In: /usr/lib/systemd/system/rc-local.service.d
             └─debian.conf
     Active: inactive (dead)
       Docs: man:systemd-rc-local-generator(8)
```

然后我们把下面的Nginx开机启动命令添加到 `/etc/rc.local` 文件中 `exit 0` 前面即可。

**复制

```
/etc/init.d/nginx start
```

如果你有别的需要开机启动的命令、脚本，都可以添加在这里。之后尝试重启就会发现已经生效了。

如果是参数较多或是较为复杂的需要开机启动的服务，这里还是建议你使用 `Systemd` 。因为 `init` 是串行启动，前一个进程启动完才会启动下一个进程。如果太过复杂的服务，就会导致开机启动变慢。

文章来源: https://blog.upx8.com/3251
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)