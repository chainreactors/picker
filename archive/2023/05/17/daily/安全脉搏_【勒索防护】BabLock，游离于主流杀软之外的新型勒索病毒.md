---
title: 【勒索防护】BabLock，游离于主流杀软之外的新型勒索病毒
url: https://www.secpulse.com/archives/200456.html
source: 安全脉搏
date: 2023-05-17
fetch_date: 2025-10-04T11:37:08.368258
---

# 【勒索防护】BabLock，游离于主流杀软之外的新型勒索病毒

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 【勒索防护】BabLock，游离于主流杀软之外的新型勒索病毒

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-05-16

26,399

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221050.gif)

**恶意文件名称：**

BabLock（又名 Rorschach）

**威胁类型：**

勒索病毒

**简单描述：**

该勒索病毒通常通过电子邮件漏洞进行传播，利用三个组件包执行勒索加密功能，它的家族加密速度相当之快，是目前观察到的加密速度最快的勒索软件之一。它会加密受感染计算机上的文件，并要求受害者支付赎金以获取解密。

**恶意文件分析**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-16842210501.gif)

**事件描述**

深信服深盾终端实验室在近期的运营工作中，捕获了一款特殊的勒索病毒，该病毒似乎属于新的勒索家族，但是部分逻辑结构与多个勒索家族相似，如Lockbit2.0、Babuk等。根据提交到VirusTotal 上的样本，发现该家族曾对欧洲、中东、亚洲发动了攻击。在其中一次攻击案例中，发现攻击者使用了电子邮件软件 Zimbra Collaboration (ZCS) 8.8.15 和 9.0 中的远程代码执行 (RCE) 漏洞，即CVE-2022-41352使威胁行为者能够远程执行任意代码。

当勒索软件在具有域管理员权限的域控上启动时，会通过创建组策略对象（GPO）在局域网传播。

该勒索病毒的攻击流程图如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221051.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221052.gif)

**恶意文件分析**

**ATT&CK**

|  |  |  |  |
| --- | --- | --- | --- |
| TA阶段 | T技术 | S技术 | 动作 |
| 初始访问  TA0001 | T1190  利用面向公众的应用程序 | N/A | 利用了电子邮件软件 Zimbra 中的漏洞远程命令执行 |
| 执行  TA0002 | T1059  系统服务 | T1059.003  Windows Command Shell | 使用一系列Windows命令，如bcdedit.exe、net1.exe等 |
| T1047 WMI | N/A | 使用WMIC删除卷影副本 |
| T1106  原生API | N/A | 使用直接系统调用 (syscall) 来启动系统API 函数 |
| T1574  劫持执行流程 | T1574.002  DLL侧加载 | 使用合法的exe程序加载dll文件 |
| 防御规避  TA0005 | T1562  削弱防御 | T1562.004  禁用或修改系统防火墙 | 关闭并禁用系统防火墙 |
| T1562.001  禁用或修改工具 | 终止杀毒软件实时监控程序(Defwatch.exe) |
| T1497  虚拟化/沙箱规避 | T1497.002  基于用户活动 | 只有当—run=xxxx参数正确时，才会执行加密操作 |
| T1140  解密或解混淆文件和信息 | N/A | 勒索软件的有效负载动态在运行时，才会被解码 |
| T1070  指标清除 | T1070.001  清除Windows事件日志 | 清除系统中应用程序、安全、系统、PowerShell的事件日志 |
| T1070.004  文件删除 | 勒索程序执行后，删除勒索相关文件 |
| T1055  进程注入 | T1055.002      PE文件注入 | 注入经VMP加壳后的PE文件 |
| 隐藏工件  T1564 | T1564.010  进程参数欺骗 | 修改进程内存以隐藏进程命令行参数 |
| 发现TA0007 | T1057  枚举进程 | N/A | 枚举当前系统环境中所有正在运行的进程 |
| T1083  文件和目录发现 | N/A | 查询指定的文件、文件夹和文件后缀 |
| T1082  系统信息发现 | N/A | 查询系统默认语言环境 |
| 影响  TA0040 | T1490  禁止系统恢复 | N/A | 删除卷影副本，禁用Windows系统恢复功能 |
| T1489  终止服务 | N/A | 终止与数据库、服务器、备份相关的进程和服务 |
| T1485  数据销毁 | N/A | 使用SHEmptyRecycleBinA清空回收站 |
| T1486  为影响而加密的数据 | N/A | 加密计算机上的文件。 |

该病毒的编译时间早于2022年3月，截止到本文发布，国内外主流50家杀毒软件厂商仍无法识别该勒索病毒的威胁，基于威胁情报和动静态规则的防护软件或安全平台，在面临此类新型病毒时，全部失效。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221052.png)

读取配置文件命令行如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221053.png)

**功能分析**

样本启动后，会立即删除三个勒索相关文件，随后加密系统中的文件，并释放勒索信以诱使受害者通过勒索信中的联系方式与攻击者进行沟通及缴纳赎金，被加密文件添加特定扩展k1k2k3(0- 99)，勒索信文件名“\_r\_e\_a\_d\_m\_e.txt”,勒索信中展示受害者可以通过邮箱与攻击者取得联系，其中勒索信中并未表明赎金金额及支付方式。

\_r\_e\_a\_d\_m\_e.txt勒索信内容如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-16842210531.png)

被加密后文件系统情况：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221056.png)

勒索病毒执行的三个相关程序如下所示：

其中winutils.dll 程序使用魔改后的UPX3.96进行加壳，无法通过标准版本的 UPX 对其进行解包，动态调试进行解包。

**信息收集**

1、查询系统的UUID

UUID用于标识受感染的计算机，以便攻击者对其进行跟踪和管理。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-16842210561.png)

2、查询系统语言

使用GetSystemDefaultUILanguage和GetUserDefaultUILanguage根据系统或用户的默认语言环境，判断当前系统的国家或地区编码，避免加密 CIS 独立国家联合体。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221057.png)

**防御规避**

1、固定参数启动

只有当必选参数—run的值正确时，勒索程序才会执行加密操作，如果密码参数不正确，则不执行任何操作。

```
cy.exe  -run=xxxx
--pt=C:UsersJohnDesktopFileFolderwinutils.dll
--cg=C:UsersJohnDesktopFileFolderconfig.ini
--we=C:UsersJohnDesktopFileFoldercy.exe
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221058.png)

除了必选参数外，该样本还支持余下可选参数形式：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221059.png)

2、Side-Loads(DLL侧载)/“白”+“黑”免杀

使用合法的添加数字证书的软件cy.exe来加载winutils.dll，其中cy.exe是由网络安全公司Palo Alto Networks开发，用于将Cortex XDR平台上的数据转储到本地存储设备中，最初的程序名为cydump.exe。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221061.png)

3、白进程注入

调用如下API函数将shellcode注入白进程notepad.exe的内存中，从而实现在目标进程的上下文中执行任意代码，该操作能够绕过一些杀毒软件、防火墙等的安全措施。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221062.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221063.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221064.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221065.png)

勒索样本启动notepad.exe后，将notepad.exe设置为suspend的状态，注入notepad.exe的shellcode头部填充了一些垃圾字符，清除掉垃圾字符后为PE文件，该PE文件依然是被加壳的，采用VMProtect的壳。勒索软件向notepad.exe内存中一次写入64Kb的数据，如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221066.png)

第一个写入内存的未知中的数据dump下来后，采用VMP的壳，如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200456-1684221067.png)

4、进程参数欺骗技术

将要执行的进程设置为挂起状态并初始化PEB结构，将执行的命令替换成合法参数（与命令参数同等长度的1），随后通过PEB定位进程参数的地址，使用WriteProcessMemory()在内存中重写为真实参数，最后恢复被注入进程，从而能够规避基于程序内存的分析。如执行命令“bcdedit.exe /set {default} recoveryenabled no”其中“/set {default} recoveryenabled no”字符串长度为33，所以替换成33个1来执行命令。

![](https://se...