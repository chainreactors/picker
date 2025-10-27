---
title: 俄乌冲突地区发现新的APT
url: https://www.4hou.com/posts/r7y6
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-25
fetch_date: 2025-10-04T10:34:16.151388
---

# 俄乌冲突地区发现新的APT

俄乌冲突地区发现新的APT - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 俄乌冲突地区发现新的APT

luochicun
[新闻](https://www.4hou.com/category/news)
2023-03-24 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)177487

收藏

导语：我们之前发布了一份与俄罗斯和乌克兰冲突有关的网络活动和威胁形势的介绍，并继续监测这些地区的新威胁。

![abstract_random_red_code-1000x600.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563407134215.jpeg "1679563407134215.jpeg")

自俄乌冲突开始以来，网络攻击就被大量用于其中。我们之前发布了一份与俄罗斯和乌克兰冲突有关的网络活动和威胁形势的介绍，并继续监测这些地区的新威胁。

2022年10月，研究人员发现顿涅茨克、卢甘斯克和克里米亚地区的政府、农业和运输组织出现了大量网络攻击。尽管最初攻击途径尚不清楚，但下一阶段的细节意味着要使用鱼叉式网络钓鱼或类似方法。受害者导航到指向恶意网络服务器上托管的ZIP存档的URL，该存档包含两个文件：

1.诱饵文件（研究人员发现了PDF、XLSX和DOCX版本）；

2.具有双重扩展名（例如.pdf.LNK）的恶意LNK文件，打开后会导致感染；

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563421209972.png "1679563421209972.png")

恶意ZIP存档

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563432511469.png "1679563432511469.png")

虚假文字文件

在一些情况下，诱饵文件的内容与恶意LNK的名称直接相关，以诱使用户激活它。例如，一个档案包含一个名为 “Приказ Минфина ДНР № 176.pdf.lnk” 的LNK文件，诱饵文件在文本中明确提到了它的名字。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563443203453.png "1679563443203453.png")

带有恶意快捷方式文件的诱饵PDF(主题：关于朝鲜民主主义人民共和国财政部第176号法令的信息)

ZIP文件是从托管在webservice-srv[.]online和webservice-srv1[.]online两个域上的不同位置下载的。

已知附件名称，编辑后删除个人信息：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563455106882.png "1679563455106882.png")

当潜在受害者激活ZIP文件中包含的LNK文件时，它会触发一系列事件，导致计算机感染之前未见的恶意框架，我们将其命名为CommonMagic。该活动中使用的恶意软件和技术并不特别复杂，但很有效，并且代码与任何已知的攻击没有直接关系。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563466188683.png "1679563466188683.png")

感染链

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563477148759.png "1679563477148759.png")

安装工作流

恶意LNK指向一个远程托管的恶意MSI文件，该文件由Windows安装程序可执行文件下载并启动。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563490950706.png "1679563490950706.png")

MSI文件实际上是一个滴管程序包，包含一个加密的下一阶段有效负载（service\_pack.dat）、一个滴管脚本（runservice\_pack.vbs）和一个应该显示给受害者的诱饵文件。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563500348904.png "1679563500348904.png")

附件.msi中包含的文件

加密的有效负载和诱饵文件被写入名为%APPDATA%\WinEventCom的文件夹。反过来，VBS滴管脚本是一个启动嵌入式PowerShell脚本的包装器，该脚本使用简单的单字节XOR解密下一阶段，启动它并将其从磁盘中删除。

**service\_pack.dat文件的解密**

Расшифровка файла service\_pack.dat

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563512506756.png "1679563512506756.png")

下一阶段脚本完成安装，它打开诱饵文件并将其显示给用户，将两个名为config和manutil.vbs的文件写入%APPDATA%\WinEventCom，并创建一个名为WindowsActiveXTaskTrigger的任务调度程序作业，以每天执行wscript.exe%APPDATA%\WinEventCom\manutil.vbs命令。

**PowerMagic后门**

初始包释放的脚本manutil.vbs是一个加载程序，用于在PowerShell中编写的以前未知的后门，我们将其命名为PowerMagic。后门的主体从文件%APPDATA%\WinEventCom\config中读取，并使用简单的XOR（密钥：0x10）进行解密。

包含“PowerMagic”字符串的PowerMagic代码片段：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563522374885.png "1679563522374885.png")

启动后，后门会创建一个互斥对象——WinEventCom。然后，它进入一个无限循环，与C&C服务器通信，接收命令并上传结果作为响应。它使用OneDrive和Dropbox文件夹作为传输，使用OAuth刷新令牌作为凭据。

后门每分钟都在执行以下操作：

修改位于/$AppDir/$ClientDir/

下载以文件形式存储在/$AppDir/$ClientTaskDir目录中的命令；

将每个命令作为PowerShell脚本执行；

将执行PowerShell命令的输出上载到云存储，并将其放置在/$AppDir/$ClientResultDir/

**CommonMagic框架**

事实证明，PowerMagic并不是攻击者使用的唯一恶意工具包。PowerMagic的所有受害者都感染了一个更复杂、以前从未见过的模块化恶意框架，我们将其命名为CommonMagic。这个框架是在最初感染PowerShell后门后部署的，这让人们相信CommonMagic是通过PowerMagic部署的。

CommonMagic框架由几个可执行模块组成，所有模块都存储在目录C:\ProgramData\CommonCommand中。模块从独立的可执行文件开始，并通过命名管道进行通信。有专用模块用于与C&C服务器交互、加密和解密C&C流量以及各种恶意行为。

该框架的体系结构如下图所示。CommonMagic框架由几个可执行模块组成，所有模块都存储在目录C:\ProgramData\CommonCommand中。模块从独立的可执行文件开始，并通过命名管道进行通信。有专用模块用于与C&C服务器交互、加密和解密C&C流量以及各种恶意行为。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230323/1679563533112544.png "1679563533112544.png")

该框架的体系结构

**网络通信**

该框架使用OneDrive远程文件夹进行传输。它利用Microsoft Graph API，使用嵌入到模块二进制文件中的OAuth刷新令牌进行身份验证。RapidJSON库用于解析Graph API返回的JSON对象。

一个专用的heartbeat线程会每隔五分钟用受害者的本地时间戳更新一次远程文件

然后，在单独的线程中，网络通信模块从目录

通过OneDrive位置与运营商交换的数据使用RC5Simple开源库进行加密。默认情况下，此库在加密序列的开头使用七字节序列“RC5SIMP”，但后门的开发人员将其更改为“Hwo7X8p”。加密是在一个单独的进程中实现的，通过名为\\.\pipe\PipeMd 和\\.\pipe\PipeCrDtMd管道进行通信。

**插件**

到目前为止，我们已经发现了两个实现恶意业务逻辑的插件。它们位于目录C:\ProgramData\CommonCommand\Other中。

Screenshot (S.exe)——使用GDI API每三秒进行一次屏幕截图；

USB (U.exe) ——从连接的USB设备收集具有以下扩展名文件的内容：.doc、.docx..xls、.xlsx、.rtf、.odt、.ods、.zip、.rar、.txt、.pdf。

**总结**

到目前为止，卡巴斯基实验室的研究人员还没有发现这场活动中使用的样本和数据与任何以前已知的攻击者之间有什么联系。我们也将持续跟踪关于俄乌冲突中出现的恶意攻击。

本文翻译自：https://securelist.com/bad-magic-apt/109087/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GbGiRy1n)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/wp-content/uploads/2017/07/6cfb327dad8fe371f6fa.jpg)

# [luochicun](https://www.4hou.com/member/aOZG)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/aOZG)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou...