---
title: APT-C-48（CNC）组织近期钓鱼攻击活动分析报告
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247504896&idx=1&sn=42097a09cd3420fd7168ba1afc84939e&chksm=f9c1e709ceb66e1fd732a72853e48466ae332109a6200a58c1ddab56e1c7d90b902cbbd64027&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-11-27
fetch_date: 2025-10-06T19:19:27.712195
---

# APT-C-48（CNC）组织近期钓鱼攻击活动分析报告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZzmu3TI4c1h7Ydib593Wbw8N3hGEkpl6U9MZRcmC52dONMicEaItkQTmjQ/0?wx_fmt=jpeg)

# APT-C-48（CNC）组织近期钓鱼攻击活动分析报告

高级威胁研究院

360威胁情报中心

##

**APT-C-48**

**CNC**

APT-C-48（CNC）是一个拥有南亚地区政府背景的APT组织，该组织主要攻击目标为政府、军工、教育、科研、医疗、媒体等行业。

近期360安全大脑监测到多起通过投递携带有“简历”相关话题的钓鱼鱼叉邮件作为初始访问阶段攻击载荷，诱导用户收取并打开其中携带的压缩包附件。CNC组织通过将压缩包内携带的恶意可执行文件的图标修改成正常PDF文件图标，并在文件名中加入大量空白字符隐藏真实的文件后缀名来进一步降低用户的警惕性，诱导用户打开恶意可执行文件。

通过对攻击者所使用的技战术和相关资源进一步分析，确认为CNC组织发起的钓鱼攻击。

## **一、攻击流程**

CNC组织通过通过投递携带有“简历”相关话题的钓鱼鱼叉邮件，将压缩包内携带的恶意可执行文件的图标修改成正常PDF文件图标，并在文件名中加入大量空白字符隐藏真实的文件后缀名，诱导用户打开恶意可执行文件。当恶意可执行文件执行后，将会从远端服务器上下载并打开为伪装文档及后续攻击组件。

其攻击流程图如下图1-1所示：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZz8APCytt6iawq7yjaXQeX8fN7jLDftlPwtWvaDL3gHoIS2gITJia53ZaQ/640?wx_fmt=png&from=appmsg)

图1-1 攻击流程

## **二、详细分析**

### **1.样本分析**

在本次行动中，我们捕获到了一批CNC组织所使用的样本，其功能大同小异，同属于下载器。攻击者将样本图标修改为PDF文档图标，如下图1-2所示，降低用户警惕性。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZzS4KYeL6QZrkspT8clBm5HQH2JYsl6dFUmT7WWNaWcmXvd4BWar8L6A/640?wx_fmt=png&from=appmsg)

图1-2 恶意样本图标

在样本中，相关字符串采取动态解密的方式用以规避反病毒软件静态扫描，解密算法采用chacha20，如下图1-3所示。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZzbYIXD95iaAYwonRHFkeToxkWS2Bp2CStPqf7Oy4wJoCiaEGYgRvRTqnA/640?wx_fmt=png&from=appmsg)

图1-3 chacha20

在样本执行后，首先会动态获取相关API地址、动态解密相关字符串，其中涉及字符串主要包含以下内容：

* 下载伪装PDF文档及后续攻击组件相关URL
* 伪装PDF文档名、攻击组件名、攻击组件落地路径
* 计划任务等信息相关字符串

接着下载伪装文档到当前目录下，其名称通常涉及“简历”相关话题。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZzlZSDWsIDXZ8p3ib49BJ7JptdIIIXQiblr75RZ9WYSBxnBZeYp7lBubkg/640?wx_fmt=png&from=appmsg)

图1-4 下载伪装PDF文档

通过”C:\Windows\System32\cmd.exe /c”命令打开该伪装PDF文档用以迷惑用户。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZzq0iaWKrNN5HfZU9tRE0cyZp5nhBju5icwjoY25e81kV3YlicnZ8cW4xZg/640?wx_fmt=png&from=appmsg)

图1-5 打开伪装PDF文档

紧接着通过遍历进程列表比对进程名来进行反调试，并且在未发现进程列表中存在相关敏感进程后，将通过查询注册表HKEY\_LOCAL\_MACHINE\HARDWARE\DESCRIPTION\System\SystemBiosVersion项来进行反虚拟机操作。其中，主要涉及进程如下表1-1所示：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ollydbg.exe | x64dbg.exe | idag.exe | idaw.exe | idaq.exe |
| idaq64.exe | ImmunityDebugger.exe | Wireshark.exe | dumpcap.exe | HookExplorer.exe |
| ImportREC.exe | LordPE.exe | PEiD.exe | PETools.exe | procexp.exe |
| procexp64.exe | procmon.exe | windbg.exe | ResourceHacker.exe | ProcessHacker.exe |
| QzhddrUpdate.exe | QzhddrSrv.exe | QzhddrGuard.exe | iSafeClient.exe | nedr-agent.exe |
| antivirus.exe | nedr-etd.exe | procdump64.exe | vmtoolsd.exe | vmware-tray.exe |
| vmware.exe | VGAuthService.exe | vm3dservice.exe | VirtualBox.exe | VBoxManage.exe |
| VirtualBoxVM.exe | vboxtray.exe |  |  |  |

表1-1 反调试及反虚拟机阶段检查进程名

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZzFa7rDEKwOowHerjibWwFTgHguddSr0856eko74YyJW985bWicvibLS1fw/640?wx_fmt=png&from=appmsg)

图1-6 遍历进程列表

如果在此阶段发现“自身”正处于调试环境或是处于虚拟机当中，则该样本将触发“自毁机制”，利用SetFileInformationByHandle函数删除自身，如下图1-7所示：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZzyM3nZibgjnicORSSLZHIhl1yfQW5DicTctXtXicfDMTpU0cicAA5MuzbUDw/640?wx_fmt=png&from=appmsg)

图1-7 自删除

然后将当前用户名、当前进程列表及模块列表发送到服务端，并通过InternetOpenUrl函数打开访问远程资源，以备后面下载攻击组件使用，如下图1-8、1-9、1-10所示：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZzJ23BjQklPibB2TqAiclkFD6rQlOufWMGzfxCvJTSUiaok7VuJCDMTlJjA/640?wx_fmt=png&from=appmsg)

图1-8 网络通信–上线

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZzmHZpcpz6EUoajoeAT68fRic1V0zDqt7nicMJekgicfnpLOCPq7CC85xqg/640?wx_fmt=png&from=appmsg)

图1-9 InternetOpenUrl打开远程资源

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZzTFkwyYRrXj8VA5sowOlVYjhl8tPh9NjicsGw4DAwpI9trqkHMNTicFvQ/640?wx_fmt=png&from=appmsg)

图1-10 下载后续攻击组件

当上线包发送成功后，获取当前时间，利用COM组件创建计划任务，其目标指向正是要下载的两个后续的攻击组件。该计划任务将会以当前时间为开始，无限期的每隔10分钟执行一次。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZzrWZF8V4LQ9FsKEiavH7icicmlToH9RRWMJBiaNYKy5tRwAAATJGZbAEkFA/640?wx_fmt=png&from=appmsg)

图1-11 利用COM组件创建计划任务

但可惜的是，在分析阶段我们没有获取到其后续的攻击组件。涉及计划任务相关信息如下表1-2所示：

|  |  |
| --- | --- |
| **任务名** | **动作** |
| SCS-Update | 启动   %Appdata%\SCSCloudService\scs64.exe |
| User\_Feed\_Synchronization | 启动   %UserProfile%\AppData\Local\Microsoft\Feeds\msfeedsync.exe |

图1-2计划任务信息

在上述主要工作完成后，将使用SetFileInformationByHandle函数删除自身清理痕迹，如下图1-12所示：

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqfTXj8GwmFhnq8AfLiaQdZz3R0r3hzXydicMHVhibEibTDAHrdGV7PKf8YzxtPI0etT5bQmDnlBB9ib0Q/640?wx_fmt=png&from=appmsg)

图1-12 工作完成后删除自身

### **2. 技战术变化**

在本次行动中涉及样本主要行为逻辑与历史APT-C-48（CNC）组织所使用样本基本一致。

在样本持久化方面采用了COM组件创建计划任务的形式，同时将后续攻击组件的启动从直接创建进程改为了计划任务启动，有效规避反病毒软件动态查杀。

## **三、溯源分析**

通过投递带有“招聘”、“推荐信”、“简历”等题材为话题压缩包附件的鱼叉钓鱼邮件作为初始访问阶段攻击载荷是CNC组织惯用手法。

通过诱导用户自主打开其精心准备的“下载器”，释放伪装文档迷惑用户的同时，在后台下载并执行后续攻击组件，对目标设备进行窃密活动。

APT-C-48（CNC）组织长时间关注教育科研领域，所选鱼叉邮件题材也与之相关。在本次行动中涉及样本主要行为逻辑与历史APT-C-48（CNC）组织所使用样本基本一致，结合受影响用户所处行业领域，我们高度怀疑该行动为APT-C-48（CNC）组织发起。

## **四、防范排查建议**

基于对本次报告中提到的攻击流程进行分析，我们认为可以从以下几个方向排查设备是否存在被感染的痕迹：

1.排查邮箱中是否存在以“简历”为话题，同时邮件内带有压缩包附件，压缩包内存在可疑的PE文件。

2.排查设备是否存在与相关C2服务器通联记录。

3.排查设备是否存在上文提到的可疑计划任务及相关路径下是否存在可疑PE文件。

4.建议将文件夹选项中“显示隐藏文件、文件夹和驱动器”选项勾选，将“隐藏已知文件类型的扩展名”选项取消勾选。

**附录 IOC**

**Hash:**

e74d7351a73c0343c2b607c8f137f847

974f51eb0ea821434504cb22c36fbfab

ef98ed09bedea8daef9d09ec62ffe9cc

**C2 & URL：**

https://panbaiclu[.]com/Guide/Architecture.pdf

https://panbaiclu[.]com/Guide/structure

https://panbaiclu[.]com/Metadata/indexes

https://panbaiclu[.]com/APIs/BaiduSearchAPI

panbaiclu[.]com - 158.255.215[.]248

**团队介绍**

TEAM INTRODUCTION

**360****高级威胁研究院**

360高级威胁研究院是360政企安全集团的核心能力支持部门，由360资深安全专家组成，专注于高级威胁的发现、防御、处置和研究，曾在全球范围内率先捕获双杀、双星、噩梦公式等多起业界知名的0day在野攻击，独家披露多个国家级APT组织的高级行动，赢得业内外的广泛认可，为360保障国家网络安全提供有力支撑。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

360威胁情报中心

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过