---
title: Dark Pink APT组织针对东南亚以及欧洲地区的攻击活动（二）
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247559326&idx=3&sn=f55cf5c819be66ce8e541cf074559aae&chksm=e91438a4de63b1b20c869a4e56ae438b1f75e3061a78c6a1598f703208975aa822ee7e52f09a&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-03-29
fetch_date: 2025-10-04T11:02:21.051198
---

# Dark Pink APT组织针对东南亚以及欧洲地区的攻击活动（二）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvdK1CGAZoiahV3qz5dlrvzIwgTRJ3Q8of1s53nOX8ICPQ9gI1eYLZ3Nw/0?wx_fmt=jpeg)

# Dark Pink APT组织针对东南亚以及欧洲地区的攻击活动（二）

luochicun

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv4px86ibRib0FBibRb9NBNAicglLBQH78SOqMmlg1emfQia1NzKMyewZoQOQ/640?wx_fmt=png)侦察和横向移动

只要受害者组织网络中的一台设备被攻击，Dark Pink的下一个目标是收集尽可能多的关于受害者网络基础设施的信息。研究人员发现攻击者对以下内容感兴趣：

来自标准实用程序的信息，例如标准实用程序systeminfo的输出；

来自网络浏览器的信息；

安装软件，包括防病毒解决方案；

有关连接的USB设备和网络共享的信息；

攻击者还收集了可用于写入的网络和USB驱动器列表，然后将这些驱动器用于横向移动。接下来，攻击会看到用启动TelePowerDropper的命令创建一个LNK文件(Windows快捷方式)，而不是原始文件。在这个阶段，受害者是看不见原始文件的。

攻击者如何在USB设备上进行横向移动？首先攻击者注册一个新的WMI事件处理程序。从现在开始，每次将USB设备插入受感染的设备时，都会执行一个特定的操作，看到TeleBotDropper下载并存储在USB设备。让我们更深入地分析一下这个过程。

1.受害者将USB设备插入受攻击设备；

2.WMI事件被触发，并导致从攻击者的Github帐户自动下载. zip压缩文件。这个压缩文件中有三个文件：Dism.exe, Dism.sys和Dismcore.dll。第一个文件是具有有效数字签名的合法文件。DLL文件的功能是从文件Dism.sys中解压缩原始可执行文件。

3.压缩文件被解压缩到%tmp%文件夹，然后将这些文件复制到USB设备，并在其中创建一个名为“dism”的新文件夹。文件夹属性更改为隐藏和系统；

4.创建一个名为system.bat的文件，其中包含启动Dism.exe的命令；

5.最后，创建的LNK文件数量与USB驱动器上的文件夹数量相同。原始文件夹的属性将更改为隐藏和系统。使用命令创建LNK文件，打开explorer.exe中的隐藏文件夹并启动system.bat。

之后，用户将看到与USB设备上找到的文件夹同名的LNK文件。一旦用户打开此恶意LNK文件，TeleBotDropper将通过DLL侧加载技术启动（TeleBotDroper的功能已在上一节中显示）。结果，读取注册表项、解密和启动TelePowerBot的命令被传输到新设备。必须记住，如果USB设备上只有一个文件夹，则此解决方案有效。这就是为什么我们观察到不同的实现，例如，在USB设备上创建LNK文件而不是.pdf文件（不仅仅是文件夹）。附录B中提供了更详细的工作原理示例，在原始文件的位置创建LNK文件的机制也用于网络共享。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv4px86ibRib0FBibRb9NBNAicglLBQH78SOqMmlg1emfQia1NzKMyewZoQOQ/640?wx_fmt=png)数据泄露

与许多其他类似攻击一样，攻击者通过ZIP压缩文件泄露数据。在Dark Pink攻击期间，所有要发送给攻击者的数据(来自公共网络共享的文件列表、web浏览器数据、文档等)都堆叠在$env:tmp\backuplog文件夹中。但是，收集和发送过程彼此独立运行。当受攻击的设备发出下载$env:tmp\backuplog文件夹的命令时，文件列表将被复制到$env:tmp\backuplog文件夹中，添加到压缩文件并发送到攻击者的Telegram木马。在此步骤完成后，$env:tmp\ backuplo1目录将被删除。

攻击者还可以利用他们自定义的窃取程序Cucky和Ctealer从受攻击的设备中提取数据。这两个窃取程序的功能是一样的。它们可以用来从网络浏览器中提取密码、历史记录、登录名和cookie等数据。窃取程序本身不需要任何互联网连接，因为他们将执行结果(被盗数据)保存到文件中。通过恶意软件发出的命令，可以从攻击者的Github帐户自动下载这两种窃取程序。用于启动Cucky的脚本示例见附录C。

总的来说，Group-IB研究人员发现，Dark Pink通过三个不同的途径泄露文件。第一种途径是攻击者使用Telegram接收文件。当设备被攻击时，恶意软件会收集特定文件夹中的信息，并通过一个特殊命令通过Telegram发送。通过扩展，发送给攻击者的文件是:.doc， .docx, xls，.xlsx，.ppt，.pptx，.pdf，执行此过程的脚本示例可以在附录D中找到。

除了Telegram, Group-IB还发现了攻击者通过Dropbox窃取文件的证据。这种方法与通过Telegram进行窃取的方法略有不同，因为它涉及一系列PowerShell脚本，通过使用硬编码令牌执行HTTP请求，将文件从特定文件夹传输到Dropbox帐户。

Group-IB还发现了一次特别的攻击，尽管该设备是由攻击者控制的Telegram方式通过Telegram木马发出的命令控制的，但一些有趣的文件是通过电子邮件发送的。该命令的示例如下所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEve9IE2gVyHr447MsSGJ3ubUQvjWvUp5AEB7RQcSxeGuJSLK9mzsyuSg/640?wx_fmt=png)

数据泄露过程中使用的邮件列表如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvlZNjs2jZZiaAqxdv0vQbSRnIZ2zV7JrmzK86y5UnvOMsyhvd8xcdQSg/640?wx_fmt=png)

在这一阶段，Group-IB研究人员认为，选择的泄露方法取决于受害者网络基础设施中设置的潜在限制。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv4px86ibRib0FBibRb9NBNAicglLBQH78SOqMmlg1emfQia1NzKMyewZoQOQ/640?wx_fmt=png)逃避技术

在他们的攻击过程中，攻击者使用了一种已知的技术来绕过用户帐户控制(UAC)来更改Windows Defender中的设置。他们通过提升COM接口来做到这一点。所使用的方法并不是唯一的，在不同的编程语言中发现了不同的实现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv92VJFqfsEqJNaYaLtSGiby4auShLX22K4GnuKOKDGGxgx7057qmXkpQ/640?wx_fmt=png)

允许绕过UAC的反编译可执行文件截图

设置由一个特殊的PowerShell脚本更改，该脚本作为命令接收，并在.NET应用程序中实现。该命令以可执行文件(在base64视图中)的形式出现，在攻击时自动从Github下载。可执行文件不会获得持久性，也不会保存在受攻击的系统上。可执行文件不会持久存在，也不会保存到受攻击的系统中。下载和启动的示例如下所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvYh5x6vFdXiaxiaE62X8qnkgMA0Pd9DqIUgPhO3wjE3jSFrEH0jib4ZNAQ/640?wx_fmt=png)

修改Windows Defender设置的PowerShell命令作为参数传递，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvrDbtJnhicYggZgjPfN4icSwUoG8FSdyiaeOwoxT2n6lmmpamsrTVRTic4g/640?wx_fmt=png)

PowerShell命令将使用.NET应用程序作为权限升级工具来执行

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv4px86ibRib0FBibRb9NBNAicglLBQH78SOqMmlg1emfQia1NzKMyewZoQOQ/640?wx_fmt=png)工具

**Cucky**

Cucky是在.NET上开发的一个简单的自定义窃取程序。在调查过程中发现了各种各样的样本。分析最多的版本是由Confuser打包的。它不与网络通信，收集的信息保存在文件夹%TEMP%\backuplog中。Cucky能够从目标网络浏览器中提取密码、历史记录、登录名和cookie等数据。虽然我们没有任何与使用被盗数据相关的信息，但我们认为它可以用于访问电子邮件web客户端，根据web历史进行额外的基础设施侦察，编制组织员工列表，传播恶意附件，并评估目标设备是真实的还是虚拟的。

Cucky具有从以下浏览器窃取数据的功能：

Chrome, MS Edge, CocCoc, Chromium, Brave, Atom, Uran, Sputnik, Slimjet, Epic Privacy, Amigo, Vivaldy, komita, Comodo, Nichrome, Maxthon, Comodo Dragon, Avast浏览器，Yandex浏览器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEviboQI3sC0U0Fscux4wjmjGdyTBPs2nIfjxG6521lDTZrLPVfQg7qJ9Q/640?wx_fmt=png)

反编译的Cucky 窃取程序的截图

找到的示例包含以下调试信息的路径：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvYAvOIFWDaYE3mw7xKz7GcbibIiaUZUSLAnzrIVX1tQxuMQNwFTD4LLwA/640?wx_fmt=png)

**Ctealer**

Ctealer是Cucky的模拟版本，但是在C/ c++上开发的。TelePowerDropper或攻击者发出的特殊命令可用于部署Ctealer。工作过程也非常类似于Cucky，因为它还将收集的文件保存到%TEMP%\backuplog文件夹。Ctealer可以从以下web浏览器获取信息：

Chrome, Chromium, MS Edge, Brave, Epic Privacy, Amigo, Vivaldi, Orbitum, Atom, komita, Dragon, Torch, Comodo, Slimjet, 360浏览器，Maxthon, K-Melon, Sputnik, nicchrorome, CocCoc, Uran, Chromodo, Yandex浏览器。

找到的示例包含以下调试信息的路径：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvzvswKibFbztkbIl9HYj39C1ibMX4FVVpq50QjutIY4pFcAnSx6XSCIcw/640?wx_fmt=png)

**TelePowerBot**

正如我们已经注意到的，每次受攻击设备的用户登录系统时，TelePowerBot都会被启动。当这种情况发生时，将启动一个特殊的脚本。脚本读取另一个regkey的值(例如HKCU\SOFTWARE\Classes\abcdfile\shell\abcd)，开始解密并启动TelePowerBot。加密基于xor，其中密钥是0到256之间的数组号。在解密之前，原始有效负载将从base64解码。去模糊化的命令示例如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvZmJEnyPsiafiaWiaSFiaqQEfW8L5wqiaUTnh3uWqdeCC7qd3qibcf9Dr9YlQ/640?wx_fmt=png)

解密阶段不是最终阶段，这是一个中间阶段，也是基于PowerShell的，并且是高度模糊的。在这个阶段，最终脚本已经存储在阶段中，但是它被分割成块。由此，创建一个base64字符串，解码后，我们将得到一个ZIP流。最后，TelePowerBot在解压缩后启动。

该工具可以与Telegram通道通信，以接收来自攻击者的新任务。木马可以与各种受攻击的设备通信，木马每60秒检查一次新命令。在执行过程中，木马使用两个注册表项：HKCU\Environment\Update和HKCU\Environment\guid。第一个存储最后一个消息id，该消息id由Telegram 木马处理(来自Telegram的参数update\_id)。第二个密钥存储受攻击设备的唯一标识。它是在木马第一次启动时由命令[guid]::NewGuid()生成的。注册后，攻击者就会获得有关受攻击设备的各种信息，如ip、guid、设备名称。IP地址也通过获取请求来确定https://ifconfig.me/ip，这些进程也是基于PowerShell命令的，我们将在后面的报告中更深入地讨论这些命令。木马的实施如附录A所示。

该模块的一些变体包含用于确保横向移动的附加功能。所有其他功能都是一样的。在Group-IB进行分析的情况下，Telegram参数可以硬编码在脚本中，也可以从注册表项中读取。

**KamiKakaBot**

KamiKakaBot是TelePowerBot的. net版本，我们发现它们之间几乎没有区别。在读取命令之前，KamiKakaBot能够从Chrome, MS Edge和Firefox浏览器中窃取。它能够更新自己，一旦它接收到命令，它可以将参数传递给cmd.exe进程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEv3ERpzghYFJhk09KCHvv7623vMrBNRib44xpW2jA6JRdDBV9ticZrJHkg/640?wx_fmt=png)

详细说明包含KamiKakaBot的反编译可执行文件的屏幕截图

**PowerSploit / Get-MicrophoneAudio**

如上所述，Dark Pink背后的攻击者几乎只利用定制工具。然而，为了记录来自受感染设备的麦克风音频，他们转向了公开可用的PowerSploit模块- Get-MicrophoneAudio。这是通过从Github下载加载到受害者的设备上的。Group-IB研究人员发现，当攻击者试图启动该模块时，受害者设备上的防病毒软件会阻止这一进程。我们发现攻击者试图混淆原始的PowerSploit模块，使其无法被检测到，但这些都没有成功。结果，攻击者返回绘图板并添加了一个脚本(如下所示)，该脚本能够成功地在受攻击的设备上录制麦克风音频。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28jfMmkA4ibNgmpjZpuAqdEvckesfO3EuLQhicPWdSVYKysPaJZYvk3nMQJWGOQsibY2wDFhXGI4maCg/640?wx_fmt=png)

这个简单的脚本启动了一个后台任务，它会触发一个标准实用程序PSR，以每分钟捕获一次声音。录制的音频文件将保存在位于临时文件夹(%TEMP%\record)的ZIP压缩文件中。文件的命名模板如下:“yyyyMMddHHmmss”。然后，这些音频文件被一个单独的脚本泄露，该脚本将它们(作为ZIP压缩文件)发送给攻击者的Telegram木马。

**ZMsg(即时通讯工具信息泄露)**

攻击者还对从受攻击设备上的即时通讯工具中窃取数据感兴趣。为此，它们能够执行命令来识别主要的即时通讯工具，如Viber、Telegram和Zalo。在Viber的示例中，这些命令允许攻击者窃取受攻击设备上的%APPDATA%\Viberpc文件夹，从而允许他们访问受害者的消息和联系人列表。我们仍在努力评估攻击者能够从受攻击设备上的Telegram账户中获取什么信息，但Zalo的示例却非常独特。

如果受害者的设备上存在Zalo即时通讯工具，攻击者可以启动命令从Github下载一个特殊的实用程序(Group-IB称为ZMsg)。这个实用程序是一个基于FlaUI库的.NET应用程序，它允许组织在Zalo平台上窃取受害者的消息。FlaUI是一个帮助Windows应用程序自动UI测试的库，入口点通常是应用程序或桌面，以生成自动化元素。通过这种方式，可以分析子元素并与其交互。

ZMsg迭代Windows应用程序中的元素，以发现具有特定名称的元素。例如，带有消息的元素的名称为“messageView”。所有收集的信息存储在%TEMP%\KoVosRLvmU\文件夹中，文件扩展名为.dat和.bin。文件名创建为编码的十六进制字符串，并根据以下模板生成：

%PERSON\_NAME%\_%DAY%\_%MONTH%\_%YEAR%

**命令**

攻击者通过指定ip、设备名或botid向受攻击的设备发出命令，还可以同时向所有受感染的设备发出任务。在检查过程中，我们注意到几种不同的命令。其中一些命令的功能是重叠...