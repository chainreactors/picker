---
title: 使用 Bunny CDN 加速你的网站
url: https://einverne.github.io/post/2024/03/bunny-cdn-speed-up-your-site.html
source: Verne in GitHub
date: 2024-03-21
fetch_date: 2025-10-04T12:07:30.672117
---

# 使用 Bunny CDN 加速你的网站

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

# 使用 Bunny CDN 加速你的网站

Posted on 03/20/2024
, Last modified on 03/20/2024
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2024-03-20-bunny-cdn-speed-up-your-site.md)

前两天看到 Twitter 上有人发帖说求推荐 CDN，突然发现很多人其实不知道 Bunny CDN，虽然这一家 CDN 成立时间比较早了，但是很多人还是只知道大名鼎鼎的 Cloudflare。这里就简单的介绍一下这个 CDN 吧。

[Bunny](https://gtk.pw/bunny) 是一家成立于 2014 年的 CDN 加速服务商，提供快速、强大且价格实惠的 CDN 加速服务，总计 80Tbps+网络，连接 3000 多家 ISP 和 14 家一级传输提供商，采用顶级 AMD CPU 和 NVMe+ SSD 服务器，平均 24 毫秒延迟，并提供最先进的 DDoS 缓解安全措施，帮你的网站抵御任何攻击。

Bunny 的域名 DNS 解析服务除了基本功能还具有负载均衡、地理/延迟智能解析，还可使用编写脚本的 DNS 记录简化部署、做出智能路由决策。另外，bunny.net 还提供对象存储、网站压缩优化、在线视频存储播放等服务。

Bunny CDN 提供节点非常地多，其中亚太节点在二十多个，包括日本东京、韩国首尔、中国香港等，这些节点都是连接速度快节点。

简单注册个 Bunny.net 账号就可以获得 14 天 1TB 流量免费试用，并且还可以使用优惠码免费充值 5 美元额度！按照最低 0.01 美元/GB 的定价这 10 美元免费额度可以用 1TB CDN 流量，当然也可以用于使用 Bunny 的域名 DNS 解析、对象存储、网站压缩优化、在线视频存储播放等服务。

![5ITHy_4r4s](https://pic.einverne.info/images/5ITHy_4r4s.png)

## 功能

* 支持一键设置 SSL
* 提供 Smart Cache 功能，当站点离线也可以访问到 Bunny 节点上缓存的内容
* 兼容 S3
* 自定义访问规则，可以配置一键屏蔽某个地区
* Bunny 还提供了 WordPress 插件，

如果你也想尝试一下 Bunny 可以点击[这里](https://gtk.pw/bunny) 访问。

注册账号之后，记得在站内兑换优惠码，价值 5 刀，`BUNNYFIVER`，如果兑换码出现问题，欢迎加入[讨论群](https://t.me/%2BRUBhyY60iVcl6hdX)一起讨论。

另外还可以开 Ticket，说对 Bunny CDN 很感兴趣能不能有一个 Promo Code，这个时候客服也会非常开心地发过来一个 5 USD 的优惠码，这样就有了 10 USD 的余额，也能使用 10 个月左右了。

![q1bD4QTeqL](https://pic.einverne.info/images/q1bD4QTeqL.png)

## 设置

和大多数 CDN 的设置一样，当注册完成账号之后，可以点击页面中的 「Add Pull Zone」 创建 CDN。

![8yal25aEA8](https://pic.einverne.info/images/8yal25aEA8.png)

填入自定义的 Pull Zone Name，然后在 Origin URL 中填入需要加速的网站地址。接下来根据自己的需求选择 CDN 地区，页面上也会表明不同地区的价格。

然后绑定自定义域名，因为 Bunny 默认的域名是 xxx.b-cdn.net ，你可以根据自己的需求比如将静态资源全部设置为 asset.your-domain.com 这样，那么直接在 Add Custom Hostname 中添加自己的域名即可。

![s4Mce4eP-f](https://pic.einverne.info/images/s4Mce4eP-f.png)

添加完成之后需要配置 DNS 的 CNAME 记录，比如将 asset.your-domain.com 指向 Bunny 给出的 Hostname。等待 DNS 解析完成即可使用自己的域名来访问 CDN。

Bunny 也提供免费的 SSL 证书，到页面上一键申请即可。其他 CDN 的设置根据自己的需求进行设置即可。

## related

* [[Cloudflare]]
* [[Fastly]]
* [[CloudCone CDN]]

## Related Posts

* [使用 Bunny CDN 加速你的网站](/post/2024/03/bunny-cdn-speed-up-your-site.html) - 03/20/2024

---

* [← Previous（前一篇）](/post/2024/03/bypass-paywalls.html "绕过付费墙")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2024/03/chisel-tcp-udp-over-http.html "Go 语言编写的网络穿透工具 chisel")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2024/03/bunny-cdn-speed-up-your-site.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [产品体验 185](/categories.html#产品体验)

* [bunny-cdn 1](/tags.html#bunny-cdn)
* [cdn 3](/tags.html#cdn)
* [cloudflare 8](/tags.html#cloudflare)
* [fastly 1](/tags.html#fastly)
* [cloudfront 1](/tags.html#cloudfront)
* [website 16](/tags.html#website)
* [网站优化 1](/tags.html#网站优化)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").