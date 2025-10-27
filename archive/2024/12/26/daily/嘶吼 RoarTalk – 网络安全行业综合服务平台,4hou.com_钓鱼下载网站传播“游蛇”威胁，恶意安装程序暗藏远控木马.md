---
title: 钓鱼下载网站传播“游蛇”威胁，恶意安装程序暗藏远控木马
url: https://www.4hou.com/posts/6MVz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-26
fetch_date: 2025-10-06T19:34:23.759898
---

# 钓鱼下载网站传播“游蛇”威胁，恶意安装程序暗藏远控木马

钓鱼下载网站传播“游蛇”威胁，恶意安装程序暗藏远控木马 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 钓鱼下载网站传播“游蛇”威胁，恶意安装程序暗藏远控木马

安天
[技术](https://www.4hou.com/category/technology)
2024-12-25 17:02:19

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)128198

收藏

导语：近期，安天CERT监测到“游蛇”黑产团伙利用仿冒成远程控制软件下载站点的钓鱼网站传播恶意MSI安装程序。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735112636140275.jpg "1735112519357367.jpg")

**1 概览**

“游蛇”黑产团伙（又名“银狐”、“谷堕大盗”、“UTG-Q-1000”等）自2022年下半年开始活跃至今，针对国内用户发起了大量攻击活动，以图窃密和诈骗，对企业及个人造成了一定的损失。该黑产团伙主要通过即时通讯软件（微信、企业微信等）、搜索引擎SEO推广、钓鱼邮件等途径传播恶意文件，其传播的恶意文件变种多、免杀手段更换频繁且攻击目标所涉及的行业广泛。近期，安天CERT监测到“游蛇”黑产团伙利用仿冒成远程控制软件下载站点的钓鱼网站传播恶意MSI安装程序。

当恶意MSI安装程序执行后，会在用户选择的安装路径中释放一个正常的安装程序以及一个恶意程序，在桌面中创建指向正常安装程序的快捷方式，并执行恶意程序。恶意程序执行后，从指定URL处获取shellcode并在内存中执行。该shellcode通过异或解密算法进行自解密，在内存中执行嵌入其中的1.dll文件。1.dll文件从指定URL处下载、执行两段shellcode。

第一段shellcode在内存中释放执行RpcTsch.dll，该DLL文件通过RPC创建称为“MM”的计划任务；第二段shellcode在内存中释放执行Dll1.dll，该DLL文件持续对剪贴板内容进行监控，并对符合指定条件的内容进行窃取并连续截取20张图片，推测该DLL文件用于窃取加密货币钱包地址及密钥信息，可能存在黑产团伙之间的“黑吃黑”行为。然后，1.dll对当前的系统环境进行多种检测，收集各类系统信息、构建上线包并与C2服务器连接。攻击者能够利用该恶意文件进行远程控制、信息窃取等恶意操作。

“游蛇”黑产团伙仍在频繁地对恶意软件及免杀手段进行更新，并且由于该黑产团伙使用的远控木马及攻击组件的源代码在网络中流传，因此存在更多恶意变种，每天依旧有一定数量的用户遭受攻击并被植入远控木马。安天CERT建议用户从官方网站下载安装应用程序，避免点击安全性未知的可执行程序、脚本、文档等文件，以免遭受“游蛇”攻击造成损失。

经验证，安天智甲终端防御系统（简称IEP）可有效查杀该远控木马。相关防护建议详见第四章节。

**2 技术梳理**

**2.1 传播阶段**

在此次攻击活动中，攻击者利用仿冒成ToDesk、向日葵等远程控制软件下载站点的钓鱼网站传播恶意程序，并且恶意程序会下载执行用于窃取加密货币钱包地址及密钥信息的组件，因此其攻击目标可能更偏向于网络管理类人员以及涉及黑灰产的人员。当用户点击钓鱼网站中的“下载”按钮时，下载到的将会是打包成压缩文件的恶意安装程序。

![图 2-1仿冒ToDesk的钓鱼网站.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113203135569.png "1735113203135569.png")

图 2‑1仿冒ToDesk的钓鱼网站

![图 2-2仿冒向日葵的钓鱼网站.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113179208163.png "1735113179208163.png")

图 2‑2仿冒向日葵的钓鱼网站

此外，攻击者也在利用仿冒Gmail等电子邮箱登录页面的钓鱼网页传播恶意程序，推测攻击者可能会结合利用钓鱼邮件进行攻击活动。

![图 2-3仿冒Gmail登录页面的钓鱼网页.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113164174073.png "1735113164174073.png")

图 2‑3仿冒Gmail登录页面的钓鱼网页

**2.2 攻击流程**

攻击者利用钓鱼网站传播恶意MSI安装程序，当恶意MSI安装程序执行后，会在用户选择的安装路径中释放一个正常的安装程序以及一个恶意程序，在桌面创建指向正常安装程序的快捷方式，并执行恶意程序。

恶意程序执行后，从指定URL处获取shellcode保存为C:\ProgramData\3文件，并在内存中执行该shellcode。该shellcode通过异或解密算法进行自解密，在内存中执行嵌入其中的1.dll。1.dll创建C:\Users\Public\Documents\MM文件夹，将恶意程序复制到该文件夹中命名为svchos1.exe，然后下载两段shellcode至该文件夹中。

第一段shellcode在内存中释放执行RpcTsch.dll，该DLL文件通过RPC创建名称为“MM”的计划任务；第二段shellcode在内存中释放执行Dll1.dll，该DLL文件持续对剪贴板内容进行监控，对符合指定条件的内容进行窃取并同时连续截取20张图片，推测该DLL文件用于窃取加密货币钱包地址及密钥信息。然后，1.dll通过创建文件及写注册表的方式记录感染时间，创建C:\ProgramData\9.ini文件以及C:\ProgramData\Microsoft Drive1文件夹，遍历窗口检查是否存在指定的安全产品或工具。确认没有相关安全产品或工具运行后，1.dll收集各类系统信息，用以构建上线包与C2服务器进行连接。

上述恶意程序的执行流程如下图所示：

![图 2-4样本执行流程图.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113146987341.png "1735113146987341.png")

图 2‑4样本执行流程图

**3 样本分析**

**3.1  MSI程序**

该恶意MSI程序伪装成ToDesk的安装程序，执行后会将正常的ToDesk下载器以及名称为“aaa安装9.exe”的恶意程序释放至用户选择的安装路径中，并执行该恶意程序。

![图 3-1该恶意MSI程序释放的文件.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113130237227.png "1735113130237227.png")

图 3‑1该恶意MSI程序释放的文件

同时，该恶意MSI程序也会在桌面上创建一个快捷方式，指向正常的ToDesk下载器。

![图 3-2在桌面创建指向正常ToDesk下载器的快捷方式.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113110675820.png "1735113110675820.png")

图 3‑2在桌面创建指向正常ToDesk下载器的快捷方式

**3.2 aaa安装9.exe**

恶意程序“aaa安装9.exe”运行后，从硬编码的URL处下载载荷文件，并保存为文件C:\ProgramData\3。

![图 3-3从硬编码的URL处下载文件并保存至指定路径.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113091136327.png "1735113091136327.png")

图 3‑3从硬编码的URL处下载文件并保存至指定路径

当执行过程中出现异常时，该程序会弹窗显示错误信息。

![图 3-4出现异常时弹窗.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113072735304.png "1735113072735304.png")

图 3‑4出现异常时弹窗

该程序读取文件C:\ProgramData\3，根据文件大小申请一段内存空间，并将该文件内容写入申请的内存空间中执行。

![图 3-5执行下载的shellcode.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113056561221.png "1735113056561221.png")

图 3‑5执行下载的shellcode

该shellcode执行后，通过异或解密的方式对自身代码进行解密。

![图 3-6该shellcode通过异或算法进行自解密.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113030189495.png "1735113030189495.png")

图 3‑6该shellcode通过异或算法进行自解密

申请一段内存空间，将嵌入其中的PE文件写入该段内存中，将内存保护属性指定为PAGE\_EXECUTE\_READWRITE，然后执行该PE文件。

![图 3-7执行下一阶段的PE文件.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113018158944.png "1735113018158944.png")

图 3‑7执行下一阶段的PE文件

**3.3 1.dll**

该PE文件是DLL文件，原名称为“1.dll”。

![图 3-8 该PE文件信息.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735113001459912.png "1735113001459912.png")

图 3‑8 该PE文件信息

1.dll在内存中执行后，检查是否存在C:\Users\Public\Documents\MM\svchos1.exe，若不存在该文件，则检查当前进程是否具有管理员权限，若不是则以管理员权限重新执行当前进程。确认具有管理员权限后，1.dll执行cmd命令在C:\Users\Public\Documents创建MM文件夹，将“aaa安装9.exe”复制到该文件夹中，并命名为svchos1.exe。随后，1.dll创建两个线程，分别从指定URL处下载4.txt和7.txt至C:\Users\Public\Documents\MM中，并执行这两个shellcode。完成以上操作后，1.dll执行其Shellex函数。

![图 3-9 1.dll主要执行流程.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735112976928700.png "1735112976928700.png")

图 3‑9 1.dll主要执行流程

**3.3.1 shellcode-1**

该shellcode同样使用异或算法进行自解密，然后将嵌入其中的PE文件写入内存中执行。该PE文件的原名称为“RpcTsch.dll”，pdb路径为“C:\Users\ZZ\Desktop\RpcTsch\Release\RpcTsch.pdb”。

![图 3-10 RpcTsch.dll信息.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735112957138201.png "1735112957138201.png")

图 3‑10 RpcTsch.dll信息

RpcTsch.dll

该DLL文件通过RPC创建计划任务，计划任务名称为MM，用于当任何用户登录时执行C:\Users\Public\Documents\MM\svchos1.exe。

![图 3-11通过RPC创建计划任务.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735112937123924.png "1735112937123924.png")

图 3‑11通过RPC创建计划任务

**3.3.2 shellcode-2**

该shellcode同样使用异或算法进行自解密，然后将嵌入其中的PE文件写入内存中执行。该PE文件原名称为“Dll1.dll”，pdb路径为“C:\Users\ZZ\Desktop\截图\Release\Dll1.pdb”。

Dll1.dll

该DLL文件持续对剪贴板进行监控，每隔0.5秒窃取符合条件的剪贴板内容并进行截图操作。

![图 3-12 Dll1.dll文件的主要功能.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735112920655990.png "1735112920655990.png")

图 3‑12 Dll1.dll文件的主要功能

当剪贴板中的内容以T开头且长度小于45时，该DLL文件会将剪贴板内容保存至C:\ProgramData\Microsoft Drive\stop.ini中，在同一文件夹中创建以当前日期时间命名的文件夹，同时连续截取20张图片并保存至该文件夹中。

![图 3-13将符合条件的剪贴板内容保存至stop.ini中并截图.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735112903501230.png "1735112903501230.png")

图 3‑13将符合条件的剪贴板内容保存至stop.ini中并截图

当剪贴板中的内容符合以下条件时，该DLL文件会将剪贴板内容保存至C:\ProgramData\Microsoft Drive\Desktop.ini中，同时连续截取20张图片保存至以当前日期时间命名的文件夹中：

1.字符串长度为64

2.字符串长度大于65且第66位是T

3.字符串以Key开头且长度大于68

4.字符串以0x开头且长度大于40

![图 3-14将符合条件的剪贴板内容保存至Desktop.ini中并截图.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241225/1735112886177278.png "1735112886177278.png")

图 3‑14将符合条件的剪贴板内容保存至Desktop.ini中并截图

**3.4 执行Shellex函数**

执行Shellex函数时，首先解析硬编码在其中的配置信息，用于后续选择是否执行指定的功能。

![图 3-15解析配置信息.png](https://img.4hou...