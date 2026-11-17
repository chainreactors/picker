---
title: ArcticRAT安卓恶意软件利用隐藏VNC控制手机，受害者仅可见黑屏
url: https://mp.weixin.qq.com/s/VxGsvcEVy1GWfzoQ0ZsXMw
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:51:45.102465
---

# ArcticRAT安卓恶意软件利用隐藏VNC控制手机，受害者仅可见黑屏

# ArcticRAT安卓恶意软件利用隐藏VNC控制手机，受害者仅可见黑屏

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX1uqsDicF8Ya5rZMqewPVNgqEbTm7MqbPUFY5JI5WgqBRxickuf9FfBWibbkL7Qbe3GGKrphP6notcwWEIFTia2P2AsKwDSSot7Pdk/640?wx_fmt=gif)

![ArcticRAT安卓木马](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3kuPe0zwuCwV4tqWZI1aBiblM7rKytrFy1IGEdHchOua6PH5QIW6AAaMfwt7jFyxMIr1NKLKWXfLgeC8xWnYJM9M3S4toOP3Cg/640?wx_fmt=png)

一款名为ArcticRAT的新型安卓远程访问木马可完全控制用户手机，机主仅能看到黑屏界面。设备表面看似锁屏或关机，攻击者却已在后台打开银行类应用、自动批准各类敏感权限申请并窃取数据。

该恶意软件最初是一款小型间谍工具，仅针对11款加密货币应用的用户。如今它已演变为功能完整的远程访问木马，支持129条控制指令，最新版本还利用隐藏VNC（一种远程屏幕控制技术）和人工智能提升窃密效率。

ArcticRAT的名称来源于早期版本的包名net.iceflow.arcticlink和net.frostlink.iceforge，由Zimperium旗下zLabs团队的研究人员发现并持续追踪。研究人员共找到78个独特样本、42个投放器样本、36个恶意载荷，以及21个命令与控制（C2）服务器IP地址。相关攻击活动持续迭代，6.3至6.5.2版本的样本显示，该恶意软件仍在稳定、活跃地开发中。

Part01

仿冒渠道诱导用户安装

ArcticRAT的感染链路始于恶意广告、短信或第三方论坛引流，受害者点击后会进入仿冒网站。多数投放器托管在仿冒Google Play的页面上，部分载荷直接来自亚马逊云科技存储服务，伪装成亚马逊客户端、TikTok、文件管理器、加密货币工具等各类应用。

投放器的设计十分狡猾。它先申请VPN权限，利用该权限切断手机网络流量，让Google Play Protect无法检测到后续真实载荷的安装过程。随后它会显示伪造的安装进度界面，解密隐藏的载荷、完成安装后再关闭VPN连接。这种分阶段加载的手法，与此前报道的RATHat滥用Gemini AI攻击活动中利用无障碍服务的套路如出一辙。

一旦受害者授予恶意软件无障碍权限，ArcticRAT就会连接9999端口的C2服务器，上传包含电量、屏幕状态、Wi-Fi信息在内的设备配置数据。它还会抓取用户当前的壁纸，大概率是为了验证自身运行在真实设备而非沙箱环境中，随后服务器会根据设备情况选择启用对应的攻击模块。

![仿冒Google Play的钓鱼网站（来源：Zimperium）](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2I4aPbC8UVgFZOiczQqlib4raAlMFHspkvLIF7GvSf6eA9beSXXicqCqzicGXZtDAoEmkkibpVtdwRZLrRez5jmgI2WuIqHTjxbXJU/640?wx_fmt=png)

隐藏VNC模块运行在8888端口，会在设备内存中构建虚拟显示器，将屏幕画面以JPEG格式实时回传，攻击者可同步查看并操控受害者手机。

黑屏欺骗是ArcticRAT的核心隐蔽手段。攻击者操作银行应用、批准权限申请时，ArcticRAT会在屏幕顶层绘制无法关闭的黑色遮罩，同时将屏幕亮度调至0，让受害者误以为手机处于锁屏状态。类似手法也曾出现在安卓银行木马StreamRAT的攻击活动中，说明这种静默控制方式已成为网络犯罪分子的主流选择。

Part02

内置假勒索界面恐吓用户

ArcticRAT还内置了虚假勒索软件界面，会展示无限循环的加密进度条，谎称正在加密用户文件，实际上不会对任何文件进行加密操作，唯一目的是恐吓受害者支付赎金。

更值得警惕的是该恶意软件引入了AI能力。其内置的xAI\_API指令可向手机下发API密钥与提示词，其中一条提示词会扫描设备已安装应用，识别银行、加密货币、交易类的高价值目标应用。

![恶意软件展示的勒索软件遮罩界面（来源：Zimperium）](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0oP3NLtOFoCuBptC9HFbQBhPkohHKkrhib5ntMBYngKiaxyggdng2owdniaty7QhGk2nJOtAHBbvEokUKV38v3Fgos1laC88gSro/640?wx_fmt=png)

另一条提示词负责分析窃取的短信内容，过滤推广类垃圾信息，提取一次性验证码、余额变动、转账通知等敏感内容，甚至可以评估受害者的资产水平。

Zimperium观测到，该恶意软件调用xAI服务的grok-4.20-0309-non-reasoning模型，将返回结果存储在/storage/emulated/0/config/AI\_DATA/路径下。这类隐藏屏幕控制手法最早见于Windows平台的Shadow hVNC远程桌面控制工具，如今已被迁移到移动端攻击场景中。

ArcticRAT还会窃取用户的手机解锁密码。它通过Phsing指令启动伪造的锁屏界面，记录用户输入的PIN、解锁图案或密码，再调用shell命令locksettings verify验证窃取到的密码是否正确。新版本还会滥用安卓11及以上系统的无线调试功能，获取高权限ADB shell，自行开启无障碍权限、移除原有锁屏、设置新PIN将机主锁在系统外。用户的按键输入、触摸操作、截图都会先存储在/storage/emulated/0/config/路径下的隐藏文件夹中，再被外传到攻击者服务器。

此前针对搭载隐藏VNC功能的银行木马的报告已经指出，这类技术结合界面遮罩的攻击方式风险极高。普通用户应仅从官方Play Store安装应用，不要点击广告、短信中的不明链接，拒绝非预期的无障碍、VPN或屏幕共享权限申请。如果手机突然出现锁屏、黑屏或其他异常行为，应立即断网排查。银行与企业应监控敏感业务会话过程中的屏幕共享行为、遮罩窗口调用以及无障碍权限滥用情况。

Part03

相关失陷指标清单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1ZhPzagMVTeBhmNwE2tAq4Rg10Jq4qdeRCAFjupSw8ibcb2qF4LwDfufRVSMtXjPXMTY1tsKniazrLcq1VetB6nZ6pxfS2xOxrw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3OOfcCBtIVZ1W1nGsM9Vl84OMlLtZY0AvGrFDRE6rvjoMZoVOJCynxmvS98BjsMjI8PeZx4pCTWicT9iaIO1AKA1A9pcNuf2HN4/640?wx_fmt=png&from=appmsg)

注：文中涉及的IP地址与域名均已做去活化处理（例如替换为[.]格式），防止意外解析或直接跳转。仅可在MISP、VirusTotal或企业内部SIEM等受控威胁情报平台中恢复原始地址使用。

参考来源：

ArcticRAT Android Malware Uses Hidden VNC to Control Smartphones While Showing Victims a Black Screen

https://cybersecuritynews.com/arcticrat-android-malware/

### **推荐阅读** [![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX38ibvFWu8tnORNBELsice6a0HbKoyGH0LDKjzxAxpAr4ib5Qn3oKb4huesy0pnDicAXIdDmoumzuj6nAPZsCTU1QBX0hQYzdJj5uo/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651351016&idx=3&sn=d224081e5f21f76580f08cd93c037d34&scene=21#wechat_redirect) **电报讨论** ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2cCEVtIlLczLq1S4rms9uYa8x5Xedy0Il667ib20FMyHawNapLuHBl3peZxWoStYkAJdBcMicfmy9icChQA8uKfBib5EPaMicU5ykw/640?wx_fmt=png&from=appmsg) ![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png) ![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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