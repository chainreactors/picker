---
title: 在光猫/软路由上使用 Cloudflare 的动态域名
url: https://buaq.net/go-168150.html
source: unSafe.sh - 不安全
date: 2023-06-11
fetch_date: 2025-10-04T11:44:49.047077
---

# 在光猫/软路由上使用 Cloudflare 的动态域名

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/5d782416926a33619e766fb81f1349c2.jpg)

在光猫/软路由上使用 Cloudflare 的动态域名

相信很多小伙伴对于动态域名已经很熟悉了，大多数光猫/路由器也都内置了 DDNS 功能。但是在使用过程中，好像总是有点掣肘，例如一些早期的光猫/路由器提供
*2023-6-10 13:36:0
Author: [blog.upx8.com(查看原文)](/jump-168150.htm)
阅读量:57
收藏*

---

相信很多小伙伴对于动态域名已经很熟悉了，大多数光猫/路由器也都内置了 DDNS 功能。但是在使用过程中，好像总是有点掣肘，例如一些早期的光猫/路由器提供的 DDNS 功能只支持更新 IPv4 地址，由于移动宽带只提供公网的 IPv6 公网地址，DDNS 功能会无法使用。因此在两年前，我就写了两段简单的 DDNS 更新脚本，使用 [DnsPod.cn](https://gist.github.com/hiifeng/ed11c5527c3f55f5c5fdc20e3bd19dad) 或 [dynv6.com](https://gist.github.com/hiifeng/0afc189bb79b3a6cc239d45af3ec6dbe) 动态域名完成 IPv4&IPv6 地址的更新。

现在看来，使用 DnsPod.cn 或 dynv6.com 动态域名仍然有一些不完美的地方，由于三大运营商都关闭了家庭宽带的 80 & 443 端口，如果想利用家庭宽带搭建一个 Blog ，或者将自己群晖里的内容分享给其他朋友使用时，总要在网址后面带上端口才可以访问。如果使用 Cloudflare.com 的动态域名，另外配合 [Cloudflare Origin Rules](https://www.hicairo.com/post/57.html) 功能，即可完美解决上述问题。

**一、获取域名的 Zone ID 和 API 令牌**

1、登录 Cloudflare.com ，点击域名，我以 ifeng.xyz 这个域名为例。

[![1-DDNS-ZoneID-1.webp](https://blog.upx8.com/usr/uploads/auto_save_image/e0c3835a2fc5b204eb3639c4e015c1b6.webp "1-DDNS-ZoneID-1.webp")](https://blog.upx8.com/usr/uploads/auto_save_image/e0c3835a2fc5b204eb3639c4e015c1b6.webp)2、Copy 页面右下角的“区域 ID” （ Cloudflare\_Zone\_ID ）备用，然后点击“获取您的 API 令牌” （ Cloudflare\_API\_Tokens ） 。

[![2-DDNS-ZoneID-2.webp](https://www.foxhup.com/usr/uploads/auto_save_image/2a3c8700fd1b0fdc0c85f666729b883d.webp "2-DDNS-ZoneID-2.webp")](https://blog.upx8.com/usr/uploads/auto_save_image/d0557c0bea1e73afb5f1bf8363c33ce4.webp)3、点击“创建令牌”。

[![3-DDNS-Token-1.webp](https://www.foxhup.com/usr/uploads/auto_save_image/8362a425febb780e4d98434bdb573f55.webp "3-DDNS-Token-1.webp")](https://blog.upx8.com/usr/uploads/auto_save_image/a4adfe4133a4d54cd7e9dda0304293cd.webp)4、将页面拉到底部，点击“创建自定义令牌”。

[![4-DDNS-Token-2.webp](https://www.foxhup.com/usr/uploads/auto_save_image/2089aa3e96f09f96f938ccc8949a25fd.webp "4-DDNS-Token-2.webp")](https://blog.upx8.com/usr/uploads/auto_save_image/82fed67cfd04d6d35ded6e5f87f28e44.webp)5、如下图所示填入令牌名称，例如我填入了“dynamic”；权限选择 “区域” -> “DNS” ->“编辑” ；区域资源选择 “包含” -> “特定域名” ->“自己的域名（例如我选择 ifeng.xyz ）” ，最后点击页面底部的“继续以显示摘要”。

[![5-DDNS-Token-3.webp](https://www.foxhup.com/usr/uploads/auto_save_image/12600fd6fb0f6f4e0e018477750ee1af.webp "5-DDNS-Token-3.webp")](https://blog.upx8.com/usr/uploads/auto_save_image/558afd94edf0a8cb21654e214ab1abc7.webp)6、点击“创建令牌”。

[![6-DDNS-Token-4.webp](https://www.foxhup.com/usr/uploads/auto_save_image/dd503cf0c72844025ba994f501c96102.webp "6-DDNS-Token-4.webp")](https://blog.upx8.com/usr/uploads/auto_save_image/f187501764883a8bb89bc2cd2378462e.webp)7、Copy “API 令牌” （ Cloudflare\_API\_Tokens ）备用 。

[![7-DDNS-Token-5.webp](https://www.foxhup.com/usr/uploads/auto_save_image/ffbee390b1687dc9263cf757f98bd1a9.webp "7-DDNS-Token-5.webp")](https://blog.upx8.com/usr/uploads/auto_save_image/2ce28981bad358e98813e9a2260319e4.webp)**二、登录光猫/软路由安装 DDNS 更新脚本**

ddns\_update.sh 脚本中有关 Cloudflare 域名记录更新的代码为 update\_IP 函数中 24 行代码，其他代码主要用于获取光猫/软路由的公网 IPv4/IPv6 地址，同时检测 IP 地址是否发生变化，然后调用 update\_IP 函数更新。如果对于特定的光猫/软路由，代码会写的更简单一些，例如使用类似“ip -6 addr list scope global pppoe | grep -v " fd" | sed -n 's/.\*inet6 \([0-9a-f:]\+\).\*/\1/p' | head -n 1”这样的命令来获取本机的 IPv6 地址，但是不同品牌的光猫/路由器由于固件版本不同，在建立 pppoe 链接后 interface 名称有所区别，为了脚本的通用性，这种方法不能使用，因此代码中的处理逻辑相对来说更复杂一点。当然，你可以根据自己光猫/路由器的情况自行修改代码，让代码更加简单高效。例如可以使用 /etc/ppp/ipv6-up 来启动脚本，来减少循环检测 IP 地址是否发生变化对系统资源的占用。

1、下载并安装 DDNS 更新脚本，以 EdgeMAX EdgeRouter ER-X 路由器为例。

项目地址：<https://github.com/hiifeng/Dynamic-DNS-using-Cloudflare>

在上述地址下载 ddns\_update.sh ，使用 WinSCP 等 ftp 工具将脚本上传到 /usr/local/ 目录中。

2、使用 ssh 登录光猫/软路由

3、重启光猫/软路由使其生效。

**三、注意事项**

Cloudflare API 不支持对 .cf, .ga, .gq, .ml, .tk 域名的更新。

文章来源: https://blog.upx8.com/3631
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)