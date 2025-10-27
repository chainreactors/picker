---
title: App 里的那些精美动效，是如何与 Airbnb 扯上关系的？
url: https://buaq.net/go-170231.html
source: unSafe.sh - 不安全
date: 2023-06-26
fetch_date: 2025-10-04T11:45:03.612244
---

# App 里的那些精美动效，是如何与 Airbnb 扯上关系的？

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

![](https://8aqnet.cdn.bcebos.com/e47df102668a7bae4335d3667f808f75.jpg)

App 里的那些精美动效，是如何与 Airbnb 扯上关系的？

前言动画工具 LottieFiles 前不久更新了 Figma 插件，支持在 Figma 中快速创建单帧或多帧动画。其最新推出的极简动画设计工具 Lottie Creator 也正在公测中。看得出，L
*2023-6-25 17:30:0
Author: [sspai.com(查看原文)](/jump-170231.htm)
阅读量:22
收藏*

---

![](https://cdn.sspai.com/2023/06/20/7803168204fb4b9949eb37bafb9b0715.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

## 前言

动画工具 LottieFiles 前不久更新了 Figma 插件，支持在 Figma 中快速创建单帧或多帧动画。其最新推出的极简动画设计工具 Lottie Creator 也正在公测中。

看得出，LottieFiles 正在为降低动画设计的技术门槛而努力。但这一切，都是得益于 **Lottie** 的出现。

我们工作中会使用很多工具产品，却鲜少关注产品的幕后，这篇文章就来带你全面了解一下 Lottie 的发展之路。

废话不多说，一起进入正题：

## Airbnb 的 Lottie

Airbnb？做 AE 的动画插件？还开源？

这是我在 2017 年某个工作日午后，看着面前一脸激动的 CTO 发出的灵魂三问。

相信很多设计师第一次接触 Lottie 时，多少也会有类似的不解。

### 01. 以社区为导向的动画工具

2015 年，动画脚本开发者 [Hernan Torrisi](https://github.com/bodymovin) 开发了一款运行在 Adobe 特效软件 After Effects（AE）里的动画插件——Bodymovin，该插件以 JSON 格式将 AE 生成的动画描述成文本，允许 Web 开发人员轻松访问。

Hernan Torrisi 将其开源到 GitHub 上并作为副业一直维护和不断更新。此外他还为 JSON 格式提供了首个渲染器（基于 JS 的 Web 动画播放器）。而这一切的努力都被 Airbnb 的开发团队看在眼里。

2016 年，Airbnb 的工程师 [Gabriel Peal](https://github.com/airbnb/lottie-android)、[Brandon Withrow](https://github.com/buba447)、[Leland Richardson](https://github.com/lottie-react-native/lottie-react-native) 和动画师 [Salih Abdul-Karim](https://www.linkedin.com/in/salihabdulkarim/) 一起，基于 Hernan Torrisi 和社区开发者们的贡献又拓展出了 Android、 iOS 和 React Native 动画库——可以解析 JSON 数据并渲染成动画运行在移动设备上。

![](https://cdn.sspai.com/2023/06/20/6b1615cedea2ba0b5377fc3d5cfdb99d.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Airbnb 的 Lottie 多平台宣传图

2017 年，Airbnb 正式推出此项目，命名其为 Lottie，并秉承着 Hernan Torrisi 的开源精神，打造了 GitHub 上的 Lottie 社区。之后在 Salih（Airbnb 前设计主管）和 Karri Saarinen（Linear 创始人）的努力下又迅速推广到设计师圈层。

![](https://cdn.sspai.com/2023/06/20/37c65d0e4ee8d4ef8b67a68e601fe4a3.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Lottie 创始者们以及 Airbnb 的 Lottie 团队早期成员

时至今日，Lottie 当时的创始人们早已都不在 Airbnb 供职，却仍在 GitHub 上维护着各自版本的 Lottie 动画库，并跟 Lottie 的后继者 LottieFiles 始终保持着交流与合作。

### 02. Lottie 是什么？

前面讲了 Lottie 的由来，那 Lottie 具体是什么？

先来看看 Airbnb 的官方说法：

> Lottie 是一种适用于 Android、iOS、Web 和 Windows 的动画库，它解析使用 Bodymovin 导出为 JSON 格式的 Adob​​e After Effects 动画，并在移动设备和 Web 上本地渲染它们！

官方简单把它描述为动画库，但事实上，Lottie 并不是具体的某一个产品或工具，它是一套成体系、跨平台的完整动画解决方案。

这一点，我们通过了解 Lottie 的工作原理便可领会：

### 03. Lottie 的工作原理

原理很简单，设计师在 AE 中制作完动画，安装好的 Bodymovin 插件可以将 AE 生成的 .aep 格式文件转换为 Lottie 可以解析的 .json 文件，平台安装了 Lottie 动画库就可以直接渲染动画并绘制在设备上。

整个流程如图所示：

![](https://cdn.sspai.com/2023/06/20/954daf4fd0b92a5b25c73983028e1412.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

截至目前，在主流系统 [Web](https://github.com/airbnb/lottie-web)、[iOS](https://github.com/airbnb/lottie-ios)、[Android](https://github.com/airbnb/lottie-android)、[Windows](https://github.com/windows-toolkit/Lottie-Windows)、[React Native](https://github.com/react-native-community/lottie-react-native) 和其他平台 [Xamarin](https://github.com/martijn00/LottieXamarin)、[NativeScript](https://github.com/bradmartin/nativescript-lottie)、[Vue](https://github.com/chenqingspring/vue-lottie)、[Angular](https://github.com/chenqingspring/ng-lottie)、[QT](https://blog.qt.io/blog/2019/03/08/announcing-qtlottie/)、[Skia](https://skia.org/user/modules/skottie)、[Framer X](https://store.framer.com/package/airbnb/lottie)、[Sketch](https://aeux.io/) 中均存在开源和免费的 Lottie 播放器。

另外需要注意，在 AE 中使用 Lottie 时要避免使用位图，**Lottie 只能解析矢量图形**，尽量不要使用表达式、蒙版、合并路径等功能，它更适合用来制作应用程序里的加载、刷新、小提示、icon 点击或 tab 切换等特定场景下动画。

初学者可参考 [如何在 AE 中使用 Lottie](https://airbnb.io/lottie/#/after-effects) 和 [Lottie 支持的 AE 功能](https://airbnb.io/lottie/#/supported-features)。

### 04. 为什么叫 Lottie

Lottie 取自德国剪影动画先驱 [Charlotte Lotte Reiniger](http://www.lotte-movie.com/about-lotte)（1899 年～1981 年）的中间名。

Lotte 是一位才华横溢充满创造力的动画导演，以她开创性的定格剪影动画而闻名。她一生制作了大概 70 余部动画和影片，多取材自神话、童话和寓言。

![](https://cdn.sspai.com/2023/06/20/a4a56867b65b707fa7ccfcd39062e008.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

Charlotte Lotte Reiniger 于 1972 年获得德国电影奖金奖

因受纳粹迫害，导致二战期间颠沛流离，Lotte 很多战前的作品被损坏或遗失，她于 1926 年发行的《艾哈迈德王子历险记》(The Adventures of Prince Achmed)，被认为有可能是世界上第一部长篇动画电影。

Airbnb 团队以 Lottie 来纪念这位动画先驱，同时也寄予了 Lottie 兼备开创性和创新性的期望。

### 05. Lottie 的优势所在

讲了这么多，到底 Lottie 好在哪里？有什么具体优势？

我们先来看几个动画：

![](https://cdn.sspai.com/2023/06/21/00ace422aeb2efb5d07cf3fd5f8e9a28.gif)

多邻国 App 内形象动画

![](https://cdn.sspai.com/2023/06/21/93310a54a3151411643917cad5485060.gif)

TG 动态贴纸

![](https://cdn.sspai.com/2023/06/21/7e3d574714dad5131517071ce6b3b53b.gif)

toss 大量使用 3D 位图与 Lottie 动画结合

以上这些动画无一例外都是 Lottie 实现的，在动画落地方面，Lottie 是设计师和开发者协作的最佳桥梁。

它的具体优势如下：

* 易操作
* 高质量、轻量级
* 基于矢量，可扩展性好
* 跨平台，适用任何设备
* 可交互性

比起 GIF，Lottie 动画小了 600 倍，运行速度快了 10 倍；Lottie 解析的 JSON 格式通常只有几千字节，这意味着它生成的动画体量极小，极大减少系统和设备的负载；因为 Lottie 支持的是矢量动画，生成文件可以在不影响质量的情况下随意缩放，在任何设备上都不会掉帧卡帧；视觉上，Lottie 也支持透明度和渐变等效果，这一点，GIF 首先不支持透明度，而且还有最让设计师头痛的边缘锯齿问题；另外，前面也说了，Lottie 社区有针对各种平台和系统的动画库，你能想到的平台，都可以运行 Lottie 动画。

![](https://cdn.sspai.com/2023/06/20/10fbfc7c6541ec8001ea6e1cf130a58b.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

图源：[what-is-lottie?](https://lottiefiles.com/what-is-lottie?utm_medium=web&utm_source=navigation-what-is-lottie)

Lottie 对数字产品的支持优于其他所有格式，更重要的是，它的内置选项支持你在加载页面时自动播放动画，可以设置循环播放、悬停播放、加/减速、添加播放控件甚至基于交互手势触发。你还可以在代码层面指定宽高和背景色。

毋庸置疑，Lottie 的流行让互联网数字产品都灵动了起来，越来越多的产品开始拓展自己的品牌形象动画，因为动态总是比静态更有记忆点和辨识度。试想一下，如果多邻国 app 里的卡通形象都是纯静态的，你的使用体验会不会大打折扣。

尽管 Lottie 有以上诸多优点，其最实质性的作用还是在于——解决了动画交付和落地效果的现实难题。

这就不得不回溯历史，从 Flash 的惨淡退场讲起了。

## Flash 退场是契机

前不久我在某微信群看到一张招聘截图，招聘要求上赫然写着「熟练掌握 Flash」，心想这 JD 够复古的。

Flash 对上了点年纪的设计师来说，是一段悲伤往事。

Flash 彻底退场是在 2021 年（2021 年 1 月 12 日，[Adobe 禁止全平台运行所有 Flash 内容](https://www.bbc.com/news/technology-55497353)）。但它在 2011 年就因为乔布斯与 Adobe 交恶而被迫退出了 Apple 市场，当时的 Flash Player 正是 Adobe 的主要盈利项目。

当时，乔帮主列出了 Flash 的三宗罪：

* 非开源
* 性能差、安全漏洞
* 不支持触摸屏交互

一通操作后，Flash 彻底失去了移动端市场，甚至电脑端的市场份额也受到影响。这一切几乎断送了 Flash，却也催生了 HTML5 的流行。

![](https://cdn.sspai.com/2023/06/20/2662ed9d7c80ad2ddf0bed49f37cb612.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

图源：[Sofia Green](https://www.ispringsolutions.com/blog/flash-alternative)

是危机也是转机，这之后 Adobe 把商业重心转移到了 Adobe 全家桶上，推出了 CC 系列，拓展了更大的市场，疯狂收购更是停不下来，然后就有了去年**「**[**Adobe 收购 Figma 并认购股票，斥资 200 亿美元**](https://news.adobe.com/news/news-details/2022/Adobe-to-Acquire-Figma/default.aspx)**」**这样震惊设计圈一整年的炸裂新闻！

Flash 最初也是 Adobe 收购来的，跟古早的 Fireworks、 Dreamweaver 一起打包以 36 亿美元的价格包圆，而其中的 30 亿美元都被用于 Flash。之后 Adobe 将 Flash 重新命名为编辑器 Flash Professional（2016 年改名为 Adob​​e Animate）和播放器 Flash Player。

事实上，Flash 本身也确有很多问题，最典型的就是用户必须在本地安装 Flash Player ，需要经常更新插件不说， Flash 动画通常还需要加载一下才能正常显示，这非常挑战用户的耐心。诚然，Flash 是划时代的产品，但随着数字设备的升级换代，Flash 逐渐力不从心也是事实。

总之先拉回来，为什么要讲这段陈谷子烂芝麻？

正因为 Lottie 的诞生与 Flash 的退场息息相关。

迫于 Flash 离开了 Apple 平台，Bodymovin 的开发者 Hernan Torrisi 才不得已开发替代品来弥补 Flash 留下的缺口，他成功了，就有了后来的 Lottie。

谈到 Lottie 的影响，他直言：

> 事实上，Lottie 减少了代码量从而促使进了这种解决方案的可行性，我认为这是支撑 Lottie 重要性的柱石。即使从开发者的角度，使用 Lottie 实现动画也是非常简单。因此，它不仅是设计师的简单解决方案，也是开发者的简单解决方案。

的确，Lottie 为开发者节省了大量的时间，要知道，以往做动画，迫于现有格式的限制，往往为了更好的产品体验，是需要让开发者直接用代码去绘制的。同时，设计师还要输出 demo 和详细标注，遇到比较懒的设计师，开发人员的工作量就主打一个加倍，看到「会动的」设计需求就瑟瑟发抖。

而设计师这边也不轻松，对设计师来说，做设计不是最困难的，交付物料环节才最麻烦。

在软件里做完动画，要么需要导出序列帧再到 PS 里生成 GIF 文件，要么就是导出序列帧生成雪碧图或者转换成 APNG 文件，中间还要涉及图像压缩、监测色值变化、导出效果等等。最糟心的是，交付之后运行起来发现掉帧还要再回炉重造，之后整个流程再来一遍或多遍。光是这样描述一下都让人倍感心累。

自从有了 Lottie，这些复杂环节统统都不需要了。设计师可以集中精力在动画制作上，在 AE 里设计完动画使用 Bodymovin 直接导出 JSON 文件即可。

而开发者这边拿到 JSON 文件后，只需要使用 Lottie 播放器渲染即可直接在设备上运行，也不需要再拿素材反复调试，也不用在代码里构建复杂效果。相信没有哪个平台开发者是不喜欢设计师提供 Lottie 格式动画的。

看到这里，是不是能理解开篇我的那位 CTO 为什么一脸激动了。有人说设计师 + Lottie =「开发者友好」动画，不无道理。

解放了生产力，优秀的产品设计和动效体验成几何增长，以至于在全球排名前 500 的应用程序中你都可以看到 Lottie 动画的身影。

## 开源社区，花开遍地

既然 Lottie 主打构建开源社区，那么基于 Lottie 的拓展项目就会不断涌现。

**2017 年**， LottieFiles 初始版本发布，支持 Lottie 动画预览和文件管理，团队致力于打造全球最大...