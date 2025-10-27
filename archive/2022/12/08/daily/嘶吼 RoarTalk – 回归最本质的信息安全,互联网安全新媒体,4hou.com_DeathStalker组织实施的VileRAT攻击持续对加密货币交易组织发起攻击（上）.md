---
title: DeathStalker组织实施的VileRAT攻击持续对加密货币交易组织发起攻击（上）
url: https://www.4hou.com/posts/O9LL
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-08
fetch_date: 2025-10-04T00:51:14.608715
---

# DeathStalker组织实施的VileRAT攻击持续对加密货币交易组织发起攻击（上）

DeathStalker组织实施的VileRAT攻击持续对加密货币交易组织发起攻击（上） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# DeathStalker组织实施的VileRAT攻击持续对加密货币交易组织发起攻击（上）

gejigeji
[技术](https://www.4hou.com/category/technology)
2022-12-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)136131

收藏

导语：自2022年3月以来，研究人员已经识别出更多与VileRAT相关的恶意文件和新基础设施的示例，这可能是攻击尝试增加的征兆。

![vilerat_featured-1200x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208574132702.jpeg "1660208574132702.jpeg")

早在2020年8月下旬，就有研究人员发布了DeathStalker的活动报告，包括Janicab、Evilnum和PowerSing活动。同时，在2020年8月，研究人员还首次发布了一份关于VileRAT的私人报告。VileRAT是一种Python植入程序，是专门针对外汇和加密货币交易公司一种高度复杂的攻击活动，其幕后攻击者就是DeathStalker。

自2020年6月首次被发现以来，DeathStalker确实不断利用和更新其VileRAT工具链来对付相同类型的目标。而且DeathStalker最近可能会加大力度使用此工具链来破坏目标。自2022年3月以来，研究人员已经识别出更多与VileRAT相关的恶意文件和新基础设施的示例，这可能是攻击尝试增加的征兆。

**VileRAT的初始攻击和工具集介绍**

早在2020年夏天，DeathStalker的VileRAT的攻击就包括发送给外汇公司的鱼叉式网络钓鱼电子邮件。如果目标上钩，假冒的角色会在某个时候根据请求提供指向托管在GoogleDrive上的恶意文件的链接（伪装成PDF或ZIP存档的Windows快捷方式文件），作为身份证明文件，然后，恶意链接将触发任意系统命令的执行，以释放无害的诱饵文档，以及我们称为VileLoader的恶意且非常复杂的二进制加载程序。

至少从2021年末开始，攻击技术略有变化，但最初的攻击媒介仍然是恶意消息：通过电子邮件向目标发送Word文档。2022年7月，攻击者利用嵌入在目标公司公共网站中的聊天木马向目标发送恶意DOCX。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208581127648.png "1660208581127648.png")

恶意DOCX的钓鱼消息

DOCX文档经常使用“合规性”或“投诉”关键字来命名，这表明攻击者正在回答识别请求或表达某个问题作为发送它们的理由。

至少从2021年底开始，最初的攻击和工具集部署如下图所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208597817168.png "1660208597817168.png")

VileRAT攻击和工具集概述

**秘密执行VileDropper**

最初的DOCX攻击文档本身是无害的，但它包含指向另一个恶意和启用宏的DOTM文档的链接作为“远程模板”。打开DOCX时，Word会自动下载这些DOTM文件，如果收件人启用了执行，则会触发其嵌入的宏。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208605731509.png "1660208605731509.png")

DOCX中包含的恶意远程模板

恶意DOTM远程模板利用VBAstomping技术来隐藏嵌入式宏的代码。VBAstomping使可编辑的VBA源代码（即宏的可见代码）不同与实际执行的代码。这是可能的，因为可编辑源代码和被称为p-code的经过转换的内部版本都嵌入在启用宏的文档中。由于使用了VBAstomping，将要执行的真正宏代码对标准工具（MicrosoftWord的宏编辑工具以及OLETools）是隐藏的。

这种技术有一个严重的限制：隐藏的宏（即内部p代码）只有在启用宏的文档使用生成它的相同Office版本打开时才能执行。否则，隐藏的宏将无法运行，而将执行可见的宏。在最后一种情况下，DeathStalker确保它会向用户弹出一条消息。但最重要的是，DeathStalker确保将多个攻击文档变体传播给目标，每个变体都针对特定的Office版本进行准备。

![4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208614463966.jpeg "1660208614463966.jpeg")

恶意DOTM远程模板中的VBAstomping失败

在任何情况下，可见和隐藏的宏都会下载一张图片来取代感染文档中的社会工程消息，并欺骗读者相信某些事情失败了。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208623162108.png "1660208623162108.png")

执行宏时下载的图像示例

然而，在后台，如果VBAstomping有效，嵌入DOTM的宏会使用WMI静默收集有关安装在目标计算机上的安全产品的信息，将它们发送到命令和控制(C2)服务器，解码并释放文件，然后最终执行我们称为VileDropper的恶意混淆JavaScript(JS)后门。

嵌入DOTM的宏本身已经揭示了一些有趣且具体的技术。它被轻微混淆，因为大多数文本字符串都是XOR编码的，其密码源自一个句子，例如，“OperatesCatholicsmalltownspueblosTwoof”。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208632853075.png "1660208632853075.png")

DOTM嵌入宏中的XOR解码函数

XOR解码算法看起来非常接近过去在PowerPepper工具链的VBS加载程序脚本中使用的算法，而且看起来合法的函数名也让人想起PowerPepper宏中使用的函数名，例如"insert\_table\_of\_figures"，"change\_highlight\_color"等。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208640129029.png "1660208640129029.png")

PowerPepperVBS加载程序中的XOR解码函数(MD5DB6D1F6AB887383782E4E3D6E4AACDD0)

嵌入DOTM的宏从编码数据中解码并删除两个文件（在“%APPDATA%”文件夹中：“Redist.txt”和“ThirdPartyNotice.txt”，或“pattern.txt”和“changelog.txt”）存储在不可见的TextBox表单中。利用Office对象属性作为隐藏数据源也是之前采用的技术。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208649196142.png "1660208649196142.png")

用作恶意DOTM文档中数据存储的TextBox表单，如Microsoft的VBA编辑器所示

另一个值得注意的特性是，嵌入DOTM的宏通过向固定的C2URL发送HTTPGET请求来指示执行过程中的进展或错误。有趣的是，VBA宏中的所有HTTP请求都是使用远程图片插入函数触发的。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208658110677.png "1660208658110677.png")

嵌入DOTM的宏利用“AddPicture”作为Web客户端

在任何情况下，嵌入DOTM的宏最终都会触发VileDropper的执行，使用“WScript”解释器的重命名副本（“%APPDATA%”文件夹中的“msdcat.exe”或“msgmft.exe”），使用如下命令作为：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208669739752.png "1660208669739752.png")

“changelog.txt”是VileDropper，“91”是VileDropper用来解码异或数据的密码的一部分，“pattern.txt”是一个包含VileLoader的编码包。

**VileDropper：一个过度混淆的任务调度器**

在DeathStalker错综复杂的VileRAT攻击链中还有一个VileDropper。它是一个混淆的JavaScript文件，主要释放和调度下一阶段的执行：VileLoader。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208678124835.png "1660208678124835.png")

VileDropper代码的原始形式

第一次运行VileDropper至少需要两个参数，第三个参数可以用作触发特定环境执行变化的标志，具体取决于安装在目标计算机上的安全产品：

第一个是部分密码（用于解码XOR编码的数据），第二个是一个编码的有效负载文件的路径(包含VileLoader及其配套的shellcode)。

VileDropper还会检查它的解释器和文件名，如果它没有按计划调用，则立即停止执行，这可能是为了规避沙箱检测：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208687502976.png "1660208687502976.png")

VileDropper中的反混淆执行检查

VileDropper的确切执行流程取决于目标计算机上安装的安全产品，但大多数时候，它将自己复制到另一个文件，重新启动自己，并删除其原始副本。在执行VileDropper期间：

1.收集有关目标环境的附加数据（使用WMI）以及生成目标标识符并将它们发送到C2服务器；

2.解码并释放VileLoader及其编码的结果shellcode。文件名和位置会因示例而异，但他们被放在一个看似合法的公共文件夹“%APPDATA%”(例如，“exe”和“dev0Y11ZF.tmp”在“%APPDATA%\Microsoft\PrinterSettings\Printers\”)下。

3.安排一个任务在35到65秒后运行VileLoader，之后每3小时45分钟运行一次。

使用预设的User-Agent(C2的URL和User-Agent的变化取决于VileDropper的示例)，VileDropper使用一个HTTPGET请求将数据发送到C2服务器到一个固定的URL(例如，“hxxp://hubflash[.]co/admin/auth.php”)。有用的信息被存储为一个JSON项，然后该文档被xor编码、base64编码、url编码，并被设置为HTTP请求中的cookie值：

JSON 项和内容（JSON 值）如下：

1.u，目标标识符：标识符是目标登录（%USERNAME% 环境变量）和计算机 UUID（在 WMI 查询的第一个结果中获得的类似 UUID 的自定义表示形式：SELECT UUID FROM Win32\_ComputerSystemProduct）。然后这个类似 UUID 的值是 base64 编码和 URL 编码的。由于标识符生成逻辑的固定长度和填充，标识符的最终形式总是 48 个字符长。

2.d，一个硬编码的 VileDropper 标识符，它可能指定一个活动或版本（例如，“9745B355”）。

3.a，安装在目标计算机上的安全产品（WMI 中的 AntiVirusProduct）名称列表，以竖线符号 (|) 分隔，然后是 XORed、base64 编码和 URL 编码。

4.n，目标的完全限定登录，作为“%USERDOMAIN%\%USERNAME%”的shell扩展，然后进行异或、base64 编码和 URL 编码。

5.w ,目标的操作系统版本，从 WMI 查询 SELECT Version FROM Win32\_OperatingSystem 返回，然后是 base64 编码和 URL 编码。

由VileDropper调度的任务(其名称因样例而异，如“CDS同步”或“UpdateModel任务”)会触发以下类型的执行命令：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208697138578.png "1660208697138578.png")

命令行中方括号之间的字符（例如[u]）指定相应JSON项的内容，即[u]是编码的目标标识符。

在继续讨论VileLoader之前，请注意VileDropper使用XOR编码方案来保护发送到C2服务器的数据，因为类似的方案将在以后使用。该算法生成的数据块布局如下，有时还会进一步进行base64编码和URL编码：

类型一：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208707989523.png "1660208707989523.png")

生成的blob是自给自足的，并且可以由接收者解码，而无需访问预共享密钥。在VileDropper中，作为JavaScript混淆的一部分编码的字符串受益于额外的异或：嵌入数据blob中的异或密钥还使用特定于脚本的固定密码进行了异或，此固定密码的一部分被传递给VileDropper在攻击链中的前一个DOTM宏执行的命令行上，另一部分在VileDropper中硬编码。

后来，VileLoader和VileRAT使用该算法的其他变体。

类型二：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208715318765.png "1660208715318765.png")

类型三：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220811/1660208724191680.png "1660208724191680.png")

类型四...