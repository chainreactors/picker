---
title: 利用 Dev3000 优化 Claude Code 代码调试流程
url: https://blog.einverne.info/post/2025/09/dev3000.html
source: Verne in GitHub
date: 2025-09-17
fetch_date: 2025-10-02T20:14:12.601350
---

# 利用 Dev3000 优化 Claude Code 代码调试流程

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

# 利用 Dev3000 优化 Claude Code 代码调试流程

Posted on 09/16/2025
, Last modified on 09/16/2025
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2025-09-16-dev3000.md)

不知道大家在使用 Claude Code 辅助编写代码的过程中，有没有遇到过这样的烦恼，当 Claude Code 生成的代码不完美，发生错误时，我们需要将错误日志文件，这也前端页面截图再反馈给 Claude Code，让其修正错误，或者修复画面的错误。那有没有方法可以让 Claude Code 自己发现错误，并修正呢？那今天要介绍的这一个开源的工具 Dev3000 就是一个辅助 AI 开发的调试工具。

## Dev3000 是什么

[Dev3000 AI](https://github.com/vercel-labs/dev3000) 是一款面向 AI 调试的辅助工具，Dev3000 会自动监控服务器日志、浏览器事件、网络请求及截图，构建一条可供 AI 助手（如 Claude Code、Cursor）实时分析的时间线，提升 AI 调试效率。

## 主要功能

### 统一时间线监控

– 将服务器输出、浏览器控制台消息、用户操作（点击、滚动）、网络请求和错误截图按时间戳整合于同一视图，支持快速定位问题 ¹。

### 自动截图

– 在页面导航、关键事件和错误发生时，自动捕获截图并附加到日志中，帮助开发者还原用户操作和错误场景 ¹。

### 全量日志捕获

* 服务器端：完整的输出日志和控制台消息；
* 浏览器端：控制台日志、错误、点击、滚动及其他关键事件；
* 网络层：所有 HTTP 请求与响应的详细信息 ¹。

### AI 助手集成

通过 MCP（Message Control Protocol）服务器，将日志流接入 Claude Code，AI 助手能够实时搜索错误、分析日志并提供调试建议。

## 快速上手

安装 Dev3000

```
pnpm i -g dev3000
dev3000
```

替换开发命令

将 `pnpm dev` 或 `next dev -p 5000` 等命令替换为 `dev3000` 或 `dev3000 --port 5000`，即可启动监控。

连接 AI 助手

对于 Claude：

```
claude mcp add --transport http dev3000 http://localhost:3684/api/mcp/mcp
```

对于 Cursor：编辑配置文件，添加 MCP 服务器地址。

```
{
  "mcpServers": {
      "dev3000": {
          "type": "http",
          "url": "http://localhost:3684/api/mcp/mcp"
      }
  }
}
```

启动后，Dev3000 将同时在本地启动开发服务器、自动打开 CDP 连接的浏览器，并在 `http://localhost:3684/logs` 生成可视化时间线。

### Chrome 插件

因为现在插件还没有发布到 Chrome Web Store，所以需要本地开启开发者模式，然后将 dev3000 安装目录中的 `chrome-extension` 目录手动打包加载到 Chrome 。

如果要使用 Chrome 插件，需要添加

```
dev3000 --servers-only
```

## 使用场景

* **前端/后端联调**：无需在多个终端间切换，即可一次性查看服务器与浏览器的所有日志与操作。当前端项目请求后端产生错误之后，自动获取错误日志
* **跨团队协作**：共享统一时间线，减少因环境不同或信息不全导致的沟通成本。
* **AI 辅助调试**：结合 Claude 或 Cursor，让 AI 助手直接读取和分析日志流，高效定位并修复 Bug。

## 支持框架及扩展

Dev3000 并不限于 Next.js，也兼容 React、Vue、Vite 等主流前端框架，并可通过 `--script` 参数灵活指定任意自定义开发命令。

## Related Posts

* [搭建 Claude Code 中转服务](/post/2025/09/claude-relay-service.html) - 09/20/2025
* [利用 Dev3000 优化 Claude Code 代码调试流程](/post/2025/09/dev3000.html) - 09/16/2025

---

* [← Previous（前一篇）](/post/2025/09/complexity.html "Complexity 插件提升 Perplexity.ai 使用体验")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2025/09/claude-relay-service.html "搭建 Claude Code 中转服务")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2025/09/dev3000.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [dev3000 1](/tags.html#dev3000)
* [debug 5](/tags.html#debug)
* [mcp 3](/tags.html#mcp)
* [claude-code 13](/tags.html#claude-code)
* [cursor 7](/tags.html#cursor)
* [log 15](/tags.html#log)
* [ai-debug 1](/tags.html#ai-debug)
* [error-log 1](/tags.html#error-log)
* [codex 2](/tags.html#codex)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").