---
title: Git 本地忽略文件：.git/info/exclude 的作用与使用技巧
url: https://blog.einverne.info/post/2026/10/git-info-exclude.html
source: Verne in GitHub
date: 2026-10-14
fetch_date: 2026-10-15T06:41:57.761496
---

# Git 本地忽略文件：.git/info/exclude 的作用与使用技巧

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

# Git 本地忽略文件：.git/info/exclude 的作用与使用技巧 不修改 .gitignore，也能让 Git 忽略只属于你自己的文件

Posted on 10/14/2026
, Last modified on 10/14/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-10-14-git-info-exclude.md)

由于本地 IDE、插件、Agent 的差异，所以经常打开项目之后会出现一些只属于我自己的文件，AI Agent 和一些 MCP，Skill 也喜欢在项目根目录里面添加文件。每次 `git status` 都能看到这一串红色的 untracked 文件，看着很烦，又不太好意思为了自己的习惯去改项目的 `.gitignore`。这时候我想起了 `.git` 目录里一个存在感极低的文件 `info/exclude`，它刚好就是为这种场景设计的。

![Git info exclude](https://pic.einverne.info/images/2026-10-14-17-30-00-git-info-exclude.png)

## 什么是 exclude 文件

每次执行 `git init` 或者 `git clone`，[[Git]] 都会根据模板目录在 `.git/info/` 下创建一个 `exclude` 文件。我之前在 [关于 .git 目录你需要知道的一切](https://blog.einverne.info/post/2020/02/everything-about-dot-git-directory.html) 里只用一句话带过了它，说它和 `.gitignore` 作用相同。这个说法没错，但其实漏掉了最关键的一点：`exclude` 位于 `.git` 目录内部，而 `.git` 目录本身是不会被提交和推送的，所以写在里面的规则只对当前这个本地仓库生效，不会影响任何其他协作者。打开一个新仓库的 `info/exclude`，默认内容只有几行注释：

```
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~
```

它的语法和 `.gitignore` 完全一致，支持 `*` 通配符、`**` 匹配任意层级目录、以 `/` 结尾表示只匹配目录、以 `!` 开头表示取反等规则。规则和 `.gitignore` 一样。

## 三个层级的忽略规则

Git 判断一个文件是否被忽略时，会从多个来源读取规则。理解这几个来源的分工，比记住某个文件的用法更有价值。按照官方文档，优先级从高到低依次是：

| 来源 | 位置 | 是否随仓库共享 | 适合放什么 |
| --- | --- | --- | --- |
| 命令行参数 | `--exclude` 等 | 否 | 临时性的一次性过滤 |
| `.gitignore` | 仓库内各级目录 | 是，会被提交 | 所有人都应该忽略的文件，如 `node_modules/`、`target/`、构建产物 |
| `info/exclude` | `.git/info/exclude` | 否，仅当前仓库 | 只和你自己在这个项目里的工作方式有关的文件 |
| 全局忽略文件 | `core.excludesFile`，默认 `~/.config/git/ignore` | 否，对本机所有仓库生效 | 和操作系统、编辑器相关的文件，如 `.DS_Store`、`.idea/` |

如果一个文件是项目本身会产生的，任何人 clone 下来编译都会遇到，就应该写进 `.gitignore` 提交上去；如果是我的电脑、我的编辑器在所有项目里都会产生的，比如 [[macOS]] 的 `.DS_Store`，就放到全局忽略文件里；剩下那些只跟”我在这个具体项目里的习惯”有关的文件，才是 `info/exclude` 的主场。这三层各管一摊，项目的 `.gitignore` 也就不会被每个人的个人偏好塞得乱七八糟。

## 优先级带来的一个细节

上面表格里的优先级不只是一个排列顺序，它会直接影响 `!` 取反规则的效果。Git 的规则是同一来源中后出现的匹配优先，不同来源中高优先级来源的匹配优先。我在本地用 Git 2.56 做了一个小实验：`.gitignore` 里写了 `*.log`，然后在 `info/exclude` 里写 `!a.log` 想把它”捞回来”，结果用 `git check-ignore -v` 一看，`a.log` 依然被 `.gitignore:1:*.log` 这条规则忽略，`info/exclude` 里的取反完全没起作用。

```
$ git check-ignore -v a.log
.gitignore:1:*.log	a.log
```

反过来就可以：`info/exclude` 里写 `*.txt`，`.gitignore` 里写 `!b.txt`，那么 `b.txt` 会重新出现在 `git status` 中。所以 `info/exclude` 只能”多忽略一些”，没法推翻项目 `.gitignore` 的决定。这其实挺合理的，本地个人规则本来就不应该和团队约定对着干，但如果你哪天发现某条取反规则不生效，可以先想想是不是写错了层级。

`git check-ignore -v` 这个命令非常值得记住，它会告诉你某个文件到底被哪个文件的第几行规则命中。当忽略规则分散在多个 `.gitignore`、`info/exclude` 和全局配置里的时候，靠肉眼排查非常痛苦，用这条命令几秒就能定位问题。

## 适合放进 exclude 的文件

结合自己平时的使用，下面这些是我经常往 `info/exclude` 里加的东西：

```
# 个人笔记和草稿
notes.md
TODO.local.md
scratch/

# 只在本地使用的调试脚本
debug.sh
*.local.sh

# 本地环境变量和工具配置
.envrc
.tool-versions

# AI 编程工具的本地文件
CLAUDE.local.md
.aider*
```

第一类是个人笔记和草稿。我习惯在项目根目录放一个 `notes.md`，记录排查问题的过程、待办事项或者 review 时的疑问，这些内容对其他人没有价值，但对我自己很重要，放在项目目录里随手就能打开。第二类是本地调试脚本，比如一个连着测试数据库跑某个接口的 shell 脚本，里面可能还写死了本地的端口和账号。第三类是像 [[direnv]] 的 `.envrc` 这类本地环境配置，团队里不一定每个人都用同样的工具，把它写进项目 `.gitignore` 反而显得多余。最后一类是这两年新增的需求，[[Claude Code]]、[[Aider]] 之类的 AI 编程工具会在项目里生成各种本地配置和记忆文件，如果项目没有统一约定，放在 `info/exclude` 里是最不打扰别人的做法。

编辑方式也很直接，用任何编辑器打开 `.git/info/exclude` 追加内容即可，或者直接用一行命令：

```
echo "notes.md" >> .git/info/exclude
```

需要注意，如果你在一个 submodule 里操作，它的 git 目录并不在 submodule 根目录下的 `.git` 文件夹，而是在父仓库的 `.git/modules/<name>/` 中，这时候用 `$(git rev-parse --git-dir)/info/exclude` 来定位会更保险。

## 在 worktree 中是共享的

我日常大量使用 [git worktree](https://blog.einverne.info/post/2019/03/git-worktree.html) 来同时处理多个分支，所以专门验证了一下 `info/exclude` 在 worktree 里的表现。结论是：所有 worktree 共享主仓库的 `info/exclude`。在主仓库的 `.git/info/exclude` 里写上 `notes.md`，然后新建一个 worktree，在里面创建同名文件，`git status` 同样不会显示它。这是因为 worktree 自己的 git 目录里只存放 `HEAD`、`index` 这类和工作区强相关的文件，而 `info/exclude` 位于通过 `git rev-parse --git-common-dir` 得到的公共目录中。

这个行为对我来说是好事，配置一次，所有 worktree 都生效，不用每开一个分支就重新写一遍。但也意味着你没办法给某一个 worktree 单独设置不同的本地忽略规则，如果真有这种需求，只能借助其他手段，比如在那个 worktree 的子目录里放一个不提交的 `.gitignore`，再把这个 `.gitignore` 本身写进 `info/exclude`。

## 对已跟踪的文件无效

这是使用 `exclude` 时最常见的误区，`.gitignore` 也有同样的问题：忽略规则只对 untracked 文件生效。如果一个文件已经被提交到仓库里，你再把它写进 `exclude`，Git 依然会跟踪它的修改，`git status` 照样会显示 `M`。我在实验仓库里提交了 `t.cfg`，再把它加进 `exclude` 并修改内容，`git status` 毫不客气地列出了它。

很多人想用 `exclude` 来解决”项目里有个配置文件，我本地要改，但不想提交”的问题，这种场景应该用的是另外两个命令：

```
# 告诉 Git 这个文件在本地会被修改，不要提交本地的改动
git update-index --skip-worktree config/application-local.yml

# 取消
git update-index --no-skip-worktree config/application-local.yml

# 查看哪些文件设置了 skip-worktree
git ls-files -v | grep '^S'
```

另一个经常被拿来对比的是 `--assume-unchanged`，它的设计初衷是性能优化，告诉 Git 不用去检查某个文件是否变化，在大仓库或者慢速文件系统上减少 `lstat` 调用。用它来隐藏本地修改虽然也能凑合，但语义不对，在某些操作下 Git 可能会重新检测并覆盖你的改动。如果目的是”保留本地修改不提交”，`--skip-worktree` 才是更合适的选择。当然，这两种方式在上游修改了同一个文件时都会让 `git pull` 报冲突，需要先取消标记再处理，这也是我更倾向于让项目提供 `xxx.example` 模板文件、真正的本地配置文件不入库的原因。

## 小心 git clean

最后提一个容易踩的坑。被 `info/exclude` 忽略的文件，在 Git 眼里就是普通的 ignored 文件，和 `node_modules/` 没有任何区别。如果你习惯用 `git clean -fdx` 或者 `git clean -fX` 来清理工作区，那么你的 `notes.md`、调试脚本也会被一并删除，而且这些文件从来没有被提交过，删了就真的找不回来了。

```
$ git status --short --ignored
!! a.log
!! notes.md

$ git clean -nX
Would remove a.log
Would remove notes.md
```

我的建议是执行 `git clean` 之前先加 `-n` 做一次 dry-run，看清楚会删哪些文件再动手。另外 `git clean` 支持 `-e` 参数临时添加排除规则，比如 `git clean -fdx -e notes.md` 可以在清理时保住这个文件。真正重要的笔记，最好还是放在项目目录之外，或者定期同步到自己的笔记系统里，别把 `exclude` 当成一个安全的存放位置，它只是让 Git 看不见这些文件，并不会保护它们。

## 最后

`.git/info/exclude` 是一个非常小的功能，小到很多用了多年 Git 的人都没注意过它，但它恰好填补了 `.gitignore` 和全局忽略文件之间的空白：既不污染团队共享的规则，又能精确到单个仓库。

理解了这三层忽略规则各自的定位之后，写忽略规则这件事就从”往 `.gitignore` 里一顿塞”变成了”想清楚这个文件属于谁”。再配合 `git check-ignore -v` 排查规则、`--skip-worktree` 处理已跟踪文件、`git clean -n` 做清理前的检查，日常和 Git 打交道时能少掉不少小麻烦。如果你也有一堆不想提交又懒得每次手动跳过的文件，不妨现在就打开 `.git/info/exclude` 试试。

## Related Posts

* [Git 本地忽略文件：.git/info/exclude 的作用与使用技巧](/post/2026/10/git-info-exclude.html) - 10/14/2026
* [Git 分支管理与发布上线流程实战指南](/post/2026/07/git-branch-management-and-release-workflow.html) - 07/03/2026
* [Entire：让 AI 编程会话成为 Git 历史的一部分](/post/2026/03/entire-git-ai-session-capture.html) - 03/18/2026
* [gitconfig includeIf 管理多用户配置](/post/2020/10/gitconfig-includeIf.html) - 10/18/2020
* [git subtree 简单使用记录](/post/2020/04/git-subtree-usage.html) - 04/29/2020
* [使用 Git worktree 将同一个项目分裂成多个本地目录](/post/2019/03/git-worktree.html) - 03/21/2019
* [使用 hub 命令来操作 GitHub](/post/2018/10/use-hub-command-to-interact-with-github.html) - 10/30/2018
* [使用 git bisect 来快速定位出错版本](/post/2018/04/git-bisect-to-locate-error-commit.html) - 04/12/2018
* [git 分支管理](/post/2018/04/git-branching.html) - 04/09/2018
* [使用 Phabricator 来 code review](/post/2018/03/phabricator.html) - 03/29/2018

---

* [← Previous（前一篇）](/post/2026/09/meta-muse-use-cases-tutorial.html "Meta Muse 使用教程：上手设置、提示词技巧与实用案例")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2026/10/ragflow-open-source-rag-engine.html "RAGFlow：以深度文档理解为核心的开源 RAG 引擎介绍与部署使用教程")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2026/10/git-info-exclude.html)评论。

* [学习笔记 516](/categories.html#学习笔记)

* [git 52](/tags.html#git)
* [gitignore 2](/tags.html#gitignore)
* [git-exclude 1](/tags.html#git-exclude)
* [version-control 11](/tags.html#version-control)
* [developer-tools 13](/tags.html#developer-tools)

---

© 2026 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's Git...