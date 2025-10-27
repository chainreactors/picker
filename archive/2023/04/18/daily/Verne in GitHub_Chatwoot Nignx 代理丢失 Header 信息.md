---
title: Chatwoot Nignx 代理丢失 Header 信息
url: https://einverne.github.io/post/2023/04/chatwoot-nginx-header-underscore.html
source: Verne in GitHub
date: 2023-04-18
fetch_date: 2025-10-04T11:31:24.370475
---

# Chatwoot Nignx 代理丢失 Header 信息

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

# Chatwoot Nignx 代理丢失 Header 信息

Posted on 04/17/2023
, Last modified on 04/17/2023
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2023-04-17-chatwoot-nginx-header-underscore.md)

之前的一篇[文章](/post/2023/03/chatwoot-open-source-customer-engagement.html)介绍过如何使用 Docker 自建 [[Chatwoot]]，但是最近调用 API 的时候总是发现问题。在调用最普通的接口的时候，按照要求在 Header 中传了 `api_access_token`，但是接口返回 401 或者是

```
{"errors":["You need to sign in or sign up before continuing."]}
```

简单的查询了一下之后，发现问题出现在 Nginx 上，Nginx 默认情况下不允许带下划线的 Header，所以当请求到 Nginx，然后转发到后台 Chatwoot 的时候这个 `api_access_token` 就丢了。所以一直出现 401 和需要登录的状况。

解决办法非常容易，在 Nginx 的配置 `server` 块中增加如下的配置

```
underscores_in_headers on;
```

然后 Nginx 配置 reload 即可，因为我使用 [[HestiaCP]] 控制面板，所以后台修改一下配置模板即可。

## reference

* <https://www.chatwoot.com/docs/self-hosted/deployment/caprover#api-requests-failing-with-you-need-to-sign-in-or-sign-up-before-continuing>

## Related Posts

* [Chatwoot Nignx 代理丢失 Header 信息](/post/2023/04/chatwoot-nginx-header-underscore.html) - 04/17/2023

---

* [← Previous（前一篇）](/post/2023/04/proxmox-install-ubuntu-server-22-04.html "Proxmox VE 安装 Ubuntu Server 22.04")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2023/04/installing-ioncube-loader-with-hestiacp.html "在 Hestia CP 的 VPS 上安装 ionCube Loader")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2023/04/chatwoot-nginx-header-underscore.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [chatwoot 3](/tags.html#chatwoot)
* [online-business 3](/tags.html#online-business)
* [self-hosted 32](/tags.html#self-hosted)
* [nginx 16](/tags.html#nginx)
* [http-header 1](/tags.html#http-header)
* [http-request 2](/tags.html#http-request)
* [postman 2](/tags.html#postman)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").