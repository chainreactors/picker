---
title: “伪装广告”：谷歌的Ad-Words被威胁分子大规模滥用，攻击众多组织、GPU和加密货币钱包
url: https://www.4hou.com/posts/JXmg
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-08
fetch_date: 2025-10-04T03:18:59.319820
---

# “伪装广告”：谷歌的Ad-Words被威胁分子大规模滥用，攻击众多组织、GPU和加密货币钱包

“伪装广告”：谷歌的Ad-Words被威胁分子大规模滥用，攻击众多组织、GPU和加密货币钱包 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# “伪装广告”：谷歌的Ad-Words被威胁分子大规模滥用，攻击众多组织、GPU和加密货币钱包

布加迪
[新闻](https://www.4hou.com/category/news)
2023-01-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)151274

收藏

导语：一项新发现的滥用谷歌广告关键字（ad-words）强大广告平台的技术正在大规模传播恶意推广搜索结果。

一项新发现的滥用谷歌广告关键字（ad-words）强大广告平台的技术正在大规模传播恶意推广搜索结果。这些搜索结果指向所谓可信的广告网站（实际上完全由威胁分子控制），它们被用来伪装，并将广告点击者重定向到恶意钓鱼页面，从而获得谷歌搜索结果的强大可信度和广告投放功能。威胁分子添加定制的恶意软件载荷后，通过Grammarly、Malwarebytes和Afterburner等广告关键字，以及Visual Studio、Zoom、Slack甚至Dashlane攻击目标组织，提高在个人电脑上成功部署恶意软件的机率。

我们将披露这种技术，展示实际的例子，并揭露名为“Vermux”的最大威胁团伙之一，该团伙利用大量的“伪装广告”（masquerAds）网站和域名（主要来自俄罗斯），攻击美国居民的GPU和加密货币钱包，这些活动已经引起了美国联邦调查局（FBI）的注意。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539663184690.png "1672539663184690.png")

图1. 威胁分子在谷歌广告流中伪装其恶意网站的广告

**谷歌广告的视角**

谷歌广告平台信誉卓著，可能是世界上使用最多的广告平台之一，这有其充分的理由。我们都习惯不仅用它获得有效相关的广告，还通常快速导航到我们所寻找的网站。

比方说，你搜索Grammarly，最终摆脱所有那些拼写错误。你在搜索栏中输入“Grammarly”，按回车键，然后迅速在搜索结果页面的顶部获得官方（可能是推广的）Grammarly网站。很容易。这也是谷歌看到的——他们得到与广告登录页关联的关键字的竞价。广告客户是有效客户吗？广告网站是合法网站吗？没问题，你的广告已投放！

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539676492934.png "1672539676492934.png")

图2. 从谷歌广告的角度来看，一起标准的推广搜索结果广告活动

从更广泛的角度分析这个简单的广告流，并考虑到网站主机和访客的异常行为，我们发现了许多传播恶意软件的恶意活动，目的和来源各异——完全使用谷歌广告平台进行传播。这个效果颇好的概念甚至已经引起了联邦调查局的注意。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539688911819.png "1672539688911819.png")

图3. 品牌、广告关键字和知名搜索引擎都落入威胁分子的手里

**一个简单的技巧就能避开谷歌广告的注意**

这个技巧很简单——创建一个良性网站，用想要的关键字进行推广，并保持它在策略执行者眼中有效且安全。不过，那些“伪装”的网站被目标访客（那些实际点击推广搜索结果的人）访问时，服务器立即将他们重定向到恶意网站，进而重定向到恶意载荷——它们通常也隐藏在信誉良好的文件共享和代码托管服务器中，比如GitHub、Dropbox或discord的CDN等。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539708537173.png "1672539708537173.png")

图4. 谷歌广告的背后到底发生了什么？

那些恶意网站实际上是访客看不见的，在爬虫程序、机器人程序、偶尔的访客，当然还有谷歌的策略执行者看来，真正的推广流（比如以有效的gclid值到达）显示为良性的无关网站。2022年12月期间活跃的此类广告流的几个例子可以在这里看到——左边显示了谷歌实际上做广告的被屏蔽网站，右边显示的是广告点击者被重定向到的实际钓鱼网站：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539718351798.png "1672539718351798.png")

图5. 钓鱼攻击美国第一银行客户/利用uTorrent、Audacity和Brave等品牌传播恶意软件

为了深入研究这起骗局的技术细节，以下是2022年11月下旬观察到的一路针对Grammarly的真实样本流。推广搜索结果会将你发送到域名grammalry[.]org，这是“Christian供暖和空调”广告，只向那些直接访问它的人投放。如果你点击了这个推广搜索结果，就生成一个唯一的点击id（谷歌的Click ID，或gclid），由威胁分子加以检查；如果有效（而且只有效一次!），结合其他参数，比如访客的地理位置和用户代理等，它会将你转发到域名gramm-alry[.]com下的恶意Grammarly钓鱼页面。

请注意，转发在服务器端完成，隐藏起来、不被谷歌以及永远不会看到“伪装广告”网站的访客看见，看见的只是实际的钓鱼页面：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539732186075.png "1672539732186075.png")

图6. 从搜索下载Grammarly到下载和安装恶意负载

**Gramnarly恶意软件——Raccoon窃取器变种**

不，这不是拼写错误……gramnarly[.]com只是其中一个Grammarly品牌的钓鱼页面。不，他们不会等别人拼错域名。只需要竞购Grammarly广告关键字，并创建“伪装广告”流：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539747248239.png "1672539747248239.png")

图7. Grammarly品牌的伪装广告流

既然这些威胁分子不需要浪费时间和精力就能覆盖到最相关的目标（谷歌为他们做到了这点），他们可以在恶意载荷上投入更多的精力。的确，在这起活动中，Grammarly载荷并不是普通保护机制可以快速检测到的简单窃取器。我们看到的一些更值得关注的特征包括如下：

与实际软件捆绑——安装Grammarly品牌的恶意软件实际上会安装Grammarly的副本。当然，它与悄然从事所有恶意活动的另一个可执行文件捆绑在一起。

臃肿的文件——安装可执行文件（或其他变体的容器压缩包）充斥着臃肿的零文件，只是为了使文件比自动恶意软件分析系统的最大允许大小更大，通常为500Mb及以上。此外，把带有恶意代码片段指纹的代码降到1%以下是另一种减少检测的好方法。动态执行是真正发现问题的最有效方法——我们几乎看不到任何当前的保护供应商自动执行这些巨大的文件。

定期更改载荷——由于规模较小，每天可以使用细小的更改来重新创建载荷，使用窃取器或加密货币挖矿软件等恶意软件的不同恶意载荷。所以有一天你从dropbox文件夹下载了Raccoon窃取器 ，下一天它成了来自discord CDN服务器的可执行MSI文件中的Vidar窃取器。

即使对Virus-Total而言，我们提交的内容也花了好几天才得到启发式检测：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539764749757.png "1672539764749757.png")

图8. 从grammartly[.]org下载的Grammartly.exe

当前的Virus Total报告在此： https://www.virustotal.com/gui/file/3baf692a1589355af206f4e3886a09fe8997f0b62c78c1403556285eaba40e94/detection

**Vermux——针对GPU的大规模活动**

滥用这种技术进行传播的大规模活动无疑是我们称为Vermux的攻击GPU的威胁分子。Vermux针对任何拥有或可能拥有GPU硬件的计算机，通过攻击受这类PC用户欢迎的相关品牌的软件工具或驱动程序来攻击。

列表顶部是关键字“Afterburner”，指MSI Afterburner显卡工具，可以在这些真正的搜索结果中看到，显示adBuffer域名afterbern[.]live如何出现在列表顶部：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539777758420.png "1672539777758420.png")

图9. 真正的搜索结果显示了推广的伪装广告网站afterbern[.]live

Afterburner被许多游戏玩家以及图形设计师用来控制、超频和榨取GPU。Vermux针对的就是这种GPU，不过出于另一个原因：挖掘加密货币。的确，点击上图所示的推广搜索结果，最终会将你重定向到隐藏的恶意网站，它看起来与原始网站一模一样：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539788168726.png "1672539788168726.png")

图10. 你能看出区别吗？（右边是假的）

几周前，研究人员注意到MSI Afterburner活动的载荷，这种载荷其实很难被检测到。我们充分了解伪装广告这种难以捉摸的传播技术后，得以发现Vermux的全面性和多用途性——其覆盖范围远不止一个虚假的Afterburner安装程序这么小。

Vermux在主要位于俄罗斯的服务器上部署了数百个域名、“伪装广告”网站以及钓鱼页面，主要向美国和加拿大居民投放恶意广告。这伙威胁分子滥用大量品牌，并不断演变。

主要的攻击途径是追踪这些GPU。以下是表明adBuffer流在2022年11月至12月期间活动的几个例子。首先是流行的MSI Afterburner，我们已在上面看到：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539800138646.png "1672539800138646.png")

图11. Vermux MSI Afterburner流

另一个备受GPU用户欢迎的知名品牌是开源3d编辑和渲染软件“Blender”：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539814502545.png "1672539814502545.png")

图12. 针对Blender用户的伪装广告流

除此之外，Vermux还利用其他途径获取更多利润——一些针对加密货币钱包和密码，一些针对Vermux能获得控制的其他流行工具，还有一些直接针对交易或银行账户：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539826104003.png "1672539826104003.png")

图13. Vermux操纵的伪装广告流的另外几个例子

**Vermux恶意软件载荷——在GitHub上免费投放**

Vermux的载荷主要基于用来控制的Vidar木马，以及针对基于python的Monero挖矿软件的一些专有编译。这些文件遵循我们之前提到的规则，这使得它们难以被发现。Vermux不仅滥用谷歌广告的声誉和传播力量，还滥用BitBucket、GitHub、Dropboxx和OneDrive等已知文件共享服务和代码库的声誉。下面是在GitHub中发现的此类代码库的几个例子：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539841132312.png "1672539841132312.png")

图14. GitHub上的MyNameisVermux公共代码库

上述是一个名为sofwarefree的代码库，用户Dor4il135上传了不同的“恶意软件化”安装包，面向Slack、OBS、Blender甚至Norton Antivirus（18.exe）。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230101/1672539852147653.png "1672539852147653.png")

图15. GitHub上的Dor4il135公共代码库

最后一个是Dor4il135自己的代码库活跃了一个多月，现在终于被下架了。一个月的时间够长了，它投放与Vidar及其他恶意软件变体捆绑在一起的不同类型的软件，几乎每天都会以新版本加以更新，主要是为了改变二进制足迹以免被检测。

**总结**

安全说白了是信任的问题——因此，我们在网络上的日常活动不断依赖信誉良好的供应商。人无完人，可能更多的坏人利用这些安全漏洞，其手法是我们无法想象的。本文披露了这一点——强大的广告系统、全球内容交付和安全基础设施背后的那些公司与那些行踪捉摸不定的威胁分子不断较量，威胁分子设法隐蔽起来，利用值得信赖的其他品牌牟取私利。

这个“伪装广告”概念很简单，但恰恰是那些威胁分子所需要的——滥用我们有时对谷歌及推广搜索结果盲目寄予的信任。除此之外，滥用信誉良好的文件共享服务以及知名软件品牌使威胁分子甚至逃避市场上最先进的终端检测和响应（EDR）产品。我们不可避免地要采取一种更注重行为的保护措施，即使是针对像谷歌搜索这种最常见的行为。

不要被拼写错误的域名所迷惑，总是仔细检查从哪里下载文件。

**攻陷指标（IOC）**

2022年11月至12月期间各种活跃域名和IP，包括恶意软件样本链接和virus-total分析：

https://gist.github.com/guardiolabs/2178c54367d20b0655b5cc5e9d297760

2022年11月至12月期间的Vermux活动：

https://gist.github.com/guardiolabs/7f46d1adda8b0c08e76f23d9fab27fe9

本文翻译自：https://labs.guard.io/masquerads-googles-ad-words-massively-abused-by-threat-actors-targeting-organizations-gpus-42ae73ee8a1e如...