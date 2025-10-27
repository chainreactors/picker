---
title: Sieve 一个过滤邮件的语言
url: https://einverne.github.io/post/2023/04/sieve-mail-filter-languange.html
source: Verne in GitHub
date: 2023-04-13
fetch_date: 2025-10-04T11:32:54.896885
---

# Sieve 一个过滤邮件的语言

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

# Sieve 一个过滤邮件的语言

Posted on 04/12/2023
, Last modified on 04/12/2023
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2023-04-12-sieve-mail-filter-languange.md)

之前在搭建 [Mailcow](/post/2022/04/mailcow-email-server.html) 邮件服务器的时候简单的了解到了 Sieve 这个可以用来编程过滤邮件的语言。刚好现在要充分利用起 [Mailcow](https://client.einverne.info)，所以系统地学习一下 Sieve 这个邮件过滤编程语言。

## 什么是 Sieve

[Sieve](https://en.wikipedia.org/wiki/Sieve_%28mail_filtering_language%29) 是由 [RFC 5528](http://www.ietf.org/rfc/rfc5228.txt) 定义的一门专门用来处理电子邮件的语言。它被设计不仅可以用于邮件客户端的邮件过滤，也可以在邮件服务器端进行过滤。设计它的目的在于扩展性，且独立于邮件架构和操作系统。 它适合运行在不允许用户执行程序的邮件服务器上运行，例如在 IMAP 服务器上。因为 Sieve 中没有变量，没有循环，也不运行调用外部的 Shell。

## Sieve 不是什么

* Sieve 不计划独立成为一门成熟的编程语言
* Sieve 并不适用于过滤或处理除 RFC 822 消息以外的内容
* Sieve 也不打算代替现存的其他工具

## Sieve 过滤器的格式

Sieve 没有特别复杂的结构，只是包含一组命令，比如 `discard`, `if`, `fileinto` 等等

```
require ["fileinto", "reject"];

# Daffy Duck is a good friend of mine.
if address :is "from" "daffy.duck@example.com"
{
    fileinto "friends";
}

# Reject mails from the hunting enthusiasts at example.com.
if header :contains "list-id" "<duck-hunting.example.com>"
{
    reject "No violence, please";
}

# The command "keep" is executed automatically, if no other action is taken.
```

第一行脚本（require 命令）告诉 Sieve 解释器将使用可选的命令文件。然后是两个过滤规则。第一个过滤规则将所有来自 “ daffy.duck@example.com” 的邮件存储到名为“friends”的邮箱中。第二个规则拒绝头部包含字符串“”的 List-Id 字段的邮件。

如果脚本中没有匹配的条件，则应用默认操作，即隐式“保留”命令。该命令将邮件存储在默认邮箱中，通常是 INBOX。

Sieve 有两种注释写法

```
# Everything after # character will be ignored.

/* this is a bracketed (C-style) comment. */
```

和地址比较，`From:`, `To:`, `Sender:`

还有三个可选的参数可以用来比较

* `:localpart`，`@` 符号前面的部分
* `:domain`，`@` 符号后面的部分
* `:all`，全部

```
# The two test below are equivalent;
# The first variant is clearer and probably also more efficient.
if address :is :domain "to" "example.com"
{
    fileinto "examplecom";
}
if address :matches :all "to" "*@example.com"
{
    fileinto "examplecom";
}
```

一个邮件地址通常是 `"FirstName LastName" <localpart@domain>` 这样组成的。

比较 Header 中其他字段。

```
# File mails with a Spamassassin score of 4.0 or more
# into the "junk" folder.
if header :contains "x-spam-level" "****"
{
    fileinto "junk";
}
```

### 匹配类型

Sieve 提供了三种比较方法：

* `:is`，比较两个字符串完全相等
* `:contains`，是否包含
* `:matches`，使用通配符 `?` 来匹配一个未知字符，使用`*` 来匹配零个或多个未知字符

```
# Reject all messages that contain the string "viagra"in the Subject.
if header :contains "subject" "viagra"
{
    reject "go away!";
}
# Silently discard all messages sent from the tax man
elsif address :matches :domain "from" "*hmrc.gov.uk"
{
    discard;
}
```

### List of Strings

匹配列表：

```
# A mail to any of the recipients in the list of strings is filed to the folder "friends".
if address :is "from" ["daffy.duck@example.com", "porky.pig@example.com", "speedy.gonzales@example.com"]
{
    fileinto "friends";
}
```

如果要表达，from 或 sender 是某邮箱的时候，做什么

```
# Check if either the "from" or the "sender" header is from Porky.
if address :is ["from", "sender"] "porky.pig@example.com"
{
    fileinto "friends";
}
```

如果要组合表达

```
# Match "from" or the "sender" file with any of Daffy, Porky or Speedy.
if address :is ["from", "sender"] ["daffy.duck@example.com", "porky.pig@example.com", "speedy.gonzales@example.com"]
{
    fileinto "friends";
}
```

### allof, anyof

* `allof` 测试列表，如果列表中的每一个都是 true，则返回 true，逻辑上的 and
* `anyof` 测试列表，只要其中一个满足，则返回 true，逻辑上的 or

```
# This test checks against Spamassassin's header fields:
# If the spam level ls 4 or more and the Subject contains too
# many illegal characters, then silently discard the mail.
if allof (header :contains "X-Spam-Level" "****",
          header :contains "X-Spam-Report" "FROM_ILLEGAL_CHARS")
{
    discard;
}
# Discard mails that do not have a Date: or From: header field
# or mails that are sent from the marketing department at example.com.
elsif anyof (not exists ["from", "date"],
        header :contains "from" "marketing@example.com") {
    discard;
}
```

### 过滤信息大小

可以使用 `size` 来检测

```
# Delete messages greater than half a MB
if size :over 500K
{
    discard;
}
# Also delete small mails, under 1k
if size :under 1k
{
    discard;
}
```

## Example

一个简单的 Sieve 过滤器的例子是将所有来自特定发件人的邮件自动转发到另一个邮箱。下面是一个示例 Sieve 脚本：

```
if header :contains "From" "example@example.com" {
  redirect "another@example.com";
}
```

这个脚本将检查邮件的发件人是否是”example@example.com”，如果是，则将邮件重定向到”another@example.com”。

## Mailcow

在 Mailcow 中可以通过如下的路径设置 Sieve 过滤器。

```
Configuration -> Mail Setup -> Filters -> Add filter
```

另外如果有人想要创建自己的自定义域名邮箱，欢迎到 [EV Hosting](https://client.einverne.info) 订购使用。

## reference

* <http://sieve.info/>
* <https://p5r.uk/blog/2011/sieve-tutorial.html>
* <https://proton.me/support/sieve-advanced-custom-filters>

## Related Posts

* [常见的邮件发送错误](/post/2024/03/common-email-error.html) - 03/09/2024
* [端到端加密邮箱 Skiff 邮箱使用体验](/post/2023/07/skiff-mail.html) - 07/14/2023
* [Sieve 一个过滤邮件的语言](/post/2023/04/sieve-mail-filter-languange.html) - 04/12/2023
* [介绍一下新推出的 EV Hosting 网络共享托管服务](/post/2023/04/introducing-ev-hosting.html) - 04/04/2023
* [记录一下 Clientexec 中配置 SMTP 时的一些问题](/post/2023/04/clientexec-smtp-config.html) - 04/04/2023
* [使用 Mailcow 自建邮件服务器](/post/2022/04/mailcow-email-server.html) - 04/23/2022
* [电子邮件是如何工作的](/post/2022/03/how-email-send-and-receive.html) - 03/01/2022
* [邮件服务器相关概念学习](/post/2018/09/mail-server.html) - 09/05/2018

---

* [← Previous（前一篇）](/post/2023/04/raycast-ai-usage.html "Raycast AI 使用体验")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2023/04/coinpayments.html "CoinPayments 加密货币支付网关")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2023/04/sieve-mail-filter-languange.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [学习笔记 496](/categories.html#学习笔记)

* [mail 7](/tags.html#mail)
* [mailcow 5](/tags.html#mailcow)
* [sieve 1](/tags.html#sieve)
* [email 20](/tags.html#email)
* [programming-language 3](/tags.html#programming-language)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").