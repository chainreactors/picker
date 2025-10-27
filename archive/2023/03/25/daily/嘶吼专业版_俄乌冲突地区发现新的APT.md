---
title: 俄乌冲突地区发现新的APT
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247559087&idx=3&sn=2a8871af5694e9124a8f15c9648afb53&chksm=e9143795de63be8340560c69c358fff01bb400dc417ddfda67bc76a50463c488092f2cbd8c99&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-03-25
fetch_date: 2025-10-04T10:38:21.472110
---

# 俄乌冲突地区发现新的APT

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMSpYaIkywIRQ7rehaTvR8JriaeIDxmO4FibpkGKJA2oXlRw82gYt0hNyQ/0?wx_fmt=jpeg)

# 俄乌冲突地区发现新的APT

luochicun

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMicO6DxkjEIudnryjxWUhXxvG04rzLzMdbm5XYpKqC5wwApDO4INcMNA/640?wx_fmt=jpeg)

自俄乌冲突开始以来，网络攻击就被大量用于其中。我们之前发布了一份与俄罗斯和乌克兰冲突有关的网络活动和威胁形势的介绍，并继续监测这些地区的新威胁。

2022年10月，研究人员发现顿涅茨克、卢甘斯克和克里米亚地区的政府、农业和运输组织出现了大量网络攻击。尽管最初攻击途径尚不清楚，但下一阶段的细节意味着要使用鱼叉式网络钓鱼或类似方法。受害者导航到指向恶意网络服务器上托管的ZIP存档的URL，该存档包含两个文件：

1.诱饵文件（研究人员发现了PDF、XLSX和DOCX版本）；

2.具有双重扩展名（例如.pdf.LNK）的恶意LNK文件，打开后会导致感染；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMHj1Xy6SkWM0wQaEgagVt0YE5E4mPoytkic9RcqVlP2jNywibs4MBYOCw/640?wx_fmt=png)

恶意ZIP存档

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMONr70v49QrP1GAS14m47CuaaTjicCgMSYWkGEZ4JannOSImqLvLtdqg/640?wx_fmt=png)

虚假文字文件

在一些情况下，诱饵文件的内容与恶意LNK的名称直接相关，以诱使用户激活它。例如，一个档案包含一个名为 “Приказ Минфина ДНР № 176.pdf.lnk” 的LNK文件，诱饵文件在文本中明确提到了它的名字。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMl8y2T7psGxFbO9lichAluicfQWePIAKTwziaGjRcDLgQsLcwDibxiaWDKww/640?wx_fmt=png)

带有恶意快捷方式文件的诱饵PDF(主题：关于朝鲜民主主义人民共和国财政部第176号法令的信息)

ZIP文件是从托管在webservice-srv[.]online和webservice-srv1[.]online两个域上的不同位置下载的。

已知附件名称，编辑后删除个人信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMktiazx0Jz29qfG5sEYKicMREINsAULE4FVvSlicWmXaphVliaV37wOLFpQ/640?wx_fmt=png)

当潜在受害者激活ZIP文件中包含的LNK文件时，它会触发一系列事件，导致计算机感染之前未见的恶意框架，我们将其命名为CommonMagic。该活动中使用的恶意软件和技术并不特别复杂，但很有效，并且代码与任何已知的攻击没有直接关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeM7I3Hia87iatMobKvH4LXHA3xtuMRoTnwV75xOsfl5kLJ5hsqxOHGDuiag/640?wx_fmt=png)

感染链

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMSoFCUZDMfKT8MFqQBUeuICXicibjWicqpkdN1vAoRHfUC2kHg4JPgChcg/640?wx_fmt=png)

安装工作流

恶意LNK指向一个远程托管的恶意MSI文件，该文件由Windows安装程序可执行文件下载并启动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMRMAWZrVIN0KUDIwpQ3GBlZI0iaeb1Qz4bwRKqLsF6aJriaxJZwZHR17w/640?wx_fmt=png)

MSI文件实际上是一个滴管程序包，包含一个加密的下一阶段有效负载（service\_pack.dat）、一个滴管脚本（runservice\_pack.vbs）和一个应该显示给受害者的诱饵文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMDEQEWUib654ZnawhkjQYo67WVzoAMZicyQ1GiajAOxJQ4IsDOMXPbU0kA/640?wx_fmt=png)

附件.msi中包含的文件

加密的有效负载和诱饵文件被写入名为%APPDATA%\WinEventCom的文件夹。反过来，VBS滴管脚本是一个启动嵌入式PowerShell脚本的包装器，该脚本使用简单的单字节XOR解密下一阶段，启动它并将其从磁盘中删除。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMDFgT7CDbqibKc2icPNMJK4vAkia8iaPPhkDUsvCiceWo1I6gdQFbDj7bSTg/640?wx_fmt=png)service\_pack.dat文件的解密

Расшифровка файла service\_pack.dat

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeM1q4RZe1HCyYwr7S8FNxStVSeP5f4O0yWEqGXdSu5wCtbsMibOL9KlFQ/640?wx_fmt=png)

下一阶段脚本完成安装，它打开诱饵文件并将其显示给用户，将两个名为config和manutil.vbs的文件写入%APPDATA%\WinEventCom，并创建一个名为WindowsActiveXTaskTrigger的任务调度程序作业，以每天执行wscript.exe%APPDATA%\WinEventCom\manutil.vbs命令。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMDFgT7CDbqibKc2icPNMJK4vAkia8iaPPhkDUsvCiceWo1I6gdQFbDj7bSTg/640?wx_fmt=png)PowerMagic后门

初始包释放的脚本manutil.vbs是一个加载程序，用于在PowerShell中编写的以前未知的后门，我们将其命名为PowerMagic。后门的主体从文件%APPDATA%\WinEventCom\config中读取，并使用简单的XOR（密钥：0x10）进行解密。

包含“PowerMagic”字符串的PowerMagic代码片段：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMa4KtgGuarlP7licGleB3iabE6Vbfx0tCsQ45XhFZ15LwR5IU4ubH3hmw/640?wx_fmt=png)

启动后，后门会创建一个互斥对象——WinEventCom。然后，它进入一个无限循环，与C&C服务器通信，接收命令并上传结果作为响应。它使用OneDrive和Dropbox文件夹作为传输，使用OAuth刷新令牌作为凭据。

后门每分钟都在执行以下操作：

修改位于/$AppDir/$ClientDir/

下载以文件形式存储在/$AppDir/$ClientTaskDir目录中的命令；

将每个命令作为PowerShell脚本执行；

将执行PowerShell命令的输出上载到云存储，并将其放置在/$AppDir/$ClientResultDir/

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMDFgT7CDbqibKc2icPNMJK4vAkia8iaPPhkDUsvCiceWo1I6gdQFbDj7bSTg/640?wx_fmt=png)CommonMagic框架

事实证明，PowerMagic并不是攻击者使用的唯一恶意工具包。PowerMagic的所有受害者都感染了一个更复杂、以前从未见过的模块化恶意框架，我们将其命名为CommonMagic。这个框架是在最初感染PowerShell后门后部署的，这让人们相信CommonMagic是通过PowerMagic部署的。

CommonMagic框架由几个可执行模块组成，所有模块都存储在目录C:\ProgramData\CommonCommand中。模块从独立的可执行文件开始，并通过命名管道进行通信。有专用模块用于与C&C服务器交互、加密和解密C&C流量以及各种恶意行为。

该框架的体系结构如下图所示。CommonMagic框架由几个可执行模块组成，所有模块都存储在目录C:\ProgramData\CommonCommand中。模块从独立的可执行文件开始，并通过命名管道进行通信。有专用模块用于与C&C服务器交互、加密和解密C&C流量以及各种恶意行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMe12OxpMowjHkIPBwM0icfe2d0lAAXgTibh49k7LnfVzrOcWjok4BSjpA/640?wx_fmt=png)

该框架的体系结构

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMDFgT7CDbqibKc2icPNMJK4vAkia8iaPPhkDUsvCiceWo1I6gdQFbDj7bSTg/640?wx_fmt=png)网络通信

该框架使用OneDrive远程文件夹进行传输。它利用Microsoft Graph API，使用嵌入到模块二进制文件中的OAuth刷新令牌进行身份验证。RapidJSON库用于解析Graph API返回的JSON对象。

一个专用的heartbeat线程会每隔五分钟用受害者的本地时间戳更新一次远程文件

然后，在单独的线程中，网络通信模块从目录

通过OneDrive位置与运营商交换的数据使用RC5Simple开源库进行加密。默认情况下，此库在加密序列的开头使用七字节序列“RC5SIMP”，但后门的开发人员将其更改为“Hwo7X8p”。加密是在一个单独的进程中实现的，通过名为\\.\pipe\PipeMd 和\\.\pipe\PipeCrDtMd管道进行通信。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMDFgT7CDbqibKc2icPNMJK4vAkia8iaPPhkDUsvCiceWo1I6gdQFbDj7bSTg/640?wx_fmt=png)插件

到目前为止，我们已经发现了两个实现恶意业务逻辑的插件。它们位于目录C:\ProgramData\CommonCommand\Other中。

Screenshot (S.exe)——使用GDI API每三秒进行一次屏幕截图；

USB (U.exe) ——从连接的USB设备收集具有以下扩展名文件的内容：.doc、.docx..xls、.xlsx、.rtf、.odt、.ods、.zip、.rar、.txt、.pdf。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMDFgT7CDbqibKc2icPNMJK4vAkia8iaPPhkDUsvCiceWo1I6gdQFbDj7bSTg/640?wx_fmt=png)总结

到目前为止，卡巴斯基实验室的研究人员还没有发现这场活动中使用的样本和数据与任何以前已知的攻击者之间有什么联系。我们也将持续跟踪关于俄乌冲突中出现的恶意攻击。

参考及来源：https://securelist.com/bad-magic-apt/109087/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMqgWl9MbggPwGvhKvytdDGvNR3I5mE3l2m5I2eAWbwrJs6qTg8RgzQA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29jk6sAIvOAqrFIiczkWEMeMReJCBk2G2qzIhEb5ZPNyeLOsHiaXw00dPTVYSFehVI5rp10XwibN3rMA/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过