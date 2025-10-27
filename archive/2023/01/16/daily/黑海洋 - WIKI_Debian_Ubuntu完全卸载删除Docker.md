---
title: Debian/Ubuntu完全卸载删除Docker
url: https://blog.upx8.com/3189
source: 黑海洋 - WIKI
date: 2023-01-16
fetch_date: 2025-10-04T03:59:49.617595
---

# Debian/Ubuntu完全卸载删除Docker

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Debian/Ubuntu完全卸载删除Docker

发布时间:
2023-01-15

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
34093

卸载Docker，同时删除Docker镜像、容器、数据卷等文件。

Docker自17.03版本开始分为两个版本Docker CE和Docker EE：

* Docker CE：Docker Community Edition，即Docker社区版
* Docker EE：即Docker Enterprise Edition，即Docker企业版。

卸载Docker的命令如下：

|  |
| --- |
| ``` # 卸载Docker CE sudo apt-get purge docker-ce # 卸载Docker EE sudo apt-get purge docker-ee # 删除Docker镜像、容器、数据卷等文件 sudo rm -rf /var/lib/docker ``` |

在完成这些操作之后，运行以下命令检查系统中是否还存在docker文件：

```
sudo find / -name '*docker*'
```

可能仍然存在一些docker文件。这个时候，你可以执行一下删除方式，再次进行卸载。

删除安装时自动安装的所有包

```
sudo apt-get autoremove docker docker-ce docker-engine docker.io containerd runc
```

查看删除docker其他有没有没有卸载干净的包

```
dpkg -l | grep docker
```

卸载相应的包

```
sudo apt-get autoremove docker-ce-*
```

删除docker的相关配置&目录

```
sudo rm -rf /etc/systemd/system/docker.service.d
sudo rm -rf /var/lib/docker
sudo rm /etc/apparmor.d/docker
sudo groupdel docker
sudo rm -rf /var/run/docker.sock
```

确定docker卸载完毕

```
docker --version
```

确定docker卸载完毕

最后可以再执行一遍检查：

```
sudo find / -name "*docker*" -exec `rm -rf` {} +
```

删除所有相关文件即可。

1. ![nex](https://gravatar.loli.net/avatar/avatar/640faf93228afe30cd031c7dc3fd3c09?s=32&r=&d=)

   **nex**

   2023-03-18 10:15:08

   [回复](https://blog.upx8.com/3189/comment-page-1?replyTo=26989#respond-post-3189)

   很棒，非常感谢！

[取消回复](https://blog.upx8.com/3189#respond-post-3189)

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