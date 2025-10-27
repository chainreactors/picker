---
title: 简洁高效的开源网络终端 Next Terminal
url: https://blog.einverne.info/post/2025/06/next-terminal.html
source: Verne in GitHub
date: 2025-06-24
fetch_date: 2025-10-06T22:52:15.192608
---

# 简洁高效的开源网络终端 Next Terminal

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

# 简洁高效的开源网络终端 Next Terminal

Posted on 06/23/2025
, Last modified on 06/23/2025
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2025-06-23-next-terminal.md)

我个人一直都是使用本地的 SSH Config 来管理我的 SSH 连接，虽然这个方案有自身的优点，就是安全，易配置，我所有的连接都只允许使用 SSH Key 访问，关闭了用户名密码，另外所有的配置都通过 assh 一键配置，我给所有的节点都配置了昵称，所以我只需要输入 `ssh alias` 就可以连接到任何我想连接的机器。

但这个方案有一个缺点，就是我必须在我经常使用的机器旁，我才能访问我的服务器，一旦我离开了我的电脑，那么任何设备我都无法连接上。但是前段时间我发现了一款基于浏览器的远程连接管理工具 Next Terminal。在我看来 Next Terminal 更像是一个堡垒机，可以在一个中心化的节点上来管理 SSH，Telnet 等等连接，还提供了安全审计等功能。

[Next Terminal](https://github.com/dushixiang/next-terminal) 是一款使用 Golang 和 React 开发的 HTML5 远程桌面网关，具有小巧、易安装、易使用、资源占用小的特点，支持多种远程协议如 RDP、SSH、VNC 和 Telnet 的连接和管理。作为一个开源的交互审计系统，它为用户提供了一种高效且安全的方式来管理远程连接，特别强调了易用性和安全性。Next Terminal 虽然定位轻量堡垒机，但是支持RDP、SSH、VNC、Telnet、Kubernetes协议超多协议。

## 核心功能

Next Terminal 拥有众多实用功能，使其成为运维和安全团队的理想选择：

* 多协议支持：在一套系统中访问 RDP、SSH、VNC、TELNET 等协议资产，无需插件，只需一个浏览器即可。
* 实时监控：随时查看当前活跃的会话，进行监控和阻断。对于字符协议，甚至可以限制禁止某些命令的执行和记录。
* 事后审计：观察并记录所有环境中的每个在线资源、连接、交互会话和其他安全事件，这些事件被记录在结构化的审计日志中。
* 授权凭证管理：集中管理用户的授权凭证，确保安全访问。
* 批量执行命令：支持批量执行命令，提高操作效率。
* 双因素认证：增强系统的安全性，确保用户身份的可靠性。
* 资产标签和授权：为资产打标签，方便分类和管理，同时精确控制资产的授权。
* 多用户与用户分组：支持多用户和用户分组，方便权限管理。

## 商业化

目前 Next Terminal 已经开始进行商业化的尝试，可以在[官网](https://next-terminal.typesafe.cn/) 购置专业版以及商业版的授权。

## Installation

参考官方[文档](https://next-terminal.typesafe.cn/)

```
version: '3.3'
services:
  guacd:
    image: dushixiang/guacd:latest
    volumes:
      - ./data:/usr/local/next-terminal/data
    restart: always
  next-terminal:
    image: dushixiang/next-terminal:latest
    environment:
      DB: sqlite
      GUACD_HOSTNAME: guacd
      GUACD_PORT: 4822
    ports:
      - "8088:8088"
    volumes:
      - /etc/localtime:/etc/localtime
      - ./data:/usr/local/next-terminal/data
    restart: always
```

## 安全建议

Next Terminal 提供了便捷的远程访问能力，但是服务器的安全性依然是首要考虑的因素。建议安装之后立即修改复杂的管理员密码，并开启双因素认证。

尽量避免将 Next Terminal 直接暴露到公网环境，合理配置授权策略，遵循最小权限原则。

## 最后

Next Terminal 相较于其他的开源堡垒机项目，更轻量，简单，被管理资产透明，适合个人和小型团队使用。JumpServer 功能全面，但是非常笨重，适合大型企业。Teleport 安全性相对较好，但是需要在被管理资产上进行额外的操作，适合对安全性要求较高的场景。

## related

* [[teleport]]
* [[JumpServer]]

## Related Posts

* [简洁高效的开源网络终端 Next Terminal](/post/2025/06/next-terminal.html) - 06/23/2025
* [开源跨平台终端 XPipe](/post/2025/03/xpipe.html) - 03/06/2025
* [使用 assh 来管理 SSH config](/post/2020/07/advanced-ssh-config-management.html) - 07/28/2020
* [使用 port knocking 隐藏 SSH daemon 端口](/post/2019/07/how-to-use-port-knocking-hide-ssh-daemon-port.html) - 07/19/2019
* [VPS 安全设置](/post/2018/03/vps-security.html) - 03/18/2018

---

* [← Previous（前一篇）](/post/2025/06/chatwise.html "ChatWise 本地多模型支持的 AI 客户端")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2025/06/google-gemini-cli.html "Google Gemini CLI 使用初体验：命令行上的 AI 工作流引擎")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2025/06/next-terminal.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [产品体验 185](/categories.html#产品体验)

* [next-terminal 1](/tags.html#next-terminal)
* [terminal 13](/tags.html#terminal)
* [assh 2](/tags.html#assh)
* [ssh 22](/tags.html#ssh)
* [rdp 1](/tags.html#rdp)
* [vnc 2](/tags.html#vnc)
* [telnet 1](/tags.html#telnet)
* [vps 31](/tags.html#vps)
* [vps-management 1](/tags.html#vps-management)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").