---
title: 【安全圈】UNC6692 通过微软 Teams 冒充 IT 服务台部署 SNOW 恶意软件
url: https://mp.weixin.qq.com/s/XrUqanB8fYfxWX_CoGZsjQ
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:32:29.809407
---

# 【安全圈】UNC6692 通过微软 Teams 冒充 IT 服务台部署 SNOW 恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGpgrqOh5LLfdNJUscFab0QgCqka1tJP2zW8hclAia9OEib3uph2yqL0gyQBILsXc7hB553zuOr1RBVfk6fyUq4LEaahml0Zmia20/0?wx_fmt=jpeg)

# 【安全圈】UNC6692 通过微软 Teams 冒充 IT 服务台部署 SNOW 恶意软件

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

一个此前未被记录的威胁活动集群 UNC6692，被发现通过微软 Teams 利用社会工程策略，在受入侵主机上部署一套定制的恶意软件。

谷歌旗下的Mandiant在今日发布的一份报告中指出：“与近年来的许多其他入侵事件一样，UNC6692 严重依赖冒充 IT 服务台员工，诱使受害者接受来自组织外部账户的微软 Teams 聊天邀请。”

UNC6692 与一场大规模的电子邮件活动有关，该活动旨在用大量垃圾邮件淹没目标的收件箱，制造一种紧迫感。随后，威胁行为者通过微软 Teams 联系目标，声称自己来自 IT 支持团队，可为电子邮件轰炸问题提供帮助。

值得注意的是，用垃圾邮件轰炸受害者收件箱，随后通过微软 Teams 冒充服务台，这种策略长期以来一直被前 Black Basta 组织成员采用。尽管该组织在去年年初停止了勒索软件业务，但这一策略并未有放缓的迹象。

在上周发布的一份报告中，ReliaQuest 透露，这种方法正被用于针对企业高管和高级员工，以获取企业网络的初始访问权限，从而进行潜在的数据盗窃、横向移动、部署勒索软件和实施勒索。在某些情况下，聊天邀请间隔仅 29 秒。

对话的目的是诱骗受害者安装 Quick Assist 或 Supremo Remote Desktop 等合法的远程监控和管理（RMM）工具，以实现直接访问，然后利用这些工具投放更多有效载荷。

ReliaQuest 的研究人员约翰・迪尔根（John Dilgen）和亚历克萨・费米内拉（Alexa Feminella）表示：“在 2026 年 3 月 1 日至 4 月 1 日期间，77% 的观测事件针对高级员工，高于 2026 年前两个月的 59%。这一活动表明，一个威胁组织最有效的策略可能在该组织消失后仍长期存在。”

另一方面，Mandiant 详细描述的攻击链与上述方法有所不同。受害者被指示点击通过 Teams 聊天分享的网络钓鱼链接，以安装本地补丁来解决垃圾邮件问题。点击链接后，会从威胁行为者控制的亚马逊云服务（AWS）S3 存储桶下载一个 AutoHotkey 脚本。网络钓鱼页面名为 “邮箱修复与同步工具 v2.1.5”。

该脚本旨在进行初步侦察，然后通过 “--load - extension” 命令行开关，以无头模式启动，在 Edge 浏览器上安装 SNOWBELT，这是一个恶意的基于 Chromium 的浏览器扩展。

Mandiant 的研究人员 JP・格拉布（JP Glab）、图费尔・艾哈迈德（Tufail Ahmed）、乔希・凯利（Josh Kelley）和穆罕默德・乌迈尔（Muhammad Umair）表示：“攻击者使用了一个看门狗脚本，旨在确保有效载荷仅交付给目标，同时避开自动化安全沙箱。该脚本还会检查受害者的浏览器。如果用户未使用微软 Edge，页面会显示一个持续的覆盖警告。通过 SNOWBELT 扩展，UNC6692 下载了包括 SNOWGLAZE、SNOWBASIN、AutoHotkey 脚本，以及一个包含便携式 Python 可执行文件和所需库的 ZIP 存档在内的其他文件。”

网络钓鱼页面还设计了一个配置管理面板，上面有一个醒目的 “健康检查” 按钮。点击该按钮会提示用户输入邮箱凭据，表面上是为了进行身份验证，但实际上是用于收集并将数据渗出到另一个亚马逊 S3 存储桶。

SNOW 恶意软件生态系统是一个模块化工具包，协同工作以实现攻击者的目标。SNOWBELT 是一个基于 JavaScript 的后门程序，接收命令并将其转发给 SNOWBASIN 执行；SNOWGLAZE 是一个基于 Python 的隧道工具，在受害者内部网络和攻击者的命令与控制（C2）服务器之间创建一个安全的、经过身份验证的 WebSocket 隧道。

第三个组件是 SNOWBASIN，它作为一个持久化后门程序，在端口 8000、8001 或 8002 上作为本地 HTTP 服务器运行。

UNC6692 在获得初始访问权限后执行的一些其他利用后操作如下：

* 使用 Python 脚本扫描本地网络上的端口 135、445 和 3389，以进行横向移动，通过 SNOWGLAZE 隧道工具建立到受害者系统的 PsExec 会话，并通过 SNOWGLAZE 隧道从受害者系统发起一个到备份服务器的远程桌面协议（RDP）会话。
* 利用本地管理员账户，通过 Windows 任务管理器提取系统的本地安全授权子系统服务（LSASS）进程内存，以提升权限。
* 使用哈希传递（Pass - The - Hash）技术，利用权限提升用户的密码哈希值横向移动到网络的域控制器，下载并运行 FTK Imager 捕获敏感数据（如活动目录数据库文件），并将其写入 “\Downloads” 文件夹，然后使用 LimeWire 文件上传工具渗出数据。

这家科技巨头表示：“UNC6692 活动展示了策略上的有趣演变，特别是社会工程、定制恶意软件和恶意浏览器扩展的使用，利用了受害者对多个不同企业软件供应商的固有信任。”

“这一策略的关键要素是系统地滥用合法云服务进行有效载荷交付、渗出以及建立命令与控制（C2）基础设施。通过在可信云平台上托管恶意组件，攻击者通常可以绕过传统的网络信誉过滤器，并混入大量合法云流量中。”

与此同时，Cato Networks）详细描述了一场基于语音网络钓鱼的活动，该活动在微软 Teams 上采用类似的冒充服务台策略，引导受害者通过从外部服务器获取的混淆 PowerShell 脚本，执行一个名为 PhantomBackdoor 的基于 WebSocket 的木马程序。

这家网络安全公司表示：“这一事件表明，通过微软 Teams 会议进行的服务台冒充如何能够取代传统网络钓鱼，并导致相同的结果：分阶段执行 PowerShell 脚本，随后植入 WebSocket 后门。防御者应将协作工具视为首要攻击面，实施服务台验证工作流程，收紧外部 Teams 和屏幕共享控制，并强化 PowerShell 安全设置。”

***END***

阅读推荐

[【安全圈】《王者荣耀》惊现逆天bug](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075971&idx=1&sn=87382d2f57b8f0b6d5e7f3203b830e4d&scene=21#wechat_redirect)

[【安全圈】理想汽车严正声明：系统遭黑客破解、配合走私均为不实信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075971&idx=2&sn=ef4ca71b65ec892a68ab6e5aeb1ab6df&scene=21#wechat_redirect)

[【安全圈】Claude Mythos 发现 271 个火狐浏览器漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075971&idx=3&sn=d88245ccf278317f520a1fdb52cbc91b&scene=21#wechat_redirect)

[【安全圈】未受保护的 Perforce 服务器暴露主要组织的敏感数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075943&idx=1&sn=473119abec6a4c6ed316801316b3723b&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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