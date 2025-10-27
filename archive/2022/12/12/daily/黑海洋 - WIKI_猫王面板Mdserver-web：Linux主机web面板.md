---
title: 猫王面板Mdserver-web：Linux主机web面板
url: https://blog.upx8.com/3051
source: 黑海洋 - WIKI
date: 2022-12-12
fetch_date: 2025-10-04T01:15:07.042941
---

# 猫王面板Mdserver-web：Linux主机web面板

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Linux主机mw面板（Mdserver-web）

发布时间:
2022-12-11

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
30117

## **mdserver-web：支持Centos、Debian、Ubuntu等系统**

[![2022-10-15T15:32:20.png](https://testingcf.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/15/1665847957.png "2022-10-15T15:32:20.png")](https://testingcf.jsdelivr.net/gh/notetoday/img/usr/uploads/2022/10/15/1665847957.png "2022-10-15T15:32:20.png")

### Github地址：[https://github.com/midoks/mdserver-web](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL21pZG9rcy9tZHNlcnZlci13ZWI)

插件：[https://github.com/mw-plugin](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL213LXBsdWdpbg)

简介：简单的Linux面板,感谢BT.CN写出如此好的web管理软件。我一看到，就知道这是我一直想要的页面化管理方式。 复制了后台管理界面，按照自己想要的方式写了一版。

* SSH终端工具
* 面板收藏功能
* 网站子目录绑定
* 网站备份功能
* 插件方式管理

基本上可以使用,后续会继续优化!欢迎提供意见！

* 吹水组 - [https://t.me/mdserver\_web](https://blog.upx8.com/go/aHR0cHM6Ly90Lm1lL21kc2VydmVyX3dlYg)
* [兼容性测试报告](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL21pZG9rcy9tZHNlcnZlci13ZWIvYmxvYi9tYXN0ZXIvY29tcGF0aWJpbGl0eS5tZA)
* [常用命令说明](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL21pZG9rcy9tZHNlcnZlci13ZWIvYmxvYi9tYXN0ZXIvY21kLm1k)

### 主要插件介绍

* OpenResty - 轻量级，占有内存少，并发能力强。
* PHP[53-82] - PHP是世界上最好的编程语言。
* MySQL - 一种关系数据库管理系统。
* MariaDB - 是MySQL的一个重要分支。
* MongoDB - 一种非关系NOSQL数据库管理系统。
* phpMyAdmin - 著名Web端MySQL管理工具。
* Memcached - 一个高性能的分布式内存对象缓存系统。
* Redis - 一个高性能的KV数据库。
* PureFtpd - 一款专注于程序健壮和软件安全的免费FTP服务器软件。
* Gogs - 一款极易搭建的自助Git服务。
* Rsyncd - 通用同步服务。

### 插件开发相关

```
插件文档还不完善，如果有不明白的地方提Issue! 我会尽力完善。
如果你自己写了插件，想分享出来，也可以提Issue。
```

* 简单例子 - [https://github.com/mw-plugin/simple-plugin](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL213LXBsdWdpbi9zaW1wbGUtcGx1Z2lu)
* 插件地址 - [https://github.com/mw-plugin](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL213LXBsdWdpbg)
* 开发文档 - [https://github.com/midoks/mdserver-web/wiki/插件开发](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL21pZG9rcy9tZHNlcnZlci13ZWIvd2lraS8lRTYlOEYlOTIlRTQlQkIlQjYlRTUlQkMlODAlRTUlOEYlOTE)

# Note

```
phpMyAdmin[4.4.15]支持MySQL[5.5-5.7]
phpMyAdmin[5.2.0]支持MySQL[8.0]

PHP[53-72]支持phpMyAdmin[4.4.15]
PHP[72-81]支持phpMyAdmin[5.2.0]
```

# Docker

* 由[DDSRem](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0REU1JlbQ)开发维护。
* [https://hub.docker.com/r/ddsderek/mw-server](https://blog.upx8.com/go/aHR0cHM6Ly9odWIuZG9ja2VyLmNvbS9yL2Rkc2RlcmVrL213LXNlcnZlcg)

```
docker run -itd --name mw-server --privileged=true -p 7200:7200 -p 80:80 -p 443:443 -p 888:888 ddsderek/mw-server:latest
```

### 版本更新 0.12.2

* 开放菜单权限配置。
* 升级SSH终端2.0。
* 增加已安装类型。
* 加入切换linux软件源的命令。
* iptables安装优化。
* 网站统计POST获取数据优化。
* mysql[apt/yum]迁移优化。
* 优化防火墙导入。
* 图标可设置。
* 各种细节优化。

### JSDelivr安装地址

* 初始安装

```
curl -fsSL https://testingcf.jsdelivr.net/gh/midoks/mdserver-web@latest/scripts/install.sh | bash
```

* 直接更新

```
curl -fsSL https://testingcfcdn.jsdelivr.net/gh/midoks/mdserver-web@latest/scripts/update.sh | bash
```

* 卸载脚本

```
wget -O uninstall.sh https://testingcf.jsdelivr.net/gh/midoks/mdserver-web@latest/scripts/uninstall.sh && bash uninstall.sh
```

### 备用地址

* 初始安装

```
curl -fsSL  https://raw.githubusercontent.com/midoks/mdserver-web/master/scripts/install.sh | bash
```

* 直接更新

```
curl -fsSL  https://raw.githubusercontent.com/midoks/mdserver-web/master/scripts/update.sh | bash
```

* 卸载脚本

```
wget -O uninstall.sh https://raw.githubusercontent.com/midoks/mdserver-web/master/scripts/uninstall.sh && bash uninstall.sh
```

### 通用软件安装[命令行安装]

* 需已经安装mdserver-web

```
curl -fsSL  https://raw.githubusercontent.com/midoks/mdserver-web/dev/scripts/quick/app.sh | bash
```

### DEV使用

```
curl -fsSL  https://raw.githubusercontent.com/midoks/mdserver-web/dev/scripts/install_dev.sh | bash
curl -fsSL  https://raw.githubusercontent.com/midoks/mdserver-web/dev/scripts/update_dev.sh | bash

wget -O uninstall.sh https://raw.githubusercontent.com/midoks/mdserver-web/dev/scripts/uninstall.sh && bash uninstall.sh

curl -fsSL  https://raw.githubusercontent.com/midoks/mdserver-web/dev/scripts/quick/debug.sh | bash

curl -fsSL https://gitee.com/midoks/mdserver-web/raw/dev/scripts/install_dev.sh | bash
curl -fsSL https://gitee.com/midoks/mdserver-web/raw/dev/scripts/update_dev.sh | bash
```

##

[取消回复](https://blog.upx8.com/3051#respond-post-3051)

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