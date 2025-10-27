---
title: linux设置默认网关，网关ip不在同一子网
url: https://blog.upx8.com/3780
source: 黑海洋 - WIKI
date: 2023-08-15
fetch_date: 2025-10-04T12:02:39.971524
---

# linux设置默认网关，网关ip不在同一子网

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# linux设置默认网关，网关ip不在同一子网

发布时间:
2023-08-14

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
15802

还是那台机器又碰到个网络问题，机器默认的网关ip不在同一个网段，

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/06/lala.im_2023-06-02_21-46-57.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/06/lala.im_2023-06-02_21-46-57.png)

以往添加默认网关使用下面这个命令即可：

```
ip route add default via 148.251.xxx.xxx dev eth0
```

但是对于这种网关不在同一网段的情况会报错，解决办法是使用onlink：

```
ip route add default via 148.251.xxx.xxx dev eth0 onlink
```

机器用的systemd-networkd，编辑对应的网卡配置文件：

```
nano /etc/systemd/network/20-wired.network
```

增加一个[Route]然后在里面配置网关地址并使用GatewayOnLink=yes：

```
[Match]
Name=eth0

[Network]
Address=5.9.xxx.xxx/24
Address=xxx:xxx:xxx:xxx:x::x/80
IPv6AcceptRA=no

[Route]
Gateway=148.251.xxx.xxx
GatewayOnLink=yes

[Route]
Gateway=xxx:xxx:xxx:xxx:x::x
GatewayOnLink=yes
```

重启networkd：

```
systemctl restart systemd-networkd
```

[取消回复](https://blog.upx8.com/3780#respond-post-3780)

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