---
title: “游蛇”黑产利用仿冒的WPS Office下载站传播远控木马
url: https://www.4hou.com/posts/42yV
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-23
fetch_date: 2025-10-06T22:27:15.144294
---

# “游蛇”黑产利用仿冒的WPS Office下载站传播远控木马

“游蛇”黑产利用仿冒的WPS Office下载站传播远控木马 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# “游蛇”黑产利用仿冒的WPS Office下载站传播远控木马

安天
[技术](https://www.4hou.com/category/technology)
2025-05-22 16:55:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)96509

收藏

导语：安天CERT发现“游蛇”黑产利用仿冒的WPS Office下载站传播远控木马，若用户下载该网站的WPS Office，实际下载的是托管在OSS中的虚假安装程序。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902724199824.jpg "1747902724199824.jpg")

**1 概述**

安天CERT发现“游蛇”黑产利用仿冒的WPS Office下载站传播远控木马，若用户下载该网站的WPS Office，实际下载的是托管在OSS中的虚假安装程序。该程序执行后，在临时文件夹%temp%中释放执行一个正常的WPS安装程序，以此迷惑用户，并在C:\ProgramData文件夹中释放三个文件，执行其中的Shine.exe程序后加载恶意libcef.dll文件，该DLL读取1.txt文件，从而在内存中执行原名称为“Install.dll”的文件，调用其Shellex导出函数，最终执行Gh0st远控木马，并创建注册表启动项实现持久化。

“游蛇”黑产团伙（又名“银狐”、“谷堕大盗”、“UTG-Q-1000”等）自2022年下半年开始频繁活跃至今，针对国内用户发起了大量攻击活动，以图窃密和诈骗，对企业及个人造成了一定的损失。该黑产团伙主要通过即时通讯软件（微信、企业微信等）、搜索引擎SEO推广、钓鱼邮件等途径传播恶意文件，其传播的恶意文件变种多、免杀手段更换频繁且攻击目标所涉及的行业广泛。用户可以在安天垂直响应平台（https://vs2.antiy.cn）中下载使用“游蛇”专项排查工具和安天系统安全内核分析工具（ATool）对“Gh0st”木马进行排查和清除。

经验证，安天智甲终端防御系统（简称IEP）可有效查杀该远控木马。

**2 样本分析**

**2.1 仿冒网站**

仿冒成WPS Office下载站的网站hxxps://wpsice[.]com：

![图 2-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902692184242.png "1747902692184242.png")

图 2‑1仿冒网站页面

若点击“立即下载”按钮，将会下载托管在OSS中的虚假安装程序。

![图 2-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902676100831.png "1747902676100831.png")

图 2‑2该仿冒网站的页面源代码

**2.2 虚假安装程序**

表 2‑1样本标签

|  |  |
| --- | --- |
| 病毒名称 | Trojan/Win32.SwimSnake |
| 原始文件名 | WPS\_Setup.exe |
| MD5 | 9232FBCCF8B566B0C0A6D986B65BBC98 |
| 处理器架构 | Intel 386 or later   processors and compatible processors |
| 文件大小 | 253 MB (265,306,009字节) |
| 文件格式 | BinExecute/Microsoft.EXE[:X86] |
| 时间戳 | 2023-05-31 21:15:01 |
| 数字签名 | 无 |
| 加壳类型 | 无 |
| 编译语言 | Microsoft   Visual C/C++ |

该程序执行后，会在临时文件夹%temp%中释放执行一个正常的WPS安装程序，以此迷惑用户。

![图 2-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902664807833.png "1747902664807833.png")

图 2‑3释放执行正常的WPS安装程序

然后在C:\ProgramData中释放三个文件：Shine.exe含有正常的数字签名，libcef.dll是一个恶意DLL文件，1.txt是一个包含Gh0st远控木马的Shellcode。

![图 2-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902650132958.png "1747902650132958.png")

图 2‑4在C:\ProgramData中释放攻击组件

Shine.exe程序运行后加载libcef.dll读取1.txt文件，从而在内存中加载执行一个原名称为“Install.dll”的文件并调用其Shellex导出函数，最终执行Gh0st远控木马。

![图 2-5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902639142385.png "1747902639142385.png")

图 2‑5 Install.dll文件信息

该程序所在路径被添加至注册表启动项“HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run”中实现持久化。

![图 2-6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902626922503.png "1747902626922503.png")

图 2‑6创建注册表启动项实现持久化

**3 使用工具排查与处置**

基于本次攻击活动中攻击者使用Gh0st远控木马家族变种情况，用户可以在安天垂直响应平台（https://vs2.antiy.cn）中下载使用“游蛇”专项排查工具和安天系统安全内核分析工具对Gh0st远控木马进行排查和清除。

“游蛇”专项排查工具可用于排查“游蛇”黑产团伙在攻击活动中投放的加载器和加载至内存中的远控木马（包括Gh0st远控木马家族）。

安天系统安全内核分析工具（简称ATool）是一款面向威胁检测与威胁分析人员的Windows系统深度分析工具，其能够有效检测操作系统中潜在的窃密木马、后门及黑客工具等恶意程序并辅助专业人员开展手动处置工作，具有已知威胁有效检测，未知威胁及时发现，顽固感染一键处置等功能特点。

![图 3-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902611213666.png "1747902611213666.png")

图 3‑1安天垂直响应平台

**3.1 使用“游蛇”专项排查工具排查Gh0st远控木马**

为了更精准、更全面的清除受害主机中存在的威胁，客户在使用专项排查工具检出威胁后，可以联系安天应急响应团队（cert@antiy.cn）。

![图 3-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902599123582.png "1747902599123582.png")

图 3‑2使用“游蛇”专项排查工具发现恶意进程

**3.2 使用安天系统安全内核分析工具清除Gh0st远控木马**

发现Gh0st远控木马后，用户可以在安天垂直响应平台下载使用ATool对该木马进行清除。例如，在ATool的“进程管理”页面中，右键点击恶意进程“Shine.exe”：先点击“在Windows文件管理器中定位”定位“Shine.exe”所在路径，然后点击“终止”结束“Shine.exe”进程，最后删除“Shine.exe”程序所在路径中的恶意文件。

![图 3-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902567190476.png "1747902567190476.png")

图 3‑3使用ATool工具定位、终止恶意进程

在ATool的“自启动项”页面中，使用“查找”功能搜索恶意进程名称，发现并删除恶意自启动项。

![图 3-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902553199798.png "1747902553199798.png")

图 3‑4通过恶意进程名称查找恶意自启动项

此外，ATool针对可执行对象支持四个对象维度的信誉查询，即“发布者信誉”、“内容信誉”、“行为信誉”和“路径信誉（位置信誉）”。点击工具上方的“信誉分析”按钮能够执行对当前清单对象的云端信誉查询，从而帮助用户发现系统中的潜在威胁。

![图 3-5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902516212551.png "1747902516212551.png")

图 3‑5使用ATool的“信誉分析”功能发现恶意进程

**4 终端安全防护**

经过测试，安天智甲终端安全系列产品（以下简称“智甲”）依托安天自研威胁检测引擎和内核级主动防御能力，可以有效查杀和防御本次发现病毒样本。

智甲可对本地磁盘进行实时监测，对新增文件自动化进行病毒检测。针对此次威胁，当病毒文件libcef.dll文件落地本地时，智甲会立即对病毒文件进行查杀并向用户发送告警，有效阻止病毒启动。

![图4-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902505516387.png "1747902505516387.png")

图 4‑1 病毒文件落地时，智甲第一时间捕获并发送告警

另外智甲具备驱动级主动防御模块，可以对进程行为实时监控，当发现进程存在风险行为时可立即拦截，有效防止攻击行为执行。本次事件中，当攻击者利用Shine.exe加载恶意文件libcef.dll时，智甲会通过内存防护模块捕获恶意程序加载行为，并立即拦截。

![图4-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902490594916.png "1747902490594916.png")

图4-2直接主动防御模块拦截恶意程序加载行为

智甲还为用户提供统一管理平台，管理员可通过平台集中查看网内威胁事件详情，并批量进行处置，提高终端安全运维效率。

![图4-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250522/1747902473108816.png "1747902473108816.png")

图4-3智甲管理中心助力管理员实现高效的终端安全管理

**5 攻击载荷执行体全生命周期与安全产品关键能力映射矩阵**

通过威胁事件分析，得出攻击载荷执行体全生命周期中运行对象和运行动作的攻击过程，可进一步评估终端侧部署的安全防护软件应具备反病毒引擎和主动防御的关键能力映射矩阵。本次系列攻击活动的检测和防御关键能力点描述如下表：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 攻击执行体    生命周期 | | 对象 | 动作 | 威胁检测引擎    关键能力 | 主动防御能力    关键能力 |
| 预    置    与    投    放 | 投    放 | 仿冒网站 | 仿冒WPS   Office下载站，诱导用户下载捆绑了后门的安装程序。程序大于200M。 | 仿冒域名检测 | 1.（主机防火墙）监测应用程序访问C2服务器请求数据包，获取访问的IP、域名和URL，投递引擎检测，拦截威胁C2服务器访问请求数据包  2.（主机防火墙）应用请求IP、Domain和URL为非授信地址设定记录/告警/拦截规则 |
| 加  载  执  行 | 执  行 | 捆绑了后门的安装程序 | 释放文件：  %temp%\WPS\_Setup.exe（白文件）  C:\ProgramData\Shine.exe（白文件）  C:\ProgramData\libcef.dll  C:\ProgramData\1.txt | 1.安装包类型识别  2.安装程序衍生文件拆解并递归检测  3.大文件冗余虚假数据异常识别 | 1.（文件防御）监控磁盘文件创建/修改，投递引擎检测，删除威胁文件  2. (文件防御）设定文件全盘监控 |
| 加载并解密；  1、白加黑加载：  Shine.exe（白文件）  2、解密：  libcef.dll | Shine.exe（白文件）  加载：  libcef.dll  libcef.dll解密：1.txt  解出：Install.dll（可执行文件） | 1、离线数字签名验证  2.PE格式和编译器类型识别  3.PE真实入口点恶意指令检测 | （进程防御）监控进程模块加载，拆解进程全路径、加载模块全路径后，投递引擎检测，拦截威胁模块加载，并删除威胁模块 |
| 内存加载：Install.dll | Gh0st远控木马 | Gh0st远控木马内嵌恶意指令检测 | 1.（内存防御）监控内存加载行为  2. (内存防御）设定禁止加载含有某shellcode内容的内存加载 |
| 持    久    化 | 添加注册表启动项：  libcef.dll | 添加注册表启动项：HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run  值:   字符串: " Management "："C:\Program Data\Shine.exe" | 注册表项检测 | （注册表防御）监控注册表启动项新建/修改，拆解修改注册表进程的文件路径、启动项名称及启动项的内容后，投递引擎检测，删除威胁启动项 |
| 致    效    运    用 | 过    程    致    效 | 远控木马（Gh0st）：Install.dll | 1、收集系统信息发送上线包回连C2    2、等待接收并执行远控指令 | 远控C2域名检测 | 1.（主机防火墙）监测应用程序访问C2服务器请求数据包，获取访问的IP、域名和URL，投递引擎检测，拦截威胁C2服务器访问请求数据包  2.（主机防火墙）应用请求IP、Domain和URL为非授信地址设定记录/告警/拦截规则 |

**6 IoCs**

|  |
| --- |
| IoCs |
| 9232FBCCF8B566B0C0A6D986B65BBC98 |
| A9710294489B6893F59120C5DF76A60C |
| 444F8...