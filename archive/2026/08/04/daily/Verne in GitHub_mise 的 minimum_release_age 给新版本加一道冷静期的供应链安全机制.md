---
title: mise 的 minimum_release_age 给新版本加一道冷静期的供应链安全机制
url: https://blog.einverne.info/post/2026/08/mise-minimum-release-age.html
source: Verne in GitHub
date: 2026-08-04
fetch_date: 2026-08-05T04:54:53.998427
---

# mise 的 minimum_release_age 给新版本加一道冷静期的供应链安全机制

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

# mise 的 minimum\_release\_age 给新版本加一道冷静期的供应链安全机制

Posted on 08/04/2026
, Last modified on 08/04/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-08-04-mise-minimum-release-age.md)

![新版本在时间闸门前等待放行](https://pic.einverne.info/images/2026-08-04-10-00-00-mise-minimum-release-age.png)

今天在终端里跑 `mise upgrade` 想要升级 herdr 的时候，突然看到一条以前没见过的 WARN 提示，「mise WARN 1 newer herdr release hidden by minimum\_release\_age」，大意是有一个更新的版本存在，但因为发布时间太短，被 `minimum_release_age` 设置过滤掉了，暂时不会被安装。最后去看了 [[mise]] 的更新日志才发现，这是 mise 在 2026 年新引入的一个供应链安全机制，而且从 v2026.6.2 开始默认对所有人生效。这篇文章就把这个机制的来龙去脉、警告的含义以及怎么配置讲清楚。

## minimum\_release\_age 是什么

简单说，`minimum_release_age` 的作用是：一个新版本发布之后，必须先等待一段时间（默认 24 小时），mise 才会认为它”可用”。在这个时间窗口内，即使上游已经发布了新版本，`mise install`、`mise upgrade`、`mise latest` 这些命令也会当它不存在，继续解析到上一个满足时间要求的版本。

这个设计针对的是近几年愈演愈烈的软件供应链攻击。典型的攻击场景是这样的：攻击者拿到某个流行包的发布权限（钓鱼拿到 maintainer 的 npm token、CI 配置泄露等等），发布一个带恶意代码的新版本，然后等着全世界的自动更新工具在几小时内把它拉下来。这类被投毒的版本通常存活时间很短，社区、安全厂商和 registry 官方往往在几小时到一两天内就会发现并下架。所以”等一等”本身就是一种非常朴素但有效的防御——只要你不做第一批吃螃蟹的人，绝大多数投毒版本在到达你机器之前就已经被清理掉了。

这个思路并不是 mise 首创。[[Renovate]] 很早就有 `minimumReleaseAge` 配置，用来推迟自动升级 PR 的创建；[[pnpm]] 也在 10.16 之后加入了同名的 `minimumReleaseAge` 设置，安装依赖时跳过太新的版本。mise 做的事情是把同样的理念搬到了开发工具版本管理这一层——你通过 mise 安装的 node、go、terraform，以及各种通过 aqua、npm、pipx 后端装的 CLI 工具，统一套上这道时间闸门。

## 那条 WARN 警告到底在说什么

回到开头那条警告。当你运行 `mise upgrade` 或者 `mise outdated` 之类的命令时，mise 会去查询各个工具的远程版本列表。如果它发现存在比当前已安装版本更新的版本，但那个版本的发布时间还没超过 `minimum_release_age` 设定的时长，就会打印一条 WARN，告诉你有 N 个更新版本因为太新而被暂时过滤掉了。

这里要强调的是，这不是错误，也不需要你做任何事。mise 会继续使用满足时间要求的最新版本，被过滤的那个版本会在时间窗口过去之后（默认发布满 24 小时）自动变为可用，下次再跑 `mise upgrade` 就会正常升级上去。这条警告存在的意义只是告知，避免你困惑”明明上游发新版了为什么 mise 装不到”。

从 v2026.6.2 开始，mise 为所有能提供发布时间戳的后端内置了这个 24 小时的默认延迟，包括 core（node、go 这些核心工具）、aqua、github、cargo、go、npm、pipx 等。也就是说即使你从来没在配置里写过 `minimum_release_age`，这个机制也已经在保护你了，这也是为什么很多人像我一样是先看到警告、再反过来查文档的。

## 几个容易误解的细节

在翻 mise 文档和源码的过程中，我发现这个机制有几个行为细节值得单独说清楚，不然很容易产生错误的预期。

第一，它只影响模糊版本解析，不影响显式 pin 的版本。所谓模糊版本，就是 `latest`、`node@20`、`terraform@1` 这种需要 mise 去解析”到底是哪个具体版本”的写法。如果你在 `mise.toml` 里明确写死了 `node = "22.14.0"`，那不管这个版本是不是一小时前刚发布的，mise 都会照装不误。这个设计是合理的——显式 pin 意味着你明确知道自己要什么，工具不应该替你做主；而模糊解析场景下你把选择权交给了 mise，它就有责任帮你过滤掉风险窗口内的版本。

第二，过滤能力取决于后端能不能提供发布时间戳。core、aqua、github、cargo、go、npm、pipx 这些后端能拿到每个版本的发布时间，过滤就能生效；拿不到时间戳的版本会被默认放行，不会因为”无法判断”而被误伤。

第三，传递依赖的覆盖范围目前还有限。对于 `npm:` 和 `pipx:` 后端安装的工具，mise 会把时间窗口透传给底层的包管理器，让传递依赖也遵守同样的规则；其他后端目前只过滤顶层工具本身的版本。如果你的威胁模型主要担心 npm 生态的依赖投毒，这一点算是个不小的加分项。

## 配置方式与实践建议

默认的 24 小时对大多数人来说是个不错的平衡点，但 mise 提供了完整的配置手段，可以按自己的风险偏好调整。

全局调整时间窗口，在 `~/.config/mise/config.toml` 或项目的 `mise.toml` 里设置：

```
[settings]
minimum_release_age = "7d"   # 只安装发布超过 7 天的版本
```

时长支持 `24h`、`7d`、`1y` 这种相对写法。如果你所在的团队对安全要求比较高，把这个值调到 3 到 7 天是常见做法。

有些工具的更新是时间敏感的，比如漏洞扫描器 trivy，它的新版本往往携带最新的漏洞库，晚装一天反而降低安全性。这种情况可以按工具覆盖全局设置：

```
[settings]
minimum_release_age = "7d"

[tools.trivy]
version = "latest"
minimum_release_age = "1d"
```

也可以用排除列表把特定工具或整个后端排除在全局策略之外，支持通配符：

```
[settings]
minimum_release_age = "7d"
minimum_release_age_excludes = ["trivy", "npm:*"]
```

需要注意优先级顺序：命令行的 `--minimum-release-age` 参数最高，其次是按工具的设置，最后才是全局设置。被排除的工具仍然会尊重它自己的 per-tool 设置和命令行参数。

如果某次你确实需要立刻装上一个刚发布的版本（比如上游刚修了一个影响你的 bug），不用改配置文件，临时用命令行参数绕过即可：

```
mise upgrade node --minimum-release-age 0
mise latest node --minimum-release-age 2024-01-01   # 也支持绝对日期
```

反过来，如果你完全不想要这个机制，在全局配置里把 `minimum_release_age` 设为 `0` 就可以彻底关掉。不过在关掉之前建议想清楚，这个默认值的存在几乎没有日常成本——你感知到的无非就是新版本晚一天到手——换来的却是躲开绝大多数投毒版本存活窗口的保护。

另外值得一提的是它和 `mise.lock` 的配合。lockfile 保证的是”团队所有人装到的是同一个被验证过的版本”，`minimum_release_age` 保证的是”解析新版本时不会撞上刚出炉的风险版本”，两者是互补关系而不是替代关系。对于有 CI 环境的项目，lockfile 加上默认的时间窗口，基本就把工具链这一层的供应链风险控制在了一个比较舒服的水平。

## 最后

`minimum_release_age` 是那种典型的”好的默认值”设计：机制本身极其简单，就是给新版本加一道冷静期，但它选择了默认开启，让所有 mise 用户在无感知的情况下获得了对供应链投毒攻击的基础免疫。从 npm 的 event-stream 到近几年层出不穷的 maintainer 账号劫持事件，这类攻击的共同特点就是投毒版本存活时间短、传播依赖自动更新，而”等 24 小时”恰好精准打在这两个特点上。

## Related Posts

* [mise 的 minimum\_release\_age 给新版本加一道冷静期的供应链安全机制](/post/2026/08/mise-minimum-release-age.html) - 08/04/2026
* [利用 mise 替换 asdf 的迁移方案](/post/2026/04/migrate-from-asdf-to-mise.html) - 04/08/2026

---

* [← Previous（前一篇）](/post/2026/07/chezmoi.html "chezmoi Go 语言编写的跨平台 dotfiles 管理工具")
* [Archive（目录）](/archive.html)
* Next（后一篇） →

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2026/08/mise-minimum-release-age.html)评论。

* [经验总结 608](/categories.html#经验总结)

* [mise 3](/tags.html#mise)
* [supply-chain-security 1](/tags.html#supply-chain-security)
* [version-manager 2](/tags.html#version-manager)
* [devtools 2](/tags.html#devtools)
* [npm 4](/tags.html#npm)
* [security 11](/tags.html#security)
* [cli 44](/tags.html#cli)

---

© 2026 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").