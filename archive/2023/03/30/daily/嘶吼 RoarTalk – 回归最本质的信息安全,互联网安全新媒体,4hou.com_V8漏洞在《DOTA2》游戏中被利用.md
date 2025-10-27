---
title: V8漏洞在《DOTA2》游戏中被利用
url: https://www.4hou.com/posts/4Kg1
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-30
fetch_date: 2025-10-04T11:06:04.623465
---

# V8漏洞在《DOTA2》游戏中被利用

V8漏洞在《DOTA2》游戏中被利用 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# V8漏洞在《DOTA2》游戏中被利用

xiaohui
[漏洞](https://www.4hou.com/category/vulnerable)
2023-03-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)203196

收藏

导语：V8漏洞是如何在《DOTA2》游戏中被利用的？

![微信截图_20230311165308.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678524809149474.png "1678524809149474.png")

当我们想到V8的漏洞时，首先想到的可能是复杂的浏览器零日漏洞链。虽然浏览器可能是V8最有喜欢的攻击目标，但除了浏览器之外，这个开源JavaScript引擎也嵌入了无数的项目中。如果跨安全边界使用JavaScript引擎来执行可能不受信任的代码，则可能出现安全问题。

比如大受欢迎的Dota 2视频游戏。《刀塔2》也被称作《DOTA2》，由《DOTA》的地图核心制开发者IceFrog（冰蛙）联手美国Valve公司研发的一款游戏，是一款5v5多人对抗游戏。Dota使用了2018年12月编译的过时版本v8.dll。毫不奇怪，这容易受到一系列cve的攻击，其中许多甚至是已知的概念证明(PoC)利用的漏洞。我们发现其中一个漏洞CVE-2021-38003在游戏中发布的四个自定义游戏模式中被利用。由于V8在Dota中并没有沙盒检测，这个漏洞本身就允许对其他Dota玩家进行远程代码执行。

目前，我们已向《Dota 2》的开发者Valve透露了该发现。作为回应，Valve在1月12日推出了Dota的更新，升级了老旧且脆弱的V8版本。另外，Valve还采取了额外的行动，通过下架违规的自定义游戏模式，通知受影响的玩家，并引入新的缓解措施来减少游戏的攻击面。![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678524867774890.png "1678524867774890.png")

Dota 2是一款MOBA游戏，最初发布于2013年7月9日。尽管它是一款老游戏了，但它仍然每月吸引着约1500万活跃玩家。和其他流行的游戏一样，Dota是一个复杂的软件，由多个独立的组件组装而成。我们特别感兴趣的一个组件是Panorama框架。

这是Valve自己设计的框架，用于支持使用HTML、CSS和JavaScript这三大web元素进行用户界面开发。其中的JavaScript部分有问题，因为它是由易受攻击的V8版本执行的。因此，恶意JavaScript可以利用V8漏洞并获得对受害者设备的控制权。对于未修改的游戏来说，这并不是一个问题，因为默认情况下，只有合法的valve编写的脚本才会被执行。然而，Dota对玩家社区的自定义是非常开放的，这为攻击者打开了大门，他们试图将恶意JavaScript部分偷偷传递给毫无戒心的受害者。

Dota的自定义可以有多种形式，自定义可穿戴的游戏道具、解说员包、加载屏幕、聊天表情符号等等。最重要的是，这里还有社区开发的自定义游戏模式。这些游戏基本上都是全新的游戏，利用Dota强大的游戏引擎，让任何有一点编程经验的人都能实现自己的游戏想法。自定义游戏模式在Dota中扮演着重要的角色，Valve很清楚让玩家通过开发自定义游戏模式来表达他们的创造力的好处。毕竟，Dota本身就是《魔兽争霸3:冰封王座》的游戏模式。这可能就是为什么游戏模式可以在游戏中通过一次点击来安装，因此，有成千上万的游戏模式可供选择，其中一些非常受欢迎。例如，《DOTA AUTO CHESS》拥有超过1000万玩家。

在一个游戏模式可以被普通玩家玩之前，它必须在Steam商店上发布。发布过程包括Valve执行的验证。虽然这可能会清除一些恶意游戏模式，但没有任何验证过程是完美的。正如我们稍后将展示的，至少有四种恶意游戏模式设法通过。我们认为，验证过程的主要目的是防止不适当的内容被发布。有许多方法可以在游戏模式中隐藏后门，并且在验证过程中尝试检测所有后门非常耗时。

自定义游戏模式的主要游戏逻辑是用Lua编码的。这是在游戏服务器上执行的，它可以是主机玩家的设备，也可以是Valve拥有的专用服务器。对于客户端脚本，有来自Panorama框架的JavaScript。这主要用于控制用户界面元素，如记分牌或任务状态栏。JavaScript由V8引擎执行，并且完全支持许多高级特性，包括WebAssembly执行。

此外，还有一个特定于Dota的API，可以公开额外的功能。特别有趣的是$.AsyncWebRequest 函数，与eval结合使用，可以用于后门游戏模式，以便它可以执行从互联网下载的任意额外JavaScript代码。也许正是这种担忧导致$.AsyncWebRequest 函数被弃用并最终被完全移除。然而，有一些方法可以解决这个问题。例如，web请求可以由服务器端Lua代码发出，并使用游戏事件消息传递API将响应传递给客户端JavaScript。

我们在Steam商店中发现了四种恶意自定义游戏模式，它们都是由同一开发者开发的。第一个游戏模式（id 1556548695）特别有趣，因为从没有附加实际有效负载的情况来看，攻击者似乎只在该模式下测试了漏洞。有趣的是，攻击者还使用该游戏模式测试了其他各种技术，留下了注释掉的代码或未使用的函数。这为我们提供了一个了解攻击者思维过程的绝佳机会。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678524886170766.png "1678524886170766.png")

自定义游戏模式的Steam页面，攻击者在其中测试了漏洞

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678524902508880.png "1678524902508880.png")

如上图所示，攻击者对这个游戏模式的性质非常了解，将其命名为test addon plz ignore，甚至进行说明来敦促其他玩家不要下载这个游戏模式。虽然这看起来像是一种善意的表达，但我们很快就会看到，在其他三种恶意游戏模式中，相同的攻击者采取了完全相反的方法，并试图使恶意代码尽可能隐蔽。

这个自定义游戏模式中的JavaScript漏洞可以在overthrow\_scoreboard.vjs\_c中找到。这是一个实现记分板功能的合法JavaScript文件，但攻击者用CVE-221-38003漏洞替换了其内容。这个漏洞最初是由谷歌研究人员Clément Lecigne和Samuel Groß作为零日漏洞发现的，当时该漏洞在野外被用于攻击一款完全修补的三星手机。

现在有公开的PoC和该CVE的记录。然而，这些在2022年3月攻击者上次更新游戏模式时不可用。这意味着他们必须自己开发大部分漏洞（即使当时有公共PoC，攻击者仍需要掌握一些技术技能才能将其移植到Dota使用的过时V8版本）。

即使如此，漏洞的核心还是在CVE的Chromium 漏洞跟踪器条目中提供的。有一段代码可以触发漏洞，泄漏据称无法访问的TheHole对象，然后使用这个泄漏的对象破坏映射的大小。攻击者将此片段粘贴到他们的漏洞中，在这个损坏的映像构建其余的漏洞。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678524921115755.png "1678524921115755.png")

触发CVE-2021-38003漏洞

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678524938783274.png "1678524938783274.png")

有趣的是，该漏洞包含大量注释掉的代码和调试打印。这进一步表明，攻击者必须投入大量精力将漏洞武器化。攻击者开发的部分漏洞首先是使用损坏的映射来损坏阵列的长度，从而实现相对的读/写原语。然后，它破坏ArrayBuffer后备存储指针，以获得任意读/写原语。没有addrof函数，因为地址是通过将目标对象放置在距损坏数组已知的偏移位置，然后使用相对读取原语而泄漏的。最后，有了任意的读/写，该漏洞利用了一个著名的WebAssembly技巧来执行自定义shellcode。我们已经在Dota上测试了整个漏洞，并可以确认它是有效的。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678524954903860.png "1678524954903860.png")

从该漏洞中获取的JavaScript代码部分。请注意调试打印、注释和注释掉的代码

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678524974530778.png "1678524974530778.png")

除了这个JavaScript漏洞，自定义游戏模式还包含另一个有趣的文件，这个文件名为evil.lua。攻击者在这里测试了服务器端lua执行的能力，攻击者在其中特别测试了以下内容：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678524995955208.png "1678524995955208.png")

evil.lua

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678525016164859.png "1678525016164859.png")

不幸的是，我们无法访问此特定游戏模式的完整更新历史。因此，我们分析的版本中可能不再出现以前版本中一些有趣的代码。可以从更新日志中看到，这个游戏模式有9次更新，并且都发生在2018年11月或2022年3月。由于被利用的JavaScript漏洞是在2021年才发现的，我们假设游戏模式最初是一个合法的游戏，恶意功能只是在2022年3月的更新中添加的。

在发现第一个恶意游戏模式后，我们当然想知道是否还有更多这样的漏洞。由于攻击者没有向Valve报告该漏洞，我们发现他们很可能有恶意功能，并试图更大规模地利用该漏洞。因此，我们开发了一个脚本，可以从Steam商店中发布的所有自定义游戏模式中下载所有JavaScript文件。这为我们提供了千兆字节的JavaScript，可以查询可疑的代码模式。

没过多久，我们就发现了另外三种恶意游戏模式，并且都是同一个开发者(他也是之前分析的test addon plz ignore模式的开发者)。这些游戏模式被命名为Overdog no annoying heroes (id 2776998052), Custom Hero Brawl (id 2780728794)和Overthrow RTZ Edition X10 XP (id 2780559339)。有趣的是，同一位开发者还发布了名为《Petah Tiqwa》(id 1590547173)的第五种游戏模式，其中并没有包含任何恶意代码，这确实出乎意料。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678525037492959.png "1678525037492959.png")

其中一个后门自定义游戏模式的Steam页面

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678525058268377.png "1678525058268377.png")

这三种新游戏模式中的恶意代码名称非常有技巧。没有一个文件叫evil.lua或任何在源代码中直接可见的JavaScript漏洞。相反，它只是一个简单的后门，只有大约20行代码。这个后门可以执行通过HTTP下载的任意JavaScript，使攻击者不仅能够隐藏利用代码，而且能够自行更新它，而无需更新整个自定义游戏模式。

后门从JavaScript代码向服务器发送自定义ClientReady事件开始。这是向服务器发出信号，表明有一个新的受害游戏客户端正在等待接收JavaScript有效负载。服务器上的Lua代码为ClientReady事件注册了一个侦听器。当它接收到此事件时，它向其C&C服务器发出HTTP GET请求以获取JavaScript有效负载。此有效负载应在响应主体中，并在名为test的自定义事件中转发给客户端JavaScript。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678525078757165.png "1678525078757165.png")

后门的Lua部分，在游戏服务器上执行

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678525097863902.png "1678525097863902.png")

当客户端JavaScript接收到这个测试事件时，它将打开有效负载，动态地从中创建一个新函数，并立即执行它。在高层次上，这显然只是一个简单的下载器，能够执行从C&C服务器下载的任意JavaScript。客户端JavaScript和服务器端Lua代码的合作只是必要的，因为JavaScript不再被允许直接访问互联网。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678525115213907.png "1678525115213907.png")

后门的JavaScript部分，在游戏客户端上执行

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230311/1678525131144585.png "1678525131144585.png")

当我们发现这个后门时，C&C服务器不再响应。尽管如此，我们可以假设这个后门是为了下载CVE-221-38003的JavaScript漏洞。这是因为所有三种后门游戏模式都是由同一开发者在将JavaScript漏洞引入其第一个恶意游戏模式后的10天内更新的。然而，我们仍然不确定该漏洞是否附加了恶意shellcode。毕竟，在C&C中使用ngrok有点不合常规，可能表明攻击者只测试了后门功能。不管怎样，这次攻击规模不大。据Valve称，有不到200名玩家受到影响。

**总结**

在发现四种恶意游戏模式后，我们试图寻找更多的游戏模式，但没有找到。因此，目前还不清楚攻击者的最终意图是什么。然而，我们认为，出于两个主要原因，它们并非纯粹的研究意图。首先，攻...