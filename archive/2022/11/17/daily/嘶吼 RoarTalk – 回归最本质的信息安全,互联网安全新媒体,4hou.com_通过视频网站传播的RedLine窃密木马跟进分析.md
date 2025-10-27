---
title: 通过视频网站传播的RedLine窃密木马跟进分析
url: https://www.4hou.com/posts/QLlZ
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-17
fetch_date: 2025-10-03T22:58:07.184467
---

# 通过视频网站传播的RedLine窃密木马跟进分析

通过视频网站传播的RedLine窃密木马跟进分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 通过视频网站传播的RedLine窃密木马跟进分析

安天
[行业](https://www.4hou.com/category/industry)
2022-11-16 16:30:47

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)134988

收藏

导语：安天智甲可实现对该窃密木马、挖矿程序等恶意软件的有效查杀。

**1.概述**

安天自2021年11月发布《通过视频网站传播的RedLine窃密木马分析》[1]报告后，始终对此类借助视频分享网站传播的攻击活动保持关注。近日，安天CERT在监测通过视频网站传播RedLine窃密木马的攻击活动中发现攻击者增加了自动登录视频网站发布恶意视频的攻击模块，实现了“发布视频->窃取账号->用窃取到的账号进一步传播”的攻击流程自动化体系，增强了恶意代码传播扩散的能力。

攻击者利用视频网站YouTube上传破解软件、游戏作弊程序等内容的视频，并在视频简介中添加恶意下载链接，诱导用户下载恶意代码。恶意代码会释放并执行RedLine窃密木马、Ethminer挖矿程序，以及利用受害者的账号上传钓鱼视频的自动传播模块。直接在受害者设备和网络环境中执行视频上传功能的攻击手段可在一定程度上绕过平台的风险控制机制，提高攻击成功率。

RedLine窃密木马最早于2020年3月被发现，是流行的窃密木马家族之一，国内外传播较为广泛。该木马具备多种信息窃取功能，如自动窃取目标系统浏览器、FTP、VPN、即时通讯软件的敏感信息，以及屏幕截图及搜集指定文件等功能。该木马以一次性购买或订阅的形式，在地下论坛出售。

目前该攻击活动仍处于活跃状态，安天CERT将持续跟进分析。经验证，安天智甲终端防御系统（简称IEP）可实现对该窃密木马、挖矿程序等恶意软件的有效查杀。

**2.事件对应的ATT&CK映射图谱**

事件对应的技术特点分布图：

![2-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586230630099.png "1668586230630099.png")

图 2‑1技术特点对应ATT&CK的映射

具体ATT&CK技术行为描述表：

表 2‑1 ATT&CK技术行为描述表

|  |  |  |
| --- | --- | --- |
| ATT&CK阶段/类别 | 具体行为 | 注释 |
| 资源开发 | 获取基础设施 | 搭建服务器 |
| 入侵账户 | 入侵视频网站账户 |
| 能力开发 | 开发自动传播模块 |
| 建立账户 | 建立视频网站账户 |
| 能力获取 | 获取挖矿程序及RedLine木马 |
| 环境整备 | 搭建攻击环境 |
| 初始访问 | 网络钓鱼 | 网络钓鱼 |
| 执行 | 诱导用户执行 | 诱导用户执行 |
| 持久化 | 利用自动启动执行引导或登录 | 设置启动项 |
| 利用计划任务/工作 | 设置计划任务 |
| 防御规避 | 反混淆/解码文件或信息 | 解密载荷 |
| 隐藏行为 | 隐藏行为 |
| 削弱防御机制 | 修改反病毒API |
| 混淆文件或信息 | 加密载荷 |
| 进程注入 | 进程注入 |
| 凭证访问 | 从存储密码的位置获取凭证 | 获取浏览器保存的密码 |
| 窃取Web会话Cookie | 获取浏览器Cookie |
| 发现 | 发现文件和目录 | 发现文件和目录 |
| 发现软件 | 发现软件 |
| 发现系统信息 | 发现系统信息 |
| 发现系统地理位置 | 发现系统语言区域 |
| 发现系统所有者/用户 | 发现系统用户 |
| 收集 | 自动收集 | 自动收集 |
| 数据暂存 | 数据暂存 |
| 命令与控制 | 使用应用层协议 | 使用应用层协议 |
| 数据渗出 | 自动渗出数据 | 自动回传数据 |
| 限制传输数据大小 | 限制文件收集最多50MB |
| 使用C2信道回传 | 使用C2信道回传 |
| 影响 | 资源劫持 | 挖矿劫持系统计算资源 |

**3.防护建议**

为有效防御此类恶意代码，提升安全防护水平，安天建议企业采取如下防护措施：

3.1 终端防护

1.安装终端防护系统：安装反病毒软件，建议安装安天智甲终端防御系统；

2.加强口令强度：避免使用弱口令，建议使用16位或更长的密码，包括大小写字母、数字和符号在内的组合，同时避免多个服务器使用相同口令；

3.部署入侵检测系统（IDS）：部署流量监控类软件或设备，便于对恶意代码的发现与追踪溯源。安天探海威胁检测系统（PTD）以网络流量为检测分析对象，能精准检测出已知海量恶意代码和网络攻击活动，有效发现网络可疑行为、资产和各类未知威胁；

3.2  网站传播防护

1.建议使用官方网站下载的正版软件。如无官方网站建议使用可信来源进行下载，下载后使用反病毒软件进行扫描；

2.建议使用沙箱环境执行可疑的文件，在确保安全的情况下再使用主机执行。安天追影威胁分析系统（PTA）采用深度静态分析与沙箱动态加载执行的组合机理，可有效检出分析鉴定各类已知与未知威胁。

3.3 遭受攻击及时发起应急响应

联系应急响应团队：若遭受恶意软件攻击，建议及时隔离被攻击主机，并保护现场等待安全工程师对计算机进行排查；安天7\*24小时服务热线：400-840-9234。

经验证，安天智甲终端防御系统（简称IEP）可实现对该窃密木马、挖矿程序等恶意软件的有效查杀。

![3-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586318103820.png "1668586318103820.png")

图3‑1 安天智甲为用户终端提供有效防护

**4.攻击流程**

攻击者在视频网站YouTube上传钓鱼视频诱导用户下载包含恶意代码的压缩包。用户下载并执行其中的恶意代码后，其中的自解压程序会释放多个exe文件，包括RedLine窃密木马cool.exe、挖矿程序h\*\*.exe以及用于自动传播恶意代码的AutoRun.exe、nir.exe、p\*\*.bat、j\*\*.bat等（不文明词语以\*隐去）。攻击流程如下图所示。

![4-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586336122373.png "1668586336122373.png")![4-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586396309668.png "1668586396309668.png")

图4-1 通过视频网站自动传播的恶意代码事件流程图

详细攻击流程描述如下。

1.   攻击者向视频网站Youtube投递钓鱼视频（含有恶意压缩包下载地址）；

2.   受害者下载恶意压缩包，压缩包中的Installer.exe自解压释放多个exe及bat文件后运行cool.exe、h\*\*.exe及AutoRun.exe；

3.   cool.exe为RedLine窃密木马，能够窃取系统信息、浏览器数据、软件配置等重要文件并回传至C2；

4.   h\*\*.exe为挖矿程序，利用存储在自身资源中的RunPE.dll将挖矿程序ethminer.exe镂空注入到explorer.exe中执行；

5.   AutoRun.exe为自动传播程序，运行p\*\*.bat以利用nir.exe以无窗口隐藏模式启动j\*\*.bat。j\*\*.bat依次运行MakiseKurisu.exe、download.exe和upload.exe；

6.   MakiseKurisu.exe窃取浏览器中的Cookies，并将其存储到临时文件中；

7.   download.exe下载7z压缩包，其中包含多组用于后续上传的钓鱼视频及配套图片封面、描述文本；

8.   upload.exe利用临时文件中Youtube及Google的Cookie，将下载的视频上传到Youtube。

**5.样本分析**

5.1 样本标签

表5‑1 二进制可执行文件

|  |  |
| --- | --- |
| 病毒名称 | Trojan/Win32.ChildHaveTrojan |
| 原始文件名 | Installer.exe |
| MD5 | 9C4CE3073F2EA119951BD3226C839504 |
| 处理器架构 | Intel 386 or   later, and compatibles |
| 文件大小 | 24.09 MB   (25,255,643字节) |
| 文件格式 | BinExecute/Microsoft.EXE[:X86] |
| 时间戳 | 2022-03-03   13:15:57 UTC |
| 数字签名 | 无 |
| 加壳类型 | 无 |
| VT首次上传时间 | 2022-08-03 05:05:32   UTC |
| VT检测结果 | 33/68 |

 5.2 详细分析

压缩包中包含Installer.exe及多个用于伪装的正常DLL文件。

![5-1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586586201138.png "1668586586201138.png")

图5‑1 压缩包中的文件

Installer.exe为WinRAR自解压程序，会将多个exe及bat文件释放到%Temp%目录下，并依次执行cool.exe、hui.exe、AutoRun.exe。

![5-2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586645510520.png "1668586645510520.png")

图5‑2 自解压脚本

5.2.1 RedLine窃密木马cool.exe

cool.exe外层加载器使用C/C++编写，执行后利用进程镂空技术加载RedLine窃密木马。

![5-3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586667758609.png "1668586667758609.png")

 图5‑3 解密RedLine窃密木马并注入执行

检测系统语言区域，若为“亚美尼亚、阿塞拜疆、白俄罗斯、哈萨克斯坦、吉尔吉斯斯坦、摩尔多瓦、塔吉克斯坦、乌兹别克斯坦、乌克兰、俄罗斯”之一，则退出自身，不再继续执行。

![5-4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586676547897.png "1668586676547897.png")

图5‑4 检测语言区域

使用C#语言中的ChannelFactory与C2服务器45.150.108.67:80进行TCP通信，获取待窃密的数据列表等配置信息，目前该服务器已失效。

![5-5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586690205628.png "1668586690205628.png")

图5‑5 连接C2

RedLine窃密木马能够窃取硬件信息、浏览器数据（保存的密码、Cookie、自动填充、信用卡）、FTP客户端数据、部分VPN软件配置等，还可以根据C2配置收集指定路径或文件名格式的文件。详情可参考安天此前发布的报告《通过视频网站传播的RedLine窃密木马分析》[1]。

5.2.2 挖矿模块h\*\*.exe

修改AmsiScanBuffer反病毒API函数入口点代码，避免后续执行的Powershell代码被反病毒程序查杀。

![5-6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586710199337.png "1668586710199337.png")

图5‑6 修改反病毒API入口点

将自身复制到%Appdata%\Google\Chrome\updater.exe并设置计划任务或自启动注册表项。

![5-7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586724278110.png "1668586724278110.png")

图5‑7 设置持久化

从资源“gtoplrfnypylyb”中解密出一个zip压缩包，压缩包内含挖矿程序“ethminer.exe”。

![5-8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586739385982.png "1668586739385982.png")

图5‑8 解密获得挖矿程序

从资源“zwslgktgnwpvyauynyb”中解密出载荷“RunPE.dll”，用于将PE文件镂空注入到explorer.exe中执行。

![5-9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586748171702.png "1668586748171702.png")

图5‑9 通过注入执行挖矿程序

注入的PE文件为上述压缩包中的Ethminer挖矿程序。

![5-10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586756213297.png "1668586756213297.png")

图5‑10 注入的可执行程序

5.2.3 自启动模块AutoRun.exe

AutoRun.exe功能为将自身复制到启动（Startup）路径下，实现自启动。

![5-11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586853109295.png "1668586853109295.png")

图5‑11 复制到启动目录

然后执行p\*\*.bat。

![5-12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221116/1668586865198172.png "1668586865198172.png")

图5‑12 执行pidorpizda.bat

p\*\*.bat的功能为利用nir.exe以后台隐藏模式启动j\*\*.bat。j\*\*.bat功能为启动MakiseKurisu.exe、download.exe和upload.exe。

![5-13.png](https://img.4hou.com/uploads/ueditor/php/upl...