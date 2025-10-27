---
title: Mac恶意软件MacStealer伪装成P2E应用程序大肆传播
url: https://www.4hou.com/posts/lkYl
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-21
fetch_date: 2025-10-04T11:32:37.691065
---

# Mac恶意软件MacStealer伪装成P2E应用程序大肆传播

Mac恶意软件MacStealer伪装成P2E应用程序大肆传播 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Mac恶意软件MacStealer伪装成P2E应用程序大肆传播

gejigeji
[技术](https://www.4hou.com/category/technology)
2023-04-20 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)111182

收藏

导语：恶意软件背后的攻击者会伪装成一家合法的游戏公司，寻找测试人员，并吸引潜在的受害者下载他们的应用程序。

趋势科技的研究人员检测到Mac恶意软件MacStealer通过网站、社交媒体和消息平台Twitter、Discord和Telegram大肆传播。MacStealer，是使用 Telegram 作为命令和控制 (C2) 平台来窃取数据的最新威胁示例。它主要影响运行 macOS 版本 Catalina 以及之后运行在 M1 和 M2 CPU 上的设备。现在该恶意程序又有了新的传播途径，攻击者通过假冒合法的游戏赚钱(P2E)应用程序的图片，引诱受害者下载它。P2E是Play-to-earn 的缩写,允许玩家通过玩游戏来产生稳定的加密收入。每个游戏的机制可能不同,但奖励通常来自质押、刷游戏币或生成可交易的NFT物品。

趋势科技的研究人员最近分析了一种名为MacStealer的Mac恶意软件(检测为TrojanSpy.MacOS.CpypwdStealer.A)，这是一种加密货币钱包和信息窃取程序，伪装成合法游戏赚钱(P2E)游戏应用程。研究人员已经发现MacStealer的源代码已经通过在线公共扫描服务泄露。该恶意软件目前通过第三方网站传播，使用从真实P2E应用程序中窃取的图像和图形，并在社交媒体和消息平台Twitter、Discord和Telegram上传播。恶意软件背后的攻击者会伪装成一家合法的游戏公司，寻找测试人员，并吸引潜在的受害者下载他们的应用程序。

**引诱新玩家**

与其他在感染设备的同时重定向用户的假冒应用程序不同，攻击者没有假装创建游戏，只是从现有的P2E中复制。Twitter账户和网站只是吸引用户下载MacStealer的幌子。一旦恶意软件执行，用户就会在GUI提示中输入各自的密码，存储在设备中的特定信息就会被窃取。

研究人员的传感器在例行检查中检测到了高危示例进行分析，经过仔细检查，发现worldofcretures[.]io网站与示例有关，该网站在Twitter上得到了大肆传播。

检查该网站后台发现假冒应用程序的页面是在2023年1月才创建的，所有的图形和文本都是直接从另一个P2E应用程序的网站上获取的。这款假冒应用程序的推特页面图像也直接取自合法应用程序的社交媒体页面，于2022年10月创建，与2021创建的合法应用程序帐户相比，这是相对较新的。不知情的受害者可能没有听说过这款游戏，他们很容易将假冒页面误认为是合法应用程序的原始游戏和官方社交媒体账号。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114294324116.png "1681114294324116.png")

真实游戏的网页（上）和假冒游戏的网页（下）

这些网站在很多方面都有所不同（例如图形、名称和公司），如果感兴趣的用户知道这些细节，这些网站仍然可以识别。社交媒体帖子包括下载该应用程序的促销活动，让新玩家似乎只要连接到Discord渠道并下载游戏就可以获得免费赠品。一旦用户加入攻击者的渠道，攻击者就会通过聊天说服用户点击恶意链接或下载恶意软件文件。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114304109314.png "1681114304109314.png")

假冒应用程序的帖子示例，用于重定向潜在受害者，并在Discord上“下载”游戏

**技术细节**

一旦受害者下载了游戏，一个名为LauncherMacOS的.dmg文件，dmg（SHA256:8ea33c34645778b79dd8bb7dcf01a8ad1c79e7ada3fd61aca397ed0a2a57276，被Trend Micro检测为TrojanSpy.MacOS.CypwdStealer.A）在系统中执行。签名如下：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114313114652.png "1681114313114652.png")

特别签名在ARM64 M1苹果处理器上尤为重要。它要求所有本机代码都有有效的签名（如果只是临时的），否则操作系统将不会执行它。相反，它会在启动时阻止本机代码。

在检查dmg中的应用程序包时，研究人员观察到它包含以下使用Python编译器Nuitka编译的Mach-O二进制文件：

启动器（SHA256:5e8f37420efb738a820e70b55a6b6a669222f03e4a8a408a7d4306b3257e12ff，被Trend Micro检测为TrojanSpy.MacOS.CpypodStealer.A）Nuitka是一个不常见的编译器，在测试过程中，主要的Mach-O显示出可疑的网络活动。研究人员还注意到Nuitka可以将Python脚本编译成Mach-O二进制文件。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114323638785.png "1681114323638785.png")

DMG示例的应用程序捆绑内容

程序本身分为两个阶段。第一个阶段是Nuitka引导程序的执行。就其本身而言，逻辑本身是无害的，但会将恶意负载释放到目标路径，而第二阶段是执行恶意负载。

恶意软件的第一阶段实现以下例程：

1.它从一个名为“有效载荷”的特殊部分读取内容。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114332124649.png "1681114332124649.png")

由恶意软件二进制文件提取的部分

2. 它将内容写入路径为

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114344543592.png "1681114344543592.png")

第二阶段Mach-O二进制文件释放到系统上

3.它将环境变量NUITKA\_ONEFILE\_PARENT更改为当前进程号。

4.它执行提取内容的主要可执行文件，并清理引导版本本身。

第二阶段可执行文件是一个基于CPython实现的程序，该程序由Nuitka从Python编译而成。在编译过程中，编译器会清除部分信息以提高程序的执行效率，而Nuitka转换的Python代码完全清除了原始字节码，无法恢复。由于不可逆的编译过程，研究人员无法从Python源代码的角度对其进行分析，但函数名称和动态行为日志提供了大量信息。

1.它试图从以下钱包中窃取数据：
Binance
Exodus
Keplr
Metamask
Phantom
Trust wallet

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114357510352.png "1681114357510352.png")

用于窃取钱包数据的函数

2.它试图窃取浏览器数据和密钥链。在测试过程中，研究人员在系统上使用以下命令发现了该示例，用于文件/目录发现和系统信息收集：

/bin/sh -c uname -p 2> dev/null

/bin/sh -c security default-keychain

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114368203649.png "1681114368203649.png")

用于窃取钥匙链和钱包数据的函数

3.它使用chainbreaker转储钥匙链。

4.弹出对话框，使用osascript骗取用户密码，命令如下：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114381211774.png "1681114381211774.png")

对话框标题为“系统首选项”，图标警告默认答案为“隐藏答案”。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114391888636.png "1681114391888636.png")

获取受害者密码的对话框

5.它试图将收集到的信息以Zip文件的形式发送到命令与控制（C&C）服务器mac[.]cracked23[.]网站。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114400172408.png "1681114400172408.png")

泄露数据的网络数据包（顶部）和Zip文件的内容

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114409157537.png "1681114409157537.png")

发送到C&C服务器的general\_info.txt文件的内容

一旦下载并在受害者的系统中运行，MacStealer就会窃取受害者的钱包数据，并清空加密货币钱包。如果受害者没有加密货币钱包，恶意软件就会窃取用户信息和钥匙链。

**通过社交媒体和其他平台传播**

在扫描其他社交媒体帖子时，研究人员发现了攻击者尝试传播MacStealer恶意软件的努力。考虑到使用的战术、技术和过程（TTP）是相似的，这个示例和部署可能是一个组织完成的。在本节中，我们以Impulse Flow假冒应用程序为例。

攻击者创建一个Twitter账户和相关网站来宣传假冒的游戏应用。以下是一个带有验证图标的Twitter账户示例。然后，他们将游戏宣传为基于区块链技术的免费P2E在线游戏。

有一个链接树链接，其中包含到他们其他通道的链接，Linktree 是一家在线工具平台，可以让你在社交媒体上展示自己或品牌的多个网站链接。Linktree 的主要业务是提供一个简单易用的工具，让用户能够在 Instagram、TikTok、Twitter 等社交媒体上分享多个链接，从而帮助他们更好地展示自己或品牌，增加流量、转化率和销售额，其中包含指向其他渠道的链接：

Website: https[:]//play-impulseflow[.]com/

Website: https[:]//impulse-flow[.]gitbook[.]io/impulse\_flow-whitepaper/

Website: https[:]//github[.]com/ImpulseFlowBeta/1[.]0[.]3

Discord: https[:]//discord[.]gg/Impulse-flow

Twitter: https[:]//twitter[.]com/lmpulse\_Flow

Telegram: https[:]//t[.]me/impulseflow\_official

图片搜索查询显示，推特和其他社交媒体账户中使用的媒体(图片和视频)抄袭了游戏《余烬之剑》(Ember Sword)。Ember Sword是一个多资产的虚拟经济游戏，其主要功能是支持用户社区购买，出售和使用游戏专属虚拟资产。在Ember Sword中，用户可以购买，出售和发行各种游戏币和令牌，包括经典货币，装备，材料和其他供玩家交易的内容，这种内容可以用来升级角色，改善游戏内的经济秩序，以及丰富游戏体验。攻击者利用这些平台诱使潜在受害者执行恶意软件可执行文件。所观察到的一些方法如下：

1.他们将其宣传为一款公测游戏，并吸引人们参与他们的测试计划以换取奖励。这些测试人员被邀请加入攻击者的Discord或Telegram渠道，在那里他们会得到恶意软件二进制文件或下载恶意软件二进制文件的链接。在某些情况下，链接或文件将需要密码，他们通过Discord或Telegram渠道接收:https[://]twitter.com/lmpulse\_Flow/status/1633735911782400000。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114425371781.png "1681114425371781.png")

输入密钥可以让潜在的受害者下载MacStealer恶意软件二进制文件

2.他们直接向内容创造者传达信息，帮助他们推广游戏。这被怀疑是一种针对这些有影响力的人的社会工程策略。

https[://]twitter.com/powrdragn/status/1638024217412390913

https[://]twitter.com/ender\_thien/status/1637659072379101185

https[://]twitter.com/naerycrypto/status/1637226997817692161

https[://]twitter.com/CiervoKing/status/1637220583736762370

3.他们发布虚假的职位空缺，并引诱求职者下载他们的恶意软件二进制文件：https://twitter.com/witty\_taeil/status/s1631654308218298368。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114451790979.png "1681114451790979.png")

一些人在推特账户上发布了关于与假冒游戏应用程序和网站相关的恶意活动的警告。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230410/1681114463268032.png "1681114463268032.png")

一些用户据称是MacStealer恶意软件的受害者

**总结**

虽然P2E游戏并不新鲜，但它正在重新引起人们的兴趣，越来越受欢迎，而攻击者也在努力利用这一不断增长的趋势。MacStealer恶意软件只是众多利用P2E吸引力的恶意软件之一。P2E游戏玩家最适合成为攻击目标，因为这些游戏的经济模式要求他们使用加密货币和钱包。

安全研究人员可以发现，考虑到攻击者使用Discord和Telegram直接与受害者沟通，使用不常见的手段传播恶意软件，调查分析恶...