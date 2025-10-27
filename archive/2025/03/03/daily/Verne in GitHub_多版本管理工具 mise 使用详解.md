---
title: 多版本管理工具 mise 使用详解
url: https://blog.einverne.info/post/2025/03/mise.html
source: Verne in GitHub
date: 2025-03-03
fetch_date: 2025-10-06T21:56:17.701746
---

# 多版本管理工具 mise 使用详解

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

# 多版本管理工具 mise 使用详解

Posted on 03/02/2025
, Last modified on 03/02/2025
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2025-03-02-mise.md)

我用了很多年的 [asdf](https://blog.einverne.info/post/2020/04/asdf-vm-manage-multiple-language.html) 作为管理各种语言版本的工具，但是最近一次更新，asdf 多了一些变化，我也写了一篇文章介绍怎么[升级](https://blog.einverne.info/post/2025/02/asdf-upgrade-0-16-0.html)的。在文章下方有小伙伴(lonelyhentxi) 给我推荐了 mise 这样一款使用 Rust 编写的多版本管理工具 mise，我大致的看了一下 mise，觉得是一个非常不错的项目，在这里再次感谢。

所以今天我就来介绍一下 mise，替换 mise 倒不是因为 asdf 不能用了，而是 Rust 在执行效率上确实要更快一些，比如我之前介绍的 [Meilisearch](https://blog.einverne.info/post/2024/08/meilisearch.html)，[espanso](https://blog.einverne.info/post/2021/09/espanso-text-expand.html) 等等都是因为 Rust 编写，效率上都有所提升。

## mise 是什么

[mise](https://github.com/jdx/mise) 是 Rust 编写的一个多版本开发环境工具。

mise 可以无缝替换 asdf，具有 asdf 所有功能。asdf 会自动加载当前目录下的 `.tool-versions` 文件。mise 则使用稍微复杂一些的 `toml` ，命令为 `.mise.toml`。

mise 一个工具就可以管理 Node.js, Ruby, Python, Flutter, Rust 等等非常多的语言和工具。

如果举一个具体的例子来说，比如你是一个 Python 开发者，如果你本地有多个需要维护的项目，但是这些项目是使用不同的 Python 版本来编写的，那么你可能需要类似 [pyenv](https://blog.einverne.info/post/2017/04/pyenv.html) 这样的工具来安装和维护本地的多个 Python 版本，并且在项目之间切换。而同样的如果你是 Node.js 开发者，你可能需要借助 nvm 这样的版本管理工具。很多语言和工具都会存在类似的工具，Flutter 有 fvm，Ruby 下有 rbenv ，那如果你同时会学习了解多种语言，那么既有可能你本地需要安装非常多的版本管理工具，但是如果你有了 mise ，那么 mise 一个工具就可以替换上面所有的 pyenv, rbenv, nvm, fvm 等等。

我之前介绍过的 asdf 也是类似的工具，但是 asdf 是完全使用 Shell 实现的，最近的更新是利用了 Go 语言进行了重写，但是使用上依然没有今天要介绍的 mise 快。

[Bilibili](https://www.bilibili.com/video/BV1NLRdYkEog/) [YouTube](https://www.youtube.com/watch?v=dxUytJAIA74)

## 功能

mise 完全可以代替 asdf：

* 官方支持多语言，包括 Bun, Deno, Erlang, Flutter, Go, Java, Maven, Python, Node, Ruby, Rust 等等
* 完全兼容 asdf 插件生态系统，通过插件支持更多开发工具
* 每个项目可以使用独立的运行时版本
* 自动切换对应的环境配置
* 支持 latest, lts 等版本标识
* 全局和项目级版本管理

## mise 相比于 asdf 的优势

mise 完全兼容 asdf 的 `.tool-version` 文件，也会默认加载。如果想要实现 mise 特有的功能，则可以切换成 `.mise.toml` 配置

### 自动化安装

在 asdf 下，如果用户切换到目录，发现没有安装对应的版本，asdf 需要用户手动通过 `asdf install` 来安装，而 mise 会自动进行安装。

### 传递选项

mise 可以通过 `.mise.toml` 配置文件工具传递选项。例如给 Python 传递虚拟环境。

```
[tools]
python = { version = '3.10', virtualenv = '.venv' }
```

配置文件

```
# .mise.toml 示例
[tools]
node = '18.12.0'
python = '3.10.0'

[env]
NODE_ENV = 'development'
```

## 安装

可以使用脚本一键安装 mise：

```
curl https://mise.run | sh
```

但是如果你是在 macOS 下，推荐使用

```
brew install mise
```

将 mise 添加到 Zsh Shell 中

```
echo 'eval "$(~/local/bin/mise activate zsh)"' >> ~/.zshrc
source ~/.zshrc
```

## 使用

安装完了之后，可以直接使用如下的命令来进行安装和使用。这里以 Python 为例。

比如安装对应的 Python 版本

```
# list all available python versions
mise ls-remote python
# install python
mise install [email protected]
```

插件管理

Node.js, Python 等都是内置插件（core plugin），不需要额外添加。

```
mise plugins list-all
mise plugins add flutter
mise plugins ls
mise plugins update
```

版本管理以及安装对应版本

```
# 列举所有可用版本
mise ls-remote node
mise ls-remote python

# 列举安装版本
mise ls node
mise ls python

# 安装版本
mise install [email protected]

mise use --global [email protected]
mise use [email protected]
mise use node@lts
```

环境变量

```
mise set NODE_ENV=development
mise settings
```

mise 是一个支持多语言多工具的版本管理器，主打**命令简单、速度快、功能集中**（如同时支持工具版本、环境变量、任务流管理）。常用 mise 命令总结：

| 命令 | 主要用途 |
| --- | --- |
| \*\*mise use <工具>@版本\*\* | 在当前目录启用指定工具及其版本。例：`mise use [[email protected]](/cdn-cgi/l/email-protection)` |
| **mise install** | 根据 `.mise.toml` 或兼容配置文件自动安装所需工具 |
| \*\*mise use <工具>@版本 -g/--global\*\* | 设置全局默认工具版本 |
| **mise list**/ **mise ls** | 列出已安装工具和版本 |
| \*\*mise list-remote <工具>\*\* | 查看某工具支持的全部可安装版本 |
| \*\*mise exec <命令>\*\* | 使用当前环境执行命令（等效于直接走当前 PATH 环境） |
| **mise env** | 显示当前生效的环境变量 |
| \*\*mise uninstall <工具>@版本\*\* | 卸载指定工具的特定版本 |
| **mise activate** | 激活 mise，为 shell 添加 PATH 等集成（首次安装需写入 shell rc 配置） |
| **mise plugins** | 显示已安装插件列表 |
| \*\*mise plugin add <工具>\*\* | 添加新插件 |
| **mise upgrade** / **mise self-update** | 升级 mise 本体 |
| **mise doctor** | 检查 mise 当前配置与环境问题 |
| \*\*mise task <任务名>\*\* | 运行配置在 `.mise.toml` 的任务流，如 `mise task build` |

mise 的命令体系比 [[asdf]] 更扁平易懂，日常主要用 use、install、list、exec、task 这几条为主。

## 以 Python 为例

上述一些命令介绍了 mise 的基础用法，现在以一个具体的例子，使用 mise 安装 Python 3.12.9 并配置本地使用，来介绍一下 mise 使用。

确保 mise 安装成功，并且在 Bash，Zsh 中配置

查看可安装的版本

```
mise ls-remote python
```

安装 Python

```
mise install [email protected]
```

安装完成之后可以通过 `mise list python` 来查看已经安装的版本。

如果要设置全局模式使用，可以

```
mise use -g [email protected]
```

如果只是想当前项目目录生效

```
mise use [email protected]
```

## 一些比较重要的文件夹

mise 会将插件和工具安装到 `~/.local/share/mise` 目录中。

`~/.local/share/mise/installs` 目录中存放所有已经安装好的工具。

## Related Posts

* [多版本管理工具 mise 使用详解](/post/2025/03/mise.html) - 03/02/2025
* [asdf 升级 0.16.0 问题记录](/post/2025/02/asdf-upgrade-0-16-0.html) - 02/11/2025
* [使用 uv 作为 Python 包和项目管理工具](/post/2025/02/python-uv-package-management.html) - 02/09/2025
* [Python 依赖管理工具 Poetry 使用笔记](/post/2022/01/poetry-python-dependency-management-notes.html) - 01/25/2022
* [使用 asdf-vm 管理编程语言多个版本](/post/2020/04/asdf-vm-manage-multiple-language.html) - 04/25/2020
* [pipenv 使用](/post/2018/01/pipenv-usage.html) - 01/23/2018
* [使用 pyenv 管理 Python 版本](/post/2017/04/pyenv.html) - 04/22/2017

---

* [← Previous（前一篇）](/post/2025/03/joplin-self-hosted-server.html "搭建 Joplin 同步服务器")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2025/03/open-webui-search.html "Open WebUI 基于网页的大语言交互界面及联网搜索配置")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2025/03/mise.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [mise 1](/tags.html#mise)
* [asdf 4](/tags.html#asdf)
* [multi-version 1](/tags.html#multi-version)
* [multi-platform 2](/tags.html#multi-platform)
* [python 77](/tags.html#python)
* [pyenv 7](/tags.html#pyenv)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").