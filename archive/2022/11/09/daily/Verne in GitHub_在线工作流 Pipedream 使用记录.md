---
title: 在线工作流 Pipedream 使用记录
url: https://einverne.github.io/post/2022/11/pipedream-usage.html
source: Verne in GitHub
date: 2022-11-09
fetch_date: 2025-10-03T22:01:07.232949
---

# 在线工作流 Pipedream 使用记录

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

# 在线工作流 Pipedream 使用记录

Posted on 11/08/2022
, Last modified on 11/08/2022
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2022-11-08-pipedream-usage.md)

今天在看 Grafana 入门 [教程](https://grafana.com/tutorials/grafana-fundamentals/) 的时候偶然间发现了 Pipedream 这个网站，在 Grafana 的演示中利用 Pipedream 创建 Workflows，然后在 Alert Manager 中通过 Webhook 想 Pipedream 发起调用，然后利用 Pipedream 的能力就可以向集成的应用（Telegram，Email，Slack）等等发送告警通知了。

## 什么是 Pipedream

Pipedream 是一个可以定义自己的在线自动化工作流的 SaaS 工具，Pipedream 允许用户创建并运行一个工作流，这个工作流可以串联多个不同的应用，可以执行用户代码定义的逻辑。可以认为是一个更高级，可编程的 [[IFTTT]]，[[Zapier]]。

* <https://pipedream.com/>
* Docs: <https://pipedream.com/docs/>

Pipedream 可以定义不同的触发器（HTTP，Webhook，定时，收到邮件，RSS，Telegram 消息，Discord Channel 等等）来触发工作流的执行。因为 Pipedream 工作流程允许编程，所以一个 Pipedream Workflow 就相当于直接运行了一个 在线的 serverless 的服务。

特性：

* 每个月提供 10000 次免费调用，每天近 333 次，对集成的应用，事件源没有任何限制
* 支持超过 [1000 多个外部 APP](https://pipedream.com/apps) ，Google，GitHub，Netlify，Twilio，Slack，Discord，等等
* 并且因为支持编程，并且可以通过环境变量将 API keys 或验证等传入给代码，所以 Pipedream 几乎可以连接任意的应用
* 可以编写代码完全控制工作流
* serverless 架构，完全不需要自己的服务器

Pipedream 的用途：

* 新用户注册，发送通知到 Slack
* 定时检测网站（RSS，Twitter）更新，发送消息通知，可以通过 Slack，Telegram，Email 等等
* 调用某个服务器 API，并发送通知
* 检测自己的服务是否宕机，即使每 5 分钟检查一次，一个月最多也只用了免费方案的 8%

## Workflows

Workflows 工作流，集成应用，数据，APIs。

* Workflows 由代码组成，是代码组织和执行的顺序，包含多个 steps
* 通过 Event（事件）触发，可以是 HTTP Requests，或者定时触发
* 添加 steps 来执行 Node.js， Python，Go，Bash 等等，或者使用内置的 actions
* Steps 按照 Workflow 中定义的顺序执行
* 每一个 step 产生的数据可以通过 `step` 对象获取

## Related Posts

* [在线工作流 Pipedream 使用记录](/post/2022/11/pipedream-usage.html) - 11/08/2022
* [使用 Huginn 搭建自己的 IFTTT](/post/2019/01/huginn.html) - 01/11/2019
* [Workflow for iOS 使用指南](/post/2018/02/workflow-usage.html) - 02/25/2018

---

* [← Previous（前一篇）](/post/2022/11/japanese-learning-tools-in-obsidian.html "Obsidian 中的日语学习工具")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2022/11/mastodon-custom-emoji.html "Mastodon 站点管理：导入自定义表情包")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2022/11/pipedream-usage.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [产品体验 185](/categories.html#产品体验)

* [pipedream 1](/tags.html#pipedream)
* [ifttt 5](/tags.html#ifttt)
* [workflow 5](/tags.html#workflow)
* [email 20](/tags.html#email)
* [rss 12](/tags.html#rss)
* [telegram 8](/tags.html#telegram)
* [serverless 3](/tags.html#serverless)
* [saas 8](/tags.html#saas)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").