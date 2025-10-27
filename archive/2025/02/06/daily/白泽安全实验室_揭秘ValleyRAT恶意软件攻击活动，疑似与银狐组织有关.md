---
title: 揭秘ValleyRAT恶意软件攻击活动，疑似与银狐组织有关
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492532&idx=1&sn=7667f5553927fce86a7587cc607f87c4&chksm=e90dc99ede7a40883a481167f506ae6d9f125e3df7c9faf745e06b07edbc576f09d3f9ac7733&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2025-02-06
fetch_date: 2025-10-06T20:37:06.505382
---

# 揭秘ValleyRAT恶意软件攻击活动，疑似与银狐组织有关

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 揭秘ValleyRAT恶意软件攻击活动，疑似与银狐组织有关

BaizeSec

白泽安全实验室

**一、背景概述**

近日，Morphisec安全研究团队发现并揭露了一起针对全球企业的复杂恶意软件活动，代号为“ ValleyRAT”。该攻击活动利用先进的远程访问木马（RAT）技术，复杂多变的攻击手段等，针对多个行业的企业进行定向攻击。此次攻击活动展示了攻击者在隐蔽性、持久性和技术复杂性上的高度专业化，其攻击背景疑似与银狐（Silver Fox）组织相关。

ValleyRAT背后的攻击者在2024年更新了其战术、技术与程序（TTPs），且在攻击过程中，他们巧妙地重用了旧版本攻击所使用的URL，这种“以旧换新”的手法极具迷惑性。该组织通过多种渠道传播远程访问木马（RAT），包括钓鱼邮件、恶意网站和即时通讯平台等，尤其将目标精准锁定在企业内部的关键岗位，如财务、会计和销售等部门，这些部门通常掌握着大量敏感数据和关键系统权限，一旦被攻破，后果不堪设想。

![](https://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIPspOLKHFhZib6qEVV3zDzElmstHYAG6YSYT9icsr1xgmL9icXXlkPOmKD6J89ymJucTlWbBCj2fZtiaQ/640?wx_fmt=png&from=appmsg)

图 1  ValleyRAT感染链

**二、攻击过程及技术分析**

ValleyRAT的感染链从用户下载一个伪装成Chrome浏览器的文件开始。攻击者精心制作了一个假冒国内的移动商务服务公司“Karlos”的网站，诱导用户下载名为“Setup.zip”的文件，其中包含“Setup.exe”。当用户运行该文件后，一系列复杂的恶意操作便悄然展开。“Setup.exe”（原名fotuy.exe）是一个用.NET编写的文件，它首先会检查自身是否拥有管理员权限，若没有，则会请求获取。随后，它会根据操作系统类型下载四个文件：sscronet.dll、douyin.exe、mpclient.dat和tier0.dll，并将它们保存在“C:\Program Files (x86)\Common Files\System\”目录下。接着，该文件会加载sscronet.dll到内存中，并调用其中的两个导出函数Cronet\_UrlRequest\_Start和Cronet\_UrlRequest\_Read，最终执行douyin.exe。

sscronet.dll是攻击者精心设计的伪装文件，其名称看似合法，实则暗藏玄机。该DLL导出的众多函数中，只有Cronet\_UrlRequest\_Start和Cronet\_UrlRequest\_Read被实际使用。Cronet\_UrlRequest\_Start函数会搜索名为svchost.exe的进程，为其分配内存并写入数据，然后利用CreateThreadpoolWait和ZwAssociateWaitCompletionPacket函数执行DLL文件。而Cronet\_UrlRequest\_Read函数则负责在注册表的“Software\Microsoft\Windows\CurrentVersion\Run”路径下添加名为“MyPythonApp”的条目，以此实现持久化。svchost.exe在这一过程中扮演着“监视者”的角色，其主要职责是确保预定义列表中的某些进程不会运行。攻击者通过将DLL注入svchost.exe，构建了一个监控机制，一旦检测到列表中的进程，便会立即终止它们，从而确保自身代码的持续运行。

douyin.exe是抖音国际版TikTok的可执行文件，攻击者利用DLL侧加载技术对其进行恶意利用。他们将恶意DLL放置在与douyin.exe相同的文件夹中，当douyin.exe运行时，便会加载恶意DLL，进而执行恶意操作。

tier0.dll是Valve的Source Engine及其相关工具的核心动态链接库。当线程开始执行时，它会检查系统中是否已运行nslookup进程，该进程在此处充当互斥锁的角色。如果发现nslookup正在运行，则将其终止；否则，创建一个新的nslookup实例。攻击者采用了一种巧妙的手段来避免检测：他们选择了一个自然接受输入且在用户交互前保持空闲状态的预定义进程，从而在不引起怀疑的情况下执行恶意代码。

mpclient.dat文件是ValleyRAT恶意软件的核心载体，其中包含Donut shellcode和加密的PE文件。shellcode的作用是在内存中解密PE文件并执行，使其无需写入磁盘即可运行。此外，ValleyRAT还会挂钩AmsiScanString、AmsiScanBuffer和EtwEventWrite等函数，以绕过AMSI（反恶意软件扫描接口）和ETW（Windows事件跟踪）等安全机制，从而逃避检测。

**三、ValleyRAT恶意软件介绍**

ValleyRAT是一款用C++编写的RAT，具有典型的RAT功能，如捕获输入、注入操作、屏幕监控和键盘记录等。它通过访问Windows工作站winsta0来控制屏幕、键盘和鼠标，并通过OpenWindowStationW和SetProcessWindowStation函数与用户桌面进行交互，同时利用SetErrorMode(1u)抑制错误对话框，以避免被发现。

在屏幕监控方面，ValleyRAT通过EnumDisplayMonitors函数枚举所有连接的显示器，并通过fnEnum回调函数处理其信息。它使用GetMonitorInfoW函数获取屏幕坐标和显示属性等详细信息，并将这些数据存储在内存中，以便进行屏幕捕获或与显示相关的操作。

键盘记录功能则根据攻击者在样本中嵌入的预定义配置文件激活，攻击者还可以设置注册表键以实现动态配置，而非依赖固定配置。如果一切设置妥当，攻击者会在“ProgramData”目录中创建一个名为“sys.key”的文件，并将记录的按键存储其中。

为了实现持久化，攻击者创建了一个名为“GFIRestart64.exe”的文件，以避免引起怀疑。此外，ValleyRAT还具备反VMware功能，它通过检查“C:\Program Files\VMware\VMware Tools”目录和特定的VMware进程，以及验证系统是否属于“WORKGROUP”、物理内存是否低于1,173,624,064字节、硬盘大小是否超过110GB等条件，来判断自身是否运行在VMware虚拟机中。如果检测到VMware环境，它可能会更改或终止执行，以逃避检测。如果未检测到虚拟机环境，它会尝试连接到www.baidu.com，作为其网络通信检查的一部分。

在C2（命令与控制）通信方面，ValleyRAT在安装过程中初始化C2 IP地址和端口，并通过一系列命令与C2服务器进行交互，执行诸如清理插件、获取系统进程列表、下载和执行文件、设置开机启动等操作。

**四、总结**

ValleyRAT恶意软件连接的C2服务器分布在全球多个地区，部分服务器位于国内。攻击者使用动态域名和快速更换IP地址的策略，以逃避封锁和追踪溯源。所以在面对ValleyRAT恶意软件的攻击威胁时，传统的基于公开情报或简单行为模式的检测技术已显得力不从心，需要针对性调整检测方法及防御技术策略。另外，根据Morphisec的分析，攻击者的主要动机是窃取商业机密、知识产权和财务信息。此外，攻击者还可能利用受感染系统作为跳板，进一步渗透目标企业的合作伙伴或客户网络。

参考链接：

https://www.morphisec.com/blog/rat-race-valleyrat-malware-china/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

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