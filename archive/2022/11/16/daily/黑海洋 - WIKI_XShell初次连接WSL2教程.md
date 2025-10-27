---
title: XShell初次连接WSL2教程
url: https://blog.upx8.com/3090
source: 黑海洋 - WIKI
date: 2022-11-16
fetch_date: 2025-10-03T22:53:17.349090
---

# XShell初次连接WSL2教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# XShell初次连接WSL2教程

发布时间:
2022-11-15

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
14305

1、先删ssh，再安装ssh

sudo apt-get remove --purge openssh-server ## 先删ssh
sudo apt-get install openssh-server ## 在安装ssh
sudo rm /etc/ssh/ssh\_config ## 删配置文件，让ssh服务自己想办法链接
sudo service ssh --full-restart

2、修改配置文件

sudo vim /etc/ssh/sshd\_config
Port 6666
ListenAddress 0.0.0.0
PasswordAuthentication yes
3、重启ssh（每次重启wsl都要执行该语句）

sudo service ssh --full-restart
4、重新生成host key

sudo dpkg-reconfigure openssh-serve
5、连接XShell

[取消回复](https://blog.upx8.com/3090#respond-post-3090)

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