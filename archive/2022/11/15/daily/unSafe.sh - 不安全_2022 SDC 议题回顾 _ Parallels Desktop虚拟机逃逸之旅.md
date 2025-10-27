---
title: 2022 SDC 议题回顾 | Parallels Desktop虚拟机逃逸之旅
url: https://buaq.net/go-135579.html
source: unSafe.sh - 不安全
date: 2022-11-15
fetch_date: 2025-10-03T22:42:35.555232
---

# 2022 SDC 议题回顾 | Parallels Desktop虚拟机逃逸之旅

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

![](https://8aqnet.cdn.bcebos.com/46585061e4735a3d38d11bdb40233057.jpg)

2022 SDC 议题回顾 | Parallels Desktop虚拟机逃逸之旅

01研究动机与目标选择首先我们先看一下议题概览，简单的介绍一下为什么我会选择这个目标，当时我在做这个的时候是完全没有接触过虚拟机逃逸的，当我刚开始接触虚拟机逃逸的时候，我就想如何展开这个项目并快速的挖
*2022-11-14 17:59:19
Author: [mp.weixin.qq.com(查看原文)](/jump-135579.htm)
阅读量:20
收藏*

---

**01**

**研究动机与目标选择**

首先我们先看一下议题概览，简单的介绍一下为什么我会选择这个目标，当时我在做这个的时候是完全没有接触过虚拟机逃逸的，当我刚开始接触虚拟机逃逸的时候，我就想如何展开这个项目并快速的挖到一些漏洞，然后继续去推进这个研究项目。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0hibviclnzX5WtDhWNpBYg3UuT5ics0750462wiaicwrLynJSYyia8KL7qsmA/640?wx_fmt=png)

接着我介绍如何从Parallels Desktop虚拟机，我怎么逃逸到masOS后的一些常见的攻击面分析。为什么我选择Parallels Desktop呢？因为首先我是对虚拟机逃逸非常的好奇，你只有好奇你才能去有动力去理解它到底的底层原理是什么。

而且虚拟机逃逸在当下云计算这个环境下面，其实是有实际的研究价值的。同时，我希望在一个实际的目标的研究过程中，去检验自己的能力是否有提高。比如说我在做代码审计的时候，我认为我这套审计代码的这套体系是否完善，我的立项能力是不是能支撑我对这个代码审计的一个需求，我发现漏洞之后，我觉得是漏洞或者可能是漏洞的这个问题，我能不能转化为利用。

我们在开展一个目标之前，我们首先要选择一个合适的研究目标。不能比如说Hypver-V虚拟机打穿后价值最高，我就去搞它，但是我从来没有搞过虚拟机，我一上来定个很高的目标，很可能就干到一半，撞个墙直接就撞死了。

那么我们首先要选择一个自己熟悉的，因为我之前是在做 Mac平台的一些工作，那么Mac上我是最熟悉的，我可以减少很多工作量。

其次就是要找一个相对容易发现漏洞的目标，就是说，比如上去我可能花个一周的时间可能会找到至少是一些崩溃，那么跟着崩溃我去进一步的分析，心理上可能就是觉得更顺其自然一点，如果我搞个一周两周三周连个崩溃都没有看见，那很痛苦。

首先Parallels Desktop for MAC，它是一个在MAC平台上专门为苹果电脑提供虚拟化的一个工具，它也是我日常主力使用的一个虚拟机工具。那么在苹果的平台上，其实还有一些其他的，qemu 和 Visualbox 等等，但是这些有的是开源的，还有就是VMWare，VMWare可能大家攻防做的比较多了，又比较难搞。

**02**

**虚拟机逃逸初探**

所以我选择 Parallels Desktop，为什么？因为首先刚刚我说它是Mac OS上的一款虚拟机产品，macOS是我最熟悉的环境，其次我在做一些基础调查的时候，我看到了一些漏洞报告，这是一个印度的安全研究员的漏洞报告，大家可以看到它的poc非常简单，它就是在0x3c4 0x3c5 0x3c6 这硬件的port上随机的生成一些数据，就把它打崩了。

我觉得那肯定 Parallels Desktop 代码质量不会特别的高，可以值得深入的看一下。

那么在没有任何积累的情况下，我是如何去展开审计工作的？首先我们要去看之前的一些漏洞报告，那么我刚才说的Parallels Desktop可能研究的人比较少，没有Parallels Desktop的漏洞研究报告，可能刚刚印度的研究人员的报告可能是我找到的唯一一篇，我只能看一些其他虚拟机产品的的漏洞报告。传统的漏洞报告一般是这样的，通常是说我有一个漏洞，我教大家我是怎么利用它的，那么利用的内容包括我如何触发这个漏洞，我可以得到一些什么primitive，然后我利用这些primitive的一些技巧是什么，以及最后我利用的整体流程是什么，然后给大家一个分享的代码，然后跑起来好，那么可能这个代码就跑通了，但这是完全不足够的，因为我只是知道了这个漏洞是如何利用的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0qNWdN0DvGpUG4THxDkrVuIic9oNnlhcQ5PibxibN2mosIGyVr5emOcWwQ/640?wx_fmt=png)

我读完这个报告之后，我第一感觉是我学到了这个漏洞怎么利用，但我不知道怎么去挖，对吧？所以看完了这个报告之后，你真的看懂这个漏洞了吗？其实我觉得未必。那么我们首先要学会如何去阅读漏洞报告，也是在今年的 GP0的一篇文章里面，我第一次看到他们有这个系统的提炼出来，首先我要去分析它的 Root cause到底是什么原因导致的漏洞，这个是在漏洞报告里一般是不会写的，其次我要去看类似的问题是否存在，比如说同样的漏洞的pattern，是不是还有别的模块也有这个问题，或者说别的相似的实现里面是不是还有这种问题？在后面的实例当中，我会给大家解详细的看一下到底大概是什么意思，以及我分析一下它的修复是否合理，它的修复是否真的修掉了这个问题，它的修复有没有引入新的问题，最后才是这个漏洞是怎么利用的，我们只有带着这样的心情去阅读这个报告，我才能学会去通过阅读别人的漏洞报告，去提高自己漏洞挖掘的能力。

那么总结一下他常见的攻击面其实就几类，第一个最常见最基础的攻击面就是一个是vmtools的，比如说我两个虚拟机和 host之间和你的物理机之间拷贝数据，什么文件共享之类的东西，都是用这个vmtools来实现的。

在Parallels Desktop里面它有一个类似的东西，其次的话比较常见的就是虚拟虚拟设备，比如说虚拟网卡、虚拟显卡、虚拟USB外设，这些里面存在一些问题，那么实际上我是如何展开工作的，这是大家可以参考的一个我的个人经验，首先通过inline hook加上加上一些dumb fuzzing，大家现在也知道dumb fuzzing其实很难找到漏洞了。我们做最简单的fuzz，但dumb fuzzing目的并不是发现漏洞，而是获得一些简单的崩溃，如果即便不能发现崩溃，我通过inline hook我可以打开一些log的接口，我可以看到一些错误日志，我的dumb fuzz确实可以触及到我要攻击的代码，仅此而已就可以了，我并不指望这个东西真的可以发现好用的漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0zNclMQMq0IzQn1Fomf6cE357mz3eAKQzSF9WMzJTNSwT3V4Jibc2qSw/640?wx_fmt=png)

然后我再分析崩溃日志，或者我触发的一些错误，比如说告诉我什么size不对或者输入数据过长或者什么，告诉我我的输入有问题，被检测代码过滤了，我就可以知道这个地方其实是我有可能可以攻击的地方，我也可以借由这个分析，我大概了解一下它的数据的流程，数据走向是一个什么样的，然后这个时候我们的人工审计再介入，就是说我确认了这个数据我是可控的，我这个时候我就人工审计介入，因为我在拿到一个完全新的目标的时候，我并不能快速的确认就是哪些东西我人工投入进去看能出成果，最后发现一些漏洞，然后写poc然后再去写利用，同时这个地方有一个经验，一定要自己去写poc去写代码和你的研究目标进行一些交互。

我有很多漏洞其实是我认为API或者说我认为和系统交互做的事情是a，但其实他做的事情是b，我自己没看懂，我写了个poc写的是错的，但是开发人员不会这么写，莫名其妙触发一个崩溃，然后找到一些漏洞，所以一定要一定要自己去写代码去尝试和系统交互，有的时候会有意外收获的。

**03**

**从Parallels Desktop到macOS的虚拟机逃逸之旅**

那么我们首先接触第一个审计目标就是toolgate也就VMWare里的vmtools，首先它的实现是通过一个叫做prl\_tg的一个进程，它是跑在虚拟机里面的，就是我把虚拟机拉起来，我装了一个ubuntu之后，它会有一个叫做prl\_tg的进程，它是通过一些底层的类似于虚拟设备的一个东西，通过一些端口和内存映射和 host发生交互，然后有plr\_xxx这些进程去负责逻辑实现它。

完成逻辑之后，底层通过 prl\_tg和虚拟机进行通信，那么我的guest里面是windows或者是mac的时候，它的实现其实是类似的，那么这个时候我第一反应就是我要去分析一下toolgate他的请求大概是什么样的，因为他是在MAC平台跑了一个虚拟机，它的实现其实和我们在做MAC研究的时候的一个叫做mach message的东西其实是特别像。

通俗简单的来说，就是我们抽象的来说，它的消息请求的结构只有两种，第一种就是我发一个包，有ID，然后有inline data，可能是1024个字节。

第二种就是我把它叫做复杂请求，就是我告诉你ID是什么，然后我告诉你一个fd或者说一个它叫做 vitual address。就是我映射的地址，然后他再通过映射重新把共享内存拿出来，其实就两种方式去传递一块内存，那么我做的事情就是使用Frida去写了一个脚本，在send和receive的接口去下了hook。

下了hook的目的其实就是为了把这个其实就是一个嗅探工具，就是把它这个里面有什么东西捞出来，然后去修改 request的内容，做一些dumb fuzzing，然后其实很快的我就拿到一个崩溃。那么这个时候要做的事情其实就是分析崩溃，当时我的一个崩溃是在我印象中是在一个文件共享的什么打开一个目录之后，他在解析这个文件名字的时候，那崩溃说实话我都没看懂，他在解析一个字符串的时候出了问题，然后直接就崩了，但是我觉得不好用，我都没有细看，但是我借由这个崩溃，我把Parallels Desktop从guess到host的交互流程，我把它理清楚了，我大概理了一周左右把它理清楚了。

然后这个时候我们之前实验室的一个同事他也跑来搞这个了，他告诉在Linux平台下面有开源的ToolGate头文件。

其实这个头文件里面写的很清楚，大家可以看到左边这个图，它的request就是不同的id代表了不同的功能，然后借由这个东西我就去专门去看了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EUvNq2rQycZibURG09OtYP00kYx2pTkclZQicCf4w4Or63tMo7IJziaT1RJQSVNF6eJoCW8xalT99PQ/640?wx_fmt=png)

这个叫做drag and drop，其实就是我从外面往里面拖，我在这里面我就针对性的看了一下，我找到了在Parallels Desktop里面第一个可以用的漏洞，为什么这里只贴了一个PRC，因为这个漏洞太久远了，当时我找到这个漏洞之后，我只找到这是一个inform leak，我可以借由他去过掉这个地址随机化，我找到这个漏洞之后，过了好久我都没有找到可以用的溢出，导致在某一个版本修复之后，这个leak被这个版本更迭修掉了。

那么后面我看到了虚拟文件共享的功能，虚拟文件共享的功能我发现它是默认开着的，我只要装一个虚拟机，它是默认开着的，然后而且它是默认共享后目录的，我的虚拟机里面我装一个ubuntu，我的ubuntu启动之后，它默认是把我mac的home目录已经共享到虚拟机里面了，很神奇，就觉得不太正常，一般我们可能会在MV的时候，它可以让你选择我共享哪些文件，但是在Parallels Desktop他没有让我选，它默认就全部共享进来了。

很奇怪这到底是它的特性还是它的一个bug，然后上网搜了一下，可能在好多年前就有人提出过这个问题，那么我构建了我做的第一个虚拟机逃逸了，因为你加载home目录，Mac OS home目录已经被共享进来了，那么我完全可以看到 Parallels Desktop的这台虚拟机的配置文件，我在我这台虚拟机配置文件里面有一个也是和文件共享的，有一个叫做 SHARE ALL MAC DISK，就是把整个MAC的磁盘共享进来，它本来是0，我把它改成1了。我随便找了一个DOS的洞，把我的虚拟机打崩了之后，就等着他重启，重启完了之后我就能拿到所有的数据了，当然做得很粗糙。

然后在pwn2own中洞被撞掉了，被撞掉了之后，我去看了一下别人的利用，这个我贴在PPT里面，大家有兴趣可以自己去看一下，别人的利用当然比我优美的多了。

那么我的第二个审计目标就刚刚说的虚拟设备，在Parallels Desktop虚拟机设备的实现，它是底层的逻辑是在一个叫做libmonitor.dylib的一个里面去实现了它的底层，它的虚拟设备的抽象的逻辑，它是在prl\_vm\_app里面去实现，它是分两段去实现的。分别实现底层逻辑和业务功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EUvNq2rQycZibURG09OtYP06zjVm7fm3R123lExic3VmWbHGLxUQ9pNDTflicFOxIeD9WLZp0vqibUgQ/640?wx_fmt=png)

那么主要我就去看了一下libmonitor.dylib的底层的，因为说实话底层实现相对简单一点。我找到一个叫做create\_device个虚拟设备的创建函数。它这个里面大家可以看到倒数第二个参数，它是一个handler，就是我的输入和输出是如何通过这个函数去分析的去处理的，在这个virt-io的这个的device里存在一个非常明显的漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0EThP1QicfiaciazZtrTJx5pmSHiaT1zgciaN1LlEbQNWpwwdwYaR0NnYibBQ/640?wx_fmt=png)

大家看到这个case 4其实是我们可以写的任意一个值，这个case 6用我们任意值去做一个索引，从一块内存里面去读写，它是一个很明显的越界读写。然后一个越界读写就很容易，如果大家是搞漏洞了，非常清楚，我把它转换成一个任意读写，然后绕过它的边界地址随机化，最后完成一个虚拟机逃逸。

然后在pwn2own中洞又被撞掉了。

在我创建一个虚拟机的时候，它可以让我选择Apple的hyper。我发现苹果大力的发展了自己虚拟机的技术栈，首先它肯定是苹果的新特性，苹果的新特性代表他写了大量的新代码，大量新代码，首先肯定是存在新的攻击面，因为新的代码肯定会引入漏洞。

我们第三个审计目标就是 Apple的hyper，首先我们要看一下 Apple，因为我们平时在做MAC研究的时候，显卡是我们一个常见的攻击面，其实我个人对显卡更熟悉一点。那么大家可以看到就是说在正常的一台物理机的显卡工作，我一个应用层进程通过io-kit就是苹果的一套虚拟内核沟通的东西和显卡驱动沟通。那么在物理机的环境当中，这个是我们macOS/iOS常见的一个攻击面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0ME9q2WanrAWkwWb5uHj9Jvk3uCovibLwaOaqYGias9icnEPtiattA9HoWQ/640?wx_fmt=png)

通过分析虚拟机显卡渲染的request的请求，然后dumb fuzzing确认攻击面，最后通过我获得的一些崩溃，迅速的去定位了攻击面的代码。

通过一个内核的简单dumb fuzzing工具，我获得了以下崩溃。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0WhYP6VYrV9bvx8U3Tq7cicaOeeUYQqePDLXicUFMURRjxqaibktTUowuA/640?wx_fmt=png)

然后我去逆向看了一下调用栈，我发现它崩溃在了这个叫pgfif process的函数。

那么我通过继续通过逆向分析，我们可以看到有大量的不同的message，我可以去去调用，然后这里面就肯定是有大量的攻击面的，每一个函数可能都有问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0Kz2ZF0T11Bl01vOWWbHuMhCWZjcp3mvCTicxjZZiaLDlPFjv0c2RPdibg/640?wx_fmt=png)

我着重看了一下当时我拿到崩溃的调用栈，我继续做了一些逆向分析，最后进到prepare resource这个函数里面。然后我可以看到里面有大量的decode的函数，然后我去逐个看了一下，在里面发现了一个越界写漏洞。结合一个信息泄漏漏洞完成了对macos虚拟机到macos物理机的虚拟机逃逸。

Parallels Desktop逃逸之旅就到此结束了，特别感谢工作中提供帮助的同事还有朋友，谢谢大家。

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MjM5NTc2MDYxMw==&mid=2458483697&idx=1&sn=129f76a91f260fbc0842d7341f6db83e&chksm=b18e4b7b86f9c26d1aab859df418ea70b40584a78908c94c51a6910878366854bb3e55cf3757#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](...