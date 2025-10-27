---
title: linux关闭ipv6的ra
url: https://blog.upx8.com/3779
source: 黑海洋 - WIKI
date: 2023-08-15
fetch_date: 2025-10-04T12:02:40.252259
---

# linux关闭ipv6的ra

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# linux关闭ipv6的ra

发布时间:
2023-08-14

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
16265

前两天给一台机器配置ipv6的时候出现个奇怪的问题：

刚开始能ping通，过几分钟就不行了，重启systemd-networkd后能短暂恢复，过几分钟又嗝屁，如此反复。。

找半天原因最后通过查看路由表发现问题：

[![](https://pic.7761.cf/https://lala.im/wp-content/uploads/2023/06/lala.im_2023-06-02_15-57-53.png)](https://pic.7761.cf/https%3A//lala.im/wp-content/uploads/2023/06/lala.im_2023-06-02_15-57-53.png)

图中红框的这条路由就是问题所在，通过看到proto ra可以得知这条路由是上级路由器发的ra通告。机器收到ra后systemd-networkd就会自动加上这条路由。。这个时候你手动用ip -6 route del去删是没用的，过一会又给你自动加上。。

解决办法，编辑对应网卡的networkd配置文件：

```
nano /etc/systemd/network/20-wired.network
```

在[Network]里面加上IPv6AcceptRA=no：

```
[Network]
Address=xxx.xxx.xxx.xxx/24
Address=xxx:xxx:xxx:xxx:x::x/80
IPv6AcceptRA=no
```

重启networkd：

```
systemctl restart systemd-networkd
```

如果机器没用networkd，也可以通过修改内核配置来关闭ra：

```
echo 'net.ipv6.conf.all.accept_ra = 0' >> /etc/sysctl.d/99-sysctl.conf
sysctl --system
```

[取消回复](https://blog.upx8.com/3779#respond-post-3779)

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