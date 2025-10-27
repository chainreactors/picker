---
title: Windsurf 又一款 AI 智能编辑器
url: https://blog.einverne.info/post/2024/11/windsurf.html
source: Verne in GitHub
date: 2024-11-24
fetch_date: 2025-10-06T19:13:53.367926
---

# Windsurf 又一款 AI 智能编辑器

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

# Windsurf 又一款 AI 智能编辑器

Posted on 11/23/2024
, Last modified on 11/23/2024
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2024-11-23-windsurf.md)

这两年随着 AI 模型在代码编程领域越来越强大，尤其是 Claude 的发布，在此基础上诞生了很多相关的 AI 辅助编程工具，比如 [[Cursor]]，[[GitHub Copilot]] 等等，今天我想要介绍另外一款 AI 驱动的集成开发环境 Windsurf。

[Windsurf](https://codeium.com/windsurf) 是 Codeium 公司发布的一款 AI 辅助编程工具。

## 功能

Windsurf 不仅提供了代码自动补全，还提供了包括独立 Agents 上下文理解等等功能：

* 不仅包括了代码生成和补全，还包含了 Agents，可以作为一个独立的个体来协助完成编码
  + Flows = Agents + Copilots
* Cascade，更强的上下文感知能力，理解整个代码库，多文件编辑
* Windsurf 甚至可以直接在终端安装依赖，协助完成环境搭建

![JdNDLfohKV](https://pic.einverne.info/images/JdNDLfohKV.png)

## 使用

Windsurf 也是基于 Visual Studio Code，所以第一次打开的时候，可以直接从本地的 Visual Studio Code，或者 Cursor 中导入配置，并且所有的操作和我之前的配置一样，几乎什么都没有改动就可以直接开始使用。

视频介绍

[Bilibili](https://www.bilibili.com/video/BV1EfB2YeEdj/) [YouTube](https://youtu.be/kteBXWS-orY)

## 使用小技巧

在编辑器中按下 Cmd + i ，可以使用自然语言生成或重构代码。直接在行内就可以呼唤出提示框。

![knUKaxwg8a](https://pic.einverne.info/images/knUKaxwg8a.png)

在任何代码产生变动的时候，都会产生一个变更记录。

![FS6tz7t2b6](https://pic.einverne.info/images/FS6tz7t2b6.png)

自动补充

在我短暂的体验中，发现 Windsurf 的自动提示和补全确实要更智能一些，智能的点在于，它不是和传统的编辑器一样，会自动补全代码后面的内容，它会分析前后的代码内容，并且根据内容智能分析并提示，我在使用的过程中，因为从外部粘贴了几句话，但是文字中使用的标点是英文的逗号，但是在我的上下文中，全部都是使用的中文的符号，在我继续编码后面的内容的时候，它会自动提示我前面的内容从英文的逗号，变更为中文的逗号，并且我直接使用 Tab 就完成了四处逗号的替换。

@ 引用符号

可以在对话框中通过 @ 符号来引用函数，类，文件，整个目录等等，将其加入到上下文中。

## 价格

两周之后，可以根据自己的需要来订购使用。

![dq4LEOdbVg](https://pic.einverne.info/images/dq4LEOdbVg.png)

现在 Windsurf 刚刚上线，官方还给了两个月的 Pro 使用体验。

![qUAl9W8rPi](https://pic.einverne.info/images/qUAl9W8rPi.png)

可以点击链接 <https://codeium.com/offers?offer_code=codeium-thanks-you>

截止 11 月 23 日，目前上面的链接已经无法领取。不过新用户还是可以免费试用两个礼拜的。

## 最后

现在下载 Windsurf 还可以自动获得两周的 Pro 体验，

## related

* [[Copilot]]
* [[Cursor.so]]
* [[CopyCoder]]
* [[Replit Agent]]

## Related Posts

* [利用 SpecStory 记录每一次和 AI 的对话](/post/2025/06/specstory-save-ai-chat-history.html) - 06/17/2025
* [Cursor Rules 为 AI 设限](/post/2025/04/cursor-rules.html) - 04/02/2025
* [Trae 字节推出的一款本地 AI 代码编辑器](/post/2025/01/trae-ide-from-bytedance.html) - 01/21/2025
* [Windsurf 又一款 AI 智能编辑器](/post/2024/11/windsurf.html) - 11/23/2024
* [让 AI 无处不在](/post/2023/07/ai-everywhere-in-daily-life.html) - 07/13/2023
* [AI 支持的编辑器 Cursor 使用体验](/post/2023/03/ai-powered-editor-cursor-so.html) - 03/24/2023
* [由 ChatGPT 延展开整理一下 AI 相关的服务和产品](/post/2023/02/chatgpt-ai-powered-services.html) - 02/28/2023

---

* [← Previous（前一篇）](/post/2024/11/macos-windows-management-1piece.html "macOS 上强大的窗口管理工具 1Piece")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2024/11/snippetslab-personal-code-snippets.html "SnippetsLab 私人的代码片段库")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2024/11/windsurf.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [产品体验 185](/categories.html#产品体验)

* [ai 45](/tags.html#ai)
* [editor 28](/tags.html#editor)
* [visual-code 3](/tags.html#visual-code)
* [cursor 7](/tags.html#cursor)
* [codeium 1](/tags.html#codeium)
* [编辑器 1](/tags.html#编辑器)
* [代码生成 1](/tags.html#代码生成)
* [aigc 2](/tags.html#aigc)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").