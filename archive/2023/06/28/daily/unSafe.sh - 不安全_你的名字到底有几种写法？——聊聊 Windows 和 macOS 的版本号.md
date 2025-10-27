---
title: 你的名字到底有几种写法？——聊聊 Windows 和 macOS 的版本号
url: https://buaq.net/go-170590.html
source: unSafe.sh - 不安全
date: 2023-06-28
fetch_date: 2025-10-04T11:44:15.669180
---

# 你的名字到底有几种写法？——聊聊 Windows 和 macOS 的版本号

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

![](https://8aqnet.cdn.bcebos.com/aa7634935400fea759b3f6d7a4d98161.jpg)

你的名字到底有几种写法？——聊聊 Windows 和 macOS 的版本号

开场白Platy 夏天又到了。如果说秋天是收获的季节，那么夏天就是……Lincoln ……为收获做测试的季节？Platy 没错。每年的这个时候，也是各大厂商为下半年将要推出的系统更新做测试的扎堆
*2023-6-27 22:4:32
Author: [sspai.com(查看原文)](/jump-170590.htm)
阅读量:31
收藏*

---

## 开场白

**Platy** 夏天又到了。如果说秋天是收获的季节，那么夏天就是……

**Lincoln** ……为收获做测试的季节？

**Platy** 没错。每年的这个时候，也是各大厂商为下半年将要推出的系统更新做测试的扎堆时间；作为科技爱好者，大家的收藏夹和下载文件夹在这几个月也往往会被各种标着一长串版本号的安装镜像文件占据。

以前，因为 macOS 的版本编号比较简单，我对版本号这回事也没做过深入研究。直到我去年[成为了](https://sspai.com/post/77527)一名光荣的 Surface 用户，才发现 Windows 如今的版本号着实复杂得让我有些昏厥。

所以今天，我就请来编辑部里[「脚踏两条船」最拿手](https://sspai.com/prime/story/zhuanglesha-lincoln)的专家 Lincoln（[@广陵止息](https://sspai.com/u/kgguxr0e) ），一起来唠唠操作系统起名编号的家长里短。

**Lincoln** 知无不言。

## 版本号与构建号

### Windows

**Platy** 好的，那请快来救我一下，我现在正在看 Windows 设置里的这个「系统信息」界面……**这里为什么有三个「版本」，「版本」「版本」「操作系统版本」**？我是不是装了盗版系统？

![](https://cdn.sspai.com/2023/06/27/218db3bd046abb452c1aeee59df2c24a.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

**Lincoln** ……有没有一种可能，比如说他们中文本地化团队被拖欠工资太久了。

总之你冷静一下，我们先从最长的看起吧，看那串叫做**「操作系统版本」（OS build）**的数字。这里显示的已经是一个简化的格式，完整的应该是 `11.0.22000.2057`，它由这四个部分构成：

|  |  |
| --- | --- |
| 主版本号 major version | 11 |
| 次版本号 minor version | 0 |
| 构建号 build number | 22000 |
| 修订号 revision number | 2057 |

**Platy** 主次版本那两位好懂，构建号和修订号是什么意思呢？

**Lincoln** 其实看英文名会更好理解一点：我们知道软件开发都涉及一个环节叫「构建」（build），指的是把软件从源代码转换成能跑起来的二进制格式。

但构建并不是发布之前的一锤子买卖，而是贯穿在整个开发过程中：一般是开发到一定阶段，就构建一个版本进行测试，然后根据运行效果和发现的问题，一边继续开发，一边构建新的版本进行测试，如此循环。

在这个过程中，一般会给每次构建一个编号，以便追溯，这就是构建号（Build）。构建号越大，一般也就代表开发推进的时间越长；构建号提升，也就意味着新功能的加入。

特定构建推出后，有时需要补充一些微小更改，提供错误修复、安全补丁或性能优化等，也就是大家耳熟能祥的「KB」开头的「月度安全更新」——有时也叫「累积更新」「质量更新」之类。这种不涉及功能更新的升级就通过修订号（Revision）来体现。

**Platy** 这么一说我想起来，Windows 的构建号好像是「代代相传」的，一直在变大？Vista 刚出那会还是 6000，然后就是 Win 7 的 7600、Win 10 的 10240 之类，到 Win 11 就是 22000 起步了，越涨越快的感觉。

![](https://cdn.sspai.com/2023/06/27/a3b19ba5dc92d7821f0d359c188b67a9.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

（来源：BetaWiki）

**Lincoln** 是的，其实构建号以前主要是在测试版阶段比较重要，正式版系统推出后就没什么存在感了，仅仅是推出服务包（Service Pack）这种重大更新的时候才会递增。

**但从 Windows 10 开始，微软引入了所谓「**[**Windows 即服务**](https://learn.microsoft.com/en-us/windows/deployment/update/waas-quick-start)**」（Windows as a Service，简称 WaaS）的更新模式**，不再像以前一样发布服务包了，而是改成发布功能更新（feature update）。

此后，微软在很长一段时间内维持了半年一次的节奏，直到 2022 年底调整为每年一次，中间穿插大约每个季度一次、内部称为「Moment」的小型功能更新。

**无论是 feature update 还是 moment update，都会对应一个新的构建号。**再加上微软现在会通过 Windows Insider（预览体验计划）广泛招募测试者，分通道（channel）推送开发成熟度各异的功能更新测试版本，给用户的感觉就是构建号的变化频率比以前更高，重要性也更高了；很多科技媒体和技术社区在报道新功能时也会用构建号来代指具体版本，因为这样比较准确。

**Platy** 但好像也挺难记的，五位数字里我能熟读成诵的只有电信和联通的客服号。

**Lincoln** ……所以这就说到了之前那张截图里第二个「版本」，在英文版里对应的术语是 version，但为了不引起歧义，一般可以补充说成「显示版本号」（display version）或者「功能更新版本号」（feature release version）。

![](https://cdn.sspai.com/2023/06/27/3c1233c9d8769a8ab5957e2d60cf14cf.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

这也是为了配合「Windows 即服务」的模式，从 Windows 10 开始使用的概念，或多或少取代了在过去用「服务包」指代具体版本的用途。

功能更新版本号的格式一开始是推出年月的简写，比如 1507、1803、1909，有点像 Ubuntu；但从 2020 年下半年就改成了年份尾数加推出的半年编号，比如 21H1、22H2。这虽然没有以前的 XP SP3 那么朗朗上口，但比你硬背构建号还是轻松多了。

不过就像刚刚说的，Windows 11 现在又改成了每年一次大更新，中间穿插几次小更新的模式，功能更新版本号的意义很大程度上又被架空了，所以也许微软的起名部门已经开工筹划一个新的版本号了……

**Platy** 救命。

**Lincoln** 那你说说 macOS 的情况呗？我正好歇歇……

### macOS

**Platy** OK，先说说 macOS 看版本号的[官方方法](https://support.apple.com/zh-cn/HT201260)吧。打开左上角的苹果菜单，然后**选择「关于本机」，其中「macOS」那行写的就是版本号**，比如下面这张图中的 Ventura 13.4.1。

不过这也不是版本号的完全体，**如果你在那个版本号上点一下**，它就会变成……

![](https://cdn.sspai.com/2023/06/27/fe47baff77b0aa04d455620d7fe29e13.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1)

**Lincoln** 好家伙，还带一键翻脸的。但好像比 Windows 的版本号要简短一点？

**Platy** 其实跟 Windows 那边挺像的，我们来拆解一下：

文章来源: https://sspai.com/prime/story/windows-macos-version-number-explained
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)