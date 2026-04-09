---
title: 利用 mise 替换 asdf 的迁移方案
url: https://blog.einverne.info/post/2026/04/migrate-from-asdf-to-mise.html
source: Verne in GitHub
date: 2026-04-08
fetch_date: 2026-04-09T04:30:05.046151
---

# 利用 mise 替换 asdf 的迁移方案

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

# 利用 mise 替换 asdf 的迁移方案 先复用 .tool-versions，再逐步切到 mise.toml，尽量不打断现有项目

Posted on 04/08/2026
, Last modified on 04/08/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-04-08-migrate-from-asdf-to-mise.md)

![利用 mise 替换 asdf 的迁移方案](https://pic.einverne.info/images/2026-04-08-mise-replace-asdf.png)

前面我分别写过[使用 asdf-vm 管理编程语言多个版本](https://blog.einverne.info/post/2020/04/asdf-vm-manage-multiple-language.html)和[多版本管理工具 mise 使用详解](https://blog.einverne.info/post/2025/03/mise.html)。那两篇更偏工具介绍，适合第一次认识 asdf 和 mise。但真轮到自己迁移的时候，最关心的通常不是概念，而是另外一个问题：我已经在机器上用 asdf 管了很多年的 Python、Node.js、Ruby，现在如果想换到 mise，到底该怎么换，才能既不打断当前工作，又不把已有项目折腾乱。

我自己这段时间重新梳理了一遍本地环境，最后得出的结论很简单：不要一上来就卸载 asdf，也不要先把所有仓库里的 `.tool-versions` 全部改成 `mise.toml`。最稳妥的路线，是先让 Shell 切到 mise，然后继续复用已有的 `.tool-versions` 文件，等核心项目都验证稳定之后，再决定哪些项目值得进一步切到 mise 自己的配置格式。这样做的好处是迁移成本非常低，基本不会影响你今天就要交付的代码和脚本。

## 为什么我现在更愿意用 mise

先说清楚一点，我并不是觉得 asdf 不能用了。尤其是 asdf 在 0.16.0 之后完成了 Go 重写，速度和维护性都比早年的 Bash 版本好很多，继续用完全没有问题。只是从我自己的日常体验来看，mise 在两个地方更合我胃口。

第一个地方是命令体系更扁平。以前在 asdf 里，安装插件、安装版本、写入本地版本，往往要分成好几步来做；而在 mise 里，很多常见动作可以直接收敛成一条 `mise use`。第二个地方是迁移成本确实低。官方文档明确提到 mise 可以直接读取 `.tool-versions`，也能通过 asdf backend 使用大量 asdf 插件。这意味着对于已经用 asdf 很久的人来说，mise 不是一套完全重新学习的新体系，而更像是在原有习惯上做一次更平滑的升级。

不过这里也有一个很重要的边界要提前讲明白：mise 虽然兼容 `.tool-versions`，但默认不会复用你 `~/.asdf` 下面已经安装好的版本目录。也就是说，迁移之后第一次执行 `mise install` 的时候，它很可能还是会重新下载一遍你常用的 Python、Node.js 或者别的工具。这一点如果事先没意识到，迁移时很容易产生“为什么又下载一次”的错觉。

## 迁移前先把边界想清楚

我建议在正式动手之前，先记住下面几件事情，这几件事情基本决定了整套迁移动作应该怎么做。

* mise 可以直接读取现有项目中的 `.tool-versions`，所以旧项目不一定要立刻改配置文件。
* mise 的 `install` 和 `use` 是两件事，前者偏向“下载到本地”，后者偏向“安装并写入当前配置”。
* mise 当前官方默认写入的是 `mise.toml`，如果你看过我之前那篇文章，里面大量出现的 `.mise.toml` 更像是早期习惯写法，迁移时最好跟当前官方默认保持一致。
* mise 可以自动安装缺失插件，而不是像早年使用 asdf 时那样，先 `plugin add` 再 `install` 再 `local`。
* 如果你今天还在用 asdf 旧版的 `global` 和 `local` 语法，那么迁移时也要顺便意识到：新版 asdf 本身都已经把这套命令改成了 `set`，所以你现在换成 mise，其实并不只是“从 asdf 换到另一个工具”，同时也是一次重新整理肌肉记忆的机会。

把这几件事情想清楚之后，迁移就会简单很多。因为你会发现自己真正要处理的，不是几十个项目配置文件，而是 Shell 初始化、版本安装目录和几条常用命令的替换。

## 先装 mise 再接管 shell

如果你在 macOS 上，按照当前官方文档，最省心的方式依然是通过 Homebrew 安装：

```
brew install mise
```

安装之后，我会直接把激活命令写进 `~/.zshrc`：

```
echo 'eval "$(mise activate zsh)"' >> "${ZDOTDIR-$HOME}/.zshrc"
source "${ZDOTDIR-$HOME}/.zshrc"
```

官方文档提到，某些安装方式下 Homebrew 可能会自动处理一部分激活逻辑，但我个人还是更喜欢显式写一行配置。原因很简单，环境问题通常都出在“我以为系统会帮我做这件事”，显式配置虽然土一点，但排查起来最省心。配置完成之后，先跑一遍 `mise doctor`，这一步能很快发现 PATH、Shell hook、插件解析之类的问题。

如果你之前在 `~/.zshrc` 或 `~/.bashrc` 里已经有 asdf 的初始化代码，这个时候可以把旧的加载逻辑删掉或者注释掉，只保留数据目录本身，不急着物理删除文件：

```
# 老 asdf 常见初始化方式
. "$HOME/.asdf/asdf.sh"
. /opt/homebrew/opt/asdf/libexec/asdf.sh
```

我不建议在第一天迁移时就把 `~/.asdf` 整个删掉。先让 Shell 只走 mise，确认几个核心项目都能正常跑，再决定要不要做后续清理，这样风险最低。

## 让老项目先继续吃 .tool-versions

这一步是我觉得整篇文章里最值钱的地方。很多人迁移工具时，总想把配置文件一并“升级”掉，但对已经稳定运行的项目来说，这通常不是最划算的选择。因为 mise 官方本来就支持 `.tool-versions`，所以最省事的方式其实是保持项目文件不动，直接进入项目目录运行：

```
cd your-project
mise install
```

如果当前目录里已经有 `.tool-versions`，mise 会按照里面声明的版本去安装对应工具。装完之后，再跑一遍你最关心的命令确认环境是否正确：

```
node -v
python -V
ruby -v
mise ls
```

只要这一步验证通过，说明这个项目已经基本被 mise 接管了，而你根本没有改动项目里的版本文件。对团队仓库来说，这个策略尤其友好，因为你不需要为了个人环境偏好去提交一堆和业务无关的配置变更。

## 把常用命令换成 mise 的写法

下面这张表，是我自己迁移时最常参考的一组命令映射。你不需要一口气全部记住，只要把最常用的几条先换过来，后面自然就顺手了。

| 场景 | asdf 常见写法 | mise 写法 |
| --- | --- | --- |
| 给当前项目安装并写入版本 | `asdf plugin add python` `asdf install python 3.12.9` `asdf set python 3.12.9` | `mise use [[email protected]](/cdn-cgi/l/email-protection)` |
| 只安装一个版本，不改当前项目配置 | `asdf install python 3.12.9` | `mise install [[email protected]](/cdn-cgi/l/email-protection)` |
| 设置用户级默认版本 | `asdf set --home python 3.12.9` | `mise use -g [[email protected]](/cdn-cgi/l/email-protection)` |
| 查看远程可安装版本 | `asdf list all python` | `mise ls-remote python` |
| 查看本地已经安装的版本 | `asdf list python` | `mise ls python` |
| 按项目配置批量安装 | `asdf install` | `mise install` |
| 安装缺失插件 | `asdf plugin add flutter` | `mise plugins install flutter` |
| 安装并切到某个 Node 版本 | `asdf plugin add nodejs` `asdf install nodejs 22.17.0` `asdf set nodejs 22.17.0` | `mise use [[email protected]](/cdn-cgi/l/email-protection)` |

如果你脑子里还保留着更老一代 asdf 的命令，比如 `asdf local` 和 `asdf global`，也不用担心。你完全可以把它们分别理解成 `mise use` 和 `mise use -g`。迁移过程中最重要的不是百分百对应每个历史语法，而是抓住 mise 的核心思路：尽量用更少的命令，把“安装”和“声明当前项目该用哪个版本”这两件事情一次做完。

还有一个我觉得很容易踩坑的点，是工具命名不一定一一对应。比如你在 asdf 里常用的是 `nodejs` 插件名，到了 mise 里通常会写成 `node`。所以如果你直接照着旧习惯把插件名照搬过来，偶尔会遇到名字不一样的情况。遇到这种问题时，直接用 `mise search` 或者去查官方 registry，比硬猜更省时间。

## 什么时候再切到 mise.toml

等你确认 mise 已经稳定接管了日常开发环境，这时再来考虑要不要把某些项目从 `.tool-versions` 切到 `mise.toml`。我自己的建议是，不要为了“新”而切，而是等你真正需要 mise 独有能力的时候再切，比如环境变量、任务定义、工具选项或者多 backend 支持。

举个非常典型的例子，如果一个项目除了版本管理之外，还希望顺手把环境变量和常用命令也集中在一起，那 `mise.toml` 的价值就出来了：

```
[tools]
node = "22"
python = { version = "3.12", virtualenv = ".venv" }
pnpm = "10"

[env]
NODE_ENV = "development"

[tasks.dev]
run = "pnpm dev"
```

这种写法和 `.tool-versions` 最大的区别，不只是文件格式从纯文本换成了 TOML，而是它开始承担更多“项目开发入口”的角色。你可以在一个文件里声明运行时版本、环境变量、虚拟环境、任务命令，团队协作时也会更直观。

不过对已经运行很多年的老项目，我依然建议保守一点。哪怕你最后决定切换，也最好先在一个项目里试，再逐步推广，而不是一口气改完整个工作目录。工具迁移最怕的不是技术上做不到，而是一次改动范围过大，最后谁都说不清到底是哪一处变更引入了问题。

## 我自己的迁移建议

如果让我把这次迁移经验压缩成几条最实用的建议，我会这样做。

* 先安装 mise 并接管 Shell，不要一开始就删 asdf 数据目录。
* 先让旧项目继续使用 `.tool-versions`，只用 `mise install` 验证兼容性。
* 先把最常用的几条命令换过来，尤其是 `mise use`、`mise install`、`mise ls-remote` 和 `mise ls`。
* 只有当项目确实需要环境变量、任务流、虚拟环境这些扩展能力时，再切到 `mise.toml`。
* 真正确认迁移完成之后，再考虑清理 `~/.asdf` 里的历史数据，不要把清理动作放在验证之前。

这套顺序看起来有点慢，但对真实项目环境来说，这恰恰是最快的。因为它把“迁移工具”这件事拆成了很多个可以随时停下来的小步骤，每一步都能验证，每一步失败了也都容易回退。

## 最后

如果你已经用了很多年 asdf，那你大概率和我一样，并不缺一个“更强”的工具介绍，你缺的是一套迁移时不伤筋动骨的实践方案。mise 最吸引我的地方，不是它一定比 asdf 快多少，而是它给了我一种更轻的维护方式：新项目可以直接用一条命令起步，老项目又不用被迫马上重写版本文件，这种兼容和渐进式迁移的体验，才是真正让我决定换过去的原因。

所以我的建议非常直接：先把 Shell 切过来，让旧项目继续跑 `.tool-versions`，把常用命令慢慢换成 `mise` 的写法，最后再决定哪些项目值得升级到 `mise.toml`。如果你照这个顺序做，整个替换过程会比想象中平滑得多，而且几乎不会影响你现有的开发节奏。

## Related Posts

* [利用 mise 替换 asdf 的迁移方案](/post/2026/04/migrate-from-asdf-to-mise.html) - 04/08/2026
* [Atuin：用数据库替换 Shell 历史，跨设备同步不再是难题](/post/2026/03/atuin-shell-history-sync.html) - 03/18/2026
* [多版本管理工具 mise 使用详解](/post/2025/03/mise.html) - 03/02/2025

---

* [← Previous（前一篇）](/post/2026/04/field-theory-cli-x-bookmarks-local-sync.html "Field Theory CLI：把 X Bookmarks 同步到本地，变成可搜索的个人知识库")
* [Archive（目录）](/archive.html)
* Next（后一篇） →

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2026/04/migrate-from-asdf-to-mise.html)评论。

* [经验总结 594](/categories.html#经验总结)

* [mise 2](/tags.html#mise)
* [asdf 5](/tags.html#asdf)
* [version-manager 1](/tags.html#version-manager)
* [shell 21](/tags.html#shell)
* [developer-tools 4](/tags.html#developer-tools)
* [productivity 12](/tags.html#productivity)

---

© 2026 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").