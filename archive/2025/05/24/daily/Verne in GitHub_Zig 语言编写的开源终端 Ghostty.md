---
title: Zig 语言编写的开源终端 Ghostty
url: https://blog.einverne.info/post/2025/05/ghostty.html
source: Verne in GitHub
date: 2025-05-24
fetch_date: 2025-10-06T22:27:08.331119
---

# Zig 语言编写的开源终端 Ghostty

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

# Zig 语言编写的开源终端 Ghostty

Posted on 05/23/2025
, Last modified on 05/24/2025
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2025-05-23-ghostty.md)

在 Linux 上我使用 [[Guake]]，到后来换成 macOS 之后使用 Kitty，直到前段时间更换成 Warp，但是没想到这几天又发现一款不错的终端 Ghostty。没查不知道，但是一查之后才发现 Ghostty 背后的作者的故事是多么精彩，并且 Ghostty 使用的 Zig 语言也是我第一次听说。

[Ghostty](https://github.com/ghostty-org/ghostty) 由著名的开发者 Mitchell Hashimoto（HashiCorp 联合创始人）使用 Zig 语言编写的一款终端模拟器，在速度，功能性方面都有不错的优势。

Ghostty 目标是成为一个更快，功能更丰富的下一代终端应用，它不仅支持 GPU 加速，macOS 上使用 SwiftUI 构建，Linux 基于 GTK 构建，还内置了很多现代化的功能，在性能和易用性之间找到了一个平衡点。

## Mitchell Hashimoto

再进一步介绍 Ghostty 之前，我想先隆重介绍一下其作者 Mitchell Hashimoto。如果你在 DevOps，云计算以及软件开发领域工作，那么你一定对 Vagrant，Terraform，Packer 等等工具非常熟悉，而 Mitchell Hashimoto 就是这些作者背后的核心贡献者，他很早就热衷于编程，并且利用自己对这些技术的使用创办了 HashiCorp，极大地推动了云计算和基础设施自动化发展，深刻地改变了现代基础设施管理的构建和管理。

* Vagrant，用于构建和管理虚拟化开发环境的工具 极大的简化了开发环境的配置和共享
* Packer，用于创建相同机器镜像的自动化工具
* Terraform，「基础设施及代码」IaC 的工具，让我们可以用代码来定义和管理云资源

Mitchell Hashimoto 曾担任公司 CEO 和 CTO，但最终选择回归代码，宣布了 Ghostty 终端的诞生。

## Ghostty

简单来说，Ghostty 是一个跨平台的、使用 GPU 加速的现代化终端模拟器。它的核心优势在于：

* **卓越的性能**：和 Alacritty 一样，Ghostty 利用 GPU 进行渲染，确保了极低的延迟和高吞吐量，即使在处理大量输出时也能保持流畅。利用现代图形 API，将渲染任务交给 GPU，无论是快速滚动，复杂文本输出，还是运行 htop 这样实时更新的命令，Ghostty 都可以提供非常顺滑的使用体验
* **丰富的功能**：与 Alacritty 的极简主义不同，Ghostty 在保持高性能的同时，内置了许多开发者需要的功能，比如窗口/标签页管理（Multiplexing）、主题系统等。内置了终端多路复用，可以作为 Tmux 的一个代替，内置的原生窗口，标签页，Panes 等等，可以通过快捷键切换。
* **现代化设计**：Ghostty 在设计上考虑了许多现代化的使用场景，并致力于解决传统终端在交互和安全性上的一些痛点。支持 True Color，24-bit 真彩色，字体连字（Ligatures）支持，图像协议支持，超链接支持，支持数百款主题
* **强大的可配置选项和主题支持**，可以根据自己的使用习惯深度定制，从字体到颜色，到快捷键等等。Ghostty 已经拥有非常活跃的社区，大量的用户分享了自己的配置和主题。Ghostty 使用纯文本的配置选项，可以在 TOML 格式中完成配置

Ghostty 的目标是解决现有终端模拟器在性能，功能，稳定性和跨平台一致性方面的痛点，虽然 Ghostty 目前还在快速迭代和开发过程中，但是从 Mitchell 分享的内容和项目目标中可以看到 Ghostty 的一些核心特性和设计哲学。

## 安装

macOS 上可以使用如下的命令

```
brew install --cask ghostty
```

Ghostty 主要通过一个纯文本配置文件来自定义，这对于熟悉 Linux 环境喜欢通过文本编辑器来配置的用户来说（比如说）非常友好，并且可以通过 dotfiles 来管理我的配置。

## 使用

### 配置文件路径

首次启动之后配置文件会在如下的位置。

* Linux – `$HOME/.config/ghostty/config`
* macOS – `$HOME/Library/Application\ Support/com.mitchellh.ghostty/config`

配置文件使用键值对格式。

```
font-family = "Monaco"
```

记得编辑配置文件之后，在 Ghostty 中重新加载一下配置。在 Ghostty 菜单中「Reload Configuration」。

### 颜色和主题

背景和前景色

```
background = #ff66cc
foreground = #000000
```

### 主题

Ghostty 内置了上百个主题。你可以使用  `ghostty +list-themes`  命令列出所有可用主题，这个命令会给出每个主题外观的预览

```
theme = GruvboxDark
```

### 字体配置

Ghostty 提供了丰富的字体配置选项。

* `font-family`：设置首选字体系列。可以多次指定，用于字符回退
* `font-family-bold`, `font-family-italic`, `font-family-bold-italic`：分别设置粗体、斜体和粗斜体的字体系列
* `font-style`, `font-style-bold`, `font-style-italic`, `font-style-bold-italic`：指定用于终端字体样式的命名字体样式，例如 “Iosevka Heavy” 的样式为 “Heavy”。可以将值设为  `false`  来禁用特定样式
* `font-synthetic-style`：控制是否合成字体样式（粗体、斜体、粗斜体）。可以设为  `true`  或  `false`，或使用 “no-bold”, “no-italic” 等禁用特定合成样式
* `font-feature`：应用字体特性，例如  `ss20`  或  `-ss20`（禁用）。要禁用编程连字 (ligatures)，可以使用  `-calt`
* `font-size`：设置字体大小（以磅为单位），支持非整数值
* `font-variation`, `font-variation-bold`, `font-variation-italic`, `font-variation-bold-italic`：为可变字体设置字体变体值，格式为  `id=value`，例如  `wght=700`

要列出系统上可用的字体，可以使用命令  `ghostty +list-fonts`

### 快捷键

可以自定义键盘快捷键来执行特定操作。例如，创建一个快捷键  `Ctrl+d`  将当前 Ghostty 窗口向右分割成两个窗格

```
keybind = ctrl+d=new_split:right
```

Ghostty 还支持许多其他配置，涵盖鼠标和剪贴板行为、终端行为、启动会话等。例如，可以通过创建会话文件并使用  `--session`  命令行标志来控制启动时的标签页、窗口布局、工作目录和启动程序。

完整的配置选项列表可以在 Ghostty 的[官方文档](https://ghostty.org/docs/config/reference)或相关配置指南中找到。

## 使用

配置快捷键 Ctrl+D 分割窗口

```
keybind = ctrl+d=new_split:right
```

### 自定义主题

列出主题

```
ghostty +list-themes
```

在配置文件中使用

```
theme = Unikitty
```

可以配置将 Ghostty 窗口和内容使用相同的主题色

```
window-theme = ghostty
```

Ghostty 的出现，为我们这些追求极致效率的开发者提供了又一个新的选择。它不仅仅是一个简单的终端模拟器，更像是一个现代化的开发工作台。它融合了 Alacritty 的速度和 Kitty 的功能，并在此基础上进行了创新和优化。

虽然 Ghostty 还很年轻，但凭借其出色的设计理念、强大的性能和活跃的社区，我相信它有潜力成为未来终端模拟器领域的有力竞争者。如果你正在寻找一款新的终端工具，不妨给 Ghostty 一个机会，或许它会给你带来意想不到的惊喜。

## related

* [[Guake]]
* [[Kitty]]
* [[wezterm-terminal]]
* [[Alacritty 终端]]
* [[Mac 应用 iTerm2]]
* [[Warp]]

## Related Posts

* [Zig 语言编写的开源终端 Ghostty](/post/2025/05/ghostty.html) - 05/23/2025

---

* [← Previous（前一篇）](/post/2025/05/docker-java-gracefully-stop.html "关于在 Docker 容器中如何优雅关闭 Java 应用的记录")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2025/05/novita-ai-model-gpu-cloud.html "Novita AI 面向 AI 开发者的 GPU 云平台")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2025/05/ghostty.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [产品体验 185](/categories.html#产品体验)

* [terminal 13](/tags.html#terminal)
* [zig 1](/tags.html#zig)
* [open-source 43](/tags.html#open-source)
* [cross-platform 4](/tags.html#cross-platform)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").