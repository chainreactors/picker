---
title: EvilExtractor：一个号称啥都能做的信息窃取程序
url: https://www.4hou.com/posts/lk5J
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-14
fetch_date: 2025-10-04T11:37:19.674435
---

# EvilExtractor：一个号称啥都能做的信息窃取程序

EvilExtractor：一个号称啥都能做的信息窃取程序 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# EvilExtractor：一个号称啥都能做的信息窃取程序

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-05-13 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)114931

收藏

导语：本文将研究用于EvilExtractor的初始攻击方法及其功能。

EvilExtractor（有时拼写为Evil Extractor）是一种旨在针对Windows操作系统并从终端设备提取数据和文件的攻击工具。它包括几个通过FTP服务工作的模块。它是由一家名为Kodex的公司开发的，该公司声称这是一款教育工具。然而，FortiGuard研究表明，攻击者正在积极使用它作为信息窃取工具。

2023年3月，恶意活动显著增加。FortiGuard实验室在3月30日的一次钓鱼电子邮件活动中发现了这种恶意软件。它通常伪装成合法文件，如Adobe PDF或Dropbox文件，但一旦加载，它就开始利用PowerShell的恶意活动。它还包含环境检查和反虚拟机功能。其主要目的似乎是从受攻击的终端窃取浏览器数据和信息，然后将其上传到攻击者的FTP服务器。

研究人员最近审查了一个被注入受害者系统的恶意软件版本，作为分析的一部分，我们发现大多数受害者位于欧洲和美国。开发商于2022年10月发布了其项目，并不断更新以提高其稳定性并加强其模块。

本文将研究用于EvilExtractor的初始攻击方法及其功能。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869118203283.png "1682869118203283.png")

EvilExtractor在网上出售

**初始访问**

带有恶意附件的网络钓鱼电子邮件如下图所示。它伪装成一个帐户确认请求。攻击者还通过使用解压文件的Adobe PDF图标来欺骗受害者。PE标头如下图所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869130831258.png "1682869130831258.png")

钓鱼邮件

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869145111172.png "1682869145111172.png")

“Account\_Info.exe”的文件标头

执行文件是由PyInstaller封装的Python程序。我们用pyinstxtractor提取它，发现它的主代码文件“contain.pyc”中的“PYARMOR”字符串，是Python脚本的混淆工具，使恶意软件更难被分析和检测。我们从\_pytransform.dll中提取了密钥和iv，并使用AES-GCM解密了“contain.pyc”。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869470529974.png "1682869470529974.png")

" include .pyc"中的代码

除了Python程序之外，我们还观察到了一个可以提取EvilExtractor的.NET加载程序。下图是代码的一部分。它包含Base64编码的数据，该数据是PowerShell脚本。此执行文件由工具“PS2EXE-GUI”生成，该工具可以将PowerShell脚本转换为EXE文件。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869486913204.png "1682869486913204.png")

EvilExtractor的 .Net 代码

**EvilExtractor**

在解密pyc文件之后，我们得到了EvilExtractor的主代码。它是一个PowerShell脚本，包含以下模块：

日期时间检查；

反沙盒；

反虚拟机；

反扫描器；

FTP服务器设置；

窃取数据；

上传被盗数据；

清除日志。

它首先检查系统日期是否在2022.11.9和2023.4.12之间。如果没有，则使用以下命令删除PSReadline中的数据并终止：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869503894629.png "1682869503894629.png")

然后，它比较产品模型，看看它是否匹配以下任何一个：VirtualBox、VMWare、Hyper-V、Parallels、Oracle VM VirtualBox、Citrix Hypervisor、QEMU、KVM、Proxmox VE或Docker，如下图所示。它还将受害者的主机名与来自VirusTotal设备或其他扫描仪/虚拟机的187个名称进行检查，如下图所示。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869518211778.png "1682869518211778.png")

EvilExtractor比较产品模型以进行匹配

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869539427008.png "1682869539427008.png")

虚拟环境和扫描器/虚拟机检查

通过环境检查后，EvilExtractor从http://193[.]42[.]33[.]232下载三个用于窃取数据的组件。这些文件也是使用PyArmor进行混淆处理的Python程序。第一个是“KK2023.zip”，用于窃取浏览器数据并将其保存在“IMP\_Data”文件夹中。它可以从Google Chrome、Microsoft Edge、Opera和Firefox中提取cookie。它还从以下浏览器收集浏览器历史记录和密码：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869558149992.png "1682869558149992.png")

第二个文件是“Confirm.zip”。它是一个将数据保存在“KeyLogs”文件夹中的键盘记录器。最后一个文件“MnMs.zip”是一个网络摄像头提取器。其对应的代码如下图所示。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869575164052.png "1682869575164052.png")

下载Keylogger和Webcam Snapshot函数的组件

EvilExtractor还通过PowerShell脚本收集系统信息，如下图所示。下图显示了一个名为“Credentials.txt”的文本文件中的连接数据。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869593995636.png "1682869593995636.png")

用于收集系统信息的PowerShell脚本

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869664130838.png "1682869664130838.png")

 “Credentials.txt”的内容

EvilExtractor从Desktop和Download文件夹下载具有特定扩展名的文件，包括jpg, png, jpeg, mp4, mpeg, mp3, avi, txt, rtf, xlsx, docx, pptx, pdf, rar, zip, 7z, csv, xml和html。它还使用命令“CopyFromScreen”来捕获屏幕截图，代码如下图所示。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869680164336.png "1682869680164336.png")

下载文件并获取截图

EvilExtractor从受攻击的终端提取所有数据后，将其上传到攻击者的FTP服务器，如下图所示。EvilExtractor的开发人员还为购买其恶意软件的用户提供了FTP服务器。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869695172936.png "1682869695172936.png")

将文件上传到攻击者的FTP服务器

**Kodex 勒索软件**

EvilExtractor还具有勒索软件功能，它被称为“Kodex勒索软件”，如下图所示。我们从上一节提到的.net加载程序中提取了此PowerShell脚本，其勒索软件的脚本与其窃取程序的脚本相似。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869711167436.png "1682869711167436.png")

来自evilextracom[.]com的介绍

它从evidtextractor[.]com下载“zzyy.zip”。解压后的文件（一个7-zip的独立控制台）的详细信息如下图所示。下图显示了它利用“7za.exe”用参数“-p”加密文件，这意味着用密码压缩文件。它还生成一条保存在“KodexRansom”中的勒索消息。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869727159463.png "1682869727159463.png")

“zzyy.zip”中的文件

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869742113611.png "1682869742113611.png")

Kodex勒索软件的PowerShell脚本

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869756248437.png "1682869756248437.png")

勒索消息

**总结**

EvilExtractor是一个多功能信息窃取程序，具有包括勒索软件在内的多种恶意功能。它的PowerShell脚本可以在.NET加载程序或PyArmor中躲避检测。在很短的时间内，它的开发人员已经更新了几个功能，并提高了它的稳定性。本文介绍了攻击者如何通过网络钓鱼邮件发起攻击，以及利用哪些文件来提取EvilExtracrtor PowerShell脚本。本文还详细介绍了EvilExtractor包括哪些功能，它可以收集哪些数据，以及Kodex勒索软件的工作原理。用户应该警惕这种新的信息窃取程序，并谨慎打开可疑邮件。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230430/1682869770295556.png "1682869770295556.png")

攻击链

本文翻译自：https://www.fortinet.com/blog/threat-research/evil-extractor-all-in-one-stealer如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?4qtPgw5n)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/bo2j)

# 相关热文

* [新型钓鱼即服务平...