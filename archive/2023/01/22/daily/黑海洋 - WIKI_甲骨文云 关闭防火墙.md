---
title: 甲骨文云 关闭防火墙
url: https://blog.upx8.com/3195
source: 黑海洋 - WIKI
date: 2023-01-22
fetch_date: 2025-10-04T04:33:37.803634
---

# 甲骨文云 关闭防火墙

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 甲骨文云 关闭防火墙

发布时间:
2023-01-21

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
21112

## 彻底删除防火墙

甲骨文云提供的系统镜像开启了系统防火墙，为了方便使用通常会先关闭防火墙。

命令如下：

```
# centos
yum remove iptables* netfilter-persistent* -y

# ubuntu
apt autoremove iptables* netfilter-persistent* -y
```

## 放行所有端口

如何直接删除iptables会导致某些服务无法使用，例如CF的一键脚本等无法获取到ipv4的ip，因此更建议使用下面的方式。

命令如下：

```
# ubuntu
apt-get purge netfilter-persistent
apt autoremove netfilter-persistent* -y
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -F
```

#强制删除

```
rm -rf /etc/iptables && reboot
```

[取消回复](https://blog.upx8.com/3195#respond-post-3195)

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