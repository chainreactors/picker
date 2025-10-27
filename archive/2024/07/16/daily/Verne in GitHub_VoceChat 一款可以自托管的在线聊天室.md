---
title: VoceChat 一款可以自托管的在线聊天室
url: https://einverne.github.io/post/2024/07/vocechat-online-chat-room.html
source: Verne in GitHub
date: 2024-07-16
fetch_date: 2025-10-06T17:38:25.454145
---

# VoceChat 一款可以自托管的在线聊天室

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

# VoceChat 一款可以自托管的在线聊天室

Posted on 07/15/2024
, Last modified on 07/15/2024
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2024-07-15-vocechat-online-chat-room.md)

[VoceChat](https://voce.chat/) 是一款使用 Rust（后端），React（前端），Flutter（移动端）开发的，开源，支持独立部署的在线聊天服务。VoceChat 非常轻量，后端服务只有 15MB 的大小，打包的 Docker 镜像文件也只有 61 MB，VoceChat 可部署在任何的服务器上。

* 官方网址：<https://voce.chat/>
* 官方文档：<https://doc.voce.chat/>
* [GitHub](https://github.com/Privoce/vocechat-web)

## 特色

前端页面可以内嵌到自己的网站下，VoceChat 从 Slack, Discord, [[RocketChat,]] Solid, [[Matrix]], [[Mattermost]] 等产品和规范中博采众长，适用于团队内部交流，个人聊天服务，网站客服，网站内嵌社区的场景。

在当今众多聊天工具中，VoceChat 以其轻量、安全和易用性脱颖而出。作为一款开源的即时通讯软件，VoceChat 为个人和小型团队提供了简洁高效的沟通解决方案。

* 可以发送图片，语音，文字，emoji ，文件等
* 提供 RESTful API 文档，支持自定义客户端和机器人
* 支持 Android、iOS 端
* 支持 Docker 安装，部署极其简单
* 备份简单
* 支持第三方登录（比如 GitHub、MetaMask、Google 等）
* 支持访问控制 & 访客模式
* API 文档详细
* 支持自建频道
* 支持邀请用户
* 支持语音
* 支持网页挂件，通过 SDK 嵌入网页，在网页中实现频道聊天
* 支持 iframe 嵌入网页

## 视频演示

[YouTube 链接](https://youtu.be/W-mO0vAzKbY?si=T7K20dbhNBuq76VL)

## 安装

安装的配置文件可以参考我的 [dockerfile](https://github.com/einverne/dockerfile/tree/master/vocechat)。

```
git clone https://github.com/einverne/dockerfile.git
cd dockerfile/vocechat
```

直接使用 [[Nginx Proxy Manager]] 设置，或者使用 Nginx 代理

```
server {
 server_name vocechat.yourdomain.com;
 location / {
    proxy_pass http://127.0.0.1:3010;
    proxy_redirect off;
    proxy_set_header    Host  $host;
    proxy_set_header    X-Real-IP    $remote_addr;
    proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    proxy_max_temp_file_size 0;
    # SSE
    proxy_http_version 1.1;
    proxy_set_header Connection '';
  }
}
```

## 优点

### 轻量

之前我也分享过 [Chatwoot](https://blog.einverne.info/post/2023/03/chatwoot-open-source-customer-engagement.html) 另外一款客户支持工具，但是相较于这一款 Voce，明显 Chatwoot 更重，虽然功能也能更强大，自带 Wiki 系统，自带 HelpDesk，支持团队等等，但是部署需要创建七八个容器，而 VoceChat 只需要一个容器。

### 美观

相较于其他商业性质的产品，VoceChat 更显得美观，而不像其他商业级别的应用那么端庄正式。

![O9nGNwn4w_](https://pic.einverne.info/images/O9nGNwn4w_.png)

### 支持语音

VoceChat 通过 [[Agora]] 实现了语音和视频对话，Agora 每个月提供 1000 小时的免费在线语音通话，足够目前使用了。

![jERDCf4uSr](https://pic.einverne.info/images/jERDCf4uSr.png)

### 屏幕分享

VoceChat 还自带了一个屏幕分享，可以分享当前的屏幕窗口和网页内容。

## 一些限制

### 群组人数限制

免费版本群组有 20 人使用限制，当然付费可以解决这个问题。

![kgZL_ofXFj](https://pic.einverne.info/images/kgZL_ofXFj.png)

## Bot

* [部署 ChatGPT 机器人](https://github.com/Tansuo2021/vocechat-chatbot-vercel)

## 最后

如果想要体验，可以访问我的[实例](https://vc.einverne.info/)的大厅，可以在大厅发送 PT，我会邀请你进入私人频道。

## related

* [[Mattermost]]
* cinny+matrix 服务端
* [[Tailchat]]

## reference

* [Chatwoot](https://blog.einverne.info/post/2023/03/chatwoot-open-source-customer-engagement.html) Ruby 编写

## Related Posts

* [VoceChat 一款可以自托管的在线聊天室](/post/2024/07/vocechat-online-chat-room.html) - 07/15/2024

---

* [← Previous（前一篇）](/post/2024/07/perplexity-ai-usage.html "结合了 Google 和 AI 的对话搜索引擎：Perplexity AI")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2024/07/thailand-dtv-visa.html "泰国 DTV 数字游民签证")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2024/07/vocechat-online-chat-room.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [产品体验 185](/categories.html#产品体验)

* [vocechat 1](/tags.html#vocechat)
* [chatwoot 3](/tags.html#chatwoot)
* [business-messaging 1](/tags.html#business-messaging)
* [chatroom 1](/tags.html#chatroom)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").