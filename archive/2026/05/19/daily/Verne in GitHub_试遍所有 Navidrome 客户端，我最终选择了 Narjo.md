---
title: 试遍所有 Navidrome 客户端，我最终选择了 Narjo
url: https://blog.einverne.info/post/2026/05/narjo-music-player-review.html
source: Verne in GitHub
date: 2026-05-19
fetch_date: 2026-05-20T05:58:35.563153
---

# 试遍所有 Navidrome 客户端，我最终选择了 Narjo

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

# 试遍所有 Navidrome 客户端，我最终选择了 Narjo 最好用的 iOS Navidrome 播放器

Posted on 05/19/2026
, Last modified on 05/19/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-05-19-narjo-music-player-review.md)

我是一个对音乐播放体验有点执念的人。自从搭建了 [[Navidrome]] 自托管音乐服务器，我就开始了一段漫长的客户端寻觅之旅。在 iOS 上，我几乎把能找到的 [[Navidrome]] 客户端都试了一遍，甚至为了体验更好而付费购买了 [[音流]]。但最终，我还是删掉了它们，把 [[Narjo]] 固定在了屏幕上。

![Narjo 音乐播放器界面](https://pic.einverne.info/images/2026-05-19-14-00-00-narjo-music-player.png)

## 自托管音乐服务器的现状

在流媒体服务大行其道的今天，还在折腾自建音乐库的人，往往有些相似的执念：想要拥有自己的音乐，不依赖平台，不受版权下架的困扰，或者单纯就是喜欢把喜欢的 FLAC 文件存放在自己的硬盘上。[[Navidrome]] 就是这样一个开源的自托管音乐服务器，轻量、稳定，支持 Subsonic API，所以理论上所有兼容 Subsonic 的客户端都可以连接它。

问题在于，”兼容”只是入场门票，而体验才是核心。iOS 上能用的 Navidrome 客户端并不少，但真正做到让人用得顺手的寥寥无几。大多数客户端要么界面陈旧，停留在十年前的设计语言里；要么功能堆砌，导航逻辑混乱；还有一些干脆就是把 Web 界面套了个壳，交互完全不像一个原生 iOS 应用该有的感觉。

## 试用之路：从免费到付费

在我的寻觅过程中，[[Amperfy]] 是我第一个认真使用的客户端。它功能完整，支持离线缓存，也有基本的播放控制，作为一个免费的开源项目，确实值得称道。但它的界面让我觉得有些拥挤，信息层级不够清晰，切换专辑和浏览曲库的流程不够顺滑。[[Substreamer]] 的情况类似，功能可以用，但交互逻辑让我时不时需要多按几次才能找到想要的东西。

后来，我入手了[音流](https://blog.einverne.info/post/2024/07/stream-music-navidrom-subsonic.html)。作为一款专门面向中国用户的 Navidrome iOS 客户端，它在本地化和 UI 打磨上明显花了心思。首次打开时，它的界面确实漂亮，对齐感强，颜色搭配也舒服。我用它有一段时间，也觉得够用。但用着用着，我开始注意到一些小摩擦：某些操作需要多一步确认，某些列表加载有时显得不够流畅，以及一些我说不清楚的”不对劲”——就是那种打开 App 之后，感觉操作动线与自己的直觉有微妙偏差的感受。

就在这个阶段，我发现了 [[Narjo]]。

## Narjo 的第一印象

打开 Narjo 的第一眼，我就感觉到有些不一样。它的界面用的是深色主题，专辑封面被放大展示，字体选择和排版间距都是那种”照顾过的”状态，不是为了塞更多信息而牺牲视觉呼吸感。最重要的是，常用操作都在拇指能自然触达的区域，这是很多音乐播放器容易忽视的细节。

Narjo 对 iOS 生态的集成让我印象深刻。它支持锁屏小组件，可以在桌面直接看到当前播放的曲目；支持 CarPlay，开车时不需要掏出手机；支持 Siri 指令控制，以及 iOS Shortcuts 的自动化接入。这些不是”有聊胜于无”的功能点，而是真正能在日常使用中减少摩擦的设计决策。这背后体现的是开发者把 Narjo 当成一个认真的 iOS 公民来打造，而不是单纯移植一套功能表。

## 那些让我留下来的细节

在音质和播放控制层面，Narjo 支持交叉淡入淡出（crossfade）和无缝播放（gapless playback），这对于听专辑的完整体验来说很重要；内置的 EQ 调节功能可以针对不同耳机调整音色偏好；歌词同步显示的效果也很精准，配合深色界面，有一种恰到好处的沉浸感。

离线缓存的逻辑做得比较聪明。可以设置缓存上限，Narjo 会根据播放记录自动管理哪些内容需要保留，不需要手动管理一堆离线文件。这个细节省掉了我不少麻烦——之前用其他客户端，时不时需要手动清理缓存，Narjo 让这件事变得透明。

UPNP/DLNA 输出的支持也是我没想到的惊喜。家里有一台支持 DLNA 的音箱，以前需要通过其他 App 才能推送，现在直接在 Narjo 里就能选择输出设备，切换播放端的体验变得完整了。

## 对比音流的一些思考

我没有贬低 [[音流]] 的意思，对于很多用户来说，它是一个非常成熟的选择，中文界面和对国内用户习惯的针对性设计也有其价值。但对我个人来说，Narjo 在两个维度上胜出：一是与 iOS 原生能力的深度整合，Narjo 更像是”为 iPhone 设计的”，而不是”在 iPhone 上可以用的”；二是整体交互流的顺畅程度，我很难用一两个功能点来描述这种差异，但就是那种打开 App、找到想听的歌、按下播放的整个流程里，Narjo 让我产生的阻力更少。

## 最后

折腾自托管音乐服务的人，通常不缺耐心，但真正好的工具应该让人花时间在音乐本身，而不是操作界面上。Narjo 目前还在 TestFlight 测试阶段，这意味着它还在持续迭代，也意味着它有可能在未来引入订阅或一次性付费。但就目前的体验而言，它已经是我用过的所有 iOS Navidrome 客户端里最让我满意的一个。

如果你也在用 [[Navidrome]]，还没有找到一个用起来顺手的 iOS 客户端，[Narjo](https://narjomusic.com/) 值得一试。

## Related Posts

* [试遍所有 Navidrome 客户端，我最终选择了 Narjo](/post/2026/05/narjo-music-player-review.html) - 05/19/2026
* [SyncTrain：让 iPhone 终于能用上 Syncthing 的开源客户端](/post/2026/03/synctrain-syncthing-ios-client.html) - 03/22/2026
* [QM-MUSIC：打造属于你的私有云音乐服务器](/post/2025/12/qm-music-stream-your-music-vault.html) - 12/03/2025
* [音流：一款支持 Navidrome 兼容 Subsonic 的跨平台音乐播放器](/post/2024/07/stream-music-navidrom-subsonic.html) - 07/24/2024
* [最棒的 Navidrome 音乐客户端 Sonixd(Feishin)](/post/2024/04/best-navidrome-player-sonixd-feishin.html) - 04/02/2024
* [利用 Navidrome 搭建自己的在线音乐库](/post/2023/12/navidrome.html) - 12/08/2023
* [Music Tag Web 基于网页修改音乐的元数据](/post/2023/10/music-tag-web.html) - 10/04/2023
* [Memos: 极简美观的自托管备忘录](/post/2023/03/memos-simple-beautiful-notes.html) - 03/11/2023
* [利用 Koel 搭建在线音乐流](/post/2022/03/koel-online-stream-music.html) - 03/08/2022

---

* [← Previous（前一篇）](/post/2026/05/trellis-ai-coding-agent-framework.html "Trellis：让 AI 编码代理真正投入生产的框架")
* [Archive（目录）](/archive.html)
* Next（后一篇） →

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2026/05/narjo-music-player-review.html)评论。

* [产品体验 232](/categories.html#产品体验)

* [navidrome 6](/tags.html#navidrome)
* [narjo 1](/tags.html#narjo)
* [music-player 4](/tags.html#music-player)
* [ios 28](/tags.html#ios)
* [self-hosted 45](/tags.html#self-hosted)
* [streaming 4](/tags.html#streaming)
* [music 13](/tags.html#music)

---

© 2026 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").