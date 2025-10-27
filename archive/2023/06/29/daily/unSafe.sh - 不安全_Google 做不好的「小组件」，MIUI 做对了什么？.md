---
title: Google 做不好的「小组件」，MIUI 做对了什么？
url: https://buaq.net/go-170759.html
source: unSafe.sh - 不安全
date: 2023-06-29
fetch_date: 2025-10-04T11:46:24.920005
---

# Google 做不好的「小组件」，MIUI 做对了什么？

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

![](https://8aqnet.cdn.bcebos.com/c00294dedf4a1a23a75ac541f3f9e830.jpg)

Google 做不好的「小组件」，MIUI 做对了什么？

在今年的 WWDC 中，Apple 终于「舍得」为 iOS 的桌面小组件补上一项重要功能：可交互性。从 iOS 17 开始，无论是在锁屏、主屏还是这次刚上线的「待机」页面，我们都可以通过小组件上的交互
*2023-6-28 22:50:58
Author: [sspai.com(查看原文)](/jump-170759.htm)
阅读量:30
收藏*

---

在今年的 WWDC 中，Apple 终于「舍得」为 iOS 的桌面小组件补上一项重要功能：可交互性。从 iOS 17 开始，无论是在锁屏、主屏还是这次刚上线的「待机」页面，我们都可以通过小组件上的交互按钮完成一些简单的任务。

**关联阅读**：

* [从开发者的角度看 iOS 14 小组件](https://sspai.com/post/61371)
* [具透 | 日复一日，尽显非凡：iOS 17 中值得关注的新特性](https://sspai.com/post/80184)

但对于 Android 用户来说，小组件支持交互似乎应该是一件「天经地义」的事情。早在 2008 年 10 月发布的首个版本中，Android 就支持小组件；2021 年发布 Android 12 时，Google 还进一步[强化了](https://developer.android.com/about/versions/12/features/widgets?hl=zh-cn)小组件方方面面的功能，包括圆角、主题、自定义、功能、自适应布局、动画效果等，为小组件在平板、折叠屏等大屏设备中的表现力提供了更好的基础。

![](https://cdn.sspai.com/2023/06/28/8f482ece89505332a8ca69206c39785e.jpg?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

**不过，这种先发优势并不意味着 Android 小组件就能睥睨 iOS。**相反，正如 Android 平台的常见剧本《起个大早赶个晚集》那样，它的小组件也是功能有余、细节不足。今天，如果你在 Google Pixel 的启动器上添加几个来自不同 app 的同尺寸小组件，大概率也就能看到几种各不相同的实际尺寸和圆角半径。

或许正是出于对原生 Android 这种粗糙效果的不满意，我们看到 MIUI 等定制系统纷纷选择另起炉灶，重新制定一套小组件的开发方案和设计规范。

**那么，Google 的小组件方案到底有什么问题导致了这种现状，第三方系统又是怎么试图解决的？**

专业的问题还是要专业的人来解答。为此，我们请到了人气记账 app《[钱迹](https://qianjiapp.com/)》的开发者李唐。作为一款跨平台 app 的开发者，李唐对 iOS 和 Android 的小组件适配有着第一手的经验，也亲身体会过个中不为用户所知的种种「坑」。

下面，我们就把麦克风交给李唐，由他来为大家分析原生和定制 Android 系统小组件的功过得失。

## 找准「定位」，是小组件的首要问题

和型号总是已知、分辨率数值明确的 iPhone 不同，Android 设备的分辨率可谓千奇百怪，这种屏幕参数的碎片化，直接导致小组件无法按照开发者设想的形状进行呈现。

以下图为例，物理尺寸观感基本相同的字母 a，在左侧的低分辨率设备上显示时所使用的实际物理像素数量更少；所以反过来说，一个长宽均为 100 物理像素的正方形，在同尺寸低分辨率设备上的显示效果往往会更大。

![](https://cdn.sspai.com/2023/06/28/022d0b2a9e81bd1f168a00e936ad2345.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

尺寸相同的两个屏幕可能具有不同数量的像素 | 图：Google

为了保证不同屏幕上的尺寸和观感一致性，Android 平台引入了[密度无关像素](https://developer.android.com/training/multiscreen/screendensities?hl=zh-cn#TaskUseDP)（dp）这个度量单位来进行辅助；桌面小组件也不例外。在 Android 12 之前，Google 允许开发借助单位为 dp 的 `minHeight` 和 `minWidth` 两项参数来设定小组件在主屏上的最小长宽，希望通过这种方式来保证同一小组件在不同设备上的尺寸基本一致。

但密度问题可以「无关」，精度问题又会出来捣乱。密度无关像素的计算过程涉及根据特定公式进行计算转换，由于转换后的数值可能不是一个整数值，结果需要四舍五入，然后将结果归入最为接近的整数坐标网格内。另外，因为转换公式中屏幕密度与物理像素的正相关关系，分辨率越高的设备，在遇到类似情况时四舍五入的结果差异也就越大。

**换言之，以 dp 作为小组件尺寸参考的做法只能保证小组件在视觉观感上的大致相近，并且这种观感差异会极大程度上收到高分辨率、高像素密度等因素影响**。

开发者为了避免小组件内容显示出现错位、异常，就不得不通过一些特定的布局手段来对小组件边界进行额外调整，比如边距、比例、对齐规则等……这些额外的调整标准各不相同，最终小组件呈现出来的实际效果自然千差万别。

以下图中的 Glance Weather 与 Apple Music 的小组件为例。尽管两者名义上都是 4 × 1 尺寸，但前者追求将小组件铺满所在的网格区域，后者则以内容为中心，将小组件做得尽可能紧凑；放在一起，就会出现这种「逼死强迫症」的景观。

![](https://cdn.sspai.com/2023/06/28/a95bcdb876861437b3c9ac2b20f4ebda.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

**因此，李唐认为直到 Android 12 之前，Android 的小组件都可以说是「半成品」**。从开发者的角度触发，他的记账应用钱迹最初进行小组件开发时就遇到过非常多的痛点，加上 Android 本身比较割裂的生态，Google 以往所提供的方法或者属性在实际应用中可以说是没什么效果的：

> 早前如果我们按照 Google 的官方文档开发小组件，这个小组件在不同厂商的手机上所呈现出来的尺寸大概率各不相同，同一个小组件在 4x5 和 5x6 的桌面中宽高比也完全不一样……在经历了多轮尝试后，我们最终放弃了对尺寸统一的奢望，以 `MATCH_PARENT` 这种方式将小组件尺寸渲染完全交给手机去自行处理——尽管它在某些机型又会带来其他问题。

**那么，对小组件做出重大更新的 Android 12 是否解决了这个问题呢？答案并不十分乐观。**

首先回顾一下 Android 12 对小组件的一个主要改进和切入点：桌面网格（grid cells）。从这代系统开始，小组件可以预设自己的目标网格宽度和高度（通过 `targetCellWidth` 和 `targetCellHeight` 两项属性）了。换句话说，开发者可以向桌面声明其小组件预期呈现的形态，而不是放由系统进行不精确的估算和转换。这样，用户能够直接感，特殊情况也更易提前考虑，在 Google 看来正是更好的选择。

应当肯定，这个改进是有效果的。直接将小组件与桌面网格匹配的做法，配合 Android 12 对小组件[圆角半径](https://developer.android.com/about/versions/12/features/widgets?hl=zh-cn#rounded-corner)、[响应式布局](https://developer.android.com/develop/ui/views/appwidgets/layouts#provide-responsive-layouts)以及[精确式布局](https://developer.android.com/develop/ui/views/appwidgets/layouts#provide-exact-layouts)等方面的改进，使得借助这些新规范进行开发的小组件在 Android 12 及以上版本系统中，已经能够呈现视觉效果几乎一致的小组件尺寸了，比如下图右侧上方的 Google 天气和 Google 相册：

![](https://cdn.sspai.com/2023/06/28/ce61818e628fa34f3bce2d18873dcdf5.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

iOS 与 Android 的 2×2 小组件对比

**但这套方案与 iOS 的小组件差距依然存在，因为 Android 12 的新方案并没有解决所有问题。**网格能约束小组件的「外在」，但管不到「内在」。Google 并未像 iOS 那样为小组件规定更为严格的布局属性，如果在网格内部小组件与网格边缘的边距各不相同，依然会导致特定尺寸、尤其是不规则形状小组件在视觉效果上的「不和谐」。

以下图的两个小组件为例，虽然名义上都是 3×2 尺寸，但一个内部边距大、一个内部边距小，看起来完全不像是一个尺寸的东西：

![](https://cdn.sspai.com/2023/06/28/583c47e336b47d35ddafc19e6a84e53a.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

3×2 尺寸的不规则小组件，边距就千奇百怪了

## 立足小生态抠细节、严管理：MIUI 的尝试

Google 的原生方案不好用，定制系统也就纷纷动起了另起炉灶的心思。特别是MIUI、OriginOS 等本就或多或少借鉴了 iOS 的国内定制系统，眼看着 iOS 跟进了小组件，继续「从善如流」地打造一套更接近 Apple 做法的方案，是一个比较自然的选择。

这方面，最有代表性的就是 MIUI。2021 年 9 月，MIUI「小部件」功能上线开发版，同时上线的还有首批适配了小部件的第三方应用，包括百度、QQ 音乐、高德地图等。

文章来源: https://sspai.com/prime/story/android-widget-problems
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)