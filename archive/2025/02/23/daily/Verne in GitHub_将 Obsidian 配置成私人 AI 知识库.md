---
title: 将 Obsidian 配置成私人 AI 知识库
url: https://blog.einverne.info/post/2025/02/obsidian-personal-ai-knowledge-base.html
source: Verne in GitHub
date: 2025-02-23
fetch_date: 2025-10-06T20:32:35.517535
---

# 将 Obsidian 配置成私人 AI 知识库

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

# 将 Obsidian 配置成私人 AI 知识库

Posted on 02/22/2025
, Last modified on 02/22/2025
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2025-02-22-obsidian-personal-ai-knowledge-base.md)

前两天介绍过腾讯推出的个人知识库工具 IMA.Copilot，但是熟悉我的人肯定知道我这几年了一直都是在使用 Obsidian 作为我个人的知识库的，在本地完全使用 Markdown 作为文档的存储格式，不依赖任何的外部工具，以及联网工具，只使用 Syncthing 作为同步。

## 为什么我不使用 IMA 作为主力知识库

看过我之前文章的人应该知道我个人的选择软件工具的一个原则

* 跨平台
* 开源优先
* 本地优先

在了解到 Stallman 对[[自由软件]]的定义之后，更进一步加强了我对于开源软件的选择，而在重度理解 Self-Hosted，以及重度使用 Obsidian 之后更加深了我对本地优先（Local First）的选择。选择开源是可以让我使用的更久，尤其是在经历了过去那么多倒掉的平台，关闭的服务，那些会产生我自己数据的服务，比如说笔记，博客，我更不想依托于任何一个平台，开源才能让我自己使用地更长久。而本地优先则更是为了保护自己的数据，以纯文本的方式保存我自己产生的数据，再也不需要担心没有网络访问不到自己的数据，再也不用担心因为封号造成数据丢失，再也不用担心任何平台对自己的文字图片有任何的审查，当然前提是自己需要对自己的数据负责，比如我会至少三地备份我的主要内容。

如果以我的标准去衡量 IMA，那么 IMA 最多只能占到跨平台这一个优点，IMA 软件没有任何开放接口也不支持任何的数据导出，更不用说本地优先，所有的文档都需要上传到其云端才能完成其解析。所以 IMA 我是不会拿来作为主力产品来使用的。

## 如何配置

那么这篇文章就介绍我如何将我的 Obsidian 配置成我自己的个人知识库。

需要如下的几个插件：

* GitHub Copilot ，给 Obsidian 增加自动补全功能
  + 集成 GitHub Copilot
  + 智能自动不全
  + 代码和文本生成
* Smart Composer 给 Obsidian 增加侧边栏对话框
  + 类似 Cursor 侧边栏对话框
  + 支持多种 AI 模型
  + 直接将生成的内容应用文档
* Text Generator，内容生成，总结，简化，生成点子
  + 支持多个 AI 模型
  + 可进行文本生成，总结，改写，翻译任务
  + 支持自定义提示词模板
  + 分析上下文
* Smart Connections，自动分析笔记的关联度，建立相关笔记（可选）
  + 自动分析笔记相似度
  + 建立本地笔记关联
  + 本地向量搜索

## 必要的插件配置

### GitHub Copilot 插件

GitHub Copilot 插件将 GitHub Copilot 的能力直接带到了 Obsidian 中，让你可以在 Obsidian 中直接调用 Copilot 的 AI 功能，让 Copilot 为你生成文本。

因为这个插件使用的 Copilot 的服务，所以需要自己开通 GitHub Copilot 服务。

![AxzjbduKal](https://pic.einverne.info/images/AxzjbduKal.png)

### Smart Composer

Smart Composer 是一个支持多种模型的只能生成工具，在侧边栏会产生一个 Cursor 类似的对话框，用户可以在不离开 Obsidian 的情况下和多个 AI 模型对话，也可以将 AI 生成的内容作为文章的补充直接应用到文章中。

![XyvqkpD41s](https://pic.einverne.info/images/XyvqkpD41s.png)

### Text Generator

Text Generator 是一个支持多种 AI 模型的文本生成工具，可以进行文本生成，总结，改写，翻译等任务，支持自定义提示词模板，分析上下文。

![gvnpYNOzZ8](https://pic.einverne.info/images/gvnpYNOzZ8.png)

安装完成上述的插件之后，在设置中配置好 API Key，就可以进入到 Obsidian，开始使用 AI 来辅助了。

## 使用

我经常使用的几种模式

* 自动补全
* 自动文本生成
* 侧边栏提问

### 自动补全

类似代码补全，在编写的过程中，会自动补全后面文字，然后使用 Tab 就可以直接将 Copilot 生成的内容插入到文档中。

![557otqPvZ7](https://pic.einverne.info/images/557otqPvZ7.png)

### 自动文本生成

如果编写内容的时候希望 AI 根据上下文内容自动往后编写，可以使用 Cmd + P 快捷键，然后输入 `Text Generator`，就可以让 AI 根据上下文生成内容。我给这个模式设置了一个快捷键 Cmd + J，那么这个时候，无论我在文档的哪个部分都可以直接按下 Cmd + J，让 AI 自动帮我往后编写。

但是我自己实测 Text Generator 补全的内容很多情况不是很理想。

### 侧边栏提问

在侧边栏输入问题，然后点击回车，就可以让 AI 回答你的问题，这个模式类似于 Cursor 的侧边栏对话框。

## 简单的模式

使用 [Cursor](https://blog.einverne.info/post/2023/03/ai-powered-editor-cursor-so.html) 或 [Windsurf](https://blog.einverne.info/post/2024/11/windsurf.html) 或者 [Trae](https://blog.einverne.info/post/2025/01/trae-ide-from-bytedance.html) 直接打开 Obsidian Vault 仓库，虽然它们是代码编辑器，但是没说只能用它们来编辑代码呀。

## Related Posts

* [Google Gemini CLI 使用初体验：命令行上的 AI 工作流引擎](/post/2025/06/google-gemini-cli.html) - 06/26/2025
* [AI 时代我们是否还需要个人知识库](/post/2025/02/do-we-need-knowledge-base-in-ai-era.html) - 02/26/2025
* [将 Obsidian 配置成私人 AI 知识库](/post/2025/02/obsidian-personal-ai-knowledge-base.html) - 02/22/2025
* [腾讯推出个人知识库产品 ima.copilot](/post/2025/02/tencent-ima-copilot.html) - 02/20/2025
* [Dinox 又一款 AI 语音转录笔记](/post/2024/07/dinox-voice-memo.html) - 07/26/2024
* [让 AI 无处不在](/post/2023/07/ai-everywhere-in-daily-life.html) - 07/13/2023

---

* [← Previous（前一篇）](/post/2025/02/tencent-ima-copilot.html "腾讯推出个人知识库产品 ima.copilot")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2025/02/obs-multiple-rtmp-setup.html "OBS 配置多路推流 实现多平台同时直播")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2025/02/obsidian-personal-ai-knowledge-base.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [obsidian 21](/tags.html#obsidian)
* [copilot 4](/tags.html#copilot)
* [ai 45](/tags.html#ai)
* [ai-agent 5](/tags.html#ai-agent)
* [knowledge-base 2](/tags.html#knowledge-base)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").