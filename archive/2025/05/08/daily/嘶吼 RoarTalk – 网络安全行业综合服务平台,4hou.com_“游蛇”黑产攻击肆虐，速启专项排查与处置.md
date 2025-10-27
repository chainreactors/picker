---
title: “游蛇”黑产攻击肆虐，速启专项排查与处置
url: https://www.4hou.com/posts/8gNg
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-08
fetch_date: 2025-10-06T22:24:09.971022
---

# “游蛇”黑产攻击肆虐，速启专项排查与处置

“游蛇”黑产攻击肆虐，速启专项排查与处置 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# “游蛇”黑产攻击肆虐，速启专项排查与处置

安天
[技术](https://www.4hou.com/category/technology)
2025-05-07 15:07:52

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)87780

收藏

导语：“游蛇”黑产团伙（又名“银狐”、“谷堕大盗”、“UTG-Q-1000”等）自2022年下半年开始活跃至今，针对国内用户发起了大量攻击活动，以图窃密和诈骗，对企业及个人造成了一定的损失。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601498496417.jpg "1746597610500671.jpg")

**1 概述**

“游蛇”黑产团伙（又名“银狐”、“谷堕大盗”、“UTG-Q-1000”等）自2022年下半年开始活跃至今，针对国内用户发起了大量攻击活动，以图窃密和诈骗，对企业及个人造成了一定的损失。该黑产团伙主要通过即时通讯软件（微信、企业微信等）、搜索引擎SEO推广、钓鱼邮件等途径传播恶意文件，其传播的恶意文件变种多、免杀手段更换频繁且攻击目标所涉及的行业广泛。

安天持续对“游蛇”黑产团伙进行跟踪，发布多篇报告。近期，两类较为活跃的恶意样本持续传播：第一类是伪装成文档的恶意程序，此类恶意程序多使用Qt库进行开发，也存在部分恶意程序是在开源软件代码的基础上添加恶意代码形成的，通过释放“白加黑”组件最终执行后门文件。第二类是伪装成应用软件的恶意MSI安装程序，包含正常应用软件安装程序以及其他数十个正常文件，攻击者将“白加黑”组件隐藏在其中，最终执行上线模块及登录模块。

“游蛇”黑产团伙仍在频繁地对恶意软件及免杀手段进行更新，并且由于该黑产团伙使用的远控木马及攻击组件的源代码在网络中流传，因此存在更多恶意变种，每天有大量的用户遭受攻击并被植入远控木马。安天CERT建议用户从官方网站下载安装应用程序，避免点击安全性未知的可执行程序、脚本、文档等文件，以免遭受“游蛇”攻击造成损失。

**用户可以在安天垂直响应平台（https://vs2.antiy.cn）中下载使用“游蛇”专项排查工具和安天系统安全内核分析工具（ATool）对“游蛇”木马进行排查和清除**。

**2 样本分析**

**2.1 伪装成文档的恶意程序列表列举**

表格 2‑1相关样本文件名称

|  |
| --- |
| 样本文件名称 |
| 2025年4月份第一批信息列表pdf.exe |
| 2025年省局辖区315晚会企业曝光名单.exe |
| 2025年4月第二批信息公示pdf.exe |
| 2025年4月第一批公示文件pdf.exe |
| 2025年稳岗补贴名单.exe |
| 关于清明节，放假安排，大家自己查看.exe |
| 稽查人员名单.exe |

**2.1.1 通过QT库开发的恶意程序**

此类恶意程序近期多使用Qt库进行开发，执行后会进行多层反调试检测，并执行大量无效代码以阻碍分析。然后该程序会在内存中执行Shellcode，解密得到一个原名称为“InjectFile.dll”的DLL文件，并执行其“run”导出函数。

![图 2-1 InjectFile.dll文件信息.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601499189108.png "1746597555133233.png")

图 2‑1 InjectFile.dll文件信息

此类DLL文件会对当前进程进行判断，然后注入至目标进程的内存中执行，目前发现此类DLL文件的目标进程包括svchost.exe、spoolsv.exe、explorer.exe、winlogon.exe等。

![图 2-2 此类DLL文件“run”导出函数的主逻辑.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601500100019.png "1746597545157932.png")

图 2‑2此类DLL文件“run”导出函数的主逻辑

然后在指定路径中释放“白加黑”组件，通常由一个可执行程序、一个恶意DLL文件以及一个含有Shellcode内容的BIN文件组成。

![图 2-3 释放“白加黑”组件.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601501192305.png "1746597527201540.png")

图 2‑3释放“白加黑”组件

通过COM接口为释放的“白加黑”组件创建计划任务，计划任务名称为“.NET Framework NGEN v4.0.30318”。

![图 2-4 通过COM接口为“白加黑”组件创建计划任务.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601503100620.png "1746597516133604.png")

图 2‑4通过COM接口为“白加黑”组件创建计划任务

“白加黑”组件中的EXE程序被用于加载执行恶意DLL文件，该恶意DLL文件会读取同路径中BIN文件的内容，对其进行解密并将载荷写入内存中执行。

![图 2-5 读取bin文件内容并写入内存中执行.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601504704239.png "1746597504124770.png")

图 2‑5 读取bin文件内容并写入内存中执行

该载荷是一个原名称为“Server64.dll”的DLL文件，是“游蛇”黑产团伙使用的后门文件，具有网络通信、下载文件、远程控制、窃密等多种功能。

![图 2-6 下载执行功能.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601505109252.png "1746597493108958.png")

图 2‑6下载执行功能

**2.1.2 篡改开源软件代码形成的恶意程序**

近期还发现攻击者通过篡改开源软件的代码形成恶意程序。此类初始恶意样本通常为压缩包文件，内含一个恶意可执行程序和一个后缀名为“.dll”的文件。

![图 2-7 恶意文件组成.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601506125830.png "1746597478169471.png")

图 2‑7恶意文件组成

其中的恶意可执行程序是攻击者在开源软件的源代码基础上，添加恶意的功能函数后形成的。而后缀名为“.dll”的文件则是经过加密的二进制文件。

![图 2-8 恶意代码（左）与开源代码（右）进行比对.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601508176603.png "1746597467372049.png")

图 2‑8恶意代码（左）与开源代码（右）进行比对

恶意代码会读取加密二进制文件内容，对其进行解密得到载荷，并在指定路径中释放和2.1.1中相同的“白加黑”组件。

![图 2-9 读取加密二进制文件内容并进行解密.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601509265855.png "1746597456213974.png")

图 2‑9读取加密二进制文件内容并进行解密

**2.2 伪装成应用软件的恶意MSI安装程序列表举例**

表格 2‑2相关样本文件名称

|  |
| --- |
| 样本文件名称 |
| Google   AI Browser v2.4.1.msi |
| Youdao   Translates v1.1.1.msi |
| King   of WPS v1.1.7.msi |
| Sogou   AI inputs v2.1.4.msi |
| DeepSeek   AI Assiant v2.4.5.msi |

攻击者将“白加黑”组件（uc.exe、UCore.dll、Ucore3.cpy、update.cab）隐藏在MSI安装程序中，其中包含正常应用软件安装程序以及其他数十个正常文件，并且在用户执行后执行其中的正常应用软件安装程序，以此迷惑用户。

![图 2-10 隐藏在MSI安装程序中的恶意组件.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601510112754.png "1746597435117043.png")

图 2‑10隐藏在MSI安装程序中的恶意组件

该MSI安装程序将Ucore3.cpy文件释放至C:\ProgramData\11UCore3.cpy，“白加黑”组件执行后调用UCore.dll中的“run”函数，通过COM接口为释放的“白加黑”组件创建计划任务。

![图 2-11 创建计划任务.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601512849110.png "1746597421206736.png")

图 2‑11创建计划任务

然后读取11UCore3.cpy文件内容，并使用指定密钥对其进行xor解密得到一个DLL文件。

![图 2-12 对11UCore3.cpy文件进行xor解密.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601514207982.png "1746597406429179.png")

图 2‑12对11UCore3.cpy文件进行xor解密

该DLL文件会读取update.cab文件内容，并对其进行RC4解密得到最终载荷。

![图 2-13 对update.cab文件进行RC4解密得到最终载荷.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601515156331.png "1746597395904460.png")

图 2‑13对update.cab文件进行RC4解密得到最终载荷

该载荷文件原名称为“上线模块.dll”，是WinOs远控木马中的一个功能插件。该模块会解析硬编码的C2服务器、功能等配置信息，回连C2服务器获取载荷文件，载荷文件通常为WinOs远控木马的“登录模块”。

![图 2-14 上线模块.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601518912205.png "1746597374138815.png")

图 2‑14上线模块

****3 使用工具**排查与处置“游蛇”木马**

用户可以在安天垂直响应平台（https://vs2.antiy.cn）中下载使用“游蛇”专项排查工具和安天系统安全内核分析工具对“游蛇”木马进行排查和清除。

“游蛇”专项排查工具可用于排查“游蛇”黑产团伙在攻击活动中投放的加载器和加载至内存中的远控木马。

安天系统安全内核分析工具（简称ATool）是一款面向威胁检测与威胁分析人员的Windows系统深度分析工具，其能够有效检测操作系统中潜在的窃密木马、后门及黑客工具等恶意程序并辅助专业人员开展手动处置工作，具有已知威胁有效检测，未知威胁及时发现，顽固感染一键处置等功能特点。

![图 3-1 安天垂直响应平台.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601519144244.png "1746597326984523.png")

图 3‑1安天垂直响应平台

**3.1 使用“游蛇”专项排查工具排查“游蛇”木马**

由于“游蛇”黑产团伙使用的攻击载荷迭代较快，且持续更新免杀技术，为了更精准、更全面的清除受害主机中存在的威胁，客户在使用专项排查工具检出威胁后，可以联系安天应急响应团队（cert@antiy.cn）。

![图 3-2 使用“游蛇”专项排查工具发现恶意进程.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601520827011.png "1746597309137622.png")

图 3‑2 使用“游蛇”专项排查工具发现恶意进程

**3.2 使用安天系统安全内核分析工具清除“游蛇”木马**

发现“游蛇”威胁后，用户可以在安天垂直响应平台下载使用ATool对“游蛇”木马进行清除。例如，在ATool的“进程管理”页面中，右键点击恶意进程“uc.exe”：先点击“在Windows文件管理器中定位”定位“uc.exe”所在的路径，然后点击“终止”结束“uc.exe”进程，最后删除“uc.exe”所在路径中的所有文件。

![图 3-3 使用ATool工具定位、终止恶意进程.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601521203100.png "1746597291155377.png")

图 3‑3使用ATool工具定位、终止恶意进程

在ATool的“计划任务”页面中，使用“查找”功能搜索恶意进程名称，发现并删除恶意计划任务。

![图 3-4 通过恶意进程名称查找恶意计划任务.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601523445452.png "1746597275571410.png")

图 3‑4通过恶意进程名称查找恶意计划任务

此外，ATool针对可执行对象支持四个对象维度的信誉查询，即“发布者信誉”、“内容信誉”、“行为信誉”和“路径信誉（位置信誉）”。点击工具上方的“信誉分析”按钮能够执行对当前清单对象的云端信誉查询，从而帮助用户发现系统中的潜在威胁。

![图 3-5 使用ATool的“信誉分析”功能发现恶意进程.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250507/1746601524116352.png "1746597256863463.png")

图 3‑5使用ATool的“信誉分析”功能发现恶意进程

**4 终端安全防护**

**4.1 部署安天智甲加强终端文件接收和执行防护**

建议企业用户部署专业的终端安全防护产品，对本地新增和启动文件进行实时检测，并周期性进行网内病毒扫描。安天智甲终端安全...