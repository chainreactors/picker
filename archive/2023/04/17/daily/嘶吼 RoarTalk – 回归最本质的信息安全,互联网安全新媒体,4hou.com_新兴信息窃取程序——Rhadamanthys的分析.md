---
title: 新兴信息窃取程序——Rhadamanthys的分析
url: https://www.4hou.com/posts/3r1r
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-17
fetch_date: 2025-10-04T11:31:24.740157
---

# 新兴信息窃取程序——Rhadamanthys的分析

新兴信息窃取程序——Rhadamanthys的分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新兴信息窃取程序——Rhadamanthys的分析

gejigeji
[技术](https://www.4hou.com/category/technology)
2023-04-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)137936

收藏

导语：Rhadamanthys是一款很高级的信息窃取程序，于去年9月在暗网上首次亮相，亮相之初即受到了攻击者的热捧。

Rhadamanthys是一款很高级的信息窃取程序，于去年9月在暗网上首次亮相，亮相之初即受到了攻击者的热捧。

2022年9月24日，一个化名“kingcrete2022”的用户发布了以下内容：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680839953992855.png "1680839953992855.png")

开发者并没有急于将该产品投放市场，他们已经以“kingcrete2022”的化名在论坛上潜伏了半年，实际可能比其他化名的时间还要长。恶意软件的整体性构建在正式发布前整整一个月就已经编译完成了。在正式发布后，一系列疯狂的版本更新便开始了，开发者添加了一长串功能和子功能，并提供了英语和俄语支持。很快数千个用户的信息、数十万个密码和数百个加密货币钱包就被窃取。为了扩大攻击范围，开发者还对购买其服务的用户提供了售后服务。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680839973184594.png "1680839973184594.png")

**攻击目标**

理论上，Rhadamanthys的开发者并不关心用户如何处理窃取者窃取的非法数据，不管是实施欺诈、出售数据、发动内战，对开发者来说都是一样的。实际上，这种现成恶意软件的主要客户是投机取巧的网络犯罪分子，他们的目标是在任何时间感染任何人。因此，活动受害者遍布世界各地，特别是在一些地方，一些运营商已经开始进行创造性迭代了，比如一个活动以OBS studio等视频编辑软件为幌子传播样本，通过谷歌广告推送给不知情的受害者。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680839988485766.png "1680839988485766.png")

**攻击热图**

一般来说，操作这类恶意软件的攻击者通常不像大型勒索软件组织那样太关心大型目标。对他们来说，这只是一场数字游戏，即从众多受害者身上榨取金钱。尽管如此，从统计数据来看，这些攻击的最终目标确实是针对大型组织的；通过监测，我们能够确认Rhadamanthys试图感染加拿大的一家政府机构，以及印度基础设施部门的一家能源公司。

**功能概述**

Rhadamanthys中包含的功能非常多，其设计原则就是囊括信息窃取所需的一切功能和有关扩展。

Rhadamanthys的功能列表包括窃取受害者的系统信息：计算机名称、用户名、内存容量、CPU内核、屏幕分辨率、时区、地理位置、环境、安装的软件、屏幕截图、cookie、历史记录、自动填充、保存的信用卡、下载、收藏夹和扩展，它从FTP客户端窃取凭据——Cyberduck、FTP Navigator、FTPRush、FlashFXP、Smartftp、TotalCommander、Winscp、Ws\_FTP和Coreftp；以及来自邮件客户端CheckMail, Clawsmail, GmailNotifierPro, Mailbird, Outlook, PostboxApp, Thebat!, Thunderbird, TrulyMail, eM和Foxmail；它从双因素验证应用程序和密码管理器RoboForm、RinAuth、Authy和KeePass窃取凭据；VPN业务，包括AzrieVPN、NordVPN、OpenVPN、PrivateVPN\_Global\_AB、ProtonVPN和WindscribeVPN；笔记应用程序，包括NoteFly、Notezilla、Simple Stick Notes和Windows Stick Notes；即时通讯应用程序的消息历史记录，包括Psi+、Pidgin、tox、Discord和Telegram；此外，它还窃取了Steam、TeamViewer和SecureCRT的受害者凭据。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680840004314852.png "1680840004314852.png")

当Filezilla FTP凭据出现在攻击者端时被窃取

开发者特别强调了与窃取加密货币相关的功能，在一个版本更新中，有9项新功能，其中4项是对加密货币钱包的窃取和破解的增强。最初版本中支持的钱包列表确实很难处理，包括Auvitas, BitApp, Crocobit, Exodus, Finnie, GuildWallet, ICONex, Jaxx, Keplr, Liquality, MTV, Metamask, Mobox, Nifty, Oxygen, Phantom, Rabet, Ronin, Slope, Sollet, Starcoin, Swash, Terra, Station, Tron, XinPay, Yoroi, ZilPay, Coin98, Armory, AtomicWallet, Atomicdex, Binance, Bisq, BitcoinCore, BitcoinGold, Bytecoin, coinomi, DashCore, DeFi, Dogecoin, Electron, Electrum, Ethereum, Exodus, Frame, Guarda, Jaxx, LitecoinCore, Monero, MyCrypto, MyMonero, Safepay, Solar, Tokenpocket, WalletWasabi, Zap, Zcash 和 Zecwallet。

所有这些窃取行为都是在感染后自动执行的，如果攻击者决定对受感染的设备进行更多的操作，他们可以将新配置推到“文件抓取”模块，该模块将窃取与windows搜索查询匹配的所有文件或者对于真正的高级用户，将手工制作的powershell推到受害设备上执行。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680840019107599.png "1680840019107599.png")

在攻击者端出现时被窃取的环境变量

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680840033206746.png "1680840033206746.png")

“文件抓取”模块在攻击者端出现时窃取的文件

**技术分析**

**初步执行流程**

该恶意软件在进入信息窃取功能之前要经历六个执行阶段：滴管、shellcode、安装程序等。

在分析Rhadamanthys时，我们观察到分析样本的逻辑与上述文章中详细描述的逻辑之间的差异，这证明了恶意软件还在不断开发中。最值得注意的是NSIS加载程序DLL的行为，在我们分析的执行流中，它从C:\\Windows\\Microsoft.Net\\Framework\\v4.0.30319\\AppLaunch.exe创建一个挂起的进程，然后用注入的恶意代码逐个替换挂起的进程。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680840048211297.png "1680840048211297.png")

如上所述，注入的代码会依次加载几个执行阶段，其中一个阶段尝试从Al-Khaser项目中获取许多VM逃避，然后解绑ntdll.dll中的函数，以避免被检测到。最后，它解析了一个内部混淆的C2地址，并从其中下载包含实际信息窃取功能的最后阶段。

**分析孤立内存转储**

分析实际的窃取逻辑并不是那么简单，在无法访问实时C2服务器的情况下，分析师有两种选择。要么他们去执行一个全新的执行链，对所有阶段进行调试，并希望获得一个实时的C2服务器，该服务器会使用很多启发式方法将它们窃取；或者在不可读的状态下使用转储，这些转储是在C2仍然存在时从沙箱运行中获得的。在这种特殊的情况下，内存转储包含许多说明恶意软件大致行为的字符串，但是在进行适当的交互式反汇编之前存在许多障碍。

第一个也是最主要的障碍是缺乏API调用的解决方案。在反汇编程序中打开转储，然后进行函数调用，可以很快地运行一个必须是动态解析函数的自制导入表。转储是沙箱运行的产物，早就结束了，现在这些地址似乎毫无意义。我们能够使用下面将要解释的方法来解析几乎每个函数。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680840064339930.png "1680840064339930.png")

首先，我们知道，在沙箱运行期间，这些地址指向加载到内存中的DLL。第二，我们知道执行是在拥有代码名为Win10v2004-20220812-en的tria.ge环境中运行的。我们将自己的虚拟可执行文件上传到沙箱中，确保我们选择的环境与原始沙箱运行中使用的环境相同，然后查看我们选择的DLL并恢复DLL版本。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680840078580157.png "1680840078580157.png")

不幸的是，即使我们有DLL版本，微软也没有那么慷慨地提供DLL的历史版本供下载。这类问题有多种解决方法，你可以上winbindex查找。我们选择使用tria.ge的一个功能：许多用户要求提供手动转储执行流中生成的文件的功能。作为一种解决方案，沙箱引入了一项功能，允许用户转储他们想要的任何文件，只要他们打开windows文件资源管理器并手动删除那里的文件。好吧，如果我们尝试将kernel32.dll从C:\windows\system32中的驻留位置删除，操作系统将不会允许，但没有什么能阻止我们将文件复制到其他地方，然后删除副本。在原始沙箱运行期间加载到内存中的同一个DLL现在可以在分析结束后从分析报告的“下载”部分获得。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680840093143899.png "1680840093143899.png")

通过这种方式，我们下载了许多dll，这些dll是恶意软件或任何软件真正想要解析API的始作俑者，如advapi32.dll、user32.dll、msvcrt.dll、ws2\_32.dll等。现在我们可以在反汇编程序中打开这些文件，手动加载文件并为每个DLL函数分配虚拟地址。遗憾的是，我们还远远没有完成，因为我们仍然不知道DLL最初加载时的基址，甚至不知道特定的DLL包含某个内存地址所指向的函数。

即使不知道哪一个是相关的DLL，也可以通过简单的观察在一定程度上缓解，例如，在下图中，函数qword\_c5c08（指针值0x7ffbf1bd5f20）将注册表项作为参数，因此很可能来自advapi32.dll。但这不会适用于每个dll，我们不会总是足够幸运地找到一个函数，恶意软件会将这样一个硬编码字符串作为参数。更关键的是，即使我们以某种方式知道每个函数地址的正确DLL，这仍然不会告诉我们在最初的沙箱运行期间加载DLL的原始地址，这对于计算当时加载到内存中的函数地址(我们正在尝试解析)与我们在反汇编程序中打开的加载的带注释的DLL中的标记函数地址之间的rebase delta（基于深度学习的语音和自然语言理解模型训练平台）是必要的。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680840118144025.png "1680840118144025.png")

qword\_c5c08可能是一个以某种方式与Windows注册表交互的函数

为了克服这个障碍，我们注意到沙箱转储中的函数地址可能被划分为连续的序列，每个序列都是从同一个DLL导入的。这意味着，如果我们从表中取出10个qword指针，幸运的是它们都是从同一个DLL中解析的，那么当加载到内存中时，在该DLL中，这10个函数的地址之间将存在相同的差异。为了讲解方便，我们举一个示例：假设我们要解析的10个地址列表以某个地址AX开始，然后以AX+0x300、AX+0x500、AX+0x930等六个其他地址继续；进一步假设，在一个加载和注释的DLL中，我们发现对于某个地址AY，恰好AY+0x300、AY+0x500、AY+0x930等都是函数的地址。这是一个非常幸运的巧合，它本身就发生了，原始沙箱运行中的原始地址AX解析为我们注释文件中AY中的函数。通过查看与列表中的地址匹配的10个函数名，并验证它们似乎是沙箱中运行的软件所需的合理列表，可以进一步检查匹配情况。

以下IDAPython代码在加载的DLL数据库中运行时，将自动执行查找函数地址序列匹配项的任务：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680840147103554.png "1680840147103554.png")

例如，上图中看到的地址(我们怀疑是从advapi32.dll解析出来的地址)出现在以下10个地址的序列中：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680840167162034.png "1680840167162034.png")

我们打开从沙箱中转储的advapi32.dll文件的注释idb，加载上面的IDA脚本，并运行函数dll\_match，将此地址列表作为输入。作为输出，我们收到这些函数地址中每一个的正确分辨率。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680840182108397.png "1680840182108397.png")

事实证明，在沙箱运行期间加载到地址0x7ffbf1bd5f20的上述函数是RegQueryValueExW。使用这种方法，可以很容易地“挑选”并尝试对各种dll运行相同的脚本，以查看获得了哪些匹配，以及它们的可行性。虽然特定的工作流程不能很好地扩展，但如果需要的话，不难看出如何简化流程，例如，通过保留许多DLL版本的函数地址差异的预计算数据库，并对其进行所有差异比较。

窃取Chr...