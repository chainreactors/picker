---
title: Google 聊天机器人 Bard 逆向
url: https://einverne.github.io/post/2023/03/google-bard-reverse-engineering.html
source: Verne in GitHub
date: 2023-03-24
fetch_date: 2025-10-04T10:27:51.307959
---

# Google 聊天机器人 Bard 逆向

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

# Google 聊天机器人 Bard 逆向

Posted on 03/23/2023
, Last modified on 03/23/2023
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2023-03-23-google-bard-reverse-engineering.md)

昨天晚上申请了 Google Bard 试用，今天下班了看到很多人都是几个小时就拿到了试用体验，我想我怎么没有收到邮件呢，我反复确认了邮箱确实没有，然后我想着再去网页上看看呢，登录了一下 <https://bard.google.com/> ，开始的时候没有使用代理，提示所在的地区暂时还不能用，然后加上[美国的代理](https://board.gtk.pw)，刷新一下就进去了。

> Bard 依托 Google 的一款大型语言模型，可以生成文字、撰写各种类型的创意内容，还可以根据它掌握的信息解答你的问题。

进去的第一个弹窗就是「警告」，Bard 是一个实验性的产品，可能不会一直都是正确的，并且 Google Bard 的每一条回复都会有赞同，否定，重新回答，或者直接 Google 的按钮。
![Od34](https://photo.einverne.info/images/2023/03/23/Od34.png)

大型语言模型是会犯错的
![ORxW](https://photo.einverne.info/images/2023/03/23/ORxW.png)

说实话 Google 做这个产品确实非常小心了，在下方的输入框下也有明确的注意事项。

![OZOQ](https://photo.einverne.info/images/2023/03/23/OZOQ.png)

## Python Lib

在调研的过程中发现已经有人[逆向了 Google Bard](https://github.com/acheong08/Bard)。通过如下的方法，然后执行 Python 即可在命令行使用 Bard，不过记住需要使用美国的 IP。

Go to [Google Bard](https://bard.google.com/)

* F12 打开 console
* Copy the values
* 找到 Application → Cookies → `__Secure-1PSID` 复制这个 Cookie 值
* 然后在 Chrome Console 中输入 `window.WIZ_global_data.SNlM0e`，复制结果

## Related Posts

* [Google 聊天机器人 Bard 逆向](/post/2023/03/google-bard-reverse-engineering.html) - 03/23/2023
* [电子书常见格式及格式转换](/post/2018/09/ebook-format-introduction-and-convert.html) - 09/18/2018

---

* [← Previous（前一篇）](/post/2023/03/tawk-to-usage.html "给网站加上实时聊天对话框 tawk.to 使用记录")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2023/03/ai-powered-editor-cursor-so.html "AI 支持的编辑器 Cursor 使用体验")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2023/03/google-bard-reverse-engineering.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [学习笔记 496](/categories.html#学习笔记)

* [google-bard 1](/tags.html#google-bard)
* [chatbot 1](/tags.html#chatbot)
* [chatgpt 22](/tags.html#chatgpt)
* [reverse-engineering 1](/tags.html#reverse-engineering)
* [python 77](/tags.html#python)
* [python-lib 3](/tags.html#python-lib)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").