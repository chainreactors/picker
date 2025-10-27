---
title: 一个 Mac App 是如何诞生的：Browser Deputy
url: https://buaq.net/go-173228.html
source: unSafe.sh - 不安全
date: 2023-07-31
fetch_date: 2025-10-04T11:51:36.317171
---

# 一个 Mac App 是如何诞生的：Browser Deputy

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

![]()

一个 Mac App 是如何诞生的：Browser Deputy

一个 Mac App 是如何诞生的：Browser Deputy某日在 Vercel 上看 Anybox 网站的访问统计，其中有个从未见过的网站，自然而然的，我想了解关于 Anybox 的评论。这是一
*2023-7-30 14:33:25
Author: [sspai.com(查看原文)](/jump-173228.htm)
阅读量:21
收藏*

---

![](https://cdn-static.sspai.com/ui/img-placeholder.png)

一个 Mac App 是如何诞生的：Browser Deputy

某日在 [Vercel](https://vercel.com/) 上看 [Anybox](https://anybox.app) 网站的访问统计，其中有个从未见过的网站，自然而然的，我想了解关于 Anybox 的评论。这是一个频繁更新的个人博客，首页的三篇文章里都未提及 Anybox。归档列表也比较长，而且篇幅不短，肉眼搜索无果，只好使用谷歌的[站内搜索](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site)。

我使用的浏览器是 Chrome，具体操作步骤：

1. ⌘ + D 选中地址栏 （即「Open Location…」的快捷键，默认为 ⌘ + L，可[自定义](https://support.apple.com/zh-cn/guide/mac-help/mchlp2271/13.0/mac/13.0)）
2. ⌃ + A 将光标移动到行首
3. 输入搜索操作符「site:」
4. ⌃ + E 将光标移动到行尾，并删除 URL 路径，仅保留域名部分
5. 输入搜索关键词「anybox」
6. 按下回车执行搜索

可以看到，这个操作即使可以完全使用快捷键完成，它仍然需要敲击多次键盘，特别是在删除 URL 路径时。简而言之，它费手指。

## 有更好的办法吗？

从上面的操作我们可以看到，未知部分仅有关键词。我们可以从当前标签页获得网站，然后拼凑出网址并在浏览器中打开。

这种需求就是为什么我们使用启动器 App：通过每个启动器都支持的自定义动作实现特有的需求。

比如如果我要在 [Raycast](https://www.raycast.com/) 内实现这样的一个扩展，大概步骤会是这样：

1. ⌘ + 空格呼出 Raycast 面板窗口
2. 执行「Create Extension」命令
3. 编写具体的扩展代码，其中关键为使用 Raycast 的 `runAppleScript` 函数获取浏览器的当前标签页的 URL 和使用 `open` 函数打开链接

以我编写过多个 Raycast 扩展的经验预计，实现这个扩展用时不会超过一小时。

## 为什么还需要一个 Mac App？

当然，如果我花了这一个小时去写这个扩展，也就不会有这篇文章了。

我的问题很容易解决，但是不会写程序的其他人呢？

这几年我写的几个应用，从最早的 [Seamless](https://shinystone.net/seamless)，到 [OK](https://okjson.app)[JSON](https://okjson.app)，再到 [Anybox](https://anybox.app)，这些应用的最初想法都来源于我自身的需求。我相信，作为一个普通人，我的需求也不特殊，总会有部分人也有着同样需求。

不过，我也承认，这些都是小众需求。我的几个应用都是收费应用，现在面临着一样的问题，如何让他们被更多人知道。所以某种程度上，这个应用也是一种 #BuildInPublic 的尝试。

## 该做什么功能？

按照目前的想法，这个应用就是一个可自定义搜索引擎的应用，不同之处就是提供了当前标签页信息。它的交互应该是这样的：

![](https://cdn.sspai.com/2023/07/07/ffa95403d490fa06d1df253f65d9c544.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

初步的交互示意图

Raycast 可以添加 Quicklink，Alfred 可以添加 Web Search，LaunchBar 也可以添加 Action。我前几年用过一个叫 [Haste](https://www.plastic-software.com/haste/) 的应用，它可以通过全局快捷键呼出自定义搜索引擎面板。这些都说明，自定义搜索引擎的可替代品太多了，如 Alfred 和 LaunchBar 可谓将效率优化到极致，而新晋应用 Raycast 则通过优秀的设计降低工具门槛，效率上也可通过配置达到前辈水平。

![](https://cdn.sspai.com/2023/07/07/571f3da48bd9cf62eeb8e8b7cfdbca60.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Haste App

如果我们做一些简单的商业调查，会发现上市已五年的 Haste 应用，在中国区的 Mac App Store 仅有区区 20 个评分。换言之，这个自定义搜索引擎应用，它的商业前景是很渺茫的。

所以，得加功能。

既然这个应用已经需要通过 Apple Script 和浏览器交互了，那就想想这上面能做的事情还有什么吧。

除搜索外，复制当前标签页的 URL 也是一个常用功能，还可以支持 Markdown 形式复制。另外还可以支持搜索书签、历史记录、标签页等。

大概一年前，我就有想过写此系列文章，当时设想的应用是搜索菜单项应用，交互恰好和这个搜索引擎应用一致，所以不妨添加此功能。

「搜索菜单项」这个功能，我虽然不用，因为常见的操作我通过快捷键完成，但它其实很常见。

Raycast 有内置扩展 Search Menu Items；Alfred 有 [Menu Bar Search Workflow](https://github.com/BenziAhamed/Menu-Bar-Search)；Typora 的开发者也有一款名为 [Paletro](https://appmakes.io/paletro) 的应用；知名的 Mac 工具应用开发厂商 [Many Tricks](https://manytricks.com/) 旗下有一款偏向鼠标操作的 [Menuwhere](https://manytricks.com/menuwhere/)；还有来自独立开发者 Roey Biran 的 [Finbar](https://www.roeybiran.com/apps/finbar/)。举的这些例子说明这个功能是有市场和认知度的，并不会无谓地复杂化应用。

总结目前设想的功能：

1. 自定义搜索引擎
2. 复制当前标签页的 URL
3. 复制当前标签页的标题
4. 以 Markdown 形式复制当前标签页
5. 搜索浏览器书签、历史记录、标签页
6. 搜索浏览器菜单项

在开发一个应用时，设计总会和最终产品有区别，这其中可能是因为技术问题，也可能是因为投入思考的时间更多，有更好的设计。但在写代码前就通过文档或原型定义产品，总归是更好的。我们的大脑内存有限，写文档或者画原型的过程，不仅是思考过程，也是存储过程，除了让产品的逻辑更清晰外，还能让我们记下思维结果，不至于遗漏或重复。

## 叫什么名字呢？

俗话说得好，工欲善其事，必先立其名。

应用名称确定好后，其实也就确定了这个应用的边界。

但对我而言，在写代码前就需要想好名字的原因是，在苹果的应用开发工具 Xcode 内新建一个应用时，需要输入一个唯一的应用包名（[Bundle Identifier](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleidentifier)）。惯例是使用反向 DNS 格式（Reverse-DNS Format）。比如苹果的官网域名是 apple.com，苹果浏览器 Safari 的包名则是 `com.apple.Safari`。应用包名在应用上线前都是可以更改的，但一旦开始写代码了，代码内难免出现应用名称，这个也需要一同修改。为了减少麻烦，我一般会在新建项目前确立好应用名称。

这个应用和浏览器相关甚重，所以名字中需体现这一点，我想到了这些名字：

1. Browser Assistant
2. Browser Sidekick
3. Browser Helper
4. Web Sidekick
5. Web Helper

可以看到，我的创意实在有限，这些名字基本上就是「浏览器助手」不同翻译。

里面我最喜欢的是「Browser Sidekick」。

如果你用牛津高阶词典查一下「[sidekick](https://www.oxfordlearnersdictionaries.com/definition/english/sidekick?q=sidekick)」释义，你会发现如此例句：*Batman and his young sidekick Robin*。

当下我就觉得是它了，就是这个意思，这个应用就是你的罗宾！但该死的是，这个名字已经被一个[浏览器](https://www.meetsidekick.com/%29)抢走了，这意味着我需要直接放弃「sidekick」这个词，连带划去「Web Sidekick」。

剩下的名字里，「Browser Assistant」听起来太资本主义，让人想起上班；「Browser Helper」让人想起早些年的 IE 浏览器流氓插件。「Web」这个词虽然比较短，但不如「Browser」准确，所以名字基本可以确定为「Browser something」，其中 something 为「sidekick」的同义词。

打开 macOS 的词典应用，里面有本《American English Thesaurus》词典，虽然没有「sidekick」的同义词，但可查阅「helper」可得到：

> assistant, coworker, fellow worker, workmate, teammate, helpmate, helpmeet, associate, aider, **aide**, colleague, supporter, partner, collaborator, abetter; subordinate, **deputy**, auxiliary, second, second in command, number two, right-hand man, right-hand woman, wingman, attendant, junior, acolyte; accessory, accomplice, henchman; sidekick.

结果可谓理想也不理想，合理选择并不多。「aide」听起来太政治了，于是只剩下「deputy」，那就叫「Browser Deputy」吧。

## 注册域名吗？

名字确定后，也可以注册域名了。

对于 iOS 应用而言，网站和域名的重要性并不如 macOS 应用。因为大部分人只会在 App Store 内搜索并下载 iOS 应用。而 Mac App Store 远远不如 App Store 活跃，搜索引擎给其带来的流量仍是很重要的。而且因为应用有搜索菜单项这个需要去除沙箱才能实现的功能，所以无法上架 Mac App Store，更需要做好网站，提高下载转化率。

但另外一方面，一个 app 后缀的域名，一年需要 15 美元；虽然独立域名看起来美观一些，但同一个开发者之间的应用在域名上看不出关联，不能互相推广；而且域名多了之后，相关的网站项目也多，维护和续费也麻烦，接入 [Paddle](https://www.paddle.com/) 的支付 SDK 时，新域名都要审核。权衡之下，决定不注册新域名，直接使用开发者域名 anybox.ltd。

## 产品界面如何设计？

此时应用的功能和名称都已定义完毕，按照企业工作流程，下一步是将需求文档交由相关人士，包括客户端开发、后端开发、设计师等，然后客户端开发在收到设计师的 UI 设计图后，方可开始具体的 UI 和交互开发。

Browser Deputy 是个纯客户端应用，不需要和和服务器通讯，所以不需要后端开发；而我对设计软件的使用实在不甚熟悉，所以也无法做出高保真设计图，而且应用界面就是一个应用中常见的命令面板，所以我选择直接编写代码，不画原型也不做设计。

不过在写代码前，我一般还是会参考下相似应用是如何设计的。

## 「聚焦」搜索

![](https://cdn.sspai.com/2023/07/14/474a59c277a09b528f7e5f7d1aa272ee.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Spotlight

![](https://cdn.sspai.com/2023/07/14/25cec9d171961f68003539abb029d968.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Spotlight

macOS 自带的「聚焦」搜索（Spotlight）。默认情况下只显示搜索框，输入内容后再展开结果。搜索框左侧是放大镜图标，字体的字号较大，右侧是当前选中的结果类型的图标。每个结果项只有一行，左侧是结果类型的图标，然后是内容，右侧可能有二级结果页的提示箭头。还可能有显示结果类型的章节标题（section header）。

## Xcode 的 Open Quickly

![](https://cdn.sspai.com/2023/07/14/deb5e8e738720dd23c851a8bf5be091f.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Open Quickly

![](https://cdn.sspai.com/2023/07/14/663425de755d1761112dceaa5da27f15.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Open Quickly

Xcode 的 Open Quickly 毫无疑问是我使用次数最多的命令面板。在写代码时，可通过`⇧ + ⌘ + O` 唤起，输入大致的文件名称，按下回车，直接在 Xcode 编辑器打开当前选中的代码文件。它默认情况下和 Spotlight 一样，只有一个搜索框。每个结果项有两行文字，与左侧的文件类型图标垂直居中。标题行的内容是文件名称，详情行的内容是文件路径。当前选中行会使用 macOS 的主题色作为背景颜色，搜索的关键词使用更大的字重高亮。

## Raycast

![](https://cdn.sspai.com/2023/07/14/1bb0c52b2c08f6363e1f20050bde6367.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Raycast

相比之下，Raycast 的设计就比较复杂了。虽然是单行设计，但结果项从左往右依次是类型图标、标题、次标题、类型说明。此外也有章节标题，底部还有个固定的工具栏，提供更多操作的入口和说明。

上述三个是比较有代表性的，其他可供参考对象还有 Alfred、LaunchBar、Paletro、Arc 浏览器的 Command Bar 等。

## 实现功能：内置命令

让我们再次列举 Browser Deputy 设想的功能：

1. 自定义搜索引擎
2. 复制当前标签页的 URL
3. 复制当前标签页的标题
4. 以 Markdown 形式复制当前标签页
5. 搜索浏览器书签、历史记录、标签页
6. 搜索浏览器菜单项

我的开发习惯是，功能实现由简至难。这里面的六个功能里，二、三、四可划分为同一类功能，即内置命令。实现它们只需通过 Apple Script 获取当前浏览器的标签页，而这些我早已在 Anybox 中实现，所要做的事情只是复制粘贴。然后是搜索浏览器菜单项，搜索书签和历史记录，最后需要最多时间的，可能是自定义搜索引擎，因为涉及的界面较多。

把这些功能分类后，可以得到这些在代码内定义的功能类别：

1. 内置命令，如拷贝当前标签页的 URL
2. 搜索菜单项
3. 搜索书签
4. 搜索历史记录
5. 自定义搜索引擎

其中原定的搜索标签页，在调查后决定放弃，因为菜单项中已包含标签页，而且我怀疑此功能的实用性。上述的功能顺序也是我们实现的顺序。

![](https://cdn.sspai.com/2023/07/14/dd4c41bf4aa67d7844a19004a92b6d83.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Browser Deputy：内置命令

经过思考后，决定采用单行设计，因为内置命令如拷贝URL，并无第二行内容可展示。结果项左侧为类型图标，然后是动作名称。底部加入工具栏，一则提供当前应用信息，二是提供设置入口。用户可随时进入设置页面，而无需通过菜单栏图标或者快捷键 `⌘ + ,`。

在做过多款 macOS 应用，接触了许多用户后，我有些体会，即使你做的是效率或者工具应用，也不能假设用户会知道一些如 `⌘ + ,` 可打开设置的惯例。应用的所有功能，应该是对用户可见的。可见并不是指把...