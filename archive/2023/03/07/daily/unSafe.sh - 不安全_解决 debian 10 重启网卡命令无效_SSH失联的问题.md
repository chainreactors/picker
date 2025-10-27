---
title: 解决 debian 10 重启网卡命令无效/SSH失联的问题
url: https://buaq.net/go-152247.html
source: unSafe.sh - 不安全
date: 2023-03-07
fetch_date: 2025-10-04T08:47:23.795595
---

# 解决 debian 10 重启网卡命令无效/SSH失联的问题

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

解决 debian 10 重启网卡命令无效/SSH失联的问题

这种问题通常出现在自己 DD 系统之后，原因在于 DD 后系统的网卡名被改变。服务商处的 debian 原生系统的默认网卡名基本都是 eth0 ，我们在
*2023-3-6 21:49:0
Author: [blog.upx8.com(查看原文)](/jump-152247.htm)
阅读量:42
收藏*

---

这种问题通常出现在自己 DD 系统之后，原因在于 DD 后系统的网卡名被改变。

服务商处的 debian 原生系统的默认网卡名基本都是 eth0 ，我们在自己 DD 系统之后网卡名会变为 ens3 之类的。那么要彻底解决这个问题，就是将 DD 后的网卡名恢复。步骤也很简单：

#### **1、编辑GRUB文件**

**复制

```
vi /etc/default/grub

找到 GRUB_CMDLINE_LINUX="" 这一行，将其修改为 GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0" ，然后保存退出
```

#### 2、编辑网络配置文件：

说明：进行这一步时不要无脑照搬执行。首先通过`ip a`命令查看自己网卡名是 ens3 还是其他的。下面的命令或修改操作中涉及到的 ens3 需替换为你自己的网卡名。

**复制

```
sed -i 's/ens3/eth0/g' /etc/network/interfaces

或者是
vi /etc/network/interfaces
进去后将所有 ens3 修改为 eth0 ，然后保存退出
```

#### 3、更新Grub并重启VPS

**至此，我们就完成了网卡名的恢复。**

重启后，可以使用`ip a`命令，即可发现之前的网卡名已经变为了 eth0 。此时执行重启网卡命令也是能够正常连接的。

**复制

```
sudo service networking restart
或
sudo /etc/init.d/networking restart
```

**最后补充一点：**如果是重启失联了，我们就只能通过商家后台的 VNC 进去修改。所以，博主建议大家在自己DD完系统之后，就按照以上步骤恢复为默认网卡名。另外，一些小厂提供的 debian 系统默认网卡名会有所变化，大家根据以上步骤恢复为它本身的网卡名即可。

文章来源: https://blog.upx8.com/3252
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)