---
title: 来自编辑部的无损备份技巧
url: https://buaq.net/go-172994.html
source: unSafe.sh - 不安全
date: 2023-07-27
fetch_date: 2025-10-04T11:52:56.644334
---

# 来自编辑部的无损备份技巧

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/fac178c331d62a9d64ee72d24b643060.jpg)

来自编辑部的无损备份技巧

如果给数据安全做一份保险方案，少数派编辑部肯定会因为预估出险率高而遭遇加价：有时因为兴趣爱好，有时因为工作需要，我们总是得频繁应对换机、重装、使用测试版这些数据「高危」场景。但也因此，大家也都对备份这
*2023-7-26 20:2:22
Author: [sspai.com(查看原文)](/jump-172994.htm)
阅读量:24
收藏*

---

如果给数据安全做一份保险方案，少数派编辑部肯定会因为预估出险率高而遭遇加价：有时因为兴趣爱好，有时因为工作需要，我们总是得频繁应对换机、重装、使用测试版这些数据「高危」场景。但也因此，大家也都对备份这件事格外在意，并或多或少各自积累了一些习惯、工具和窍门。

这篇文章中，我们就请编辑部的成员们分别聊聊自己的无损备份「姿势」，或许其中就有一两点能给你带来启发。

## macOS 全盘备份

[**@张奕源Nick**](https://sspai.com/u/nicholaszhang)**：**

Time Machine 算是个 macOS 上古时代传下来的老功能。我（应该是）在使用 Snow Leopard 的时候第一次用上了这个功能，当时觉得能够穿越数字时空无比神奇，随后就开始研究起了 macOS 的系统备份方式，也数次用到 Time Machine 恢复系统。

不过，Time Machine 毕竟是和 macOS 系统绑定的备份服务，虽然和 Mac 本身的衔接最为无缝，但用起来不免笨重繁琐。另外，因为 Time Machine 是个 time machine，所以它采用的是叠加备份的方案，即保留同一份文件在不同时段的不同版本，所以备份文件的体积会随时间流逝而不断增长。如果使用移动硬盘作为 Time Machine 的备份仓库，那它会无限扩张，直到把整块硬盘塞满为止。

因此，我开始选择自主性更强、备份方案更灵活的第三方备份工具。经过一番筛选之后，最终留用了《[Carbon Copy Cloner](https://bombich.com/)》（下文简称《CCC》）和《[SuperDuper!](https://www.shirt-pocket.com/SuperDuper/SuperDuperDescription.html)》（下文简称《SD》）。

我对于全盘备份工具有两个要求：

1. 必须是包含一切的无差别备份。我的一些重要文件都有使用同步盘服务进行独立备份，所以选择全盘备份工具的目的就是在电脑本身出事的时候有东西兜底。
2. 必须能把我的电脑恢复到我备份时候的样子。该工具不能只备份文件，还要保留系统设置乃至缓存等。从〇配置新电脑是个无比琐碎又漫长的工作，我不想恢复完了数据还需要再把细碎的系统设置和运行环境等逐一更改一遍。

《CCC》和《SD》都能满足这两项要求，所以我也会轮番使用这俩工具。

从功能上来说，《SD》最为简单直接，主介面简单直白，左侧选择要备份的盘源，右侧选择存放备份文件的目的地，点击即可开始备份。如果没有外置硬盘，《SD》还能把一切都打包成 .dmg 文件，方便转移和取用。

![](https://cdn.sspai.com/2023/07/26/article/bb471a7ed0339a7fd26ddba84546d383?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

除了简单的文件平移，《SD》也能实现更复杂的自动化备份。在选项中可以设定备份周期以及新旧文件的处理方式（譬如是每次都先格式化目标盘然后完整复制，还是只复制有修改的文件，或是智能比对文件自主进行增减）等。如果还有更精细的条件限定，亦可导入或手搓外部脚本，满足特殊需求。

![](https://cdn.sspai.com/2023/07/26/article/6551bf45a5c2196f1e7071d16a128519?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)
![](https://cdn.sspai.com/2023/07/26/article/958d4192f7ae34917b77c7b8331f58a2?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

《CCC》与《SD》的基本功能大体一致，区别在于能做一些更为精细的个性化设置，并更强调备份自动化。其主介面的设计与《SD》类同，选号源盘和目标盘之后就能开始备份。

![](https://cdn.sspai.com/2023/07/26/article/91039d44334e727844284f313abcc0ac?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

在高级设置中，除了能加载脚本、设定自动备份的时间周期之外，还能执行一些后续指令，如备份完毕后关机、发送提醒邮件、执行新的备份命令等。每套备份配置都能保存为任务组（Task Group），其定位与快捷指令类似；任务组之间可以相互激活，形成更为庞大的任务串，适合需要持续备份或者复杂备份的场景。

![](https://cdn.sspai.com/2023/07/26/article/5a715825f48b59b7c2fa75c97185323f?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

前文有提到，无论《CCC》还是《SD》，在全盘备份之后都能把 Mac 恢复到备份时的状态，甚至连开着哪些 app、哪些窗口都能完整保留，用甜食老师的话来说，那就是「系统都不知道自己被恢复了」。恢复数据时需要进入 Mac 电脑的[恢复模式](https://support.apple.com/en-hk/guide/mac-help/mchl82829c17/mac))，然后把备份盘作为启动盘进入系统，随后调起《CCC》或《SD》将数据恢复到主盘即可。

这个设定还带来了一个额外的用法，那就是把备份盘当成 Mac to GO 来用，因为所有数据在备份盘里的就是以一个完整可用的系统的状态存在着（事实上在全盘恢复时的操作也都是在这个「临时系统」里完成的）。考虑到近期 SSD 价格已经非常亲民，我建议无论是纯粹用作备份还是拿来当移动版 macOS，都购买 SSD 作为备份盘，速度上会快很多。我之前要备份的数据总量大概在 500GB 上下，从〇恢复一次要一整晚，实在太过缓慢。

我最高频使用这两个备份工具的时段是我还在用 Intel 版 MacBook Pro 的时期。我那台 Mac 似乎触碰了什么神秘诅咒，机器从里到外的每个部件——萤幕、键盘、主板等——全都坏过，有的还坏过不止一次，以至于触发了[忒修斯之船悖论](https://zh.wikipedia.org/zh-hk/%E5%BF%92%E4%BF%AE%E6%96%AF%E4%B9%8B%E8%88%B9)。所以，我在那段时间非常重视全盘备份，因为说不准什么时候电脑就黑了，只能让天才们将其唤醒。这两年用上 Apple Silicon 的 Mac 之后，一切变得平稳了许多，所以我的《CCC》和《SD》序列号都还停留在老版本上，没来得及升级。这次为了写文章专门把两款 app 都更新到了最新版，导致序列号全都不能用了。

《CCC》和《SD》都是商业付费软体，两者也都采用买断制。《SD》价格为 27.95 美元，《CCC》则为 49.99 美元。如果对于全盘备份没有更高要求，我建议购买《SD》即可，其功能已经足够满足大部分场景使用，且一直在与 macOS 的最新特性保持同步。《CCC》的版本更新频率与 macOS 一致，也就是每出一代 macOS，《CCC》都会跟着更新一个大版本，这意味着即使是老用户也需要每年付费升级一次才能用上最新版，经济上并不划算。《SD》虽然也是大版本更新需付费，但大版本的更新频率没那么高，价格也相对实惠。

另外，《SD》的开发组 Shirt Pocket 是个小公司，在 Mac 还叫 Macintosh 的时候就已经在为该平台开发产品。时至今日，他们的网页依然保留着上古时期的风格，除了《SD》仍在默默维护外，其它作品都已经归入历史（都是 iTunes 辅助工具）。正如 Platy 在《[选对开源软件，从做好「背景调查」开始](https://sspai.com/prime/story/foss-how-to-select)》中所言，这种踏实稳健、长期更新的风格也是考评 app 素质的维度之一。

![](https://cdn.sspai.com/2023/07/26/article/38042f969a794c4fa94a231c66cd224a?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

《SuperDuper!》的网站截图

不过，《CCC》的开发团队也不浮夸，一直保持着十人以内的规模，产品更新稳定，且《CCC》本身也是个 2002 年就已诞生的老产品了。两款备份工具都是业界公认口碑好、功能易用的优秀软体，可以根据自己的需要和预算酌情选择。

## 浏览器数据的徒手备份迁移

[**@PlatyHsu**](https://sspai.com/u/platyhsu)**：**

无论你喜不喜欢，浏览器如今已经占据了越来越多的电脑使用时间，其中保存的数据也越来越繁多：除了传统意义上的书签、历史记录、表单信息，还有犄角旮旯的按钮布局、浏览器设置，和散落在各个浏览器扩展中的配置。如果遇到重装、换机之类的情况，从头配出一套自己顺手的浏览环境还是相当费时的。

对此，尽管如今的浏览器大多内置了一些导入导出或云端同步功能，但用过的人就知道它们的覆盖范围终归还是有限的。作为一个还挺喜欢尝试各种浏览器的人，我在这方面没少花过功夫（和吃过亏）。

有没有什么办法可以更全面、更无损地备份和迁移呢？其实，这些数据既然存在，就一定可以诉诸最简单朴素的手段——基于文件的备份；问题只在于怎么把这些数据找出来。

**答案来得可能比你想象得更简单。**对于 Chromium 和 Firefox，这其实是一场开卷考试，你可以随时查出来：

**Chromium 浏览器:** 在地址栏访问 `about:version`，然后查看其中的 Profile Path 一行。

![](https://cdn.sspai.com/2023/07/26/c87591f37edd4e094f793c7034b006af.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

**Firefox 浏览器：**在地址栏访问 `about:support`，然后查看其中的 Profile Folder 一行。

![](https://cdn.sspai.com/2023/07/26/f487f0e0d66e6b8a11f9c0fa735dd5ec.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

**注：**这里用「Chromium 浏览器」泛指各种基于 Chromium 项目发行和分叉的浏览器，包括 Google Chrome、Microsoft Edge [79+]、Brave、Vivaldi、Opera [15+] 等等等等，它们存储数据的类型和路径基本都是相通的。类似地，「Firefox 浏览器」也可以指代其他发行和分叉版，例如 Librewolf、Waterfox 等。当然，离原味版本越远的浏览器，额外的数据就越多，例如当红辣子鸡 Arc 的很多数据就是在 Profile Path 之外存储的。但限于篇幅，这里只讨论最通用的数据。

**Safari 浏览器：**情况稍微有点复杂。按住 Option 的同时，点击 Finder 窗口的 **Go** [转到] > **Library** [资料库] 菜单，其中：

* `Safari` 目录中包括 Cookies 和缓存以外的数据；
* `Containers/com.apple.Safari/Data/Library` 包括 Cookies 和缓存等数据。这些在早年其实也是直接存在 `~/Library` 目录最上层的，只是后来为了适配沙箱机制挪进了 `Containers` 目录内部。

### 全目录备份和迁移

**对于 Chromium 和 Firefox 而言，如果求省事，其实你可以囫囵备份下来整个 Profile Folder。**日后换机、重装时，直接用其中的内容覆盖新浏览器中 Profile Folder 的内容即可。

但如果这么做，要注意：

* 备份和覆盖都要在浏览器完全退出的状态下操作；
* 必须是用原有 Profile Folder 的**内容**替换当前 Profile Folder 的**内容**，不能直接将原有 Profile Folder 搬到与当前 Profile Folder 平级的位置，否则浏览器也无法识别这个 profile。
* 一些安全机制较为严格的网站的登录状态，以及浏览器扩展的安装状态等，是无法如此无缝迁移的，必须重新登录或者安装，但完成后一般会发现原来的网站和扩展数据仍然可以沿用。

根据我的经验，Firefox 比 Chromium 更适合用这种全目录迁移方法，得到的效果不能说完全一样，只能说没什么两样（原谅我偶尔用两句废话文学）；此外，越清洁的版本（例如 Librewolf 和 Ungoogled Chrome）对这种方法的适应性就越好。

### 单独迁移特定数据文件

当然，全目录的方法可能显得有些过于「泥沙俱下」了点，也因如此并不是官方推荐的做法。

如果你想要更精准地备份特定类型的数据，可以参考如下表格：

|  |  |  |  |
| --- | --- | --- | --- |
| **浏览器** | **Chromium** | **Firefox** | **Safari** |
| **书签** | `Bookmarks` 文件（无后缀名，内容为 JSON） | `places.sqlite` | `Bookmarks.plist` |
| **历史记录** | `History`（无后缀名，SQLite 数据库） | `places.sqlite` | `History.db`（SQLite 数据库） |
| **Cookies 和浏览数据** | * `Cookies`（无后缀名，SQLite 数据库） * `Local Storage`和 `Session Storage` 目录 * `IndexedDB` 目录下以 `http(s)` 开头的目录 | * `cookies.sqlite` * `webappsstore.sqlite` * `storage/<profile-name>/` 目录下以 `http(s)` 开头的子目录 | * `~/Library/Containers/com.apple.Safari/Data/Library/Cookies` * `localStorage` 目录下以 `http(s)` 开头的子目录 * `Databases` 目录 |
| **浏览状态** | `Sessions` 目录 | `sessionstore.jsonlz4` | `LastSession.plist` |
| **保存密码** | `Login Data`（无后缀名，SQLite 数据库） | `logins.json` | 位于 Login 或 iCloud 钥匙串（取决于是否开启 iCloud）中，需用 Keychain Access 应用导入导出 |
| **浏览器设置** | `Preferences`（无后缀名，内容为 JSON） | `prefs.js` | `~/Library/Preferences/com.apple.Safari.plist` |
| **扩展** | 扩展本身：`Extensions` （每个子目录一个）  扩展设置：`Local Extension Settings` 目录（每个子目录一个）  其他扩展数据：   * `Extension Rules` * `Extension Scripts` 和 `Extension State` 目录 * `IndexedDB` 目录下以 `chrome-extension` 开头的目录 | 扩展本身：`extensions` 目录  扩展设置：`extension-settings.json` 和 `extension-preferences.json`  其他扩展数据：`storage/<profile-name>/` 目录下以 `moz-extension` 开头的子目录 | 扩展本身：/Applications 下的独立应用  扩展数据：   * `localStorage` 目录下以 `safari-web-extension` 开头的子目录 * `~/Library/Containers/` 目录下相应应用的沙箱目录中，具体路径和数据各异 |

**说明：**

* 这些路径只有少数是我自己专门找的，其余大多都是从 [Firefox 数据导入功能的代码库](https://searchfox.org/mozilla-central/source/browser/components/migration)里抄的；如果帮到了你，请把赞美归于他们。

![](https://cdn.sspai.com/2023/07/26/872410ec2ed82b716e3777ade44a1a1a.png?imageView2/2/w/1120/q/40/interlace/1/ignore-erro...