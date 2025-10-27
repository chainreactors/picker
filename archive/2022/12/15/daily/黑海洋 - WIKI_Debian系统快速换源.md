---
title: Debian系统快速换源
url: https://blog.upx8.com/3151
source: 黑海洋 - WIKI
date: 2022-12-15
fetch_date: 2025-10-04T01:32:48.635057
---

# Debian系统快速换源

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Debian系统快速换源

发布时间:
2022-12-14

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
14899

## 前言

在购买服务器（VPS）后，一些商家的预装系统经常会出现各种软件和依赖包不能正常安装，这基本都是源引起的，进行更换源后即可正常。

## 备份源配置

为了减少不必要的麻烦，先执行以下命令将源文件进行备份

`mv /etc/apt/sources.list /etc/apt/sources.list.bak`

## 更换为其他源

在下列的标签里选择一个你想换的源，复制命令在ssh执行即可

官方源

> cat > /etc/apt/sources.list << EOF
> deb http://deb.debian.org/debian/ bullseye main contrib non-free
> deb-src http://deb.debian.org/debian/ bullseye main contrib non-free
> deb http://deb.debian.org/debian/ bullseye-updates main contrib non-free
> deb-src http://deb.debian.org/debian/ bullseye-updates main contrib non-free
> deb http://deb.debian.org/debian/ bullseye-backports main contrib non-free
> deb-src http://deb.debian.org/debian/ bullseye-backports main contrib non-free
> deb http://deb.debian.org/debian-security/ bullseye-security main contrib non-free
> deb-src http://deb.debian.org/debian-security/ bullseye-security main contrib non-free
> EOF

腾讯云内网源

> cat > /etc/apt/sources.list << EOF
> deb http://mirrors.tencentyun.com/debian/ bullseye main contrib non-free
> deb-src http://mirrors.tencentyun.com/debian/ bullseye main contrib non-free
> deb http://mirrors.tencentyun.com/debian/ bullseye-updates main contrib non-free
> deb-src http://mirrors.tencentyun.com/debian/ bullseye-updates main contrib non-free
> deb http://mirrors.tencentyun.com/debian/ bullseye-backports main contrib non-free
> deb-src http://mirrors.tencentyun.com/debian/ bullseye-backports main contrib non-free
> deb http://mirrors.tencentyun.com/debian-security/ bullseye-security main contrib non-free
> deb-src http://mirrors.tencentyun.com/debian-security/ bullseye-security main contrib non-free
> EOF

阿里云内网源

> cat > /etc/apt/sources.list << EOF
> deb http://mirrors.cloud.aliyuncs.com/debian/ bullseye main contrib non-free
> deb-src http://mirrors.cloud.aliyuncs.com/debian/ bullseye main contrib non-free
> deb http://mirrors.cloud.aliyuncs.com/debian/ bullseye-updates main contrib non-free
> deb-src http://mirrors.cloud.aliyuncs.com/debian/ bullseye-updates main contrib non-free
> deb http://mirrors.cloud.aliyuncs.com/debian/ bullseye-backports main contrib non-free
> deb-src http://mirrors.cloud.aliyuncs.com/debian/ bullseye-backports main contrib non-free
> deb http://mirrors.cloud.aliyuncs.com/debian-security/ bullseye-security main contrib non-free
> deb-src http://mirrors.cloud.aliyuncs.com/debian-security/ bullseye-security main contrib non-free
> EOF

Linode源

> cat > /etc/apt/sources.list << EOF
> deb http://mirrors.linode.com/debian/ bullseye main contrib non-free
> deb-src http://mirrors.linode.com/debian/ bullseye main contrib non-free
> deb http://mirrors.linode.com/debian/ bullseye-updates main contrib non-free
> deb-src http://mirrors.linode.com/debian/ bullseye-updates main contrib non-free
> deb http://mirrors.linode.com/debian/ bullseye-backports main contrib non-free
> deb-src http://mirrors.linode.com/debian/ bullseye-backports main contrib non-free
> deb http://mirrors.linode.com/debian-security/ bullseye-security main contrib non-free
> deb-src http://mirrors.linode.com/debian-security/ bullseye-security main contrib non-free
> EOF

## 更新系统索引

在换源后还需要执行以下命令代码，更新系统索引，让新源生效。

`apt update`

[取消回复](https://blog.upx8.com/3151#respond-post-3151)

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