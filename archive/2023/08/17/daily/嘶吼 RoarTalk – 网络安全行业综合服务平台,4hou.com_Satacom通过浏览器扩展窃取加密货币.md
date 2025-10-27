---
title: Satacom通过浏览器扩展窃取加密货币
url: https://www.4hou.com/posts/z4AZ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-17
fetch_date: 2025-10-04T11:59:08.209402
---

# Satacom通过浏览器扩展窃取加密货币

Satacom通过浏览器扩展窃取加密货币 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Satacom通过浏览器扩展窃取加密货币

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-08-16 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)110200

收藏

导语：我们将在本文介绍最近与Satacom下载程序相关的恶意软件传播活动。

![abstract_binary_connection-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154346383805.jpg "1691822359118164.jpg")

我们将在本文介绍最近与Satacom下载程序相关的恶意软件传播活动。Satacom下载程序释放的恶意软件的主要目的是通过对目标加密货币网站进行web注入，从受害者的账户中窃取比特币。该恶意软件试图通过为基于Chromium的网络浏览器安装扩展来实现这一点，该浏览器随后与C2服务器通信，其地址存储在比特币交易数据中。

该恶意扩展具有各种JS脚本，用于在用户浏览目标网站时执行浏览器操作，包括枚举和对加密货币网站的操作。它还能够操作一些电子邮件服务的外观，如Gmail、Hotmail和雅虎，以隐藏其与电子邮件中显示的受害者加密货币的活动。

**Satacom技术分析**

最初的攻击始于ZIP压缩文件。它是从一个似乎模仿软件门户的网站下载的，该网站允许用户免费下载他们想要的（通常是破解的）软件。该压缩包包含几个合法DLL和一个恶意Setup.exe文件，用户需要手动执行这些文件才能启动攻击链。

各种类型的网站被用来传播恶意软件。其中一些是带有硬编码下载链接的恶意网站，而另一些则通过合法的广告插件注入了“下载”按钮。在这种情况下，即使是合法的网站也可能在网页上显示恶意的“下载”链接。在撰写本文时，我们看到QUADS插件被滥用来传播Satacom。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154348759446.png "1691822376192706.png")

带有嵌入式QUADS广告插件的网站

该插件被滥用的方式与其他广告网络被滥用恶意广告的方式相同：攻击者推广看起来像“下载”按钮的广告，并将用户重定向到攻击者的网站。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154349187702.png "1691822410114502.png")

WP QUADS广告插件内的网站的内容

用户点击下载按钮或链接后，会有一系列重定向，自动引导他们通过各种服务器到达伪装成文件共享服务的网站，以传播恶意软件。在下面的截屏中，我们可以看到作为重定向链最终目的地的网站示例。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154349515934.png "1691822426177580.png")

虚假“文件共享”服务

用户下载并提取大约7MB大小的ZIP文件后，会显示一些二进制文件、EXE和DLL文件。DLL是合法的库，但“Setup.exe”文件是恶意二进制文件。它大约是450MB，但是填充了大量空字节，使其更难以分析。未添加空字节的文件的原始大小约为5MB，它是一个Inno-Setup类型的文件。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154350488258.png "1691822440144079.png")

添加到PE文件的空字节

Inno-Setup安装程序通常是这样的：在运行时，二进制文件将子安装程序提取到一个名为“Setup.tmp”的临时文件夹中。然后，它运行子安装程序“Setup.tmp”文件，该文件需要与主安装程序通信，参数指向原始“Setup.exe”及其包的位置，以便检索用于下一步安装的“Setup.exe”文件。

对于Satacom安装程序来说，Setup.tmp文件一旦运行，就会在Temp目录中创建一个新的PE DLL文件。创建DLL后，子安装程序将其进行自我加载，并从DLL运行一个函数。

然后，它解密Satacom的有效负载，并创建一个新的“explorer.exe”子进程，以便将恶意软件注入“explorer.exe”进程。

由此，研究人员可以得出结论，恶意软件在远程“explorer.exe”进程上执行一种常见的进程注入技术，称为进程空心化（process hollowing）。这是一种用于逃避检测的技术。

注入“explorer.exe”进程的恶意负载使用RC4加密实现来解密其配置数据，通信字符串以及受害者设备上其他释放的二进制文件的数据，加密的数据存储在恶意负载中。

恶意软件在每一步都使用不同的硬编码密钥来解密数据。恶意软件使用四个不同的RC4密钥来执行其操作，首先解密HEX字符串数据，将其用于其初始通信目的。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154350211765.png "1691822456163268.png")

RC4密钥（左图）和加密的HEX字符串（右图）

在上面的截屏中，左侧窗格将四个RC4硬编码密钥显示为HEX字符串，在右侧窗格中，我们可以看到使用RC4“config\_strings”密钥解密的HEX字符串以获得用于与C2通信的第一次初始化的字符串。如果我们自己使用密钥解密字符串，我们会得到截屏中显示的结果。

一旦HEX字符串被解密，“explorer.exe”将启动其第一次通信。为此，它通过Google DNS（8.8.8.8，另一个解密的字符串）执行对don-DNS[.]com（解密的HEX字符串）的DNS请求，并查询TXT记录。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154351374660.png "1691822475114780.png")

通过谷歌在don-dns[.]com上查询TXT记录

一旦请求完成，DNS TXT记录将作为另一个base64编码的RC4加密字符串“ft/gGGt4vm96E/jp”接收。由于我们拥有所有的RC4密钥，我们可以尝试使用“dns\_RC4\_key”解密字符串，并获得另一个URL。这个URL是有效负载的实际下载位置。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154352125737.png "1691822491121224.png")

TXT记录的解密字符串

**有效负载：恶意浏览器扩展**

Satacom下载程序将各种二进制文件下载到受害者的设备上。在本次活动中，研究人员观察到一个PowerShell脚本正在下载，该脚本安装了一个恶意的基于Chromium的浏览器扩展，该扩展针对Google Chrome、Brave和Opera。

扩展安装脚本负责从第三方网站服务器下载ZIP压缩文件中的扩展。PowerShell脚本将压缩文件下载到计算机的Temp目录，然后将其提取到Temp目录中的文件夹中。

之后，脚本将在“桌面”、“快速启动”和“开始菜单”等位置搜索每个目标浏览器的快捷方式的可能位置。它还配置浏览器安装文件的位置和扩展插件在计算机上的位置。

最后，PS脚本将依次搜索上述位置的任何链接（.LNK）文件，并修改所有现有浏览器快捷方式的“Target”参数，标记为“-load extension=[pathOfExtension]”，以便快捷方式加载安装了恶意扩展的浏览器。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154352156467.png "1691822506149218.png")

带有扩展参数的Chrome快捷方式

执行此操作后，脚本将关闭设备上可能运行的任何浏览器进程，以便受害者下次打开浏览器时，扩展程序将加载到浏览器中，并在用户浏览互联网时运行。

这种扩展安装技术允许攻击者在不知情的情况下将插件添加到受害者的浏览器中，而无需将其上传到官方扩展商店，如Chrome商店，该商店要求插件满足商店的要求。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154353163709.png "1691822529992112.png")

扩展安装PowerShell脚本

**恶意扩展分析**

安装扩展后，我们可以通过检查存储在扩展目录中的特定文件来分析其功能和特性。如果我们看一下'manifest.json'文件的第一行，我们会发现扩展插件通过将插件命名为“Google Drive”来伪装自己，所以即使用户访问浏览器插件，他们也只能看到一个名为“Google Drive”的插件，它看起来就像是安装在浏览器中的另一个标准Google扩展插件。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154353108824.png "1691822548212462.png")

manifest.json文件设置

当用户浏览时，另一个总是在后台运行的恶意扩展文件是“background.js”，它负责初始化与C2的通信。如果我们仔细查看JavaScript代码，我们会在脚本底部发现一个有趣的函数调用，其中包含一个字符串变量，该变量是比特币钱包的地址。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154354104877.png "1691823073324066.png")

Background.js脚本片段

查看脚本的代码，我们可以得出结论，扩展将从硬编码的URL中获取另一个字符串，脚本将比特币地址插入其中。JavaScript接收JSON格式的数据，显示钱包的交易活动，然后在最新的交易详细信息中查找特定的字符串。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154355942866.png "1691823084967209.png")

详细JSON

页面上有两个字符串，其中包含C2地址。“script”字符串是包含恶意软件C2主机的HEX字符串，“addr”字符串是Base58编码的C2地址。使用特定钱包的最后一笔加密货币交易来检索C2地址的原因是，攻击者可以随时更改服务器地址。此外，这种技巧使禁用恶意软件与其C2服务器的通信变得更加困难，因为禁用钱包比阻止或禁止IP或域要困难得多。如果C2服务器被阻止或关闭，攻击者可以通过执行新事务将“script”或“addr”字符串更改为不同的C2服务器。由于扩展总是检查这些字符串来检索C2，因此如果它发生了更改，它总是会请求新的字符串。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154355190909.png "1691823100317009.png")

从交易明细中解码C2地址

该扩展有几个其他脚本，它们负责初始化接收到的命令，并在检索到C2地址后发挥作用，因为这些脚本需要从C2获得一些重要信息。例如，C2保存比特币地址，当比特币从受害者的钱包转移到攻击者的钱包时将使用该地址。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154356146605.png "1691823395130879.png")

攻击者的比特币钱包地址

为了获得受害者的加密货币，攻击者在目标网站上使用web注入。web注入脚本也是C2在扩展与之联系后提供的。在下面的截屏中，我们可以看到来自扩展的“injections.js”脚本，它从C2服务器获取web注入脚本。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154356619881.png "1691823411169900.png")

injections.js脚本

在插件与C2服务器联系后，服务器会使用将在目标网站上使用的web注入脚本进行响应。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154358320811.png "1691823458186951.png")

C2服务器的Webinject脚本

如果我们仔细看一下脚本，就可以看到攻击者针对的是各种网站。在上面显示的脚本版本中，我们可以看到它针对的是Coinbase, Bybit, KuCoin, Huobi和Binance用户。

由于C2中的脚本可以随时更改，攻击者可以添加或删除其他web注入目标，也可以开始以比特币以外的加密货币为目标，这使得该扩展非常动态，并允许攻击者通过更改脚本来控制恶意扩展。

查看脚本，我们可以看到扩展在目标网站上执行各种操作。例如，它能够检索受害者的地址、获取账户信息、绕过2FA等等。此外，它能够将比特币从受害者的钱包转移到攻击者的钱包。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154359121210.png "1691823478235940.png")

web注入脚本中的函数

查看完整的web注入脚本，我们可以得出结论，其思路是从安装了恶意扩展的受害者那里窃取比特币。该扩展程序对账户执行各种操作，以便使用web注入脚本远程控制账户，最终该扩展程序试图将比特币提取到攻击者的钱包中。为了规避交易的双因素身份验证设置，web注入脚本使用了针对此保护技术的绕过技术。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230816/1692154359153526.png "1691823494228086.png")

从web注入脚本中提取比特币函数的代码段

在窃取加密货币之前，扩展程序与C2服务器进行通信，以获得最小比特币值。然后，它将这个值与目标钱包中的实际金额进行比较。如果钱包中包含的加密货币少于C2收到的最低金额，则不会从中提取任何加密货币。

![19.png](https://img...