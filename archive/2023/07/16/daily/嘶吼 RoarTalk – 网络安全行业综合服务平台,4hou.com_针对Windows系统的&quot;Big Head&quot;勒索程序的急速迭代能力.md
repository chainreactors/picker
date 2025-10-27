---
title: 针对Windows系统的&quot;Big Head&quot;勒索程序的急速迭代能力
url: https://www.4hou.com/posts/WKmE
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-16
fetch_date: 2025-10-04T11:51:51.412874
---

# 针对Windows系统的&quot;Big Head&quot;勒索程序的急速迭代能力

针对Windows系统的"Big Head"勒索程序的急速迭代能力 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 针对Windows系统的"Big Head"勒索程序的急速迭代能力

lucywang
[技术](https://www.4hou.com/category/technology)
2023-07-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)117936

收藏

导语：本文会详细介绍Big Head这个新勒索程序家族的技术细节。

趋势科技研究人员日前发现了有关针对Windows系统的"Big Head"勒索程序，目前该恶意勒索程序已衍生出至少三种变体，其中一种是通过网络钓鱼方法传播恶意网址，然后将"Big Head"勒索程序病毒扩散出去，并会伪装成Windows Update的接口、或是假装是Word安装资讯，诱骗下载，安装过程还有"进度条"让人以为是官方程序。

本文会详细介绍Big Head这个新勒索程序家族的技术细节。

关于Big Head的报道最早出现在5月，截止目前，该家族至少有三个变体被记录在案。经过仔细检查，我们发现这两个变体在其勒索信中共享了一个共同的联系电子邮件，这使我们怀疑这两种不同的变体来自同一个恶意程序开发人员。进一步研究这些变体，研究人员发现了该恶意程序的大量变体。接下来，我们将深入研究这些变体的例程，它们的异同，以及这些感染被滥用进行攻击时的潜在危害影响。

接下来，我们将详细介绍目前已发现的三个Big Head示例，以及它们各自的功能。分析发现，这三个Big Head勒索程序变体都是伪装成虚假Windows更新和Word安装程序传播的。

**变体1**

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134797419138.png "1689134797419138.png")

变体1的攻击流程

“Big Head”勒索程序变体1(SHA256: 6d27c1b457a34ce9edfb4060d9e04eb44d021a7b03223ee72ca569c8c4215438，被趋势科技检测为Ransom.MSIL.EGOGEN.THEBBBC)包含一个.NET编译的二进制文件。此二进制文件使用CreateMutex检查互斥锁名称8bikfjjD4JpkkAqrz，如果找到了互斥锁名称，则自我终止。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134813532393.png "1689134813532393.png")

调用CreateMutex函数

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134830135900.png "1689134830135900.png")

MTX值" 8bikfjjD4JpkkAqrz "

该示例还有一个配置列表，其中包含与安装过程相关的详细信息。它指定了各种操作，例如创建注册表项、检查文件是否存在并在必要时覆盖它、设置系统文件属性以及创建自动运行注册表项。这些配置设置由管道符号“|”分隔，并附有相应的字符串，这些字符串定义了与每个操作相关联的特定行为。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134845164285.png "1689134845164285.png")

配置列表

该恶意程序在安装时遵循的行为格式如下：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134860648287.png "1689134860648287.png")

此外，我们注意到存在三个资源，其中包含类似于扩展名为“\*.exe”的可执行文件的数据：

1.exe会释放其自身的副本以进行传播。这是一个勒索程序，在加密和附加“.pop”扩展名之前，它会检查扩展名“.r3d”。2.Archive.exe会释放了一个名为teleratserver.exe的文件，这是一个Telegram木马程序，负责与攻击者的聊天机器人ID建立通信。
3.Xarch.exe会释放了一个名为BXIuSsB.exe的文件，这是一个加密文件并将文件名编码为Base64的勒索程序。它还显示了一个虚假的Windows更新来欺骗受害者，使其认为恶意活动是一个合法的进程。

这些二进制文件是加密的，如果没有适当的解密机制，它们的内容将无法访问。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134876789936.png "1689134876789936.png")

在主示例中找到了三个资源

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134890978353.png "1689134890978353.png")

位于资源部分(“1.exe”)中的一个文件的加密内容

为了从资源中提取三个二进制文件，恶意程序采用了带有电子密码本(ECB)模式的AES解密。这个解密过程需要一个初始化向量(IV)来进行正确的解密。

值得注意的是，所使用的解密密钥是从互斥锁8bikfjjD4JpkkAqrz的MD5哈希中派生出来的。这个互斥锁是一个硬编码的字符串值，其中它的MD5哈希值用于解密三个二进制文件1.exe、archive.exe和Xarch.exe。需要注意的是，每个变体的MTX值和加密资源不同。

研究人员通过专门利用变体名称的MD5哈希来手动解密每个二进制文件中的内容。完成此步骤后，我们继续使用AES模式来解密加密的资源文件。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134905974740.png "1689134905974740.png")

用于解密三个二进制文件（顶部）和来自父文件的解密二进制文件（底部）的代码

下表显示了使用MTX值8bikfjjD4JpkkAqrz解密的恶意程序释放的二进制文件的详细信息。这三个二进制文件在代码结构和二进制文件提取方面与父变体有相似之处：

解密并提取的三个二进制文件

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134919658701.png "1689134919658701.png")

1.exe（左）、teleratserver.exe（中）和BXIuSsB.exe（右）

**二进制文件**

本节详细介绍了从上一个表中标识的已释放的二进制文件，以及父示例释放的第一个二进制文件1.exe。

![加图1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134947190662.png "1689134947190662.png")

最初，该文件将通过使用带有SW\_hide（0）的WinAPI ShowWindow来隐藏控制台窗口。该恶意程序将创建一个自动运行注册表项，使其能够在系统启动时自动执行。此外，它将制作自己的副本，并将其保存为本地计算机中

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134933203299.png "1689134933203299.png")

ShowWindow API代码隐藏当前进程的窗口(顶部)和注册表项的创建，并将其本身的副本作为“discord.exe”(底部)释放

Big Head勒索程序在%appdata%\ID中检查受害者的ID。如果ID存在，勒索程序会验证ID并读取内容。否则，它将创建一个随机生成的40个字符字符串，并将其写入文件%appdata%\ID，作为一种攻击标记，以识别其受害者。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134961147329.png "1689134961147329.png")

观察到的行为表明，扩展名为“.r3d”的文件是使用AES加密的特定目标，其密钥源自加密块链接（CBC）模式下的“123”的SHA256哈希。因此，加密的文件最终会附加“.popup”扩展名。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134977180208.png "1689134977180208.png")

恶意程序在加密和附加 ”.poop” 扩展名之前检查包含“.r3d” 的扩展名（顶部），以及当文件扩展名“.r3d” 存在时的文件加密过程（底部）

在这个文件中，我们还观察到勒索程序是如何删除其卷影副本的。用于删除卷影副本和备份的命令，也用于禁用恢复选项，如下所示：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689134995161671.png "1689134995161671.png")

它将赎金通知放在桌面、子目录和%appdata%文件夹上。Big Head勒索程序还更改了受害者机器的壁纸。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689135011221318.png "1689135011221318.png")

“1.exe”二进制文件的勒索信

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689135023481781.png "1689135023481781.png")

受害者计算机上的壁纸

最后，它将执行打开浏览器的命令，并访问恶意程序开发人员的Telegram帐户hxxps[:]//t[.]me/[REDACTED]\_69。分析显示，除了重定向之外，没有与该帐户交换任何特定的操作或通信。

![加图2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689135053866775.png "1689135053866775.png")

Teleratserver是一个64位python编译的二进制文件，它通过Telegram充当攻击者和受害者之间的通信通道。它接受命令“开始”、“帮助”、“屏幕截图”和“消息”。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689135039106985.png "1689135039106985.png")

从二进制文件反编译的Python脚本

![加图3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689135066973298.png "1689135066973298.png")

恶意程序显示了一个虚假的Windows Update UI，以欺骗受害者，使其认为恶意活动是合法的程序更新过程，其进度百分比以100秒为增量。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689135091125010.png "1689135091125010.png")

负责虚假更新的代码（左）和向用户显示的虚假更新（右）

如果用户的系统语言与俄罗斯、白俄罗斯、乌克兰、哈萨克、吉尔吉斯、亚美尼亚、格鲁吉亚、鞑靼和乌兹别克国家代码匹配，恶意程序就会自行终止。该恶意程序还禁用任务管理器，以防止用户终止或调查其进程。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689135106342890.png "1689135106342890.png")

负责禁用任务管理器的“KillCtrlAltDelete”命令

该恶意程序将其副本放入其创建的隐藏文件夹

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689135122159037.png "1689135122159037.png")

创建自动运行注册表

该恶意程序还会随机生成一个32个字符的密钥，稍后将用于加密文件。然后，该密钥将使用带有硬编码公钥的RSA-2048进行加密。

然后，勒索程序会释放包含加密密钥的勒索信。

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689135138100199.png "1689135138100199.png")

勒索信

恶意程序会避开包含以下子字符串的目录：

```
WINDOWS or WindowsRECYCLER or RecyclerProgram FilesProgram Files (x86)Recycle.Bin or RECYCLE.BINTEMP or TempAPPDATA or AppDataProgramDataMicrosoftBurn
```

通过将这些目录排除在其恶意活动之外，可以降低被检测到的可能性，并增加了在更长时间内持续运行的机会。以下是Big Head勒索程序加密的扩展名:

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689135156923676.png "1689135156923676.png")

该恶意程序还会终止以下进程：

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230712/1689135192264454.png "1689135192264454.png")

恶意程序使用Base64重命名加密文件。 我们观察到恶意程序使用LockFile功能，该功能通过重命名文件并添加标记来加密文件。此标记用作确定文件是否已加密的标识。通过进一步检查，研究人员看到了在加密文件中检查标记的功能。解密后，可以在加密文件的末尾匹配标记。

![23.png](https://img.4hou.com/uploads...