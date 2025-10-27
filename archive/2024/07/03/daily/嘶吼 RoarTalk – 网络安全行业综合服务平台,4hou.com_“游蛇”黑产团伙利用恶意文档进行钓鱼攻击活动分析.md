---
title: “游蛇”黑产团伙利用恶意文档进行钓鱼攻击活动分析
url: https://www.4hou.com/posts/6Mol
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-03
fetch_date: 2025-10-06T17:41:38.299005
---

# “游蛇”黑产团伙利用恶意文档进行钓鱼攻击活动分析

“游蛇”黑产团伙利用恶意文档进行钓鱼攻击活动分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# “游蛇”黑产团伙利用恶意文档进行钓鱼攻击活动分析

安天
[技术](https://www.4hou.com/category/technology)
2024-07-02 15:08:58

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)129128

收藏

导语：近期，安天CERT监测到“游蛇”黑产团伙针对财税人员传播恶意Excel文件，诱导用户点击其中的超链接跳转至钓鱼网站，从中下载执行恶意程序。

![封面图.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828993745877.jpg "1719828993745877.jpg")

**1 概览**

“游蛇”黑产团伙自2022年下半年开始活跃至今，针对国内用户发起了大量钓鱼攻击和诈骗活动。该类黑产传播的恶意程序变种多、频繁更换免杀手段及基础设施、攻击目标所涉及的行业广泛。近期，安天CERT监测到“游蛇”黑产团伙针对财税人员传播恶意Excel文件，诱导用户点击其中的超链接跳转至钓鱼网站，从中下载执行恶意程序。

恶意程序执行后加载恶意的Index.asp文件，然后分多个阶段下载执行恶意AutoHotKey、Python脚本、以及两段Shellcode，最终在受害者计算机的内存中执行远控木马。该远控木马具备键盘记录、剪贴板监控、屏幕截图等基本窃密功能，并支持接收执行多种远控命令。“游蛇”黑产团伙攻击者通常会利用远控木马控制受害者计算机中的即时通讯软件，冒充受害者身份进行后续的攻击、诈骗活动。

“游蛇”黑产团伙仍在频繁地对恶意软件、免杀手段以及相关基础设施进行更新，每天依旧有一定数量的用户遭受攻击并被植入远控木马。安天CERT建议用户接收文件时保持警惕，避免点击安全性未知的可执行程序、脚本、文档等文件，以免遭受“游蛇”攻击，造成不必要的损失。

**经验证，安天智甲终端防御系统（简称IEP）可实现对该远控木马的有效查杀**。

排查方案详见本文第四章节，相关防护建议详见第五章节。

**2 技术梳理**

在此次攻击活动中，攻击者投放的诱饵文件是名称为“（六月）**偷-漏涉-税-违规企业名单公示.xlsx**”的Excel文件，诱导用户点击其中的“点击查看”，从而跳转至钓鱼网站中。

![图 2-1诱饵文件.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828953446617.png "1719828953446617.png")

图 2‑1诱饵文件

该钓鱼网站如下图所示，用户点击该网站中的任意按钮后会下载一个名称为“重点稽查企业名单-终端.zip”的压缩包文件，其中包含两个文件：重点稽查企业名单-终端.exe、Index.asp。

![图 2-2钓鱼网站.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828929134107.png "1719828929134107.png")

图 2‑2钓鱼网站

重点稽查企业名单-终端.exe是一款名为“SmartServer智能端口急速版”的服务器工具，该工具运行后会加载同路径中的Index.asp文件。该Index.asp文件中含有恶意代码，执行后分多个阶段下载执行恶意的AutoHotKey、Python脚本、以及两段Shellcode，最终在内存中执行名称为“登录模块.dll”的远控木马。该远控木马具备键盘记录、剪贴板监控、屏幕截图等基本功能，并支持接收执行多种远控命令。整体攻击流程如下图所示：

![图 2-3攻击流程图.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828902130816.png "1719828902130816.png")

图 2‑3攻击流程图

**3 样本分析**

**3.1 重点稽查企业名单-终端.exe、Index.asp**

钓鱼网站的“重点稽查企业名单-终端.zip”压缩包中包含两个文件：重点稽查企业名单-终端.exe、Index.asp。

![图 3-1压缩包内的文件.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828871936604.png "1719828871936604.png")

图 3‑1压缩包内的文件

重点稽查企业名单-终端.exe是一款名为“SmartServer智能端口急速版”的服务器工具，该工具运行后会加载同路径中的Index.asp文件。

![图 3-2程序说明.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828850176414.png "1719828850176414.png")

图 3‑2程序说明

攻击者将恶意代码隐藏在Index.asp文件中，该恶意代码从攻击者服务器中下载文件并保存至受害者主机中的指定文件夹中，并使用cmd命令执行下一阶段的攻击载荷。

![图 3-3 Index.asp文件中的恶意代码.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828780692000.png "1719828780692000.png")

图 3‑3 Index.asp文件中的恶意代码

该恶意代码下载的文件如下表所示：

表 3‑1恶意代码下载的文件

|  |  |
| --- | --- |
| 下载文件 | 保存路径 |
| hxxp://xingyuqiang1688[.]vip/AHK.exe | C:\Users\Public\Music\Update\AutoHotkey\AutoHotkey.exe |
| hxxp://43.135.72[.]124/Run.ahk | C:\Users\Public\Music\Update\AutoHotkey\AutoHotkey.ahk |
| hxxp://xingyuqiang1688[.]vip/1.ahk | C:\Users\Public\Music\Update\AutoHotkey\1.ahk |

**3.2 恶意AutoHotKey脚本**

AutoHotKey是一种在Windows平台中创建自动化键盘、鼠标操作的脚本语言，攻击者利用AutoHotKey执行经过编码的恶意ahk脚本，从服务器中获取下一阶段的攻击载荷，并为AutoHotKey.exe创建计划任务。

表 3‑2恶意AutoHotKey脚本下载的文件

|  |  |  |
| --- | --- | --- |
| 下载文件 | 保存路径 | 备注 |
| 43.135.120[.]185/py.rar | C:\Users\Public\Music\python | 运行Python脚本所需的环境 |
| 43.135.72[.]124/qd.jpg | C:\Users\Public\Music\python | 恶意Python脚本文件 |
| xingyuqiang1688[.]vip/resource.data | C:\Users\Public\Bandizip\data | Bandizip压缩软件相关文件 |
| xingyuqiang1688[.]vip/web32.exe | C:\Users\Public\Bandizip\data |
| xingyuqiang1688[.]vip/English.lang | C:\Users\Public\Bandizip\langs |
| xingyuqiang1688[.]vip/ark.x64.dll | C:\Users\Public\Bandizip |
| xingyuqiang1688[.]vip/Bandizip.exe | C:\Users\Public\Bandizip |
| xingyuqiang1688[.]vip/config.ini | C:\Users\Public\Bandizip |

攻击者利用Bandizip压缩软件使用密码“Ly”对py.rar进行解压缩，该压缩包中含有Python脚本运行所需的环境。

**3.3 恶意Python脚本**

qd.jpg是一个使用Python编写的Shellcode加载器，该脚本用于从Base64编码的指定URL中获取Shellcode，并写入内存中执行。

![图 3-4 qd.jpg主要内容.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828751109820.png "1719828751109820.png")

图 3‑4 qd.jpg主要内容

**3.4 Shellcode执行PE文件**

该Shellcode用于在内存中执行其代码中的PE文件。

![图 3-5 嵌入在Shellcode中的PE文件.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828630118910.png "1719828630118910.png")

图 3‑5嵌入在Shellcode中的PE文件

该PE文件对硬编码的字符串进行倒转，并从中解析出C2配置信息。

![图 3-6 PE文件中的C2配置信息.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828604394072.png "1719828604394072.png")

图 3‑6 PE文件中的C2配置信息

该PE文件与C2服务器进行连接，获取下一阶段的Shellcode并写入注册表HKEY\_CURRENT\_USER\Console\0\ d33f351a4aeea5e608853d1a56661059中。

![图 3-7将Shellcode内容写入注册表中.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828581840288.png "1719828581840288.png")

图 3‑7将Shellcode内容写入注册表中

然后该PE文件读取注册表中的Shellcode并在内存中执行，并将C2信息写入HKEY\_LOCAL\_MACHINE\SOFTWARE\IpDates\_info中。

![图 3-8在注册表中写入C2信息.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828460211204.png "1719828460211204.png")

图 3‑8在注册表中写入C2信息

**3.5 最终载荷**

该Shellcode在内存中执行其中的PE文件，该PE文件是一个DLL文件，原名称为“登录模块.dll”，且导出函数为run。

![图 3-9 最终载荷信息.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828165916360.png "1719828165916360.png")

图 3‑9最终载荷信息

该DLL文件是远控木马，具备键盘记录、剪贴板监控、屏幕截图等基本功能，并支持接收执行多种远控命令。

![图 3-10该远控木马具备的基本功能.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240701/1719828145329909.png "1719828145329909.png")

图 3‑10该远控木马具备的基本功能

**4 排查方案**

**4.1 文件**

|  |
| --- |
| 文件路径 |
| C:\Users\Public\Music\Update\AutoHotkey\AutoHotkey.exe |
| C:\Users\Public\Music\Update\AutoHotkey\AutoHotkey.ahk |
| C:\Users\Public\Music\python\qd.zip |
| C:\Users\Public\Music\python\qd.jpg |
| C:\Users\Public\Music\python\py.rar |
| C:\Users\Public\Bandizip |

**4.2 注册表**

|  |  |
| --- | --- |
| 注册表 | 内容 |
| HKEY\_CURRENT\_USER\Console\0\   d33f351a4aeea5e608853d1a56661059 | 参考图3-7 |
| HKEY\_LOCAL\_MACHINE\SOFTWARE\IpDates\_info | 参考图3-8 |

**4.3 进程**

|  |  |
| --- | --- |
| 进程名称 | 备注 |
| 重点稽查企业名单-终端.exe | SmartServer 智能端口急速版 v 1.3 |
| python.exe | C:\Users\Public\Music\python\pythonw.exe |

**4.4  计划任务**

|  |  |
| --- | --- |
| 计划任务名称 | 启动程序路径 |
| AHK | C:\Users\Public\Music\Update\AutoHotKey\AutoHotKey.exe |

**4.5 网络**

|  |
| --- |
| IoCs |
| hxxp://www.shuiwutl2[.]cn |
| hxxp://xingyuqiang1688[.]vip/AHK.exe |
| hxxp://43.135.72[.]124/Run.ahk |
| hxxp://xingyuqiang1688[.]vip/1.ahk |
| hxxp://43.135.120[.]185/py.rar |
| hxxp://43.135.72[.]124/qd.jpg |
| hxxp://xingyuqiang1688[.]vip/resource.data |
| hxxp://xingyuqiang1688[.]vip/web32.exe |
| hxxp://xingyuqiang1688[.]vip/English.lang |
| hxxp://xingyuqiang1688[.]vip/ark.x64.dll |
| hxxp://xingyuqiang1688[.]vip/Bandizip.exe |
| hxxp://xingyuqiang1688[.]vip/config.ini |
| hxxp://xingyuqiang1688[.]vip/43.135.72.124.bin |
| 43.135.72[.]124:6666 |

**...