---
title: Mastodon 站点管理：导入自定义表情包
url: https://einverne.github.io/post/2022/11/mastodon-custom-emoji.html
source: Verne in GitHub
date: 2022-11-15
fetch_date: 2025-10-03T22:43:52.726620
---

# Mastodon 站点管理：导入自定义表情包

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

# Mastodon 站点管理：导入自定义表情包

Posted on 11/14/2022
, Last modified on 11/14/2022
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2022-11-14-mastodon-custom-emoji.md)

[[Mastodon]] 实例可以允许站点管理员自定义整站上的表情包，管理的地址在 **首选项-管理（Administration）-自定义表情（custom emojis）** ， 具体的页面地址是 `https://instance.domain/admin/custom_emojis`。

下面介绍几种方式来管理 Mastodon 实例上的表情。

## 手动上传 Emoji

如果有自制的表情，可以通过上传的方式导入。

请右上角**上传新表情**，格式必须为 png，文件大小不能超过 50KB。

## 手动拷贝他站表情

如果使用了 [[mastodon-relay-servers|Mastodon 中继站]]，那么经过一段时间的使用会导入一些其他站点的表情，在站点管理中能看到。Mastodon 允许将其他站点的标签复制到本站点。

* 点击“远程”，勾选想要的表情
* 点击右侧“复制”，即可复制至你站，可以在“本站”中见到

在“本站”一栏可以进行表情分类。

## 批量下载并导入

Mastodon 的 `tootctl` 提供了导入 Emoji 的相关命令，那么其实只要准备好表情包，然后通过 `tootctl` 命令导入即可。

这里就要使用一个开源的脚本，可以从其他网站批量下载 [表情](https://github.com/Starainrt/emojidownloader/)。

脚本的原理就是利用 Mastodon 的 [Emoji API](https://docs.joinmastodon.org/methods/instance/custom_emojis/)。

如何预览一个站点的所有表情呢，有一个在线网站 <https://emojos.in/> ，可进行表情包预览（对未开启 authorized\_fetch 的站点有效）。

顺便输入一个 Mastodon 实例的地址，得到：

* <https://emojos.in/masto.ai>

然后执行脚本：

* 到项目的 [release](https://github.com/Starainrt/emojidownloader/releases) 下载最新发布的二进制可执行文件，右键复制下载地址。
* 在服务器执行：

```
wget https://github.com/Starainrt/emojidownloader/releases/download/v0.1.0/emoji_downloader_linux_x86_64
chmod +x ./emoji_downloader_linux_x86_64
./emoji_downloader_linux_x86_64
```

运行程序，根据提示下载。可以自行选择需要下载对方站哪一种表情包分类，对表情包命名有无批量改动。（注意：如果对方站开启了 authorized\_fetch 模式，则需要拥有对方站账号。)

最后会下载一个格式为 `.tar.gz` 的压缩包，里面包括了选择的所有表情。

* 然后进入 docker 容器，导入表情：

```
docker cp ./表情路径 mastodon-web-1:/tmp/表情名字.tar.gz
docker exec -it mastodon-web-1 /bin/bash
tootctl emoji import --category 你设定的分类 文件路径/文件名
```

然后刷新页面，在 LOCAL 管理页面就能看到导入的表情了。

## Emoji 使用

在站点发送 Toot 的右上角 Emoji 选择器就可以选择表情使用。或者直接输入对应的表情编码即可。

最后欢迎大家来使用：<https://m.einverne.info>

## Related Posts

* [使用 mastodon tootctl 管理 Mastodon 实例](/post/2022/11/mastodon-tootctl.html) - 11/14/2022
* [Mastodon 站点管理：导入自定义表情包](/post/2022/11/mastodon-custom-emoji.html) - 11/14/2022
* [使用 Docker 安装 Mastodon 实例搭建自己的社交网络](/post/2022/04/install-mastodon-by-docker.html) - 04/21/2022

---

* [← Previous（前一篇）](/post/2022/11/pipedream-usage.html "在线工作流 Pipedream 使用记录")
* [Archive（目录）](/archive.html)
* [Next（后一篇） →](/post/2022/11/mastodon-tootctl.html "使用 mastodon tootctl 管理 Mastodon 实例")

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2022/11/mastodon-custom-emoji.html)评论。

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)
[blog comments powered by Disqus](https://disqus.com)

* [经验总结 560](/categories.html#经验总结)

* [mastodon 6](/tags.html#mastodon)
* [sns 2](/tags.html#sns)
* [twitter 4](/tags.html#twitter)
* [emoji 2](/tags.html#emoji)
* [tootctl 2](/tags.html#tootctl)

---

© 2025 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](http://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").