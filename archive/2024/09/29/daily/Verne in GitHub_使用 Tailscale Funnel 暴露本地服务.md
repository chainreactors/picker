---
title: 使用 Tailscale Funnel 暴露本地服务
url: https://blog.einverne.info/post/2024/09/tailscale-funnel.html
source: Verne in GitHub
date: 2024-09-29
fetch_date: 2025-10-06T18:22:11.231753
---

# 使用 Tailscale Funnel 暴露本地服务

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# 使用 Tailscale Funnel 暴露本地服务

Posted on 09/28/2024
, Last modified on 09/28/2024
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2024-09-28-tailscale-funnel.md)

之前我介绍过 [Tailscale](https://blog.einverne.info/post/2022/04/tailscale-usage.html)，也介绍过如何使用 [Tailscale 的出口节点功能配置流量出口](https://blog.einverne.info/post/2023/03/tailscale-exit-nodes.html)，今天再介绍一个 Tailscale 的功能 Tailscale Funnel，可以将本地服务完全地暴露在互联网上。Tailscale Funnel 允许将运行在私有 Tailnet 上的 Web 服务与公共互联网共享，提供了一种简单的方式，无需配置复杂的网络。

因为最好正好有一个需求需要接收并处理一个 Webhook，想在本地代码调试，查看 Webhook 的内容，所以想到了使用内网穿透的工具，之前其实知道 [[ngrok]]，[frp](https://blog.einverne.info/post/2017/11/frp-config.html) 这样的工具，但是配置相对比较复杂，而本地正好已经安装了 Tailscale，所以想到 Tailscale 是不是也有类似的功能，一搜果然有。Tailscale Funnel 就可以很方便地将本地服务暴露在互联网上。

Funnel 只需要一个命令就可以启动，并且自动提供 HTTPS 加密，可以随时启用或禁用公共访问。

当启用 Funnel 时，Tailscale 自动创建 DNS 记录，指向 Tailscale 全球入口服务器，这些服务器被授予对 tailnet 的有限访问权限，提供 TCP 连接。

当公共互联网用户请求服务时，Tailscale 使用安全隧道将请求转发至本地的服务器。

## 使用方法

确保本地已经安装并登录了 Tailscale 客户端。

如果本地运行的服务在端口 3000 上，那么可以使用如下的命令启用 Funnel

```
tailscale funnel 3000
```

第一次使用 Funnel 的时候会跳转到地址让用户授权。

Tailscale 会自动生成一个公共 URL

```
https://<device-name>.tailXXXXX.ts.net
```

访问该地址会直接将请求转发到本地 3000 端口。

## Related Posts

* [使用 Tailscale Funnel 暴露本地服务](/post/2024/09/tailscale-funnel.html) - 09/28/2024
* [Go 语言编写的网络穿透工具 chisel](/post/2024/03/chisel-tcp-udp-over-http.html) - 03/21/2024
* [使用 Cloudflare Tunnel 将本地服务公开到互联网](/post/2023/09/cloudflare-tunnel.html) - 09/23/2023

---

* [← Previous（前一篇）](/post/2024/09/i-bought-lazycat.html "我购买了一台懒猫微服")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2024/09/estonia-e-residency-activated-email-forward.html "爱沙尼亚电子公民身份启动及邮件转发")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2024/09/tailscale-funnel.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [tailscale 7](/tags.html#tailscale)
* [tailscale-funnel 2](/tags.html#tailscale-funnel)
* [frp 6](/tags.html#frp)
* [ngrok 2](/tags.html#ngrok)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").