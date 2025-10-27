---
title: EV Hosting 域名注册服务
url: https://einverne.github.io/post/2023/05/ev-hosting-domain-registrar.html
source: Verne in GitHub
date: 2023-05-07
fetch_date: 2025-10-04T11:36:37.831529
---

# EV Hosting 域名注册服务

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

# EV Hosting 域名注册服务

Posted on 05/06/2023
, Last modified on 05/06/2023
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2023-05-06-ev-hosting-domain-registrar.md)

[EV Hosting](https://client.einverne.info) 上线了[域名注册服务](https://client.einverne.info/order.php?step=1&productGroup=13)，现在可以在 EV Hosting 选购超过 20 种的域名后缀，包括了常见的 .com, .org, .me, .info 等，还上线了 .fun, .life, .studio, .store 等等新的顶级域名。域名的价格在不同时期会略有不同。

在目前阶段，.fun, .pw, .life, .shop, pics, .studio, 等等域名只需要 20~30 元不等就可以购买一年。但是域名的续费一般会比较贵，可以酌情考虑不同的域名后缀。EV Hosting 也会在不同时间提供最优惠的域名注册服务。

## 注册域名

请注意购买域名之前，保证自己的注册邮箱是能够接收邮件的，在注册完成之后会受到一封验证邮件，域名注册局在第一次购买时需要验证该邮箱的使用。

![qLFR](https://photo.einverne.info/images/2023/05/06/qLFR.png)

在下一个页面中进行支付。

![qaYI](https://photo.einverne.info/images/2023/05/06/qaYI.png)

完成付款之后在「我的域名」中就能看到购买的域名。

## 在 EV Hosting 后台进行 DNS 记录管理

在 EV Hosting 中，点开对应的域名，可以在侧边栏中修改 NS 名称服务器（Name Server）。

本站提供的四个名称服务器可以在[这里](https://client.einverne.info/index.php?fuse=knowledgebase&controller=articles&view=article&articleId=23) 查看（仅注册用户可见）。

![qiN4](https://photo.einverne.info/images/2023/05/06/qiN4.png)

## 将域名添加到 Cloudflare 管理

更推荐将域名添加到 Cloudflare 后台进行管理，访问 [Cloudflare](https://dash.cloudflare.com/) 后台，然后将域名添加到 Cloudflare。使用 Cloudflare 可以免费享受其提供的 CDN，还能隐藏背后服务器的 IP 地址。现在就介绍一下如何将 EV Hosting 购买的域名添加到 Cloudflare 。

首先要有一个 Cloudflare 的账号，进入账号之后，点击 「Add a site」，然后输入自己购买的域名。

![qCTW](https://photo.einverne.info/images/2023/05/06/qCTW.png)

然后再下一步中选择 Free，使用免费套餐。然后 Cloudflare 会自动对域名进行扫描，自动找到域名的 DNS 记录，点击导入。然后 Cloudflare 会给出两个 Name server 的地址，将这两个服务器配置到 EV Hosting 域名管理后台的名称服务器中。

![qEZQ](https://photo.einverne.info/images/2023/05/06/qEZQ.png)

完成配置之后，等待一段时间 NameServer 生效，点击页面中的 「Done，check nameservers」。Cloudflare 会自动检查 DNS 是否生效，如果检查通过，会发一封邮件到 Cloudflare 的邮箱中。

添加到 Cloudflare 之后就可以使用 Cloudflare 的 DNS 管理，添加 [[A 记录]], [[TXT 记录]], [[CNAME 记录]] 等等了。

## Related Posts

* [eu 顶级域名的限制和问题排查](/post/2025/09/eu-domain.html) - 09/21/2025
* [域名的生命周期](/post/2024/07/domain-lifecycle.html) - 07/02/2024
* [反查一个域名的所有子域名](/post/2023/09/subdomain-scanner.html) - 09/13/2023
* [EV Hosting 共享邮件服务](/post/2023/05/ev-hosting-shared-mail-hosting.html) - 05/20/2023
* [EV Hosting 域名注册服务](/post/2023/05/ev-hosting-domain-registrar.html) - 05/06/2023
* [介绍一下新推出的 EV Hosting 网络共享托管服务](/post/2023/04/introducing-ev-hosting.html) - 04/04/2023
* [Porkbun 免费领取一年 app wiki 等域名](/post/2023/03/porkbun-free-wiki-app-domain.html) - 03/14/2023
* [.info 域名涨价应对策略](/post/2022/10/domain-renewal-price-increase-solution.html) - 10/09/2022
* [club 域名宕机近 3 小时故障回顾](/post/2021/10/club-domain-down-accident.html) - 10/07/2021
* [每天学习一个命令：dig 查询 DNS 解析结果](/post/2017/03/dig.html) - 03/10/2017
* [使用 dnsmasq 转发 DNS 请求](/post/2014/05/dnsmasq-dns-forward.html) - 05/02/2014

---

* [← Previous（前一篇）](/post/2023/05/ansible-manage-crontab.html "使用 Ansible 管理 Crontab")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2023/05/it-tools-useful-tools.html "自建 IT tools 一系列常用工具集")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2023/05/ev-hosting-domain-registrar.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [ev-hosting 3](/tags.html#ev-hosting)
* [hosting 2](/tags.html#hosting)
* [clientexec 6](/tags.html#clientexec)
* [domain 15](/tags.html#domain)
* [domain-registry 3](/tags.html#domain-registry)
* [nameserver 1](/tags.html#nameserver)
* [dns 17](/tags.html#dns)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").