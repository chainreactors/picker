---
title: 防止根据IP查域名，防止源站IP泄露
url: https://blog.upx8.com/3242
source: 黑海洋 - WIKI
date: 2023-02-25
fetch_date: 2025-10-04T08:04:33.984101
---

# 防止根据IP查域名，防止源站IP泄露

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 防止根据IP查域名，防止源站IP泄露

发布时间:
2023-02-24

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
13101

有的人设置了禁止IP访问网站，但是别人用https://ip的形式，会跳到你服务器所绑定的一个域名网站上。

> 直接通过https://IP,访问网站，会出现“您的连接不是私密连接”，然后点高级，会出现“继续前往IP”，然后点击后会跳到你服务器上的一个域名网站！

[![](https://chenyu.me/usr/uploads/2022/09/2393397162.webp)](https://blog.upx8.com/go/aHR0cHM6Ly9jaGVueXUubWUvdXNyL3VwbG9hZHMvMjAyMi8wOS8yMzkzMzk3MTYyLndlYnA)

[![](https://chenyu.me/usr/uploads/2022/09/3860491208.webp)](https://blog.upx8.com/go/aHR0cHM6Ly9jaGVueXUubWUvdXNyL3VwbG9hZHMvMjAyMi8wOS8zODYwNDkxMjA4LndlYnA)

为了防止上面这种情况，所以继续看：

## 新建站点

网站——添加站点——域名随便写一个不存在的，如：ha.haha——PHP版本：纯静态，配置里添加 `return 444;` 。
[![](https://chenyu.me/usr/uploads/2020/12/2988949531.jpg)](https://chenyu.me/usr/uploads/2020/12/2988949531.jpg)

## 设置默认站点

默认站点设置为上面所建的一个假域名网站ha.haha

## 禁止IP访问网站

#### 一般方法

就是上面新建站点时的 `return 444;` 设置，一定要设置。
禁止IP访问网站，防止服务器被恶意解析

#### 进阶方法

ClientHello 中是带着 SNI 的，所以其实握手阶段是可以知道访问的域名是否合法的，NGINX 1.19.4 中添加了一个新的配置项 `ssl_reject_handshake` 用于拒绝握手，也就不会提供证书。

使用方法也很简单，将原本默认配置中的 `return 444` 替换成 `ssl_reject_handshake on` 即可。

1. server {
2. listen 443 default\_server;
3. server\_name \_;
4. include conf.d/ssl.config;
6. # 不用返回 444 了，直接拒绝握手
7. ssl\_reject\_handshake on;
8. # return 444;
9. }

配置后，再尝试 IP 访问，会发现浏览器报了 ERR\_SSL\_UNRECOGNIZED\_NAME\_ALERT 的错误，也看不到证书信息。

## 套用假证书

通过自签名证书，自签一个假的证书（假域名，假信息），然后套在上面假的域名网站上。
创建自签名SSL证书

到此完成。
[![](https://chenyu.me/usr/uploads/2022/09/4153275866.webp)](https://blog.upx8.com/go/aHR0cHM6Ly9jaGVueXUubWUvdXNyL3VwbG9hZHMvMjAyMi8wOS80MTUzMjc1ODY2LndlYnA)

此时通过https://IP,访问网站，会出现“您的连接不是私密连接”，然后点高级，会出现“继续前往IP”，然后会出现“ERR\_HTTP2\_PROTOCOL\_ERROR”错误，无法访问此网站提示！

[取消回复](https://blog.upx8.com/3242#respond-post-3242)

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