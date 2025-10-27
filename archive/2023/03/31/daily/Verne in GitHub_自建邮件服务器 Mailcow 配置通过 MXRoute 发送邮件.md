---
title: 自建邮件服务器 Mailcow 配置通过 MXRoute 发送邮件
url: https://einverne.github.io/post/2023/03/mailcow-relaying-through-mxroute.html
source: Verne in GitHub
date: 2023-03-31
fetch_date: 2025-10-04T11:13:22.365419
---

# 自建邮件服务器 Mailcow 配置通过 MXRoute 发送邮件

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

# 自建邮件服务器 Mailcow 配置通过 MXRoute 发送邮件

Posted on 03/30/2023
, Last modified on 03/30/2023
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2023-03-30-mailcow-relaying-through-mxroute.md)

之前写过一篇文章是[如何使用 Mailcow 自架邮件服务器](/post/2022/04/mailcow-email-server.html)，自那个时候开始以及使用自己架设的邮件服务器快一年左右的时间了，因为是自己使用，收件是没有什么问题，发件的话用 mail-tester.com 测试也能拿 10 分，但一直是没有作为主力发件服务器去使用的，主要还是怕会进入垃圾箱。但是最近看到 [[MXRoute]] 有[春季打折](/post/2023/03/mxroute-usage.html)，15 美元一年 25 GB 空间，就订购了一个想试试看。

有了这两个前提之后，我就像能不能让我的收件通过 Mailcow，邮件直接到我的服务器，然后发件的时候通过 MXRoute 发送，毕竟 MXRoute 的发件 IP 地址要比我自己的服务器 IP 地址要可信得多，送达率可能也比我自己的服务器要高。然后我简单地了解了一下发现 Mailcow 是自带 Relay (邮件中继服务) 功能的。

那这一篇文章就讲讲怎么在 Mailcow 中配置使用 MXRoute 来发送邮件。

## 初始 Mailcow 配置

在 Mailcow 中首先要完成正常的域名添加，然后再新增 Mailbox 邮箱。因为这个部分比较简单，直接在 Mailcow 后台操作，然后根据 Mailcow 后台的 DNS 配置，修改域名对应的 MX 记录，SPF 记录，DKIM 记录，DMARC 记录即可。

假如我想要配置一个博客评论的邮箱，比如 `no-reply@blog.einverne.info`，那么首先要在 Mailcow 后台添加 `blog.einverne.info` 的域名，然后配置如下的 DNS 记录。

![ON6L](https://photo.einverne.info/images/2023/03/30/ON6L.png)

然后在 Mailbox 中添加 `no-reply@blog.einverne.info` 的邮箱。此时使用 Mailcow 的后台也是可以对此邮箱进行发件和收件的。但这个时候走的都是此服务器。

## MXRoute 配置

首先完成[MXRoute 的基础配置](/post/2023/03/mxroute-usage.html)，当然这个地方需要注意的是必需要好好理解一下几个 DNS 记录的作用，不要完全照着 MXRoute 发过来的配置直接修改。

首先也需要在 MXRoute 后台添加域名 `blog.einvenre.info`，然后新增一个邮箱 `no-reply@blog.einverne.info`，

Configure the account as a catchall for the domain. In cPanel, this is under Forwarders / Aliases → Add Domain Forwarder. Not sure where it is in DirectAdmin as I don’t have any DirectAdmin accounts to test with. The reason it needs to be a catchall is so it can be used to send mail from any address at the domain.

然后下面重要的部分配置就需要注意了。

* 首先把域名的 MX 记录设置成自己的邮件服务器的地址，MX 记录指向自己的邮件服务器地址
* 然后修改域名的 [[SPF]] 记录，同时授权自己的邮件服务器 IP 和 MXRoute 的 IP
* 最后同时添加 Mailcow 的 DKIM 和 MXRoute 的 DKIM 记录

假如自己的 Mailcow 邮件服务器的 IP 地址是 198.52.100.1， IPv6 的地址是 2001:db8::1，那么配置可以像如下这样：

```
v=spf1 ip4:198.52.100.1 ip6:2001:db8::1 include:mxroute.com -all
```

如果不清楚 [SPF 记录](/post/2022/03/how-email-send-and-receive.html) 是什么，可以参考之前的[文章](/post/2022/03/how-email-send-and-receive.html)，解释了邮件是如何工作的。

或者，如果不想在 SPF 记录中直接使用 IP 地址，也可以使用 `mx` 来代替配置具体的 IP 地址，不过需要注意的是需要配置额外的 MX 记录（指向一个域名或 IP），如果配置的 MX 记录是域名，那么还需要注意配置 A 记录将域名解析到邮件服务器。如果配置 MX 域名，那么可能会产生一次额外的 DNS 查询，不过个人是推荐这么做的，因为邮件服务器的 IP 地址更换了，只需要修改域名的 A 记录值就可以了。

```
v=spf1 a mx include:mxroute.com ~all
```

最后为了让邮件送达率更高，还需要配置 [[DKIM]]，在 DNS 记录中需要同时配置 Mailcow 和 MXRoute 的 DKIM 记录。

一般情况下 DKIM 记录 key 是

```
dkim._domainkey.example.com
```

值就是网站提供的类似:

```
v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC...
```

这里可以看到的是 DKIM 记录的 key，Mailcow 一般是

```
dkim._domainkey.example.com
```

而 MXRoute 一般是

```
x._domainkey.example.com
```

同时把这两个记录添加到 DNS 记录中。

完成上面的 DNS 配置之后就可以进入 Mailcow 后台配置了。

### Mailcow 配置邮件中继

在 Mailcow 后台，点击 System -> Configuration (顶部菜单) → Routing 标签。

![OPn3](https://photo.einverne.info/images/2023/03/30/OPn3.png)

然后找到页面中的 「Add sender-dependent transport」

![O8KY](https://photo.einverne.info/images/2023/03/30/O8KY.png)

然后在这个地方添加 MXRoute Host，邮箱的用户名和密码。

添加完成之后，可以点击 「test」进行测试。输入自己邮箱的地址，然后保留 To Address 地址为默认的 `null@hosted.mailcow.de` 然后保证测试的结果中得到了 250 OK 。

![O3Gp](https://photo.einverne.info/images/2023/03/30/O3Gp.png)

然后在顶部菜单 E-Mail -> Configuration -> Domains，找到对应的域名，点击 Edit。

![OJRN](https://photo.einverne.info/images/2023/03/30/OJRN.png)

在编辑界面中找到「Sender-dependent transports」，在下拉菜单中选择刚刚配置的 Relay 邮箱。

现在任何通过 Webmail 或者邮件客户端通过此域名发送的邮件都是通过 MXRoute 来发送的。

上面的功能演示的是在 Mailcow 中配置邮件中继，但是这个功能底层还是依赖的 Postfix 的标准功能 `sender_dependent_relayhost_maps` ，所以用户可以在其他程序比如 Mail-in-a-box 等等中进行相同的配置，或者用户也可以手动直接修改 Postfix 配置。

## reference

* <https://lowendtalk.com/discussion/178881/self-hosted-mailcow-relaying-through-mxroute/p1>

## Related Posts

* [NameCrane 邮件托管服务体验：超大存储空间的终身邮箱解决方案](/post/2025/05/namecrane-business-email-provider.html) - 05/21/2025
* [CrossBox 使用记录](/post/2023/04/crossbox-review.html) - 04/29/2023
* [自建邮件服务器 Mailcow 配置通过 MXRoute 发送邮件](/post/2023/03/mailcow-relaying-through-mxroute.html) - 03/30/2023
* [邮件发送服务 MXRoute 使用体验](/post/2023/03/mxroute-usage.html) - 03/25/2023
* [使用 Mailcow 自建邮件服务器](/post/2022/04/mailcow-email-server.html) - 04/23/2022

---

* [← Previous（前一篇）](/post/2023/03/clientexec-installation.html "ClientExec 安装及入门使用")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2023/03/chatwoot-open-source-customer-engagement.html "Chatwoot 开源的客户支持工具：在网站上加上聊天对话框")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2023/03/mailcow-relaying-through-mxroute.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [mxroute 3](/tags.html#mxroute)
* [mailcow 5](/tags.html#mailcow)
* [email-server 7](/tags.html#email-server)
* [email-hosting 7](/tags.html#email-hosting)
* [sendmail 2](/tags.html#sendmail)
* [postfix 1](/tags.html#postfix)
* [mailu 2](/tags.html#mailu)
* [email-template 2](/tags.html#email-template)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").