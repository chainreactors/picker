---
title: 记录一下 Clientexec 中配置 SMTP 时的一些问题
url: https://einverne.github.io/post/2023/04/clientexec-smtp-config.html
source: Verne in GitHub
date: 2023-04-05
fetch_date: 2025-10-04T11:30:23.055039
---

# 记录一下 Clientexec 中配置 SMTP 时的一些问题

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

# 记录一下 Clientexec 中配置 SMTP 时的一些问题

Posted on 04/04/2023
, Last modified on 04/05/2023
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2023-04-04-clientexec-smtp-config.md)

本文记录一下在配置 Clientexec 中的 SMTP 发送邮件的时候遇到的一些错误。添加了 [[mailcow]] 的 SMTP 配置，但是测试发送邮件总是报如下的错误。

## 验证 SMTP 配置

> SMTP Error: The following recipients failed: email-test@clientexec.com: : Sender address rejected: not owned by user admin@mailcow.email

这就非常奇怪， 为了验证我的 SMTP 配置是没有问题的，我还直接写了一段 Python 发送邮件的程序，邮件是可以正常的发送出去的。所以我把怀疑点移动到了 Clientexec 面板。开始怀疑是不是 [[Clientexec]] 在 SMTP 配置的地方有什么 BUG。

Python

```
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, recipient_email, subject, body, smtp_server,
smtp_port, username, password):
    # Create a message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Add the body of the message as a MIMEText object
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the message
    with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(sender_email, recipient_email, message.as_string())

sender_email = ''
recipient_email = ''
subject = 'Test Email'
body = 'This is a test email sent from Python!'
smtp_server = ''
smtp_port = 587
username = ''
password = ''

if __name__ == '__main__':
    send_email(sender_email, recipient_email, subject, body, smtp_server,
    smtp_port, username, password)
```

## 验证 Clientexec 后台 SMTP 设置

为了验证 Clientexec 后台的 SMTP 设置是可以正常工作的，我看到官方的文档上提供了 Gmail SMTP 设置的说明，所以我直接用之前的 Gmail 的 SMTP 设置，在 Clientexec 后台配置了一下。测试是可以正常发送邮件的。唉，难道还是我的 SMTP 配置不正确。

为了验证不是 Clientexec 只优化了 Gmail 的发送邮件，我又把域名添加到 [[MXRoute]] 生成了一个 SMTP 的用户名和密码。然后在 Clientexec 后台添加了配置，测试，发现竟然也发送成功了。那么到此时我只能怀疑是不是 Mailcow 在发信的时候有一些限制。

### 开启 Clientexec 调试日志

编辑 `config.php`

```
    // ***  LOG_LEVELS (each level adds additional information) ***
    // 0: No logging
    // 1: Security attacks attempts, errors and important messages (recommended level)
    // 2: Reserved for debugging
    // 3: + Warnings and EventLogs, VIEW/ACTION and Request URIs and URI redirections and POST/COOKIE values
    // 4. + plugin events, curl requests, some function calls with their parameters, etc.
    //          (use this when sending logs to support)
    // 5: + include suppressed actions
    // 6: + Action responses (ajax,serialized,XML (as array)
    // 7: + SQL queries
    define('LOG_LEVEL', 6);

    // To activate text file logging, replace the 'false' with the file full path. Do not use relative paths.
    // Use absolute paths(e.g. /home/yourinstallationpath/ce.log, instead of ce.log)
    // The log may show passwords, so please use a file outside the web root, but writable by the web server user.
    define('LOG_TEXTFILE', 'ce.log');
```

然后将日志等级调整到 6，将日志写到文件中方便查看。

然后在页面操作的时候查看日志 `less ce.log`。

于是我又将 Mailcow 的 SMTP 配置添加到后台，进行测试。同时观察日志。

```
(4) 04/05/23 07:35:42 - Starting to send Test Email with subject "Clientexec Test Email"...
(5) 04/05/23 07:35:43 - CLIENT -> SERVER: EHLO client.einverne.info

(5) 04/05/23 07:35:43 - CLIENT -> SERVER: STARTTLS

(5) 04/05/23 07:35:44 - CLIENT -> SERVER: EHLO client.einverne.info

(5) 04/05/23 07:35:44 - CLIENT -> SERVER: AUTH LOGIN

(5) 04/05/23 07:35:44 - CLIENT -> SERVER: [credentials hidden]
(5) 04/05/23 07:35:44 - CLIENT -> SERVER: [credentials hidden]
(5) 04/05/23 07:35:45 - CLIENT -> SERVER: MAIL FROM:<admin@client.einverne.info>

(5) 04/05/23 07:35:45 - CLIENT -> SERVER: RCPT TO:<email-test@clientexec.com>

(5) 04/05/23 07:35:45 - SMTP ERROR: RCPT TO command failed: 553 5.7.1 <admin@client.einverne.info>: Sender address rejected: not owned by user admin@mailcow.mail

(5) 04/05/23 07:35:45 - CLIENT -> SERVER: QUIT

(5) 04/05/23 07:35:45 - SMTP Error: The following recipients failed: email-test@clientexec.com: <admin@client.einverne.info>: Sender address rejected: not owned by user admin@mailcow.mail
```

发现了 SMTP Error。

## 验证 Mailcow

因为排除了 Clientexec 后台配置的问题，于是我使用 Mailcow 加上 `Sender address rejected` 关键字进行搜索，这才发现 Mailcow 相关的问题出现过很多次， 原来是 Mailcow 默认开启了 Sender Addresses Verification，必须要手动关闭这个[验证](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-disable_sender_verification/) 才能代替发送邮件。

从错误日志中就能发现原来 Clientexec 在测试发送邮件的时候是使用的 `admin@clientexec-domain.com` 来发送邮件的。而我的 SMTP 配置的发件邮箱是 `no-reply@domain.com` 这样的，Mailcow 默认情况下是不允许用户以别人的身份发送邮件的(当然这也是能理解的，我不理解的是 Clientexec 后台明明是有 Override From 这样的选项的，却在测试邮件的功能里用其他邮箱来测试)，所以才会报错。

## 解决问题的方法

本来只是想简单的总结一下解决问题的过程，但这个解决问题的思维过程正好可以提炼成一个思考问题的方式。而以上解决问题的思考方式就是非常简单的排除法。

* 首先是验证 SMTP 配置是否有问题，用 Python 写了一段发信程序
* 然后是验证 Clientexec 后台 SMTP 配置是否有 BUG，通过尝试其他的 SMTP 配置，发现没有问题
* 那是不是 SMTP 提供服务的 Mailcow 有问题，通过日志和错误信息查询到原因

## Related Posts

* [常见的邮件发送错误](/post/2024/03/common-email-error.html) - 03/09/2024
* [Sieve 一个过滤邮件的语言](/post/2023/04/sieve-mail-filter-languange.html) - 04/12/2023
* [介绍一下新推出的 EV Hosting 网络共享托管服务](/post/2023/04/introducing-ev-hosting.html) - 04/04/2023
* [记录一下 Clientexec 中配置 SMTP 时的一些问题](/post/2023/04/clientexec-smtp-config.html) - 04/04/2023
* [Clientexec 汉化](/post/2023/04/clientexec-language-chinese.html) - 04/01/2023
* [自建邮件服务器的选择和比较](/post/2022/04/self-hosted-mail-server-choice.html) - 04/25/2022
* [使用 Mailcow 自建邮件服务器](/post/2022/04/mailcow-email-server.html) - 04/23/2022
* [Laravel 学习笔记：发送邮件](/post/2022/03/laravel-send-email.html) - 03/29/2022
* [电子邮件是如何工作的](/post/2022/03/how-email-send-and-receive.html) - 03/01/2022
* [使用 Poste 自行搭建邮件服务器](/post/2021/08/poste-self-hosted-email-service.html) - 08/26/2021
* [邮件服务器相关概念学习](/post/2018/09/mail-server.html) - 09/05/2018
* [免费发送邮件的服务收集整理](/post/2017/07/email-services-collection.html) - 07/30/2017

---

* [← Previous（前一篇）](/post/2023/04/why-we-sleep-notes.html "《我们为什么要睡觉》读书笔记")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2023/04/introducing-ev-hosting.html "介绍一下新推出的 EV Hosting 网络共享托管服务")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2023/04/clientexec-smtp-config.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [clientexec 6](/tags.html#clientexec)
* [web-hosting-billing 1](/tags.html#web-hosting-billing)
* [mailcow 5](/tags.html#mailcow)
* [smtp 10](/tags.html#smtp)
* [email 20](/tags.html#email)
* [python 77](/tags.html#python)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").