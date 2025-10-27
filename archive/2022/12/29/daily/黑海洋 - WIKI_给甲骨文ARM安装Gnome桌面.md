---
title: 给甲骨文ARM安装Gnome桌面
url: https://blog.upx8.com/3160
source: 黑海洋 - WIKI
date: 2022-12-29
fetch_date: 2025-10-04T02:40:27.471881
---

# 给甲骨文ARM安装Gnome桌面

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 给甲骨文ARM安装Gnome桌面

发布时间:
2022-12-28

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
20569

甲骨文ARM最高配置4核24G，这个配置安装和桌面端没有任何压力，还相当于多了一个远程电脑，今天我们来试试吧。

# 准备工作

1、甲骨文ARM，推荐2核以上；
2、建议系统使用ubuntu20.04；
3、推荐DD系统

```
bash <(wget --no-check-certificate -qO- 'https://moeclub.org/attachment/LinuxShell/InstallNET.sh') -u 20.04 -v 64 -a -firmware -p ****
```

上面的*\**\*请请替换成自己的密码哦

# 开始安装

首先是设置语言环境：

```
dpkg-reconfigure locales
```

Ubuntu

Copy

这里分为两步，第一步选择`zh_CN GB2312`，按空格键确认，再按Tab键切换到“OK”上，按回车确认。第二步选择`zh_CN`，完成语言配置。

1、更新系统

```
apt update -y ; apt upgrade -y
```

2、安装桌面

```
apt install ubuntu-desktop
```

> 安装桌面这个过程比较慢，2核12G耗时6分钟

3、安装xrdp

```
apt install xrdp -y
```

3、添加用户、重启Xrdp、开机启动

```
adduser xrdp ssl-cert
systemctl restart xrdp
systemctl status xrdp
```

# 如何连接

我使用的是Remote，Windows使用远程桌面也可以。但是请注意，推荐使用16位色，否则不够流畅。

新建连接 IP:3389，用户名和密码是vps的登陆密码如：root，*\**\*

首次连接需要简单设置，默认即可。

最后还需要修改一下默认配置，否则Lock之后ROOT登陆不上去。

```
vi /etc/pam.d/gdm-autologin
#注释 "auth requied pam_succeed_if.so user != root quiet success"

vi /etc/pam.d/gdm-password
#注释行 "auth requied pam_succeed_if.so user != root quiet success"
```

相关：[https://qing.su/article/oneclick-desktop.html](https://blog.upx8.com/go/aHR0cHM6Ly9xaW5nLnN1L2FydGljbGUvb25lY2xpY2stZGVza3RvcC5odG1s)

相关Gnome桌面安装：<https://blog.upx8.com/3211>

[取消回复](https://blog.upx8.com/3160#respond-post-3160)

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