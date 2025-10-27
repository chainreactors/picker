---
title: 通过视频网站传播的RedLine窃密木马跟进分析
url: https://www.secpulse.com/archives/191105.html
source: 安全脉搏
date: 2022-11-17
fetch_date: 2025-10-03T22:59:19.593749
---

# 通过视频网站传播的RedLine窃密木马跟进分析

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

# 通过视频网站传播的RedLine窃密木马跟进分析

[资讯](https://www.secpulse.com/archives/category/news)

[安天移动安全](https://www.secpulse.com/newpage/author?author_id=2082)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-16

10,880

点击上方"蓝字"

关注我们吧！

**01**

**概述**

安天自2021年11月发布[《通过视频网站传播的RedLine窃密木马分析》](http://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650185358&idx=1&sn=4d3a60b1d0bf57e4e20120b20eb3b554&chksm=beb93dbc89ceb4aa598c8786fc0e3982525589480e53955c39e7f59f56ae689705e91d32e34f&scene=21#wechat_redirect)[1]报告后，始终对此类借助视频分享网站传播的攻击活动保持关注。近日，安天CERT在监测通过视频网站传播RedLine窃密木马的攻击活动中发现攻击者增加了自动登录视频网站发布恶意视频的攻击模块，实现了“发布视频->窃取账号->用窃取到的账号进一步传播”的攻击流程自动化体系，增强了恶意代码传播扩散的能力。

攻击者利用视频网站YouTube上传破解软件、游戏作弊程序等内容的视频，并在视频简介中添加恶意下载链接，诱导用户下载恶意代码。恶意代码会释放并执行RedLine窃密木马、Ethminer挖矿程序，以及利用受害者的账号上传钓鱼视频的自动传播模块。直接在受害者设备和网络环境中执行视频上传功能的攻击手段可在一定程度上绕过平台的风险控制机制，提高攻击成功率。

RedLine窃密木马最早于2020年3月被发现，是流行的窃密木马家族之一，国内外传播较为广泛。该木马具备多种信息窃取功能，如自动窃取目标系统浏览器、FTP、VPN、即时通讯软件的敏感信息，以及屏幕截图及搜集指定文件等功能。该木马以一次性购买或订阅的形式，在地下论坛出售。

目前该攻击活动仍处于活跃状态，安天CERT将持续跟进分析。

**0****2**

**事件对应的ATT&CK映射图谱**

事件对应的技术特点分布图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191105-1668576979.png)

图2‑1 技术特点对应ATT&CK的映射

具体ATT&CK技术行为描述表：

表2‑1 ATT&CK技术行为描述表

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

**03**

**防护建议**

为有效防御此类恶意代码，提升安全防护水平，安天建议企业采取如下防护措施：

## **3.1 终端防护**

1.安装终端防护系统：安装反病毒软件；

2.加强口令强度：避免使用弱口令，建议使用16位或更长的密码，包括大小写字母、数字和符号在内的组合，同时避免多个服务器使用相同口令；

3.部署入侵检测系统（IDS）：部署流量监控类软件或设备，便于对恶意代码的发现与追踪溯源；

## **3.2 网站传播防护**

1.建议使用官方网站下载的正版软件。如无官方网站建议使用可信来源进行下载，下载后使用反病毒软件进行扫描；

2.建议使用沙箱环境执行可疑的文件，在确保安全的情况下再使用主机执行。

## **3.3 遭受攻击及时发起应急响应**

联系应急响应团队：若遭受恶意软件攻击，建议及时隔离被攻击主机，并保护现场等待安全工程师对计算机进行排查；

**04**

**攻击流程**

攻击者在视频网站YouTube上传钓鱼视频诱导用户下载包含恶意代码的压缩包。用户下载并执行其中的恶意代码后，其中的自解压程序会释放多个exe文件，包括RedLine窃密木马cool.exe、挖矿程序h\*\*.exe以及用于自动传播恶意代码的AutoRun.exe、nir.exe、p\*\*.bat、j\*\*.bat等（不文明词语以\*隐去）。攻击流程如下图所示。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191105-1668576983.png)

图4-1 通过视频网站自动传播的恶意代码事件流程图

详细攻击流程描述如下。

（1）攻击者向视频网站Youtube投递钓鱼视频（含有恶意压缩包下载地址）；

（2）受害者下载恶意压缩包，压缩包中的Installer.exe自解压释放多个exe及bat文件后运行cool.exe、h\*\*.exe及AutoRun.exe；

（3）cool.exe为RedLine窃密木马，能够窃取系统信息、浏览器数据、软件配置等重要文件并回传至C2；

（4）h\*\*.exe为挖矿程序，利用存储在自身资源中的RunPE.dll将挖矿程序ethminer.exe镂空注入到explorer.exe中执行；

（5）AutoRun.exe为自动传播程序，运行p\*\*.bat以利用nir.exe以无窗口隐藏模式启动j\*\*.bat。j\*\*.bat依次运行MakiseKurisu.exe、download.exe和upload.exe；

（6）MakiseKurisu.exe窃取浏览器中的Cookies，并将其存储到临时文件中；

（7）download.exe下载7z压缩包，其中包含多组用于后续上传的钓鱼视频及配套图片封面、描述文本；

（8）upload.exe利用临时文件中Youtube及Google的Cookie，将下载的视频上传到Youtube。

**05**

**样本分析**

## **5.1 样本标签**

表5‑1 二进制可执行文件

|  |  |
| --- | --- |
| **病毒名称** | Trojan/Win32.ChildHaveTrojan |
| **原始文件名** | Installer.exe |
| **MD5** | 9C4CE3073F2EA119951BD3226C839504 |
| **处理器架构** | Intel 386 or later, and compatibles |
| **文件大小** | 24.09 MB (25,255,643字节) |
| **文件格式** | BinExecute/Microsoft.EXE[:X86] |
| **时间戳** | 2022-03-03 13:15:57 UTC |
| **数字签名** | 无 |
| **加壳类型** | 无 |
| **VT****首次上传时间** | 2022-08-03 05:05:32 UTC |
| **VT****检测结果** | 33/68 |

## **5.2 详细分析**

压缩包中包含Installer.exe及多个用于伪装的正常DLL文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191105-1668576985.png)

图5‑1 压缩包中的文件

Installer.exe为WinRAR自解压程序，会将多个exe及bat文件释放到%Temp%目录下，并依次执行cool.exe、hui.exe、AutoRun.exe。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191105-1668576987.png)

图5‑2 自解压脚本

###

### 5.2.1 RedLine窃密木马cool.exe

cool.exe外层加载器使用C/C++编写，执行后利用进程镂空技术加载RedLine窃密木马。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191105-1668576989.png)

图5‑3 解密RedLine窃密木马并注入执行

检测系统语言区域，若为“亚美尼亚、阿塞拜疆、白俄罗斯、哈萨克斯坦、吉尔吉斯斯坦、摩尔多瓦、塔吉克斯坦、乌兹别克斯坦、乌克兰、俄罗斯”之一，则退出自身，不再继续执行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191105-1668576992.png)

图5‑4 检测语言区域

使用C#语言中的ChannelFactory与C2服务器45.150.108.67:80进行TCP通信，获取待窃密的数据列表等配置信息，目前该服务器已失效。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191105-1668576994.png)

图5‑5 连接C2

RedLine窃密木马能够窃取硬件信息、浏览器数据（保存的密码、Cookie、自动填充、信用卡）、FTP客户端数据、部分VPN软件配置等，还可以根据C2配置收集指定路径或文件名格式的文件。详情可参考安天此前发布的报告《通过视频网站传播的RedLine窃密木马分析》[1]。

### 5.2.2 挖矿模块h\*\*.exe

修改AmsiScanBuffer反病毒API函数入口点代码，避免后续执行的Powershell代码被反病毒程序查杀。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191105-1668576996.png)

图5‑6 修改反病毒API入口点

将自身复制到%Appdata%GoogleChromeupdater.exe并设置计划任务或自启动注册表项。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191105-1668576998.png)

图5‑7 设置持久化

从资源“gtoplrfnypylyb”中解密出一个zip压缩包，压缩包内含挖矿程序“ethminer.exe”。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191105-1668577001.png)

图5‑8 解密获得挖矿程序

从资源“zwslgktgnwpvyauynyb”中解密出载荷“RunPE.dll”，用于将PE文件镂空注入到explorer.exe中执行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-191105-1668577004.png)

图5‑9 通过注入执行挖矿程序

注入的PE文件为上述压缩包...