---
title: ubuntu优先使用ipv4，但不禁用ipv6
url: https://blog.upx8.com/3244
source: 黑海洋 - WIKI
date: 2023-02-25
fetch_date: 2025-10-04T08:04:33.677396
---

# ubuntu优先使用ipv4，但不禁用ipv6

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux系统IPv4/IPv6双栈网络下配置IPv4优先的办法

发布时间:
2023-02-24

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
27665

博主的很多VPS都是双栈网络，系统默认会以 IPv6 优先，只有 IPv6 无法访问的时候才会尝试访问 IPv4。日常使用中这个倒不会有什么影响，但最近因为一些特定用途，需要让 IPv4 被优先识别。当然，我们可以使用一些命令或现成的脚本直接禁掉 IPv6 也能达到这个效果，但这不是我的目的。于是就找了一些资料，对系统进行修改最终实现保持双栈网络的前提下让 IPv4 优先于 IPv6。这里记录一下，也方便有同需求的博友。

Linux 系统下，有一个 `/etc/gai.conf` 文件。默认情况下，它会使用 IPv6 优先，如果您安装了 curl 并且本地支持 IPv6，那么可以使用 `curl ip.sb` 测试

**复制

```
root@debian:~# curl ip.sb
2001:db8::2

# 效果等同于：curl ip.sb -6
```

如果你不想使用 IPv6 优先，可以在这个文件中找到

**复制

```
#precedence ::ffff:0:0/96  100
```

取消掉注释，修改为

**复制

```
precedence ::ffff:0:0/96  100
```

一句话命令：

**复制

```
sed -i 's/#precedence ::ffff:0:0\/96  100/precedence ::ffff:0:0\/96  100/' /etc/gai.conf
```

此时再使用 `curl ip.sb` 测试

**复制

```
root@debian:~# curl ip.sb
192.0.2.2

# 效果等同于：curl ip.sb -4
```

如此也就完成了 IPv4 的优先配置。

Centos 中如果没有这个文件，自己新建一个，然后写入 `precedence ::ffff:0:0/96 100` 即可。

##### 这里也顺带也说一下：如何禁用 IPv6

修改 `/etc/sysctl.conf` 文件，首先找到你的网卡名（以 `eth0` 为例），然后加入如下内容

**复制

```
net.ipv6.conf.all.autoconf = 0
net.ipv6.conf.default.autoconf = 0
net.ipv6.conf.all.accept_ra = 0
net.ipv6.conf.default.accept_ra = 0
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
net.ipv6.conf.eth0.disable_ipv6 = 1
```

如果需要其他网卡则更改或添加 `net.ipv6.conf.eth0.disable_ipv6 = 1` 即可。

一句话命令：

**复制

```
cat >> /etc/sysctl.conf << EOF
net.ipv6.conf.all.autoconf = 0
net.ipv6.conf.default.autoconf = 0
net.ipv6.conf.all.accept_ra = 0
net.ipv6.conf.default.accept_ra = 0
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
net.ipv6.conf.eth0.disable_ipv6 = 1
EOF
```

注意 `cat` 命令后的 `>>` 即为添加文件内容，如果使用 `>` 则是覆盖文件内容。

然后使用 `sysctl -p` 来重新加载配置文件，此时查看 `ip a` 就可以发现 IPv6 已经被禁止了。

```

```

[取消回复](https://blog.upx8.com/3244#respond-post-3244)

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