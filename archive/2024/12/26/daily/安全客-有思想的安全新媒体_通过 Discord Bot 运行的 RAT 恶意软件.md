---
title: 通过 Discord Bot 运行的 RAT 恶意软件
url: https://www.anquanke.com/post/id/302997
source: 安全客-有思想的安全新媒体
date: 2024-12-26
fetch_date: 2025-10-06T19:36:09.834836
---

# 通过 Discord Bot 运行的 RAT 恶意软件

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 通过 Discord Bot 运行的 RAT 恶意软件

阅读量**138622**

|评论**1**

发布时间 : 2024-12-25 11:14:05

**x**

##### 译文声明

本文是翻译文章，文章来源：CN-SEC

原文地址：<https://cn-sec.com/archives/3547854.html>

译文仅供参考，具体内容表达以及含义原文为准。

![通过 Discord Bot 运行的 RAT 恶意软件]()

Discord 是一个社交平台，用户可以创建服务器来组建社区并进行实时交流，支持语音、视频和文本聊天。虽然它最初在游戏玩家中很受欢迎，但现在已扩展为一个兴趣各异的群体聚集在一起交流的空间。

Discord Bot 是一个在用户创建的服务器上自动执行特定任务的程序，提供各种功能，例如服务器管理、自动消息响应、游戏辅助、音乐播放和通知传递，使服务器操作更加简单。这些机器人主要使用 Python 和 JavaScript 等语言实现，并通过 Discord API 与服务器交互。

本文分析了一个使用 Discord Bot 实施 RAT 恶意软件的案例（PySilon）。此 RAT 恶意软件的完整源代码已在 GitHub 上公开，其网站和 Telegram 服务器等平台上都有社区。

![通过 Discord Bot 运行的 RAT 恶意软件]( "通过 Discord Bot 运行的 RAT 恶意软件")

图 1. RAT 恶意软件构建程序

Builder 支持自定义，允许用户指定开发 Discord Bot 所需的服务器 ID 和机器人令牌等信息，以及在系统上安装的注册表路径和名称。之后，将自定义信息输入到预先实现的 Python 代码中，并使用 PyInstaller 将其转换为可执行文件 (.exe)。

![通过 Discord Bot 运行的 RAT 恶意软件]( "通过 Discord Bot 运行的 RAT 恶意软件")

图 2. 构建定制化 RAT 恶意软件的过程

当以此方式创建的可执行文件在用户电脑上运行后，[威胁行为者](https://cn-sec.com/archives/tag/%E5%A8%81%E8%83%81%E8%A1%8C%E4%B8%BA%E8%80%85)在服务器上会创建一个新通道。IP 地址和其他系统信息最初通过聊天发送给[威胁行为者](https://cn-sec.com/archives/tag/%E5%A8%81%E8%83%81%E8%A1%8C%E4%B8%BA%E8%80%85)，如下图所示。

为每台被机器人感染的 PC 创建一个新通道，允许威胁行为者单独控制每台被感染的 PC。

![通过 Discord Bot 运行的 RAT 恶意软件]( "通过 Discord Bot 运行的 RAT 恶意软件")

图 3. 最初安装的机器人向威胁行为者发送的系统信息

![通过 Discord Bot 运行的 RAT 恶意软件]( "通过 Discord Bot 运行的 RAT 恶意软件")

图 4. 保持持久性

当构建的 RAT 恶意软件在系统上执行时，它会自我复制并在用户文件夹中创建以保持持久性（见图 4），并使用注册表将自身添加到 RUN 键中。这样，恶意软件就会继续执行，并驻留在每次 PC 启动时系统中。威胁行为者还可以自定义和创建用于自我复制的文件夹的名称。

此外，还有反虚拟机逻辑，该逻辑使用虚拟机中存在的文件或进程的名称来实现其功能。该恶意软件被设置为识别虚拟环境，并且在执行其功能之前不会在其中运行。

![通过 Discord Bot 运行的 RAT 恶意软件]( "通过 Discord Bot 运行的 RAT 恶意软件")

图 5. 可用命令

随后，威胁行为者可以将图5列出的命令输入到创建的频道的聊天中，以执行其他恶意行为。

以下是从威胁行为者的角度来看恶意软件的主要行为。

* 收集信息

![通过 Discord Bot 运行的 RAT 恶意软件]( "通过 Discord Bot 运行的 RAT 恶意软件")

图 6. 收集信息

Grab命令可用于从安装了RAT恶意软件的系统中收集信息。

它从安装的浏览器路径收集用户的个人信息，包括支付信息，以及浏览历史记录和 cookie 信息，并提取各种密码发送给威胁行为者。

可收集信息：Discord 代币、Nitro、MFA、电子邮件、电话号码、密码、cookie 信息、网页浏览历史记录等。

* 屏幕录制和录音

![通过 Discord Bot 运行的 RAT 恶意软件]( "通过 Discord Bot 运行的 RAT 恶意软件")

图 7. 发送给威胁行为者的屏幕和录音文件

它支持使用 Python 模块（例如 pyautogui、numpy、imageio 和 sounddevice）在受感染的 PC 中录制屏幕和音频。

* 键盘记录

![通过 Discord Bot 运行的 RAT 恶意软件]( "通过 Discord Bot 运行的 RAT 恶意软件")

图 8. 键盘记录

当用户按下“Enter”键时，它会将输入内容传输到威胁行为者的服务器。

* 文件夹加密

![通过 Discord Bot 运行的 RAT 恶意软件]( "通过 Discord Bot 运行的 RAT 恶意软件")

图 9. 加密/解密命令

![通过 Discord Bot 运行的 RAT 恶意软件]( "通过 Discord Bot 运行的 RAT 恶意软件")

图 10. 在用户文件夹中创建的密钥文件

它可以对受感染PC上的文件夹内的文件进行加密。经发现，该病毒使用了Fernet算法，解密所需的密钥文件存储在用户文件夹中。

加密文件的扩展名为 .pysilon，并且没有创建赎金记录。

除了上述功能外，它还可以操纵hosts文件，创建和管理网站黑名单/白名单，上传/下载文件，执行cmd命令，启动/终止进程，甚至使用Windows原生功能触发蓝屏死机（BSOD）。

使用 Discord 实现恶意 RAT 功能的开源项目（如 PySilon）正在不断涌现。由于源代码是公开可用的，威胁行为者可以轻松地将其合并到他们的机器人中并将其伪装成有用的工具。此外，由于数据是使用为正常机器人功能实施的官方 Discord 服务器传输的，因此用户很难意识到已安装恶意软件。因此，在安装来自不受信任来源的机器人或程序时务必小心谨慎。

本文翻译自CN-SEC [原文链接](https://cn-sec.com/archives/3547854.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/302997](/post/id/302997)

安全KER - 有思想的安全新媒体

本文转载自: [CN-SEC](https://cn-sec.com/archives/3547854.html)

如若转载,请注明出处： <https://cn-sec.com/archives/3547854.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**7赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=173683)

[安全客](/member.html?memberId=173683)

这个人太懒了，签名都懒得写一个

* 文章
* **553**

* 粉丝
* **2**

### TA的文章

* ##### [年度盘点：AI+安全双重赋能，360解锁企业浏览器新动力](/post/id/303791)

  2025-01-24 10:00:53
* ##### [IntelBroker 的数字足迹： OSINT 分析揭露网络犯罪分子的行动](/post/id/303788)

  2025-01-24 09:55:58
* ##### [7-Zip 修复了可绕过 Windows MoTW 安全警告的错误，立即修补](/post/id/303776)

  2025-01-24 09:49:56
* ##### [Microsoft 在 Edge Stable 中预览 Game Assist 游戏内浏览器](/post/id/303773)

  2025-01-24 09:43:16
* ##### [ModiLoader 恶意软件利用 CAB 标头批处理文件逃避检测](/post/id/303770)

  2025-01-24 09:36:10

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)