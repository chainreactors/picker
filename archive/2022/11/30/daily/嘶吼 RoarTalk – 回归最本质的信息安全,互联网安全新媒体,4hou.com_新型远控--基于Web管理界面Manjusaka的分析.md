---
title: 新型远控--基于Web管理界面Manjusaka的分析
url: https://www.4hou.com/posts/9XMz
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-30
fetch_date: 2025-10-04T00:03:08.577393
---

# 新型远控--基于Web管理界面Manjusaka的分析

新型远控--基于Web管理界面Manjusaka的分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型远控--基于Web管理界面Manjusaka的分析

矢安科技
[行业](https://www.4hou.com/category/industry)
2022-11-29 17:39:23

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)206027

收藏

导语：Cisco Talos的研究人员最近发现了一款来自中国、相对较新的攻击框架“Manjusaka”（中文翻译为“牛屎花”），并且已经在野使用。作为防御者，重要的是要跟踪进攻性框架，如Cobalt Strike和silver，以便企业可以有效地防御使用这些工具的攻击。

**介绍**

Cisco Talos的研究人员最近发现了一款来自中国、相对较新的攻击框架“Manjusaka”（中文翻译为“牛屎花”），并且已经在野使用。作为防御者，重要的是要跟踪进攻性框架，如Cobalt Strike和silver，以便企业可以有效地防御使用这些工具的攻击。

研究始于一份恶意的Microsoft Word钓鱼文档(maldoc)，这份文件在2022年6月下半月创建，以青海省海西蒙古藏族自治州最大的城市之一格尔木市的新冠肺炎疫情作为诱饵，其中包含有Cobalt Strike (CS) Beacon。

在调查maldoc感染链时，研究者发现了一个用于检测Manjusaka感染的载荷，它与CS Beacon连接的IP地址相同。这个植入程序是用Rust语言编写的，并找到了适用于Windows和Linux的示例，Windows植入程序包括测试样本，这些样本的C2地址均为内网私有地址。

此外，研究者还在GitHub上发现了Manjusaka——一个用GoLang编写的功能齐全的C2 ELF二进制文件，带有简体中文用户界面，并且开发人员宣传它是一个类似于Cobalt Strike或Sliver的植入框架。

开发人员提供了Manjusaka框架的系统架构，说明了不同组件之间的通信。这些组件中的许多尚未在开源的C2二进制文件中实现。因此很可能该框架还在开发中，部分功能暂未实现，亦或是开发人员打算或已经通过购买服务/工具来提供这些功能，而开源的C2只是测试版本。

![1669711793243.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713423207426.png "1669711802200439.png")

Manjusaka系统架构

**MANJUSAKA 攻击框架**

Manjusaka是用GoLang写的ELF文件，而植入程序是用Rust编写的，包含各种功能，可用于控制受感染的端，包括执行任意命令等。我们发现了植入EXE和ELF版本。满足这些平台的两组样本包含几乎相同的RAT功能和通信机制。

**通信**

该示例向内网地址http://172.16.199.3/global/favicon.png发出HTTP 请求，该地址包含固定会话cookie，而不是由服务器定义的。

HTTP请求中的会话cookie是base64编码的，包含二进制数据的压缩副本，表示随机字节和系统初始信息的组合，用于向C2识别并注册受感染端。下图显示了用于生成这样一个会话cookie的信息。

![1669712057017.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713424579495.png "1669712061131055.png")

在压缩并编码到base64之前，cookie上的信息按下面所述的方式排列。

> 20个随机生成的字节.本地IP地址.用户名.主机名.系统.PID

这种通信遵循一种常规的通信模式，植入体会向一个URL发出请求，在这种情况下，URL是'/global/favicon.png'，如下图所示。

![1669712391895.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713424729117.png "1669712394164043.png")

即使是一个HTTP的GET请求，它也会发送两个字节0x191a。返回由五个字节0x1a1a6e0429组成。

如果没有提供会话cookie，服务器将返回302状态码，重定向到http://micsoft.com。

**载荷的功能**

该植入程序包含大量远程访问木马(RAT)功能，其中包括一些标准功能和一个专用的文件管理模块。

![1669712443445.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713425107142.png "1669712447196243.png")

**RAT 服务的命令**

植入程序可以根据从C2服务器收到的请求和数据在受感染的端上执行以下功能：

l执行任意命令：植入程序可以使用“cmd.exe /c”在系统上运行任意命令。

![1669712460157.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713425671718.png "1669712463577212.png")

l获取指定文件的文件信息：创建和最后写入时间、大小、卷序列号和文件索引。

l获取有关系统上建立的当前网络连接（TCP和UDP）信息，包括本地网络地址、远程地址和所属的进程ID(PID)。

l收集浏览器凭据:针对基于chrome的浏览器使用查询:SELECT signon\_realm, username\_value, password\_value FROM   logins;针对浏览器:谷歌Chrome, Chrome Beta, Microsoft Edge, 360，QQ浏览器等。

l使用命令netsh wlan show profile key=clear收集Wi-Fi SSID信息以及密码。

![1669712475302.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713426158397.png "1669712479585627.png")

l获取Premiumsoft Navicat凭据:Navicat是一个图形化的数据库管理工具，可以连接到各种数据库类型，例如 MySQL、Mongo、Oracle、SQLite、PostgreSQL 等。植入程序会枚举每个配置数据库的服务器上已安装软件的注册表项，并获取端口、用户名及密码的值。

![1669712487431.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713427981646.png "1669712492204136.png")

l截取当前桌面的屏幕截图。

l从终端获取全面的系统信息，包括：

u系统内存信息。

u处理器信息。

u使用“SELECT \* from MSAcpi\_ThermalZoneTemperature”从WMI读取当前和临界温度。

u与系统相连的网络接口信息:名称

u进程和系统时间：用户时间、退出时间、创建时间、内核时间。

u处理模块名称。

u磁盘和驱动器信息：卷序列号、名称、根路径名和磁盘可用空间。

u网络帐户名称、本地组。

uWindows 版本号和主要版本号。

l激活文件管理模块以执行与文件相关的活动。

**文件管理功能**

载荷的文件管理功能包括：

u文件枚举：列出磁盘上指定位置的文件。

u在文件系统上创建目录。

u获取并设置当前工作目录。

u获取文件的完整路径。

u删除磁盘上的文件和目录。

u在两个位置之间移动文件，将文件复制到新位置并删除旧副本。

![1669712508288.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713428145483.png "1669712510129787.png")

u从文件中读取和写入数据。

**ELF变种**

ELF变种的功能集与Windows变种的功能集几乎相同。然而，ELF变种中缺少两个关键功能:从基于chrome的浏览器收集凭证和获取Wi-Fi登录凭证的能力。

就像 Windows 版本一样，ELF 变种也从客户端收集各种系统特定的信息：

u全局系统信息，例如页面大小、当前时间、主机名、系统版本、机器 ID 等。

u/proc/meminfo 中的系统内存信息，包括缓存内存大小、可用内存和总内存、交换内存大小和 Slab 内存大小。

u/proc/uptime的系统正常运行时间：系统正常运行时间和内核空闲时间。

u/proc/os-release和lsb-release中的操作系统标识信息。

u/proc/stat 的内核活动信息。

u/proc/cpuinfo和

/sys/devices/system/cpu/cpu\*/cpufreq/scaling\_max\_freq中的 CPU 信息

u/sys/class/hwmon和/sys/class/thermal/thermal\_zone\*/temp中的温度信息

u/sys/class/net中的网络接口信息和统计信息。

u设备挂载和文件系统信息。SCSI设备信息。

u/etc/passwd中的帐户信息和用户组列表。

两个版本都包含功能相同的文件管理模块，专门用于管理受感染系统上的文件和目录。

![1669713362741.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713428452538.png "1669713367110094.png")

EXE 与 ELF 版本的植入程序，包含功能等效的文件管理模块。

**C2服务器**

GitHub 上的https://github.com/YDHCUI/manjusaka存在C2服务器二进制文件的副本。

它可以监控和管理受感染的端点，并可以为 Windows 和 Linux 生成相应的Payload。而生成的Payload就是前面所描述的 Rust载荷。

C2 服务器和管理面板主要构建在Gin Web框架，该框架用于管理和向基于 Rust的载荷发出命令。

![1669713387891.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713429983136.png "1669713392181059.png")

填写选项后，会按照以下格式向 C2 发出请求生成载荷：

![1669713400797.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713430893817.png "1669713409148684.png")

然后C2服务器将配置好的选项生成rust的载荷。C2使用packr将未配置的基于rust的植入存储在C2二进制文件中，该二进制文件由单个打包的C2二进制文件组成，且没有任何外部依赖。

C2将打开基于GoLang的C2二进制文件中的一个虚拟文件夹，它由位于“plugins/npc.exe”位置的虚拟Rust载荷组成。这个可执行文件是Rust植入程序的预构版本，然后由C2服务器根据通过Web UI输入的C2信息进行修改。

Rust植入包含C2 IP/域的占位符以及以重复特殊字符“$”和“\*”形式的扩展 URL。如，载荷中 C2 IP/Domain 的占位符为（十六进制）：

24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24

然后被C2替换为IP地址，如：

33 39 2E 31 30 34 2E 39 30 2E 34 35 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24

然后将修改后的二进制文件提供下载，以响应前面的HTTP GET请求。

![1669713416732.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221129/1669713422371657.png "1669713422371657.png")

**结论**

Manjusaka 攻击框架的可用性表明了APT组织广泛使用的攻击技术的流行程度。这个新的攻击框架包含攻击者期望从RAT中获得的大部分功能，且它是用最现代和可移植的编程语言编写的。该框架的开发人员可以轻松地集成新的操作系统平台，如MacOS X或其他在嵌入式设备上运行的Linux版本。开发人员提供了 C2的全功能版本，增加了攻击者更多选择。

参考链接：

https://blog.talosintelligence.com/2022/08/manjusaka-offensive-framework.html

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?HLZopDlV)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/de620f130a9785bd8fdb5a7d443befa3.jpg)

# [矢安科技](https://www.4hou.com/...