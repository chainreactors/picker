---
title: 存在漏洞的 PackageKit 使攻击者能够获得 root 权限
url: https://mp.weixin.qq.com/s/8DRJdSmNRz_1Rn-VxF8jqQ
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:05:22.148763
---

# 存在漏洞的 PackageKit 使攻击者能够获得 root 权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0FFY5UMlZCdiazIpYonF0JKoKn3w5ffqlagUVZKoSlphMASlVTuW7vrgmT1WJaWBrewqMPdiadUjvCQP1BU5mwLEH58llkyEq2LM/0?wx_fmt=jpeg)

# 存在漏洞的 PackageKit 使攻击者能够获得 root 权限

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0FF29bmLXtJ82yxnHYLTCvg5PKqJYbkKgFMdxTAl8F5nQuXlU0VJ0rMUj50MgedJQAmuPvLxLRouygFYU91ibfKHGYicYicvQh5hA/640?wx_fmt=png&from=appmsg)

Pack2TheRoot (CVE-2026-41651) — Linux 系统中利用PackageKit服务中的 TOCTOU 漏洞进行本地权限提升的漏洞。该服务提供了一个统一的接口，用于通过 D-Bus 安装和删除软件包，并充当用户应用程序和发行版软件包管理器（APT、RPM 等）之间的中间层。所有操作均由具有packagekitdroot 权限的服务执行。

为了与 PackageKit 交互，该漏洞利用了 GLib 库的 D-Bus API，具体来说InstallFiles()是用于安装本地 deb/rpm 软件包的方法。该方法接受一组事务标志，这些标志决定了其行为。某些标志被认为是安全的，无需完全授权即可使用。例如，该simulate标志仅执行依赖项检查，不会导致实际的软件安装。

该漏洞与已创建交易的处理有关。在初始安全检查之后，PackageKit 会将交易标记为安全，但当交易参数随后发生更改时，安全检查不会重新进行。这就造成了 TOCTOU 漏洞：使用特定标志创建的交易simulate可以更改为使用其他none标志的完整软件包安装，而 PackageKit 仍然认为授权已通过。

该 PoC 创建两个本地软件包：一个虚拟软件包和一个有效载荷软件包。前者用于通过安全检查simulate模式。后者包含一个 postinst 有效载荷，该有效载荷在上下文中执行packagekitd。在已发布的 PoC 中，该命令

```
install -m 4755 /bin/bash /tmp/.suid_bash
```

这样做会创建一个带有 SUID 权限的 bash 副本。之后，攻击者可以通过运行带有该-p参数的 bash 来获得 root 权限。

要利用此漏洞，需要通过创建两个事务g\_dbus\_connection\_call()。第一个事务调用带有标志InstallFiles()的虚拟包。第二个事务立即重用同一个事务对象，将包替换为有效载荷，并设置标志以进行完整安装。调用后，这两个操作几乎同时被添加到处理队列中。simulateg\_variant\_new("(u^as)", 4, ...) g\_variant\_new("(u^as)", 0, ...) g\_dbus\_connection\_flush\_sync()

因此，尽管仅出于安全操作的目的才获得了授权，PackageKit 仍然以 root 用户身份安装了第二个软件包。后端软件包管理器（dpkg/rpm）以 root 权限运行有效载荷软件包的 postinst/preinst 脚本。

在 Debian/Ubuntu 系统上，界面如下所示：

```
/bin/sh /var/lib/dpkg/info/<package>.postinst configure
```

关于转速系统：

```
/bin/sh /var/tmp/rpm-tmp.*
```

后渗透攻击取决于安装脚本的内容。它可能包括创建 SUID shell、修改/etc/shadow系统文件、添加 SSH 密钥、创建 systemd 单元文件、修改 PAM 配置以及其他持久化机制。

如何保护自己：

如果无法将 PackageKit 更新到已修补的版本，则通过监控 PackageKit/GLib API 调用或包管理器的进程链来检测攻击。

对于基于 Debian 的系统，一个指标可以是执行 postinst/preinst 脚本，然后/var/lib/dpkg/info/调用chmod或install设置 SUID/SGID 位。

对于基于 RPM 的系统，类似的指标是临时脚本的执行/var/tmp/rpm-tmp.\*。

监控软件包管理器调用的发起者也很有用。可疑活动可能是通过非标准软件包管理工具（apt、apt-get、dpkg、rpm、dnf、yum、zypper、mock、koji）执行的进程dpkg-deb. rpmbuild

其他 IoC 可以是 PackageKit 日志中关于身份验证失败的条目，这些条目是在漏洞利用过程中产生的：

```
May 23 13:00:00 hostname PackageKit[PID]: uid 1000 is trying to obtain org.freedesktop.packagekit.package-install-untrusted auth (only_trusted:0)

May 23 13:00:01 hostname  PackageKit[PID]: uid 1000 failed to obtain auth
```

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GgHnVEdEibr4CETet2bdkpKbeWg1bZiaesgbWJnWqNMRbKXoibKW5QDmibmbuYBqtHavcUmp5AC2NEmfqBzHqhTichzdzk9RicKn1Z8/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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