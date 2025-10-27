---
title: 隐匿的威胁：伪装成开源项目的活跃“投毒”事件分析
url: https://www.4hou.com/posts/omkX
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-23
fetch_date: 2025-10-06T22:05:32.844309
---

# 隐匿的威胁：伪装成开源项目的活跃“投毒”事件分析

隐匿的威胁：伪装成开源项目的活跃“投毒”事件分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 隐匿的威胁：伪装成开源项目的活跃“投毒”事件分析

安天
[技术](https://www.4hou.com/category/technology)
2025-04-22 11:13:44

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)81618

收藏

导语：近年来，利用开源生态的信任在GitHub伪装开源项目进行恶意代码“投毒”的攻击活动持续存在。

**1 概述**

近年来，利用开源生态的信任在GitHub伪装开源项目进行恶意代码“投毒”的攻击活动持续存在。自2024年底以来，安天CERT持续监测到通过此方式投递使用Electron打包的远控木马的攻击活动。攻击者通过伪装漏洞利用工具、游戏外挂等，针对下载开源项目进行编译、开发和使用的用户群体，将恶意代码植入开源代码的Visual Studio项目编译配置中，使项目在编译时先执行隐蔽命令，并利用多层不同语言和编译工具链开发的载荷实现混淆加载，规避安全检测，最终执行使用Electron打包的远控木马。相关攻击活动仍在活跃，样本中载荷下载URL等基础设施仍可访问。

目前相关样本在各类杀毒引擎中检出率较低，安天AVL SDK反病毒引擎通过全格式精准识别和深度预处理，支持对使用Electron打包的asar等格式的应用程序分发包裹文件进行细粒度拆解，对内嵌的恶意脚本等子文件进行精准检测。安天智甲终端防御系统可实现对该远控木马的有效查杀。

ASAR文件是一种常用于Electron应用程序的专有格式。其全称为“Atom Shell Archive”，是一种档案文件格式，类似于ZIP或TAR，能够将多个文件打包整合为一个文件。它把应用所需的众多文件，如JavaScript文件、HTML文件、CSS文件、图片、字体等资源，按照特定的结构和算法打包成一个文件。

该格式文件相关信息详见安天病毒百科。

![1745288411109897.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250422/1745291463101204.png "1745288411109897.png")

图 1-1长按识别二维码查看ASAR文件详细信息

**2 攻击活动分析**

攻击者创建漏洞利用工具、游戏外挂等内容的开源项目，在其Visual Studio项目配置中嵌入恶意编译配置代码，并上传至GitHub开源平台，利用开源用户对开源资源的信任诱导下载。

![2-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250422/1745291464201513.png "1745288394170615.png")

图 2‑1在开源平台的部分投毒项目

伪装的项目利用GitHub Action功能自动向项目仓库中反复提交当前日期，使得项目最后更新日期始终较新，增加受害者下载编译项目的几率。其提交代码使用了硬编码的邮箱地址ischhfd83@rambler.ru。

![2-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250422/1745291465445418.png "1745288385292929.png")

图 2‑2自动提交项目代码

恶意代码通过Visual Studio项目的PreBuildEvent机制触发，该设置项用于指定项目编译前执行的命令行代码，存储在项目文件中（.\*proj文件，如.vcproj、.vbproj等），可通过项目属性窗口查看，无法通过检查项目源代码发现。当编译项目代码时恶意代码便会触发执行。

![2-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250422/1745291466186964.png "1745288376760328.png")

图 2‑3通过项目属性查看恶意代码

![2-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250422/1745291466734488.png "1745288365194814.png")

图 2‑4通过项目文件查看恶意代码

该代码利用Bat、PowerShell脚本和Base64、AES等算法，嵌套执行多层后续载荷，尝试从pastebin、rlim等多个公开网站中获取下载地址，从该地址下载一个包含多个文件的加密压缩包并解压（压缩包中的文件为Electron打包的一组Node.JS程序），然后执行解压出的主程序SearchFilter.exe。使用Electron打包的程序实际执行的是JavaScript代码，代码进行了高度扁平化混淆，实现了通过Telegram API回传系统信息、反虚拟机、关闭Windows Defender反病毒软件、屏幕截图、计划任务持久化、下载后续载荷等远控功能。

![2-5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250422/1745291467520617.png "1745288356373012.png")

图 2‑5多层载荷

![2-6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250422/1745291468166285.png "1745288347751043.png")

图 2‑6下载执行的Electron打包程序

由于攻击手法较新，截至本报告发稿时，在国家计算机病毒协同分析平台中，恶意开源项目的.vbproj工程文件在各杀毒引擎中检出率较低，目前仅安天检出。

![2-7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250422/1745291468859446.png "1745288336878792.png")

图 2‑7样本检出情况

进一步关联攻击手法、提交代码邮箱地址（ischhfd83@rambler.ru）等信息，发现了更多嵌入了恶意代码的恶意开源项目，项目创建时间几天内到几个月内不等，说明攻击仍在持续进行中，具体列表如下所示。请注意避免下载以下包含恶意代码的开源项目文件。

表 2‑1植入恶意代码的GitHub项目

|  |  |
| --- | --- |
| 嵌入恶意代码的项目 | 伪造项目类型 |
| AurelienConte/Helldivers2-Internal-Cheat-FULL | 游戏外挂 |
| BlackStons/AsyncRAT-Dark-Mode | 远控木马（RAT） |
| Check-W/Autowithdraw | 虚拟货币窃取器 |
| DrMACSH/Aviator-Predictor-FULL | 漏洞利用工具 |
| FunnyDuckyy/Muck-Cheat-FULL-Source | 游戏外挂 |
| Hastorners/PUBG-Cheat-Source | 游戏外挂 |
| hmate9/Valorant-Plus-Cheat | 游戏外挂 |
| Hoddorz/COD-DLL-Injector | 游戏外挂 |
| HouseMades/SilverRAT-FULL-Source-Code | 远控木马（RAT） |
| hustleroleplayid/FiveM-External | 游戏外挂 |
| joobinwaaw/Etherum-Balance-Checker | 虚拟货币窃取器 |
| Kareasst/Simple-RunPE-Process-Hollowing | 进程注入/免杀工具 |
| Karitosmuan/Office-Exploit-Cve2025-Xml-Doc-Docx-Rce-Builder-Fud | 漏洞利用工具 |
| KatosdX/FiveM-External-Cheat | 游戏外挂 |
| Kawa1sk/Email-Bomber-SMTP | 邮件轰炸工具 |
| Kickhing/Reverse-Proxy-Soruce-Code | 网络工具 |
| MyksLoL/League-of-Legends-Cheat-Source | 游戏外挂 |
| MyskHccr/Encryptix-Crypter | 加密/免杀工具 |
| NhanX999/Free-Fire-Monster-Cheat | 游戏外挂 |
| noradlb1/PUBG-Mobile-Bypass-Antiban-BRAVE-Bypass-vb | 游戏外挂 |
| Oxygen1a1/BioGuard-Hwid-Spoofer-Hwid-Changer-BIOS-CPU | 硬件信息伪造工具 |
| Rmejia39/Discord-Token-Password-Stealer | 信息窃取工具 |
| ShelMaxs/Sleak-Crypter-FUD | 加密/免杀工具 |
| Snowjamil/Aviator-Predictor-FULL | 游戏外挂 |
| StupMain/Bitcoin-Auto-Withdraw | 虚拟货币窃取器 |
| Teastors/XWorm-5.6-FULL-Source-Code | 远控木马（RAT） |
| Terdims/Interic-Fortnite-External-Cheat | 游戏外挂 |
| Terdims/Subzero-Fortnite-Cheat | 游戏外挂 |
| therealelyayo/Ethereum-PrivateKey-Checker-Balance | 虚拟货币窃取器 |
| ThoristKaw/Anydesk-Exploit-CVE-2025-12654-RCE-Builder | 漏洞利用工具 |
| TiggoProx8/COD-Warzone-AIO-Tool-FULL-Features | 游戏外挂 |
| Tphinso/COD-MW3-UnlockALL-Tool-FULL | 游戏外挂 |
| YugrajVishwakarma/Bitcoin-bot | 虚拟货币窃取器 |

**3 终端安全防护**

目前，该攻击活动利用Visual Studio开源项目打包和分发内嵌恶意木马绕过反病毒引擎的检测，安天AVL SDK反病毒引擎通过全格式精准识别和深度预处理，支持对asar等应用程序分发包裹文件进行细粒度拆解，对内嵌的恶意脚本等子文件进行精准检测。

建议企业用户部署专业的终端安全 防护产品，对本地新增和启动文件进行实时检测，并周期性进行网内病毒扫描。安天智甲终端安全系列产品（以下简称“智甲”）依托安天自研威胁检测引擎和内核级主动防御能力，可以有效查杀本次发现病毒样本。

智甲可对本地磁盘进行实时监测，对新增文件自动化进行病毒检测，对发现病毒可在其落地时第一时间发送告警并进行处置，避免恶意代码启动。

![3-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250422/1745291469207858.png "1745288307747339.png")

图 3‑1发现病毒时，智甲第一时间捕获并发送告警

智甲还为用户提供统一管理平台，管理员可通过平台集中查看网内威胁事件详情，并批量进行处置，提高终端安全运维效率。

![3-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250422/1745291470946774.png "1745288295192317.png")

图 3‑2通过智甲管理中心查看并完成威胁事件处置

**4 样本对应的ATT&CK映射图谱**

![4-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250422/1745291474167081.png "1745288279672363.png")

图 4‑1技术特点对应ATT&CK的映射

ATT&CK技术行为描述表如下。

表 4‑1 ATT&CK技术行为描述表

|  |  |  |
| --- | --- | --- |
| ATT&CK阶段/类别 | 具体行为 | 注释 |
| 资源开发 | 环境整备 | 上传恶意项目 |
| 初始访问 | 入侵供应链 | 利用开源供应链攻击 |
| 执行 | 利用命令和脚本解释器 | 使用VBS和PowerShell |
| 执行 | 利用计划任务/工作 | 创建计划任务 |
| 防御规避 | 反混淆/解码文件或信息 | 解码后续载荷 |
| 削弱防御机制 | 关闭Windows Defender |
| 混淆文件或信息 | 加密载荷 |
| 虚拟化/沙箱逃逸 | 检测虚拟机环境 |
| 发现 | 规避调试器 | 获取和规避进程 |
| 发现进程 | 获取系统进程 |
| 发现系统信息 | 获取系统基础信息 |
| 发现系统地理位置 | 获取系统地理位置 |
| 虚拟化/沙箱逃逸 | 检测虚拟机环境 |
| 收集 | 自动收集 | 自动获取数据 |
| 屏幕捕获 | 捕获屏幕截图 |
| 命令与控制 | 使用应用层协议 | 使用HTTP协议 |
| 利用合法Web服务 | 利用Pastebin等在线服务 |
| 数据渗出 | 使用C2信道回传 | 使用C2信道回传 |
| 影响 | 金融窃取 | 窃取加密钱包 |

**5  安天澜砥威胁检测分析垂直大模型分析与评估**

安天澜砥威胁检测分析垂直大模型对app.asar包样本进行自动化分析，解析内容如下：

|  |
| --- |
| 根据提供的日志和分析结果，可以得出以下结论：  **判定结论**  初步判定结论为 Trojan.Win32.Bandos 木马，被识别为恶意软件。以下是详细的判定和评估：  **准确度评估**  评估日志中的结果准确度约为85%。原因如下：多个特征段看起来是无意义的字符数据，但结合上下文可能暗示混淆或加密技术的使用。结果中包含危险调用和恶意行为的迹象。  **判定依据**  1.  危险调用和可疑行为：  **·**日志中包含多次内存操作和函数调用，包括处理二进制数据的迹象，这可能用于恶意行为，例如内存注入(0x48 0xFF 0xC3)。  **·**出现了“Anti-Virus”相关的信息，可能与检测或规避安全机制的功能有关。  **·**"ENAMETOOLONG"、"IDECODERERROR" 等错误或状态信息暗示可能在试图访问或操作文件系统时扰乱正常操作。  2.  特征段分析：  **·**多处出现“;;;;;AAAA,O”和其他无实际意义的字符序列，可能表明填充或混淆技术。  **·**编码中的 ?? 表示数据未被选为特征，通常在特征很可能是加密或随机的数据时出现。  **·**段中包含的指令集和全局变量(例如 V(60)+e[3][0]+"y")，表明可能有动态构造和运行时代码生成的行为，属于木马常用的方法。  3.  整体逻辑和行为：  **·**日志结尾指出多个缓冲处理和指针操作，这是许多木马用来修改进程内存或加载恶意代码的常见手...