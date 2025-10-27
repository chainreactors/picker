---
title: 介绍一下新推出的 EV Hosting 网络共享托管服务
url: https://einverne.github.io/post/2023/04/introducing-ev-hosting.html
source: Verne in GitHub
date: 2023-04-05
fetch_date: 2025-10-04T11:30:23.672963
---

# 介绍一下新推出的 EV Hosting 网络共享托管服务

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

# 介绍一下新推出的 EV Hosting 网络共享托管服务

Posted on 04/04/2023
, Last modified on 04/04/2023
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2023-04-04-introducing-ev-hosting.md)

因为自己之前买过一些 VPS，但是一直空闲很多，所以想着是否能够充分利用起来。最近正好看到可以免费使用 [[Clientexec]] 管理 Web Hosting 账单，所以隆重介绍一下刚刚推出的新服务 [EV Hosting](https://client.einverne.info/)，目前上线了两个功能，共享网站托管服务和自定义域名邮箱服务。

## 新加坡 共享网站托管服务

共享网站托管服务（Shared Web Hosting） 是一种网站托管服务，是将多个网站存储在同一台服务器上，并共享服务器上的 CPU、内存和带宽。这种类型的托管服务通常是最便宜和最受欢迎的选择，特别适合个人和小型企业。

如果你是一个不懂技术的个人但想在网络上有一片属于自己的空间，或者你想以最低的成本开展在线商城，欢迎来订购使用。

本站提供的托管服务，服务器位于新加坡，CPU 是 AMD Ryzen 9 3900X 12-Core Processor，服务器共 128 GB 内存。

![ev hosting sg](https://photo.einverne.info/images/2023/04/08/sll3.jpg)

### 一键安装超过 400 种应用

目前该服务托管于新加坡的服务器，使用 [[DirectAdmin]] 面板，装有 [[Softaculous]]，可以一键安装包括 [[WordPress]]，[[Joomla]]，[[NextCloud]]，[[Tiny Tiny RSS]]，[[miniflux]]，[[FreshRSS]]，[[phpmyadmin]] 等等超过 450 种的应用程序[1](#fn:1)，不少的应用我之前也是介绍过的，并且还一直在用，比如 [[NextCloud]] 这个文件同步工具，[[miniflux]] 这个 在线的 RSS 阅读器。Softaculout 非常强大，很多功能和特性有待你去发现。

DirectAdmin 后台也有一个在线的文件管理器，可以直接基于网页对网站内容进行管理。

![nrWr](https://photo.einverne.info/images/2023/04/04/nrWr.png)

### 自定义域名邮箱

另外订购所有的套餐都可以在后台配置自定义邮箱，每一个邮箱每个小时可以发送至多 200 封邮件。请不要滥用发件发送恶意、垃圾邮件。

也可以使用后台提供的 Roundcube 网络邮箱界面来管理自己的邮件。

### MySQL 数据库

购买套餐之后可以在后台创建响应的 MySQL 数据库供应用程序保存数据使用。所有的数据库内容及网站内容都会定期通过备份来保证安全。

### 附加功能

可以通过附加功能，来设置 Node.js，PHP，Python 等应用程序。

![neId](https://photo.einverne.info/images/2023/04/04/neId.png)

为了庆祝上线，在订购所有年付套餐的时候输入 `EVHOSTING` 则可以享受 5 折的优惠（优惠截止 4 月末）。最低可以以 8 元购买一年 Bronze 套餐(限量 10 个，如果看到界面显示优惠券代码无效则表示优惠码用完或已经过期)。

## 加利福尼亚 网络优化 共享空间

加利福尼亚的共享空间是大陆网络优化空间，到大陆的网络延迟非常文档。

![ev hosting us](https://photo.einverne.info/images/2023/04/08/sokY.png)

## 自定义域名邮箱服务

如果你只需要发送邮件的服务，那么也可以订购这个自定义域名邮箱的服务，订购服务之后需要我手工启用，后台使用的是 Mailcow，我再添加了域名之后会给你的邮箱发送相应管理后台的信息。

所有在线购买的产品都可以通过在线提交工单的方式获得支持，并且后续会陆陆续续更新更多相关的使用技巧，欢迎关注。另外服务刚刚上线，如果有任何使用的问题，反馈并且到的验证的都可以免费获取一年的 Bronze 套餐。

1. <https://www.softaculous.com/software/> [↩](#fnref:1)

## Related Posts

* [EV Hosting 域名注册服务](/post/2023/05/ev-hosting-domain-registrar.html) - 05/06/2023
* [Sieve 一个过滤邮件的语言](/post/2023/04/sieve-mail-filter-languange.html) - 04/12/2023
* [介绍一下新推出的 EV Hosting 网络共享托管服务](/post/2023/04/introducing-ev-hosting.html) - 04/04/2023
* [记录一下 Clientexec 中配置 SMTP 时的一些问题](/post/2023/04/clientexec-smtp-config.html) - 04/04/2023
* [ClientExec 安装及入门使用](/post/2023/03/clientexec-installation.html) - 03/29/2023
* [使用 Mailcow 自建邮件服务器](/post/2022/04/mailcow-email-server.html) - 04/23/2022

---

* [← Previous（前一篇）](/post/2023/04/clientexec-smtp-config.html "记录一下 Clientexec 中配置 SMTP 时的一些问题")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2023/04/langchain.html "LangChain 是什么")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2023/04/introducing-ev-hosting.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [产品体验 185](/categories.html#产品体验)

* [hosting 2](/tags.html#hosting)
* [email 20](/tags.html#email)
* [mailcow 5](/tags.html#mailcow)
* [clientexec 6](/tags.html#clientexec)
* [online-business 3](/tags.html#online-business)
* [vps 31](/tags.html#vps)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").