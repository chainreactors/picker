---
title: 新的 GitDoor 和 GraphDoor 后门将 GitHub 和 SharePoint 变成隐蔽 C2 通道
url: https://mp.weixin.qq.com/s/d67gQQVA6ftU0sMXhtHrAg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:42:52.461690
---

# 新的 GitDoor 和 GraphDoor 后门将 GitHub 和 SharePoint 变成隐蔽 C2 通道

# 新的 GitDoor 和 GraphDoor 后门将 GitHub 和 SharePoint 变成隐蔽 C2 通道

爱拍照的老李
爱拍照的老李

爱拍照的老李

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导****读**

亚洲和非洲政府机构成为一场活跃的网络入侵活动的目标，该活动会部署此前未被记录的后门程序，这些程序利用微软SharePoint和GitHub等合法服务作为命令与控制（C2）渠道。

![](https://mmbiz.qpic.cn/mmbiz_png/PaFY6wibdwyLRon5XmO1bu438ODz3TtCmXmyiaPppxtfGzGkHYmLbRsRYs0gIMiagePrfibvue0SKoUhK1ibkzgzNtHKBAL6wOO0WgZOWqvHian1E/640?wx_fmt=png&from=appmsg)

卡巴斯基将此次活动的代号定为暗影云行动。这家俄罗斯网络安全公司表示，其已于2026年初发现了此次攻击活动。

“幕后威胁组织正滥用合法的 MeshAgent 工具植入两个全新的后门程序。”卡巴斯基实验室的研究人员索拉布·夏尔马（Saurabh Sharma）和努辛·沙巴布（Noushin Shabab）在一篇分为两部分的分析报告中表示。

“这些恶意植入程序将其命令与控制（C2）流量隐藏在微软 SharePoint、GitHub 和 Ably 等云服务背后，使自身流量混入正常流量中，从而有效规避了基于网络的检测。”

这种模块化后门被命名为 GraphDoor 和 GitDoor，这两个名称源于其用于命令与控制（C2）的云平台选择。它们支持按需下载额外插件，并可直接在内存中执行 shellcode 以扩展自身功能。受感染系统与命令与控制（C2）服务器之间的通信流量，通过部署修改版的 Erfrp 客户端以及基于 Ably 消息服务的插件来实现代理转发。

攻击的起点可追溯至MeshCentral代理程序，这是一款合法的远程访问工具，用于远程桌面控制、命令行访问和文件管理。据悉，此次攻击目标为一家未具名的台湾机构。

该工具在主机上的具体安装方法目前仍不明确。不过，卡巴斯基补充称，种种迹象表明这是“复用了网络中已存在的先前感染”。

MeshCentral 代理被配置为连接到一个硬编码的命令与控制服务器（"wss://27.102.66[.]162:443/agent.ashx"），然后获取部署在终端上的三个载荷：

* 用于 DLL 侧加载的合法二进制文件（start.exe、pythonw.exe 和 zoomit.exe）
* 一个恶意加载器 DLL，用于解包并执行下一级恶意软件（jli.dll、SbieDll.dll、python39.dll、WINMM.dll 以及 libcef.dll）
* 一个包含核心有效载荷的加密文件

截至目前，已发现至少两种不同的 DLL 加载器，每种加载器都采用各自的方法，通过将加密的后门负载注入到当前进程的内存中来对其进行解码并启动。

加载程序（类型1）采用混合方案：先通过RC4流密码运行数据，然后应用异或掩码，而加载程序（类型2）则仅通过直接的异或运算简化了这一过程。

最终目标是部署类似 GitDoor 和 GraphDoor 这样的后门程序，这类程序采用控制流扁平化、嵌套辅助函数等多种加密和混淆技术，以增加分析难度，让攻击者更难追踪真实的执行流程。

GitDoor，顾名思义，利用 GitHub 作为命令与控制（C2）服务器。它依赖两个不同的代码仓库来接收命令有效载荷（/repos/LatonyCharnleyaW/Havo）并上传执行结果（/repos/LatonyCharnleyaW/Trix）。其中 Havo 仓库为公开仓库，而 Trix 仓库则为私有仓库。

GraphDoor 会打开一个命名管道，在系统的应用程序数据文件夹内创建一个名为“Intel\_Log”的目录，并收集系统信息以回传给攻击者。

为了与C2服务器建立通信，它通过端口443上的“login.microsoftonline.com”向恶意应用进行身份验证，并使用访问令牌与Microsoft Graph API通信，最终将数据暂存到SharePoint驱动器中。

随后该恶意软件从服务器获取三个插件模块，并并行启动这些模块以执行截图捕获、进程列表查看和键盘记录功能。它还会重新与SharePoint网站建立连接，以获取要在目标计算机上执行的指令。

此次活动背后的威胁行为者身份尚不明确，但卡巴斯基表示，其与 Sophos 以 Bronze Sandcastle为代号追踪的活动存在一定程度关联。研究人员还观察到，该活动的战术手段与FamousSparrow和CopperTurtle（又称 BlackTech）此前发起的活动存在相似之处。

“在多台受害设备上，这些组织与 GitDoor 后门使用相同的暂存目录，其恶意程序均在 GitDoor 部署后的一天窗口期内被植入。”该公司总结道：“尽管这无法证明二者存在直接关联，但表明一个群体可能正在开发和/或使用 GitDoor 与 GraphDoor 后门。”

通过使用基于云的存储和消息服务，这些攻击者混入正常流量之中（因为对Microsoft Graph、GitHub和Ably的云API调用与合法的企业使用毫无区别，从而规避了许多基于网络的检测），并实现了动态载荷交付——按需插件和外壳代码从云存储库中获取，无需修改主机文件即可实现快速更新和功能扩展。

技术报告：

https://securelist.com/operation-shadowcloud-graphdoor/122005/

新闻链接：

https://thehackernews.com/2026/11/new-gitdoor-and-graphdoor-backdoors.html

**![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg)**

扫码关注

爱拍照的老李

**讲述普通人能听懂的安全故事**

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/AnRWZJZfVaF2RjjiaFU5rh9gjoyybDu9EvVnCYlqGSXDTZyuDbPbic33rGMe0dfB3HAicVkh6kdgo7T3OAOGwOtYw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过