---
title: Linux 更新内核至最新版
url: https://blog.upx8.com/3294
source: 黑海洋 - WIKI
date: 2023-03-19
fetch_date: 2025-10-04T10:02:53.166393
---

# Linux 更新内核至最新版

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux 更新内核至最新版

发布时间:
2023-03-18

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
14280

首先声明一下为什么要更新linux内核版本：

每一个idc服务商都采用的不是最新的源，但会是最稳定的源，我们更新内核版本就和更新病毒库一样，更新一下最好，不想更新的也无所谓，毕竟idc服务商会及时更上

教程开始：

1、查看当前内核版本以及更新内核

```
# uname -r
# yum -y install kernel
```

2、重启

```
#  reboot
```

3、查看是否启动新内核

```
# uname -r
```

4、查看内核列表

```
# rpm -q kernel
```

5、删除旧内核节省空间（对照旧内核名称删除，请小心不要把启动的内核删除了）

```
# sudo rpm -e kernel-2.6.32-504.30.3.el6.x86_64
```

6、更新所有软件源

```
# yum -y update
```

7、环境依赖组件必不可少64位系统先执行：

```
# yum install openssl098e glibc.i686 libstdc++.i686 -y
# yum localinstall
```

8、执行两行命令

```
# ln -s /usr/lib/libssl.so /usr/lib/libssl.so.6
# ln -s /usr/lib/libcrypto.so /usr/lib/libcrypto.so.6
```

9、依赖包的安装

```
# yum -y install gcc gcc-c++ autoconf libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel zlib zlib-devel glibc glibc-devel glib2 glib2-devel bzip2 bzip2-devel ncurses ncurses-devel curl curl-devel e2fsprogs e2fsprogs-devel krb5-devel libidn libidn-devel openssl openssl-devel nss_ldap openldap openldap-devel  openldap-clients openldap-servers libxslt-devel libevent-devel ntp  libtool-ltdl bison libtool vim-enhanced
```

```
# yum y install vim*
```

10、重启

```
# reboot
```

**教程结束，请注意更新内核请保证是新****服务器****，更新内核会有丢失文件风险！**

[取消回复](https://blog.upx8.com/3294#respond-post-3294)

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