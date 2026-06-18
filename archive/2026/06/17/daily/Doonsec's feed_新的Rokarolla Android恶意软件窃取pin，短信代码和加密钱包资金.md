---
title: 新的Rokarolla Android恶意软件窃取pin，短信代码和加密钱包资金
url: https://mp.weixin.qq.com/s/GR-OeATK-wOUYZu1XMX3Hw
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:47:29.461539
---

# 新的Rokarolla Android恶意软件窃取pin，短信代码和加密钱包资金

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADs9l1I87B4FAtLEgibJ0EH9NdabgGr0oDcT2usd4R1WXxia5LJaqeZ88OT4vTECTPicApUrySM3XYL5picdYibFTOicRchiadYg2UPiabp0/0?wx_fmt=jpeg)

# 新的Rokarolla Android恶意软件窃取pin，短信代码和加密钱包资金

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oPZcPicUADs9qQccicHfyzwPNeibjvpVljic50ssjK68sOp4Fyg57oHISwgxpvkkxxm9gWJibjTsHaDcq2eCNT5CyyufU2Rbch0cAbBfzXubeHSo/640?wx_fmt=jpeg&from=appmsg)

Zimperium实验室的安全研究人员记录了一种新的安卓银行木马——Rokarolla，它针对217个银行和加密货币应用程序，并打包了137个远程命令。

总之，它们让运营商几乎完全控制了受感染的手机：它可以解除锁屏pin，读取和发送短信，重写剪贴板以重定向加密支付，并关闭谷歌Play Protect。

Rokarolla以其命令和控制服务器命名，通过恶意网站冒充TikTok和Chrome等知名应用程序传播。

受害者安装的第一件事就是假装是b谷歌Play Protect的滴管。它使用这种伪装来安装有效负载并获取可访问性访问。一旦恶意软件运行，其中一个命令会关闭Play Protect。

盗窃贯穿了覆盖层。Rokarolla从它的服务器上提取一个目标列表，对于每个被标记为活动的应用程序，它下载一个假的HTML登录页面，并将其存储在本地数据库中。当受害者打开真正的银行或钱包应用程序时，恶意软件会将假页面放在顶部，并捕获输入其中的所有内容，包括信用卡详细信息。

报告显示，其中一个虚假页面模仿了银行应用“imagin”。一个单独的覆盖层模仿Android锁定屏幕来捕获PIN，图案或密码，这让操作员即使在锁定状态下也可以控制手机。

它读取设备上的每条短信，并可以自己发送信息，这足以获取银行用于批准登录和交易的一次性短信代码。通过将自己设置为手机短信和通话的默认应用程序，它还可以阻止来电，因此银行的警告电话永远不会接通。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs8u3BCf2gfLYLZia5rUIOGYtUe6Rn5cTbNfNCDRxsWYYuyg6m4mHMqicfY2E3qfk4AUrhXpbQPQKBtkJM5C8pgyfBe5eGPK83iaGA/640?wx_fmt=jpeg&from=appmsg)

键盘记录器和屏幕记录器记录用户输入和看到的内容，特洛伊木马刮擦联系人并读取通知。剪贴板被悄无声息地重写，交换攻击者的钱包地址，因此复制的加密支付进入了错误的账户。

对于监视，Rokarolla跳过了通常的MediaProjection屏幕投射，它抛出一个可见的记录提示，而是通过可访问性获取屏幕截图，将它们压缩为PNG，并将它们一次发送一帧。这种快照方法比Klopatra等家庭使用的实时隐藏VNC更简单、更安静。

恶意软件携带多个备用C2域，并且可以在运行中获得新的C2域，因此拉出单个服务器的作用很小。它的137个指令数量超过了Zimperium在HOOK木马中的107个指令数量，并且其策略与2026年Android银行的一波相同：假应用drop，易访问性滥用和HTML覆盖。

这里没有补丁可以应用。这是恶意软件，而不是产品缺陷，所以这些防御措施是针对Android银行的标准措施。只从谷歌Play安装应用程序，让Play Protect打开，并将任何意外的可访问性请求视为危险信号，因为一个权限驱动整个攻击链。

Zimperium表示，它自己的产品可以检测到这个家族，而泄露的指标在它的GitHub存储库中。

Zimperium没有将Rokarolla与一个命名的群体联系起来。构建所显示的是意图：一个银行家组合在一起，以击败用户被告知要依赖的确切保护，从Play Protect到锁定屏幕。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

HackSee安全生活

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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