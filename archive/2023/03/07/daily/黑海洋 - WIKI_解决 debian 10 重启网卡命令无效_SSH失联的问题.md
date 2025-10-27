---
title: 解决 debian 10 重启网卡命令无效/SSH失联的问题
url: https://blog.upx8.com/3252
source: 黑海洋 - WIKI
date: 2023-03-07
fetch_date: 2025-10-04T08:49:19.216127
---

# 解决 debian 10 重启网卡命令无效/SSH失联的问题

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 解决 debian 10 重启网卡命令无效/SSH失联的问题

发布时间:
2023-03-06

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
19063

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

**复制

```
update-grub

reboot
```

**至此，我们就完成了网卡名的恢复。**

重启后，可以使用`ip a`命令，即可发现之前的网卡名已经变为了 eth0 。此时执行重启网卡命令也是能够正常连接的。

**复制

```
sudo service networking restart
或
sudo /etc/init.d/networking restart
```

**最后补充一点：**如果是重启失联了，我们就只能通过商家后台的 VNC 进去修改。所以，博主建议大家在自己DD完系统之后，就按照以上步骤恢复为默认网卡名。另外，一些小厂提供的 debian 系统默认网卡名会有所变化，大家根据以上步骤恢复为它本身的网卡名即可。

[取消回复](https://blog.upx8.com/3252#respond-post-3252)

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