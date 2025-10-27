---
title: EV Hosting 独立开发者套餐
url: https://einverne.github.io/post/2024/03/indie-tools.html
source: Verne in GitHub
date: 2024-03-09
fetch_date: 2025-10-04T12:07:47.244100
---

# EV Hosting 独立开发者套餐

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

# EV Hosting 独立开发者套餐

Posted on 03/08/2024
, Last modified on 03/08/2024
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2024-03-08-indie-tools.md)

自从去年 [EV Hosting](https://client.einverne.info) 上线以来已经过快一周年了，过去的一年中陆陆续续推出了如下的服务。

* [共享空间](https://blog.einverne.info/post/2023/04/introducing-ev-hosting.html) 可以用来托管网站，图片，音频等等内容
* [域名注册服务](https://blog.einverne.info/post/2023/05/ev-hosting-domain-registrar.html) 可以低价注册 life, app, me 等等几十种域名后缀
* [域名邮箱服务](https://blog.einverne.info/post/2023/05/ev-hosting-shared-mail-hosting.html) 给域名提供无限域名邮箱的服务

这一些服务也是我开发独立产品的过程中不可缺少的一部分，比如说我可以在一分钟内直接创建一个[博客](https://twilight-time.einverne.info/)来发布我的播客，我可以用我自己的域名注册服务来注册我自己的 life 域名，比如[我的日本生活](https://japan.einverne.info) ，而我自己的域名邮箱服务已经稳定使用超过 3 年，过去我所有的域名邮箱全部都自己维护。

之前在 Twitter 上曾经看到过一篇 0 成本 Build 属于你自己的项目，其中列举了不少我也正在使用的服务，比如说 GitHub，Cloudflare 等等，但是问题的关键就在于当你自己的服务与这样的平台非常紧密地连接在一起的时候，未来带来的潜在风险也会伴随着平台的起伏而波动。

```
代码： @github  $0
CDN： @Cloudflare  $0
后端： @flydotio  $0
域名： @freenomofficial  $0
邮件： @Mail_Gun  $0
数据库： @PlanetScale  $0
日志： @AxiomFM  $0 [[AXIOM]]
存储： @Cloudflare R2  $0
CDN： @BunnyCDN  $0 [[Bunny CDN]]
统计： @googleanalytics  $0  [[Google Analytics]]
```

比如过了半年当再来看这一份清单的时候，就会发现 freenom 提供的免费域名被收回了，之前也曾经推荐的 [PlanetScale](https://blog.einverne.info/post/2022/08/planetscale-mysql-service.html) 将在 2024 年 4 月 8 号取消 Hobby 套餐，而 MailGun 也大幅度收窄了免费的额度。如果想要使用 PlanetScale，最低档的就是 39 USD 一个月，那如果你的应用构建于此，那必然要面临一个艰难的选择。我之前有一些自己和朋友的 21 天计划服务就放在了 PlanetScale 上，没有多少流量，所以我也不会为此付费订阅。但好在我的数据不是很多，使用 DataGrip 迁移一下就行了。并且在迁移的过程中我还发现了 PlanetScale 存在的问题，就是它并不支持 mysqldump，必需使用它专属的 cli 才能导出数据。而如果一旦服务数据量比较多，想必迁移起来就麻烦很多了。同样的，上述的所有服务虽然看起来入门是 0 USD，但其实很多服务的收费第一档就非常昂贵。

所以为什么我自己创建了 EV Hosting 的服务，也是因为来自我自己的需求，我有一些小网站需要一些邮件发送服务，比如给注册用户发送邮箱验证，比如我有一些静态或动态的网站需要托管，当然 GitHub Pages，Cloudflare Pages，Vercel，[Netlify](https://blog.einverne.info/post/2018/03/netlify-to-host-static-website.html) 等等都是非常不错的服务，托管自己的博客内容也完全没有问题，但同时也需要考虑比如 Vercel 的域名被屏蔽，GitHub Pages，Netlify 的访问速度等等问题。

首先我为了解决自己的托管和发邮件的问题，最早就是自建了 SMTP 和 Nginx 但我发现这个服务也能开放出来给有需求的用户用，然后就是域名的问题，不过域名的问题，我自己都是去 Google Domains（已被收购）和 Spaceship 上购买的，我建议大家先用 <https://tld-list.com/> 进行比价，然后根据自己的情况来选择，现在 Cloudflare 也开放了域名注册，但我还没用起来，如果有使用感受也可以一起来分享。而我提供的域名注册服务通常来说是因为拿到了批量销售的折扣，我自己也会根据具体的促销价格来选择，我自己选择注册 .life 域名其事就是我自己拿到的售卖价格只要十几块人民币一年，已经非常便宜了，所以就直接买了一个。

## 庆祝一周年

为了庆祝一周年生日，现在针对独立开发者推出如下的套餐。

[99 套餐](https://client.einverne.info/order.php?step=1&productGroup=14&product=47) 内容包括

* 2GB 独立域名邮箱 1 年
* 2GB 新加坡共享主机空间 1 年
* [域名注册九折优惠](https://client.einverne.info/order.php?step=1&productGroup=13) 一年

[199 套餐](https://client.einverne.info/order.php?step=1&productGroup=14&product=48)内容包括

* 5GB 独立域名邮箱 1 年
* 5GB 新加坡共享主机空间 1 年
* [域名注册九折优惠](https://client.einverne.info/order.php?step=1&productGroup=13) 一年

## 寻找同路人

我因为自己的需求所以维护了这样一套服务，如果你也是一位独立开发者，你也需要为你的早期项目接入邮件注册，也需要网站托管内容

如果你满足了如下的条件，欢迎[找我](https://blog.einverne.info/about.html)，提供免费一年的 99 套餐。

* 你愿意将你的项目主页地址公布到本文下方（GitHub Pull Request）
* 你愿意将 EV Hosting 以及官网链接放置到您的项目主页
* 你愿意根据使用至少贡献 2 篇关于 EV Hosting 使用相关的文章（至少 1000 字并配上至少 2 张图）并发布到[EV Hosting 帮助文档](https://docs.einverne.info/) 或者一篇您自己的使用体验包括一个链接到官网主页

Pull Request 格式

```
- [项目名字](项目地址)
```

使用的项目：

## Related Posts

* [EV Hosting 独立开发者套餐](/post/2024/03/indie-tools.html) - 03/08/2024

---

* [← Previous（前一篇）](/post/2024/03/ifast-global-bank.html "注册英国奕丰环球银行 iFast 数字银行")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2024/03/common-email-error.html "常见的邮件发送错误")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2024/03/indie-tools.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [indie 1](/tags.html#indie)
* [developer 2](/tags.html#developer)
* [development 2](/tags.html#development)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").