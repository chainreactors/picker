---
title: 在光猫/软路由上使用 Cloudflare 的动态域名
url: https://blog.upx8.com/3631
source: 黑海洋 - WIKI
date: 2023-06-11
fetch_date: 2025-10-04T11:46:04.883350
---

# 在光猫/软路由上使用 Cloudflare 的动态域名

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 在光猫/软路由上使用 Cloudflare 的动态域名

发布时间:
2023-06-10

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
30107

相信很多小伙伴对于动态域名已经很熟悉了，大多数光猫/路由器也都内置了 DDNS 功能。但是在使用过程中，好像总是有点掣肘，例如一些早期的光猫/路由器提供的 DDNS 功能只支持更新 IPv4 地址，由于移动宽带只提供公网的 IPv6 公网地址，DDNS 功能会无法使用。因此在两年前，我就写了两段简单的 DDNS 更新脚本，使用 [DnsPod.cn](https://blog.upx8.com/go/aHR0cHM6Ly9naXN0LmdpdGh1Yi5jb20vaGlpZmVuZy9lZDExYzU1MjdjM2Y1NWY1YzVmZGMyMGUzYmQxOWRhZA) 或 [dynv6.com](https://blog.upx8.com/go/aHR0cHM6Ly9naXN0LmdpdGh1Yi5jb20vaGlpZmVuZy8wYWZjMTg5YmI3OWIzYTZjYzIzOWQ0NWFmM2VjNmRiZQ) 动态域名完成 IPv4&IPv6 地址的更新。

现在看来，使用 DnsPod.cn 或 dynv6.com 动态域名仍然有一些不完美的地方，由于三大运营商都关闭了家庭宽带的 80 & 443 端口，如果想利用家庭宽带搭建一个 Blog ，或者将自己群晖里的内容分享给其他朋友使用时，总要在网址后面带上端口才可以访问。如果使用 Cloudflare.com 的动态域名，另外配合 [Cloudflare Origin Rules](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuaGljYWlyby5jb20vcG9zdC81Ny5odG1s) 功能，即可完美解决上述问题。

**一、获取域名的 Zone ID 和 API 令牌**

1、登录 Cloudflare.com ，点击域名，我以 ifeng.xyz 这个域名为例。

[![1-DDNS-ZoneID-1.webp](//blog.upx8.com/usr/uploads/auto_save_image/e0c3835a2fc5b204eb3639c4e015c1b6.webp "1-DDNS-ZoneID-1.webp")](https://blog.upx8.com/go/Ly9ibG9nLnVweDguY29tL3Vzci91cGxvYWRzL2F1dG9fc2F2ZV9pbWFnZS9lMGMzODM1YTJmYzViMjA0ZWIzNjM5YzRlMDE1YzFiNi53ZWJw)2、Copy 页面右下角的“区域 ID” （ Cloudflare\_Zone\_ID ）备用，然后点击“获取您的 API 令牌” （ Cloudflare\_API\_Tokens ） 。

[![2-DDNS-ZoneID-2.webp](//blog.upx8.com/usr/uploads/auto_save_image/d0557c0bea1e73afb5f1bf8363c33ce4.webp "2-DDNS-ZoneID-2.webp")](https://blog.upx8.com/go/Ly9ibG9nLnVweDguY29tL3Vzci91cGxvYWRzL2F1dG9fc2F2ZV9pbWFnZS9kMDU1N2MwYmVhMWU3M2FmYjVmMWJmODM2M2MzM2NlNC53ZWJw)3、点击“创建令牌”。

[![3-DDNS-Token-1.webp](//blog.upx8.com/usr/uploads/auto_save_image/a4adfe4133a4d54cd7e9dda0304293cd.webp "3-DDNS-Token-1.webp")](https://blog.upx8.com/go/Ly9ibG9nLnVweDguY29tL3Vzci91cGxvYWRzL2F1dG9fc2F2ZV9pbWFnZS9hNGFkZmU0MTMzYTRkNTRjZDdlOWRkYTAzMDQyOTNjZC53ZWJw)4、将页面拉到底部，点击“创建自定义令牌”。

[![4-DDNS-Token-2.webp](//blog.upx8.com/usr/uploads/auto_save_image/82fed67cfd04d6d35ded6e5f87f28e44.webp "4-DDNS-Token-2.webp")](https://blog.upx8.com/go/Ly9ibG9nLnVweDguY29tL3Vzci91cGxvYWRzL2F1dG9fc2F2ZV9pbWFnZS84MmZlZDY3Y2ZkMDRkNmQzNWRlZDZlNWY4N2YyOGU0NC53ZWJw)5、如下图所示填入令牌名称，例如我填入了“dynamic”；权限选择 “区域” -> “DNS” ->“编辑” ；区域资源选择 “包含” -> “特定域名” ->“自己的域名（例如我选择 ifeng.xyz ）” ，最后点击页面底部的“继续以显示摘要”。

[![5-DDNS-Token-3.webp](//blog.upx8.com/usr/uploads/auto_save_image/558afd94edf0a8cb21654e214ab1abc7.webp "5-DDNS-Token-3.webp")](https://blog.upx8.com/go/Ly9ibG9nLnVweDguY29tL3Vzci91cGxvYWRzL2F1dG9fc2F2ZV9pbWFnZS81NThhZmQ5NGVkZjBhOGNiMjE2NTRlMjE0YWIxYWJjNy53ZWJw)6、点击“创建令牌”。

[![6-DDNS-Token-4.webp](//blog.upx8.com/usr/uploads/auto_save_image/f187501764883a8bb89bc2cd2378462e.webp "6-DDNS-Token-4.webp")](https://blog.upx8.com/go/Ly9ibG9nLnVweDguY29tL3Vzci91cGxvYWRzL2F1dG9fc2F2ZV9pbWFnZS9mMTg3NTAxNzY0ODgzYThiYjg5YmMyY2QyMzc4NDYyZS53ZWJw)7、Copy “API 令牌” （ Cloudflare\_API\_Tokens ）备用 。

[![7-DDNS-Token-5.webp](//blog.upx8.com/usr/uploads/auto_save_image/2ce28981bad358e98813e9a2260319e4.webp "7-DDNS-Token-5.webp")](https://blog.upx8.com/go/Ly9ibG9nLnVweDguY29tL3Vzci91cGxvYWRzL2F1dG9fc2F2ZV9pbWFnZS8yY2UyODk4MWJhZDM1OGU5ODgxM2U5YTIyNjAzMTllNC53ZWJw)**二、登录光猫/软路由安装 DDNS 更新脚本**

ddns\_update.sh 脚本中有关 Cloudflare 域名记录更新的代码为 update\_IP 函数中 24 行代码，其他代码主要用于获取光猫/软路由的公网 IPv4/IPv6 地址，同时检测 IP 地址是否发生变化，然后调用 update\_IP 函数更新。如果对于特定的光猫/软路由，代码会写的更简单一些，例如使用类似“ip -6 addr list scope global pppoe | grep -v " fd" | sed -n 's/.\*inet6 \([0-9a-f:]\+\).\*/\1/p' | head -n 1”这样的命令来获取本机的 IPv6 地址，但是不同品牌的光猫/路由器由于固件版本不同，在建立 pppoe 链接后 interface 名称有所区别，为了脚本的通用性，这种方法不能使用，因此代码中的处理逻辑相对来说更复杂一点。当然，你可以根据自己光猫/路由器的情况自行修改代码，让代码更加简单高效。例如可以使用 /etc/ppp/ipv6-up 来启动脚本，来减少循环检测 IP 地址是否发生变化对系统资源的占用。

1、下载并安装 DDNS 更新脚本，以 EdgeMAX EdgeRouter ER-X 路由器为例。

项目地址：[https://github.com/hiifeng/Dynamic-DNS-using-Cloudflare](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2hpaWZlbmcvRHluYW1pYy1ETlMtdXNpbmctQ2xvdWRmbGFyZQ)

在上述地址下载 ddns\_update.sh ，使用 WinSCP 等 ftp 工具将脚本上传到 /usr/local/ 目录中。

2、使用 ssh 登录光猫/软路由

Bash

```
# 切换到 root 用户
sudo -i
# 增加可执行属性
chmod a+x /usr/local/ddns_update.sh
# 修改 ddns_update.sh 文件中的相关参数，其中包含 Cloudflare_Zone_ID 、Cloudflare_API_Tokens 和你需要解析的域名（例如：ddns.ifeng.xyz）
sed -i "s/type in zoneID/此处填入上面获取的Cloudflare_Zone_ID/g" /usr/local/ddns_update.sh
sed -i "s/type in token/此处填入上面获取的Cloudflare_API_Tokens/g" /usr/local/ddns_update.sh
sed -i "s/ddns.example.com/你的域名/g" /usr/local/ddns_update.sh
# 修改操作系统 /etc/rc.local 文件,当光猫/软路由开机或重启时，自动执行 ddns_update.sh
sed -i 's/^exit 0$/bash \/usr\/local\/ddns_update.sh\n\nexit 0/' /etc/rc.local
```

BASH

3、重启光猫/软路由使其生效。

**三、注意事项**

Cloudflare API 不支持对 .cf, .ga, .gq, .ml, .tk 域名的更新。

[取消回复](https://blog.upx8.com/3631#respond-post-3631)

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