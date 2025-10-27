---
title: Cloudflare 加速解析
url: https://blog.upx8.com/3142
source: 黑海洋 - WIKI
date: 2022-12-11
fetch_date: 2025-10-04T01:12:33.373013
---

# Cloudflare 加速解析

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# CloudFlare 非标准端口转发映射

发布时间:
2022-12-10

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
20080

### 简单介绍

Cloudflare除了支持80/443端口外，还支持一些其他的端口转发HTTP/HTTPS的流量。
不过需要注意的是，需要开启CDN小黄云才能使用，如果您仅仅用于DNS，那么你的访问都是直接访问源站的。

### 映射转发方式

默认情况下Cloudflare的映射为全端口映射，即如果你源站使用的是8443非标准端口，使用Cloudflare服务后，访问的网址后面还需要带8443。
示例：
Cloudflare节点8080端口 映射到源站8080端口 只支持HTTP协议
Cloudflare节点8443端口 映射到源站8443端口 只支持HTTPS协议

### HTTP 端口

80
8080
8880
2052
2082
2086
2095

### HTTPS 端口

443
2053
2083
2087
2096
8443

### 例外情况

对于启用了中国网络的域名的中国境内 HTTP/HTTPS 流量
Cloudflare Apps
进行 Cloudflare 缓存
以上服务仅可以使用端口 80 和 443

### 阻止转发

对于 Pro 及更高级别的计划，您可以使用 WAF 规则 ID 100015 阻止非 80 和 443 端口上的流量："Block requests to all ports except 80 and 443".

[取消回复](https://blog.upx8.com/3142#respond-post-3142)

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