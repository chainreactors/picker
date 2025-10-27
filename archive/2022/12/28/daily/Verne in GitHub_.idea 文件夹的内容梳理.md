---
title: .idea 文件夹的内容梳理
url: https://einverne.github.io/post/2022/12/behind-the-hidden-idea-folder.html
source: Verne in GitHub
date: 2022-12-28
fetch_date: 2025-10-04T02:35:37.676793
---

# .idea 文件夹的内容梳理

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

# .idea 文件夹的内容梳理

Posted on 12/27/2022
, Last modified on 12/28/2022
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2022-12-27-behind-the-hidden-idea-folder.md)

使用 JetBrains 旗下的 IDE 创建项目都会在项目的根目录中自带一个隐藏的 `.idea` 文件夹，每一次遇到这个文件夹的时候都会犹豫一下是否需要下面的内容全部放入到 `.gitignore` 文件中，大部分的时候就直接全部忽略了。现在想过来再了解一下这个文件夹下的每个文件都代表什么内容，因为有一些数据库配置，还有一些插件的临时信息都会存放在这个目录下。

`.idea` 文件夹存放的内容都是 JetBrains 旗下的 IDE，比如 IntelliJ 等等项目独有的配置文件。这些文件包括项目独有的 VCS mapping 或运行或调试的配置文件，还有一些用户操作相关的文件，比如用户当前打开的文件，浏览历史记录，当前的配置等。

文件夹：

* `codeStyles` 文件夹，包含项目所使用的代码风格
* `dictionaries` 文件夹包含用户自定义的词典，IDE 用来检查单词拼写的时候会引用，文件下的内容以用户分隔，不应该提交版本控制，除非明确知道自己想做什么
* `dataSources` 文件夹，数据库连接信息，不应该提交版本控制
* `libraries` 文件夹，包含一系列的 XML 文件，不应该提交到版本控制，这些文件会从项目中自动生成

文件：

* `dataSources.xml` 包含 IDE 中使用 Database 的数据库连接信息
* `encodings.xml` 项目编码
* `vcs.xml` 文件用来记录 VCS 相关的内部信息，启用了哪一个 VCS
* `indexLayout.xml` 该文件是用来记录项目外包括的文件夹的。这些文件夹可以通过 `Attach Existing Folder...` 来加入
* `modules.xml` 基于 Gradle 或 Maven 的项目生成的信息，可以被排除，会在导入的时候自动生成
* `vcs.xml` 文件用来记录 VCS 相关的内部信息，启用了哪一个 VCS
* `runConfigurations` 文件夹是用来存储 [shared run configurations](https://www.jetbrains.com/help/rider/Run_Debug_Configurations_dialog.html#run_config_common_options) 的。
* `indexLayout.xml` 该文件是用来记录项目外包括的文件夹的。这些文件夹可以通过 `Attach Existing Folder...` 来加入

有一些文件应该被提交到版本控制中，而有一些是需要被排除的。个人的习惯是直接排除掉 `.idea` 整个目录，貌似到目前为止还没有产生任何问题。

## gitignore

如果不知道要在 gitignore 中填写什么什么，我一般会用如下的方式自动产生 `.gitignore`:

* 使用 IDE 自带的功能，在项目上右击，选择 New -> `.ignore File` ->`.gitignore` 文件，然后会弹出选框，选择自己的系统，语言，IDE 就会自动产生
* <https://www.gitignore.io/> 在网站中根据自己的需要，输入系统，编程语言，IDE 等等，然后会自动生成一段 `.gitignore`，复制粘贴即可

## reference

* <https://intellij-support.jetbrains.com/hc/en-us/articles/206544839>
* <https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore>

## Related Posts

* [.idea 文件夹的内容梳理](/post/2022/12/behind-the-hidden-idea-folder.html) - 12/27/2022
* [我的 IntelliJ IDEA Vim 插件配置](/post/2020/12/my-idea-vimrc-config.html) - 12/02/2020
* [IntelliJ IDEA vmoptions 设置](/post/2020/04/idea-vmoptions-setup.html) - 04/03/2020

---

* [← Previous（前一篇）](/post/2022/12/java-11-new-feature.html "Java 11 新特性学习")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2022/12/reading-in-year-2022.html "2022 年读书笔记")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2022/12/behind-the-hidden-idea-folder.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [学习笔记 496](/categories.html#学习笔记)

* [idea 5](/tags.html#idea)
* [jetbrain 5](/tags.html#jetbrain)
* [dotfiles 2](/tags.html#dotfiles)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").