---
title: Surfingkeys：比 Vimium 更强大的浏览器键盘控制扩展
url: https://blog.einverne.info/post/2026/06/surfingkeys-chrome-extension.html
source: Verne in GitHub
date: 2026-06-02
fetch_date: 2026-06-03T06:45:19.722106
---

# Surfingkeys：比 Vimium 更强大的浏览器键盘控制扩展

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

# Surfingkeys：比 Vimium 更强大的浏览器键盘控制扩展 让双手不离键盘，用 Vim 的方式掌控浏览器

Posted on 06/02/2026
, Last modified on 06/02/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-06-02-surfingkeys-chrome-extension.md)

最早接触 [[Vimium]] 是在学习 Vim 编辑器之后，那种能用键盘完全控制浏览器的感觉确实让人着迷。不用频繁移手到鼠标，链接跳转、页面滚动、标签切换全用键盘搞定，效率提升的体验是实实在在的。用了几年 Vimium 之后，我开始接触到 [[Surfingkeys]]，起初以为不过是另一个同类扩展，但深入用下来才发现这两者的差距远比我想象的大。

![Surfingkeys 键盘控制浏览器](https://pic.einverne.info/images/2026-06-02-10-00-00-surfingkeys-cover.png)

## 为什么要用键盘控制浏览器

对于长期使用 [[Vim]] 的人来说，键盘操作的肌肉记忆已经根深蒂固。在编辑器里习惯了 hjkl 导航，切换到浏览器还要去抓鼠标总觉得很割裂。更重要的是，对于程序员、研究者或者任何需要长时间使用浏览器查阅资料的人，频繁移手到鼠标会带来明显的效率损失，甚至是手腕疲劳。

Vimium 在这个领域确立了基础范式：用 `f` 键激活链接提示、`hjkl` 滚动页面、`J`/`K` 切换标签页、`o`/`O` 打开链接等等。这套设计简洁而高效，是很多 Vim 用户的第一个浏览器键盘扩展。不过，随着使用深入，你会发现 Vimium 的局限性也相当明显：配置能力有限、不支持自定义 JavaScript、在某些页面上会失效、搜索功能比较基础。这时候 Surfingkeys 就显示出它的价值了。

## Surfingkeys 是什么

Surfingkeys 是一款同样基于 Vim 键位设计理念的浏览器扩展，支持 Chrome、Firefox 和 Safari。它的作者从 2015 年开始开发，目前仍在持续维护更新，在 GitHub 上有超过 13000 个星标。和 Vimium 相比，Surfingkeys 走的是功能更丰富、可定制性更强的路线，可以把它理解为浏览器键盘控制领域的”Neovim”，而 Vimium 则更像是轻量的”原版 Vim”。

核心上，两者都提供了类似的基础操作：用字母键激活页面上的链接、键盘滚动页面、标签页管理等。但 Surfingkeys 在这个基础上走得更远——它允许用户直接用 JavaScript 编写自定义快捷键逻辑，内置了一个独立的 Vim 编辑模式，甚至有自己的 PDF 查看支持和多引擎搜索系统。

## 与 Vimium 的核心差异

### 配置的深度

Vimium 的配置主要通过它的设置页面完成，支持自定义搜索引擎和重新映射键位，但能做的事情相对有限。Surfingkeys 则提供了一个完整的 JavaScript 配置接口，你可以在配置文件里写任意 JS 代码来定义行为。这意味着你可以创建复杂的按键序列，根据当前网站动态调整键位，甚至调用浏览器 API 做更高级的操作。

举个实际例子：我在 Surfingkeys 的配置里写了几个针对特定网站的快捷键，比如在 [[GitHub]] 上快速跳到文件树、在 Twitter/X 上快速点赞等。这种程度的定制在 Vimium 里根本无法实现。

### 内置 Vim 编辑器

Surfingkeys 有一个非常实用的功能：在任何网页的文本输入框里，按 `Ctrl+i` 可以弹出一个内置的 [[CodeMirror]] 编辑器，用完整的 Vim 模式来编写文本。这对于需要在网页上写长文本的人来说非常有价值。写评论、填表单、甚至在 GitHub 上编辑文件，都可以在这个编辑器里用 Vim 操作完成。Vimium 完全不提供这个功能。

### 多引擎搜索系统

按 `o` 或 `O` 调出 Surfingkeys 的搜索栏之后，你可以在多个搜索引擎之间快速切换。配置文件里可以添加任意数量的搜索引擎，每个都绑定一个短前缀。比如输入 `g 关键词` 用 [[Google]] 搜索，输入 `y 关键词` 在 [[YouTube]] 搜索，输入 `gh 关键词` 在 GitHub 搜索。这个系统比 Vimium 的搜索引擎支持灵活得多，而且不需要每次都切换默认搜索引擎。

### 视觉模式与文本选择

Surfingkeys 实现了比 Vimium 更完整的视觉模式，按 `v` 进入视觉模式后，可以用 Vim 的文本对象（如 `w`、`e`、`b`）来精确选择文字，然后按 `y` 复制。在需要精确复制页面文字的场景里，这个功能非常好用，比手动拖选鼠标准确得多。

### 对 PDF 的支持

Vimium 在 PDF 页面基本无效，而 Surfingkeys 对 PDF 有原生支持，可以用键盘翻页、搜索内容、跳转页码。这对于经常阅读 PDF 文档的用户来说是个实实在在的优势。

## 实际使用体验与配置建议

上手 Surfingkeys 的第一步建议先用默认配置熟悉两周。它的默认键位和 Vimium 有不少重合，但也有差异，比如链接提示默认用 `f` 激活（跟 Vimium 相同），但标签页切换是 `E`/`R`（Vimium 是 `J`/`K`）。这些差异需要时间适应。

配置文件可以直接在扩展设置页面里编辑，格式是纯 JavaScript。官方文档有完整的 API 说明，常用的配置项包括：

* `api.map('newKey', 'oldKey')` — 重新映射键位
* `api.mapkey('key', 'description', function() { ... })` — 创建新的自定义快捷键
* `api.addSearchAlias('prefix', 'name', 'searchUrl')` — 添加搜索引擎

有一点要注意：Surfingkeys 的键位激活逻辑偶尔会和某些单页应用的前端框架产生冲突，导致在某些网站的特定输入场景下快捷键失灵。这时候可以通过配置 `sites` 白名单或黑名单来处理。Vimium 也有类似问题，不过因为功能更简单，冲突概率相对低一些。

另外，如果你是从 Vimium 迁移过来的，可以在社区里找别人分享的仿 Vimium 配置，先让键位基本一致，然后再逐步加入 Surfingkeys 独有的功能。这样迁移成本会低很多，不用一次性重新学习所有键位。

## 最后

用了 Vimium 几年再换到 Surfingkeys，感受最直接的提升是配置自由度带来的效率改善。Vimium 是一个非常好的入门工具，设计简洁、开箱即用、学习曲线低，对于刚开始探索键盘操控浏览器的人来说是更好的起点。但如果你已经把 Vimium 用熟了，想要更深度的定制、更强大的文本操作、或者让浏览器键盘体验更接近真实的 Vim 工作流，Surfingkeys 是值得花时间迁移的选择。

两者的核心差异不在于基础功能的好坏，而在于你愿意投入多少时间去配置和适应。Vimium 的 80% 功能几乎零配置就能用上，Surfingkeys 的 100% 功能需要你真正去读文档、写配置。如果你是那种会去给 Vim 写几百行配置的人，Surfingkeys 会让你觉得非常顺手。

## Related Posts

* [Surfingkeys：比 Vimium 更强大的浏览器键盘控制扩展](/post/2026/06/surfingkeys-chrome-extension.html) - 06/02/2026
* [Vimium 教程：使用键盘来浏览网页](/post/2023/10/vimium-chrome-extension.html) - 10/11/2023

---

* [← Previous（前一篇）](/post/2026/05/introducing-denote-emacs-notes.html "Denote 介绍 Emacs 下基于文件名的笔记系统")
* [Archive（目录）](/archive.html)
* Next（后一篇） →

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2026/06/surfingkeys-chrome-extension.html)评论。

* [经验总结 598](/categories.html#经验总结)

* [chrome-extension 11](/tags.html#chrome-extension)
* [vim 44](/tags.html#vim)
* [keyboard 7](/tags.html#keyboard)
* [browser 8](/tags.html#browser)
* [productivity 16](/tags.html#productivity)
* [surfingkeys 1](/tags.html#surfingkeys)

---

© 2026 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").