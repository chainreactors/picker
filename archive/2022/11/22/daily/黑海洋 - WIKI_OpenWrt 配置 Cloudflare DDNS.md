---
title: OpenWrt 配置 Cloudflare DDNS
url: https://blog.upx8.com/3110
source: 黑海洋 - WIKI
date: 2022-11-22
fetch_date: 2025-10-03T23:24:13.405553
---

# OpenWrt 配置 Cloudflare DDNS

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# OpenWrt 配置 Cloudflare DDNS

发布时间:
2022-11-21

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
31594

## 前言

Cloud­flare 作为国际知名 CDN 大厂，对于在国际互联网自由冲浪的小伙伴应该不陌生，其免费 CDN 服务是加速还是减速在曾一度是热门话题。即使不使用 CDN 服务，其 DNS 服务也是一个非常好的选择，抛开其它的不谈，仅不需要实名认证这一点来说，就比国内的厂商不知道高到哪里去了。博主的域名都是通过 Cloud­flare 进行托管解析的，所以 DDNS 也需要使用到 Cloud­flare。

## 安装 Cloudflare DDNS 组件

默认情况下 Open­Wrt 中并没有 Cloud­flare DDNS 功能，需要在编译时选择相应的组件，其位置在 `Network`→`IP Addresses and Names`。

[![](https://imgcdn.p3terx.com/post/20191029161431.png#vwid=1067&vhei=739)](https://imgcdn.p3terx.com/post/20191029161431.png#vwid=1067&vhei=739)

不懂编译也没关系，可以通过 Open­Wrt 的 Web 管理页面安装相应的软件包。

[![](https://imgcdn.p3terx.com/post/20191029161656.png#vwid=1240&vhei=705)](https://imgcdn.p3terx.com/post/20191029161656.png#vwid=1240&vhei=705)

此外还可以通过 SSH 连接到路由器，使用软件包管理器安装命令进行安装：

```
opkg update && opkg install ddns-scripts_cloudflare.com-v4
```

## 配置 Cloudflare DDNS

Cloud­flare 接管域名解析的操作相信看到这篇文章的小伙伴们都应该有所了解，所以这里就不赘述了。

* 首先进入域名的 DNS 设置页面，添加一个 A 记录，IP 地址随意，需要注意的是要关闭 CDN 选项，也就是点一下最后面的云朵图标使其变暗。[![](https://imgcdn.p3terx.com/post/20191029164224.png#vwid=1062&vhei=457)](https://imgcdn.p3terx.com/post/20191029164224.png#vwid=1062&vhei=457)

> **TIPS：** 如果是 IPv6 则是 AAAA 记录。不过根据 IPv6 网络设置的不同所需要使用的 DDNS 方案是不同的，是否在路由器中设置还要根据实际情况来决定。除非是没有公网 IPv4 地址，一般都不建议使用 IPv6 。

* [获取 API Key](https://blog.upx8.com/go/aHR0cHM6Ly9wM3RlcnguY29tL2dvL2FIUjBjSE02THk5a1lYTm9MbU5zYjNWa1pteGhjbVV1WTI5dEwzQnliMlpwYkdVdllYQnBMWFJ2YTJWdWN3) ，复制并保存好。[![](https://imgcdn.p3terx.com/post/20191102135756.png#vwid=1053&vhei=650)](https://imgcdn.p3terx.com/post/20191102135756.png#vwid=1053&vhei=650)

> **TIPS：** API Key 可以控制整个账号，为了提升安全性可以选择创建一个 API To­ken ，权限为**Zone**(区域)-**DNS**- **Edit**(编辑)即可。感兴趣的小伙伴可以自行探索，这里点到为止。（Lean 大佬的源码博主提交了相关功能的 PR ，2020 年 10 月 13 日后编译的固件才能支持 Cloud­flare API To­ken ）

* 来到 OpenWrt 的 Web 管理页面，找到`动态 DNS`，点击 IPv4 后面的`修改`按钮，或者也可以新**添加**一个。[![](https://p3terx.com/archives/openwrt-cloudflare-ddns.html)](https://imgcdn.p3terx.com/post/20191029164632.png#vwid=1356&vhei=753)
* DDNS 服务提供商选择`cloudflare.com-v4`，然后填入前面设置的域名和获取到的 API Key 以及 Cloudflare 用户名（如果使用的是 API Token ，则用户名是`Bearer`）。这里需要注意的是二级域名要使用`@`来分隔（~~写脚本的人不知道为什么傻逼的用了这个分隔符~~）。其它设置可以自由发挥，不过一般没什么需要改的。[![](https://imgcdn.p3terx.com/post/20191029165057.png#vwid=690&vhei=680)](https://imgcdn.p3terx.com/post/20191029165057.png#vwid=690&vhei=680)
* 最后`保存&应用`，等待几秒后刷新 Cloudflare 的 DNS 管理页面，应该就可以看到 IP 变更了。

> **TIPS:** Open­Wrt DDNS 管理页面中的 IP 显示会有延迟，因为要等到下一次检测时才会刷新，这个时间如果没有修改一般是 10 分钟。

[取消回复](https://blog.upx8.com/3110#respond-post-3110)

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